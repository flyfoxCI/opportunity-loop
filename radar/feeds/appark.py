"""Appark (appark.ai): App Store + Google Play top charts, TikTok drama charts.

Guests only get *today's* charts, so this must run every day; a missed day is lost history.
We store derived ranks per (store, country, category, list), never re-host raw dumps.
"""

from __future__ import annotations

import time
import urllib.parse
from datetime import datetime, timedelta

from ..store import log_source, put_metric, upsert_product
from . import http, log

BASE = "https://appark.ai"
HDR = {"Referer": "https://appark.ai/cn/top-charts/app-store"}
LISTS = (("top_free", "free"), ("top_paid", "paid"), ("top_grossing", "grossing"))
STORE = {1: "ios", 2: "play"}

SPEC = {
    "name": "Appark charts", "surface": "apps", "label": "verified rank",
    "endpoint": "appark.ai/api/charts/top-charts", "history": "today only for guests: snapshot daily",
    "role": "discovery",
}

# Apple genre ids (Appark uses the same ids for Google Play).
GENRES = {
    6000: "Business", 6001: "Weather", 6002: "Utilities", 6003: "Travel", 6004: "Sports",
    6005: "Social Networking", 6006: "Reference", 6007: "Productivity", 6008: "Photo & Video",
    6009: "News", 6010: "Navigation", 6011: "Music", 6012: "Lifestyle", 6013: "Health & Fitness",
    6015: "Finance", 6016: "Entertainment", 6017: "Education", 6018: "Books", 6020: "Medical",
    6023: "Food & Drink", 6024: "Shopping", 6026: "Developer Tools", 6027: "Graphics & Design",
    7001: "Action", 7002: "Adventure", 7003: "Casual", 7004: "Board", 7005: "Card", 7006: "Casino",
    7009: "Family", 7011: "Music Games", 7012: "Puzzle", 7013: "Racing", 7014: "Role Playing",
    7015: "Simulation", 7016: "Sports Games", 7017: "Strategy", 7018: "Trivia", 7019: "Word",
    36: "All",
}


def _chart(platform: int, country: str, category: int, page: int, day: str, pace: float) -> dict:
    q = urllib.parse.urlencode({"date": day, "country": country, "category": category,
                                "page": page, "platform": platform})
    res = http(f"{BASE}/api/charts/top-charts?{q}", headers=HDR, pace=pace)
    if res.get("code") != 100000:
        raise RuntimeError(f"{res.get('code')} {res.get('message')}")
    return res.get("data") or {}


def collect_charts(con, day: str, cfg: dict) -> int:
    pace = cfg.get("pace", 0.6)
    jobs = []
    for country in cfg["countries"]:
        jobs.append((country, 36, cfg.get("pages_all", 5)))
    for country in cfg.get("genre_countries", []):
        for cat in cfg.get("genres", []):
            jobs.append((country, cat, cfg.get("pages_genre", 2)))
    rows, errors = 0, []
    for platform in cfg.get("platforms", (1, 2)):
        src = STORE[platform]
        for country, cat, pages in jobs:
            if platform == 2 and cat in cfg.get("genres_ios_only", []):
                continue  # Google Play has no such category: Appark would serve a stale fallback
            for page in range(1, pages + 1):
                try:
                    data = _chart(platform, country, cat, page, day, pace)
                except Exception as e:  # noqa: BLE001
                    errors.append(f"{src}/{country}/{cat}/p{page}: {e}")
                    break
                if data.get("is_fallback") or data.get("data_date") not in (None, day):
                    errors.append(f"{src}/{country}/{cat}: stale data_date {data.get('data_date')}")
                    break
                got = 0
                for key, lst in LISTS:
                    for r in data.get(key) or []:
                        pid = str(r.get("app_id") or "")
                        if not pid:
                            continue
                        got += 1
                        chart = f"{lst}:{country}:{cat}"
                        put_metric(con, src, pid, f"rank:{chart}", day, r.get("rank"))
                        if r.get("rank_change"):
                            put_metric(con, src, pid, f"chg:{chart}", day, r.get("rank_change"))
                        if r.get("newly_promoted"):
                            put_metric(con, src, pid, f"new:{chart}", day, 1)
                        if r.get("rank_days"):
                            put_metric(con, src, pid, f"days1:{chart}", day, r.get("rank_days"))
                        meta = {"cluster_id": r.get("cluster_id"), "developer": r.get("developer_name"),
                                "company": r.get("company_name"), "company_id": r.get("company_id"),
                                "icon": r.get("icon"), "iap": bool(r.get("is_iap")),
                                "price": r.get("price_formatted") or "", "genres": r.get("category_ids") or []}
                        _upsert_app(con, src, pid, day, r.get("app_name") or pid, meta)
                rows += got
                if got < 40 * 3 and page > 1:
                    break
        log(f"appark {src}: {rows} chart rows so far, {len(errors)} errors")
    log_source(con, "appark", day, rows > 0, rows, "; ".join(errors)[:500])
    return rows


