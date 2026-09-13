#!/usr/bin/env python3
"""
Publish the latest run to GitHub Pages — v2 blog-style.

New structure (Sep 2026):
  docs/
    index.html                          ← home (post-list of THIS WEEK's directions)
    feed.xml                            ← RSS 2.0
    directions/<slug>.md                ← TOP-LEVEL post pages (latest wins)
    runs/<id>/
      index.html                        ← slim week summary
      VERDICT.md                        ← why these directions (auto-renders)
    tags/<tag>.html                     ← per-tag listings

Generates:
  1. Top-level docs/directions/<slug>.md for each selectable (with front-matter:
     title, date, tier, demand, competition, tags, week, slug, excerpt, layout=post)
  2. docs/runs/<id>/index.html (slim week summary)
  3. docs/index.html (home — post-list + previous weeks)
  4. docs/tags/<tag>.html per tag
  5. docs/feed.xml (RSS)

Tags are derived heuristically from title/content keywords (no LLM needed).
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
DOCS_DIRECTIONS = DOCS / "directions"
DOCS_TAGS = DOCS / "tags"
DOCS_INDEX = DOCS / "index.html"
DOCS_FEED = DOCS / "feed.xml"

SITE_BASE = "https://flyfoxci.github.io/opportunity-loop"


# ============================================================================
# Tag inference (heuristic — no LLM needed)
# ============================================================================

TAG_KEYWORDS = {
    "AI": ["ai", "llm", "gpt", "claude", "agent", "gpt-4", "co-pilot", "copilot"],
    "iOS": ["ios", "iphone", "swift", "swiftui", "app store"],
    "Android": ["android", "play store", "kotlin"],
    "SaaS": ["saas", "web app", "subscription", "dashboard"],
    "B2B": ["b2b", "agency", "agencies", "enterprise", "teams", "contractor"],
    "B2C": ["b2c", "consumer", "parents", "kids", "creators", "shoppers"],
    "religion": ["pastor", "imam", "rabbi", "sermon", "bible", "quran", "liturgy", "worship", "church"],
    "education": ["learn", "education", "roadmap", "students", "heritage", "curriculum"],
    "creator": ["creator", "influencer", "youtube", "tiktok", "newsletter"],
    "finance": ["money", "finance", "income", "earning", "freelancer", "invoice"],
    "social": ["twitter", "x.com", "instagram", "social media"],
    "video": ["video", "ugc", "shorts", "reels", "tiktok"],
    "photo": ["photo", "image", "headshot", "render"],
    "language": ["language", "heritage", "translate", "tagalog", "yoruba"],
    "proposal": ["proposal", "pitch", "rfp", "estimate"],
    "mobile": ["mobile", "app", "ios", "android"],
    "repair": ["repair", "fix", "technician"],
    "vertical": ["white-label", "white label", "vertical", "niche"],
    "analytics": ["analytics", "tracking", "metrics", "insights"],
}


def infer_tags(text: str, explicit_tier: str | None = None) -> list[str]:
    text_lower = text.lower()
    tags = []
    if explicit_tier:
        tags.append(explicit_tier)
    for tag, keywords in TAG_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            if tag not in tags:
                tags.append(tag)
    return tags[:6]


# ============================================================================
# Parsing helpers
# ============================================================================

def parse_verdict(verdict_md: str, run_id: str) -> dict:
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

    for row in table_rows[1:6]:  # skip header row, cap at 5
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
        selectables.append(
            {
                "rank": rank,
                "slug": slug,
                "tier": tier,
                "demand": demand,
                "competition": competition,
                "one_liner": one_liner,
                "excerpt": one_liner,  # default; overwritten by meta if one_liner missing
                "title": slug,
            }
        )

    return {"run_id": run_id, "title": title, "selectables": selectables}


def parse_direction_md(direction_md: str, slug_fallback: str) -> dict:
    """Extract title, tier, demand, competition from a direction markdown.

    Handles BOTH raw direction files (no front-matter) AND output docs
    (with Jekyll front-matter prepended) — strips front-matter first.
    """
    result = {
        "title": slug_fallback.replace("-", " ").title(),
        "tier": None,
        "demand": None,
        "competition": None,
        "excerpt": "",
    }
    # Strip YAML front-matter if present
    if direction_md.startswith("---"):
        parts = direction_md.split("---", 2)
        if len(parts) >= 3:
            direction_md = parts[2]

    m = re.search(r"^#\s+(.+)$", direction_md, re.MULTILINE)
    if m:
        result["title"] = m.group(1).strip()
    m = re.search(r"\*\*Verdict:\*\*\s*(\S+)", direction_md)
    if m:
        result["tier"] = "GO" if "GO_NARROW" not in m.group(1).upper() else "GO_NARROW"
    m = re.search(r"demand=(\d)/5\s*·\s*competition=(\d)/5", direction_md)
    if m:
        result["demand"] = int(m.group(1))
        result["competition"] = int(m.group(2))
    # Excerpt: first non-heading, non-table, non-list paragraph with substance
    paragraphs = [p.strip() for p in direction_md.split("\n\n") if p.strip()]
    for p in paragraphs:
        if p.startswith("#"):  # heading
            continue
        if p.startswith(">"):  # blockquote
            continue
        if p.startswith("|"):  # table
            continue
        # Skip the front-matter-like metadata block (Run ID / Slug / Verdict / Scores)
        if p.startswith("**Run ID:**") or "Verdict:" in p[:30] or "Scores:" in p[:30]:
            continue
        # Allow lists but skip "Why this direction" style headings-content
        if "Why this direction" in p[:60] and p.startswith("###"):
            continue
        if len(p) > 60:
            # Strip any inline markdown formatting from excerpt (bold, italic, links)
            clean = re.sub(r"\*\*(.+?)\*\*", r"\1", p)  # bold
            clean = re.sub(r"\*(.+?)\*", r"\1", clean)  # italic
            clean = re.sub(r"`([^`]+)`", r"\1", clean)  # code
            # Trim leading list marker
            clean = re.sub(r"^[-*]\s+", "", clean)
            clean = re.sub(r"^\d+\.\s+", "", clean)
            result["excerpt"] = clean[:280].replace("\n", " ")
            break
    return result


def parse_run_date(run_id: str) -> datetime | None:
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


# ============================================================================
# File ops
# ============================================================================

def log(msg: str) -> None:
    print(f"[publish] {msg}", flush=True)


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> str:
    proc = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True)
    if check and proc.returncode != 0:
        log(f"CMD FAILED ({proc.returncode}): {' '.join(cmd)}")
        log(f"stderr: {proc.stderr}")
        sys.exit(proc.returncode)
    return proc.stdout.strip()


def ensure_clean_dir(d: Path) -> None:
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True, exist_ok=True)


# ============================================================================
# Per-run → top-level direction pages
# ============================================================================

def _yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def generate_direction_page(slug: str, run_id: str, run_dir: Path, run_date_iso: str, one_liner: str = "") -> dict:
    """Generate docs/directions/<slug>.md. Returns post meta dict for index.

    `one_liner` (from VERDICT.md table) takes priority as the excerpt —
    it's the Stage-B-written summary, more readable than the direction file's
    first paragraph (which is often metadata or a table).
    """
    src = run_dir / "directions" / f"{slug}.md"
    if not src.exists():
        log(f"  WARN: direction source missing for {slug}")
        return {}

    body = src.read_text(encoding="utf-8")
    meta = parse_direction_md(body, slug)

    # Prefer one_liner from VERDICT.md; fall back to direction-md excerpt.
    if one_liner:
        meta["excerpt"] = one_liner

    # Infer tags from title + excerpt + first 1500 chars of body
    blob = (meta["title"] + " " + meta["excerpt"] + " " + body[:1500])
    tags = infer_tags(blob, explicit_tier=meta["tier"])
    meta["tags"] = tags
    meta["slug"] = slug
    meta["week"] = run_id
    meta["url"] = f"/directions/{slug}.html"
    meta["date"] = run_date_iso

    front_matter_lines = [
        "---",
        "layout: post",
        f"title: {_yaml_quote(meta['title'])}",
        f"date: {run_date_iso}",
        f"week: {_yaml_quote(run_id)}",
        f"week_date: {_yaml_quote(run_date_iso)}",
        f"slug: {_yaml_quote(slug)}",
        f"permalink: /directions/{slug}.html",
    ]
    if meta["tier"]:
        front_matter_lines.append(f"tier: {meta['tier']}")
    if meta["demand"] is not None:
        front_matter_lines.append(f"demand: {meta['demand']}")
    if meta["competition"] is not None:
        front_matter_lines.append(f"competition: {meta['competition']}")
    if tags:
        front_matter_lines.append("tags:")
        for t in tags:
            front_matter_lines.append(f"  - {_yaml_quote(t)}")
    if meta["excerpt"]:
        front_matter_lines.append(f"excerpt: {_yaml_quote(meta['excerpt'])}")
    front_matter_lines.append("---")
    front_matter_lines.append("")

    # Strip the original H1 (we use front-matter title)
    body_lines = body.splitlines()
    body_no_h1 = []
    skipped_h1 = False
    for line in body_lines:
        if not skipped_h1 and line.startswith("# "):
            skipped_h1 = True
            continue
        body_no_h1.append(line)
    body_no_h1 = "\n".join(body_no_h1).strip()

    full = "\n".join(front_matter_lines) + "\n" + body_no_h1 + "\n"

    DOCS_DIRECTIONS.mkdir(parents=True, exist_ok=True)
    (DOCS_DIRECTIONS / f"{slug}.md").write_text(full, encoding="utf-8")
    log(f"  generated /directions/{slug}.md (tags={tags})")
    return meta


# ============================================================================
# Week page (slim)
# ============================================================================

def generate_week_page(run_id: str, run_dir: Path, selectables: list[dict]) -> None:
    """Generate docs/runs/<id>/index.html (slim week summary)."""
    target = DOCS_RUNS / run_id
    # Copy VERDICT.md and other raw artifacts
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(run_dir, target)

    # Generate index.html on top
    dt = parse_run_date(run_id)
    date_iso = dt.isoformat() if dt else ""
    week_lbl = week_label(run_id)

    front_matter = ["---", "layout: week"]
    front_matter.append(f"title: {_yaml_quote(week_lbl)}")
    front_matter.append(f"week_label: {_yaml_quote(week_lbl)}")
    front_matter.append(f"run_id: {_yaml_quote(run_id)}")
    front_matter.append(f"date_iso: {_yaml_quote(date_iso)}")
    front_matter.append(f"permalink: /runs/{run_id}/")
    front_matter.append("selectables:")
    for s in selectables:
        front_matter.append(f"  - rank: {s['rank']}")
        front_matter.append(f"    slug: {_yaml_quote(s['slug'])}")
        front_matter.append(f"    title: {_yaml_quote(s['title'])}")
        front_matter.append(f"    tier: {s['tier']}")
        front_matter.append(f"    demand: {s['demand']}")
        front_matter.append(f"    competition: {s['competition']}")
        front_matter.append(f"    excerpt: {_yaml_quote(s.get('excerpt',''))}")
        front_matter.append("    tags:")
        for t in s.get("tags", []):
            front_matter.append(f"      - {_yaml_quote(t)}")
        front_matter.append(f"    url: /directions/{s['slug']}.html")
    front_matter.append("---")
    front_matter.append("")

    (target / "index.html").write_text("\n".join(front_matter), encoding="utf-8")
    log(f"  generated /runs/{run_id}/index.html")


# ============================================================================
# Home page (post-list)
# ============================================================================

def collect_all_posts(weeks: list[dict]) -> list[dict]:
    """Flatten all directions across weeks into a single post-list, newest first."""
    posts = []
    for w in weeks:
        run_dir = DOCS_RUNS / w["run_id"]
        for sel in w.get("selectables", []):
            direction_md = DOCS_DIRECTIONS / f"{sel['slug']}.md"
            if not direction_md.exists():
                continue
            posts.append(
                {
                    "url": f"/directions/{sel['slug']}.html",
                    "title": sel["title"],
                    "date": sel.get("date", w["date_iso"]),
                    "excerpt": sel.get("excerpt", ""),
                    "tier": sel.get("tier"),
                    "demand": sel.get("demand"),
                    "competition": sel.get("competition"),
                    "tags": sel.get("tags", []),
                }
            )
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def collect_all_tags(posts: list[dict]) -> set[str]:
    tags = set()
    for p in posts:
        tags.update(p.get("tags", []))
    return tags


def generate_home_page(posts: list[dict], weeks: list[dict]) -> None:
    """Generate docs/index.html — post-list + previous weeks."""
    fm = [
        "---",
        "layout: home",
        f"title: {_yaml_quote('Weekly TrustMRR direction radar')}",
        f"description: {_yaml_quote('3–5 selectable startup direction packages every Monday morning.')}",
        "permalink: /",
    ]
    fm.append("posts:")
    for p in posts:
        fm.append(f"  - url: {_yaml_quote(p['url'])}")
        fm.append(f"    title: {_yaml_quote(p['title'])}")
        fm.append(f"    date: {_yaml_quote(p['date'])}")
        fm.append(f"    excerpt: {_yaml_quote(p.get('excerpt',''))}")
        if p.get("tier"):
            fm.append(f"    tier: {p['tier']}")
        if p.get("demand") is not None:
            fm.append(f"    demand: {p['demand']}")
        if p.get("competition") is not None:
            fm.append(f"    competition: {p['competition']}")
        fm.append("    tags:")
        for t in p.get("tags", []):
            fm.append(f"      - {_yaml_quote(t)}")
    fm.append("weeks:")
    for w in weeks:
        fm.append(f"  - run_id: {_yaml_quote(w['run_id'])}")
        fm.append(f"    date_iso: {_yaml_quote(w['date_iso'])}")
        fm.append(f"    selectable_count: {w['selectable_count']}")
        fm.append(f"    top_title: {_yaml_quote(w.get('top_title',''))}")
    fm.append("---")
    fm.append("")

    DOCS_INDEX.write_text("\n".join(fm), encoding="utf-8")
    log(f"generated {DOCS_INDEX} ({len(posts)} posts, {len(weeks)} weeks)")


# ============================================================================
# Tag pages
# ============================================================================

def generate_tag_pages(all_tags: set[str], posts: list[dict]) -> None:
    DOCS_TAGS.mkdir(parents=True, exist_ok=True)
    for tag in all_tags:
        matching = [p for p in posts if tag in p.get("tags", [])]
        fm = [
            "---",
            "layout: tag",
            f"title: {_yaml_quote(f'#{tag}')}",
            f"tag: {_yaml_quote(tag)}",
            f"permalink: /tags/{tag}.html",
            "posts:",
        ]
        for p in matching:
            fm.append(f"  - url: {_yaml_quote(p['url'])}")
            fm.append(f"    title: {_yaml_quote(p['title'])}")
            fm.append(f"    date: {_yaml_quote(p['date'])}")
            fm.append(f"    excerpt: {_yaml_quote(p.get('excerpt',''))}")
            if p.get("tier"):
                fm.append(f"    tier: {p['tier']}")
            if p.get("demand") is not None:
                fm.append(f"    demand: {p['demand']}")
            if p.get("competition") is not None:
                fm.append(f"    competition: {p['competition']}")
            fm.append("    tags:")
            for t in p.get("tags", []):
                fm.append(f"      - {_yaml_quote(t)}")
        fm.append("---")
        fm.append("")

        (DOCS_TAGS / f"{tag}.html").write_text("\n".join(fm), encoding="utf-8")
    log(f"generated {len(all_tags)} tag pages in /tags/")


# ============================================================================
# RSS feed
# ============================================================================

def _xml_escape(s: str) -> str:
    return html.escape(s, quote=True)


def generate_search_index(posts: list[dict]) -> None:
    """Write docs/search.json — consumed by assets/js/search.js for client-side filter."""
    search_path = DOCS / "search.json"
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "posts": [
            {
                "url": p["url"],
                "title": p["title"],
                "excerpt": p.get("excerpt", ""),
                "tags": p.get("tags", []),
                "tier": p.get("tier"),
                "demand": p.get("demand"),
                "competition": p.get("competition"),
                "date": p.get("date", ""),
            }
            for p in posts
        ],
    }
    search_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    log(f"generated {search_path} ({len(posts)} posts)")


def generate_feed(posts: list[dict]) -> None:
    now = format_datetime(datetime.now(timezone.utc))
    items = []
    for p in posts[:20]:  # cap feed at 20 most recent
        link = f"{SITE_BASE}{p['url']}"
        title = p["title"]
        desc_parts = []
        if p.get("excerpt"):
            desc_parts.append(f"<p>{_xml_escape(p['excerpt'])}</p>")
        pills = []
        if p.get("tier"):
            pills.append(f"<span>{p['tier']}</span>")
        if p.get("demand") is not None:
            pills.append(f"<span>demand {p['demand']}/5</span>")
        if p.get("competition") is not None:
            pills.append(f"<span>competition {p['competition']}/5</span>")
        if pills:
            desc_parts.append(f"<p>{' · '.join(pills)}</p>")
        if p.get("tags"):
            desc_parts.append(
                f"<p>{' '.join(f'#{_xml_escape(t)}' for t in p['tags'])}</p>"
            )
        try:
            dt = datetime.fromisoformat(p["date"])
            pub = format_datetime(dt)
        except Exception:
            pub = now
        items.append(
            f"""  <item>
    <title>{_xml_escape(title)}</title>
    <link>{link}</link>
    <guid isPermaLink="true">{link}</guid>
    <pubDate>{pub}</pubDate>
    <description><![CDATA[{"".join(desc_parts)}]]></description>
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
    log(f"generated {DOCS_FEED} ({len(items)} items)")


