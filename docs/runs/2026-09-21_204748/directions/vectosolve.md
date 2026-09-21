# Direction: vectosolve

## Why this direction

**TrustMRR evidence**
- $17 MRR / $33 last30 / 241 subscribers — small but growing 2x in subscriber count
- Stage A coarse score: demand=4, competition=2 (passes dual gate as pure GO)
- Founder @go_to_rob — public builder

**X / web evidence (Stage A heuristic)**
- "vector graphics from sketch", "AI icon generator", "SVG from image" all trending indie-tool searches
- Indie designers / Notion-template creators / slide-deck makers constantly tweet: "I need X icons and I can't afford to draw them"
- Existing tools (Recraft, Ideogram, Magnific) output raster or AI-styled vectors — none focused on clean, designer-grade vectors

**Why now**
- Figma's AI tools are still beta and tied to Figma
- Adobe Illustrator is overkill and expensive for indie creators
- Vector databases are exploding (RAG, embeddings) — making "vector tool" double-meaning a marketing win

## Competitor table

| Tier | Competitor | Price | Weakness |
|---|---|---|---|
| L1 direct | Recraft.ai | $0-12/mo | Free tier weak, style-control limited |
| L1 direct | Ideogram | $0-16/mo | Raster-focused (images, not vectors) |
| L1 direct | Vectorizer.ai | $10/mo | One-shot conversion only, no generation |
| L2 adjacent | Adobe Illustrator + Firefly | $23-60/mo | Pro-priced, complex UI |
| L2 adjacent | Figma AI | bundled | Figma-locked, beta |
| L3 substitute | Hiring an illustrator | $50-500/icon | Too slow, expensive |
| L3 substitute | Iconify / free icon sets | $0 | Generic, not custom |

**Competition score: 2** — niche is wide open. "Generate custom, editable vector icons from a sketch or text prompt" with style consistency is empty space.

## PRD MVP

**User story (P0)**
> As an indie designer / Notion creator / slide-deck maker, I describe an icon (or sketch it) and get a clean, editable SVG I can drop into Figma, with consistent style across a set.

**Epic 1 — Text/icon generation (P0)**
- Text prompt → 4 SVG variants → user picks 1 → download
- Style picker: line / filled / duotone / glass
- All output is editable SVG (not raster)

**Epic 2 — Sketch-to-vector (P0)**
- Upload hand-drawn PNG/SVG
- Backend: vectorize + clean + output editable SVG

**Epic 3 — Style-consistent sets (P1)**
- "Generate 10 icons in the same style" — important for indie designers selling template packs
- Shared style anchor across batch

**Epic 4 — Export & integrate (P0)**
- Direct SVG download
- Direct Figma import (paste-to-Figma)
- (P1) Figma plugin

**Non-goals (MVP)**
- ❌ Raster output (vectors only)
- ❌ Complex illustrations / scenes
- ❌ Photo editing
- ❌ Brand-asset management (keep it icon-focused)

**Tech stack (solo, 14 days)**
- Frontend: Next.js + Tailwind
- Backend: Next.js API + GPT-4o for SVG generation + Potrace / Vectorizer.ai API for sketch
- DB: Supabase
- Payments: Stripe
- Hosting: Vercel

## 14-day build plan

| Day | Task |
|---|---|
| 1 | Landing page + waitlist + demo (3 example icons) |
| 2 | Auth + Stripe test |
| 3 | Text-to-SVG pipeline (GPT-4o with structured SVG output) |
| 4 | 4-style picker UI |
| 5 | Sketch-to-vector pipeline (vectorizer.ai + cleanup) |
| 6 | Style-consistent batch (P1) — single prompt, 5-10 icons |
| 7 | **Soft launch** — X thread "I built a custom icon maker", IH post |
| 8 | Figma paste-export + free SVG preview |
| 9 | Polish UX, bug fixes from feedback |
| 10 | Add "icon pack" export (zip of 10-50 icons in shared style) |
| 11 | SEO blog: "How to make custom icons for Notion templates", "AI SVG generator" |
| 12 | Affiliate program for template creators (30% rev share) |
| 13 | ProductHunt assets + maker comment draft |
| 14 | **Public launch** — PH + X + IH |

## 30-day marketing calendar (budget ≤ $300)

| Week | Activity | Cost |
|---|---|---|
| 1 | X thread: "I built a custom vector icon maker" + free-tier demo | $0 |
| 1 | IndieHackers post (template-creator audience) | $0 |
| 1 | DM 30 Notion / Figma template creators with free codes | $0 |
| 2 | 5 SEO posts: "AI icon generator", "vector from sketch", etc. | $0 |
| 2 | Sponsor 1 design Twitter account (5K-15K) — $60 | $60 |
| 2 | Guest post on 1 design newsletter (free) | $0 |
| 3 | ProductHunt launch — $100 featured | $100 |
| 3 | 2 micro-influencers in design niche ($50 each) | $100 |
| 4 | "Free icon pack" lead magnet (5 icons in exchange for email) | $0 |
| 4 | User showcase: retweet best vectors made with tool | $0 |
| 4 | Email nurture → paid plans | $0 |

**Total: $260**

**KPI targets**
- Day 7: 100 signups, 15 paid
- Day 14: 400 signups, 60 paid
- Day 30: 1,000 signups, 200 paid @ $19/mo = $3,800 MRR
- Path to $10K: 525 users @ $19 OR 345 @ $29

## Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Price | $19/mo (Creator, 100 icons) or $29/mo (Pro, 500 icons) |
| Free tier | 10 icons/mo, no card |
| Conversion | 12% (free → paid) |
| LTV (10 mo avg retention) | ~$190-$290 |
| Gross margin | ~85% (GPT-4o SVG gen ~$0.02/icon) |
| CAC | ~$12 (organic-heavy) |
| LTV/CAC | ~15:1 |

**Path to $10K MRR**
- 525 @ $19 OR 345 @ $29
- Indie-creator word-of-mouth is strong in design niche → realistic

## Kill criteria
- Day 14: <10 paid users → niche or pricing pivot
- Day 30: <60 paid → kill
- SVG output quality <70% "I'd use this" → prompt rebuild
- LTV/CAC < 3 by day 60 → stop paid

## Wedge
n/a (pure GO)
