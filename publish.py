#!/usr/bin/env python3
"""
Publish the latest run to GitHub Pages — rich layout.

What this does:
  1. Copy loop/runs/<id>/* → docs/runs/<id>/*
  2. For the just-published run, generate docs/runs/<id>/index.html
     (uses _layouts/week.html; renders this-week hero + selectable cards)
  3. Regenerate docs/index.html with this-week + history (uses _layouts/home.html)
  4. Generate docs/feed.xml (RSS 2.0 with one <item> per week, newest first)
  5. Atomic git add docs/ + commit + push

Idempotent. Safe to re-run.
"""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOOP = ROOT / "loop"
STATE_FILE = LOOP / "state" / "last_run.json"
DOCS = ROOT / "docs"
DOCS_RUNS = DOCS / "runs"
DOCS_INDEX = DOCS / "index.html"
DOCS_FEED = DOCS / "feed.xml"

SITE_BASE = "https://flyfoxci.github.io/opportunity-loop"  # used in RSS for absolute URLs


# ----------------------------------------------------------------------------
# Logging
# ----------------------------------------------------------------------------

def log(msg: str) -> None:
    print(f"[publish] {msg}", flush=True)


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> str:
    proc = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True)
    if check and proc.returncode != 0:
        log(f"CMD FAILED ({proc.returncode}): {' '.join(cmd)}")
        log(f"stderr: {proc.stderr}")
        sys.exit(proc.returncode)
    return proc.stdout.strip()


# ----------------------------------------------------------------------------
# Parsing VERDICT.md
# ----------------------------------------------------------------------------

def parse_verdict(verdict_md: str, run_id: str) -> dict:
    """Pull structured summary out of a VERDICT.md for templates."""
    title = run_id
    m = re.search(r"^#\s+(.+)$", verdict_md, re.MULTILINE)
    if m:
        title = m.group(1).strip()

    selectables: list[dict] = []
    in_selectable_table = False
    table_rows: list[str] = []
    for line in verdict_md.splitlines():
        if "Selectable directions" in line:
            in_selectable_table = True
            continue
        if in_selectable_table:
            if line.startswith("|---") or line.startswith("| ---"):
                continue
            if line.startswith("|"):
                table_rows.append(line)
            elif table_rows:
                in_selectable_table = False

    for idx, row in enumerate(table_rows[1:6], start=1):  # skip header row, cap at 5
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) < 6:
            continue
        try:
            rank = int(cells[0])
        except ValueError:
            continue
        slug = cells[1].strip("`").strip()
        tier_raw = cells[2].upper()
        tier = "GO" if "GO_NARROW" not in tier_raw else "GO_NARROW"
        try:
            demand = int(cells[3].split("/")[0].strip())
        except ValueError:
            demand = 0
        try:
            competition = int(cells[4].split("/")[0].strip())
        except ValueError:
            competition = 0
        one_liner = cells[5].strip()
        # Title — usually from the corresponding direction file's H1
        title_from_file = slug  # we'll patch this later when we have directions parsed
        selectables.append(
            {
                "rank": rank,
                "slug": slug,
                "tier": tier,
                "demand": demand,
                "competition": competition,
                "one_liner": one_liner,
                "title": title_from_file,
            }
        )

    # Try to enrich titles from directions/*.md
    return {
        "run_id": run_id,
        "title": title,
        "selectables": selectables,
    }


def parse_direction_title(direction_md: str, slug_fallback: str) -> str:
    """Extract the H1 title from a direction markdown file."""
    m = re.search(r"^#\s+(.+)$", direction_md, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return slug_fallback.replace("-", " ").title()


def enrich_titles_with_directions(run_dir: Path, selectables: list[dict]) -> None:
    """Mutates selectables in place — adds 'title' and 'url' from directions/*.md."""
    for s in selectables:
        slug = s["slug"]
        d_file = run_dir / "directions" / f"{slug}.md"
        if d_file.exists():
            s["title"] = parse_direction_title(d_file.read_text(encoding="utf-8"), slug)
        else:
            s["title"] = slug.replace("-", " ").title()
        s["url"] = f"directions/{slug}.html"


def parse_run_date(run_id: str) -> datetime | None:
    """run_id like '2026-09-13_112909' → datetime(2026, 9, 13, 11, 29, 9)."""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})_(\d{2})(\d{2})(\d{2})$", run_id)
    if not m:
        return None
    y, mo, d, h, mi, s = map(int, m.groups())
    return datetime(y, mo, d, h, mi, s, tzinfo=timezone.utc)


