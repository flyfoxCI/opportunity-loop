"""Turn the snapshot store into the site model: signals, direction landscapes, Score v2, validation kits.

Score v2 (PRD):  (0.30 money + 0.25 momentum + 0.20 demand + 0.15 gap + 0.10 fit) x confidence
Verdict:         ENTER  score >= 0.60, 2+ verified products at $1K+ MRR, demand >= 0.5 and gap >= 0.3
                 NARROW score >= 0.45 and floor met (real, but pick one angle / one buyer)
                 WATCH  otherwise
Evidence floor:  a verified TrustMRR product in the direction at >= $500 MRR,
                 or >= 2 independent sources showing activity.
"""

from __future__ import annotations

import glob
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

from .store import ROOT
from .taxonomy import BY_SLUG, DIRECTIONS, classify, classify_app

# Publishers whose launches say nothing about an indie opportunity.
BIG_PUBLISHERS = ("meta platforms", "google", "microsoft", "openai", "x.ai", "xai", "x corp", "amazon", "apple",
                  "tiktok", "bytedance", "snap inc", "adobe", "netflix", "spotify", "disney", "tencent",
                  "alibaba", "samsung", "uber", "paypal", "intuit", "anthropic", "perplexity", "duolingo")

W = {"money": 0.30, "momentum": 0.25, "demand": 0.20, "gap": 0.15, "fit": 0.10}
ENTER, NARROW = 0.60, 0.45


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _d(s: str) -> datetime:
    return datetime.strptime(s[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)


def _clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def _logscale(v: float, lo: float, hi: float) -> float:
    if not v or v <= 0:
        return 0.0
    return _clamp((math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo)))


def _pct_rank(values: dict[str, float]) -> dict[str, float]:
    """Percentile 0-1 among directions; zeros stay 0."""
    nz = sorted(v for v in values.values() if v > 0)
    out = {}
    for k, v in values.items():
        if v <= 0 or not nz:
            out[k] = 0.0
        else:
            out[k] = (sum(1 for x in nz if x <= v)) / len(nz)
    return out


def _series(con, source: str, metric: str) -> dict[str, list[tuple[str, float]]]:
    s = defaultdict(list)
    for r in con.execute("SELECT pid, day, value FROM metrics WHERE source=? AND metric=? ORDER BY day", (source, metric)):
        s[r["pid"]].append((r["day"], r["value"]))
    return s


def _products(con, source: str) -> dict[str, dict]:
    out = {}
    for r in con.execute("SELECT * FROM products WHERE source=?", (source,)):
        d = dict(r)
        d["meta"] = json.loads(d.get("meta") or "{}")
        out[d["pid"]] = d
    return out


def _traces(con) -> dict[tuple[str, str], list[dict]]:
    t = defaultdict(list)
    for r in con.execute("SELECT * FROM traces ORDER BY day DESC"):
        key = (r["source"], r["pid"])
        if len(t[key]) < 4 and not any(x["url"] == r["url"] for x in t[key]):
            t[key].append({"title": r["title"], "url": r["url"], "snippet": r["snippet"]})
    return t


def _fmt_money(v: float | None) -> str:
    if v is None:
        return "–"
    if v >= 1_000_000:
        return f"${v / 1_000_000:.1f}M"
    if v >= 10_000:
        return f"${v / 1000:.0f}K"
    if v >= 1000:
        return f"${v / 1000:.1f}K"
    return f"${v:,.0f}"


# ------------------------------------------------------------------ signals

