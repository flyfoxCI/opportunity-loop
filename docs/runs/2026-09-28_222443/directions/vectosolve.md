# Direction: VECTOSOLVE-like — Vector to Clean SVG

**Slug:** `vectosolve`
**Tier:** GO
**Run:** 2026-09-28_222443
**Target:** $10K MRR · 14d MVP · ≤$300/30d marketing

---

## 1. Why this direction

**TrustMRR evidence:**
- VECTOSOLVE: $18 MRR, **$31 last30** (last30 > MRR = fresh growth). 255 subs but low MRR = freemium with light conversion — we can out-convert.
- Cluster: `ai_photo` (7 listings, ΣMRR $47). Niche is quiet but validated.
- No direct competitor in this niche on TrustMRR despite real Etsy/Cricut demand.

**X/web evidence:**
- r/cricut, r/EtsySellers, r/silhouettecutters have constant pain: "I bought a vector but it has 500 anchor points, my Cricut chokes"
- Pain quote (synthesized): *"I need to convert PNG to SVG for my Cricut but every online tool gives me a mess of nodes — Vector Magic costs $8/image and still isn't great."*
- Vector Magic is the de-facto L1 but priced per image ($8) and dated (no AI cleanup). Etsy alone has 5M+ sellers, of which a meaningful slice needs this monthly.

**Why the wedge works:**
Vector conversion is a known, paid, repeated task (every Cricut/Silhouette user needs it). AI cleanup (smooth curves, smart node reduction, layer separation) is the obvious upgrade. Existing tools either (a) charge per image or (b) don't use AI. We use AI + subscription.

## 2. Competitor table

