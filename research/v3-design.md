---
title: "Opportunity Loop v3 · Design"
author: "Opportunity Loop"
description: "From a TrustMRR radar to a multi-source, evidence-backed breakout intelligence product, designed to become a paid service in v4."
---

# Opportunity Loop v3 Design

> [!NOTE]
> **Status:** design proposal · **Date:** 2026-11-18 · **Builds on:** `radar/` v2 (SQLite store with evidence labels, 7 collectors, 40-direction taxonomy, static site, TinyFish trace) and the Stringers teardown in `research/stringers-analysis.html`.

## 0. One-Page Summary

**Product thesis.** Every morning, tell a solo builder *which small products took off yesterday, why (with evidence), whether real demand is behind it, and exactly how they could follow*, before everyone else notices.

**What changes from v2**

| | v2 (today) | v3 |
|---|---|---|
| Core source | TrustMRR (+ thin App Store RSS, GitHub Trending, Reddit, Tranco, XHS) | 12 sources across 5 surfaces: web SaaS, mobile, open source, mini-games, short drama |
| Unit of output | Direction landscape + validation kit | **Breakout item**: one product, one line it crossed, one investigation |
| Detection | Cross-product rank / percentile | **Per-entity baseline**: today ≥ 3× its own 7-day average, with absolute floors |
| Explanation | TinyFish search snippets | Agent investigation with claim-level labels, a "discount" section, retraction |
| Guidance | Validation kit per direction | Grade S–E + "how to follow" wedge + **Build Kit** (our heritage from the v1 PRD loop) |
| Knowledge layer | None | **Playbooks** induced from investigations, with cases and counter-examples |
| Trust layer | Evidence labels | Labels + **follow-up audit** (did it hold at D+14/D+30?) + a published hit rate |
| Distribution | Static site + RSS | Site (EN/ZH) + daily email + MD twins + `llms.txt` + JSON; MCP prepared for v4 |

**How we beat Stringers rather than copy it**

1. **Supply × demand cross-check.** Stringers only sees supply (products rising). We pair every breakout with demand signals it doesn't have: Reddit threads, Xiaohongshu 小工具 boards and Tranco traffic. Every item gets a **Demand Echo** score.
2. **Build Kit.** Stringers stops at "how to follow". We continue to a 72-hour validation plan, a 14-day MVP scope and a first-30-users plan. This is the v1 PRD loop, now attached to evidence.
3. **Track record.** We publish every grade's outcome at D+14 and D+30. A paid product needs a hit rate, not adjectives.
4. **Fit to you** (v4). Filter and re-rank by the buyer's skills, budget, language and market.

> [!IMPORTANT]
> **Design rule for v3:** build everything a paid v4 needs (stable IDs, structured JSON, gated-ready content, track record, email list), but ship v3 free. The paid wall in v4 should be a configuration change, not a rewrite.

---

## 1. Users & Jobs

| Persona | Job to be done | What they open v3 for |
|---|---|---|
| **Indie hacker / solo dev** (primary) | "Find something I can build and sell in weeks" | Today feed, grades, Build Kit |
| **Small app studio (2–10 people)** | "Spot rising niches and copy a working play early" | Mobile + mini-game breakouts, playbooks |
| **Growth / marketing person** | "Learn which channel moves just worked" | Playbooks, "why it grew" sections |
| **Agent users** (Claude Code, Cursor…) | "Let my agent query what's rising and why" | MD twins, JSON, later MCP |

**Non-goals for v3:** enterprise market sizing, investor deal flow, real-time alerts (v4), user accounts (v4).

---

## 2. Data Sources

### 2.1 Source registry

Every source becomes a module with one declared spec: what it captures, its history policy, its evidence label and its rate budget.

