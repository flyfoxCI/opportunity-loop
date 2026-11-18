#!/usr/bin/env python3
"""
Starter Story track (Track B) — starterstory.com idea database.

Starter Story has no public JSON API: the database lives at
`https://www.starterstory.com/data` and is server-rendered HTML. Rows carry a
business name, its domain, a solo score and a revenue badge. Detail pages
(`/businesses/<slug>`, `/stories/<slug>`) add description, category,
monetization model, precise revenue and the founder's X handle.

Design notes:
  * Track B is NEVER merged into the TrustMRR candidate pool — Starter Story
    revenue figures are agent-estimated ("not self-reported"), so they inform
    the market read but never drive GO_CANDIDATE scoring on their own.
  * Requests are sequential and paced. A burst of ~20 parallel requests earns
    a 429 from Starter Story; recovery takes ~45s. We delay between requests
    and back off on 429/5xx rather than adding concurrency.
  * Anonymous visitors only see the first page of each query. With a
    `session_cookie` configured (free Starter Story account), the Kaminari
    `data-next-url` sentinel appears and pagination is followed automatically.

Stdlib only, matching loop/pipeline.py.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# Listing row: <a class="nostylelink flex items-center gap-3 ..." href="/businesses/slug">
ROW_RE = re.compile(
    r'(?s)<a class="nostylelink flex items-center gap-3[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>'
)
NAME_RE = re.compile(r'(?s)<div class="text-sm font-semibold[^"]*"[^>]*>(.*?)</div>')
DOMAIN_RE = re.compile(r'font-mono[^>]*>([^<]+)</span>')
SOLO_RE = re.compile(r'>(Solo|Team|Company)\s+([\d.]+)<')
REVENUE_RE = re.compile(r'rounded-md[^>]*>([^<]{2,24})</span>')
NEXT_URL_RE = re.compile(r'id="infinite-scroll-sentinel"[^>]*data-next-url="([^"]+)"')
NEXT_URL_ATTR_RE = re.compile(r'data-next-url="([^"]+)"')

# Detail page text markers.
DETAIL_REV_RE = re.compile(r"Est\. Monthly Revenue ~?\$([\d,.]+[KMB]?)/mo")
STORY_REV_RE = re.compile(r"\$([\d,.]+[KMB]?)\s+revenue/mo")
STORY_FOUNDER_RE = re.compile(r"Founder(?:,|\s+of)\s+(.{2,60}?)\s+(?:\$|started)")
DETAIL_FOUNDER_RE = re.compile(r"Founder(?: of)?\s+(.{0,80}?)@([A-Za-z0-9_]{2,20})")
DETAIL_HANDLE_RE = re.compile(r"@([A-Za-z0-9_]{2,20})")
CONTENT_MARK_RE = re.compile(r"How this works\s*→\s*Overview\s+", re.S)
LEADING_NAME_RE = re.compile(r"^(.{2,60}?)\s+(?:is|are)\s+")

MULTIPLIERS = {"K": 1e3, "M": 1e6, "B": 1e9}


def log(msg: str) -> None:
    print(f"[starterstory] {msg}", flush=True)


def parse_revenue(text: str | None) -> float | None:
    """'$400/mo' | '$1.2K/mo' | '$800M/mo' | '$1B/mo' -> USD float."""
    if not text:
        return None
    s = text.replace("/mo", "").replace("$", "").replace(",", "").strip()
    m = re.match(r"^([\d.]+)\s*([KMB]?)", s)
    if not m:
        return None
    try:
        return float(m.group(1)) * MULTIPLIERS.get(m.group(2), 1)
    except ValueError:
        return None


def _strip_tags(fragment: str) -> str:
    text = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", fragment)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def parse_rows(page: str) -> list[dict[str, Any]]:
    """Extract listing rows from a /data page."""
    rows: list[dict[str, Any]] = []
    for href, body in ROW_RE.findall(page):
        name_m = NAME_RE.search(body)
        if not name_m:
            continue
        domain_m = DOMAIN_RE.search(body)
        solo_m = SOLO_RE.search(body)
        rev_m = REVENUE_RE.search(body)
        name = html.unescape(name_m.group(1)).strip()
        if not name:
            continue
        revenue_text = rev_m.group(1).strip() if rev_m else None
        rows.append(
            {
                "href": href.strip(),
                "name": name,
                "domain": domain_m.group(1).strip() if domain_m else "",
                "solo_score": float(solo_m.group(2)) if solo_m else None,
                "revenue_text": revenue_text,
                "revenue_usd": parse_revenue(revenue_text),
            }
        )
    return rows


def parse_detail(page: str, name_hint: str = "") -> dict[str, Any]:
    """Extract the fields we care about from a business/story detail page.

    Page text runs:
        ... → Overview <Name> <description...> <category> <ICP>
        Monetization <model> +2 Launched <age> Updated <age>
        Est. Monthly Revenue ~$50K/mo as of <year> ... Founder of <Name> <Person> @handle
    """
    text = _strip_tags(page)
    out: dict[str, Any] = {
        "description": "",
        "category": "",
        "monetization": "",
        "revenue_text": "",
        "revenue_usd": None,
        "founder": "",
        "x_handle": "",
    }

    # Work on the researched-profile body only (the nav repeats the same words).
    marker = CONTENT_MARK_RE.search(text)
    body = text[marker.end():] if marker else text

    if "Monetization" not in body:
        # Case-study page: "<Person>, <Company> $45,583 revenue/mo …"
        rev_m = STORY_REV_RE.search(body)
        if rev_m:
            raw = rev_m.group(1)
            out["revenue_text"] = f"${raw}/mo"
            out["revenue_usd"] = parse_revenue(raw)
        founder_m = STORY_FOUNDER_RE.search(body)
        if founder_m:
            out["founder"] = founder_m.group(1).strip()[:60]
        handle_m = DETAIL_HANDLE_RE.search(body)
        if handle_m:
            out["x_handle"] = handle_m.group(1).strip()
        return out

    # --- description + category -------------------------------------------
    head = body.split("Monetization", 1)[0].strip()
    tokens = head.split()
    cat_tokens: list[str] = []
    while tokens and len(cat_tokens) < 6 and not tokens[-1].endswith("."):
        cat_tokens.insert(0, tokens.pop())
    out["category"] = " ".join(cat_tokens).strip()
    desc = " ".join(tokens).strip()
    # Drop leading repeats of the business name ("Linkifi Linkifi is a ...").
    hint = name_hint.strip()
    if hint:
        low = desc.lower()
        while low.startswith(hint.lower()):
            desc = desc[len(hint):].lstrip()
            low = desc.lower()
    lead = LEADING_NAME_RE.match(desc)
    detail_name = hint
    if lead:
        detail_name = lead.group(1).strip()
        desc = desc[lead.end():].strip()
    out["description"] = desc.strip()[:400]

    # --- monetization -------------------------------------------------------
    mon_m = re.search(r"Monetization\s+(.{3,120}?)(?:\s+\+\d+)?(?:\s+Launched|$)", body)
    if mon_m:
        out["monetization"] = mon_m.group(1).strip()[:120]

    # --- revenue ------------------------------------------------------------
    rev_m = DETAIL_REV_RE.search(body)
    if rev_m:
        raw = rev_m.group(1)
        out["revenue_text"] = f"${raw}/mo"
        out["revenue_usd"] = parse_revenue(raw)

    # --- founder + X handle -------------------------------------------------
    founder_m = DETAIL_FOUNDER_RE.search(body)
    if founder_m:
        left = founder_m.group(1).strip()
        handle = founder_m.group(2).strip()
        # "Founder of Linkifi Christopher Panteli" -> "Christopher Panteli"
        prefixes = [detail_name, detail_name.split()[0] if detail_name else "", hint]
        for prefix in prefixes:
            if prefix and left.lower().startswith(prefix.lower()):
                left = left[len(prefix):].strip()
                break
        out["founder"] = left[:60]
        out["x_handle"] = handle
    else:
        handle_m = DETAIL_HANDLE_RE.search(body)
        if handle_m:
            out["x_handle"] = handle_m.group(1).strip()

    return out


class Fetcher:
    """Polite, cached HTTP client for starterstory.com."""

    def __init__(self, cfg: dict[str, Any], cache_dir: Path) -> None:
        self.base_url = cfg.get("base_url", "https://www.starterstory.com").rstrip("/")
        self.timeout = int(cfg.get("timeout_sec", 30))
        self.max_retries = int(cfg.get("max_retries", 4))
        self.backoff = float(cfg.get("backoff_sec", 30))
        self.delay = float(cfg.get("delay_sec", 3.5))
        self.cookie = (
            cfg.get("session_cookie") or os.environ.get("STARTERSTORY_COOKIE") or ""
        ).strip()
        self.cache_dir = cache_dir
        self.cache_ttl = float(cfg.get("cache_ttl_days", 14)) * 86400
        self._last_request = 0.0
        self.request_count = 0
        self.errors: list[str] = []

    # -- HTTP ---------------------------------------------------------------

    def _headers(self) -> dict[str, str]:
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        if self.cookie:
            headers["Cookie"] = self.cookie
        return headers

    def _sleep_between(self) -> None:
        elapsed = time.time() - self._last_request
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)

    def get(self, path: str) -> str | None:
        """GET a path (relative to base_url). Returns None if all retries fail."""
        url = path if path.startswith("http") else f"{self.base_url}{path}"
        ctx = ssl.create_default_context()
        for attempt in range(self.max_retries):
            self._sleep_between()
            req = urllib.request.Request(url, headers=self._headers())
            try:
                with urllib.request.urlopen(req, timeout=self.timeout, context=ctx) as resp:
                    body = resp.read().decode("utf-8", errors="replace")
                self._last_request = time.time()
                self.request_count += 1
                return body
            except urllib.error.HTTPError as e:
                self._last_request = time.time()
                if e.code in (429, 500, 502, 503, 504) and attempt < self.max_retries - 1:
                    wait = self.backoff * (attempt + 1)
                    log(f"HTTP {e.code} on {path} — backing off {wait:.0f}s")
                    time.sleep(wait)
                    continue
                log(f"HTTP {e.code} on {path} — giving up")
                self.errors.append(f"{path}: HTTP {e.code}")
                return None
            except (urllib.error.URLError, ssl.SSLError, TimeoutError, OSError) as e:
                self._last_request = time.time()
                if attempt < self.max_retries - 1:
                    wait = self.backoff * (attempt + 1)
                    log(f"fetch error on {path} ({e}) — retrying in {wait:.0f}s")
                    time.sleep(wait)
                    continue
                log(f"fetch error on {path} ({e}) — giving up")
                self.errors.append(f"{path}: {e}")
                return None
        return None

    # -- Cache --------------------------------------------------------------

    def _cache_path(self, key: str) -> Path:
        digest = hashlib.sha1(key.encode("utf-8")).hexdigest()[:20]
        return self.cache_dir / f"{digest}.json"

    def cached_get(self, key: str, path: str) -> str | None:
        """Fetch `path`, serving from the on-disk cache when fresh.

        The cache key includes the host so a changed `base_url` never reuses
        another host's bodies.
        """
        key = f"{self.base_url}{key}"
        cache_file = self._cache_path(key)
        if cache_file.exists():
            age = time.time() - cache_file.stat().st_mtime
            if age < self.cache_ttl:
                try:
                    return json.loads(cache_file.read_text(encoding="utf-8"))["body"]
                except (json.JSONDecodeError, KeyError, OSError):
                    pass
        body = self.get(path)
        if body is None:
            return None
        try:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            cache_file.write_text(
                json.dumps({"key": key, "path": path, "body": body}, ensure_ascii=False),
                encoding="utf-8",
            )
        except OSError:
            pass
        return body


def _slug_of(href: str) -> str:
    return href.strip("/").split("/")[-1]


def fetch_source(cfg: dict[str, Any], run_dir: Path) -> dict[str, Any]:
    """Harvest Starter Story businesses. Returns {"records": [...], "stats": {...}}.

    Never raises: failures come back as an error payload so the caller can
    keep the TrustMRR pipeline alive.
    """
    scfg = cfg.get("starterstory") or {}
    if not scfg.get("enabled", True):
        return {"records": [], "stats": {"skipped": True}}

    root = Path(__file__).resolve().parent
    cache_dir = root / scfg.get("cache_dir", "cache/starterstory")
    fetcher = Fetcher(scfg, cache_dir)

    list_paths: list[str] = list(scfg.get("list_paths") or [])
    if not list_paths:
        list_paths = ["/data"]

    band_lo, band_hi = scfg.get("revenue_band_usd", [300, 50000])
    sweet_lo, sweet_hi = scfg.get("sweet_spot_usd", [500, 20000])
    enrich_top_n = int(scfg.get("enrich_top_n", 60))
    max_pages = int(scfg.get("max_pages", 5))

    records: dict[str, dict[str, Any]] = {}
    list_requests = 0

    for path in list_paths:
        pages_fetched = 0
        next_path: str | None = path
        while next_path and pages_fetched < max_pages:
            body = fetcher.cached_get(f"list:{next_path}", next_path)
            list_requests += 1
            pages_fetched += 1
            if body is None:
                break
            for row in parse_rows(body):
                slug = _slug_of(row["href"])
                if not slug or slug in records:
                    continue
                records[slug] = {
                    "name": row["name"],
                    "slug": slug,
                    "website": row["domain"],
                    "url": f"{fetcher.base_url}{row['href']}",
                    "detail_path": row["href"],
                    "description": "",
                    "category": "",
                    "monetization": "",
                    "revenue_text": row["revenue_text"] or "",
                    "revenue_usd": row["revenue_usd"],
                    "revenue_verified": False,
                    "solo_score": row["solo_score"],
                    "founder": "",
                    "x_handle": "",
                    "track": "B",
                    "source": "starterstory",
                }
            # Pagination is only offered to logged-in visitors.
            m = NEXT_URL_RE.search(body) or NEXT_URL_ATTR_RE.search(body)
            next_path = m.group(1) if m else None

    log(f"harvested {len(records)} unique businesses from {list_requests} list pages")

    # Band filter + enrichment ordering.
    in_band = [
        r
        for r in records.values()
        if r["revenue_usd"] is not None and band_lo <= r["revenue_usd"] <= band_hi
    ]
    in_band.sort(key=lambda r: -(r["revenue_usd"] or 0))

    # Enrichment targets: the solo-buildable sweet spot first (a proven
    # $500–$20K/mo solo business is the closest analogue to our 14-day
    # solo MVP), then the biggest names for market context.
    sweet = [
        r
        for r in in_band
        if sweet_lo <= (r["revenue_usd"] or 0) <= sweet_hi and r.get("solo_score")
    ]
    sweet.sort(key=lambda r: -(r["solo_score"] or 0))
    targets: list[dict[str, Any]] = []
    seen_ids: set[int] = set()
    for rec in sweet + in_band:
        if id(rec) not in seen_ids:
            seen_ids.add(id(rec))
            targets.append(rec)
        if len(targets) >= enrich_top_n:
            break

    enriched = 0
    for rec in targets:
        body = fetcher.cached_get(f"detail:{rec['detail_path']}", rec["detail_path"])
        if body is None:
            continue
        detail = parse_detail(body, rec.get("name", ""))
        for key, value in detail.items():
            if value:
                rec[key] = value
        if rec["revenue_usd"] is None and detail.get("revenue_usd"):
            rec["revenue_usd"] = detail["revenue_usd"]
        enriched += 1

    # Kill-list categories (gambling / casino) — same rule as the TrustMRR track.
    kills = [k.lower() for k in cfg.get("kill_categories_keywords", [])]
    for rec in records.values():
        haystack = f"{rec['name']} {rec['description']} {rec['category']}".lower()
        rec["killed"] = any(k in haystack for k in kills)

    stats = {
        "harvested": len(records),
        "in_band": len(in_band),
        "enriched": enriched,
        "requests": fetcher.request_count,
        "list_paths": len(list_paths),
        "band_lo": band_lo,
        "band_hi": band_hi,
        "ok": bool(records) or not fetcher.errors,
        "errors": fetcher.errors[:10],
    }
    log(f"in revenue band: {len(in_band)} · enriched: {enriched} · requests: {fetcher.request_count}")

    return {"records": list(records.values()), "stats": stats, "in_band": len(in_band)}


def write_track_artifacts(
    run_dir: Path,
    payload: dict[str, Any],
    cfg: dict[str, Any],
) -> None:
    """Write the Track B artifacts into the run folder."""
    records = payload.get("records", [])
    band_lo, band_hi = cfg.get("starterstory", {}).get("revenue_band_usd", [300, 50000])

    (run_dir / "starterstory_raw.json").write_text(
        json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    in_band = [
        r
        for r in records
        if r.get("revenue_usd") is not None
        and band_lo <= r["revenue_usd"] <= band_hi
        and not r.get("killed")
    ]
    in_band.sort(key=lambda r: -(r["revenue_usd"] or 0))

    header = (
        "slug,name,domain,revenue_text,revenue_usd,solo_score,category,"
        "founder,x_handle,url\n"
    )
    lines = [header]
    for r in in_band:
        cells = [
            r.get("slug", ""),
            (r.get("name") or "").replace(",", " "),
            r.get("website", ""),
            r.get("revenue_text", ""),
            f"{r.get('revenue_usd'):.0f}" if r.get("revenue_usd") else "",
            f"{r['solo_score']:.1f}" if r.get("solo_score") else "",
            r.get("category", ""),
            r.get("founder", ""),
            f"@{r['x_handle']}" if r.get("x_handle") else "",
            r.get("url", ""),
        ]
        lines.append(",".join(str(c) for c in cells) + "\n")
    (run_dir / "starterstory_candidates.csv").write_text("".join(lines), encoding="utf-8")

    sweet_lo, sweet_hi = cfg.get("starterstory", {}).get("sweet_spot_usd", [500, 20000])
    sweet = [
        r
        for r in in_band
        if sweet_lo <= (r["revenue_usd"] or 0) <= sweet_hi and r.get("solo_score")
    ]
    sweet.sort(key=lambda r: -(r["solo_score"] or 0))

    def _row(r: dict[str, Any]) -> str:
        desc = (r.get("description") or "").replace("|", "/").strip()
        if desc:
            desc = desc[0].upper() + desc[1:]
        if len(desc) > 130:
            desc = desc[:127] + "…"
        founder = r.get("founder") or ""
        if r.get("x_handle"):
            founder = f"{founder} (@{r['x_handle']})".strip()
        return (
            f"| {r.get('name','')} | {r.get('revenue_text','')} | "
            f"{r.get('solo_score') or '-'} | {r.get('category') or '-'} | "
            f"{desc or '-'} | {founder or '-'} |"
        )

    header = (
        "| Idea | Revenue | Solopreneur | Category | What it is | Founder |\n"
        "|---|---:|---:|---|---|---|"
    )

    lines_md = [
        "# Track B — Starter Story ideas (inspiration pool)",
        "",
        "**Not scored, not merged into the TrustMRR candidate pool.**",
        "Starter Story revenue figures are research estimates, not verified MRR —",
        "use this list to read the market, and promote an idea by hand if you want",
        "it scored. A free Starter Story account (see `loop/config.json` →",
        "`starterstory.session_cookie`) unlocks the full 3,524-business database.",
        "",
        f"**Harvested:** {len(records)} businesses · **in band "
        f"(${band_lo:,.0f}–${band_hi:,.0f}/mo):** {len(in_band)} · "
        f"**solo sweet spot (${sweet_lo:,.0f}–${sweet_hi:,.0f}/mo):** {len(sweet)}",
        "",
        "---",
        "",
        "## Solo sweet spot — closest analogues to a 14-day solo MVP",
        "",
        f"Proven solo businesses between ${sweet_lo:,.0f} and ${sweet_hi:,.0f}/mo, "
        "ranked by solopreneur score. This is the table to mine.",
        "",
        header,
    ]
    for r in sweet[:40]:
        lines_md.append(_row(r))

    lines_md.extend(
        [
            "",
            "---",
            "",
            "## In-band ideas (highest revenue first)",
            "",
            header,
        ]
    )
    for r in in_band[:60]:
        lines_md.append(_row(r))

    lines_md.append("")
    (run_dir / "STARTERSTORY.md").write_text("\n".join(lines_md), encoding="utf-8")


def summarize(payload: dict[str, Any]) -> str:
    """Short one-paragraph summary for REPORT.md."""
    stats = payload.get("stats", {})
    if stats.get("skipped"):
        return "Track B disabled in config."
    return (
        f"**{stats.get('harvested', 0)}** businesses harvested, "
        f"**{stats.get('in_band', 0)}** inside the ${stats.get('band_lo', 300):,.0f}"
        f"–${stats.get('band_hi', 50000):,.0f}/mo band, "
        f"**{stats.get('enriched', 0)}** enriched with founder details. "
        f"See `STARTERSTORY.md`."
    )


if __name__ == "__main__":
    # Manual smoke test: python3 loop/starterstory.py
    cfg_path = Path(__file__).resolve().parent / "config.json"
    config = json.loads(cfg_path.read_text(encoding="utf-8"))
    out = fetch_source(config, Path("/tmp"))
    print(json.dumps(out["stats"], indent=2))
    for r in out["records"][:5]:
        print(r)
    sys.exit(0)
