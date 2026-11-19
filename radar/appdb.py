"""App DB (v4): every product we can put a monthly-revenue number on, and the four Stringers-style lenses.

Revenue is ESTIMATED for store apps and Shopify apps, VERIFIED for TrustMRR SaaS:
  App Store / Google Play  grossing rank -> daily revenue by a power law per country (top-grossing curves are
                           roughly rev ~ rank^-0.9), summed over the 15 countries we track, x30. A category chart is
                           scaled down from the overall chart; games categories are bigger than tool categories.
                           Countries we don't track add nothing, so most apps are UNDER-estimated. Range: x0.4-x2.5.
  Shopify                  reviews x 25 installs per review x paying share x list price (default $20/month).
  TrustMRR                 MRR as reported by the payment provider.
Chrome extensions get users, not revenue: the store publishes no money signal.

Lenses (what Stringers' appdb tabs ask):
  followed   launched within ~13 months, earns >= $10k/mo, and at least one similar product by another developer
             also earns: the idea was copied and the copies made money too
  unique     same bar, but nothing similar earns yet: an angle nobody has followed
  m3_10k     launched in the last 92 days, earns >= $10k/mo
  y_100k     launched this calendar year, earns >= $100k/mo
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime

from .taxonomy import BY_SLUG, GAME_GENRES

# share of US iOS revenue a country's App Store makes (rough public-market sizes)
COUNTRY_W = {"us": 1.0, "jp": .55, "kr": .18, "gb": .13, "de": .13, "ca": .08, "fr": .08, "au": .08, "tw": .07,
             "br": .035, "sa": .03, "mx": .025, "in": .015, "id": .015, "tr": .012}
# Google Play revenue relative to the App Store in the same country
PLAY_W = {"us": .5, "jp": .6, "kr": 1.6, "gb": .5, "de": .8, "ca": .5, "fr": .7, "au": .5, "tw": .7, "br": 1.5,
          "sa": .8, "mx": 1.2, "in": 2.5, "id": 2.0, "tr": 1.5}
US_TOP1_DAY = 1_200_000      # US iPhone top-grossing #1, all apps, per day
CAT_K = {"game": 0.30, "app": 0.05}  # a category chart's #1 relative to the overall #1
SLOPE = 0.92
COUNTRY_NAME = {"us": "US", "jp": "JP", "kr": "KR", "gb": "UK", "de": "DE", "ca": "CA", "fr": "FR", "au": "AU",
                "tw": "TW", "br": "BR", "sa": "SA", "mx": "MX", "in": "IN", "id": "ID", "tr": "TR"}
LENSES = {
    "followed": ("Others followed, and made money too", "Launched in the last year, earns over $10k a month, and "
                 "similar products from other developers earn as well: the idea was copied and the copies paid."),
    "unique": ("A unique angle, nobody followed yet", "Launched in the last year, earns over $10k a month, and "
               "nothing similar earns yet: an angle still open."),
    "m3_10k": ("Launched 3 months ago, $10k+/month", "Launched in the last 92 days and already estimated at over "
               "$10k a month."),
    "y_100k": ("Launched this year, $100k+/month", "Launched this calendar year and estimated at over $100k a month."),
}
SURFACE_OF = {"ios": "apps", "play": "apps", "trustmrr": "saas", "shopify": "shopify", "chrome": "chrome"}
STOP = set("app apps free your with from that this best easy smart pro plus lite the and for video photo photos "
           "editor maker tracker manager guide mobile online daily simple official new tool tools ai product products store "
           "shop shopify order orders sales sell customer customers chrome extension browser google page".split())


def _day(con) -> str:
    return con.execute("SELECT MAX(day) FROM metrics WHERE metric LIKE 'rank:grossing:%'").fetchone()[0] or \
        con.execute("SELECT MAX(day) FROM metrics").fetchone()[0]


def _released(meta: dict) -> str | None:
    r = meta.get("released") or meta.get("foundedDate")
    if not r:
        return None
    r = str(r)[:10] if re.match(r"\d{4}-\d{2}-\d{2}", str(r)) else str(r)
    for fmt in ("%Y-%m-%d", "%b %d, %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(r, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def rank_rev_day(rank: float, country: str, genre: int, play: bool) -> float:
    if rank is None or rank < 1:
        return 0.0
    base = US_TOP1_DAY * (1 if genre == 36 else CAT_K["game" if genre in GAME_GENRES else "app"])
    v = base * rank ** -SLOPE * COUNTRY_W.get(country, 0.01)
    return v * (PLAY_W.get(country, .6) if play else 1.0)


def store_estimates(con, day: str) -> dict:
    """(source, pid) -> {usd, basis, regions, best_rank, chg} from today's grossing charts."""
    per = defaultdict(lambda: defaultdict(float))
    best = {}
    chg = {}
    for r in con.execute("SELECT source, pid, metric, value FROM metrics WHERE day=? AND source IN ('ios','play') "
                         "AND metric LIKE 'rank:grossing:%'", (day,)):
        _, _, cc, g = r["metric"].split(":")
        g = int(g)
        v = rank_rev_day(r["value"], cc, g, r["source"] == "play")
        k = (r["source"], r["pid"])
        if v > per[k][cc]:
            per[k][cc] = v
        score = (r["value"] if g == 36 else r["value"] * 3) / max(COUNTRY_W.get(cc, .01), .01) ** .5
        if k not in best or score < best[k][0]:
            best[k] = (score, cc, g, int(r["value"]))
    for r in con.execute("SELECT source, pid, metric, value FROM metrics WHERE day=? AND source IN ('ios','play') "
                         "AND metric LIKE 'chg:grossing:%'", (day,)):
        k = (r["source"], r["pid"])
        chg[k] = max(chg.get(k, 0), r["value"] or 0)
    from .feeds.appark import GENRES
    out = {}
    for k, cs in per.items():
        _, cc, g, rk = best[k]
        out[k] = {"usd": sum(cs.values()) * 30, "regions": len(cs), "chg": chg.get(k, 0),
                  "basis": f"{COUNTRY_NAME.get(cc, cc.upper())} Top Grossing{'' if g == 36 else ' · ' + GENRES.get(g, str(g))} #{rk}"}
    return out


