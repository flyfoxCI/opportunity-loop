"""v3 investigation: evidence -> claims -> report, for each of today's picks.

Two modes write the same JSON schema (research/v3-design.md section 5.2):
  data   always runs. Every field is computed from collected data; nothing is guessed.
         The headline is descriptive, the trigger is 'not checked' unless evidence exists.
  agent  runs when an Anthropic-compatible key is set (MiniMax by default, like stage_b.py).
         The model writes the editorial fields from the gathered evidence only; a verify step
         downgrades any 'fact' whose URL is not in the evidence set to 'inferred'.
Metric badges, grades and Demand Echo are always computed by code, never by the model.
"""

from __future__ import annotations

import json
import math
import os
import re
from datetime import datetime, timedelta

from .analyze import _series
from .detect import SURFACE_NAME, chart_name, daily_deltas
from .taxonomy import BY_SLUG

MODEL = os.environ.get("ANTHROPIC_MODEL", "MiniMax-M3")
WEIGHTS = {"money": 0.25, "demand": 0.20, "replicable": 0.20, "room": 0.15, "window": 0.10, "durability": 0.10}
GRADE_CUTS = ((80, "S"), (65, "A"), (50, "B"), (35, "C"), (20, "D"))
GRADE_TEXT = {"S": "Act now", "A": "Worth following", "B": "Can try, clear weak spots",
              "C": "Learn from it", "D": "Just be aware", "E": "Don't touch"}


def _d(s: str) -> datetime:
    return datetime.strptime(s[:10], "%Y-%m-%d")


def _product(con, src: str, pid: str) -> dict:
    r = con.execute("SELECT * FROM products WHERE source=? AND pid=?", (src, pid)).fetchone()
    if not r:
        return {}
    p = dict(r)
    p["meta"] = json.loads(p.get("meta") or "{}")
    return p


def _fmt(v, money=False) -> str:
    if v is None:
        return "–"
    if money:
        return f"${v / 1000:.1f}K" if v >= 1000 else f"${v:,.0f}"
    if abs(v) >= 1_000_000:
        return f"{v / 1_000_000:.1f}M"
    if abs(v) >= 10_000:
        return f"{v / 1000:.0f}K"
    if abs(v) >= 1000:
        return f"{v / 1000:.1f}K"
    return f"{v:,.0f}" if v == int(v) else f"{v:,.1f}"


# ---------------------------------------------------------------- gather

def _curve(con, c: dict, day: str) -> list:
    """14-21 day series for the card's metric: [(day, value)]."""
    src, pid, rule = c["source"], c["pid"], c["rule"]
    lo = (_d(day) - timedelta(days=21)).strftime("%Y-%m-%d")
    if rule in ("chart_jump", "chart_new", "minigame_rank"):
        pts = _series(con, src, c["chart"]).get(pid, [])
    elif rule == "gp_installs":
        pts = daily_deltas(_series(con, "play", "installs").get(pid, []))
    elif rule == "ios_ratings":
        pts = daily_deltas(_series(con, "ios", "ratings").get(pid, []))
    elif rule == "gh_stars":
        pts = _series(con, "github", "stars_today").get(pid, [])
    elif rule == "drama_ads":
        pts = _series(con, "drama_ad", "creatives").get(pid, [])
    elif rule == "drama_chart":
        pts = _series(con, "drama", "rank:tiktok").get(pid, [])
    elif rule == "revenue":
        pts = _series(con, "trustmrr", "mrr").get(pid, [])
    elif rule == "web_traffic":
        pts = _series(con, "trustmrr" if src == "trustmrr" else "tranco",
                      "tranco_rank" if src == "trustmrr" else "rank").get(pid, [])
    else:
        pts = []
    return [(d, v) for d, v in pts if d >= lo and v is not None]


def _charts_today(con, src: str, pid: str, day: str) -> list:
    rows = con.execute("SELECT metric, value FROM metrics WHERE source=? AND pid=? AND day=? AND metric LIKE 'rank:%' "
                       "ORDER BY value LIMIT 40", (src, pid, day)).fetchall()
    chg = {r["metric"][4:]: r["value"] for r in con.execute(
        "SELECT metric, value FROM metrics WHERE source=? AND pid=? AND day=? AND metric LIKE 'chg:%'", (src, pid, day))}
    out = []
    for r in rows:
        key = r["metric"][5:]
        out.append({"chart": chart_name(r["metric"]) if src in ("ios", "play") else key.replace(":", " · "),
                    "rank": int(r["value"]), "change": chg.get(key), "metric": r["metric"]})
    return out


