---
name: opportunity-loop
description: Run the TrustMRR opportunity loop (Stage A: TrustMRR fetch + coarse filter; Stage B: web/TinyFish verify + 3–5 selectable direction packages). Use when the user asks to scan TrustMRR for startup ideas, run the weekly opportunity loop, find this week's startup directions, generate direction packages, or check what to ship next. Triggers on phrases like "run opportunity loop", "scan TrustMRR", "find weekly directions", "what should I build this week", "TrustMRR + X verification".
type: Workflow
tags: trustmrr, opportunity-loop, weekly, x10k, mrr, startup-discovery, direction-radar
---

# Opportunity Loop — weekly startup direction radar

This skill wraps the existing `loop/` system into a one-shot invocation. Stage A is non-interactive (TrustMRR fetch + coarse filter); Stage B is the LLM-driven verification + direction packaging defined in `loop/AGENT_PROMPT.md`.

The same contract is automated weekly via `.github/workflows/weekly.yml` in CI — see README.

## Pre-flight

1. Verify `loop/` exists and `loop/run.sh` is executable (`bash loop/run.sh` works).
2. Confirm `tinyfish auth` is set up (run `tinyfish search query --pretty "test"` — should return results).
3. Read `loop/state/last_run.json` to find the last run id (if any). New run will overwrite.

## Step 1 — Stage A (TrustMRR fetch + coarse filter)

```bash
cd <repo-root>   # the directory containing loop/
bash loop/run.sh
```

Produces `loop/runs/<run_id>/` with `REPORT.md`, `candidates.csv`, `filtered.json`, `trustmrr_raw.json`, `state_snapshot.json`, and writes `loop/state/last_run.json`.

If Stage A exits non-zero, check `loop/runs/<id>/error.json`. Likely causes: TrustMRR API drift (URL or auth changed), network outage. Do NOT proceed to Stage B without a clean Stage A.

## Step 2 — Read Stage A artifacts

1. `loop/state/last_run.json` → `run_dir`
2. `loop/runs/<run_id>/REPORT.md` → auto-scored clusters and GO_CANDIDATEs
3. `loop/runs/<run_id>/candidates.csv` → sortable candidate table
4. `loop/seed_directions/INDEX.md` → prior validated directions as evidence (read-only)

## Step 3 — Stage B (LLM verification + direction packaging)

You (Claude) are now the Stage B executor. **The contract is `loop/AGENT_PROMPT.md` — read it first, follow it exactly.** Do not invent your own methodology.

Key constraints from AGENT_PROMPT.md:
- Target: **3–5 selectable directions** (config `min_selectable_directions: 3`, `target: 5`)
- Hard gate: **demand ≥ 3 AND competition ≤ 3** → pure **GO**
- If pure GO < 3: add **GO_NARROW** (unbundle of a hotter market, competition 4 allowed only with explicit wedge)
- 14-day solo MVP, $300/30-day marketing, $10K MRR target
- Always emit ≥ 3 directions, never stop at 1

### 3a — Verify with web search

For each GO_CANDIDATE and top 3 WATCH by MRR:

Use the TinyFish CLI (already configured locally):
- Competition: `tinyfish search query --pretty "{name} {category} alternatives 2026"`
- Pain: `tinyfish search query --pretty "{name} (painful OR broken OR hate OR expensive OR looking for)"`
- Recommend intent: `tinyfish search query --pretty "looking for OR recommend OR alternative {name}"`

Score `demand` (1–5) and `competition` (1–5) per AGENT_PROMPT.md's table.

### 3b — Decide verdict

| demand | competition | verdict |
|---|---|---|
| ≥3 | ≤3 | **GO** |
| ≥3 | 4 | **GO_NARROW** only with explicit wedge |
| ≥3 | 5 | KILL |
| <3 | any | WATCH or KILL |

### 3c — Write artifacts

Use `loop/templates/` as structure:

- `loop/templates/verdict.md` → write to `loop/runs/<id>/VERDICT.md`
- `loop/templates/direction-go.md` → for each GO
- `loop/templates/direction-go-narrow.md` → for each GO_NARROW (must include `## Wedge (required for GO_NARROW)` section)

Filenames: `loop/runs/<id>/directions/<slug>.md`.

Append handles to `loop/runs/<id>/handles.csv` (≥ 10 rows required).

### 3d — Update state

Write `loop/state/last_run.json` with:
```json
"agent_stage": "done",
"selectable_count": N,
"notes": "N selectables: slug1, slug2, ..."
```

## Step 4 — Done definition (per AGENT_PROMPT.md)

- `VERDICT.md` lists **3–5** selectables ✓
- **3–5** files under `directions/*.md` with full PRD+14d+30d ✓
- `handles.csv` has ≥ 10 rows ✓
- `state/agent_stage = done`, `selectable_count ≥ 3` ✓

## Step 5 — Report back to user

Show:
1. The selectable directions table (from VERDICT.md)
2. Your ranked recommendation (still let the user pick)
3. WATCH + KILL lists
4. The full run folder path

Suggest: "Say `/build <slug>` to start the 14-day MVP for your pick." (Or whatever next-step command the user prefers.)

## Out of scope for this skill

- Building the actual MVP (different skill)
- Cron / GitHub Action setup (one-time repo setup, not a session task)
- Modifying `loop/config.json` thresholds (only the user changes these)

## Reference

- Source contract: `loop/AGENT_PROMPT.md` (the canonical Stage B spec)
- Playbook (deep methodology): `loop/PLAYBOOK.md`
- Pipeline: `loop/pipeline.py` (Stage A)
- Templates: `loop/templates/`
- Prior validated directions: `loop/seed_directions/` (do not modify — evidence pool)
