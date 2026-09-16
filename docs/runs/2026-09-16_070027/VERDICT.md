# Verdict — 2026-09-16_070027

## ⚠️ Infrastructure failure notice

Stage B X/web verification (TinyFish queries) returned no results for any candidate — every query produced only the TinyFish CLI help text. The demand/competition scores below are the **heuristic scores from Stage A** (`demand_h` / `comp_h` columns in `candidates.csv`), not re-verified scores. Treat all verdicts as **provisional GO_CANDIDATE**, not confirmed GO. Re-run search before committing build resources.

## Selectable directions (3) — pick one

| # | slug | tier | demand | competition | one-liner | why selectable |
|---|---|---|:-:|:-:|---|---|
| 1 | quran-unlock | GO_NARROW | 4 | 2 | Heritage-language scripture companion: tiny AI app for non-Arabic Muslims learning Quran recitation + meaning, ships on iOS in 14 days | High demand (275 subs on $7 MRR), low comp, clear vertical wedge, validated niche (matches prior "Lingua / heritage language" direction) |
| 2 | publbee | GO | 4 | 2 | "Buffer-for-newsletter-publishers" — turn 1 blog post into LinkedIn/Threads/Mastodon/Bluesky drafts in 30s, with UTM-tagged canonical URL | Real MRR $35 + last30 $32, founder actively shipping (@nezirbasar1), clear anti-Buffer wedge |
| 3 | magicslides-app | GO_NARROW | 4 | 2 | "Gamma-but-for-deck-only" — one-input → 10-slide deck with citations, locked to a single ICP: indie consultants doing client deliverables | Real MRR $114, 827 subs, strong demand, but full slide-deck space is crowded — wedge is "consultant-grade deck, not pitch deck" |

3 directions produced (minimum). 2 more could be packaged from `appalchemy` or `zerano-club` if budget allows another round.

## Ranked recommendation (still give choice)

1. **quran-unlock** — tightest wedge, smallest MVP, strongest fit for solo-14d constraint, leverages prior "heritage language" research. **Best fit for $300 marketing.**
2. **publbee** — clearest product (repurpose blog → social), most generic (= biggest TAM but also most copycats long-term). Best if you want to build distribution muscle.
3. **magicslides-app** — biggest near-term MRR evidence ($114) but also highest build cost for "consultant-grade" bar. Only pick this if you have slides/design taste.

## WATCH
- `appalchemy` (3/2) — mobile utility, demand signal OK but "convert website to app" is increasingly commodity
- `zerano-club` (3/2) — trading signal club, $42 MRR, but trading-content ethics/tos risk
- `helix` (4/2) — churn/payment, anonymous startup, hard to verify what they actually sell
- `vectosolve` (4/2) — AI photo, could be unbundled for vector-specific workflow

## KILL
- `vidai-llc` — $638 MRR but KILL_OR_UNBUNDLE; full video-gen market is funded and saturated
- `fiveml-ltd` — LinkedIn automation, ToS-bordered
- `uplinked-b-v` — same as above
- `orion-ai-solutions-inc` — $579 MRR but anonymous product, can't verify

## Handles (10+ from this run)
See `handles.csv` — appended rows include: @indianappguy (magicslides), @nezirbasar1 (publbee), @diegoroshardt (appalchemy), @thezaxteray (zerano), @abh1nash (neume), @go_to_rob (vectosolve), @iamyacine (quran-unlock), @jonaheapen (helix), @priymrj (vidai — kill ref), @httpsxcoma (autoreels — watch ref). Total: 10 handles, meets ≥10 requirement.

## Evidence quality disclosure
- Demand scores: **Stage A heuristic only, not X-verified** (search returned no data)
- Competition scores: **Stage A heuristic only, not Google-verified**
- All "GO" labels here are provisional pending real search
- If you re-run with working TinyFish/web search, expect at least 1 of these 3 to flip tier