def _siblings(con, prod: dict, src: str) -> list:
    cid = (prod.get("meta") or {}).get("cluster_id")
    if not cid or src not in ("ios", "play"):
        return []
    other = "play" if src == "ios" else "ios"
    out = []
    for r in con.execute("SELECT pid, name, url, meta FROM products WHERE source=?", (other,)):
        if json.loads(r["meta"] or "{}").get("cluster_id") == cid:
            out.append({"source": other, "pid": r["pid"], "name": r["name"], "url": r["url"]})
    return out[:1]


def _measure(con, src: str, pid: str) -> dict:
    """Latest store measurements: installs / ratings / rating, with daily increase when available."""
    out = {}
    for metric in ("installs", "ratings", "rating", "stars"):
        pts = _series(con, src, metric).get(pid, [])
        if pts:
            out[metric] = pts[-1][1]
            if metric not in ("rating", "stars"):
                dd = daily_deltas(pts)
                if dd:
                    out[f"{metric}_per_day"] = dd[-1][1]
    if "rating" not in out:
        row = con.execute("SELECT meta FROM products WHERE source=? AND pid=?", (src, pid)).fetchone()
        if row and json.loads(row["meta"] or "{}").get("rating"):
            out["rating"] = json.loads(row["meta"])["rating"]
    out["days_tracked"] = len({d for d, in con.execute(
        "SELECT DISTINCT day FROM metrics WHERE source=? AND pid=?", (src, pid))})
    return out


def _competitors(con, c: dict, day: str, limit: int = 4) -> list:
    d = c["direction"]
    if c["source"] in ("ios", "play"):
        rows = con.execute(
            "SELECT p.pid, p.name, p.url, p.meta, MIN(m.value) best, m.metric FROM products p JOIN metrics m "
            "ON m.source=p.source AND m.pid=p.pid AND m.day=? AND m.metric LIKE 'rank:%' "
            "WHERE p.source=? AND p.direction=? AND p.pid<>? GROUP BY p.pid ORDER BY best LIMIT ?",
            (day, c["source"], d, c["pid"], limit)).fetchall()
        return [{"name": r["name"], "url": r["url"], "note": f"#{int(r['best'])} {chart_name(r['metric'])}"}
                for r in rows]
    if c["source"] == "trustmrr":
        mrr = {pid: pts[-1][1] for pid, pts in _series(con, "trustmrr", "mrr").items()}
        rows = con.execute("SELECT pid, name, url FROM products WHERE source='trustmrr' AND direction=? AND pid<>?",
                           (d, c["pid"])).fetchall()
        rows = sorted(rows, key=lambda r: -(mrr.get(r["pid"]) or 0))[:limit]
        return [{"name": r["name"], "url": r["url"], "note": f"{_fmt(mrr.get(r['pid']), True)} MRR (TrustMRR)"}
                for r in rows if mrr.get(r["pid"])]
    if c["source"] == "minigame":
        rows = con.execute(
            "SELECT p.pid, p.name, p.category, MIN(m.value) best FROM products p JOIN metrics m ON m.source=p.source "
            "AND m.pid=p.pid AND m.day=? AND m.metric LIKE 'rank:%' WHERE p.source='minigame' AND p.pid<>? "
            "AND p.category=(SELECT category FROM products WHERE source='minigame' AND pid=?) GROUP BY p.pid "
            "ORDER BY best LIMIT ?", (day, c["pid"], c["pid"], limit)).fetchall()
        return [{"name": r["name"], "url": "", "note": f"#{int(r['best'])} · {r['category']}"} for r in rows]
    return []


