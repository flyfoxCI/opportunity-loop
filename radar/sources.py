"""Tier-1 (free) source fetchers. Each returns the number of rows written and never raises:
a failed source is logged to source_runs and the rest of the run carries on.

  trustmrr   verified MRR / subs / growth           (TrustMRR public API + historical run files)
  appstore   v2 only: Apple RSS charts (v3 uses radar/feeds/appark.py + stores.py)
  github     stars today on GitHub Trending          (HTML)
  reddit     buyer-intent threads per direction     (Arctic Shift search API)
  tranco     traffic rank of tracked sites + climbing tool domains (Tranco daily top 1M)
  xhs_web    Xiaohongshu 小工具 public posts via TinyFish search (inferred; CI only)
  trace      why-it-moved evidence for top spikes   (TinyFish CLI; CI only)
"""

from __future__ import annotations

import glob
from collections import defaultdict
import html
import json
import os
import re
import shutil
import subprocess
import time
from datetime import datetime, timedelta, timezone

from . import net
from .store import ROOT, get_product, log_source, put_metric, update_product, upsert_product, upsert_thread
from .taxonomy import BY_SLUG, DIRECTIONS, classify, classify_app

TRUSTMRR_API = "https://trustmrr.com/api/ai"
ARCTIC = "https://arctic-shift.photon-reddit.com/api"
APPLE_GENRES = {6000: "Business", 6002: "Utilities", 6005: "Social Networking", 6007: "Productivity",
                6008: "Photo & Video", 6011: "Music", 6012: "Lifestyle", 6013: "Health & Fitness",
                6015: "Finance", 6017: "Education", 6018: "Books", 6020: "Medical", 6023: "Food & Drink",
                6024: "Shopping", 6026: "Developer Tools", 6027: "Graphics & Design", 6003: "Travel"}


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _log(msg: str) -> None:
    print(f"[radar] {msg}", flush=True)


# ---------------------------------------------------------------- TrustMRR

def _ingest_trustmrr_payload(con, payload: dict, day: str) -> int:
    n = 0
    seen = set()
    for bucket in ("recentlyListedStartups", "bestDeals"):
        for s in payload.get(bucket) or []:
            slug = s.get("slug")
            if not slug or slug in seen:
                continue
            seen.add(slug)
            rev = s.get("revenue") or {}
            app = ((s.get("mobileApp") or {}).get("appStore")) or {}
            direction, conf = classify(s.get("name", ""), s.get("description", ""), s.get("category") or "")
            upsert_product(
                con, "trustmrr", slug, day, name=s.get("name") or slug, url=s.get("url") or "",
                description=(s.get("description") or "")[:600], category=s.get("category") or "",
                direction=direction, direction_conf=conf,
                meta={k: s.get(k) for k in ("website", "icon", "onSale", "askingPrice", "foundedDate", "targetAudience",
                                             "paymentProvider", "xHandle", "isMobileApp", "firstListedForSaleAt",
                                             "multiple", "stealthMode")},
            )
            put_metric(con, "trustmrr", slug, "mrr", day, rev.get("mrr"))
            put_metric(con, "trustmrr", slug, "last30", day, rev.get("last30Days"))
            put_metric(con, "trustmrr", slug, "subs", day, s.get("activeSubscriptions"))
            put_metric(con, "trustmrr", slug, "growth_mrr_30d", day, s.get("growthMRR30d"))
            put_metric(con, "trustmrr", slug, "growth_30d", day, s.get("growth30d"))
            put_metric(con, "trustmrr", slug, "asking_price", day, s.get("askingPrice"))
            put_metric(con, "trustmrr", slug, "rating_count", day, app.get("ratingCount"))
            n += 1
    return n


def backfill_trustmrr(con) -> int:
    """Load every historical trustmrr_raw.json under docs/runs and loop/runs."""
    files = sorted(set(glob.glob(str(ROOT / "docs/runs/*/trustmrr_raw.json")) +
                       glob.glob(str(ROOT / "loop/runs/*/trustmrr_raw.json"))))
    total = 0
    for f in files:
        run_id = os.path.basename(os.path.dirname(f))
        day = run_id[:10]
        try:
            total += _ingest_trustmrr_payload(con, json.load(open(f)), day)
        except Exception as e:  # noqa: BLE001
            _log(f"backfill skip {f}: {e}")
    _log(f"trustmrr backfill: {len(files)} snapshots, {total} rows")
    return total


