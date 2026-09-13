---
layout: post
title: "Direction: PlotHaus — AI pen-plotter art + sticker pipeline for hobbyists & small shops (GO)"
date: 2026-09-13T03:51:34+00:00
week: "2026-09-13_035134"
week_date: "2026-09-13T03:51:34+00:00"
slug: "plothaus-3d-pen-plot"
permalink: /directions/plothaus-3d-pen-plot.html
tags:
  - "AI"
  - "SaaS"
  - "mobile"
  - "vertical"
---

> Tagline: *Turn "make me a plot" into a one-click subscription.*

---

## 1. Why this direction

### TrustMRRR evidence
- **3dplotter** (per seed report) — MRR ~$1.9K. The only real entrant in the pen-plotter niche. Near-zero direct competitors.

### Why this works
1. **The hobbyist community is large and offline-meeting.** r/BambuLab, r/3Dprinting, r/plotterart — all active, all organic-friendly.
2. **Pen plotters are bought once, then they need consumables.** Ink, paper, sticker vinyl, and *content*. We're the content engine.
3. **AI-generated plotter art is the wedge.** Today hobbyists hand-design in Inkscape or pay $30 on Etsy. We sell a subscription that generates and ships files instantly.
4. **Sticker/print-on-demand integration** (Printify/Printful) creates a margin layer above the subscription.

### What we ship
A web app where the user:
- Types "a fractal of a fox in a geometric style" or uploads a sketch.
- Picks plotter preset (AxiDraw, Bambu, Silhouette, Cricut).
- Downloads SVG + G-code + PNG.
- Optionally orders a sticker (Printify) or 5×7 print (Printful).
- Saves to a personal gallery.

---

## 2. Competitor table

| Tier | Competitor | What they do | Price | Threat |
|---|---|---|---|---|
| L1 | 3dplotter (TrustMRR) | Pen-plotter content marketplace | $5–$15/mo | Direct. We compete on AI generation speed and sticker pipeline. |
| L2 | Etsy shops, Creative Market | Hand-designed plotter files | $3–$20 per file | Real but one-off, no subscription. |
| L2 | Inkscape + manual workflows | Free | $0 | Yes, the DIY path. We win on speed and idea-to-plot in 30 seconds. |
| L2 | Midjourney / DALL-E + manual vectorization | $10–$60/mo + effort | $10–$60 | Real. We win on plotter-specific presets (G-code generation). |
| L3 | Printify, Printful (POD partners) | Fulfillment | Cost+ | Suppliers, not competitors. |
| L3 | AxiDraw community, Evil Mad Scientist | Free resources | $0 | We market there. |

**Competition score: 2.** 3dplotter is the only direct competitor. Etsy is fragmented. The AI-generation layer is genuinely new.

---

## 3. PRD MVP

### User story
> *I bought an AxiDraw for my home office. I want to plotter-print a fresh design every weekend without spending 3 hours in Inkscape. I want a website where I type "minimalist line-art of a mountain range" and download a ready-to-plot SVG in 20 seconds.*

### Epics
- **E1 — Generation.** Text → SVG via a model pipeline (OpenAI image → vectorization via `vtracer` or similar).
- **E2 — Plotter presets.** G-code export for AxiDraw, Bambu, Silhouette, Cricut.
- **E3 — Gallery.** Per-user saved designs, tags.
- **E4 — POD integration.** Printify sticker order, Printful art print order.
- **E5 — Billing.** Stripe Checkout, $9/mo Hobby, $19/mo Pro (more generations + commercial license).
- **E6 — Community.** Optional: weekly design challenge.

### P0 (days 1–10)
- Web app (Next.js).
- Text → SVG pipeline using OpenAI + `vtracer` + hand-tuned prompt library.
- AxiDraw G-code export (use the open-source `axidraw` Python library via serverless).
- Stripe Checkout.
- Single landing page with 20 demo plots.

### P1 (days 11–14)
- Add Silhouette + Cricut presets.
- Save to gallery.
- Email drip (Resend) for new users.

### P2 (post-MVP, days 15–30)
- Printify sticker integration (1 SKU: 4×4 vinyl sticker).
- Printful art print integration.
- Public gallery (opt-in).
- Weekly design challenge.