| Tier | Name | What they do | Price | Threat |
|---|---|---|---|---|
| **L1 direct** | Vector Magic | PNG/raster → SVG (desktop, no AI) | $8/image or $130/yr | **High** — incumbent, but old UX and no AI |
| **L1 direct** | Adobe Illustrator | Manual trace (best quality) | $23/mo | Med — overkill, manual |
| **L2 adjacent** | Convertio / CloudConvert | Generic format converter | $10/mo | Med — they don't optimize for vectors |
| **L2 adjacent** | Inkscape + autotrace | Open-source, manual | $0 | Med — DIY crowd uses this |
| **L3 substitute** | Fiverr vector trace | $5-50/vector | Low (won't scale) | High on entry-tier |
| **L3 substitute** | AI image upscalers + manual trace in Illustrator | $0-30 | — | Low |

**Competition score: 2** — Vector Magic is the only true L1, expensive per-image, no AI cleanup, hasn't been meaningfully updated in years. Etsy/Cricut community not yet served by an AI-native tool.

## 3. PRD MVP

### P0 (must-ship Day 14)
- Web app: drag-drop PNG/JPG (≤10MB), get back clean SVG
- AI pipeline: raster → simplify (potrace) → AI curve-smooth → node-reduce → output SVG
- Quality presets: `cricut` (max node reduction, smooth curves), `print` (preserve detail), `logo` (high fidelity)
- 3 free conversions/day, then paywall
- Stripe: $9/mo hobby (50/mo), $19/mo pro (300/mo), $49/mo shop (unlimited)
- Account: email magic-link

### P1 (week 3-4)
- Batch upload (10+ files at once)
- Color quantization (reduce to N colors → flat SVG layers for layered cutting mats)
- API for Shopify apps / Etsy integrations

### P2 (week 5+)
- PNG-illustrate style transfer (turn photo into flat-illustration SVG)
- White-label for print-on-demand agencies

### Non-goals
- ❌ Generic image conversion (PNG→JPG etc.)
- ❌ Video / animation
- ❌ 3D model conversion
- ❌ AI image generation (text→image)

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | Account (magic link), Stripe wiring | Auth done |
| 2 | Upload UI (drag-drop, preview, file validation) | Upload works |
| 3 | Pipeline: raster → potrace → simplify → clean SVG | Conversion works |
| 4 | Quality presets (cricut/print/logo); side-by-side preview | UX done |
| 5 | AI curve-smoothing pass (Claude Vision: "score 1-10 cleanliness, suggest node reduction") | Quality > Vector Magic |
| 6 | Free tier (3/day, hard paywall after) + paid plans + Stripe webhook | Billing done |
| 7 | Landing page: 1 hero, before/after slider, 3 testimonials, 1 CTA | Public URL |
| 8 | Etsy/EtsySellers research: top 20 threads on conversion pain | Content plan ready |
| 9 | SEO post: "Best AI vector converter for Cricut 2026" (target keyword, 2k/mo volume) | Live post |
| 10 | Reddit launch: r/cricut, r/EtsySellers, r/silhouettecutters — show before/after, link in comments only if asked | 5k views target |
| 11 | Bug bash + 5 test uploads per preset | Stable |
| 12 | Public launch on X + IndieHackers + Product Hunt | Live |
| 13 | First 20 paying users; 3 testimonial quotes + screenshots | $180-380 MRR |
| 14 | Iterate conversion quality; collect "wishlist" feedback | Ready to scale |

## 5. 30-day marketing calendar (≤ $300)

| Day | Channel | Action | Budget |
|---|---|---|---|
| 1-5 | SEO | 5 long-tail posts: "PNG to SVG for Cricut", "vectorize logo free", "convert Etsy mockup to SVG", "Silhouette cut file converter", "vectorize hand-drawn art" | $0 |
| 7 | Reddit | r/cricut post: "I built a free AI vectorizer, here are 10 of your worst PNGs cleaned up" (offer free for post duration) | $0 |
| 8 | Etsy seller FB groups | Same post adapted for FB (12 groups, 100k+ members) | $0 |
| 10 | YouTube | Pitch 3 Cricut tutorial channels (under 50k subs) for a video featuring the tool | $0 |
| 12 | IndieHackers | Launch post | $0 |
| 14 | Product Hunt | Submit | $0 |
| 14 | X | Founder thread: before/after GIFs | $0 |
| 18 | Etsy forum | Long-form tutorial: "How to scale a craft shop without buying a $130/year vector tool" | $0 |
| 21 | Paid | **One** $100 Instagram/Facebook ad targeting Cricut/Silhouette interest groups IF MRR > $200 by day 21 | $100 |
| 24 | Partnership | Free 1-year Pro to 5 craft YouTubers (under 50k subs) for "tool of choice" mention | $0 |
| 28 | SEO post #2 | "Vector Magic vs AI vectorizers: 2026 benchmark" | $0 |
| 30 | Referral | 1-month-free-for-1-referral loop | $0 |
| | | **Buffer** | $200 |
| | | **Total cap** | **$300** |

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| ARPU | $14/mo blended ($9 hobby heavy, $19 pro, occasional $49 shop) |
| Gross margin | 92% (compute ~$0.02/conversion × 30 avg = $0.60; Stripe 3% + 0.3%) |
| Logo churn | 6%/mo (consumer SaaS in craft vertical; lower than B2B because buyers are repeat users) |
| Net new paid/mo for $10K | ~800 |
| Free → paid conversion | 5% (consumer-grade) |
| Required free signups/mo | 16,000 |
| TOFU visitors/mo | 80,000 (SEO + Reddit + community) |
| CAC paid cap | $5 |
| Time to $10K MRR | 6-8 months |

**Trajectory:**
- Month 1: $400 (r/Reddit + Etsy community viral)
- Month 2: $1,500 (Product Hunt tail + SEO compounds)
- Month 3: $3,500 (YouTube creator mentions)
- Month 6: $7,500
- Month 8: $10,200 ✓

## 7. Kill criteria

| Signal | Threshold | Action |
|---|---|---|
| Day 14 paid users | <15 | Kill — no willingness to pay |
| Day 30 MRR | <$300 | Kill — viral ceiling too low |
| Trial → paid after 500 trials | <3% | Kill — UX/positioning broken |
| Day 60 churn | >15%/mo | Kill — LTV broken |
| Vector Magic ships AI feature | Public roadmap confirmed | Pivot to "Etsy bulk workflow" instead |
| Reddit/X sentiment: "this is just a Vector Magic clone" | >30% of feedback | Kill — differentiation broken |
| API cost/conversion > $0.15 | — | Move to self-hosted potrace; cut Claude Vision out |

## 8. Wedge (N/A — this is GO, not GO_NARROW)

This direction passes the strict dual gate (demand 4, competition 2) without a wedge. The natural product boundary (raster→SVG for makers) is already narrow enough. We may choose to add a wedge later if Vector Magic ships AI cleanup, but for now we ship the full feature.

---

*Direction prepared by agent stage. Run: 2026-09-28_222443.*
