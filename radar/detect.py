"""v3 detection: which products crossed a line today, and which of them get a full brief.

Each rule compares a product with *its own* recent baseline (today >= N x its trailing average,
above an absolute floor). New sources have no history yet, so until a product has
`min_baseline_points` days we fall back to the delta the source itself reports (Appark rank
change / newly-promoted flag, Gravity rank change, drama creatives) and say so on the card:
every candidate carries `basis` = own-baseline | source-delta | cold-start.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

from .analyze import _products, _series, tranco_signals, trustmrr_signals
from .taxonomy import BY_SLUG

CFG = json.loads((Path(__file__).parent / "v3.json").read_text(encoding="utf-8"))
SURFACE = {"ios": "apps", "play": "apps", "github": "opensource", "trustmrr": "saas", "tranco": "saas",
           "minigame": "minigames", "drama": "drama", "drama_ad": "drama"}
SURFACE_NAME = {"apps": "Apps & games", "saas": "Web & SaaS", "opensource": "Open source",
                "minigames": "Mini-games", "drama": "Short drama"}
LIST_NAME = {"free": "Top Free", "paid": "Top Paid", "grossing": "Top Grossing"}
# Grossing moves mean money; paid charts are thin (a few sales move a rank in a small store).
LIST_WEIGHT = {"grossing": 1.4, "free": 1.0, "paid": 0.45}


def _d(s: str) -> datetime:
    return datetime.strptime(s[:10], "%Y-%m-%d")


def chart_name(metric: str) -> str:
    """'rank:free:us:6015' -> 'US Top Free · Finance'"""
    from .feeds.appark import GENRES
    parts = metric.split(":")
    if len(parts) < 4:
        return metric
    _k, lst, cc, cat = parts[:4]
    g = GENRES.get(int(cat), cat) if cat.isdigit() else cat
    return f"{cc.upper()} {LIST_NAME.get(lst, lst)}" + ("" if g == "All" else f" · {g}")


def daily_deltas(pts: list) -> list:
    """Cumulative series [(day, total)] -> [(day, per-day increase)]; gaps spread evenly."""
    out = []
    for (d0, v0), (d1, v1) in zip(pts, pts[1:]):
        gap = max(1, (_d(d1) - _d(d0)).days)
        if v0 is None or v1 is None or v1 < v0:
            continue
        out.append((d1, (v1 - v0) / gap))
    return out


def _baseline(vals: list, day: str, days: int) -> list:
    lo = (_d(day) - timedelta(days=days)).strftime("%Y-%m-%d")
    return [v for d, v in vals if lo <= d < day]


def _cand(source, pid, day, rule, *, metric, before, after, basis, window, label="verified",
          chart="", detail="") -> dict:
    mult = (after / before) if before and before > 0 and after is not None else None
    return {"source": source, "pid": str(pid), "day": day, "rule": rule, "metric": metric, "before": before,
            "after": after, "mult": mult, "basis": basis, "window": window, "label": label, "chart": chart,
            "detail": detail, "surface": SURFACE.get(source, "other")}


# ---------------------------------------------------------------- rules

def rule_cumulative(con, day, source, metric, rule) -> list:
    """gp_installs / ios_ratings: per-day increase of a cumulative counter vs own baseline."""
    R, G = CFG["rules"][rule], CFG["rules"]
    out = []
    for pid, pts in _series(con, source, metric).items():
        dd = daily_deltas(pts)
        if not dd or dd[-1][0] != day:
            continue
        today = dd[-1][1]
        # Play refreshes detail pages every other day: average the last two deltas when the latest is 0
        if today == 0 and len(dd) > 1:
            continue
        base = _baseline(dd[:-1], day, G["baseline_days"])
        if len(base) < G["min_baseline_points"]:
            continue
        avg = sum(base) / len(base)
        if today >= R["floor"] and avg > 0 and today >= R["mult"] * avg:
            out.append(_cand(source, pid, day, rule, metric=R["label"], before=avg, after=today,
                             basis="own-baseline", window=f"vs {len(base)}-day average",
                             label="verified" if source == "play" else "estimated"))
    return out


def rule_charts(con, day, source) -> list:
    """chart_jump + chart_new from Appark's own rank_change / newly_promoted (source-delta)."""
    J, N = CFG["rules"]["chart_jump"], CFG["rules"]["chart_new"]
    best = {}
    rows = con.execute("SELECT pid, metric, value FROM metrics WHERE source=? AND day=? AND "
                       "(metric LIKE 'chg:%' OR metric LIKE 'new:%')", (source, day)).fetchall()
    ranks = {(r["pid"], r["metric"]): r["value"] for r in con.execute(
        "SELECT pid, metric, value FROM metrics WHERE source=? AND day=? AND metric LIKE 'rank:%'", (source, day))}
    for r in rows:
        kind, chart = r["metric"].split(":", 1)
        rank = ranks.get((r["pid"], f"rank:{chart}"))
        if rank is None:
            continue
        lst = chart.split(":")[0]
        if kind == "chg" and r["value"] >= J["min_jump"] and rank <= J["max_rank"]:
            c = _cand(source, r["pid"], day, "chart_jump", metric=J["label"], before=rank + r["value"], after=rank,
                      basis="source-delta", window="since yesterday", chart=f"rank:{chart}")
            c["strength"] = math.log2((rank + r["value"]) / rank) * LIST_WEIGHT.get(lst, 1.0) * \
                (1.2 if chart.split(":")[-1] != "36" else 1.0) * (1 + (J["max_rank"] - rank) / J["max_rank"])
        elif kind == "new" and rank <= N["max_rank"]:
            c = _cand(source, r["pid"], day, "chart_new", metric=N["label"], before=None, after=rank,
                      basis="source-delta", window="first day on this chart", chart=f"rank:{chart}")
            c["strength"] = 1.5 * LIST_WEIGHT.get(lst, 1.0) * (1 + (N["max_rank"] - rank) / N["max_rank"])
        else:
            continue
        if r["pid"] not in best or c["strength"] > best[r["pid"]]["strength"]:
            best[r["pid"]] = c
    return list(best.values())


