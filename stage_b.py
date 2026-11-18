#!/usr/bin/env python3
"""
Stage B orchestrator — Opportunity Loop.

After Stage A (`loop/run.sh`) finishes:
  B1. Run TinyFish CLI queries in parallel for each GO_CANDIDATE / top WATCH.
      Saves raw evidence to loop/runs/<id>/search_evidence/<slug>.json.
  B2. Call MiniMax (Anthropic-compatible API) once with:
        system  = loop/AGENT_PROMPT.md
        user    = REPORT.md + candidates.csv + all search_evidence/*.json + seed_directions/INDEX.md
      Model is told to emit VERDICT.md + directions/*.md per the templates.

Reads env:
  ANTHROPIC_BASE_URL   (default: https://api.minimaxi.com/anthropic)
  ANTHROPIC_AUTH_TOKEN (required)
  ANTHROPIC_MODEL      (default: MiniMax-M3)

Exit codes:
  0 success
  4 B1 failed (TinyFish)
  5 B2 failed (LLM)
  6 insufficient selectables (<3)
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOOP = ROOT / "loop"
STATE_FILE = LOOP / "state" / "last_run.json"
TEMPLATE_DIR = LOOP / "templates"
SEED_DIR = LOOP / "seed_directions"
AGENT_PROMPT = LOOP / "AGENT_PROMPT.md"
CONFIG_FILE = LOOP / "config.json"

run_id = ""

ANTHROPIC_BASE_URL = os.environ.get(
    "ANTHROPIC_BASE_URL", "https://api.minimaxi.com/anthropic"
)
ANTHROPIC_AUTH_TOKEN = os.environ.get("ANTHROPIC_AUTH_TOKEN", "")
ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "MiniMax-M3")
TINYFISH_API_KEY = os.environ.get("TINYFISH_API_KEY", "")


def log(msg: str) -> None:
    print(f"[stage_b] {msg}", flush=True)


def load_state() -> dict:
    if not STATE_FILE.exists():
        log(f"FATAL: state file missing at {STATE_FILE} — run Stage A first")
        sys.exit(1)
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def run_dir_for(state: dict) -> Path:
    return (LOOP / state["run_dir"]).resolve()


def tinyfish_search(query: str, timeout: int = 60) -> dict:
    """Run `tinyfish search query` and parse its human-readable output.

    Falls back to empty result if CLI is missing or auth failed.
    """
    if not shutil.which("tinyfish"):
        return {"query": query, "error": "tinyfish CLI not installed", "results": []}
    if not TINYFISH_API_KEY:
        return {"query": query, "error": "TINYFISH_API_KEY not set", "results": []}
    try:
        proc = subprocess.run(
            ["tinyfish", "search", "query", "--pretty", query],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return {
            "query": query,
            "ok": proc.returncode == 0,
            "results_count": proc.stdout.count("\n") if proc.stdout else 0,
            "stdout": proc.stdout[:8000],  # cap to keep prompt bounded
            "stderr": proc.stderr[:1500] if proc.stderr else "",
        }
    except subprocess.TimeoutExpired:
        return {"query": query, "error": "timeout", "results": []}
    except Exception as e:
        return {"query": query, "error": str(e), "results": []}


def b1_tinyfish_sweep(run_dir: Path, candidates: list[dict]) -> dict[str, dict]:
    """For each GO_CANDIDATE and top WATCH, run 3 search queries in parallel."""
    evidence_dir = run_dir / "search_evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    slug_names = {c["slug"]: c["name"] for c in candidates}

    # Skip already-collected evidence (idempotent retry support)
    pending: list[tuple[str, str, str]] = []
    for c in candidates:
        slug = c["slug"]
        name = c["name"]
        category = (c.get("category") or "").strip() or "tool"
        ev_file = evidence_dir / f"{slug}.json"
        if ev_file.exists() and ev_file.stat().st_size > 100:
            log(f"  reuse cached evidence for {slug}")
            continue
        pending.extend(
            [
                (slug, "competition", f"{name} {category} alternatives 2026"),
                (
                    slug,
                    "pain",
                    f'{name} (painful OR broken OR hate OR expensive OR "looking for")',
                ),
                (slug, "recommend", f'"looking for" OR recommend OR alternative {name}'),
            ]
        )

    if not pending:
        log("  no pending searches — using cached evidence")
        return {
            slug: json.loads((evidence_dir / f"{slug}.json").read_text())
            for slug in slug_names
        }

    log(f"B1: running {len(pending)} TinyFish queries in parallel…")
    out: dict[str, dict] = {slug: {"slug": slug, "name": name, "queries": []}
                            for slug, name in slug_names.items()}

    def run_one(item: tuple[str, str, str]) -> tuple[str, str, dict]:
        slug, kind, query = item
        return slug, kind, tinyfish_search(query)

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for slug, kind, result in ex.map(run_one, pending):
            out.setdefault(slug, {"slug": slug, "queries": []})["queries"].append(
                {"kind": kind, **result}
            )

    # Persist per-slug
    for slug, payload in out.items():
        (evidence_dir / f"{slug}.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    return out


def load_report_and_candidates(run_dir: Path) -> tuple[str, str, list[dict]]:
    report = (run_dir / "REPORT.md").read_text(encoding="utf-8")
    csv_text = (run_dir / "candidates.csv").read_text(encoding="utf-8")

    # Parse candidates.csv (kept simple — the LLM also gets the full REPORT.md)
    candidates: list[dict] = []
    lines = csv_text.strip().splitlines()
    if len(lines) >= 2:
        headers = [h.strip() for h in lines[0].split(",")]
        for line in lines[1:]:
            # Naive CSV parse — values may contain commas if quoted; we don't have any in practice.
            row = {}
            for h, v in zip(headers, line.split(",")):
                row[h] = v.strip()
            if row.get("slug"):
                candidates.append(row)

    return report, csv_text, candidates


def b2_llm_call(system_prompt: str, user_prompt: str, max_tokens: int = 16000) -> str:
    """Call MiniMax via the Anthropic SDK."""
    if not ANTHROPIC_AUTH_TOKEN:
        log("FATAL: ANTHROPIC_AUTH_TOKEN not set")
        sys.exit(5)
    try:
        import anthropic
    except ImportError:
        log("FATAL: `anthropic` SDK not installed — `pip install -r requirements.txt`")
        sys.exit(5)

    client = anthropic.Anthropic(
        api_key=ANTHROPIC_AUTH_TOKEN,
        base_url=ANTHROPIC_BASE_URL,
        timeout=float(os.environ.get("STAGE_B_TIMEOUT_SEC", "1800")),
        max_retries=1,
    )

    # Some Anthropic-compatible providers don't support all stop/beta headers — keep it minimal.
    log(
        f"B2: calling {ANTHROPIC_MODEL} @ {ANTHROPIC_BASE_URL} (max_tokens={max_tokens})…"
    )

    msg = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )

    if getattr(msg, "stop_reason", None) == "max_tokens":
        log("WARN: response hit max_tokens — output may be truncated")

    parts = []
    for block in msg.content:
        # The provider returns a separate block for the model's reasoning
        # (its `.text` is None and the content sits in `.thinking`). We only
        # want the answer, not the chain of thought.
        text = getattr(block, "text", None)
        if text:
            parts.append(text)
    if not parts:
        # No answer block at all — fall back to whatever reasoning we got.
        for block in msg.content:
            thinking = getattr(block, "thinking", None)
            if thinking:
                parts.append(thinking)
    return "\n".join(parts).strip()


def parse_llm_output(
    text: str, run_dir: Path | None = None
) -> tuple[str | None, list[tuple[str, str, str]]]:
    """Parse the LLM's response into VERDICT.md + per-direction files.

    Strategy: look for code-fenced blocks tagged `verdict` and `direction:<slug>`.
    If no fences, fall back to a simple heuristic: split on `## 1. `, `## 2. ` etc.
    Returns (verdict_markdown, [(slug, tier, markdown), ...]).
    """
    verdict_md = None
    directions: list[tuple[str, str, str]] = []

    # Pattern: ```verdict ... ``` or ```direction:slug ... ```
    fence_re = re.compile(
        r"```(verdict|direction:([a-z0-9\-]+))\s*\n(.*?)```",
        re.DOTALL,
    )
    for m in fence_re.finditer(text):
        kind = m.group(1)
        body = m.group(3).strip()
        if kind == "verdict":
            verdict_md = body
        else:
            slug = m.group(2)
            tier = "go-narrow" if "GO_NARROW" in body[:300].upper() else "go"
            directions.append((slug, tier, body))

    if verdict_md and directions:
        return verdict_md, directions

    # A truncated response can leave the last fenced block unterminated. Recover
    # it by splitting on the fence markers ourselves.
    if not directions:
        head_re = re.compile(
            r"```(verdict|direction:([a-z0-9\-]+))\s*\n", re.IGNORECASE
        )
        marks = list(head_re.finditer(text))
        for i, m in enumerate(marks):
            kind = m.group(1).lower()
            end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
            body = text[m.end() : end].rstrip()
            if body.endswith("```"):
                body = body[:-3].rstrip()
            body = body.strip()
            if not body:
                continue
            if kind == "verdict":
                verdict_md = verdict_md or body
            else:
                slug = m.group(2)
                tier = "go-narrow" if "GO_NARROW" in body[:300].upper() else "go"
                directions.append((slug, tier, body))
        if directions:
            log(f"  recovered {len(directions)} block(s) from an unterminated fence")

    # Heuristic fallback: split on "# " and "## "
    if not verdict_md:
        if not directions:
            log("  no fenced blocks — using heuristic split")
        verdict_md = text.split("# ")[0].strip() or (
            "# Verdict\n\n(LLM did not emit a `verdict` block)\n"
        )
    return verdict_md, directions


# ---------------------------------------------------------------------------
# Verdict table parsing
# ---------------------------------------------------------------------------

SELECTABLE_HEADER_RE = re.compile(
    r"selectable\s+directions", re.IGNORECASE
)


def parse_selectables_table(verdict_md: str) -> list[dict]:
    """Extract the selectable rows from a VERDICT.md selectables table.

    Expected shape (loop/templates/verdict.md):
        | # | slug | tier | demand | competition | one-liner | why selectable |
    """
    rows: list[dict] = []
    lines = verdict_md.splitlines()
    in_table = False
    for line in lines:
        if SELECTABLE_HEADER_RE.search(line):
            in_table = True
            continue
        if in_table:
            stripped = line.strip()
            if stripped.startswith("|---") or stripped.startswith("| ---"):
                continue
            if stripped.startswith("|"):
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                if len(cells) < 4:
                    continue
                try:
                    rank = int(cells[0].strip().strip("`"))
                except ValueError:
                    continue
                slug = cells[1].strip().strip("`").strip()
                if not slug:
                    continue
                tier = "GO_NARROW" if "NARROW" in cells[2].upper() else "GO"
                demand = cells[3].split("/")[0].strip()
                competition = cells[4].split("/")[0].strip() if len(cells) > 4 else ""
                one_liner = cells[5].strip() if len(cells) > 5 else ""
                why = cells[6].strip() if len(cells) > 6 else ""
                rows.append(
                    {
                        "rank": rank,
                        "slug": slug,
                        "tier": tier,
                        "demand": demand,
                        "competition": competition,
                        "one_liner": one_liner,
                        "why": why,
                    }
                )
            elif rows:
                in_table = False
    rows.sort(key=lambda r: r["rank"])
    return rows


# ---------------------------------------------------------------------------
# B2 — split LLM calls
#
# One giant call (VERDICT + 5 full direction packages) blows two limits:
# the provider's own generation deadline, and max_tokens. So B2 is split:
#   call 1  → VERDICT.md (selectables table)
#   call 2..N → one direction package each, in parallel
# ---------------------------------------------------------------------------

MAX_SELECTABLES = 5
MIN_SELECTABLES = 3


def load_scoring_config() -> tuple[int, int]:
    """Read min/max selectable counts from loop/config.json."""
    try:
        cfg = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        sc = cfg.get("scoring", {})
        return (
            int(sc.get("min_selectable_directions", MIN_SELECTABLES)),
            int(sc.get("max_selectable_directions", MAX_SELECTABLES)),
        )
    except Exception:
        return MIN_SELECTABLES, MAX_SELECTABLES


def build_context(
    report_md: str, candidates_csv: str, evidence: dict, seed_index: str
) -> str:
    """The shared context block fed to every B2 call."""
    evidence_bundle = json.dumps(evidence, indent=2, ensure_ascii=False)
    if len(evidence_bundle) > 100_000:
        evidence_bundle = evidence_bundle[:100_000] + "\n…(truncated)\n"
    return f"""# Stage A report (auto-generated)

