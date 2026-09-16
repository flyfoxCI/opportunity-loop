# Opportunity Loop — TrustMRR startup-direction radar (runs every 3 days)

> **Mission:** every Tuesday and Friday morning, surface 3–5 selectable startup
> directions from TrustMRR + X/web signals — each one a complete PRD + 14-day MVP +
> 30-day marketing plan ready to ship.

The system runs automatically via GitHub Action (`Mon + Thu 17:00 UTC` = `Tue + Fri 01:00 Beijing`). Twice a week — fast enough to catch fresh TrustMRR listings within 72 hours. Results publish to GitHub Pages as a searchable history.

**Live site:** `https://<your-github-user>.github.io/opportunity-loop/`

---

## Architecture

```
loop/                       Stage A (TrustMRR) + Stage B (LLM) + templates + seed
  pipeline.py               Stage A — pure Python stdlib, no secrets
  AGENT_PROMPT.md           Stage B contract — the canonical spec
  config.json               thresholds, scoring, keywords
  run.sh                    Stage A entry point
  templates/
    verdict.md              VERDICT.md skeleton
    direction-go.md         pure-GO direction template
    direction-go-narrow.md  GO_NARROW template (with Wedge section)
  seed_directions/          six prior validated direction packages (read-only)
  PLAYBOOK.md               full methodology (read by skill + humans)

stage_b.py                  Stage B orchestrator (TinyFish + MiniMax)
publish.py                  copies run → docs/, regenerates docs/index.md, git push
.github/workflows/weekly.yml  cron + manual trigger
docs/                       GitHub Pages output (auto-regenerated weekly)
SKILL.md                    Claude Code slash command
install.sh                  cp SKILL.md → ~/.claude/skills/opportunity-loop/
_config.yml                 Jekyll (Pages) config — minima theme
```

**Pipeline flow:**

```
       Mon + Thu 17:00 UTC (cron, every ~3 days) or manual trigger
                        ↓
   ┌───────────────────────────────────────┐
   │  Stage A — loop/run.sh                │
   │  • Fetch TrustMRR public API          │
   │  • Coarse filter + cluster            │
   │  • Heuristic score (auto_verdict)     │
   │  • Smoke check (non-empty response)   │
   └───────────────────────────────────────┘
                        ↓
   ┌───────────────────────────────────────┐
   │  Stage B — stage_b.py                 │
   │  B1: TinyFish CLI (parallel queries)  │
   │  B2: MiniMax messages.create          │
   │      → VERDICT.md + 3–5 directions/   │
   └───────────────────────────────────────┘
                        ↓
   ┌───────────────────────────────────────┐
   │  Publish — publish.py                 │
   │  • cp loop/runs/<id> → docs/runs/<id> │
   │  • regenerate docs/index.md           │
   │  • git commit + push to main          │
   └───────────────────────────────────────┘
                        ↓
       GitHub Pages auto-rebuilds
```

---

## Setup

### 1. Create the GitHub repo

```bash
# from this directory
gh repo create opportunity-loop --public --source=. --remote=origin --push
# (or manually: create empty repo on GitHub, then `git remote add origin git@github.com:<user>/opportunity-loop.git && git push -u origin main`)
```

### 2. Enable GitHub Pages

Settings → Pages → Build from branch → Branch: `main` · Folder: `/docs` → Save.

The site will be live at `https://<user>.github.io/opportunity-loop/` within ~30 seconds of the first push.

### 3. Add repo secrets

Settings → Secrets and variables → Actions → New repository secret:

| Secret | Value | Required |
|---|---|---|
| `ANTHROPIC_BASE_URL` | `https://api.minimaxi.com/anthropic` | yes |
| `ANTHROPIC_AUTH_TOKEN` | your MiniMax / Anthropic-compatible token | yes |
| `TINYFISH_API_KEY` | your TinyFish API key (run `tinyfish auth` locally to get one) | yes |
| `ANTHROPIC_MODEL` | `MiniMax-M3` (default if unset) | no |

The action reads these same env-var names that your local `~/.claude/settings.json` uses — no special MiniMax magic.

### 4. Install the slash command (local)

```bash
bash install.sh
# → Installed: ~/.claude/skills/opportunity-loop/SKILL.md
```

Then in any Claude Code session, `/opportunity-loop` (or describe what you want) triggers the skill.

### 5. (Optional) Adjust the cron

`.github/workflows/weekly.yml` currently fires `0 17 * * 1,4` UTC = **Tuesday + Friday 01:00 Beijing** (~every 3 days).
Edit the cron expression if your cadence needs differ:

- `'0 17 * * 0'` — once a week (Sun)
- `'0 17 * * 1,4'` — twice a week (Mon + Thu) ← current
- `'0 17 */2 * *'` — every 2 days
- `'0 17 * * *'` — daily (not recommended, $9/mo LLM cost)

See [crontab.guru](https://crontab.guru/).

---

## Local usage

```bash
cd /Users/jerry/code/10k-in-month/opportunity-loop

# Stage A only
bash loop/run.sh

# Stage A + B (requires ANTHROPIC_* and TINYFISH_API_KEY in env)
export ANTHROPIC_BASE_URL=https://api.minimaxi.com/anthropic
export ANTHROPIC_AUTH_TOKEN=sk-...
export ANTHROPIC_MODEL=MiniMax-M3
export TINYFISH_API_KEY=...
python stage_b.py

# Publish to docs/ + git push (requires git remote set up)
python publish.py
```

Or via the skill:

```
/opportunity-loop
```

The skill will run Stage A, then act as the Stage B LLM executor, then publish.

---

## Troubleshooting

### Stage A fails — empty listings

`loop/runs/<id>/error.json` will have the curl / TrustMRR response. Common causes:

- **TrustMRR API drift**: the endpoint or response shape changed. Check `https://trustmrr.com/api/ai` manually. If they require auth now, add a `TRUSTMRR_API_KEY` secret and update `pipeline.py:fetch_json` to pass `Authorization: Bearer $TRUSTMRR_API_KEY`.
- **Network outage**: re-run via `workflow_dispatch` after.

### Stage B fails — LLM error

Symptoms: action exits 5, no `VERDICT.md` written. Check the action logs:

- **Auth error**: `ANTHROPIC_AUTH_TOKEN` is wrong or expired. Test locally with the same env vars.
- **Model not found**: confirm `ANTHROPIC_MODEL` matches a model your provider serves. Default is `MiniMax-M3`.
- **Context too long**: 32K max_tokens may be exceeded for 5 direction packages. Reduce to 4 directions in `AGENT_PROMPT.md`'s `max_selectable_directions` config, or split `stage_b.py:b2_llm_call` into two calls.

### Stage B fails — TinyFish error

Symptoms: `search_evidence/*.json` files have `error` field set. Likely: `tinyfish auth` not run, or API key rate-limited.

The action catches this in `B1` and exits 4 — Stage A artifacts are preserved as workflow artifacts (Settings → Actions → failed run → Artifacts).

### Publish fails — git push error

- **No remote**: `git remote add origin git@github.com:<user>/opportunity-loop.git`
- **Permission denied**: workflow's `GITHUB_TOKEN` has `contents: write` set explicitly. For cross-repo pushes, you'd need a PAT.
- **Conflicts**: another run is in progress. The `concurrency:` block in `weekly.yml` serializes runs; if it still happens, `git pull --rebase` then re-run.

### Pages site doesn't update

- Settings → Pages → confirm `main` / `/docs` is selected
- Check the Actions tab — did `Publish` step succeed?
- Hard-refresh browser (Cmd-Shift-R) — Pages caches for ~1 min

---

## Files of interest

- **`loop/AGENT_PROMPT.md`** — the Stage B contract. Don't modify casually; both the local skill and CI read this.
- **`loop/config.json`** — all hard thresholds. Change `target_selectable_directions` to up/down the output count.
- **`loop/seed_directions/`** — six prior validated direction packages as evidence. Read-only.
- **`loop/templates/`** — the three skeleton templates (verdict, direction-go, direction-go-narrow).
- **`.github/workflows/weekly.yml`** — cron schedule + step ordering. `concurrency:` prevents run collisions.

---

## Migrating from the original `loop/` system

If you've been using `/Users/jerry/code/10k-in-month/loop/` locally:

- The two systems are independent after this split. The new repo vendors a copy.
- `loop/runs/` in the old location is gitignored — keep using it for local manual runs.
- The new repo's `stage_b.py` automates Stage B with TinyFish + MiniMax; locally you can still execute Stage B interactively (the `SKILL.md` describes how).
- `reports/directions/01–06-*.md` are mirrored into `loop/seed_directions/` as evidence; if you add new validated directions, copy them into both locations.

---

## License & attribution

Methodology: derived from the [TrustMRR × X Opportunity Playbook](../loop/PLAYBOOK.md).
Data source: [TrustMRR](https://trustmrr.com) public listings API.