# ============================================================================
# Git ops
# ============================================================================

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
    push = subprocess.run(["git", "push"], cwd=ROOT, capture_output=True, text=True)
    if push.returncode != 0:
        if "no upstream" in push.stderr or "set upstream" in push.stderr:
            run(["git", "push", "--set-upstream", "origin", "main"])
        else:
            log(f"push failed: {push.stderr}")
            sys.exit(push.returncode)
    log("pushed to origin/main")


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    if not STATE_FILE.exists():
        log(f"FATAL: state file missing at {STATE_FILE} — run Stage A first")
        sys.exit(1)

    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    if state.get("agent_stage") != "done":
        log(f"FATAL: agent_stage='{state.get('agent_stage')}' — run Stage B first")
        sys.exit(1)

    run_id = state["last_run_id"]
    run_dir = (LOOP / state["run_dir"]).resolve()
    if not run_dir.exists():
        log(f"FATAL: run dir missing: {run_dir}")
        sys.exit(1)

    log(f"publishing run {run_id}")

    # Clean stale generated dirs
    DOCS.mkdir(parents=True, exist_ok=True)
    ensure_clean_dir(DOCS_DIRECTIONS)
    ensure_clean_dir(DOCS_RUNS)
    ensure_clean_dir(DOCS_TAGS)

    # 1. Parse current run
    verdict_md = (run_dir / "VERDICT.md").read_text(encoding="utf-8")
    summary = parse_verdict(verdict_md, run_id)

    dt = parse_run_date(run_id)
    date_iso = dt.isoformat() if dt else ""

    # 2. Generate top-level direction pages for THIS run
    log("generating direction pages:")
    selectables_with_meta = []
    for sel in summary["selectables"]:
        meta = generate_direction_page(
            sel["slug"], run_id, run_dir, date_iso, one_liner=sel.get("one_liner", "")
        )
        if not meta:
            continue
        sel.update(meta)
        selectables_with_meta.append(sel)

    # 3. Slim week page
    generate_week_page(run_id, run_dir, selectables_with_meta)

    # 4. Build weeks[] across all runs (from docs/runs/)
    weeks = []
    for r in sorted(DOCS_RUNS.iterdir(), key=lambda p: p.name, reverse=True):
        verdict_path = r / "VERDICT.md"
        if not verdict_path.exists():
            continue
        summary = parse_verdict(verdict_path.read_text(encoding="utf-8"), r.name)
        # Re-enrich from SOURCE direction files (loop/runs/<id>/directions/),
        # NOT from docs/directions/ which has front-matter prepended.
        source_dir = LOOP / "runs" / r.name / "directions"
        for sel in summary["selectables"]:
            src_md = source_dir / f"{sel['slug']}.md"
            if src_md.exists():
                meta = parse_direction_md(src_md.read_text(encoding="utf-8"), sel["slug"])
                sel["title"] = meta["title"]
                # Prefer one_liner from VERDICT.md (designed as summary).
                # Fall back to md-derived excerpt.
                if not sel.get("one_liner"):
                    sel["excerpt"] = meta.get("excerpt", "")
                # Re-derive tags from original content
                body = src_md.read_text(encoding="utf-8")
                sel["tags"] = infer_tags(
                    meta["title"] + " " + (sel.get("excerpt") or meta.get("excerpt", "")) + " " + body[:1500],
                    explicit_tier=meta.get("tier"),
                )
        dt = parse_run_date(r.name)
        weeks.append(
            {
                "run_id": r.name,
                "date_iso": dt.isoformat() if dt else "",
                "selectable_count": len(summary["selectables"]),
                "top_title": summary["selectables"][0]["title"] if summary["selectables"] else "",
                "selectables": summary["selectables"],
            }
        )

    # 5. Collect all posts (flattened) + tags
    posts = collect_all_posts(weeks)
    all_tags = collect_all_tags(posts)

    # 6. Generate home, tag pages, RSS, search index
    generate_home_page(posts, weeks)
    generate_tag_pages(all_tags, posts)
    generate_feed(posts)
    generate_search_index(posts)

    # 7. Commit + push
    git_commit_and_push()
    log("DONE")


if __name__ == "__main__":
    main()