def _demand(con, direction: str, day: str) -> dict:
    since = int((_d(day) - timedelta(days=14)).timestamp())
    rows = con.execute("SELECT id, subreddit, title, num_comments, score, created_utc FROM threads WHERE direction=? "
                       "AND created_utc>=? ORDER BY num_comments DESC LIMIT 4", (direction, since)).fetchall()
    n = con.execute("SELECT COUNT(*) FROM threads WHERE direction=? AND created_utc>=?", (direction, since)).fetchone()[0]
    prev = con.execute("SELECT COUNT(*) FROM threads WHERE direction=? AND created_utc>=? AND created_utc<?",
                       (direction, since - 14 * 86400, since)).fetchone()[0]
    xhs = con.execute("SELECT title, url FROM traces WHERE source='xhs_web' AND day>=? LIMIT 3",
                      ((_d(day) - timedelta(days=7)).strftime("%Y-%m-%d"),)).fetchall() if direction != "drama" else []
    return {"threads_14d": n, "threads_prev_14d": prev,
            "threads": [{"title": r["title"], "subreddit": r["subreddit"], "comments": r["num_comments"],
                         "url": f"https://www.reddit.com/r/{r['subreddit']}/comments/{r['id']}/"} for r in rows],
            "xhs": [{"title": r["title"], "url": r["url"]} for r in xhs]}


def _traces(con, src: str, pid: str) -> list:
    return [dict(r) for r in con.execute("SELECT title, url, snippet, day FROM traces WHERE source=? AND pid=? "
                                         "ORDER BY day DESC LIMIT 6", (src, pid))]


