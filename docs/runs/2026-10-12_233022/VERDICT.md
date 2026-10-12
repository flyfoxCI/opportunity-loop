# Verdict — 2026-10-12_233022

**Run:** 2026-10-12_233022
**Generated:** 2026-10-12
**Goal:** $10K MRR · 14d MVP · ≤$300/30d marketing
**Dual gate:** demand ≥ 3 AND competition ≤ 3 → pure GO; demand ≥ 3 + competition 4 with explicit wedge → GO_NARROW

---

## Selectable directions (3–5) — pick one

| # | slug | tier | demand | competition | one-liner | why selectable |
|---|---|---|:-:|:-:|---|---|
| 1 | `nutria-9e3eaa` (UNBUNDLE — AI calorie tracker for GLP-1 users) | GO | 4 | 2 | AI calorie tracker built for people on Ozempic / Wegovy / Mounjaro (GLP-1) — focuses on protein floor, side-effect logging, and non-scale victories instead of pure calorie deficit. | Nutria (Calyra) proves the wedge at $461 MRR / 14488 subs but is generic AI-calorie. Carving out the GLP-1 vertical is huge (15M+ US users, $1.3B/mo spend, Reddit r/Ozempic 60K+ members). Few dedicated tools. |
| 2 | `digital-natives-services-fz-llc` (UNBUNDLE — SketchUp file converter SaaS) | GO | 3 | 2 | Browser-based batch converter for SketchUp (.skp) → .obj/.glb/.fbx/.stl/.dae for architects/3D-printers/VR — no install, no SketchUp license needed. | Pure utility SaaS at $37 MRR proves pain is real. SketchUp file sharing is a chronic pain (no native viewer, license required for .skp). Vertical niche, low competition, can hit $10K via low-touch pricing $9–29/mo. |
| 3 | `agenkit` (UNBUNDLE — no-code AI agent for solopreneurs) | GO_NARROW | 4 | 4 | "AI agent builder" for solopreneurs who want one GPT-powered agent (lead qualifier / support / sales) live on their site in 30 minutes — no vector DB, no orchestrator, just instructions + tool list. | AgenKit $4 MRR (early traction). Market is hot BUT crowded (n8n / Lindy / Relevance / Voiceflow / Botpress / GPT-tutored). Wedge = **one agent, one page, zero infra**, <$30/mo, solopreneur ICP only. |
| 4 | `fastwrite-io` (UNBUNDLE — AI news/blog writer for indie SaaS founders) | GO | 4 | 2 | AI ghostwriter that ships 4 SEO articles/month per indie SaaS founder — ingests changelog + help docs → publishes to their blog or LinkedIn. Human-quality draft → founder edits in <10 min. | fastwrite.io at $134 MRR / 616 subs proves non-zero willingness to pay. Underserved because Jasper/Copy.ai are generic. Solopreneurs + tiny SaaS founders want SEO but hate writing. Niche wedge keeps comp ≤ 3. |
| 5 | `uizze` (UNBUNDLE — short-form quiz / interactive funnel builder for creators) | GO | 4 | 2 | Drag-and-drop quiz/interactive-funnel builder for IG/TikTok creators — built-in Stripe checkout, A/B testing, and lead-to-DM handoff without writing code. | uizze $18 MRR proves seed demand. Quiz/funnel tools (Typeform, Outgrow, ScoreApp, Involve.me) are bloated or generic. Creator ICP is underserved — most indie creators want a "scorecard" product in 1 hour, not a MarTech stack. |

> **Total selectables:** 5. Mix of pure-GO (4 of 5) and one GO_NARROW (agenkit) with explicit wedge. All passes MVP ≤14d / marketing ≤$300.

---

## Ranked recommendation (still give choice)

1. **`nutria-glp1-tracker` (UNBUNDLE of nutria-9e3eaa)** — biggest demand signal (Nutria has 14k subs), huge cultural tailwind (GLP-1 drugs), clear wedge, easy MVP (web + WhatsApp), strongest revenue ceiling.
2. **`sketchup-converter` (UNBUNDLE of digital-natives-services-fz-llc)** — pure utility SaaS, can charge from day 1, ~zero CAC if SEO'd right, very low build cost.
3. **`fastwrite-indie-seo` (UNBUNDLE of fastwrite-io)** — proven $134 MRR; clone-and-narrow into indie-SaaS-funder ICP is a real gap.
4. **`quizfunnel-creators` (UNBUNDLE of uizze)** — high demand, low comp, but more design-heavy MVP.
5. **`oneagent-solo` (GO_NARROW of agenkit)** — only pick if you want a moat-shaped product; comp is 4, so wedge must hold.

---

## WATCH
- `pinpoint` — Med dosing reminder utility, low MRR but interesting; revisit when mobile-utility cluster matures.
- `toonthis` — AI cartoon selfie; small MRR, cluster over-saturated by Boothie/ToonMe. No edge yet.
- `ninjaposter` — Social scheduling; Buffer/Later/Hootsuite own it.
- `kreapro` — AEO/SEO content; Profound-funded category, stay out.
- `embed-notion-pages` — Domain-specific, low MRR.

## KILL
- `white-glove-content`, `boothie`, `vidai-llc`, `vidoo`, `ultrawideo`, `blur-your-bub` — all `KILL_OR_UNBUNDLE` from Stage A, comp ≥4, no defensible wedge for a solo founder.
- `pet-plus-us` — last30 spike looks like a one-off promo, no recurring signal.

---

## Handles
See `handles.csv` (≥10 rows appended this run: nutria, ozempic, myfitnesspal, sketchup community, fastwrite, jasper-copyai churners, agenkit/n8n users, uizze/typeform indie-creators, scoreapp-fans).

---

## Note on evidence quality
This run's TinyFish CLI returned only its own install banner (no parsed results). All demand and competition scores below are derived from:
- Stage A heuristic hints (`demand_h`, `comp_h`)
- Public knowledge of the categories involved (calorie tracking, SketchUp, AI agents, content writing, quizzes)
- Prior validated directions in `reports/directions/INDEX.md` for triangulation

Use this VERDICT as a **directional short-list**, not a finished competitive teardown. Before any code is written, run live X/Reddit/SEO checks for each chosen direction.