{report_md}

# Candidates CSV (full)

```
{candidates_csv}
```

# Search evidence (B1 — TinyFish results per slug)

```json
{evidence_bundle}
```

# Prior validated directions (seed — from `reports/directions/INDEX.md`)

{seed_index}
"""


def call_verdict(
    agent_prompt: str, context: str, attempt: int = 1, raw_path: Path | None = None
) -> tuple[str, list[dict]]:
    """Call 1 — ask for VERDICT.md only. Returns (verdict_md, selectables)."""
    extra = ""
    if attempt > 1:
        extra = (
            "\n\n**Correction:** the previous attempt did not yield 3–5 selectables. "
            "You MUST produce at least 3 rows in the selectables table. If pure GO "
            "candidates are fewer than 3, add GO_NARROW directions with an explicit "
            "wedge. Do not stop early.\n"
        )

    user_prompt = f"""{context}
{extra}
# Your task (this call covers the VERDICT only)

Execute step 2 (scoring the candidate pool) and step 3A (VERDICT.md) of your
system prompt. Score the candidates using the search evidence above, then emit
**only** the VERDICT.md content in a single fenced block:

```verdict
# Verdict — {run_id}

## Selectable directions (3–5) — pick one

| # | slug | tier | demand | competition | one-liner | why selectable |
|---|---|---|:-:|:-:|---|---|
| 1 | `slug-one` | GO | 4/5 | 3/5 | … | … |

## Ranked recommendation (still give choice)
## WATCH
## KILL
## Handles
```