def rule_github(con, day) -> list:
    R, G = CFG["rules"]["gh_stars"], CFG["rules"]
    out = []
    for pid, pts in _series(con, "github", "stars_today").items():
        if pts[-1][0] != day:
            continue
        today = pts[-1][1]
        base = _baseline(pts[:-1], day, G["baseline_days"] * 2)
        if len(base) >= 2:
            avg = sum(base) / len(base)
            if today >= R["floor"] and today >= R["mult"] * avg:
                out.append(_cand("github", pid, day, "gh_stars", metric=R["label"], before=avg, after=today,
                                 basis="own-baseline", window=f"vs {len(base)} earlier trending days"))
        elif today >= R["cold_floor"]:
            out.append(_cand("github", pid, day, "gh_stars", metric=R["label"], before=None, after=today,
                             basis="cold-start", window=f"{len(base) + 1} trending day(s) in our data: too few for a baseline"))
    for c in out:
        c["strength"] = (math.log2(c["mult"]) if c["mult"] else 1.6) * math.log10(max(c["after"], 10)) / 2
    return out


def rule_minigames(con, day) -> list:
    R = CFG["rules"]["minigame_rank"]
    ranks = {(r["pid"], r["metric"][5:]): r["value"] for r in con.execute(
        "SELECT pid, metric, value FROM metrics WHERE source='minigame' AND day=? AND metric LIKE 'rank:%'", (day,))}
    best = {}
    for r in con.execute("SELECT pid, metric, value FROM metrics WHERE source='minigame' AND day=? AND "
                         "metric LIKE 'chg:%'", (day,)):
        board = r["metric"][4:]
        rank = ranks.get((r["pid"], board))
        if rank is None or r["value"] < R["min_jump"] or rank > R["max_rank"] or board.endswith("publisher_heat"):
            continue
        c = _cand("minigame", r["pid"], day, "minigame_rank", metric=R["label"], before=rank + r["value"], after=rank,
                  basis="source-delta", window="since yesterday", chart=f"rank:{board}")
        c["strength"] = math.log2((rank + r["value"]) / rank) * (1.3 if "bestseller" in board else 1.0) + 0.3
        if r["pid"] not in best or c["strength"] > best[r["pid"]]["strength"]:
            best[r["pid"]] = c
    return list(best.values())


