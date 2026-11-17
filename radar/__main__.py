"""Opportunity Radar v2 CLI.

  python -m radar collect [--backfill] [--only trustmrr,appstore,github,reddit]
  python -m radar build            # analyze + (trace if tinyfish) + write docs/radar/
  python -m radar all [--backfill] # collect then build
"""

from __future__ import annotations

import argparse

from . import sources
from datetime import datetime, timezone

from .store import connect_cached, export_all, export_day


def collect(backfill: bool, only: set[str] | None) -> None:
    con = connect_cached()
    want = lambda s: not only or s in only  # noqa: E731
    if backfill:
        sources.backfill_trustmrr(con)
        con.commit()
    for name, fn in (("trustmrr", sources.fetch_trustmrr), ("github", sources.fetch_github),
                     ("appstore", sources.fetch_appstore), ("reddit", sources.fetch_reddit)):
        if want(name):
            fn(con)
            con.commit()
    if backfill:
        print(f"[radar] exported {export_all(con)} snapshot days")
    else:
        export_day(con, datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    con.close()


def build(trace: bool = True) -> None:
    from . import analyze, site
    con = connect_cached()
    model = analyze.run(con)
    if trace:
        targets = [s for s in model["signals"] if s["source"] in ("trustmrr", "appstore")][:12]
        if sources.trace_products(con, targets):
            con.commit()
            export_day(con, datetime.now(timezone.utc).strftime("%Y-%m-%d"))
            model = analyze.run(con)
    site.write(model)
    con.close()


def main() -> None:
    ap = argparse.ArgumentParser(prog="radar")
    ap.add_argument("cmd", choices=["collect", "build", "all"])
    ap.add_argument("--backfill", action="store_true", help="load historical TrustMRR snapshots from run folders")
    ap.add_argument("--only", default="", help="comma list of sources to collect")
    ap.add_argument("--no-trace", action="store_true")
    a = ap.parse_args()
    only = {s.strip() for s in a.only.split(",") if s.strip()} or None
    if a.cmd in ("collect", "all"):
        collect(a.backfill, only)
    if a.cmd in ("build", "all"):
        build(trace=not a.no_trace)


if __name__ == "__main__":
    main()
