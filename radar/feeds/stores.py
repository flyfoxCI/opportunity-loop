"""Store measurement: exact Google Play installs and iOS rating counts for charted apps.

Appark tells us *which* apps chart; these pulls measure *how much* they move:
  Google Play detail page  -> exact cumulative installs (installs/day = day-over-day delta)
  iTunes Lookup            -> userRatingCount (new ratings/day, a download proxy)
They also fill description, genre, release date and seller site, which classification needs.
"""

from __future__ import annotations

import json
import re
import urllib.parse
from datetime import datetime, timezone

from ..store import log_source, put_metric
from ..taxonomy import classify_app
from . import http, log

GP_SPEC = {
    "name": "Google Play detail", "surface": "apps", "label": "verified",
    "endpoint": "play.google.com/store/apps/details", "history": "our daily snapshots",
    "role": "measurement: exact installs",
}
IT_SPEC = {
    "name": "iTunes Lookup", "surface": "apps", "label": "verified count / estimated proxy",
    "endpoint": "itunes.apple.com/lookup", "history": "our daily snapshots",
    "role": "measurement: rating count",
}


def _charted(con, src: str, day: str) -> dict:
    """pid -> (best rank, best country, is_mover) for apps on any chart today."""
    out = {}
    for r in con.execute("SELECT pid, metric, value FROM metrics WHERE source=? AND day=? AND "
                         "(metric LIKE 'rank:%' OR metric LIKE 'chg:%' OR metric LIKE 'new:%')", (src, day)):
        best, cc, mover = out.get(r["pid"], (999, "us", False))
        kind, _lst, country, _cat = (r["metric"].split(":") + ["", "", "", ""])[:4]
        if kind == "rank" and r["value"] < best:
            best, cc = r["value"], country
        if kind in ("chg", "new") and (kind == "new" or abs(r["value"]) >= 10):
            mover = True
        out[r["pid"]] = (best, cc, mover)
    return out


def _merge_meta(con, src: str, pid: str, extra: dict, *, description: str = "", category: str = "",
                url: str = "", direction: tuple | None = None) -> None:
    row = con.execute("SELECT meta FROM products WHERE source=? AND pid=?", (src, pid)).fetchone()
    meta = json.loads(row["meta"]) if row and row["meta"] else {}
    meta.update({k: v for k, v in extra.items() if v not in (None, "", [])})
    sets, args = ["meta=?"], [json.dumps(meta, ensure_ascii=False)]
    if description:
        sets.append("description=?"); args.append(description[:500])
    if category:
        sets.append("category=?"); args.append(category)
    if url:
        sets.append("url=?"); args.append(url)
    if direction:
        sets += ["direction=?", "direction_conf=?"]; args += [direction[0], direction[1]]
    con.execute(f"UPDATE products SET {', '.join(sets)} WHERE source=? AND pid=?", (*args, src, pid))


# ---------------------------------------------------------------- iTunes Lookup

def collect_itunes(con, day: str, cfg: dict) -> int:
    charted = _charted(con, "ios", day)
    by_cc: dict = {}
    for pid, (_best, cc, _m) in charted.items():
        by_cc.setdefault(cc, []).append(pid)
    rows, errors = 0, []
    for cc, ids in by_cc.items():
        for i in range(0, len(ids), 150):
            batch = ids[i:i + 150]
            try:
                res = http("https://itunes.apple.com/lookup?" + urllib.parse.urlencode(
                    {"id": ",".join(batch), "country": cc, "entity": "software"}), pace=cfg.get("pace", 1.0))
            except Exception as e:  # noqa: BLE001
                errors.append(f"{cc}: {e}")
                continue
            for a in res.get("results") or []:
                pid = str(a.get("trackId") or "")
                if not pid:
                    continue
                put_metric(con, "ios", pid, "ratings", day, a.get("userRatingCount"))
                desc = a.get("description") or ""
                direction = classify_app(a.get("trackName") or "", desc, a.get("primaryGenreId"))
                _merge_meta(con, "ios", pid, {
                    "released": (a.get("releaseDate") or "")[:10],
                    "version": a.get("version"), "version_date": (a.get("currentVersionReleaseDate") or "")[:10],
                    "release_notes": (a.get("releaseNotes") or "")[:400], "seller": a.get("sellerName"),
                    "seller_url": a.get("sellerUrl"), "price": a.get("formattedPrice"),
                    "genre": a.get("primaryGenreName"), "lookup_cc": cc, "icon": a.get("artworkUrl100"),
                    "screenshot": (a.get("screenshotUrls") or [None])[0],
                    "rating": round(a["averageUserRating"], 2) if a.get("averageUserRating") else None,
                }, description=desc, category=a.get("primaryGenreName") or "", url=a.get("trackViewUrl") or "",
                    direction=direction)
                rows += 1
    log_source(con, "itunes", day, rows > 0, rows, "; ".join(errors)[:500])
    log(f"itunes: {rows} apps measured across {len(by_cc)} storefronts, {len(errors)} errors")
    return rows