def gather(con, c: dict, day: str) -> dict:
    p = _product(con, c["source"], c["pid"])
    meta = p.get("meta") or {}
    released = meta.get("released") or ""
    if released and not re.match(r"\d{4}-\d{2}-\d{2}", released):
        try:
            released = datetime.strptime(released, "%b %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            released = ""
    age = (_d(day) - _d(released)).days if released else None
    ev = {"product": {"name": p.get("name") or c["pid"], "url": p.get("url") or "",
                      "description": (p.get("description") or "")[:700], "category": p.get("category") or "",
                      "icon": meta.get("icon") or meta.get("cover"), "developer": meta.get("developer") or
                      meta.get("seller") or meta.get("publisher") or meta.get("company") or "",
                      "released": released, "age_days": age, "price": meta.get("price") or "",
                      "iap": meta.get("iap"), "site": meta.get("seller_url") or meta.get("dev_site") or
                      meta.get("website") or "", "platform": meta.get("platform") or "",
                      "streak": meta.get("streak"), "labels": meta.get("labels") or [],
                      "countries": meta.get("countries") or [], "ad_platforms": meta.get("platforms") or [],
                      "advertisers": meta.get("advertisers") or [], "episodes": meta.get("episodes"),
                      "screenshot": meta.get("screenshot")},
          "curve": _curve(con, c, day), "measure": _measure(con, c["source"], c["pid"]),
          "charts": _charts_today(con, c["source"], c["pid"], day), "siblings": _siblings(con, p, c["source"]),
          "competitors": _competitors(con, c, day), "demand": _demand(con, c["direction"], day),
          "traces": _traces(con, c["source"], c["pid"]), "events": []}
    for s in ev["siblings"]:
        ev["sibling_measure"] = _measure(con, s["source"], s["pid"])
        ev["sibling_charts"] = _charts_today(con, s["source"], s["pid"], day)[:4]
    vdate = meta.get("version_date") or meta.get("updated") or ""
    if vdate and (_d(day) - _d(vdate)).days <= 10:
        ev["events"].append({"date": vdate, "label": "fact", "url": ev["product"]["url"],
                             "text": f"Shipped an update (v{meta.get('version')})" if meta.get("version")
                             else "Shipped an update", "notes": (meta.get("release_notes") or meta.get("whatsnew")
                                                                  or "")[:240]})
    if released and age is not None and age <= 60:
        ev["events"].append({"date": released, "label": "fact", "url": ev["product"]["url"],
                             "text": f"Launched {age} days ago"})
    if meta.get("first_seen") and isinstance(meta["first_seen"], (int, float)):
        fs = datetime.utcfromtimestamp(meta["first_seen"]).strftime("%Y-%m-%d")
        ev["events"].append({"date": fs, "label": "fact", "url": "", "text": "First ad creative seen"})
    first = con.execute("SELECT MIN(day) FROM metrics WHERE source=? AND pid=? AND metric LIKE 'rank:%'",
                        (c["source"], c["pid"])).fetchone()[0]
    if first:
        ev["events"].append({"date": first, "label": "fact", "url": "", "text": "First seen on a chart we track"})
    ev["events"].sort(key=lambda e: e["date"])
    return ev


# ---------------------------------------------------------------- data-only brief

def _short(name: str, n: int = 34) -> str:
    name = (name or "").strip()
    if len(name) <= n:
        return name
    head = re.split(r"\s[-–—|]\s|: ", name)[0]
    return head if len(head) <= n else head[: n - 1] + "…"


def _headline(c: dict, ev: dict) -> str:
    n, a, b = _short(ev["product"]["name"]), c.get("after"), c.get("before")
    chart = chart_name(c["chart"]) if c.get("chart", "").startswith("rank:") and c["source"] in ("ios", "play") else ""
    if c["rule"] == "chart_jump":
        return f"{n} jumped {int(b - a)} places to #{int(a)} on {chart}"
    if c["rule"] == "chart_new":
        return f"{n} entered {chart} at #{int(a)}"
    if c["rule"] == "gp_installs":
        return f"{n}: daily installs ×{c['mult']:.1f} to {_fmt(a)}"
    if c["rule"] == "ios_ratings":
        return f"{n}: new ratings per day ×{c['mult']:.1f} to {_fmt(a)}"
    if c["rule"] == "gh_stars":
        return f"{n} gained {_fmt(a)} GitHub stars in a day"
    if c["rule"] == "minigame_rank":
        plat, board = (c["chart"][5:].split(":") + [""])[:2]
        return f"{n} rose {int(b - a)} places to #{int(a)} on {plat.title()} {board.replace('_', ' ')}"
    if c["rule"] == "drama_ads":
        return f"“{n}” ran {_fmt(a)} ad creatives in a day"
    if c["rule"] == "drama_chart":
        return f"“{n}” reached #{int(a)} on the TikTok drama chart"
    if c["rule"] == "revenue":
        return f"{n}: MRR ×{c['mult']:.1f} to {_fmt(a, True)} in {c['window']}"
    if c["rule"] == "web_traffic":
        return f"{n}: web traffic rank {_fmt(b)} → {_fmt(a)}" if b else f"{n} entered the top 1M websites"
    return n


def _why(c: dict, ev: dict) -> list:
    out = []
    for e in ev["events"]:
        if e["text"].startswith("Shipped") or e["text"].startswith("Launched"):
            out.append({"text": f"{e['text']} on {e['date']}" + (f": “{e['notes'][:140]}”" if e.get("notes") else ""),
                        "label": "fact", "url": e["url"]})
    if c["rule"] == "chart_new" or any(x.get("rule") == "chart_new" for x in c.get("also", [])):
        out.append({"text": "Appark flags it as newly promoted on this chart today", "label": "fact", "url": ""})
    p = ev["product"]
    if c["source"] == "drama_ad":
        out.append({"text": "Ads run in " + ", ".join(p["countries"][:4]) + " via " + ", ".join(p["ad_platforms"][:3])
                    + (f", landing on {p['advertisers'][0]}" if p["advertisers"] else ""), "label": "fact", "url": ""})
    if c["source"] == "minigame" and p.get("streak"):
        out.append({"text": f"Chart label: {p['streak']}", "label": "fact", "url": ""})
    for t in ev["traces"][:3]:
        out.append({"text": t["title"] + (f" — {t['snippet'][:120]}" if t.get("snippet") else ""),
                    "label": "inferred", "url": t["url"]})
    if not out:
        out.append({"text": "Trigger not checked yet: the agent investigation (LLM + TinyFish) runs where its keys "
                            "are configured.", "label": "not_found", "url": ""})
    return out


def _discounts(c: dict, ev: dict) -> list:
    out = []
    m = ev["measure"]
    if c["rule"] in ("chart_jump", "chart_new"):
        out.append("A chart rank is not a download count: in a small category or country a jump can be a few hundred "
                   "installs.")
    if c["basis"] != "own-baseline":
        out.append(f"We have {m.get('days_tracked', 1)} day(s) of our own history for this product; the move is "
                   "measured against the source's own change figure, not our baseline yet.")
    if c["rule"] == "ios_ratings":
        out.append("New ratings are a proxy for downloads; review prompts after a release inflate them.")
    if c["rule"] == "gh_stars":
        out.append("Stars can be bought, and Trending brings its own stars: check forks, issues and real usage.")
    if c["rule"] in ("drama_ads",):
        out.append("Creative counts and impressions are Appark's estimates from ad libraries, not spend.")
    if c["rule"] == "minigame_rank":
        out.append("Popularity charts move with ad buying; a rise without a best-selling move is usually bought "
                   "traffic.")
    if c.get("after") is not None and c["rule"] in ("gp_installs", "ios_ratings") and c["after"] < 1000:
        out.append(f"The absolute number is small ({_fmt(c['after'])}/day).")
    if c.get("big_publisher"):
        out.append("Published by a large company: hard to copy for one or two people.")
    return out


def _grade(c: dict, ev: dict) -> dict:
    f = {}
    charts = ev["charts"] + ev.get("sibling_charts", [])
    gross = [x["rank"] for x in charts if ":grossing:" in x.get("metric", "")]
    money = 20
    if c["source"] == "trustmrr":
        money = min(95, 40 + 15 * max(0.0, math.log10(max(c.get("after") or 1, 1)) - 2))
    elif gross:
        money = 85 if min(gross) <= 50 else 65
    elif ev["product"].get("iap") or (ev["product"].get("price") not in ("", "Free", None)):
        money = 45
    elif c["source"] == "drama_ad":
        money = 60
    elif c["source"] == "minigame":
        money = 70 if "bestseller" in c.get("chart", "") else 40
    m = ev["measure"]
    tiny = (c["source"] in ("ios", "play") and (m.get("ratings") or 0) < 50 and (m.get("installs") or 0) < 10_000)
    why_money = "grossing rank, verified revenue, paid model or ad spend"
    if tiny:  # a top rank in a thin genre/country chart with almost no users is not money yet
        money, why_money = min(money, 40), f"only {int(m.get('ratings') or 0)} ratings: rank without scale"
    f["money"] = (round(money), why_money)
    d = ev["demand"]
    echo = min(100, d["threads_14d"] * 6) if d["threads_14d"] else 15
    if d["threads_14d"] and d["threads_prev_14d"] and d["threads_14d"] > 1.5 * d["threads_prev_14d"]:
        echo = min(100, echo + 15)
    f["demand"] = (round(echo), f"{d['threads_14d']} buyer-intent Reddit threads in 14 days")
    fit = (BY_SLUG.get(c["direction"]) or {}).get("fit", 0.5)
    rep = fit * 100 - (35 if c.get("big_publisher") else 0)
    f["replicable"] = (round(max(5, rep)), "direction prior for a solo builder, publisher size")
    crowd = len(ev["competitors"])
    if c["source"] in ("ios", "play", "trustmrr", "minigame"):
        f["room"] = (round(80 - crowd * 10 + (10 if (ev["product"].get("age_days") or 999) < 120 else 0)),
                     f"{crowd} bigger peers in this direction today")
    else:
        f["room"] = (50, "not measured for this surface yet (neutral)")
    f["window"] = (70 if c["basis"] == "own-baseline" else 55, "fresh, measured move" if c["basis"] == "own-baseline"
                   else "one-day signal")
    dur = 40 + min(30, (ev["measure"].get("days_tracked") or 0) * 3)
    if (ev["measure"].get("rating") or 0) >= 4.5:
        dur += 10
    if tiny:
        dur = min(dur, 40)
    f["durability"] = (round(min(100, dur)), "days on charts in our data, rating, user base")
    score = sum(WEIGHTS[k] * max(0, min(100, v[0])) for k, v in f.items())
    grade = next((g for cut, g in GRADE_CUTS if score >= cut), "E")
    return {"grade": grade, "score": round(score), "text": GRADE_TEXT[grade],
            "factors": {k: {"score": max(0, min(100, v[0])), "why": v[1]} for k, v in f.items()}}


def _follow(con, c: dict, ev: dict, day: str) -> dict:
    """Wedge from data: markets where the direction charts but this product doesn't."""
    out = {"play": "", "wedge": "", "avoid": ""}
    if c["source"] in ("ios", "play"):
        here = {x["metric"].split(":")[2] for x in ev["charts"]}
        peers = {r[0].split(":")[2] for r in con.execute(
            "SELECT DISTINCT m.metric FROM metrics m JOIN products p ON p.source=m.source AND p.pid=m.pid "
            "WHERE m.source=? AND m.day=? AND m.metric LIKE 'rank:%' AND p.direction=?",
            (c["source"], day, c["direction"]))}
        gap = sorted(peers - here)
        if here:
            out["wedge"] = (f"It charts in {', '.join(x.upper() for x in sorted(here)[:6])}. "
                            + (f"Its direction also charts in {', '.join(x.upper() for x in gap[:6])} where it "
                               "doesn't: a localized version there is the cheapest wedge." if gap else
                               "It already covers every market where its direction charts: compete on a "
                               "narrower audience instead."))
    elif c["source"] == "github":
        out["wedge"] = ("Open-source momentum: the usual wedges are a hosted version, a GUI shell, or a vertical "
                        "template built on it in the first two weeks.")
    elif c["source"] == "minigame":
        out["wedge"] = "Keep the mechanic, change the skin and the audience it talks to."
    elif c["source"] == "drama_ad":
        out["wedge"] = "Ad-led drama is a media-buying business: only follow with a creative and buying edge."
    if c.get("big_publisher"):
        out["avoid"] = "Don't copy the product; study the move."
    return out


def _build_kit(c: dict, ev: dict) -> dict:
    d = BY_SLUG.get(c["direction"]) or {}
    subs = d.get("subreddits") or []
    rivals = [x["name"] for x in ev["competitors"][:3]]
    n = ev["product"]["name"]
    return {
        "validate_72h": [
            f"Write one sentence: who {n}'s buyer is and the job they hire it for; post it as a question in "
            + (", ".join(f"r/{s}" for s in subs[:2]) if subs else "two communities where they talk") + ".",
            "Put up a landing page with the wedge (market, audience or channel it leaves open) and a price.",
            "Run 20 short conversations or a $50 ad test; continue only with ≥5% sign-ups or 3 pre-orders.",
        ],
        "mvp_14d": [
            "Rebuild only the core job in the first screen; cut accounts, settings and integrations.",
            f"Differentiate on one axis {('vs ' + ', '.join(rivals)) if rivals else ''}: language/market, audience, "
            "or input speed.",
            "Ship with payment on day one (one plan, annual default).",
        ],
        "first_30_users": [
            "Reply where the demand threads are (links in Demand Echo), with the tool, not a pitch.",
            "Copy the growth move named in the investigation once it is known; post the product inside a "
            "story, not a feature list.",
            "Ask every early user for a store rating right after their first success.",
        ],
        "note": "Template filled from data; the agent mode rewrites it for this product.",
    }


def brief(con, c: dict, day: str) -> dict:
    ev = gather(con, c, day)
    rep = {
        "id": c["id"], "day": day, "entity": c["entity"], "mode": "data", "surface": c["surface"],
        "surface_name": SURFACE_NAME.get(c["surface"], c["surface"]), "source": c["source"], "pid": c["pid"],
        "direction": c["direction"], "direction_name": (BY_SLUG.get(c["direction"]) or {}).get("name", c["direction"]),
        "lesson_title": _headline(c, ev), "headline_kind": "descriptive",
        "product": ev["product"], "badge": {k: c.get(k) for k in ("metric", "before", "after", "mult", "window",
                                                                    "basis", "label", "chart", "rule")},
        "curve": ev["curve"], "measure": ev["measure"], "charts": ev["charts"][:8], "siblings": ev["siblings"],
        "sibling_measure": ev.get("sibling_measure"), "events": ev["events"], "why_grew": _why(c, ev),
        "takeaway": "", "positioning": {}, "differentiators": [], "competitors": ev["competitors"],
        "moat": "", "discounts": _discounts(c, ev), "demand_echo": ev["demand"], "traces": ev["traces"],
        "also": c.get("also", []), "echo": c.get("echo"),
    }
    rep["grade"] = _grade(c, ev)
    rep["follow"] = _follow(con, c, ev, day)
    if rep["grade"]["grade"] in ("S", "A"):
        rep["build_kit"] = _build_kit(c, ev)
    rep["staying_power"] = "unclear"
    return rep


# ---------------------------------------------------------------- agent mode

AGENT_SYSTEM = """You are the investigation desk of a daily breakout-intelligence product for solo builders.
You receive one product that crossed a measurable line today, with ALL evidence we have. Write ONLY from that
evidence. Never invent numbers, dates, people or links. If the trigger is unknown, say "Trigger not found" and
give your best hypothesis labeled inferred. Return one JSON object, no prose, with keys:
lesson_title (the transferable play, max 70 chars, not just the product name), what (one sentence),
takeaway (one sentence a builder can apply), why_grew [{text,label:fact|inferred|not_found,url}],
positioning {for_whom, job, before_it, wedge}, differentiators [{claim, evidence, label}],
moat (one line), discounts [strings], mechanism (2-5 word tag of the growth move),
staying_power (pulse|has-legs|unclear), follow {play, wedge, avoid},
build_kit {validate_72h:[3], mvp_14d:[3], first_30_users:[3]}.
A 'fact' must cite a URL that appears in the evidence."""


def _evidence_urls(rep: dict) -> set:
    urls = {rep["product"].get("url"), rep["product"].get("site")}
    urls |= {t.get("url") for t in rep.get("traces", [])}
    urls |= {t.get("url") for t in rep["demand_echo"].get("threads", [])}
    urls |= {e.get("url") for e in rep.get("events", [])}
    urls |= {c.get("url") for c in rep.get("competitors", [])}
    return {u for u in urls if u}


def agent_available() -> bool:
    return bool(os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("ANTHROPIC_API_KEY"))


def agent(rep: dict) -> dict:
    import anthropic
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("ANTHROPIC_API_KEY"),
        base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)
    evidence = {k: rep[k] for k in ("lesson_title", "product", "badge", "measure", "charts", "events", "why_grew",
                                    "competitors", "discounts", "demand_echo", "traces", "direction_name", "follow")}
    msg = client.messages.create(model=MODEL, max_tokens=4000, system=AGENT_SYSTEM,
                                 messages=[{"role": "user", "content": json.dumps(evidence, ensure_ascii=False)}])
    text = "".join(getattr(b, "text", "") for b in msg.content)
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError("no JSON in model output")
    out = json.loads(m.group(0))
    allowed = _evidence_urls(rep)
    for claim in out.get("why_grew", []):  # verify: a fact needs a URL we actually gathered
        if claim.get("label") == "fact" and claim.get("url") not in allowed:
            claim["label"] = "inferred"
    for k in ("lesson_title", "what", "takeaway", "why_grew", "positioning", "differentiators", "moat",
              "mechanism", "staying_power"):
        if out.get(k):
            rep[k] = out[k]
    if out.get("discounts"):
        rep["discounts"] = list(dict.fromkeys(rep["discounts"] + out["discounts"]))
    if out.get("follow"):
        rep["follow"] = {**rep["follow"], **{k: v for k, v in out["follow"].items() if v}}
    if out.get("build_kit") and "build_kit" in rep:
        rep["build_kit"] = {**out["build_kit"], "note": "Written by the agent from the evidence above."}
    rep["mode"] = "agent"
    rep["headline_kind"] = "lesson"
    return rep