def week_label(run_id: str) -> str:
    dt = parse_run_date(run_id)
    if not dt:
        return run_id
    iso = dt.isocalendar()
    return f"Week {iso.week} · {dt.strftime('%Y-%m-%d')}"


# ----------------------------------------------------------------------------
# File ops
# ----------------------------------------------------------------------------

def copy_run_to_docs(run_dir: Path, run_id: str) -> Path:
    target = DOCS_RUNS / run_id
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(run_dir, target)
    log(f"copied {run_dir} → {target}")
    return target


# ----------------------------------------------------------------------------
# Per-week page generator (docs/runs/<id>/index.html)
# ----------------------------------------------------------------------------

def generate_week_page(run_id: str, target_dir: Path, selectables: list[dict], week_lbl: str) -> None:
    """Write target_dir/index.html with front-matter so Jekyll uses week.html layout."""
    if selectables:
        selectables_sorted = sorted(selectables, key=lambda x: x["rank"])
        top = selectables_sorted[0]
        if not top.get("title"):
            top["title"] = top["slug"]
        for s in selectables_sorted:
            if not s.get("title"):
                s["title"] = s["slug"]
            s["url"] = f"directions/{s['slug']}.html"
    else:
        selectables_sorted = []

    front_matter = {
        "layout": "week",
        "title": week_lbl,
        "week_label": week_lbl,
        "run_id": run_id,
        "selectables": selectables_sorted,
        "verdict_url": "VERDICT.html",
        "permalink": f"/runs/{run_id}/",
    }
    yaml = "---\n" + "\n".join(
        f"{k}: {_yaml_val(v)}" for k, v in front_matter.items()
    ) + "\n---\n\n"
    (target_dir / "index.html").write_text(yaml, encoding="utf-8")
    log(f"generated week page → {target_dir}/index.html")


def _yaml_val(v) -> str:
    """Quick YAML scalar/array serializer (no PyYAML dep)."""
    if isinstance(v, str):
        # Always quote to avoid YAML parsing issues
        escaped = v.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if isinstance(v, int):
        return str(v)
    if isinstance(v, list):
        items = []
        for item in v:
            if isinstance(item, dict):
                inner = ", ".join(f"{k}: {_yaml_val(vv)}" for k, vv in item.items())
                items.append(f"{{ {inner} }}")
            else:
                items.append(f"- {_yaml_val(item)}")
        return "\n" + "\n".join(items)
    return f'"{v}"'


# ----------------------------------------------------------------------------
# Top-level home page (docs/index.html)
# ----------------------------------------------------------------------------

def collect_history() -> list[dict]:
    """Walk docs/runs/* for the full history."""
    runs = sorted(
        [p for p in DOCS_RUNS.iterdir() if p.is_dir()],
        key=lambda p: p.name,
        reverse=True,
    )
    history = []
    for r in runs:
        verdict_path = r / "VERDICT.md"
        if not verdict_path.exists():
            continue
        try:
            summary = parse_verdict(verdict_path.read_text(encoding="utf-8"), r.name)
            enrich_titles_with_directions(r, summary["selectables"])
        except Exception as e:
            log(f"  failed to parse {r.name}: {e}")
            continue
        top = summary["selectables"][0] if summary["selectables"] else None
        history.append(
            {
                "week_label": week_label(r.name),
                "run_id": r.name,
                "run_url": f"runs/{r.name}/",
                "selectable_count": len(summary["selectables"]),
                "top_slug": top["slug"] if top else "",
                "top_title": top["title"] if top else "",
                "date_iso": (parse_run_date(r.name).isoformat() if parse_run_date(r.name) else ""),
            }
        )
    return history


