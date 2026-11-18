"""Gravity Engine (rank.gravity-engine.com): WeChat + Douyin mini-game charts.

Public JSON, no login: top 20 per board. The ids are the same ones Stringers uses.
"""

from __future__ import annotations

from ..store import log_source, put_metric, upsert_product
from . import http, log

SPEC = {
    "name": "Gravity Engine mini-games", "surface": "minigames", "label": "verified rank",
    "endpoint": "rank.gravity-engine.com/rank-data/{wechat,douyin}/{day,week}/",
    "history": "today only: snapshot daily (public = top 20 per board)", "role": "discovery + measurement",
}
PLATFORM_NAME = {"wechat": "WeChat", "douyin": "Douyin"}
BOARD_NAME = {"popularity": "Popularity", "bestseller": "Best-selling", "most_played": "Most played",
              "fresh_game": "New games", "publisher_heat": "Publisher heat"}


def collect(con, day: str, cfg: dict) -> int:
    rows, errors = 0, []
    for plat in ("wechat", "douyin"):
        try:
            res = http(f"https://rank.gravity-engine.com/rank-data/{plat}/day/", pace=cfg.get("pace", 1.0))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{plat}: {e}")
            continue
        for board in res.get("ranks") or []:
            btype = board.get("type")
            for it in ((board.get("data") or {}).get("list") or []):
                info = it.get("app_info") or {}
                pid = str(it.get("app_id") or info.get("app_id") or "")
                if not pid:
                    continue
                genre = info.get("game_type_main_name")
                genre = genre if isinstance(genre, str) else ""
                upsert_product(con, "minigame", pid, day, name=info.get("app_name") or pid,
                               url=f"https://rank.gravity-engine.com/{plat}/day/",
                               description=(info.get("description") or "")[:400],
                               category=" / ".join(x for x in (genre, info.get("game_type_sub_name") or "") if x),
                               direction="minigame",
                               meta={"platform": plat, "publisher": info.get("publisher_name"),
                                     "publisher_id": info.get("publisher_id"), "icon": info.get("icon_url"),
                                     "mini_app_id": info.get("mini_app_id"),
                                     "streak": (it.get("change_label") or {}).get("first_msg")})
                key = f"{plat}:{btype}"
                put_metric(con, "minigame", pid, f"rank:{key}", day, it.get("ranking"))
                if it.get("change"):
                    put_metric(con, "minigame", pid, f"chg:{key}", day, it.get("change"))
                rows += 1
    log_source(con, "gravity", day, rows > 0, rows, "; ".join(errors)[:500])
    log(f"gravity: {rows} rows, {len(errors)} errors")
    return rows