def _latest(con, source: str, metric: str) -> dict:
    return {r["pid"]: r["value"] for r in con.execute(
        "SELECT m.pid, m.value FROM metrics m JOIN (SELECT pid, MAX(day) d FROM metrics WHERE source=? AND metric=? "
        "GROUP BY pid) x ON x.pid=m.pid AND x.d=m.day WHERE m.source=? AND m.metric=?", (source, metric, source, metric))}


def _price(s: str) -> float | None:
    m = re.search(r"\$\s?([\d.]+)", s or "")
    return float(m.group(1)) if m else None


def _tokens(name: str) -> set:
    return {w for w in re.findall(r"[a-z]{4,}", (name or "").lower()) if w not in STOP}


def universe(con, day: str | None = None) -> list:
    """All products with a money number (or users, for Chrome), merged across iOS/Android twins."""
    day = day or _day(con)
    today = datetime.strptime(day, "%Y-%m-%d")
    est = store_estimates(con, day)
    rows = {}
    prods = {}
    keys = list(est)
    mrr = _latest(con, "trustmrr", "mrr")
    reviews = _latest(con, "shopify", "reviews")
    users = _latest(con, "chrome", "users")
    keys += [("trustmrr", p) for p, v in mrr.items() if v]
    keys += [("shopify", p) for p, v in reviews.items() if v]
    keys += [("chrome", p) for p, v in users.items() if v]
    for src in ("ios", "play", "trustmrr", "shopify", "chrome"):
        want = {p for s, p in keys if s == src}
        if not want:
            continue
        for r in con.execute(f"SELECT * FROM products WHERE source=? AND pid IN ({','.join('?' * len(want))})",
                             (src, *want)):
            prods[(src, r["pid"])] = r
    for k in keys:
        p = prods.get(k)
        if not p:
            continue
        src, pid = k
        meta = json.loads(p["meta"] or "{}")
        rel = _released(meta)
        row = {"source": src, "pid": pid, "name": p["name"] or pid, "url": p["url"], "icon": meta.get("icon"),
               "developer": meta.get("developer") or meta.get("company") or "", "released": rel,
               "age_days": (today - datetime.strptime(rel, "%Y-%m-%d")).days if rel else None,
               "direction": p["direction"] or "other",
               "desc": "" if (p["description"] or "").lstrip().startswith("<") else (p["description"] or "").strip().split("\n")[0][:160],
               "genre": (meta.get("genres") or [None])[0] if src in ("ios", "play") else meta.get("store_category"), "category": p["category"] or meta.get("genre") or "",
               "surface": SURFACE_OF[src], "platforms": [src], "usd": None, "label": "estimated", "basis": "",
               "chg": 0, "users": None, "model": "", "price": meta.get("price") or ""}
        if src in ("ios", "play"):
            e = est[k]
            row.update(usd=e["usd"], basis=e["basis"], chg=e["chg"], regions=e["regions"])
            row["model"] = "in-app purchases" if meta.get("iap") else ("paid upfront" if row["price"] and
                                                                         row["price"] not in ("Free", "0") else "")
        elif src == "trustmrr":
            row.update(usd=mrr[pid], label="verified", basis="MRR, payment-verified", model="subscription",
                       developer=meta.get("xHandle") and "@" + meta["xHandle"] or "")
        elif src == "shopify":
            n = reviews[pid] or 0
            pr = meta.get("price") or ""
            if n >= 20 and pr.strip().lower() != "free":
                share = 0.35 if "free" in pr.lower() else 0.8
                row.update(usd=n * 25 * share * (_price(pr) or 20.0), basis=f"{int(n):,} reviews · {pr}")
            row["model"] = pr
        elif src == "chrome":
            row.update(users=users[pid], basis=f"{int(users[pid]):,} users", label="verified")
        cid = meta.get("cluster_id")
        mk = ("c", cid) if cid and src in ("ios", "play") else k
        if mk in rows:  # the Android twin of an iOS app: add its money, keep the better row's text
            o = rows[mk]
            o["usd"] = (o["usd"] or 0) + (row["usd"] or 0)
            o["platforms"] = sorted(set(o["platforms"] + row["platforms"]), key=lambda s: s != "ios")
            if row["released"] and (not o["released"] or row["released"] < o["released"]):
                o["released"], o["age_days"] = row["released"], row["age_days"]
            o["chg"] = max(o["chg"], row["chg"])
        else:
            rows[mk] = row
    out = list(rows.values())
    for r in out:
        r["direction_name"] = (BY_SLUG.get(r["direction"]) or {}).get("name", "Other")
        r["tokens"] = _tokens(r["name"])
        r["dtokens"] = _tokens(r["desc"]) - r["tokens"]
    # the same app listed under two store ids (regional re-listings): keep the bigger one
    seen = {}
    for r in sorted(out, key=lambda r: -(r["usd"] or r["users"] or 0)):
        k = (re.sub(r"\W+", "", r["name"].lower())[:16], r["developer"])
        if k in seen:
            o = seen[k]
            o["usd"] = (o["usd"] or 0) + (r["usd"] or 0) if o["usd"] is not None else r["usd"]
            continue
        seen[k] = r
    return list(seen.values())