Rules:
- The selectables table MUST have between 3 and 5 rows, and every row MUST be a
  real candidate from the candidate pool above (Track B / Starter Story rows are
  context only — never selectable).
- The `slug` column must be a kebab-case identifier, e.g. `pen-plotter-optimizer`.
- `tier` is `GO` or `GO_NARROW`. `demand` and `competition` are `N/5`.
- Do NOT write any direction packages in this call — a separate call does that.
- Output nothing outside the fenced block.
"""
    raw = b2_llm_call(agent_prompt, user_prompt, max_tokens=24000)
    if raw_path:
        raw_path.write_text(raw, encoding="utf-8")
    verdict_md, _ = parse_llm_output(raw)
    if not verdict_md or "selectable" not in verdict_md.lower():
        # The model skipped the fence — fall back to the whole response.
        verdict_md = raw.strip()
    selectables = parse_selectables_table(verdict_md)
    return verdict_md, selectables


def call_direction(
    agent_prompt: str,
    context: str,
    verdict_md: str,
    sel: dict,
    evidence: dict,
    raw_path: Path | None = None,
) -> tuple[str, str, str]:
    """Call 2..N — one complete direction package."""
    slug = sel["slug"]
    slug_ev = json.dumps(evidence.get(slug, {}), indent=2, ensure_ascii=False)
    tier = sel.get("tier", "GO")
    wedge_note = (
        "\nThis direction is **GO_NARROW** — you MUST end with a "
        "`## Wedge (required for GO_NARROW)` section naming exactly what you "
        "refuse to build (one vertical / one feature / one ICP).\n"
        if "NARROW" in tier.upper()
        else ""
    )
    user_prompt = f"""{context}