def trustmrr_signals(con, prods) -> list[dict]:
    mrr = _series(con, "trustmrr", "mrr")
    g30 = _series(con, "trustmrr", "growth_mrr_30d")
    cutoff = (_now() - timedelta(days=60)).strftime("%Y-%m-%d")
    out = []
    for pid, pts in mrr.items():
        p = prods.get(pid)
        if not p or pts[-1][0] < cutoff:
            continue
        last_day, last = pts[-1]
        if last < 100:
            continue
        sig = None
        # Prefer our own history: earliest snapshot in the last 45 days as the baseline.
        base = [x for x in pts[:-1] if x[0] >= (_d(last_day) - timedelta(days=45)).strftime("%Y-%m-%d") and x[1] > 0]
        if base:
            b_day, b = base[0]
            mult = last / b if b else 0
            if mult >= 1.3 and last - b >= 100:
                days = (_d(last_day) - _d(b_day)).days or 1
                sig = {"metric": "MRR", "before": b, "after": last, "mult": mult,
                       "window": f"{days} days", "basis": "our snapshots"}
        if sig is None:
            g = (g30.get(pid) or [(None, None)])[-1][1]
            if g is not None and 40 <= g <= 2000:
                before = last / (1 + g / 100)
                if last - before >= 100:
                    sig = {"metric": "MRR", "before": before, "after": last, "mult": last / before if before else 0,
                           "window": "30 days", "basis": "TrustMRR growth figure"}
        if sig:
            sig.update(source="trustmrr", pid=pid, name=p["name"], url=p["url"], direction=p["direction"],
                       label="verified", icon=(p["meta"] or {}).get("icon"),
                       desc=p.get("description") or "", day=last_day,
                       strength=sig["mult"] * _logscale(last, 100, 50_000) + 0.5)
            out.append(sig)
    return out


def appstore_signals(con, prods) -> list[dict]:
    out = []
    days = [r[0] for r in con.execute("SELECT DISTINCT day FROM metrics WHERE source='appstore' ORDER BY day")]
    if not days:
        return out
    today = days[-1]
    half_year = (_now() - timedelta(days=183)).strftime("%Y-%m-%d")
    for kind in ("grossing", "free"):
        ranks = _series(con, "appstore", f"rank_{kind}")
        for pid, pts in ranks.items():
            p = prods.get(pid)
            if not p or pts[-1][0] != today:
                continue
            rank = pts[-1][1]
            meta = p["meta"] or {}
            if any(b in (meta.get("seller") or "").lower() for b in BIG_PUBLISHERS):
                continue
            release = (meta.get("release") or "")[:10]
            prior = [v for d, v in pts[:-1] if d >= (_d(today) - timedelta(days=8)).strftime("%Y-%m-%d")]
            sig = None
            if prior and prior[0] - rank >= 15:
                sig = {"metric": f"Top {kind} rank ({p['category']})", "before": prior[0], "after": rank,
                       "mult": prior[0] / rank, "window": f"{len(prior) + 1} snapshots", "basis": "Apple chart", "rank": True}
            elif kind == "grossing" and release and release >= half_year and rank <= 40:
                age = (_now() - _d(release)).days
                sig = {"metric": f"Top grossing #{int(rank)} in {p['category']}", "before": None, "after": rank,
                       "mult": None, "window": f"launched {age} days ago", "basis": "Apple chart", "rank": True,
                       "young": True}
            if sig:
                sig.update(source="appstore", pid=pid, name=p["name"], url=p["url"], direction=p["direction"],
                           label="verified", icon=meta.get("icon"), desc=(p.get("description") or "")[:220], day=today,
                           strength=(2.5 if sig.get("young") else min(sig["mult"] or 1, 6)) + (1.0 if kind == "grossing" else 0))
                out.append(sig)
    # Daily new-rating spikes (stringers-style): today's delta >= 3x the trailing average delta.
    for pid, pts in _series(con, "appstore", "rating_count").items():
        if len(pts) < 4 or pts[-1][0] != today:
            continue
        deltas = [(pts[i][1] - pts[i - 1][1]) / max(1, (_d(pts[i][0]) - _d(pts[i - 1][0])).days) for i in range(1, len(pts))]
        today_d, base = deltas[-1], deltas[-8:-1]
        avg = sum(base) / len(base) if base else 0
        if today_d >= 20 and avg > 0 and today_d / avg >= 3:
            p = prods.get(pid)
            if p:
                out.append({"metric": "Daily new ratings", "before": avg, "after": today_d, "mult": today_d / avg,
                            "window": "vs 7-day avg", "basis": "iTunes Lookup", "source": "appstore", "pid": pid,
                            "name": p["name"], "url": p["url"], "direction": p["direction"], "label": "estimated",
                            "icon": (p["meta"] or {}).get("icon"), "desc": (p.get("description") or "")[:220],
                            "day": today, "strength": min(today_d / avg, 10)})
    return out


