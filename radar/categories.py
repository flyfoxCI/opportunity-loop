"""Category deep dives (v4): one page per surface (apps, mini-games, web & SaaS, Chrome extensions, Shopify apps).

Each surface gets
  stats     computed from our data: KPIs, lanes where NEW products earn, how they charge, who launched recently
  guidance  where to look (direction), how products here get users (growth), how they charge (money), and what one
            or two people should build / avoid. Written by the LLM from the stats + the week's briefs when a key is
            set (data/categories.json, refreshed daily); otherwise derived from the stats by rules.
"""

from __future__ import annotations

import json
import os
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

from . import appdb, synth
from .taxonomy import BY_SLUG

PATH = Path(__file__).resolve().parents[1] / "data" / "categories.json"
SURFACES = {
    "apps": ("Apps", "iOS and Google Play apps, games excluded from the money lenses"),
    "minigames": ("Mini-programs & mini-games", "WeChat and Douyin mini-games (Gravity Engine boards)"),
    "saas": ("Web & SaaS", "indie web products with payment-verified MRR (TrustMRR)"),
    "chrome": ("Chrome extensions", "Chrome Web Store, 18 categories"),
    "shopify": ("Shopify apps", "Shopify App Store, 18 categories"),
}


def fusd(v) -> str:
    if v is None:
        return "–"
    v = float(v)
    for lim, suf in ((1e6, "M"), (1e3, "k")):
        if abs(v) >= lim:
            return f"${v / lim:.1f}{suf}".replace(".0" + suf, suf)
    return f"${v:,.0f}"


def _row(r: dict) -> dict:
    keep = ("name", "url", "icon", "developer", "released", "age_days", "usd", "label", "basis", "users",
            "direction", "direction_name", "platforms", "model", "price", "desc", "source", "pid")
    return {k: r.get(k) for k in keep}


def _briefs(con, day: str, surface: str) -> list:
    since = (datetime.strptime(day, "%Y-%m-%d") - timedelta(days=14)).strftime("%Y-%m-%d")
    return [r for r in synth.investigations(con) if r["surface"] == surface and r["day"] >= since]


def _moves(briefs: list) -> dict:
    out = defaultdict(list)
    for b in briefs:
        for p in b.get("plays") or []:
            out[p.get("category")].append({"product": b["product"].get("name"), "move": p.get("move"),
                                           "result": p.get("result"), "causality": p.get("causality")})
        if b.get("mechanism"):
            out["mechanism"].append(b["mechanism"])
    return out