| # | Source | Surface | Endpoint | Role | History policy | Label |
|---|---|---|---|---|---|---|
| 1 | **TrustMRR** | Web SaaS | `trustmrr.com/api/ai` (existing) | Measurement: verified revenue, MRR, for-sale | API + our snapshots | verified |
| 2 | **Appark top charts** | iOS + Google Play | `appark.ai/api/charts/top-charts` | Discovery: rank, rank change, newly promoted, days at #1 | **Today only for guests → must snapshot daily** | verified rank |
| 3 | **Google Play detail** | Android | Play store app page | Measurement: exact cumulative installs → installs/day | Our snapshots | verified |
| 4 | **iTunes Lookup** | iOS | `itunes.apple.com/lookup` (existing) | Measurement: `userRatingCount` → new ratings/day | Our snapshots | estimated (proxy) |
| 5 | **Gravity Engine** | WeChat / Douyin mini-games | `rank.gravity-engine.com/rank-data/{wechat,douyin}/{day,week}/` | Discovery + measurement: rank, change, genre rank, publisher | Our snapshots (public = top 20) | verified rank |
| 6 | **Appark drama** | TikTok short drama | `POST /api/advertiser/tiktok-series-list`, `playlet-list` | Discovery: drama chart, ad creatives, impressions | Drama-ad chart has history; series chart today only | verified / estimated |
| 7 | **GitHub Trending** | Open source | `github.com/trending[/lang]?since=daily` (existing, widen) | Discovery: "stars today", language chart position | Our snapshots | verified |
| 8 | **GitHub stars API** | Open source | GraphQL, 100 repos per query | Measurement: daily star count for tracked repos | Our snapshots | verified |
| 9 | **Tranco** | Web | existing | Measurement: traffic rank of every tracked domain | API by date | verified |
| 10 | **Reddit (Arctic Shift)** | Demand | existing | Demand echo: threads asking for this kind of product | API | verified counts |
| 11 | **Xiaohongshu 小工具** | Demand (CN) | existing CSV import + TinyFish | Demand echo + CN tool boards | Our imports | verified / inferred |
| 12 | **Hacker News (Algolia)** + **Product Hunt** | Launch events | `hn.algolia.com/api/v1`, PH GraphQL (token) | Trigger evidence: launches, scores, dates | API | verified |

**Investigation-time lookups, not bulk collection:** Meta / TikTok / Google ad libraries, X posts, TikTok videos, store reviews. These are fetched per candidate by the investigation agent (TinyFish / browser), because none offers a usable bulk API.

### 2.2 Collection budget

Appark at full Stringers scale (115 regions × 46 categories × 5 pages × 2 stores) would be tens of thousands of calls a day. v3 uses tiers:

| Tier | Countries | Categories | Pages | Calls/day (iOS + GP) |
|---|---|---|---|---|
| A | us, gb, ca, au, de, fr, jp, kr, br, in, id, mx, tw, sa, tr (15) | all (36) + 46 genres | 5 (top 200) on "all", 2 (top 80) per genre | about 3,000 |
| B | 30 more growth markets | all (36) only | 5 | about 300 |
| C | the rest | rotate 1/7 per day | 2 | about 150 |

At 1 call/second that is about 1 hour, run as its own CI job. Measurement pulls (GP detail, iTunes Lookup) only cover **apps that appeared in any chart in the last 30 days**, batched 200 ids per Lookup call.

> [!WARNING]
> **Source risk.** Appark and Gravity Engine are undocumented internal APIs. v3 must: send a generic User-Agent, pace and cache, **publish derived metrics and links, never re-host raw chart dumps**, and keep fallbacks (Apple RSS, Play pages). For v4 (paid), get written permission or a data licence for any source whose data appears in paid content.

### 2.3 Storage

Snapshots grow from about 80 KB/day today to several MB/day with Appark. Committing raw snapshots to git stops scaling within months.