def github_signals(con, prods) -> list[dict]:
    out = []
    st = _series(con, "github", "stars_today")
    tot = _series(con, "github", "stars")
    if not st:
        return out
    today = max(pts[-1][0] for pts in st.values())
    for pid, pts in st.items():
        if pts[-1][0] != today:
            continue
        v = pts[-1][1]
        total = (tot.get(pid) or [(None, 0)])[-1][1] or 0
        prev = [x for _, x in pts[:-1]]
        p = prods.get(pid)
        if not p or v < 150:
            continue
        base = (sum(prev) / len(prev)) if prev else None
        out.append({"metric": "GitHub stars per day", "before": base, "after": v,
                    "mult": (v / base) if base else None, "window": "vs prior days" if base else f"{int(total):,} total",
                    "basis": "GitHub Trending", "source": "github", "pid": pid, "name": pid, "url": p["url"],
                    "direction": p["direction"], "label": "verified", "icon": None,
                    "desc": (p.get("description") or "")[:220], "day": today,
                    "strength": min(v / 400, 3) + (v / total * 5 if total else 0)})
    return out


# ------------------------------------------------------------------ directions

def _asks_first(threads: list[dict]) -> list[dict]:
    """Posts whose title itself asks for something rank above chatter with a buried ask."""
    from .sources import INTENT
    return sorted(threads, key=lambda t: (0 if INTENT.search(t.get("title") or "") else 1, -(t.get("num_comments") or 0)))


def _reddit_rates(con) -> tuple[dict, dict]:
    """Sum each subreddit's latest per-direction weekly intent rate into a per-direction rate."""
    posts, comments = defaultdict(float), defaultdict(float)
    latest = {r[0]: r[1] for r in con.execute(
        "SELECT pid, MAX(day) FROM metrics WHERE source='reddit_sub' AND metric='posts_scanned' GROUP BY pid")}
    for r in con.execute("SELECT pid, metric, day, value FROM metrics WHERE source='reddit_sub' AND metric LIKE '%:%'"):
        if latest.get(r["pid"]) != r["day"]:
            continue
        kind, slug = r["metric"].split(":", 1)
        (posts if kind == "intent_wk" else comments)[slug] += r["value"] or 0
    return dict(posts), dict(comments)


def _packages() -> list[dict]:
    pk = []
    for f in sorted(glob.glob(str(ROOT / "docs/directions/*.md"))):
        txt = open(f, encoding="utf-8").read()
        fm = txt.split("---", 2)[1] if txt.startswith("---") else ""
        get = lambda k: (re.search(rf'^{k}:\s*"?(.*?)"?\s*$', fm, re.M) or [None, ""])[1]  # noqa: E731
        title, excerpt, slug = get("title"), get("excerpt"), get("slug")
        tier = (re.search(r"Tier:\s*\*\*(\w+)\*\*", txt) or [None, ""])[1]
        direction, _ = classify(title, excerpt)
        pk.append({"slug": slug or f.rsplit("/", 1)[-1][:-3], "title": title.replace("Direction — ", ""),
                   "excerpt": excerpt, "tier": tier, "date": get("date")[:10], "direction": direction,
                   "url": f"../directions/{(slug or f.rsplit('/', 1)[-1][:-3])}.html"})
    return pk