def stats(con, day: str, rows: list) -> dict:
    out = {}
    since = (datetime.strptime(day, "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
    from .detect import CFG
    lab = {k: v.get("label", k) for k, v in CFG["rules"].items() if isinstance(v, dict)}
    moves = defaultdict(Counter)
    for r in con.execute("SELECT surface, rule FROM candidates WHERE day>? AND day<=?", (since, day)):
        moves[r["surface"]][lab.get(r["rule"], r["rule"])] += 1
    solo = appdb.solo_fit(rows)
    year = day[:4]
    # ---- apps
    apps = [r for r in solo if r["surface"] == "apps" and r["usd"]]
    young = [r for r in apps if r["age_days"] is not None and r["age_days"] <= 365]
    yearn = [r for r in young if r["usd"] >= 10_000]
    models = Counter(r["model"] or "free with ads / unknown" for r in yearn)
    ctry = Counter(r["basis"].split(" ")[0] for r in yearn if r["basis"])
    out["apps"] = {
        "kpis": [(f"{len(apps):,}", "non-game apps on a grossing chart today", ""),
                 (f"{len(yearn):,}", "launched in the last 12 months, est. $10k+/month", "estimated"),
                 (f"{sum(1 for r in yearn if r['usd'] >= 100_000):,}", "of them est. $100k+/month", "estimated"),
                 (fusd(statistics.median([r["usd"] for r in yearn])) if yearn else "–", "median est. month, newcomers", "")],
        "lanes": appdb.by_lane(solo, "apps")[:12],
        "models": [(k, v, v / max(1, len(yearn))) for k, v in models.most_common(4)],
        "markets": ctry.most_common(8),
        "top_new": sorted(young, key=lambda r: -r["usd"])[:12],
    }
    # ---- web & SaaS
    saas = [r for r in rows if r["surface"] == "saas" and r["usd"]]
    g30 = {r["pid"]: r["value"] for r in con.execute(
        "SELECT pid, value FROM metrics WHERE source='trustmrr' AND metric='growth_30d' AND day=(SELECT MAX(day) FROM "
        "metrics WHERE source='trustmrr')")}
    for r in saas:
        r["growth"] = g30.get(r["pid"])
    sy = [r for r in saas if (r["released"] or "") >= f"{int(year) - 1}-{day[5:]}"]
    out["saas"] = {
        "kpis": [(f"{len(saas):,}", "indie products with payment-verified MRR", "verified"),
                 (f"{sum(1 for r in saas if r['usd'] >= 10_000):,}", "earn $10k+ MRR", "verified"),
                 (f"{len(sy):,}", "founded in the last 12 months", ""),
                 (fusd(statistics.median([r["usd"] for r in saas])) if saas else "–", "median MRR", "verified")],
        "lanes": appdb.by_lane(saas, "saas")[:12],
        "growers": sorted([r for r in saas if (r.get("growth") or 0) > 0 and r["usd"] >= 500],
                          key=lambda r: -(r.get("growth") or 0))[:12],
        "top_new": sorted(sy, key=lambda r: -r["usd"])[:12],
    }
    # ---- Shopify
    shop = [r for r in rows if r["surface"] == "shopify"]
    price = Counter(("Free plan + paid" if "free" in (r["price"] or "").lower() and r["price"].lower() != "free"
                     else ("Free" if (r["price"] or "").lower() == "free" else "Paid only")) for r in shop)
    syoung = [r for r in shop if r["age_days"] is not None and r["age_days"] <= 365]
    out["shopify"] = {
        "kpis": [(f"{len(shop):,}", "apps tracked across 18 categories", ""),
                 (f"{sum(1 for r in shop if (r['usd'] or 0) >= 10_000):,}", "est. $10k+/month", "estimated"),
                 (f"{len(syoung):,}", "launched in the last 12 months (of those we dated)", ""),
                 (f"{price.get('Free plan + paid', 0) * 100 // max(1, len(shop))}%", "use a free plan + paid tiers", "")],
        "lanes": appdb.by_lane(shop, "shopify")[:10],
        "models": [(k, v, v / max(1, len(shop))) for k, v in price.most_common()],
        "top_new": sorted(syoung, key=lambda r: -(r["usd"] or 0))[:12],
        "top": sorted(shop, key=lambda r: -(r["usd"] or 0))[:12],
    }
    # ---- Chrome
    ch = [r for r in rows if r["surface"] == "chrome"]
    cyoung = [r for r in ch if r["age_days"] is not None and r["age_days"] <= 730]
    bycat = defaultdict(list)
    for r in ch:
        bycat[r["category"]].append(r)
    out["chrome"] = {
        "kpis": [(f"{len(ch):,}", "featured extensions tracked", ""),
                 (f"{sum(1 for r in ch if (r['users'] or 0) >= 1_000_000):,}", "with 1M+ users", "verified"),
                 (f"{len(cyoung):,}", "published in the last 2 years", ""),
                 (f"{statistics.median([r['users'] for r in cyoung]):,.0f}" if cyoung else "–", "median users, recent ones", "")],
        "cats": sorted(((k, len(v), sum(x["users"] or 0 for x in v), sum(1 for x in v if x["age_days"] is not None and
                                                                             x["age_days"] <= 730)) for k, v in bycat.items()),
                       key=lambda x: -x[3]),
        "top_new": sorted(cyoung, key=lambda r: -(r["users"] or 0))[:12],
    }
    # ---- mini-games
    boards = defaultdict(list)
    for r in con.execute("SELECT m.metric, m.value, p.name, p.category, p.meta, m.pid FROM metrics m JOIN products p ON "
                         "p.source=m.source AND p.pid=m.pid WHERE m.source='minigame' AND m.day=? AND m.metric LIKE "
                         "'rank:%' ORDER BY m.value", (day,)):
        boards[r["metric"]].append(r)
    cats = Counter()
    pubs = Counter()
    for ms in boards.values():
        for r in ms:
            cats[(r["category"] or "?").split(" / ")[0]] += 1
            pubs[json.loads(r["meta"] or "{}").get("publisher") or "?"] += 1
    first_mg = con.execute("SELECT MIN(day) FROM metrics WHERE source='minigame'").fetchone()[0] or day
    history_ok = (datetime.strptime(day, "%Y-%m-%d") - datetime.strptime(first_mg, "%Y-%m-%d")).days >= 7
    streak = {}
    for r in con.execute("SELECT pid, COUNT(DISTINCT day) n FROM metrics WHERE source='minigame' AND metric LIKE 'rank:%' "
                         "GROUP BY pid"):
        streak[r["pid"]] = r["n"]
    fresh = []
    for ms in boards.values():
        for r in ms:
            if history_ok and streak.get(r["pid"], 0) <= 3 and r["value"] <= 20:
                fresh.append({"name": r["name"], "category": r["category"], "rank": int(r["value"]),
                              "board": r["metric"][5:]})
    out["minigames"] = {
        "kpis": [(f"{sum(len(v) for v in boards.values()):,}", "chart slots on today's WeChat + Douyin boards", ""),
                 (f"{len({r['pid'] for v in boards.values() for r in v}):,}", "distinct games", ""),
                 (f"{len(fresh)}" if history_ok else "–", "in a top 20 after 3 days or less on our boards"
                  if history_ok else "newcomers: needs 7 days of boards", ""),
                 (f"{len(pubs)}", "publishers", "")],
        "genres": cats.most_common(10),
        "publishers": pubs.most_common(8),
        "fresh": fresh[:15],
    }
    for k in out:
        out[k]["moves"] = moves[k].most_common(4)
    return out


# ---------------------------------------------------------------- guidance

SYSTEM = """You are the editor of Opportunity Loop, a daily briefing for solo builders (one or two people, small budget).
You get one category's numbers (computed from store charts, payment-verified MRR or store listings) and the products we
investigated in it over the last two weeks, with the direction / growth / monetization moves each one made.

Write guidance, not a data summary. Every point must say what it means for a builder and cite the numbers or products it
rests on. Revenue for apps and Shopify apps is an ESTIMATE from rank or reviews: say "estimated" when you use it.
Return ONLY JSON:
{"headline": "one sentence: the most useful thing to know about this category right now",
 "summary": "2-3 sentences",
 "direction": [{"point": "where to look and why the gap is open now", "evidence": "numbers / product names"}],  (2-4)
 "growth": [{"point": "how products here actually get users", "evidence": "..."}],  (2-4)
 "money": [{"point": "how and when they charge, price shape", "evidence": "..."}],  (2-4)
 "solo": {"build": "one concrete thing to build this month", "avoid": "one trap", "first_week": ["step", "step", "step"]}}
Do not invent numbers or products that are not in the input."""


def _payload(surface: str, st: dict, briefs: list) -> dict:
    def slim(x):
        if isinstance(x, dict):
            return {k: slim(v) for k, v in x.items() if k not in ("icon", "url", "tokens", "dtokens", "followers", "examples")}
        if isinstance(x, (list, tuple)):
            return [slim(v) for v in x[:12]]
        return x
    lanes = [{"lane": l["name"], "new_10k": l["new_10k"], "total": l["total"], "examples": [
        f"{e['name']} ({fusd(e['usd'])})" for e in l["examples"][:3]]} for l in st.get("lanes", [])]
    return {"category": SURFACES[surface][0], "stats": slim({k: v for k, v in st.items() if k != "lanes"}), "lanes": lanes,
            "investigated": [{"product": b["product"].get("name"), "lesson": b["lesson_title"], "grade": b["grade"]["grade"],
                              "verdict": b.get("verdict") or b.get("what"), "plays": b.get("plays") or [],
                              "how_to_follow": b.get("how_to_follow") or (b.get("follow") or {}).get("wedge")}
                             for b in briefs[:20]]}


def _rules(surface: str, st: dict, briefs: list) -> dict:
    lanes = [l for l in st.get("lanes", []) if l["slug"] != "other" and (l["new_10k"] or l["total"])][:3]
    mv = _moves(briefs)
    direction = [{"point": f"{l['name']}: {l['new_10k']} products launched in the last year earn $10k+/month (estimated)",
                  "evidence": ", ".join(f"{e['name']} {fusd(e['usd'])}" for e in l["examples"][:3])} for l in lanes if l["new_10k"]]
    growth = [{"point": m.get("move") or "", "evidence": f"{m.get('product')}: {m.get('result') or ''}"}
              for m in mv.get("growth", [])[:3] if m.get("move")]
    if not growth and st.get("moves"):
        tot = sum(n for _, n in st["moves"]) or 1
        growth = [{"point": f"{k}: {n} products crossed this line in the last 7 days",
                   "evidence": f"{n * 100 // tot}% of this category's detected moves"} for k, n in st["moves"][:3]]
    if not growth and mv.get("mechanism"):
        c = Counter(mv["mechanism"]).most_common(3)
        growth = [{"point": f"Most recent breakouts here came from: {k}", "evidence": f"{n} of {len(briefs)} briefs"} for k, n in c]
    money = [{"point": m.get("move") or "", "evidence": f"{m.get('product')}: {m.get('result') or ''}"}
             for m in mv.get("monetization", [])[:3] if m.get("move")]
    if not money and st.get("models"):
        money = [{"point": f"{k}: {v} of the products counted", "evidence": f"{share * 100:.0f}% of them"}
                 for k, v, share in st["models"][:3]]
    top = (st.get("top_new") or [None])[0]
    head = (f"{lanes[0]['name']} is where newcomers make money: {lanes[0]['new_10k']} products launched in the last "
            f"year earn $10k+/month" if lanes and lanes[0]["new_10k"] else
            f"{SURFACES[surface][0]}: {st['kpis'][0][0]} {st['kpis'][0][1]}")
    return {"headline": head, "summary": "Written from the numbers by rules: the agent analysis replaces this once its "
                                         "LLM key is configured.",
            "direction": direction, "growth": growth, "money": money,
            "solo": {"build": (f"A narrower or localized take on {top['name']} ("
                               + (fusd(top['usd']) + "/month, estimated" if top.get('usd') else f"{int(top.get('users') or 0):,} users")
                               + ")" if isinstance(top, dict) and top.get("name") else ""),
                     "avoid": "Lanes where the top earners are big publishers: they win on ad budget, not product.",
                     "first_week": []},
            "by": "rules"}


def analyze(con, day: str | None = None) -> dict:
    day = day or appdb._day(con)
    rows = appdb.universe(con, day)
    st = stats(con, day, rows)
    old = json.loads(PATH.read_text()) if PATH.exists() else {}
    out = {"updated": day, "surfaces": {}}
    client = None
    from .investigate import BASE_URL, agent_available
    if agent_available():
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("ANTHROPIC_API_KEY"),
                                     base_url=BASE_URL)
    for s in SURFACES:
        briefs = _briefs(con, day, s)
        g = None
        if client:
            try:
                from .playbook import _ask
                g = _ask(client, SYSTEM, _payload(s, st[s], briefs), 6000)
                g["by"] = "agent"
            except Exception as e:  # noqa: BLE001
                print(f"[radar] categories {s}: agent failed ({e}), using rules", flush=True)
        if not g:
            prev = (old.get("surfaces") or {}).get(s, {}).get("guidance")
            g = prev if prev and prev.get("by") == "agent" else _rules(s, st[s], briefs)
        out["surfaces"][s] = {"guidance": g}
    PATH.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str))
    return out


def load() -> dict:
    return json.loads(PATH.read_text()) if PATH.exists() else {"surfaces": {}}
