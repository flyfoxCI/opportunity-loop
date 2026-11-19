"""Chrome Web Store extensions and Shopify App Store apps.

Chrome: each category page server-renders its first 32 items as a JS array (AF_initDataCallback). An item is
  [id, icon, name, rating, rating_count, banner, summary, website, _, _, _, [category, _, _], _, _, users, _, _,
   [published_unix, nanos], manifest, ...]
  We keep users, rating and rating count per day (users is rounded by the store), plus the publish date.
Shopify: each category page lists 40 app cards with rating, review count and the pricing line. The detail page
  carries "Launched <date>"; we fetch it once per app (capped per run). Reviews are the growth signal.
Both are HTML scrapes: a changed page layout yields zero rows and a logged failure, never a crash.
"""

from __future__ import annotations

import html
import json
import re
import time
from datetime import datetime, timezone

from .. import net
from ..store import log_source, put_metric, upsert_product
from ..taxonomy import classify

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
      "Accept-Language": "en-US,en;q=0.9"}

CHROME_CATS = ["productivity/communication", "productivity/developer", "productivity/education", "productivity/tools",
               "productivity/workflow", "lifestyle/art", "lifestyle/entertainment", "lifestyle/games", "lifestyle/household",
               "lifestyle/fun", "lifestyle/news", "lifestyle/shopping", "lifestyle/social", "lifestyle/travel",
               "lifestyle/well_being", "make_chrome_yours/accessibility", "make_chrome_yours/functionality",
               "make_chrome_yours/privacy"]
CHROME_NAME = {c: c.split("/")[1].replace("_", " ").title() for c in CHROME_CATS}
CHROME_NAME.update({"productivity/developer": "Developer tools", "lifestyle/well_being": "Well-being",
                    "make_chrome_yours/functionality": "Functionality & UI", "productivity/tools": "Tools"})

SHOPIFY_CATS = ["finding-products", "finding-products-sourcing-options-dropshipping", "marketing-and-conversion",
                "marketing-and-conversion-advertising", "marketing-and-conversion-checkout",
                "marketing-and-conversion-customer-loyalty", "marketing-and-conversion-gifts",
                "marketing-and-conversion-marketing", "marketing-and-conversion-marketing-email-marketing",
                "marketing-and-conversion-promotions", "marketing-and-conversion-social-trust",
                "marketing-and-conversion-upsell-and-bundles", "orders-and-shipping", "sales-channels", "selling-products",
                "store-design", "store-management", "store-management-support"]


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _log(msg: str) -> None:
    print(f"[radar] {msg}", flush=True)


def _page(url: str) -> str:
    return net.get(url, as_json=False, headers=UA, retries=2, backoff=8.0)


# ---------------------------------------------------------------- Chrome Web Store

def parse_chrome(page: str) -> list:
    dec, out, seen = json.JSONDecoder(), [], set()
    for m in re.finditer(r'\["([a-p]{32})","https', page):
        if m.group(1) in seen:
            continue
        try:
            a, _ = dec.raw_decode(page, m.start())
        except ValueError:
            continue
        if len(a) < 18 or not isinstance(a[2], str):
            continue
        seen.add(a[0])
        pub = a[17][0] if isinstance(a[17], list) and a[17] and isinstance(a[17][0], (int, float)) else None
        out.append({"id": a[0], "icon": a[1], "name": a[2], "rating": a[3], "ratings": a[4], "summary": a[6] or "",
                    "website": a[7] or "", "category": (a[11] or [None])[0] if isinstance(a[11], list) else None,
                    "users": a[14] if isinstance(a[14], (int, float)) else None,
                    "published": datetime.fromtimestamp(pub, timezone.utc).strftime("%Y-%m-%d") if pub else None})
    return out


def collect_chrome(con, day: str | None = None, cfg: dict | None = None) -> int:
    day = day or _today()
    cfg = cfg or {}
    rows, errors = 0, []
    for cat in cfg.get("categories", CHROME_CATS):
        try:
            items = parse_chrome(_page(f"https://chromewebstore.google.com/category/extensions/{cat}"))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{cat}: {e}")
            continue
        for pos, it in enumerate(items, 1):
            direction, conf = classify(it["name"], it["summary"], CHROME_NAME.get(cat, ""))
            slug = re.sub(r"[^a-z0-9]+", "-", it["name"].lower()).strip("-")[:40] or "x"
            upsert_product(con, "chrome", it["id"], day, name=it["name"],
                           url=f"https://chromewebstore.google.com/detail/{slug}/{it['id']}",
                           description=it["summary"][:600], category=CHROME_NAME.get(cat, cat),
                           direction=direction, direction_conf=conf,
                           meta={"icon": it["icon"], "website": it["website"], "released": it["published"],
                                 "store_category": cat})
            put_metric(con, "chrome", it["id"], "users", day, it["users"])
            put_metric(con, "chrome", it["id"], "rating", day, it["rating"])
            put_metric(con, "chrome", it["id"], "ratings", day, it["ratings"])
            put_metric(con, "chrome", it["id"], f"rank:cws:{cat}", day, pos)
            rows += 1
        time.sleep(cfg.get("pace", 1.5))
    _log(f"chrome: {rows} extension rows, {len(errors)} errors")
    log_source(con, "chrome", day, rows > 0, rows, "; ".join(errors)[:500])
    return rows