def generate_home_page(history: list[dict]) -> None:
    this_week = history[0] if history else None
    past = history[1:] if len(history) > 1 else []

    fm = {
        "layout": "home",
        "title": "Weekly TrustMRR direction radar",
        "description": "3–5 selectable startup direction packages every Monday morning.",
        "permalink": "/",
    }

    yaml_lines = ["---"]
    for k, v in fm.items():
        yaml_lines.append(f"{k}: {_yaml_val(v)}")
    yaml_lines.append("this_week:")
    if this_week:
        # We pass selectables inline so the home template can render them directly
        this_week_dict = dict(this_week)
        # Hydrate selectables for the template (reuse what collect_history already built)
        verdict_path = DOCS_RUNS / this_week["run_id"] / "VERDICT.md"
        if verdict_path.exists():
            sv = parse_verdict(verdict_path.read_text(encoding="utf-8"), this_week["run_id"])
            enrich_titles_with_directions(DOCS_RUNS / this_week["run_id"], sv["selectables"])
            this_week_dict["selectables"] = sv["selectables"]
        this_week_dict["verdict_url"] = f"runs/{this_week['run_id']}/VERDICT.html"
        this_week_dict["run_url"] = f"runs/{this_week['run_id']}/"
        yaml_lines.append(f"  week_label: {_yaml_val(this_week['week_label'])}")
        yaml_lines.append(f"  run_id: {_yaml_val(this_week['run_id'])}")
        yaml_lines.append(f"  run_url: {_yaml_val(this_week_dict['run_url'])}")
        yaml_lines.append(f"  verdict_url: {_yaml_val(this_week_dict['verdict_url'])}")
        yaml_lines.append("  selectables:")
        for s in this_week_dict.get("selectables", []):
            yaml_lines.append(f"    - rank: {s['rank']}")
            yaml_lines.append(f"      slug: {_yaml_val(s['slug'])}")
            yaml_lines.append(f"      title: {_yaml_val(s['title'])}")
            yaml_lines.append(f"      tier: {_yaml_val(s['tier'])}")
            yaml_lines.append(f"      demand: {s['demand']}")
            yaml_lines.append(f"      competition: {s['competition']}")
            yaml_lines.append(f"      one_liner: {_yaml_val(s['one_liner'])}")
            yaml_lines.append(f"      url: {_yaml_val(s['url'])}")
    else:
        yaml_lines.append("  week_label: \"\"")
        yaml_lines.append("  run_id: \"\"")
        yaml_lines.append("  selectables: []")

    yaml_lines.append("history:")
    for h in past:
        yaml_lines.append(f"  - week_label: {_yaml_val(h['week_label'])}")
        yaml_lines.append(f"    run_id: {_yaml_val(h['run_id'])}")
        yaml_lines.append(f"    run_url: {_yaml_val(h['run_url'])}")
        yaml_lines.append(f"    selectable_count: {h['selectable_count']}")
        yaml_lines.append(f"    top_slug: {_yaml_val(h['top_slug'])}")
        yaml_lines.append(f"    top_title: {_yaml_val(h['top_title'])}")
        yaml_lines.append(f"    date_iso: {_yaml_val(h['date_iso'])}")
    yaml_lines.append("---")
    yaml_lines.append("")

    DOCS_INDEX.write_text("\n".join(yaml_lines), encoding="utf-8")
    log(f"generated home → {DOCS_INDEX} ({len(history)} runs in history)")


# ----------------------------------------------------------------------------
# RSS feed (docs/feed.xml)
# ----------------------------------------------------------------------------

def _xml_escape(s: str) -> str:
    return html.escape(s, quote=True)


