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


def b2_llm_call(system_prompt: str, user_prompt: str, max_tokens: int = 32000) -> str:
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

    parts = []
    for block in msg.content:
        if hasattr(block, "text"):
            parts.append(block.text)
    return "\n".join(parts).strip()


def parse_llm_output(
    text: str, run_dir: Path
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

    # Heuristic fallback: split on "# " and "## "
    log("  no fenced blocks — using heuristic split")
    if not verdict_md:
        verdict_md = text.split("# ")[0].strip() or (
            "# Verdict\n\n(LLM did not emit a `verdict` block)\n"
        )
    return verdict_md, directions


def main() -> None:
    state = load_state()
    run_dir = run_dir_for(state)
    if not run_dir.exists():
        log(f"FATAL: run dir missing: {run_dir}")
        sys.exit(1)

    log(f"run_id={state['last_run_id']}")
    report_md, candidates_csv, candidates = load_report_and_candidates(run_dir)
    log(f"loaded {len(candidates)} candidates from candidates.csv")

    # ----- B1: TinyFish sweep -----
    evidence = b1_tinyfish_sweep(run_dir, candidates)
    log(f"B1 done — evidence for {len(evidence)} slugs")

    # ----- B2: LLM call -----
    agent_prompt = AGENT_PROMPT.read_text(encoding="utf-8")
    seed_index = (SEED_DIR / "INDEX.md").read_text(encoding="utf-8") if (SEED_DIR / "INDEX.md").exists() else ""

    # Concatenate evidence into a bounded JSON bundle
    evidence_bundle = json.dumps(evidence, indent=2, ensure_ascii=False)
    # Cap each piece so the prompt fits comfortably in 200K context
    if len(evidence_bundle) > 100_000:
        evidence_bundle = evidence_bundle[:100_000] + "\n…(truncated)\n"

    user_prompt = f"""# Stage A report (auto-generated)

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

# Your task

Execute the Stage B contract in your system prompt exactly. Emit your output as:

1. A single fenced block tagged ```verdict containing the full VERDICT.md content.
2. One fenced block per selectable direction tagged ```direction:<slug> containing the full direction markdown.

If a direction is GO_NARROW, include a `## Wedge (required for GO_NARROW)` section at the end.
Use the templates in `loop/templates/` as your structure — fill in the placeholders.

Do not output anything outside the fenced blocks.
"""

    raw = b2_llm_call(agent_prompt, user_prompt)

    # ----- Parse + write artifacts -----
    verdict_md, directions = parse_llm_output(raw, run_dir)

    if verdict_md:
        (run_dir / "VERDICT.md").write_text(verdict_md, encoding="utf-8")
        log(f"wrote VERDICT.md ({len(verdict_md)} bytes)")
    else:
        log("WARN: no verdict block parsed")

    dirs_dir = run_dir / "directions"
    dirs_dir.mkdir(parents=True, exist_ok=True)
    # Clear any previous run's directions
    for old in dirs_dir.glob("*.md"):
        old.unlink()

    for slug, tier, body in directions:
        template_name = f"direction-{tier}.md"
        template = (TEMPLATE_DIR / template_name).read_text(encoding="utf-8")
        # We don't try to fill the template — the LLM is told to use it as structure.
        # Just stamp a small header on top so each file is identifiable.
        final = f"{body.rstrip()}\n"
        (dirs_dir / f"{slug}.md").write_text(final, encoding="utf-8")
        log(f"wrote directions/{slug}.md ({tier}, {len(final)} bytes)")

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

    if selectable_count < 3:
        log(f"FATAL: only {selectable_count} selectables (minimum 3)")
        sys.exit(6)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("interrupted")
        sys.exit(130)
