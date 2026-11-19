# Opportunity Loop — daily breakout intelligence for solo builders

> **Mission:** every morning, show which small products (apps, SaaS, open source, mini-games,
> short drama) crossed a measurable line, why, whether buyers are asking for it, and how one or
> two people could follow — with every number labeled and linked.

Runs daily via GitHub Actions (`radar-daily.yml`, 06:30 UTC) and publishes to GitHub Pages.
The original TrustMRR direction loop (Stage A/B, PRD packages) is retired as a schedule; its
packages live on at `/archive/` and its templates feed the v3 Build Kit.

**Live site:** Cloudflare Pages, `https://<project>.pages.dev/` (deployed by `.github/workflows/deploy-cloudflare.yml`)

---

## v3 — daily breakout briefing (current)

**v3 is the product.** Every day it answers: *which small products crossed a measurable line, why,
whether buyers are asking for it, and how one or two people could follow.* Site: `docs/v3/` (the
root `/` redirects there). Design: `research/v3-design.html`; teardown of Stringers: `research/stringers-analysis.html`.

| Surface | Discovery | Measurement | Label |
|---|---|---|---|
| Apps & games | Appark top charts: iOS + Google Play, 15 countries × all + 20 genres, top 200 | Google Play detail (exact installs), iTunes Lookup (rating counts) | verified / estimated proxy |
| Web & SaaS | TrustMRR, Tranco climbers | TrustMRR payment-verified MRR, Tranco rank | verified |
| Open source | GitHub Trending, 8 languages | stars/day vs own history | verified |
| Mini-games | Gravity Engine WeChat + Douyin boards (public top 20) | rank change | verified rank |
| Short drama | Appark TikTok drama chart + drama-ad chart (30-day backfill) | creatives, impressions | estimated |
| Demand Echo | Reddit buyer-intent threads; Xiaohongshu public posts **via TinyFish only** | — | verified counts / inferred |

```bash
python -m radar collect      # all sources (or --only appark,drama,gravity,itunes,gplay,...)
python -m radar detect       # the line each product crossed today + the day's picks (radar/v3.json)
python -m radar investigate  # briefs: data-only, or agent mode when ANTHROPIC_AUTH_TOKEN is set
python -m radar playbook     # induce playbooks from the agent's per-brief plays -> data/playbook.json
python -m radar build        # docs/v3/
python -m radar all          # everything
```

- **Detection** (`radar/detect.py`, thresholds in `radar/v3.json`): today ≥ 3× the product's own
  7-day baseline above a floor. Until a product has 3 days of our own history, the source's own change
  figure is used and the card says `source delta` / `cold start`.
- **Briefs** (`radar/investigate.py`): one JSON per pick. Data-only mode computes every field from
  collected data; agent mode (LLM + TinyFish) writes the editorial fields from the gathered evidence and a
  verify step downgrades unlinked "facts" to "inferred". Grades S–E are always computed by code.
- **Synthesis** (`radar/synth.py`): directions, the product DB (one page per product with its daily
  history), D+7/14/30 track record.