def generate_feed(history: list[dict]) -> None:
    now = format_datetime(datetime.now(timezone.utc))
    items = []
    for h in history:
        link = f"{SITE_BASE}/{h['run_url']}"
        verdict_link = f"{SITE_BASE}/runs/{h['run_id']}/VERDICT.html"
        title = f"{h['week_label']} — {h['selectable_count']} selectables"
        if h.get("top_title"):
            title += f" · {h['top_title']}"
        pub = h["date_iso"]
        # format_datetime expects RFC 2822
        try:
            dt = parse_run_date(h["run_id"])
            pub = format_datetime(dt) if dt else now
        except Exception:
            pub = now

        desc_parts = [
            f"<p><strong>{h['selectable_count']} selectable directions</strong>",
        ]
        if h.get("top_title"):
            desc_parts.append(f" — top pick: <a href=\"{link}\">{_xml_escape(h['top_title'])}</a>")
        desc_parts.append("</p>")
        desc_parts.append(
            f"<p><a href=\"{verdict_link}\">Read VERDICT.md</a> · "
            f"<a href=\"{link}\">Open week page</a></p>"
        )
        description = "".join(desc_parts)

        items.append(
            f"""  <item>
    <title>{_xml_escape(title)}</title>
    <link>{link}</link>
    <guid isPermaLink="true">{link}</guid>
    <pubDate>{pub}</pubDate>
    <description><![CDATA[{description}]]></description>
  </item>"""
        )

    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Opportunity Loop</title>
    <link>{SITE_BASE}/</link>
    <description>Weekly TrustMRR startup direction radar — 3–5 selectable direction packages every Monday morning (Beijing time). $10K MRR · 14d MVP · ≤$300/30d marketing.</description>
    <atom:link href="{SITE_BASE}/feed.xml" rel="self" type="application/rss+xml" />
    <language>en-us</language>
    <lastBuildDate>{now}</lastBuildDate>
    <generator>opportunity-loop action</generator>
{chr(10).join(items) if items else '  <!-- no items yet -->'}
  </channel>
</rss>
"""
    DOCS_FEED.write_text(feed, encoding="utf-8")
    log(f"generated feed → {DOCS_FEED} ({len(items)} items)")


# ----------------------------------------------------------------------------
# Git ops
# ----------------------------------------------------------------------------

def git_commit_and_push() -> None:
    run(["git", "config", "user.name", "opportunity-loop-bot"])
    run(["git", "config", "user.email", "actions@users.noreply.github.com"])

    run(["git", "add", "docs/"])

    diff = run(["git", "diff", "--cached", "--name-only"], check=False)
    if not diff.strip():
        log("no docs/ changes — skipping commit")
        return

    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    msg = f"weekly: {state['last_run_id']} — {state.get('selectable_count', 0)} selectables"
    run(["git", "commit", "-m", msg])
    log(f"committed: {msg}")

    push = subprocess.run(
        ["git", "push"], cwd=ROOT, capture_output=True, text=True
    )
    if push.returncode != 0:
        if "no upstream" in push.stderr or "set upstream" in push.stderr:
            log("no upstream — setting and pushing")
            run(["git", "push", "--set-upstream", "origin", "main"])
        else:
            log(f"push failed: {push.stderr}")
            sys.exit(push.returncode)
    log("pushed to origin/main")


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> None:
    if not STATE_FILE.exists():
        log(f"FATAL: state file missing at {STATE_FILE} — run Stage A first")
        sys.exit(1)

    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    if state.get("agent_stage") != "done":
        log(
            f"FATAL: agent_stage is '{state.get('agent_stage')}' — run Stage B first"
        )
        sys.exit(1)

    run_dir = (LOOP / state["run_dir"]).resolve()
    if not run_dir.exists():
        log(f"FATAL: run dir missing: {run_dir}")
        sys.exit(1)

    run_id = state["last_run_id"]
    log(f"publishing run {run_id}")

    DOCS.mkdir(parents=True, exist_ok=True)
    DOCS_RUNS.mkdir(parents=True, exist_ok=True)

    # 1. Copy raw artifacts (VERDICT.md, directions/*.md, REPORT.md, etc.)
    target = copy_run_to_docs(run_dir, run_id)

    # 2. Parse VERDICT.md for this run
    verdict_md = (target / "VERDICT.md").read_text(encoding="utf-8")
    summary = parse_verdict(verdict_md, run_id)
    enrich_titles_with_directions(target, summary["selectables"])

    # 3. Generate per-week page
    generate_week_page(run_id, target, summary["selectables"], week_label(run_id))

    # 4. Walk all weeks for history (top-level home + RSS)
    history = collect_history()

    # 5. Generate top-level home + RSS feed
    generate_home_page(history)
    generate_feed(history)

    # 6. Atomic git commit + push
    git_commit_and_push()
    log("DONE")


if __name__ == "__main__":
    main()
