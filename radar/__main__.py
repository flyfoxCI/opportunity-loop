"""Opportunity Loop radar CLI (v3).

  python -m radar collect [--backfill] [--only appark,drama,gravity,itunes,gplay,trustmrr,tranco,github,reddit,xhs_web]
  python -m radar detect            # today's candidates + picks (the line each product crossed)
  python -m radar investigate       # briefs for today's picks (agent mode when LLM keys are set)
  python -m radar playbook          # induce playbooks from the agent's per-brief plays (needs LLM keys)
  python -m radar build             # write the v3 site to docs/v3/
  python -m radar all               # collect, detect, investigate, build

Xiaohongshu is only collected through TinyFish (xhs_web); the manual CSV import was removed in v3.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone

from . import sources
from .store import connect_cached, export_all, export_day

ORDER = ("trustmrr", "tranco", "github", "reddit", "xhs_web", "appark", "drama", "gravity", "itunes", "gplay")


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def collect(backfill: bool, only: set | None) -> None:
    from .detect import CFG
    from .feeds import appark, gravity, stores
    con = connect_cached()
    day = _today()
    cc = CFG["collect"]
    want = lambda s: not only or s in only  # noqa: E731
    if backfill:
        sources.backfill_trustmrr(con)
        con.commit()
    jobs = {
        "trustmrr": lambda: sources.fetch_trustmrr(con),
        # tranco runs after trustmrr: it ranks the websites of the products trustmrr just refreshed
        "tranco": lambda: sources.fetch_tranco(con),
        "github": lambda: sources.fetch_github(con, languages=tuple(cc["github_languages"])),
        "reddit": lambda: sources.fetch_reddit(con),
        "xhs_web": lambda: sources.fetch_xhs_web(con),
        "appark": lambda: appark.collect_charts(con, day, cc["appark"]),
        "drama": lambda: appark.collect_drama(con, day, cc["drama"]),
        "gravity": lambda: gravity.collect(con, day, cc["gravity"]),
        # measurement runs after discovery: it measures whatever charted today
        "itunes": lambda: stores.collect_itunes(con, day, cc["itunes"]),
        "gplay": lambda: stores.collect_gplay(con, day, cc["gplay"]),
    }
    for name in ORDER:
        if want(name):
            try:
                jobs[name]()
            except Exception as e:  # noqa: BLE001 - one broken source never blocks the rest
                print(f"[radar] {name} crashed: {e}", flush=True)
                from .store import log_source
                log_source(con, name, day, False, 0, f"crashed: {e}")
            con.commit()
    if backfill:
        print(f"[radar] exported {export_all(con)} snapshot days")
    days = {r[0] for r in con.execute("SELECT DISTINCT day FROM metrics WHERE source='drama_ad'")} if want("drama") else set()
    for d in sorted(days | {day}):
        export_day(con, d)
    con.close()


def detect() -> list:
    from . import detect as det
    con = connect_cached()
    day = _today()
    cands = det.detect(con, day)
    det.save(con, day, cands)
    con.commit()
    export_day(con, day)
    picked = sum(1 for c in cands if c["picked"])
    by = {}
    for c in cands:
        by[c["rule"]] = by.get(c["rule"], 0) + 1
    print(f"[radar] detect {day}: {len(cands)} crossed a line, {picked} picked · {json.dumps(by)}", flush=True)
    con.close()
    return cands


def investigate() -> None:
    from . import investigate as inv
    con = connect_cached()
    day = _today()
    n = inv.run(con, day)
    con.commit()
    export_day(con, day)
    print(f"[radar] investigate {day}: {n} briefs", flush=True)
    con.close()


def playbook() -> None:
    from . import playbook as pb
    con = connect_cached()
    day = _today()
    try:
        n = pb.induce(con, day)
        print(f"[radar] playbook {day}: {n} plays", flush=True)
    except Exception as e:  # noqa: BLE001  a failed induction keeps yesterday's playbook
        print(f"[radar] playbook skipped: {e}", flush=True)
    con.close()


def build() -> None:
    from .web import build as web_build
    con = connect_cached()
    web_build.write(con)
    con.close()


def main() -> None:
    ap = argparse.ArgumentParser(prog="radar")
    ap.add_argument("cmd", choices=["collect", "detect", "investigate", "playbook", "build", "all"])
    ap.add_argument("--backfill", action="store_true", help="load historical TrustMRR snapshots from run folders")
    ap.add_argument("--only", default="", help="comma list of sources to collect")
    a = ap.parse_args()
    only = {s.strip() for s in a.only.split(",") if s.strip()} or None
    if a.cmd in ("collect", "all"):
        collect(a.backfill, only)
    if a.cmd in ("detect", "all"):
        detect()
    if a.cmd in ("investigate", "all"):
        investigate()
    if a.cmd in ("playbook", "all"):
        playbook()
    if a.cmd in ("build", "all"):
        build()


if __name__ == "__main__":
    main()
