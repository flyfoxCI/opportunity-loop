# Agent Stage Prompt — Opportunity Loop (Steps 3–7)

**When to run:** After `./run.sh` or `python3 pipeline.py` succeeds.  
**Input:** Latest folder in `loop/runs/` (see `loop/state/last_run.json` → `run_dir`).  
**Output:** Write into that same run folder (do not invent a new method).

---

## Goal constraints (hard)

- Target: **$10K MRR**
- MVP: **≤ 14 days**, solo
- Marketing: **≤ $300 / 30 days**, organic-first
- Dual gate: **demand ≥ 3 AND competition ≤ 3** → pure **GO**
- **Output count (hard):** produce **3–5 selectable directions** every run (config: `min_selectable_directions`–`max_selectable_directions`)
  - Prefer pure GO
  - If pure GO < 3: add **GO_NARROW** = unbundle of a hotter market (competition 4 allowed **only** with a written narrow wedge)
  - Never stop at 1 direction package

---

## Instructions (execute in order)

### 0. Load context

1. Read `loop/config.json`
2. Read `loop/state/last_run.json`
3. Read `{run_dir}/REPORT.md` and `{run_dir}/candidates.csv`
4. Read `reports/trustmrr-x-opportunity-playbook.md` if unclear
5. Optionally re-use prior deep packs under `reports/directions/01–06` and `vibecheck/` as evidence—not as the only GO

### 1. Candidate pool

- All `GO_CANDIDATE` from Stage A
- Top WATCH by MRR
- Prior validated niches if needed to hit **3–5 selectables** (security, vertical cert coach, pen-plot, trade leads, heritage language, YouTube-only parental, etc.)
- Max 12 candidates scored; max 5 become full packages

### 2. For each candidate (max 20 min each)

**Competition (desktop):**

- Search: `"{product or category} alternatives 2026"`
- List L1 direct competitors with pricing if found
- Assign **competition score 1–5** (see playbook)

**X / social demand:**

Use search tools (TinyFish/X/web) with queries from config:

- pain / recommend / competitor hate / just shipped  
  Fill keywords from candidate name + category.

Assign **demand score 1–5**.

**Decision:**

| demand | competition | verdict |
|---|---|---|
| ≥3 | ≤3 | **GO** (full package) |
| ≥3 | 4 | **GO_NARROW** only if wedge is explicit (one vertical / one feature / one ICP); full package required |
| ≥3 | 5 | KILL (or WATCH) |
| <3 | any | WATCH or KILL |

### 3. Write artifacts into `{run_dir}/`

#### A. `VERDICT.md` (must list 3–5 selectables)

```markdown
# Verdict — {run_id}

## Selectable directions (3–5) — pick one
| # | slug | tier (GO / GO_NARROW) | demand | competition | one-liner | why selectable |

## Ranked recommendation (still give choice)
1. ...
2. ...

## WATCH
## KILL
## Handles
```

#### B. `handles.csv` (append rows)

`handle,type,pain_quote,source_url,status,notes,run_id`

#### C. For **each of 3–5 selectables**: `directions/{slug}.md`

Use `loop/templates/direction.md`. Must include ALL sections:

1. Why this direction (TrustMRR evidence + X/web evidence)
2. Competitor table (L1/L2/L3)
3. PRD MVP (P0/P1/P2 + non-goals)
4. 14-day day-by-day build plan
5. 30-day marketing calendar with **budget ≤ $300**
6. Unit economics to $10K MRR
7. Kill criteria
8. If GO_NARROW: **Wedge** section (what you refuse to build)

#### D. Update `loop/state/last_run.json`

```json
"agent_stage": "done",
"notes": "N selectable directions: slug1, slug2, ...",
"selectable_count": 3
```

### 4. Do NOT

- Rewrite the whole methodology
- Start coding unless user says “build {slug}”
- Output only 1 direction package
- Mark full-market GO if competition ≥ 4 without GO_NARROW wedge
- Spend time on gambling/casino/sweep ethics-risk products

### 5. Done definition

- `VERDICT.md` lists **3–5** selectables
- **3–5** files under `directions/*.md` with full PRD+14d+30d
- handles.csv has ≥ 10 rows
- state agent_stage = done, selectable_count ≥ 3

---

## One-shot paste for Claude Code

```
Run the opportunity loop agent stage.
Repo root: this project.
1) Read loop/state/last_run.json
2) Follow loop/AGENT_PROMPT.md exactly
3) Output 3–5 selectable directions (not 1), each with full package in the latest loop/runs/* folder
4) Stop when Done definition is met
```