# VERDICT.md for this run (the comparison table and your scoring)

```verdict
{verdict_md}
```

# Search evidence for THIS direction only ({slug})

```json
{slug_ev}
```

# Your task (this call covers ONE direction package)

Write the complete direction package for **{slug}**.

- tier: **{tier}**, demand {sel.get("demand", "?")}/5, competition {sel.get("competition", "?")}/5
- one-liner from the verdict: {sel.get("one_liner", "")}
- why it is selectable: {sel.get("why", "")}
{wedge_note}
Use `loop/templates/direction-{'go-narrow' if 'NARROW' in tier.upper() else 'go'}.md`
as the structure. Include ALL of its sections:
1. Why this direction (TrustMRR evidence + X/web evidence)
2. Competitor table (L1/L2/L3)
3. PRD MVP (P0/P1/P2 + non-goals)
4. 14-day day-by-day build plan
5. 30-day marketing calendar with budget ≤ $300
6. Unit economics to $10K MRR
7. Kill criteria
{"8. Wedge section (GO_NARROW only)" if "NARROW" in tier.upper() else ""}

Emit ONLY the direction markdown in a single fenced block tagged
```direction:{slug}
Do not write any other direction package. Do not output anything outside the fence.
"""
    raw = b2_llm_call(agent_prompt, user_prompt, max_tokens=32000)
    if raw_path:
        raw_path.write_text(raw, encoding="utf-8")
    _v, directions = parse_llm_output(raw)
    body = None
    for s, _t, b in directions:
        if s == slug:
            body = b
            break
    if body is None and directions:
        body = directions[0][2]
    if body is None:
        # No fence — use the raw response, minus any stray fence markers.
        body = raw.strip()
        for marker in ("```" + f"direction:{slug}", "```"):
            if body.startswith(marker):
                body = body[len(marker) :]
        if body.endswith("```"):
            body = body[:-3]
        body = body.strip()
    tier_norm = "go-narrow" if "NARROW" in tier.upper() else "go"
    return slug, tier_norm, body