def directions(con, signals: list[dict]) -> list[dict]:
    tm = _products(con, "trustmrr")
    ap = _products(con, "appstore")
    gh = _products(con, "github")
    mrr = {pid: pts[-1][1] for pid, pts in _series(con, "trustmrr", "mrr").items()}
    g30 = {pid: pts[-1][1] for pid, pts in _series(con, "trustmrr", "growth_mrr_30d").items()}
    cutoff60 = (_now() - timedelta(days=60)).strftime("%Y-%m-%d")
    ap_day = (con.execute("SELECT MAX(day) FROM metrics WHERE source='appstore'").fetchone()[0]) or ""
    gross = {pid: pts[-1][1] for pid, pts in _series(con, "appstore", "rank_grossing").items() if pts[-1][0] == ap_day}
    free = {pid: pts[-1][1] for pid, pts in _series(con, "appstore", "rank_free").items() if pts[-1][0] == ap_day}
    gh_day = (con.execute("SELECT MAX(day) FROM metrics WHERE source='github'").fetchone()[0]) or ""
    gh_today = {pid: pts[-1][1] for pid, pts in _series(con, "github", "stars_today").items() if pts[-1][0] == gh_day}
    reddit_posts, reddit_comments = _reddit_rates(con)
    since = int((_now() - timedelta(days=30)).timestamp())
    packages = _packages()
    year_ago = (_now() - timedelta(days=365)).strftime("%Y-%m-%d")

    rows = []
    for d in DIRECTIONS:
        slug = d["slug"]
        t_items = sorted(
            [{"pid": pid, "name": p["name"], "url": p["url"], "desc": (p.get("description") or "")[:200],
              "mrr": mrr.get(pid), "growth": g30.get(pid), "last_seen": p["last_seen"],
              "founded": ((p["meta"] or {}).get("foundedDate") or "")[:10], "on_sale": (p["meta"] or {}).get("onSale"),
              "asking": (p["meta"] or {}).get("askingPrice"), "icon": (p["meta"] or {}).get("icon"),
              "website": (p["meta"] or {}).get("website")}
             for pid, p in tm.items() if p["direction"] == slug and p["last_seen"] >= cutoff60 and (mrr.get(pid) or 0) > 0],
            key=lambda x: -(x["mrr"] or 0))
        a_items = sorted(
            [{"pid": pid, "name": p["name"], "url": p["url"], "category": p["category"], "grossing": gross.get(pid),
              "free": free.get(pid), "release": ((p["meta"] or {}).get("release") or "")[:10],
              "rating": (p["meta"] or {}).get("rating"), "icon": (p["meta"] or {}).get("icon"),
              "seller": (p["meta"] or {}).get("seller")}
             for pid, p in ap.items() if p["direction"] == slug and (pid in gross or pid in free)],
            key=lambda x: (x["grossing"] or 999, x["free"] or 999))
        g_items = [{"pid": pid, "url": p["url"], "desc": p.get("description") or "", "today": gh_today.get(pid)}
                   for pid, p in gh.items() if p["direction"] == slug and pid in gh_today]
        threads = [dict(r) for r in con.execute(
            "SELECT * FROM threads WHERE direction=? AND created_utc>=? AND title NOT LIKE '[%Removed%' "
            "AND title NOT LIKE '[deleted%' ORDER BY num_comments DESC, score DESC LIMIT 80", (slug, since))]
        threads = _asks_first(threads)[:40]
        top5 = [x["mrr"] for x in t_items[:5] if x["mrr"]]
        median_top5 = sorted(top5)[len(top5) // 2] if top5 else 0
        stats = {
            "tm_players": len(t_items),
            "tm_earners_1k": sum(1 for x in t_items if (x["mrr"] or 0) >= 1000),
            "tm_earners_10k": sum(1 for x in t_items if (x["mrr"] or 0) >= 10_000),
            "tm_top_mrr": t_items[0]["mrr"] if t_items else 0,
            "tm_median_top5": median_top5,
            "tm_growers": sum(1 for x in t_items if (x["growth"] or 0) >= 30),
            "tm_new": sum(1 for x in t_items if x["founded"] and x["founded"] >= year_ago),
            "app_chart": len(a_items),
            "app_grossing": sum(1 for x in a_items if x["grossing"]),
            "app_best_grossing": min([x["grossing"] for x in a_items if x["grossing"]] or [0]),
            "app_new": sum(1 for x in a_items if x["release"] and x["release"] >= year_ago),
            "gh_trending": len(g_items),
            "reddit_posts": round(reddit_posts.get(slug, 0), 1),
            "reddit_comments": round(reddit_comments.get(slug, 0)),
            "signals": sum(1 for s in signals if s["direction"] == slug),
        }
        cadence = Counter()
        for x in t_items:
            if x["founded"] and x["founded"] >= year_ago:
                cadence[x["founded"][:7]] += 1
        for x in a_items:
            if x["release"] and x["release"] >= year_ago:
                cadence[x["release"][:7]] += 1
        rows.append({"slug": slug, "name": d["name"], "group": d["group"], "fit": d["fit"],
                     "subreddits": d["subreddits"], "queries": d["queries"], "keywords": d["keywords"],
                     "stats": stats, "trustmrr": t_items, "apps": a_items, "github": g_items,
                     "threads": threads, "cadence": sorted(cadence.items()),
                     "packages": [p for p in packages if p["direction"] == slug]})

    # ---- Score v2
    gross_p = _pct_rank({r["slug"]: r["stats"]["app_grossing"] for r in rows})
    money_v = {r["slug"]: 0.7 * _logscale(r["stats"]["tm_median_top5"], 300, 30_000) + 0.3 * gross_p[r["slug"]]
               for r in rows}
    mom_raw = {r["slug"]: r["stats"]["tm_growers"] * 2 + r["stats"]["signals"] * 1.5 + r["stats"]["gh_trending"] * 0.5
               + r["stats"]["app_new"] * 0.5 for r in rows}
    dem_raw = {r["slug"]: r["stats"]["reddit_posts"] + r["stats"]["reddit_comments"] / 20 for r in rows}
    crowd_raw = {r["slug"]: r["stats"]["tm_players"] + r["stats"]["app_chart"] for r in rows}
    per_player = {k: dem_raw[k] / (crowd_raw[k] + 1) for k in dem_raw}
    mom_p, dem_p, crowd_p, pp_p = _pct_rank(mom_raw), _pct_rank(dem_raw), _pct_rank(crowd_raw), _pct_rank(per_player)
    for r in rows:
        s = r["slug"]
        st = r["stats"]
        comp = {
            "money": round(money_v[s], 2),
            "momentum": round(mom_p[s], 2),
            "demand": round(dem_p[s], 2),
            "gap": round(0.5 * (1 - crowd_p[s]) + 0.5 * pp_p[s], 2),
            "fit": r["fit"],
        }
        n_src = sum([st["tm_players"] > 0, st["app_chart"] > 0, st["reddit_posts"] > 0, st["gh_trending"] > 0])
        conf = {0: 0.3, 1: 0.5, 2: 0.8}.get(n_src, 1.0)
        score = round(sum(W[k] * comp[k] for k in W) * conf, 3)
        floor = (st["tm_top_mrr"] or 0) >= 500 or n_src >= 2
        enter = (score >= ENTER and floor and st["tm_earners_1k"] >= 2
                 and comp["demand"] >= 0.5 and comp["gap"] >= 0.3)
        verdict = "ENTER" if enter else "NARROW" if score >= NARROW and floor else "WATCH"
        r.update(components=comp, confidence=conf, sources=n_src, score=score, floor=floor, verdict=verdict,
                 kit=validation_kit(r))
        r["why"] = _why(r)
    order = {"ENTER": 0, "NARROW": 1, "WATCH": 2}
    rows.sort(key=lambda r: (order[r["verdict"]], -r["score"]))
    return rows


def _why(r: dict) -> str:
    st, c = r["stats"], r["components"]
    bits = []
    if st["tm_earners_1k"]:
        bits.append(f"{st['tm_earners_1k']} verified product{'s' if st['tm_earners_1k'] > 1 else ''} at $1K+ MRR")
    elif st["tm_top_mrr"]:
        bits.append(f"top verified MRR {_fmt_money(st['tm_top_mrr'])}")
    if st["app_grossing"]:
        bits.append(f"{st['app_grossing']} apps in US top-grossing charts")
    if st["reddit_posts"]:
        bits.append(f"{st['reddit_posts']:g} buyer-intent Reddit posts a week")
    if st["tm_growers"]:
        bits.append(f"{st['tm_growers']} growing 30%+ a month")
    if c["gap"] >= 0.6:
        bits.append("demand is high for the number of players")
    elif c["gap"] <= 0.25:
        bits.append("crowded for the demand we can see")
    return "; ".join(bits[:4]) or "little evidence yet"


def validation_kit(r: dict) -> dict:
    """A 72-hour test built from this direction's own evidence."""
    threads = r["threads"]
    handles, seen = [], set()
    for t in threads:
        a = t.get("author") or ""
        if a and a not in seen and a not in ("[deleted]", "AutoModerator"):
            seen.add(a)
            handles.append({"handle": a, "subreddit": t["subreddit"], "title": t["title"],
                            "url": f"https://www.reddit.com/r/{t['subreddit']}/comments/{t['id']}/"})
        if len(handles) >= 20:
            break
    pains = [t["title"] for t in threads[:5]]
    comps = [x["name"] for x in r["trustmrr"][:3]] + [x["name"] for x in r["apps"][:3]]
    return {
        "pains": pains,
        "competitors": comps[:5],
        "channels": [f"r/{s}" for s in r["subreddits"]],
        "handles": handles,
        "pass_bar": "≥ 5% of 200+ visitors leave an email, or ≥ 3 people pre-pay / book a call within 72 hours",
        "kill_bar": "< 2% signup after 200 visitors, or every reply says 'I already use X' — go back to Direction",
    }


# ------------------------------------------------------------------ entry point

def reclassify(con) -> None:
    """Re-file every product with the current taxonomy, so keyword edits apply to history too."""
    rows = con.execute("SELECT source, pid, name, description, category, meta FROM products").fetchall()
    for r in rows:
        meta = json.loads(r["meta"] or "{}")
        if r["source"] == "appstore":
            d, c = classify_app(r["name"], r["description"], meta.get("genre_id"))
        else:
            d, c = classify(r["name"], r["description"], r["category"] or "")
            if r["source"] == "github" and d == "other":
                d, c = "devtools", 0.2
        con.execute("UPDATE products SET direction=?, direction_conf=? WHERE source=? AND pid=?", (d, c, r["source"], r["pid"]))
    con.commit()


def run(con) -> dict:
    reclassify(con)
    tm, ap, gh = _products(con, "trustmrr"), _products(con, "appstore"), _products(con, "github")
    signals = trustmrr_signals(con, tm) + appstore_signals(con, ap) + github_signals(con, gh)
    traces = _traces(con)
    for s in signals:
        s["trace"] = traces.get((s["source"], s["pid"]), [])
        s["direction_name"] = BY_SLUG.get(s["direction"], {}).get("name", "Unclassified")
    signals.sort(key=lambda s: -s["strength"])
    dirs = directions(con, signals)
    health = [dict(r) for r in con.execute(
        "SELECT source, day, ok, rows, note FROM source_runs WHERE (source, day) IN "
        "(SELECT source, MAX(day) FROM source_runs GROUP BY source)")]
    since = int((_now() - timedelta(days=30)).timestamp())
    hot_threads = [dict(r) for r in con.execute(
        "SELECT * FROM threads WHERE created_utc>=? AND title NOT LIKE '[%Removed%' AND title NOT LIKE '[deleted%' "
        "ORDER BY num_comments DESC LIMIT 200", (since,))]
    hot_threads = _asks_first(hot_threads)[:12]
    for t in hot_threads:
        t["direction_name"] = BY_SLUG.get(t["direction"], {}).get("name", "")
    counts = {r[0]: r[1] for r in con.execute("SELECT source, COUNT(*) FROM products GROUP BY source")}
    snapshot_days = con.execute("SELECT COUNT(DISTINCT day) FROM metrics WHERE source='trustmrr'").fetchone()[0]
    return {"generated": _now().strftime("%Y-%m-%d %H:%M UTC"), "signals": signals, "directions": dirs,
            "health": health, "hot_threads": hot_threads, "counts": counts, "snapshot_days": snapshot_days,
            "packages": _packages()}
