"""v3 synthesis: directions, track record (follow-up audit), playbook mechanisms.

Read-only over the store; the site builder calls these.
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timedelta

from .analyze import _series
from .detect import daily_deltas
from .taxonomy import BY_SLUG, DIRECTIONS

HORIZONS = (7, 14, 30)
RANK_RULES = {"chart_jump", "chart_new", "minigame_rank", "drama_chart", "web_traffic"}


def _d(s: str) -> datetime:
    return datetime.strptime(s[:10], "%Y-%m-%d")


def investigations(con, day: str | None = None) -> list:
    q = "SELECT json FROM investigations WHERE status='published'" + (" AND day=?" if day else "") + " ORDER BY day DESC"
    out = [json.loads(r["json"]) for r in con.execute(q, (day,) if day else ())]
    return out


def candidates(con, day: str) -> list:
    return [json.loads(r["json"]) for r in con.execute(
        "SELECT json FROM candidates WHERE day=? ORDER BY picked DESC, score DESC", (day,))]


def days_with_candidates(con) -> list:
    return [r[0] for r in con.execute("SELECT DISTINCT day FROM candidates ORDER BY day DESC")]


# ---------------------------------------------------------------- track record

def _value_at(con, rep: dict, day: str):
    b = rep["badge"]
    src, pid, rule = rep["source"], rep["pid"], b.get("rule")
    if rule in ("chart_jump", "chart_new", "minigame_rank"):
        pts = _series(con, src, b.get("chart") or "").get(pid, [])
    elif rule == "drama_chart":
        pts = _series(con, "drama", "rank:tiktok").get(pid, [])
    elif rule == "gp_installs":
        pts = daily_deltas(_series(con, "play", "installs").get(pid, []))
    elif rule == "ios_ratings":
        pts = daily_deltas(_series(con, "ios", "ratings").get(pid, []))
    elif rule == "gh_stars":
        pts = _series(con, "github", "stars").get(pid, [])
    elif rule == "drama_ads":
        pts = _series(con, "drama_ad", "creatives").get(pid, [])
    elif rule == "revenue":
        pts = _series(con, "trustmrr", "mrr").get(pid, [])
    else:
        pts = []
    near = [(d, v) for d, v in pts if abs((_d(d) - _d(day)).days) <= 2]
    return near[-1][1] if near else None


def followups(con, today: str) -> dict:
    """For each published item old enough: did it hold at D+7/14/30? Rank rules: still within 1.5x of the
    rank it reached. Volume rules: still >= 2x its before-baseline. Off-chart counts as faded."""
    rows = []
    for rep in investigations(con):
        b = rep["badge"]
        age = (_d(today) - _d(rep["day"])).days
        rec = {"id": rep["id"], "day": rep["day"], "name": rep["product"]["name"], "grade": rep["grade"]["grade"],
               "surface": rep["surface"], "rule": b.get("rule"), "outcomes": {}}
        for h in HORIZONS:
            if age < h:
                continue
            v = _value_at(con, rep, (_d(rep["day"]) + timedelta(days=h)).strftime("%Y-%m-%d"))
            if b.get("rule") in RANK_RULES:
                ok = v is not None and b.get("after") and v <= b["after"] * 1.5
                grew = v is not None and b.get("after") and v < b["after"]
            elif b.get("rule") == "gh_stars":
                ok = v is not None
                grew = ok
            else:
                base = b.get("before") or 0
                ok = v is not None and base and v >= 2 * base
                grew = v is not None and b.get("after") and v > b["after"]
            rec["outcomes"][h] = "grew" if grew else ("held" if ok else "faded")
        rows.append(rec)
    stats = {}
    for h in HORIZONS:
        by = defaultdict(lambda: {"n": 0, "held": 0})
        for r in rows:
            o = r["outcomes"].get(h)
            if not o:
                continue
            for key in (r["grade"], "all"):
                by[key]["n"] += 1
                by[key]["held"] += 1 if o in ("held", "grew") else 0
        stats[h] = dict(by)
    first = min((r["day"] for r in rows), default=None)
    return {"rows": rows, "stats": stats, "first_day": first,
            "next_audit": (_d(first) + timedelta(days=7)).strftime("%Y-%m-%d") if first else None}


# ---------------------------------------------------------------- mechanisms -> playbooks

def mechanism(rep: dict) -> str:
    if rep.get("mechanism"):
        return rep["mechanism"].strip().lower()
    b, ev = rep["badge"], rep.get("events") or []
    shipped = [e for e in ev if e["text"].startswith("Shipped") and (_d(rep["day"]) - _d(e["date"])).days <= 4]
    if rep["source"] == "drama_ad":
        return "ad-led drama push"
    if rep["source"] == "minigame":
        return "mini-game chart push"
    if rep["source"] == "github":
        return "open-source trending wave"
    if shipped:
        return "update-driven climb"
    if b.get("rule") == "chart_new":
        return "fresh chart entry"
    if rep["source"] == "trustmrr":
        return "revenue climb"
    return "unexplained climb"


def plays(con) -> list:
    groups = defaultdict(list)
    for rep in investigations(con):
        groups[mechanism(rep)].append(rep)
    out = []
    for mech, reps in groups.items():
        out.append({"mechanism": mech, "n": len(reps), "agent": sum(1 for r in reps if r["mode"] == "agent"),
                    "last": max(r["day"] for r in reps), "status": "verified play" if len(reps) >= 3 and any(
                        r["mode"] == "agent" for r in reps) else "forming",
                    "cases": sorted(reps, key=lambda r: -r["grade"]["score"])[:6]})
    return sorted(out, key=lambda p: (-p["n"], p["mechanism"]))


# ---------------------------------------------------------------- directions

def directions(con, day: str) -> list:
    week = (_d(day) - timedelta(days=7)).strftime("%Y-%m-%d")
    year = (_d(day) - timedelta(days=365)).strftime("%Y-%m-%d")
    since14 = int((_d(day) - timedelta(days=14)).timestamp())
    brk = defaultdict(list)
    for r in con.execute("SELECT day, json FROM candidates WHERE day>? AND day<=?", (week, day)):
        c = json.loads(r["json"])
        brk[c["direction"]].append(c)
    inv = defaultdict(list)
    for rep in investigations(con):
        if rep["day"] > week:
            inv[rep["direction"]].append(rep)
    charting = defaultdict(set)
    new12 = defaultdict(set)
    for src in ("ios", "play"):
        on = {r[0] for r in con.execute(
            "SELECT DISTINCT pid FROM metrics WHERE source=? AND day=? AND metric LIKE 'rank:%'", (src, day))}
        for r in con.execute("SELECT pid, direction, meta FROM products WHERE source=?", (src,)):
            if r["pid"] in on:
                charting[r["direction"]].add(f"{src}:{r['pid']}")
                rel = json.loads(r["meta"] or "{}").get("released") or ""
                if rel[:4].isdigit() and rel >= year:
                    new12[r["direction"]].add(f"{src}:{r['pid']}")
    mrr = {pid: pts[-1][1] for pid, pts in _series(con, "trustmrr", "mrr").items()
           if pts[-1][0] >= (_d(day) - timedelta(days=60)).strftime("%Y-%m-%d")}
    saas = defaultdict(list)
    for r in con.execute("SELECT pid, name, url, direction FROM products WHERE source='trustmrr'"):
        if mrr.get(r["pid"]):
            saas[r["direction"]].append({"name": r["name"], "url": r["url"], "mrr": mrr[r["pid"]]})
    threads = defaultdict(int)
    for r in con.execute("SELECT direction, COUNT(*) n FROM threads WHERE created_utc>=? GROUP BY direction",
                         (since14,)):
        threads[r["direction"]] = r["n"]
    out = []
    for d in DIRECTIONS:
        slug = d["slug"]
        s = sorted(saas[slug], key=lambda x: -x["mrr"])
        row = {"slug": slug, "name": d["name"], "group": d["group"], "fit": d["fit"],
               "breakouts_7d": len(brk[slug]), "investigated_7d": len(inv[slug]),
               "charting": len(charting[slug]), "new_12m": len(new12[slug]),
               "saas": len(s), "saas_10k": sum(1 for x in s if x["mrr"] >= 10_000), "top_saas": s[:6],
               "threads_14d": threads[slug], "items": sorted(inv[slug], key=lambda r: r["day"], reverse=True)[:12],
               "cands": sorted(brk[slug], key=lambda c: (c["day"], c["score"]), reverse=True)[:30]}
        out.append(row)
    return sorted(out, key=lambda r: (-r["breakouts_7d"], -r["threads_14d"]))


def direction_meta(slug: str) -> dict:
    return BY_SLUG.get(slug) or {"name": slug, "group": "Other", "subreddits": []}