def _similar(a: dict, b: dict) -> bool:
    if a["developer"] and a["developer"] == b["developer"]:
        return False
    if a["surface"] != b["surface"] and not {a["surface"], b["surface"]} <= {"apps", "saas"}:
        return False
    if re.sub(r"\W+", "", a["name"].lower())[:8] == re.sub(r"\W+", "", b["name"].lower())[:8]:
        return False  # a twin listing, not a follower
    same_lane = (a["direction"] not in ("other", "mobile-games") and a["direction"] == b["direction"]) or \
        (a["genre"] is not None and a["genre"] == b["genre"])
    if not same_lane:
        return False
    name_hit = a["tokens"] & (b["tokens"] | b["dtokens"]) or b["tokens"] & a["dtokens"]
    return bool(name_hit) or len(a["dtokens"] & b["dtokens"]) >= 4


def solo_fit(rows: list) -> list:
    """Drop games and big publishers: the lenses are for one or two builders, as on Stringers."""
    from .detect import CFG
    deny = [d.lower() for d in CFG["pick"].get("deny_publishers", [])]
    size = defaultdict(int)
    for r in rows:
        if r["developer"]:
            size[r["developer"]] += 1
    big_n = CFG["pick"].get("big_publisher_apps", 8)
    return [r for r in rows if r["direction"] != "mobile-games" and r["genre"] not in GAME_GENRES
            and not any(d in (r["developer"] or "").lower() for d in deny) and size[r["developer"]] < big_n]


def lenses(rows: list, day: str) -> dict:
    """lens -> rows (sorted by money), each row gets 'followers': similar earners (top 3) and n_followers."""
    year = day[:4]
    rows = solo_fit(rows)
    earners = [r for r in rows if (r["usd"] or 0) >= 2_000]
    by_dir = defaultdict(list)
    for r in earners:
        by_dir[r["direction"]].append(r)
        by_dir["g:" + str(r["genre"])].append(r)
    for r in rows:
        if (r["usd"] or 0) < 10_000:
            r["followers"], r["n_followers"] = [], 0
            continue
        pool = {id(x): x for x in by_dir[r["direction"]] + by_dir["g:" + str(r["genre"])]}.values()
        f = sorted((x for x in pool if x is not r and _similar(r, x)), key=lambda x: -(x["usd"] or 0))
        r["followers"], r["n_followers"] = f[:3], len(f)
    young = [r for r in rows if r["age_days"] is not None and r["age_days"] <= 400 and (r["usd"] or 0) >= 10_000]
    out = {
        "followed": [r for r in young if r["n_followers"]],
        "unique": [r for r in young if not r["n_followers"]],
        "m3_10k": [r for r in rows if r["age_days"] is not None and r["age_days"] <= 92 and (r["usd"] or 0) >= 10_000],
        "y_100k": [r for r in rows if (r["released"] or "") >= f"{year}-01-01" and (r["usd"] or 0) >= 100_000],
    }
    for k in out:
        out[k].sort(key=lambda r: -(r["usd"] or 0))
    return out


def by_lane(rows: list, surface: str | None = None) -> list:
    """Directions ranked by how many products launched in the last year earn >= $10k/mo."""
    agg = defaultdict(lambda: {"new_10k": 0, "total": 0, "usd": 0.0, "examples": []})
    for r in rows:
        if surface and r["surface"] != surface:
            continue
        a = agg[r["direction"]]
        a["total"] += 1
        a["usd"] += r["usd"] or 0
        if (r["usd"] or 0) >= 10_000 and r["age_days"] is not None and r["age_days"] <= 400:
            a["new_10k"] += 1
            a["examples"].append(r)
    out = []
    for d, a in agg.items():
        a["examples"].sort(key=lambda r: -(r["usd"] or 0))
        out.append({"slug": d, "name": (BY_SLUG.get(d) or {}).get("name", "Other"), **a})
    return sorted(out, key=lambda x: (-x["new_10k"], -x["usd"]))