- **Playbooks** (`radar/playbook.py`, modelled on `research/stringers-plays-analysis.md`): the agent reads each
  product through three lenses (direction, growth, monetization) and records the move it used, with causality
  hard / medium / weak. A daily *draft* pass groups moves shared by 2+ products into plays (recipe, mechanism, five
  steps with evidence, cases, tried-it-didn't-work, who it suits / risks, notes); a *verify* pass re-reads each
  play against its cases' full briefs, regrades causality and drops what doesn't hold. Ids are kept in
  `data/playbook.json` (committed). Breakouts that faded by D+7 are added as counter-examples automatically.
- **CI**: `.github/workflows/radar-daily.yml`, 06:30 UTC. Appark only gives guests today's charts —
  every missed day is lost history.
- Xiaohongshu: the manual CSV import (`data/xhs_tools/`) was removed in v3; only TinyFish search remains.

## v2 (retired)

v2 was the daily signals site at `/radar/`. v3 replaced it; its site output and builder were removed.
`radar/analyze.py` remains because v3 detection reuses its TrustMRR, Tranco and series helpers.

---

## Architecture

```
loop/                       Stage A (TrustMRR) + Stage B (LLM) + templates + seed
  pipeline.py               Stage A — pure Python stdlib, no secrets
  starterstory.py           Track B — Starter Story fetcher (separate track)
  AGENT_PROMPT.md           Stage B contract — the canonical spec
  config.json               thresholds, scoring, keywords, starterstory settings
  run.sh                    Stage A entry point
  templates/
    verdict.md              VERDICT.md skeleton
    direction-go.md         pure-GO direction template
    direction-go-narrow.md  GO_NARROW template (with Wedge section)
  seed_directions/          six prior validated direction packages (read-only)
  PLAYBOOK.md               full methodology (read by skill + humans)

stage_b.py                  Stage B orchestrator (TinyFish + MiniMax, split calls)
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
   │  ┌─────────────────────────────────┐  │
   │  │  Track B — starterstory.py      │  │
   │  │  • Fetch /data listing pages    │  │
   │  │  • Enrich top 60 w/ founder X   │  │
   │  │  • → STARTERSTORY.md (separate) │  │
   │  └─────────────────────────────────┘  │
   └───────────────────────────────────────┘
                        ↓
   ┌───────────────────────────────────────┐
   │  Stage B — stage_b.py                 │
   │  B1: TinyFish CLI (parallel queries)  │
   │  B2a: MiniMax → VERDICT.md            │
   │       (selectables table, 3–5 rows)   │
   │  B2b: MiniMax → directions/<slug>.md  │
   │       (one package per selectable,    │
   │        3 calls in parallel)           │
   │  (Track B is context only — never     │
   │   scored, never a selectable)         │
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

### 2. Publish on Cloudflare Pages

`.github/workflows/deploy-cloudflare.yml` builds `docs/` with Jekyll and uploads it to Cloudflare Pages after every
daily/weekly run and every push that touches `docs/`.

1. Cloudflare dashboard → Workers & Pages → Create → Pages → **Upload assets** (direct upload, not "Connect to Git")
   → project name `opportunity-loop` → upload any small file once to create it. (Or run
   `npx wrangler pages project create opportunity-loop --production-branch main`.)
2. Create an API token: My Profile → API Tokens → Create token → Custom → permission
   *Account · Cloudflare Pages · Edit*. Copy your Account ID from the Workers & Pages overview.
3. Repo → Settings → Secrets and variables → Actions: add `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`
   (and a variable `CF_PAGES_PROJECT` if you named the project differently).
4. Actions → "deploy to Cloudflare Pages" → Run workflow. The site is at `https://opportunity-loop.pages.dev/`.
5. Optional: Pages project → Custom domains. Once Cloudflare works, turn off GitHub Pages (Settings → Pages → None).

### 3. Add repo secrets

Settings → Secrets and variables → Actions → New repository secret:

| Secret | Value | Required |
|---|---|---|
| `ANTHROPIC_BASE_URL` | `https://api.minimaxi.com/anthropic` | yes |
| `ANTHROPIC_AUTH_TOKEN` | your MiniMax / Anthropic-compatible token | yes |
| `TINYFISH_API_KEY` | your TinyFish API key (run `tinyfish auth` locally to get one) | yes |
| `ANTHROPIC_MODEL` | `MiniMax-M3` (default if unset) | no |
| `STARTERSTORY_COOKIE` | a free Starter Story account's session cookie — unlocks full pagination for Track B | no |

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

## Track B — Starter Story (separate track)

TrustMRR is the only source that feeds the automatic scoring. Alongside it, every run also
harvests [Starter Story](https://www.starterstory.com/data) — a database of ~3,500 real
businesses with revenue, category, monetization model and founder details — as a **separate
inspiration track**.

**Why separate:** Starter Story labels its revenue figures as research estimates
("*Estimated from public sources by our research agent — not self-reported*"), while
TrustMRR exposes verified MRR. Mixing estimated revenue into the same candidate pool lets a
wrong number become a GO_CANDIDATE. So Track B rows are never merged into `filtered.json` /
`candidates.csv`, never scored, and never counted toward the 3–5 selectables. A human
promotes an idea by hand.

**What a run produces:**

| Artifact | Contents |
|---|---|
| `starterstory_raw.json` | every harvested business, pre-filter |
| `starterstory_candidates.csv` | in-band rows with revenue, category, founder, X handle |
| `STARTERSTORY.md` | the "solo sweet spot" table (closest analogues to a 14-day solo MVP) + the biggest in-band businesses |

**How it works:** Starter Story has no public JSON API — the database is server-rendered
HTML at `/data`. `loop/starterstory.py` walks a matrix of listing queries (`sort=`,
`search=`, `category=`, `starting_costs=`), parses each row's revenue badge, then fetches the
detail page of the top 60 candidates to add description, category and the founder's X handle.
Requests are sequential and paced — a burst of parallel requests earns a `429`, so the
fetcher delays between calls and backs off on `429`/`5xx`. Detail pages are cached under
`loop/cache/starterstory/` for 14 days, so repeat runs cost almost nothing.

**Config** (`loop/config.json` → `starterstory`):

| Key | Default | Meaning |
|---|---|---|
| `enabled` | `true` | set `false` to skip Track B entirely |
| `base_url` | `https://www.starterstory.com` | |
| `session_cookie` | `""` | set to a free-account session cookie to unlock full pagination (CI: `STARTERSTORY_COOKIE` secret) |
| `list_paths` | 18 queries | the listing-query matrix to walk |
| `max_pages` | `5` | pages to follow per query (only when a cookie is set) |
| `enrich_top_n` | `60` | detail pages fetched per run |
| `revenue_band_usd` | `[300, 50000]` | which businesses count as in-band |
| `sweet_spot_usd` | `[500, 20000]` | the band ranked as "solo sweet spot" |
| `delay_sec` | `3.5` | pause between requests |
| `max_retries` / `backoff_sec` | `4` / `30` | retry + backoff on `429`/`5xx` |
| `cache_ttl_days` | `14` | detail-page cache lifetime |

**Coverage limits (anonymous):** the site only serves the first page of each query to
logged-out visitors, so one run sees ~200–300 of the ~3,500 businesses. A free Starter Story
account (email signup, no payment) removes the limit — paste its session cookie into
`session_cookie` and the fetcher starts following the site's own pagination links
automatically. No other change is needed.

**When it fails:** Track B never breaks the run. A failure writes
`loop/runs/<id>/starterstory_error.json` and the TrustMRR pipeline continues untouched.

---

## Stage B — split LLM calls

`stage_b.py` does **not** ask the model for `VERDICT.md` and all direction
packages in one response. One giant call hits two walls: the provider's own
generation deadline (a 64K-token request came back `500 context deadline
exceeded`) and `max_tokens` (a 32K request was cut off after 2 of 5 packages).

So B2 is split:

| Call | Produces | `max_tokens` |
|---|---|---|
| B2a | `VERDICT.md` — the selectables table, WATCH/KILL, handles | 24000 |
| B2b | one `directions/<slug>.md` per selectable, 3 in parallel | 32000 |

B2a is retried once if it returns fewer than `min_selectable_directions` rows
(3 by default, from `config.json`). Each B2b call gets the full context plus
the verdict and the search evidence for its own slug, so the packages are
independent of each other.

The provider's reasoning comes back in a separate content block from the
answer; `stage_b.py` reads only the answer block, and saves every raw response
under `loop/runs/<id>/llm_raw/` for debugging (not published).

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
- **Context too long**: B2 is already split (verdict call + one call per direction). If a single direction call still gets cut off, the raw response is in `loop/runs/<id>/llm_raw/direction_<slug>.md` and the log shows `WARN: response hit max_tokens` — lower `scoring.max_selectable_directions` in `loop/config.json` or ask the model for a tighter package.

### Stage B fails — TinyFish error

Symptoms: `search_evidence/*.json` files have `error` field set. Likely: `tinyfish auth` not run, or API key rate-limited.

The action catches this in `B1` and exits 4 — Stage A artifacts are preserved as workflow artifacts (Settings → Actions → failed run → Artifacts).

### Track B returns nothing

Symptoms: `starterstory_error.json` in the run folder, or `STARTERSTORY.md` empty.

- **`429 Too Many Requests`** — Starter Story rate-limits bursts. The fetcher already paces itself; if it still trips, raise `starterstory.delay_sec` and lower `enrich_top_n` rather than adding concurrency.
- **Markup changed** — all selectors live in `loop/starterstory.py`; a rename in the site's HTML breaks parsing in one place. Compare a cached page under `loop/cache/starterstory/` against the live page.
- **Host unreachable / DNS** — Starter Story down; the run still succeeds via TrustMRR.

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