# ---------------------------------------------------------------- Shopify App Store

CARD = re.compile(r'data-app-card-handle-value="([^"]+)"\s+data-app-card-name-value="([^"]*)"\s+'
                  r'data-app-card-icon-url-value="([^"]*)"')


def parse_shopify(page: str) -> list:
    out, starts = [], [m for m in CARD.finditer(page)]
    for i, m in enumerate(starts):
        a = page.find(">", m.end()) + 1
        chunk = page[a: starts[i + 1].start() if i + 1 < len(starts) else a + 6000]
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " | ", chunk)))
        rating = re.search(r"\| ([0-5]\.\d) \| out of 5 stars", text)
        reviews = re.search(r"([\d,]+) total reviews", text)
        parts = [p.strip() for p in text.split("|") if p.strip()]
        price, blurb = "", ""
        for j, p in enumerate(parts):
            if p == "•" and j + 1 < len(parts):
                price = parts[j + 1]
                blurb = parts[j + 2] if j + 2 < len(parts) and parts[j + 2] != "•" else ""
                break
        out.append({"handle": m.group(1), "name": html.unescape(m.group(2)), "icon": m.group(3),
                    "rating": float(rating.group(1)) if rating else None,
                    "reviews": int(reviews.group(1).replace(",", "")) if reviews else 0,
                    "price": price, "blurb": blurb, "bfs": "Built for Shopify" in text})
    return out


def shopify_launched(handle: str) -> str | None:
    t = _page(f"https://apps.shopify.com/{handle}")
    m = re.search(r"Launched\s+([A-Z][a-z]+ \d{1,2}, \d{4})", re.sub(r"<[^>]+>", " ", t))
    return datetime.strptime(m.group(1), "%B %d, %Y").strftime("%Y-%m-%d") if m else None


def collect_shopify(con, day: str | None = None, cfg: dict | None = None) -> int:
    day = day or _today()
    cfg = cfg or {}
    rows, errors, need = 0, [], []
    for cat in cfg.get("categories", SHOPIFY_CATS):
        try:
            items = parse_shopify(_page(f"https://apps.shopify.com/categories/{cat}"))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{cat}: {e}")
            time.sleep(10)
            continue
        cname = cat.replace("-", " ").replace("and", "&").capitalize()
        for pos, it in enumerate(items, 1):
            row = con.execute("SELECT meta FROM products WHERE source='shopify' AND pid=?", (it["handle"],)).fetchone()
            old = json.loads(row["meta"]) if row and row["meta"] else {}
            direction, conf = classify(it["name"], it["blurb"], "ecommerce shopify store")
            old.update({"icon": it["icon"], "price": it["price"], "bfs": it["bfs"],
                        "store_category": old.get("store_category") or cat})
            upsert_product(con, "shopify", it["handle"], day, name=it["name"], url=f"https://apps.shopify.com/{it['handle']}",
                           description=it["blurb"][:600], category=cname,
                           direction=direction if direction != "other" else "ecommerce", direction_conf=conf, meta=old)
            put_metric(con, "shopify", it["handle"], "reviews", day, it["reviews"])
            put_metric(con, "shopify", it["handle"], "rating", day, it["rating"])
            put_metric(con, "shopify", it["handle"], f"rank:shop:{cat}", day, pos)
            if not old.get("released") and it["handle"] not in need:
                need.append(it["handle"])
            rows += 1
        time.sleep(cfg.get("pace", 3.0))
    got = 0
    for h in need[: cfg.get("detail_max", 100)]:
        try:
            when = shopify_launched(h)
        except Exception as e:  # noqa: BLE001
            errors.append(f"detail {h}: {e}")
            time.sleep(10)
            continue
        if when:
            row = con.execute("SELECT meta FROM products WHERE source='shopify' AND pid=?", (h,)).fetchone()
            meta = json.loads(row["meta"] or "{}")
            meta["released"] = when
            con.execute("UPDATE products SET meta=? WHERE source='shopify' AND pid=?", (json.dumps(meta), h))
            got += 1
        time.sleep(cfg.get("pace", 3.0))
    _log(f"shopify: {rows} app rows, {got} launch dates, {len(errors)} errors")
    log_source(con, "shopify", day, rows > 0, rows, "; ".join(errors)[:500])
    return rows