def _upsert_app(con, src: str, pid: str, day: str, name: str, meta: dict) -> None:
    """Merge chart meta into the product row without clobbering store-detail fields (a patch: no read)."""
    url = (f"https://apps.apple.com/app/id{pid}" if src == "ios"
           else f"https://play.google.com/store/apps/details?id={pid}")
    upsert_product(con, src, pid, day, name=name, url=url,
                   meta={k: v for k, v in meta.items() if v not in (None, "", [])})


# ---------------------------------------------------------------- TikTok drama

DRAMA_SPEC = {
    "name": "Appark drama", "surface": "drama", "label": "verified rank / estimated impressions",
    "endpoint": "appark.ai/api/advertiser/{tiktok-series-list, playlet-list}",
    "history": "drama-ad chart has daily history (we backfill 30 days); series chart today only",
    "role": "discovery",
}


def collect_drama(con, day: str, cfg: dict) -> int:
    pace = cfg.get("pace", 0.6)
    rows, errors = 0, []
    # 1. TikTok drama series chart (top 100, 20 per page)
    for page in range(1, 6):
        try:
            res = http(f"{BASE}/api/advertiser/tiktok-series-list", body={"page": page}, headers=HDR, pace=pace)
        except Exception as e:  # noqa: BLE001
            errors.append(f"series p{page}: {e}")
            break
        for r in ((res.get("data") or {}).get("list") or []):
            pid = str(r.get("source_series_id") or r.get("domestic_playlet_full_id") or "")
            if not pid:
                continue
            upsert_product(con, "drama", pid, day, name=r.get("title") or pid,
                           url=f"https://www.tiktok.com/search?q={urllib.parse.quote(r.get('title') or '')}",
                           category="TikTok series", direction="drama",
                           meta={"cover": r.get("cover_url"), "episodes": r.get("episode_count"),
                                 "labels": r.get("labels") or [], "kind": "series"})
            put_metric(con, "drama", pid, "rank:tiktok", day, r.get("ranking_num"))
            rows += 1
    # 2. Drama ad chart (creatives / impressions), with history: backfill missing days
    have = {r[0] for r in con.execute("SELECT DISTINCT day FROM metrics WHERE source='drama_ad'")}
    days = [(datetime.strptime(day, "%Y-%m-%d") - timedelta(days=i)).strftime("%Y-%m-%d")
            for i in range(cfg.get("drama_backfill_days", 30), -1, -1)]
    for d in days:
        if d in have and d != day:
            continue
        try:
            res = http(f"{BASE}/api/advertiser/playlet-list", headers=HDR, pace=pace,
                       body={"chart_type": 1, "date": int(d.replace("-", ""))})
        except Exception as e:  # noqa: BLE001
            errors.append(f"ads {d}: {e}")
            continue
        lst = ((res.get("data") or {}).get("list") or [])
        for i, r in enumerate(lst, 1):
            pid = r.get("name_md5") or ""
            if not pid:
                continue
            adv = [a.get("domain") for a in (r.get("playlet_advertisers") or []) if a.get("domain")]
            upsert_product(con, "drama_ad", pid, d, name=r.get("playlet_search_name") or pid,
                           url=f"https://{adv[0]}" if adv else "", category="Drama ads", direction="drama",
                           meta={"cover": r.get("cdn_url"), "advertisers": adv[:5], "lang": r.get("lan"),
                                 "countries": [c.get("code") for c in (r.get("top_country") or [])][:6],
                                 "platforms": [p.get("code") for p in (r.get("top_platform") or [])][:4],
                                 "first_seen": r.get("first_seen"), "aigc": bool(r.get("is_aigc")), "kind": "ads"})
            put_metric(con, "drama_ad", pid, "rank", d, i)
            put_metric(con, "drama_ad", pid, "creatives", d, r.get("creative_count"), "estimated")
            put_metric(con, "drama_ad", pid, "new_creatives", d, r.get("new_creative_count"), "estimated")
            put_metric(con, "drama_ad", pid, "impressions", d, r.get("impression"), "estimated")
            put_metric(con, "drama_ad", pid, "heat", d, r.get("heat"), "estimated")
            rows += 1
        time.sleep(pace)
    log_source(con, "drama", day, rows > 0, rows, "; ".join(errors)[:500])
    log(f"drama: {rows} rows, {len(errors)} errors")
    return rows