### Non-goals
- Selling plotter hardware. (We don't touch margins on $500 plotters.)
- Vector-editing UX. (We generate; the user doesn't edit. Yet.)
- Mobile app. (Web only at MVP.)
- Community forums. (Reddit exists.)

### Pricing
- **Hobby ($9/mo):** 30 generations/mo, personal use license.
- **Pro ($19/mo):** 200 generations/mo, commercial license, sticker/print fulfillment.
- **Pay-as-you-go (no sub):** $1 per generation.

---

## 4. 14-day day-by-day build plan

| Day | Output |
|---|---|
| 1 | Lock stack. Buy domain. Landing page with 10 demo plots (hand-make them in Inkscape to seed). |
| 2 | Auth (Clerk) + Stripe Checkout. |
| 3 | Text → image (OpenAI gpt-image-1 or DALL-E). |
| 4 | Image → SVG via `vtracer` (Rust, runs serverless). |
| 5 | SVG cleanup (remove duplicate paths, snap to grid). |
| 6 | G-code export for AxiDraw (use axidraw Python lib in a Lambda). |
| 7 | Save-to-gallery (S3 + Postgres). |
| 8 | Email drip (Resend) for first-run users. |
| 9 | Add Silhouette + Cricut presets. |
| 10 | Generation metering (per plan). |
| 11 | Seed 50 hand-curated demo plots for SEO. |
| 12 | Public gallery opt-in. |
| 13 | Bug bash + Plausible + Sentry. |
| 14 | Public launch in r/BambuLab, r/plotter, r/3Dprinting. |

**Stack:** Next.js + Postgres (Supabase) + Stripe + OpenAI + `vtracer` (serverless Rust) + S3 + Resend.

**Infra cost at MVP:** ~$60/mo.

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget allocation**
- $120 — Reddit ads in r/3Dprinting, r/BambuLab (small CPC, $4/day)
- $80 — Sponsorship of 2 plotter YouTubers (one $50, one $30)
- $50 — Etsy ads retargeting (people searching "plotter SVG")
- $30 — Canva Pro for plot showcase graphics
- $20 — Sample-sticker mailers to 10 hobbyist influencers

**Daily calendar (organic + community-led)**

| Wk | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| 1 | Reddit post in r/3Dprinting: "I built an AI plotter art generator — free for first 50 users" | X thread: "From text to plot in 30 seconds" | TikTok: timelapse of an AI plot | Reddit: r/BambuLab, r/plotter | YouTube Short demo | Reddit ads on ($4/day) | Rest |
| 2 | Plotter YouTuber outreach (cold email) | First YouTuber sponsorship live ($50) | X thread: 7 prompt ideas | Reddit: r/cricut, r/silhouette | TikTok: "Plotter art under $1" | Etsy ads live ($50) | Press release to 3 plotter blogs |
| 3 | Add Silhouette + Cricut presets | Second YouTuber live ($30) | Reddit: r/printmaking | X thread: customer plot reveals | TikTok: behind-the-scenes | Sample-sticker mailers out | Reddit ad optimization |
| 4 | Email blast to 500-person list from Etsy | TikTok: "10 prompt ideas for your AxiDraw" | Reddit: r/Maker, r/DIY | X thread: gallery favorites | Etsy ad optimization | Wrap-up retrospective | Final X thread: 30-day stats |

**Targets (week 4):**
- 5,000 unique visitors
- 200 email signups
- 12% → paid = 24 paid
- 24 × $9 = **~$216 MRR by day 30**
- Realistic month-1 MRR: $150–$250.

---

## 6. Unit economics to $10K MRR

| Metric | Value | Source |
|---|---|---|
| ARPU (Hobby vs Pro) | $13/mo | 65% Hobby ($9), 35% Pro ($19) |
| Gross margin | 75% | OpenAI + infra + Printify/Printful COGS on sticker margins |
| Monthly churn | 6% | Hobbyist churn is moderate; people take breaks |
| Net new paid subs/mo (steady state) | 130 | Slow but steady; viral through plot community |
| Months to $10K MRR | ~9 | (10,000 / 13) / (130 × 0.94) ≈ 9 months |

**Sensitivity:**
- If churn is 10% → ~14 months (outside window).
- If Pro mix rises to 50% → ARPU $14, time to $10K ~8 months.
- If a YouTuber with 500K subs organically features us → +1,000 subs/month, time compresses to ~5 months.

**Worst case (churn 10%, ARPU $11):** ~16 months. Outside window. Plan B: exit at $3–5K MRR or pivot into POD-focused brand.

---

## 7. Kill criteria

- **Day 14:** If landing conversion (visitor → email signup) <3%, kill. The audience isn't interested.
- **Day 30:** If free → paid conversion <8%, kill. The product doesn't earn its keep at hobbyist price.
- **Day 60:** If MRR < $400, kill. The community engine isn't producing.
- **Day 90:** If churn >12%, kill. Hobbyists churn out too fast for the price.
- **Hard kill:** 3dplotter ships a comparable AI generation feature and our organic growth flatlines for 14 days.

---

## 8. Founder fit notes

- **Best for:** founder who is themselves a plotter hobbyist or has access to one (a friend with an AxiDraw is enough). Bonus: design eye.
- **Bad fit if:** you have no interest in plotter art and can't recruit a hobbyist advisor. The product is niche; you have to live it.
- **Extension path after $10K MRR:** add POD to be the consumer-facing brand (Etsy store on autopilot), sell commercial-license packs to small design studios, exit to a print-on-demand roll-up.