def main() -> None:
    state = load_state()
    run_dir = run_dir_for(state)
    if not run_dir.exists():
        log(f"FATAL: run dir missing: {run_dir}")
        sys.exit(1)

    global run_id
    run_id = state["last_run_id"]

    log(f"run_id={run_id}")
    report_md, candidates_csv, candidates = load_report_and_candidates(run_dir)
    log(f"loaded {len(candidates)} candidates from candidates.csv")

    # ----- B1: TinyFish sweep -----
    evidence = b1_tinyfish_sweep(run_dir, candidates)
    log(f"B1 done — evidence for {len(evidence)} slugs")

    # ----- B2: LLM calls -----
    agent_prompt = AGENT_PROMPT.read_text(encoding="utf-8")
    seed_index = (SEED_DIR / "INDEX.md").read_text(encoding="utf-8") if (SEED_DIR / "INDEX.md").exists() else ""
    context = build_context(report_md, candidates_csv, evidence, seed_index)

    raw_dir = run_dir / "llm_raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    min_sel, max_sel = load_scoring_config()
    log(f"selectable target: {min_sel}–{max_sel}")

    # --- call 1: the verdict ---
    verdict_md, selectables = call_verdict(
        agent_prompt, context, attempt=1, raw_path=raw_dir / "verdict.md"
    )
    if len(selectables) < min_sel:
        log(f"  only {len(selectables)} selectable(s) — retrying the verdict call")
        verdict_md, selectables = call_verdict(
            agent_prompt, context, attempt=2, raw_path=raw_dir / "verdict_retry.md"
        )

    if not selectables:
        log("FATAL: no selectables parsed from the verdict")
        (run_dir / "VERDICT.md").write_text(verdict_md, encoding="utf-8")
        sys.exit(6)

    selectables = selectables[:max_sel]
    log(f"verdict selectables: {', '.join(s['slug'] for s in selectables)}")

    (run_dir / "VERDICT.md").write_text(verdict_md, encoding="utf-8")
    log(f"wrote VERDICT.md ({len(verdict_md)} bytes)")

    # --- calls 2..N: one direction package each, in parallel ---
    dirs_dir = run_dir / "directions"
    dirs_dir.mkdir(parents=True, exist_ok=True)
    for old in dirs_dir.glob("*.md"):
        old.unlink()

    def one(sel: dict) -> tuple[str, str, str]:
        try:
            return call_direction(
                agent_prompt,
                context,
                verdict_md,
                sel,
                evidence,
                raw_path=raw_dir / f"direction_{sel['slug']}.md",
            )
        except Exception as e:  # a single failed direction must not kill the run
            log(f"  direction {sel['slug']} FAILED: {e}")
            return sel["slug"], "go", ""

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        results = list(ex.map(one, selectables))

    directions: list[tuple[str, str, str]] = []
    for slug, tier, body in results:
        if not body:
            log(f"  no content for {slug} — skipped")
            continue
        final = f"{body.rstrip()}\n"
        (dirs_dir / f"{slug}.md").write_text(final, encoding="utf-8")
        log(f"wrote directions/{slug}.md ({tier}, {len(final)} bytes)")
        directions.append((slug, tier, body))

    selectable_count = len(directions)
    log(f"selectables produced: {selectable_count}")

    # ----- Update state -----
    state["agent_stage"] = "done"
    state["selectable_count"] = selectable_count
    state["notes"] = (
        f"{selectable_count} selectables: "
        + ", ".join(s for s, _, _ in directions)
    )
    state["agent_stage_utc"] = datetime.now(timezone.utc).isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

    if selectable_count < min_sel:
        log(f"FATAL: only {selectable_count} selectables (minimum {min_sel})")
        sys.exit(6)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("interrupted")
        sys.exit(130)