# ---------------------------------------------------------------- Google Play detail

_DS5 = re.compile(r"AF_initDataCallback\(\{key: 'ds:5'.*?data:(.*?), sideChannel", re.S)


def _dig(x, *path):
    for p in path:
        try:
            x = x[p]
        except (IndexError, KeyError, TypeError):
            return None
    return x


def _gp_detail(pkg: str) -> dict | None:
    page = http("https://play.google.com/store/apps/details?" + urllib.parse.urlencode(
        {"id": pkg, "hl": "en", "gl": "us"}), as_json=False, timeout=30)
    m = _DS5.search(page)
    if not m:
        return None
    info = _dig(json.loads(m.group(1)), 1, 2)
    if not info:
        return None
    released = _dig(info, 10, 0)
    updated = _dig(info, 145, 0, 1, 0)
    return {
        "name": _dig(info, 0, 0), "installs": _dig(info, 13, 2), "installs_label": _dig(info, 13, 0),
        "ratings": _dig(info, 51, 2, 1), "score": _dig(info, 51, 0, 1),
        "description": re.sub(r"<[^>]+>", " ", _dig(info, 72, 0, 1) or "")[:1500],
        "genre": _dig(info, 79, 0, 0, 0), "developer": _dig(info, 68, 0),
        "dev_site": _dig(info, 69, 0, 5, 2), "released": released if isinstance(released, str) else "",
        "updated": (datetime.fromtimestamp(updated, timezone.utc).strftime("%Y-%m-%d")
                    if isinstance(updated, (int, float)) else ""),
        "whatsnew": re.sub(r"<[^>]+>", " ", _dig(info, 144, 1, 1) or "")[:400],
    }


def collect_gplay(con, day: str, cfg: dict) -> int:
    charted = _charted(con, "play", day)
    tracked = {r[0] for r in con.execute("SELECT DISTINCT pid FROM metrics WHERE source='play' AND metric='installs'")}
    done = {r[0] for r in con.execute("SELECT pid FROM metrics WHERE source='play' AND metric='installs' AND day=?",
                                      (day,))}
    # Continuity first (a series with gaps can't make a baseline), then movers, then best rank.
    order = sorted(charted.items(), key=lambda kv: (kv[0] not in tracked, not kv[1][2], kv[1][0]))
    todo = [pid for pid, _ in order if pid not in done][: cfg.get("gp_max", 400)]
    rows, errors = 0, []
    for pkg in todo:
        try:
            d = _gp_detail(pkg)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{pkg}: {e}")
            if len(errors) > 25:
                break
            continue
        if not d:
            continue
        put_metric(con, "play", pkg, "installs", day, d["installs"])
        put_metric(con, "play", pkg, "ratings", day, d["ratings"])
        put_metric(con, "play", pkg, "rating", day, d["score"])
        prow = con.execute("SELECT meta FROM products WHERE source='play' AND pid=?", (pkg,)).fetchone()
        genres = (json.loads(prow["meta"]) if prow and prow["meta"] else {}).get("genres") or [None]
        direction = classify_app(d["name"] or pkg, d["description"], genres[0])
        _merge_meta(con, "play", pkg, {k: d[k] for k in ("installs_label", "genre", "developer", "dev_site",
                                                          "released", "updated", "whatsnew")},
                    description=d["description"], category=d["genre"] or "", direction=direction)
        rows += 1
        if cfg.get("pace"):
            import time
            time.sleep(cfg["pace"])
        if rows % 50 == 0:
            con.commit()
            log(f"gplay: {rows}/{len(todo)}")
    log_source(con, "gplay", day, rows > 0, rows, "; ".join(errors)[:500])
    log(f"gplay: {rows} apps measured, {len(errors)} errors")
    return rows