def fetch_trustmrr(con) -> int:
    day = _today()
    try:
        n = _ingest_trustmrr_payload(con, net.get(TRUSTMRR_API, timeout=45), day)
        log_source(con, "trustmrr", day, n > 0, n, "" if n else "empty payload")
        return n
    except Exception as e:  # noqa: BLE001
        log_source(con, "trustmrr", day, False, 0, str(e))
        _log(f"trustmrr failed: {e}")
        return 0


# ---------------------------------------------------------------- App Store

def _chart(kind: str, genre: int | None, country: str, limit: int) -> list[dict]:
    g = f"/genre={genre}" if genre else ""
    data = net.get(f"https://itunes.apple.com/{country}/rss/{kind}/limit={limit}{g}/json")
    out = []
    for rank, e in enumerate((data.get("feed") or {}).get("entry") or [], start=1):
        try:
            out.append({
                "id": e["id"]["attributes"]["im:id"], "name": e["im:name"]["label"], "rank": rank,
                "summary": (e.get("summary") or {}).get("label", ""),
                "genre": (e.get("category") or {}).get("attributes", {}).get("label", ""),
                "url": e["id"]["label"],
            })
        except (KeyError, TypeError):
            continue
    return out


def fetch_appstore(con, country: str = "us", limit: int = 100) -> int:
    day = _today()
    genres = sorted({g for d in DIRECTIONS for g in d["genres"]})
    apps: dict[str, dict] = {}
    rows = 0
    errors = []
    for genre in genres:
        for kind, key in (("topgrossingapplications", "grossing"), ("topfreeapplications", "free")):
            try:
                for a in _chart(kind, genre, country, limit):
                    apps.setdefault(a["id"], a)
                    put_metric(con, "appstore", a["id"], f"rank_{key}", day, a["rank"])
                    a.setdefault("genre_id", genre)
                    rows += 1
            except Exception as e:  # noqa: BLE001
                errors.append(f"{kind}/{genre}: {e}")
            time.sleep(0.6)
    # Rating counts + release dates via Lookup (batched).
    ids = list(apps)
    for i in range(0, len(ids), 100):
        batch = ids[i:i + 100]
        try:
            res = net.get("https://itunes.apple.com/lookup", {"id": ",".join(batch), "country": country})
            for r in res.get("results", []):
                a = apps.get(str(r.get("trackId")))
                if a is not None:
                    a.update(rating_count=r.get("userRatingCount"), rating=r.get("averageUserRating"),
                             release=r.get("releaseDate"), price=r.get("price"), seller=r.get("sellerName"),
                             description=(r.get("description") or "")[:600], icon=r.get("artworkUrl100"),
                             url=r.get("trackViewUrl") or a["url"], genre=r.get("primaryGenreName") or a["genre"])
        except Exception as e:  # noqa: BLE001
            errors.append(f"lookup: {e}")
        time.sleep(1.0)
    for aid, a in apps.items():
        direction, conf = classify_app(a["name"], a.get("description") or a.get("summary", ""), a.get("genre_id"))
        upsert_product(con, "appstore", aid, day, name=a["name"], url=a.get("url", ""),
                       description=a.get("description") or a.get("summary", "")[:600], category=a.get("genre", ""),
                       direction=direction, direction_conf=conf,
                       meta={k: a.get(k) for k in ("release", "rating", "price", "seller", "icon", "genre_id")})
        put_metric(con, "appstore", aid, "rating_count", day, a.get("rating_count"))
    log_source(con, "appstore", day, rows > 0, rows, "; ".join(errors)[:500])
    _log(f"appstore: {len(apps)} apps, {rows} chart rows, {len(errors)} errors")
    return rows


# ---------------------------------------------------------------- GitHub Trending