| Layer | Where | Kept |
|---|---|---|
| Raw snapshots (`<source>/<day>.jsonl.gz`) | Object storage (Cloudflare R2 / S3) or GitHub Release assets per month | Forever (it's the moat) |
| Working DB (`radar.sqlite` / DuckDB) | CI cache, rebuilt from raw | Rolling |
| Derived daily facts (candidates, investigations, plays) | Git (`data/derived/`) | Forever, small |
| Site | `docs/` (GitHub Pages) → Cloudflare Pages in v4 | Latest |

---

## 3. Data Model

v2 keys everything by `(source, pid)`. v3 adds an **entity layer**: one product seen by many sources.

```text
entity  ─┬─ links:  trustmrr:acme · ios:6505107527 · play:com.acme.app · gh:acme/acme · web:acme.com
         ├─ metrics (time series, per source/metric/day, with label)
         ├─ events  (dated triggers: post, ad, featuring, release, chart entry)
         ├─ candidates (lines crossed per day)
         └─ investigations ─── claims (label + source URL) ─── plays (case | counter-example)
                                     └─ followups (D+7 / D+14 / D+30 outcome)
```

| Table | Key columns | Notes |
|---|---|---|
| `entities` | entity_id, kind (app / saas / repo / minigame / drama / site), name, direction, fit | Stable slug, never reused |
| `entity_links` | source, pid → entity_id, method, confidence | Resolution: Appark `cluster_id` (iOS↔Android), website domain (TrustMRR↔Tranco↔store seller URL), GitHub homepage, name + developer fuzzy match |
| `metrics` | source, pid, metric, day, value, label | Existing table, unchanged |
| `events` | entity_id, day, type, url, title, numbers | Filled by investigation + launch sources |
| `candidates` | day, entity_id, metric, before, after, mult, rule_id, score, status | status: picked / skipped / suppressed |
| `investigations` | id, entity_id, day, status, lang, json, model, tokens, version | status: draft / published / **retracted** |
| `plays` | id, title, mechanism, category, steps json, last_verified | |
| `play_evidence` | play_id, investigation_id, role | role: case / counter |
| `followups` | investigation_id, horizon, metric_value, outcome | outcome: held / faded / grew |

---

## 4. Detection: "The Line It Crossed"

### 4.1 Rules (one config file, `radar/rules.toml`)

Each rule compares an entity with **its own** recent baseline and adds an absolute floor so tiny numbers don't qualify.

| Rule | Metric | Trigger | Floor | Notes |
|---|---|---|---|---|
| `gp_installs` | GP installs/day | ≥ 3× trailing 7-day average | ≥ 300/day | 2-day smoothing (Play refreshes every other day) |
| `ios_ratings` | iOS new ratings/day | ≥ 3× | ≥ 20/day | Proxy; label estimated |
| `chart_jump` | iOS / GP rank | Entered a category top 50 from > 150, or `newly_promoted` | Category top 200 | Per country |
| `revenue` | TrustMRR daily revenue | ≥ 3× | ≥ $50/day | Or MRR × 1.3 in 30 days with ≥ $500 MRR |
| `gh_stars` | Stars/day | ≥ 3× | ≥ 100/day | Suspicion flag: stars/forks ratio, burst shape |
| `minigame_rank` | Mini-game rank | ↑ ≥ 15 into top 30, or new in top 20 | — | Cross-board check |
| `drama` | Drama chart / ad creatives | New in top 20, or creatives ≥ 3× | ≥ 200 creatives | |
| `web_traffic` | Tranco rank | Rank ≥ 2× better in 7 days | Within top 500k | Existing logic |
| `demand_spike` | Reddit threads per direction | ≥ 2× week over week | ≥ 10 threads | Direction-level, not entity |

### 4.2 Picking what to investigate

Thousands cross a line; we investigate a daily budget (v3: 15–20, v4: 40+).

```text
score = log2(mult) × log10(after) × novelty × solo_fit × (1 + demand_echo)
  novelty     = 0 if investigated in last 14 days, 0.5 if in 15–45 days, else 1
  solo_fit    = direction prior (taxonomy.fit), penalty for big-company publishers
  demand_echo = matching Reddit / XHS / Tranco movement for the same direction (0–1)
quota       = max 40% of picks from one source; at least 1 per surface when available
```

Suppress: big brands (publisher on a deny list or > 50 apps), seasonal repeats already explained, suspected star or rank manipulation (still listed, marked).

---

## 5. Investigation: Evidence → Claims → Report

### 5.1 Pipeline per candidate

| Step | Who | Output |
|---|---|---|
| 1. Gather | Code + TinyFish | 14-day metric curve; store page + reviews; founder / company; launch events (HN, PH); search hits for name in the last 14 days on X, TikTok, Reddit, YouTube; ad library check (Meta / TikTok) |
| 2. Align | Code | Events placed on the curve; the "first move day" detected |
| 3. Write | LLM (structured output) | JSON matching `investigation.schema.json` (blocks below), every claim with `label` and `source_url` |
| 4. Verify | Code + second LLM pass | Every *fact* has a URL that resolves and contains the number or name; otherwise downgraded to *inference*; the headline must not rely on an inference alone |
| 5. Decide | Rules | Publish, hold (needs more evidence) or **retract** (trigger contradicts curve, numbers don't reconcile, duplicate) |
| 6. Translate | LLM | ZH ⇄ EN from the same JSON, never re-researched |

### 5.2 Report schema (one JSON → every page, email, MD twin, API)

| Block | Field | Rule |
|---|---|---|
| Headline | `lesson_title` | The transferable play, ≤ 30 characters ZH / 70 EN. Never just the product name |
| Product line | `name, one_liner, platform, launched, age_days, url` | |
| Metric badge | `metric, before, after, mult, window` | From `candidates`, never from the LLM |
| Summary card | `what, why_grew, takeaway, who, model, staying_power` | `staying_power` ∈ pulse / has-legs / unclear |
| Positioning | `for_whom, job, before_it, wedge` | Jobs-to-be-done |
| Differentiators | `[claim, evidence, label]` × 2–4 | |
| Competitors | `[name, how_it_differs]` × 2–4 | |
| Moat | `moat` | One line |
| Timeline | `[date, event, url, label]` | |
| Discount | `discounts[]` | Required: bought reach, base size, chart effects, lagging data |
| **Demand Echo** (ours) | `reddit_threads[], xhs_hits[], traffic_delta` | Code-filled, not LLM |
| Grade | `grade, reasons[]` | Rubric §6.2 |
| How to follow | `follow_play, wedge, avoid` | "Copy the play, not the category" |
| **Build Kit** (ours) | `validate_72h[], mvp_14d[], first_30_users[]` | Only for S/A grades |

> [!TIP]
> **Labels shown to readers:** ↗ fact (linked), *inferred*, *not found*, *estimated*. "Trigger not found" is an allowed and honest answer. The verify step makes it impossible to publish an unlabeled number.

### 5.3 Cost control

- One model call for writing, one cheaper call for verification, one for translation. Gather is mostly code + TinyFish.
- Hard caps per item (input tokens, output tokens, TinyFish calls) and per day, logged in `investigations.tokens`.
- Cache by entity: a second breakout of the same product reuses its dossier and only investigates the new window.
- The existing MiniMax setup (`stage_b.py`) is reused behind one `llm.py` interface so the model can be swapped.

---

## 6. Synthesis: Directions, Grades, Playbooks, Track Record

### 6.1 Directions

- Two levels: about **12 groups × 120 directions** (v2 has 40). Keep v2 slugs; split big ones.
- Assignment: keywords (existing) → LLM classifier for leftovers → human review queue for new-direction proposals.
- Each direction page shows: breakouts by day (`before → today ×N`, "investigated" marker), a **landscape** block (apps / repos / SaaS count, launched in last 12 months, revenue > $10k, growing > 30%), the demand panel (Reddit, XHS), and three one-sentence takeaways.

### 6.2 Grade rubric (S–E = odds for 1–2 people to make money within months)

| Factor | Evidence used | Weight |
|---|---|---|
| Money is real | TrustMRR revenue, grossing rank, IAP price, ad spend seen | 25% |
| Demand is real | Demand Echo, reviews asking for features, search interest | 20% |
| Replicable by 1–2 people | Build complexity, data / licence needs, capital | 20% |
| Room left | Number of competitors, how few people know (visibility), crowding of the direction | 15% |
| Window | Event-driven deadline, platform shift, seasonality | 10% |
| Durability | Moat, pulse vs legs, retention signals | 10% |

Score ≥ 80 S · 65 A · 50 B · 35 C · 20 D · else E. The LLM proposes factor scores with reasons; code computes the grade, so grades are reproducible and auditable.

### 6.3 Playbooks

- Every investigation tags its growth mechanism (e.g. *founder lifestyle post*, *comparison video*, *new-hardware day-one*, *localized store page in a small market*).
- Weekly job clusters mechanisms → proposes a play when ≥ 3 investigations share it → a human approves the title and steps.
- Each play shows: recipe, *why it works*, steps, cases, **counter-examples** (same play, didn't move), "N products verified", "last verified".

### 6.4 Follow-up audit (the trust engine)

- At D+7, D+14 and D+30, re-read the metric for every published item → held / faded / grew.
- Publish on the Method page, per grade and per source, a line such as "S-grade items still above 2× baseline at D+30: N%" (illustrative format, not a target).
- Feed outcomes back into the rubric weights each month.

---

## 7. Presentation

### 7.1 Site map

| Page | Path | Content |
|---|---|---|
| **Today** | `/` | One-line headline, lines-crossed counters, investigated feed (tabs: All / Apps / SaaS / Open source / Mini-games / Drama / Watched directions) |
| **Item** | `/i/<entity>/<date>` | The full investigation (schema §5.2) |
| **Directions** | `/d/` and `/d/<slug>` | Index by group; landscape + breakouts + demand |
| **Playbooks** | `/plays/` and `/plays/<id>` | Cards with verified count and recency |
| **Charts today** | `/charts/` | Top movers per surface (derived, linked to source) |
| **Track record** | `/record/` | Hit rates by grade and source |
| **Method & data** | `/method/` | Each source: range, caveats, labels, refresh time |
| **Archive** | `/day/<date>` | Every past day |
| Machine | `*.md`, `/llms.txt`, `/api/*.json`, `/feed.xml` | Same content for agents |

### 7.2 Today page layout

```text
┌──────────────────────────────────────────────────────────────┐
│ Nov 18 · "Three budgeting apps grew from one TikTok format."  │  ← one-line daily judgment
│ Lines crossed: Apps 214 · SaaS 9 · Repos 37 · Games 6 · Drama 4│
│ [All] [Apps] [SaaS] [Open source] [Mini-games] [Drama] [★ Mine]│
├──────────────────────────────────────────────────────────────┤
│ A  One new-phone lifestyle post sold the subscriptions       │  ← lesson headline + grade
│    Monveo · voice + receipt budgeting · iOS · 91 days old    │
│    Daily revenue ×7  $19 → $131                ✓ verified    │  ← metric badge
│    Why: founder's Threads post 7,220 likes + App Store feature│
│    Take: put the product inside a lifestyle post, link below │
│    Demand echo ●●○  r/personalfinance +4 threads this week   │  ← ours
├──────────────────────────────────────────────────────────────┤
│ …                                                            │
└──────────────────────────────────────────────────────────────┘
```

### 7.3 Item page layout

```text
Lesson headline                                        [Grade A]
Name: one-liner · platform · launched (age) · source ↗
[ metric ×N  before → after ]   [ 14-day chart ]
┌ What it is │ Why it grew │ What to take │ Who · Model · Legs ┐
Positioning (for whom / job / before it / wedge)
How it differs (claim + evidence)        Competitors table
Timeline (dated, ↗)                      Discount the numbers
Demand Echo (Reddit · XHS · traffic)     Grade reasons
How to follow  →  Build Kit (72h validate · 14-day MVP · first 30 users)
Labels legend · data dates · "report an error"
```

### 7.4 Writing style rules (from Stringers, enforced in the prompt and the verify step)

- Lesson before product. Absolute numbers next to every multiplier.
- Conditional verdicts: "You can, but…" + who it suits + a deadline.
- Every guess says it's a guess. "Not found" is fine.
- Advice is a wedge (market, audience, channel left open), never "build a clone".
- No adjectives without a number. No charts stretched or padded.

### 7.5 Daily email

Subject = today's one-line judgment. Body = top 5 items (headline, badge, why, take), one play of the day, one demand spike. Sent via a provider with a free tier (Buttondown / Resend). The subscriber list is the main v4 asset.

---

## 8. System Architecture

### 8.1 Code layout

```text
radar/
  sources/          one module per source, each exports SPEC + collect(con, day)
    trustmrr.py appark.py gplay.py itunes.py gravity.py drama.py
    github.py ghstars.py tranco.py reddit.py xhs.py launches.py
  entities.py       resolution + links
  detect.py         rules.toml → candidates
  investigate/
    gather.py  align.py  write.py  verify.py  translate.py
    schema/investigation.schema.json
  synthesize/
    directions.py  grade.py  plays.py  followup.py
  publish/
    site.py  email.py  feeds.py  md.py  llms.py  api.py
  llm.py            one interface (MiniMax today, swappable)
  store.py net.py taxonomy.py rules.toml
```

### 8.2 Daily schedule (GitHub Actions; move to a small VPS if runtime > 2 h)

| Time (UTC) | Job | Duration | Secrets |
|---|---|---|---|
| 00:30 | `collect-charts` (Appark tiers, Gravity, drama) | about 60 min | none |
| 01:40 | `collect-measure` (GP detail, iTunes Lookup, GitHub stars, Tranco, TrustMRR) | about 30 min | GITHUB_TOKEN |
| 02:20 | `collect-demand` (Reddit, XHS, HN, PH) | about 20 min | PH token |
| 02:45 | `detect` → candidates + picks | 2 min | none |
| 02:50 | `investigate` (15–20 items, parallel 4) | about 40 min | LLM, TinyFish |
| 03:40 | `synthesize` + `publish` (site, email, feeds) | 5 min | email provider |
| Weekly | `plays` clustering, rubric review | — | LLM |

Each job writes a `source_runs` health row. The Method page shows source health. A failed source never blocks the build; it marks its panels "not refreshed today".

---

## 9. Roadmap to v3

| Milestone | Scope | Exit check |
|---|---|---|
| **M1 · Data foundation** (wk 1–2) | Source registry; Appark (tier A) + GP detail + iTunes counts + Gravity + GitHub widen + stars API; raw snapshots to object storage | 7 consecutive days collected, health page green |
| **M2 · Entities + detection** (wk 3) | Entity resolution; `rules.toml`; candidates + picking; "Lines crossed" page | Manual review: ≥ 70% of top-20 picks look like real breakouts |
| **M3 · Investigation** (wk 4–5) | Gather / align / write / verify / translate; item page; retraction | 30 published items, 0 unlabeled numbers, retraction works |
| **M4 · Synthesis** (wk 6) | Directions v3, grade rubric, Build Kit, first playbooks, follow-up job | 10 plays, D+14 audit running |
| **M5 · Distribution** (wk 7) | New Today page, email, MD twins, `llms.txt`, JSON, Track record page | 14 days of daily emails sent |

**Retire:** the Mon/Thu Stage A/B PRD loop as a schedule. Its templates become the Build Kit generator, called only for S/A items.

---

## 10. Designed-In for v4 (Paid)

| v4 feature | What v3 must already have |
|---|---|
| Free vs paid content | Every item is one JSON; the site can render "summary" or "full" from the same file |
| Watchlists + alerts (direction, competitor, keyword) | Stable entity and direction IDs; candidates table queryable by direction |
| Personal fit ranking | `solo_fit` factors stored per item (skills, capital, language, market) |
| Agent access (MCP, API keys) | MD twins, JSON API, `llms.txt`; read-only query layer over derived tables |
| Proof of value | Track record page with D+30 hit rates |
| Audience | Email list growing from day one of v3 |
| Data rights | Licence or permission for every source shown in paid content; raw dumps never sold |

**Suggested v4 packaging (to validate during v3):**

| Plan | For | Includes |
|---|---|---|
| Free | Everyone | Today feed with 3 full investigations a day, summaries for the rest, weekly email |
| Pro | Solo builders | All investigations, Build Kits, playbooks with counter-examples, watchlists, daily email, archive |
| Agent | Builders who use AI agents | Pro + MCP / API quota over investigations and derived metrics |

---

## 11. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Undocumented APIs change or block | Lose a surface | Fallbacks per source; health page; never depend on one source for a surface |
| Data licensing in a paid product | Legal | Derived metrics + links only; seek permission before v4 |
| LLM hallucinated evidence | Trust | Verify step; facts need resolving URLs; retraction; track record |
| Cost creep (LLM, TinyFish) | Margin | Daily budget caps; entity cache; cheaper model for verify / translate |
| Short history at launch | Weak trends | Start M1 collection immediately, even before the rest is built: every day not collected is gone |
| Copying Stringers too closely | Weak position | Lead with Demand Echo, Build Kit, track record, fit-to-you |

> [!IMPORTANT]
> **First action:** ship the M1 collectors this week. Appark only gives guests today's charts, so every day v3 waits is history we can never get back.
