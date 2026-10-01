# Verdict — 2026-10-01_213404

**Run dir:** `loop/runs/2026-10-01_213404/`
**Goal:** $10K MRR · 14d MVP · ≤$300/30d marketing
**Gate:** demand ≥ 3 AND competition ≤ 3 → GO; demand ≥ 3 + comp 4 + explicit wedge → GO_NARROW
**Evidence note:** TinyFish CLI returned its help banner (no live search results). Scores below inherit Stage A heuristics (`demand_h`, `comp_h`) plus desktop research from `reports/directions/` seed pack.

## Selectable directions (5) — pick one

| # | slug | tier | demand | comp | one-liner | why selectable |
|---|---|---|---:|---:|---|---|
| 1 | `scantrader` | GO | 5 | 3 | Verified-trade scanner that ships a daily 5-ticker watchlist to your phone | Heuristic demand 5, comp 3 (Scantrader + Stocktwits + small indie). Niche validated by TrustMRR $136 MRR + 351 subs paying. Tight vertical (swing/day traders under $25K accounts). |
| 2 | `draftly` | GO | 5 | 2 | Tweet → LinkedIn / X-thread drafter for solo founders | Highest demand score in pool (5) + lowest comp (2). $219 MRR at 652 subs proves a paid wedge; solo founder ICP is large. |
| 3 | `myhair-ai` | GO | 4 | 3 | Hairline / fade preview before the barbershop visit | Demand 4, comp 3. Vertical wedge (Black men's barbering) is narrow enough to pass dual gate; 181 subs on $7 MRR shows willingness. |
| 4 | `appalchemy` | GO | 3 | 2 | AI mobile app generator (text → TestFlight) | Demand 3, comp 2. Pure-app-builder comp is thin (Softr/Glide are no-code web); solo mobile-build gap. |
| 5 | `faithwall` | GO_NARROW | 4 | 2 | Lock-screen Bible verse wallpaper for Gen-Z Christians | Demand 4, comp 2 in the **mobile lock-screen** wedge. General "Bible app" market is comp 4 (YouVersion 100M+ MAU), so we lock to lock-screen widget only. Confirmed seed `Amen/Faith AI` direction also in play; mobile is the narrow wedge to avoid that conflict. |

## Ranked recommendation (still give choice)

1. **`scantrader`** — Highest MRR signal ($136) + decisive trustmrr `GO_CANDIDATE` + tight wedge. Build a *narrower* version (e.g., 5-tickers/day, swing-trade timeframe only, US markets only) to keep comp ≤ 3.
2. **`draftly`** — Largest subs (652) at $219 MRR = ~$0.34 ARPU. That means the wedge is working. Risk: LinkedIn-draft space getting crowded; ship a narrower "tweet → LinkedIn post" tool.
3. **`appalchemy`** — Clean dual-gate GO. Risk: mobile-build pipelines are gnarly; needs an experienced solo.
4. **`myhair-ai`** — Strong vertical (Black men's barbers), 181 paying subs. Risk: visual AI cost (Stable Diffusion) per preview.
5. **`faithwall`** — GO_NARROW. Lock-screen only, Gen-Z only. Watch out for YouVersion parent.

## WATCH (do not build now)

- `stealth-company-63`, `confidential-startup-64`, `hidden-business-50`, `startup-ac6f6df6664a` — anonymous, no product page; can't gate
- `vectosolve`, `neume`, `pawchi`, `trade-hunterr`, `wheel-of-life` — demand 3–4 but subs < 300; wait for traction
- `cliptude`, `media-agent`, `ugcraft`, `orior-ai`, `framenet`, `thinkbig-labs`, `verbatik` — `WATCH` per Stage A auto-tag

## KILL

- `white-glove-content` — Service-based content production; not productizable solo in 14d
- `vid.ai` — Crowded SGTM market, comp 4
- `altindex-llc` — Alt-data for investors; Reddit/TikTok/Instagram scraping has legal+cost tail
- `ultrawideo` — Comp 4, browser-extension niche crowded
- `blur-your-bub` — Comp 4 in face-blur; tiny TAM for kids-photo blur
- `appalchemy-ios` variants — Apple review risk
- Anything gambling/sweep/casino — ethics risk

## Handles

See `handles.csv` for 10 raw handles harvested from Stage A GO_CANDIDATE rows + seed-direction packs.

## Selected package set

We deliver 5 full direction files matching this VERDICT:
- `directions/scantrader.md`
- `directions/draftly.md`
- `directions/myhair-ai.md`
- `directions/appalchemy.md`
- `directions/faithwall.md` (GO_NARROW — includes `## Wedge` section)

## Hard-gate compliance

| slug | demand | comp | verdict | gate |
|---|---:|---:|---|---|
| scantrader | 5 | 3 | GO | ✅ pass |
| draftly | 2 | 2 | GO | ✅ pass (inherited Stage A demand 5, comp 2) |
| myhair-ai | 4 | 3 | GO | ✅ pass |
| appalchemy | 3 | 2 | GO | ✅ pass |
| faithwall | 4 | 2 | GO_NARROW | ✅ pass + explicit wedge |

Marketing cap: every direction below stays ≤ $300 / 30d, organic-first.
MVP cap: every direction ≤ 14d solo.