_ROW = re.compile(r'<article class="Box-row">(.*?)</article>', re.S)
_REPO = re.compile(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', re.S)
_DESC = re.compile(r'<p class="col-9[^"]*">(.*?)</p>', re.S)
_TODAY = re.compile(r"([\d,]+) stars (?:today|this week)")
_TOTAL = re.compile(r'href="/[^"]+/stargazers"[^>]*>.*?([\d,]+)\s*</a>', re.S)


def fetch_github(con, languages=("", "python", "typescript")) -> int:
    day = _today()
    rows = 0
    try:
        for lang in languages:
            page = net.get(f"https://github.com/trending/{lang}", {"since": "daily"}, as_json=False)
            for block in _ROW.findall(page):
                m = _REPO.search(block)
                if not m:
                    continue
                repo = m.group(1).strip()
                dm = _DESC.search(block)
                desc = html.unescape(re.sub(r"<[^>]+>", "", dm.group(1))).strip() if dm else ""
                today = _TODAY.search(block)
                total = _TOTAL.search(block)
                direction, conf = classify(repo.split("/")[-1].replace("-", " "), desc)
                if direction == "other":
                    direction, conf = "devtools", 0.2
                upsert_product(con, "github", repo, day, name=repo, url=f"https://github.com/{repo}",
                               description=desc[:600], category=lang or "all", direction=direction, direction_conf=conf)
                put_metric(con, "github", repo, "stars_today", day, today.group(1).replace(",", "") if today else None)
                put_metric(con, "github", repo, "stars", day, total.group(1).replace(",", "") if total else None)
                rows += 1
            time.sleep(1.5)
        log_source(con, "github", day, rows > 0, rows)
    except Exception as e:  # noqa: BLE001
        log_source(con, "github", day, False, rows, str(e))
        _log(f"github failed: {e}")
    _log(f"github: {rows} trending rows")
    return rows


# ---------------------------------------------------------------- Reddit (Arctic Shift)

INTENT = re.compile(
    r"\b(looking for|recommend(ation)?s?|any (good )?(app|tool|software|alternative)s?|is there (an?|any) (app|tool|way|software)"
    r"|alternatives? to|switch(ed|ing)? from|what do you use|what (app|tool|software)s?|best (app|tool|software)"
    r"|would (you )?pay|willing to pay|hate (using|that app|this app)|too expensive|overpriced|cancel(led)? my subscription|"
    r"how do (you|i) (track|manage|find|keep|automate)|need (an? )?(app|tool|way to))\b", re.I)
# Builders promoting their own thing, or people hiring, are not buyers.
NOT_BUYER = re.compile(
    r"\b(i (built|made|created|launched|shipped)|we (built|launched|made)|just launched|my (app|tool|saas|startup|side project|product)|"
    r"our (app|tool|saas|product)|feedback on|roast my|beta testers?|waitlist|looking for (feedback|users|testers|a co-?founder|cofounder|"
    r"developers?|devs?|a developer|freelancers?|clients|work|a job|an? (job|internship))|hiring|\[for hire\]|\[hiring\]|promote)\b", re.I)
# Buyer intent also needs a product in view; "looking for advice" in a support subreddit is not demand.
PRODUCT = re.compile(r"\b(apps?|tools?|software|saas|platform|service|website|plugin|extension|subscription|"
                     r"spreadsheet|template|crm|program|solution|alternatives?|would pay|willing to pay)\b", re.I)


def fetch_reddit(con, days: int = 14, pages: int = 3, pace: float = 1.2) -> int:
    """Pull the newest posts of every direction subreddit (no server-side search: Arctic Shift's
    full-text search times out on big subreddits), detect buyer intent locally, and file each
    intent post under the direction it best matches. Demand = intent posts per week."""
    day = _today()
    floor = int((datetime.now(timezone.utc) - timedelta(days=days)).timestamp())
    owners: dict[str, list[dict]] = {}
    for d in DIRECTIONS:
        for sub in d["subreddits"]:
            owners.setdefault(sub, []).append(d)
    rows, errors = 0, []
    done_today = {r[0] for r in con.execute(
        "SELECT pid FROM metrics WHERE source='reddit_sub' AND metric='posts_scanned' AND day=?", (day,))}
    for sub, dirs in owners.items():
        if sub in done_today:  # resumable: a rerun the same day skips finished subreddits
            continue
        weekly_posts = {d["slug"]: 0.0 for d in dirs}
        weekly_comments = {d["slug"]: 0.0 for d in dirs}
        posts, before = [], None
        for _ in range(pages):
            params = {"subreddit": sub, "limit": 100, "sort": "desc",
                      "fields": "id,title,selftext,score,num_comments,created_utc,subreddit,author"}
            if before:
                params["before"] = before
            try:
                res = net.get(f"{ARCTIC}/posts/search", params, retries=3, backoff=8.0, timeout=60)
            except Exception as e:  # noqa: BLE001
                errors.append(f"{sub}: {e}")
                break
            batch = res.get("data") or []
            posts += batch
            time.sleep(pace)
            if len(batch) < 100 or batch[-1]["created_utc"] < floor:
                break
            before = batch[-1]["created_utc"]
        posts = [p for p in posts if p.get("created_utc", 0) >= floor]
        if not posts:
            put_metric(con, "reddit_sub", sub, "posts_scanned", day, 0)
            con.commit()
            continue
        span_days = max(1.0, (posts[0]["created_utc"] - posts[-1]["created_utc"]) / 86400)
        per_week = 7.0 / span_days
        hits = 0
        for p in posts:
            body = p.get("selftext") or ""
            if body in ("[removed]", "[deleted]"):
                body = ""
            text = f"{p.get('title', '')} {body[:1500]}"
            if (not (INTENT.search(text) and PRODUCT.search(text)) or NOT_BUYER.search(text)
                    or (p.get("title") or "").startswith(("[ Removed", "[Removed", "[deleted"))):
                continue
            # File under the owning direction with the most keyword hits; a subreddit that belongs
            # to a single direction keeps its intent posts even without a keyword hit.
            low = text.lower()
            scored = sorted(((sum(1 for kw in d["keywords"] if kw in low), d) for d in dirs), key=lambda x: -x[0])
            best_hits, best = scored[0]
            if best_hits == 0 and len(dirs) > 1:
                continue
            hits += 1
            weekly_posts[best["slug"]] += per_week
            weekly_comments[best["slug"]] += (p.get("num_comments") or 0) * per_week
            upsert_thread(con, {"id": p["id"], "direction": best["slug"], "subreddit": p.get("subreddit") or sub,
                                "title": p.get("title") or "", "body": body[:700], "score": p.get("score") or 0,
                                "num_comments": p.get("num_comments") or 0, "created_utc": p.get("created_utc") or 0,
                                "query": "intent", "first_seen": day, "author": p.get("author") or ""})
            rows += 1
        # Saved per subreddit so a crash or timeout keeps what was finished; analyze sums them.
        for slug in weekly_posts:
            put_metric(con, "reddit_sub", sub, f"intent_wk:{slug}", day, round(weekly_posts[slug], 2))
            put_metric(con, "reddit_sub", sub, f"comments_wk:{slug}", day, round(weekly_comments[slug], 1))
        put_metric(con, "reddit_sub", sub, "posts_scanned", day, len(posts))
        con.commit()
        _log(f"reddit r/{sub}: {len(posts)} posts over {span_days:.1f} days, {hits} intent")
    log_source(con, "reddit", day, rows > 0, rows, "; ".join(errors)[:500])
    _log(f"reddit: {rows} intent threads from {len(owners)} subreddits, {len(errors)} errors")
    return rows


def refilter_reddit(con, day: str) -> int:
    """Re-apply the current buyer filters to threads already stored for `day` and rescale each
    subreddit's weekly rate by what survives (rate per stored thread = original rate / count)."""
    removed = 0
    rows = con.execute("SELECT id, subreddit, direction, title, body, num_comments FROM threads WHERE first_seen=?", (day,)).fetchall()
    keep = defaultdict(list)
    drop = []
    for r in rows:
        text = f"{r['title']} {r['body'] or ''}"
        ok = (INTENT.search(text) and PRODUCT.search(text) and not NOT_BUYER.search(text)
              and not r["title"].startswith(("[ Removed", "[Removed", "[deleted")))
        (keep[(r["subreddit"], r["direction"])] if ok else drop).append(r)
    counts = defaultdict(int)
    for r in rows:
        counts[(r["subreddit"], r["direction"])] += 1
    for (sub, slug), n in counts.items():
        m = con.execute("SELECT value FROM metrics WHERE source='reddit_sub' AND pid=? AND metric=? AND day=?",
                        (sub, f"intent_wk:{slug}", day)).fetchone()
        if not m or not n:
            continue
        per_thread = (m[0] or 0) / n
        kept = keep.get((sub, slug), [])
        put_metric(con, "reddit_sub", sub, f"intent_wk:{slug}", day, round(per_thread * len(kept), 2))
        put_metric(con, "reddit_sub", sub, f"comments_wk:{slug}", day,
                   round(per_thread * sum(k["num_comments"] or 0 for k in kept), 1))
    for r in drop:
        con.execute("DELETE FROM threads WHERE id=?", (r["id"],))
        removed += 1
    con.execute("UPDATE source_runs SET rows=? WHERE source='reddit' AND day=?", (len(rows) - removed, day))
    con.commit()
    _log(f"reddit refilter {day}: dropped {removed} of {len(rows)} threads")
    return removed


# ---------------------------------------------------------------- Causal trace (TinyFish)

_URL = re.compile(r"https?://[^\s)\]>\"']+")


def trace_products(con, targets: list[dict], max_items: int = 12) -> int:
    """targets: [{source,pid,name,direction}] — the day's top spikes. Needs the tinyfish CLI + key."""
    if not shutil.which("tinyfish") or not os.environ.get("TINYFISH_API_KEY"):
        _log("trace: tinyfish CLI or TINYFISH_API_KEY missing — skipped (cards say 'trigger not checked')")
        return 0
    day = _today()
    rows = 0
    for t in targets[:max_items]:
        exists = con.execute("SELECT 1 FROM traces WHERE source=? AND pid=? AND day>=?",
                             (t["source"], t["pid"], (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%d"))).fetchone()
        if exists:
            continue
        name = re.sub(r"[:|\-–—].*$", "", t["name"]).strip() or t["name"]
        for q in (f'"{name}" app launch OR viral OR tiktok OR reddit OR "product hunt"', f'"{name}" review'):
            try:
                proc = subprocess.run(["tinyfish", "search", "query", "--pretty", q],
                                      capture_output=True, text=True, timeout=60)
            except Exception as e:  # noqa: BLE001
                _log(f"trace {name}: {e}")
                continue
            lines = [ln.strip() for ln in (proc.stdout or "").splitlines() if ln.strip()]
            for i, ln in enumerate(lines):
                for url in _URL.findall(ln):
                    title = lines[i - 1] if i > 0 and not _URL.search(lines[i - 1]) else ln
                    snippet = lines[i + 1] if i + 1 < len(lines) and not _URL.search(lines[i + 1]) else ""
                    con.execute("INSERT OR IGNORE INTO traces(source,pid,day,query,title,url,snippet) VALUES(?,?,?,?,?,?,?)",
                                (t["source"], t["pid"], day, q, title[:200], url[:500], snippet[:300]))
                    rows += 1
    _log(f"trace: {rows} evidence links")
    return rows


# ---------------------------------------------------------------- Tranco top 1M (web traffic)
# Tranco publishes a daily top-1M list (30-day average of 5 providers), so a 7-day rank change
# is a real traffic trend, not a one-day blip. Two uses:
#   1. traffic rank for products we already track (TrustMRR websites) -> verified MRR + traffic trend
#   2. discovery: climbing domains whose homepage reads like a tool/product in one of our directions
# Only the derived rows are stored; the 1M-row lists are fetched fresh each run (two ~22 MB CSVs).

TRANCO_API = "https://tranco-list.eu/api/lists/date/{}"
HOSTING = ("vercel.app", "netlify.app", "github.io", "notion.site", "carrd.co", "framer.website", "webflow.io",
           "bubbleapps.io", "pages.dev", "replit.app", "lovable.app", "apple.com", "google.com", "github.com",
           "chromewebstore.google.com", "producthunt.com", "gumroad.com", "wordpress.com", "wixsite.com", "shopify.com")
_TR_BAD = re.compile(r"(movie|film|satta|matka|toto|slot|bet|casino|sex|porn|xxx|xnhau|toon|manga|manhwa|anime|"
                     r"torrent|apk|iptv|stream|tvwiki|hentai|jav|dpboss|lottery|togel|gacor|judi|kasino|escort|"
                     r"onlyfans|leak|crack|warez|loan|pharma|viagra|dating|bokep|yadong|nude|cuevana|flix|novel)", re.I)
_TR_TOOL = re.compile(r"\b(tools?|generator|converter|maker|editor|calculator|checker|app|ai|online|free|software|"
                      r"platform|templates?|builder|tracker|planner|assistant|api|saas|extension|quiz|test|game|"
                      r"simulator)\b", re.I)
_TR_NOPE = re.compile(r"(casino|\bbet\b|slot|porn|sex|movie|watch .* online|streaming|loan|login|sign in|404|"
                      r"not found|forbidden|just a moment|attention required|parked|for sale|coming soon|index of|"
                      # local service businesses (local-SEO churn, not products)
                      r"contractor|roofing|roofer|plumb|electric(al|ian)|pest control|hvac|movers|cleaning service|"
                      r"law firm|lawyer|attorney|dentist|clinic|salon|restaurant|hotel|real estate agent|dealer|"
                      # gambling and number games common in IN/ID traffic churn
                      r"4d\b|situs|gacor|togel|fatafat|yono|rummy|teen patti|aviator|daman|tiranga|satta|matka|"
                      r"bayaran|result today|"
                      # shops and downloads
                      r"buy .* online|wholesale|products online|free download|download pc games|apk)", re.I)
_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
_DESC = re.compile(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', re.I)


def _registered_domain(url: str) -> str:
    host = re.sub(r"^[a-z]+://", "", (url or "").strip().lower()).split("/")[0].split(":")[0]
    host = host[4:] if host.startswith("www.") else host
    parts = host.split(".")
    if len(parts) >= 3 and parts[-2] in ("co", "com", "org", "net", "ac", "gov", "edu") and len(parts[-1]) == 2:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def _tranco_list(day: datetime) -> tuple[str, dict[str, int]]:
    """(list date, {domain: rank}) for the newest list on or before `day`."""
    for back in range(0, 4):
        d = (day - timedelta(days=back)).strftime("%Y-%m-%d")
        meta = net.get(TRANCO_API.format(d), retries=1)
        if meta.get("available") and meta.get("download"):
            body = net.get(meta["download"], as_json=False, timeout=180, retries=2)
            ranks = {}
            for line in body.splitlines():
                r, _, dom = line.partition(",")
                if dom:
                    ranks[dom.strip()] = int(r)
            return d, ranks
    raise RuntimeError(f"no Tranco list near {day:%Y-%m-%d}")


def _homepage(domain: str) -> tuple[str, str, str] | None:
    """(title, description, final host) or None. Reads at most 200 KB."""
    import urllib.request
    try:
        req = urllib.request.Request(f"https://{domain}/", headers={
            "User-Agent": "Mozilla/5.0 (compatible; opportunity-radar/2.0)", "Accept-Language": "en,zh;q=0.8"})
        with urllib.request.urlopen(req, timeout=8) as r:
            body = r.read(200_000).decode("utf-8", "replace")
            final = _registered_domain(r.geturl())
    except Exception:  # noqa: BLE001
        return None
    title = html.unescape((_TITLE.search(body) or [None, ""])[1]).strip()[:160]
    desc = html.unescape((_DESC.search(body) or [None, ""])[1]).strip()[:400]
    return title, desc, final


def fetch_tranco(con, max_rank: int = 500_000, min_factor: float = 2.0, max_checks: int = 600) -> int:
    from collections import Counter  # noqa: F811
    from concurrent.futures import ThreadPoolExecutor
    from .taxonomy import _scores
    day = _today()
    try:
        now_day, now = _tranco_list(datetime.now(timezone.utc) - timedelta(days=1))
        old_day, old = _tranco_list(datetime.strptime(now_day, "%Y-%m-%d").replace(tzinfo=timezone.utc) - timedelta(days=7))
    except Exception as e:  # noqa: BLE001
        log_source(con, "tranco", day, False, 0, str(e))
        _log(f"tranco failed: {e}")
        return 0
    rows = 0
    # 1. Traffic rank for products we already track. A domain shared by 2+ products is a host,
    #    and a top-2,000 domain is a platform, not the product's own traffic.
    sites = {}
    for r in con.execute("SELECT pid, meta FROM products WHERE source='trustmrr'").fetchall():
        dom = _registered_domain((json.loads(r["meta"] or "{}") or {}).get("website") or "")
        if dom and not any(dom.endswith(h) for h in HOSTING):
            sites[r["pid"]] = dom
    shared = {d for d, n in Counter(sites.values()).items() if n > 1}
    for pid, dom in sites.items():
        if dom in shared or now.get(dom, 0) < 2000:
            continue
        r = {"pid": pid}
        if dom in now:
            put_metric(con, "trustmrr", r["pid"], "tranco_rank", day, now[dom])
            put_metric(con, "trustmrr", r["pid"], "tranco_rank_7d", day, old.get(dom, 1_000_001))
            rows += 1
    # 2. Discovery: climbers that pass the homepage test.
    family = Counter(re.sub(r"\d+$", "", d.split(".")[0]) for d in now)
    cands = []
    for dom, rank in now.items():
        if rank > max_rank:
            continue
        before = old.get(dom, 1_000_001)
        if before / rank < min_factor:
            continue
        name = dom.split(".")[0]
        if (_TR_BAD.search(dom) or family[re.sub(r"\d+$", "", name)] >= 3 or re.search(r"\d{2,}", name)
                or dom.count(".") > 2 or len(name) < 3):
            continue  # domain-hopping clusters and the usual piracy/gambling churn
        cands.append((before / rank, dom, rank, before))
    cands.sort(reverse=True)
    cands = cands[:max_checks]
    known = {r[0] for r in con.execute(
        "SELECT pid FROM products WHERE source IN ('tranco','tranco_rejected') AND last_seen>=?",
        ((datetime.now(timezone.utc) - timedelta(days=21)).strftime("%Y-%m-%d"),))}
    to_check = [c for c in cands if c[1] not in known]
    with ThreadPoolExecutor(24) as ex:
        pages = dict(zip([c[1] for c in to_check], ex.map(_homepage, [c[1] for c in to_check])))
    kept = 0
    for factor, dom, rank, before in cands:
        if dom in pages:
            page = pages[dom]
            ok = False
            if page:
                title, desc, final = page
                text = f"{title} {desc}"
                sc = _scores(title, desc)
                best = max(sc.values()) if sc else 0
                ok = (bool(title) and final == dom and not _TR_NOPE.search(text)
                      and bool(_TR_TOOL.search(title)) and best >= 1)
            if not ok:
                upsert_product(con, "tranco_rejected", dom, day)
                continue
            direction, conf = classify(title, desc)
            upsert_product(con, "tranco", dom, day, name=title or dom, url=f"https://{dom}/", description=desc,
                           category="web", direction=direction, direction_conf=conf,
                           meta={"list_day": now_day, "base_day": old_day})
        elif get_product(con, "tranco", dom):
            update_product(con, "tranco", dom, last_seen=day)
        else:
            continue  # rejected within the last 21 days
        put_metric(con, "tranco", dom, "rank", day, rank)
        put_metric(con, "tranco", dom, "rank_7d", day, before)
        kept += 1
        rows += 1
    log_source(con, "tranco", day, True, rows, f"lists {old_day} -> {now_day}; {len(cands)} climbers, {kept} kept")
    _log(f"tranco {old_day}->{now_day}: {rows - kept} tracked sites ranked, {len(cands)} climbers, {kept} kept")
    return rows


# ---------------------------------------------------------------- Xiaohongshu 小工具 (TinyFish only)
# v3 keeps Xiaohongshu only where TinyFish can fetch it: public posts about 小工具 (inferred, CI only).
# The manual CSV import of the in-app boards was removed.


# Xiaohongshu: v3 reads it only through TinyFish (fetch_xhs_web). The manual CSV import was removed.


def fetch_xhs_web(con) -> int:
    """Public posts about 小工具 via TinyFish search. Inferred; CI only."""
    if not shutil.which("tinyfish") or not os.environ.get("TINYFISH_API_KEY"):
        _log("xhs web: tinyfish CLI or TINYFISH_API_KEY missing — skipped")
        return 0
    day = _today()
    rows = 0
    for q in ("site:xiaohongshu.com 小工具 vibe coding", "site:xiaohongshu.com 小红书小工具 上线",
              "site:xiaohongshu.com 小工具 榜单", "小红书 小工具 独立开发 爆了"):
        try:
            proc = subprocess.run(["tinyfish", "search", "query", "--pretty", q], capture_output=True, text=True, timeout=60)
        except Exception as e:  # noqa: BLE001
            _log(f"xhs web {q}: {e}")
            continue
        lines = [ln.strip() for ln in (proc.stdout or "").splitlines() if ln.strip()]
        for i, ln in enumerate(lines):
            for url in _URL.findall(ln):
                title = lines[i - 1] if i > 0 and not _URL.search(lines[i - 1]) else ln
                snippet = lines[i + 1] if i + 1 < len(lines) and not _URL.search(lines[i + 1]) else ""
                con.execute("INSERT OR IGNORE INTO traces(source,pid,day,query,title,url,snippet) VALUES(?,?,?,?,?,?,?)",
                            ("xhs_web", "mentions", day, q, title[:200], url[:500], snippet[:300]))
                rows += 1
    log_source(con, "xhs_web", day, rows > 0, rows)
    _log(f"xhs web: {rows} public post links")
    return rows