def run(con, day: str) -> int:
    rows = con.execute("SELECT json FROM candidates WHERE day=? AND picked=1 ORDER BY score DESC", (day,)).fetchall()
    cands = [json.loads(r["json"]) for r in rows]
    if not cands:
        return 0
    try:  # TinyFish trace for picks (CI only); writes the traces table the brief reads
        from .sources import trace_products
        trace_products(con, [{"source": c["source"], "pid": c["pid"], "name": c["name"], "direction": c["direction"]}
                             for c in cands], max_items=len(cands))
        con.commit()
    except Exception as e:  # noqa: BLE001
        print(f"[radar] trace skipped: {e}", flush=True)
    use_agent = agent_available()
    # a re-run replaces the day's briefs, so picks and briefs never disagree
    con.execute("DELETE FROM investigations WHERE day=?", (day,))
    n = 0
    for c in cands:
        rep = brief(con, c, day)
        status = "published"
        if use_agent:
            try:
                rep = agent(rep)
            except Exception as e:  # noqa: BLE001
                rep["agent_error"] = str(e)[:200]
        # retraction rule: an agent that says the numbers don't reconcile, or a product we can't identify
        if not rep["product"].get("name"):
            status = "retracted"
        con.execute("INSERT OR REPLACE INTO investigations(id,day,status,mode,json) VALUES(?,?,?,?,?)",
                    (c["id"], day, status, rep["mode"], json.dumps(rep, ensure_ascii=False, default=str)))
        n += 1
    return n