def rule_drama(con, day) -> list:
    R, G = CFG["rules"]["drama_ads"], CFG["rules"]
    out = []
    created = _series(con, "drama_ad", "creatives")
    fresh = {pid: pts[-1][1] for pid, pts in _series(con, "drama_ad", "new_creatives").items() if pts[-1][0] == day}
    for pid, pts in created.items():
        if pts[-1][0] != day or (pts[-1][1] or 0) < R["floor"]:
            continue
        today = pts[-1][1]
        base = _baseline(pts[:-1], day, G["baseline_days"])
        if len(base) >= G["min_baseline_points"]:
            avg = sum(base) / len(base)
            if avg > 0 and today >= R["mult"] * avg:
                out.append(_cand("drama_ad", pid, day, "drama_ads", metric=R["label"], before=avg, after=today,
                                 basis="own-baseline", window=f"vs {len(base)}-day average", label="estimated"))
        elif fresh.get(pid, 0) >= R["fresh_share"] * today:
            out.append(_cand("drama_ad", pid, day, "drama_ads", metric=R["label"], before=None, after=today,
                             basis="cold-start", window=f"{int(fresh[pid]):,} of them new today", label="estimated"))
    C = CFG["rules"]["drama_chart"]
    rank = _series(con, "drama", "rank:tiktok")
    for pid, pts in rank.items():
        if pts[-1][0] != day or pts[-1][1] > C["max_rank"]:
            continue
        prev = [v for d, v in pts[:-1] if d >= (_d(day) - timedelta(days=3)).strftime("%Y-%m-%d")]
        if prev and prev[-1] <= pts[-1][1]:
            continue
        out.append(_cand("drama", pid, day, "drama_chart", metric=C["label"], before=prev[-1] if prev else None,
                         after=pts[-1][1], basis="own-baseline" if prev else "cold-start",
                         window="since last snapshot" if prev else "new to our snapshots"))
    for c in out:
        c["strength"] = (math.log2(c["mult"]) if c["mult"] else 1.2) * (math.log10(max(c["after"], 10)) / 2
                                                                       if c["rule"] == "drama_ads" else 1.0)
    return out


def rule_v2(con, day) -> list:
    """TrustMRR revenue climbs and Tranco traffic climbs, reusing the v2 signal logic."""
    out = []
    tm, web = _products(con, "trustmrr"), _products(con, "tranco")
    for s in trustmrr_signals(con, tm):
        c = _cand("trustmrr", s["pid"], day, "revenue", metric="MRR", before=s["before"], after=s["after"],
                  basis="own-baseline" if s.get("basis") == "our snapshots" else "source-delta",
                  window=s["window"], detail=s.get("basis", ""))
        c["strength"] = s.get("strength", 1.0)
        c["money"] = True
        out.append(c)
    for s in tranco_signals(con, web, tm):
        pid = s["pid"]
        src = "trustmrr" if pid.startswith("tm:") else "tranco"
        c = _cand(src, pid[3:] if src == "trustmrr" else pid, day, "web_traffic", metric="Web traffic rank",
                  before=s["before"], after=s["after"], basis="own-baseline" if s["before"] else "cold-start",
                  window=s["window"], detail=s.get("basis", ""))
        c["rank_metric"] = True
        c["strength"] = s.get("strength", 1.0) * 0.8
        out.append(c)
    return out


# ---------------------------------------------------------------- entity + scoring

def entity_of(c: dict, prods: dict) -> str:
    p = prods.get((c["source"], c["pid"])) or {}
    meta = p.get("meta") or {}
    if c["source"] in ("ios", "play") and meta.get("cluster_id"):
        return f"app-{meta['cluster_id']}"
    return f"{c['source']}-{c['pid']}".replace("/", "_").replace(":", "_")


def demand_echo(con, day: str) -> dict:
    """Direction -> 0..1 from buyer-intent Reddit threads in the last 14 days (+ XHS mentions via TinyFish)."""
    since = int((_d(day) - timedelta(days=14)).timestamp())
    counts = defaultdict(int)
    for r in con.execute("SELECT direction, COUNT(*) n FROM threads WHERE created_utc>=? GROUP BY direction", (since,)):
        counts[r["direction"]] = r["n"]
    top = max(counts.values()) if counts else 0
    return {k: min(1.0, v / max(8, top * 0.6)) for k, v in counts.items()}


def detect(con, day: str) -> list:
    cands = []
    cands += rule_cumulative(con, day, "play", "installs", "gp_installs")
    cands += rule_cumulative(con, day, "ios", "ratings", "ios_ratings")
    for src in ("ios", "play"):
        cands += rule_charts(con, day, src)
    cands += rule_github(con, day)
    cands += rule_minigames(con, day)
    cands += rule_drama(con, day)
    cands += rule_v2(con, day)

    prods = {}
    for src in {c["source"] for c in cands}:
        for pid, p in _products(con, src).items():
            prods[(src, pid)] = p
    echo = demand_echo(con, day)
    P = CFG["pick"]
    pub_size = defaultdict(int)
    for (src, _pid), p in prods.items():
        if src in ("ios", "play"):
            pub_size[(p.get("meta") or {}).get("company_id") or (p.get("meta") or {}).get("developer")] += 1
    recent = {r[0] for r in con.execute(
        "SELECT json_extract(json,'$.entity') FROM candidates WHERE picked=1 AND day>=? AND day<?",
        ((_d(day) - timedelta(days=14)).strftime("%Y-%m-%d"), day))}

    merged = {}
    for c in cands:
        p = prods.get((c["source"], c["pid"])) or {}
        meta = p.get("meta") or {}
        c["entity"] = entity_of(c, prods)
        c["name"] = p.get("name") or c["pid"]
        c["direction"] = p.get("direction") or "other"
        if c["source"] in ("minigame",):
            c["direction"] = "minigame"
        if c["source"] in ("drama", "drama_ad"):
            c["direction"] = "drama"
        if c.get("strength") is None:
            c["strength"] = (math.log2(c["mult"]) if c["mult"] else 1.0) * math.log10(max(c["after"] or 10, 10)) / 2
        pub = " ".join(str(meta.get(k) or "") for k in ("developer", "company", "publisher", "seller"))
        big = any(d.lower() in pub.lower() for d in P["deny_publishers"])
        size = pub_size.get(meta.get("company_id") or meta.get("developer"), 0)
        penalty = 0.15 if big else (0.35 if size >= P["big_publisher_apps"] else 1.0)
        fit = (BY_SLUG.get(c["direction"]) or {}).get("fit", 0.5)
        novelty = 0.0 if c["entity"] in recent else 1.0
        age = _age_days(meta.get("released"), day)
        c["age_days"] = age
        freshness = 1.0 if age is None else (1.3 if age <= 365 else (1.0 if age <= 3 * 365 else 0.55))
        c["echo"] = round(echo.get(c["direction"], 0.0), 2)
        c["big_publisher"] = big or size >= P["big_publisher_apps"]
        c["score"] = round(c["strength"] * penalty * freshness * (0.5 + fit) * (1 + c["echo"]) * (0.2 + 0.8 * novelty), 4)
        c["id"] = f"{day}-{c['entity']}"[:120]
        prev = merged.get(c["entity"])
        if prev is None or c["score"] > prev["score"]:
            if prev:
                c["also"] = prev.get("also", []) + [_brief(prev)]
            merged[c["entity"]] = c
        else:
            prev.setdefault("also", []).append(_brief(c))
    out = sorted(merged.values(), key=lambda c: -c["score"])
    _pick(out, P)
    return out


def _age_days(released, day: str):
    if not released or not isinstance(released, str):
        return None
    for fmt in ("%Y-%m-%d", "%b %d, %Y"):
        try:
            return (_d(day) - datetime.strptime(released[:12] if fmt != "%Y-%m-%d" else released[:10], fmt)).days
        except ValueError:
            continue
    return None


def _brief(c: dict) -> dict:
    return {k: c.get(k) for k in ("source", "pid", "rule", "metric", "before", "after", "mult", "chart", "basis")}


def _pick(cands: list, P: dict) -> None:
    budget = P["budget"]
    cap = max(1, int(budget * P["max_share_per_surface"]))
    per = defaultdict(int)
    picked = []
    # Unidentifiable products (TrustMRR "Anonymous startup") stay listed but can't be investigated.
    eligible = [c for c in cands if c["score"] > 0 and not c["big_publisher"]
                and not (c.get("name") or "").lower().startswith("anonymous")]
    for surf in SURFACE_NAME:  # floor: every surface that has something gets a voice
        for c in [x for x in eligible if x["surface"] == surf][: P["min_per_surface"]]:
            picked.append(c)
            per[surf] += 1
    for c in eligible:
        if len(picked) >= budget:
            break
        if c in picked or per[c["surface"]] >= cap:
            continue
        picked.append(c)
        per[c["surface"]] += 1
    ids = {id(c) for c in picked}
    for c in cands:
        c["picked"] = id(c) in ids


def save(con, day: str, cands: list) -> None:
    con.execute("DELETE FROM candidates WHERE day=?", (day,))
    for c in cands:
        con.execute("INSERT OR REPLACE INTO candidates(id,day,surface,source,pid,rule,score,picked,json) "
                    "VALUES(?,?,?,?,?,?,?,?,?)",
                    (c["id"], day, c["surface"], c["source"], c["pid"], c["rule"], c["score"],
                     1 if c["picked"] else 0, json.dumps(c, ensure_ascii=False, default=str)))
