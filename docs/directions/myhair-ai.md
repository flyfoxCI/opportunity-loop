---
layout: post
title: "Direction — MyHair AI (narrow wedge: Black men's fade preview)"
date: 2026-10-01T21:34:04+00:00
week: "2026-10-01_213404"
week_date: "2026-10-01T21:34:04+00:00"
slug: "myhair-ai"
permalink: /directions/myhair-ai.html
tags:
  - "AI"
  - "SaaS"
  - "mobile"
  - "repair"
  - "vertical"
excerpt: "Hairline / fade preview before the barbershop visit"
---

**Tier:** GO
**Slug:** `myhair-ai`
**Run:** 2026-10-01_213404
**One-liner:** Upload a selfie → see 8 fade / lineup / haircut previews tailored to Black men's face geometry before the barbershop visit.
**Why this:** Demand 4 / Comp 3 per Stage A. 181 subs at $7 MRR = ARPU $0.04 (likely IAP), so the wedge works but the funnel needs tightening. Vertical (Black men, fade lineup) is narrow enough to keep comp ≤ 3.

## 1. Why this direction

### TrustMRR evidence
- Listing: `myhair.ai`, MRR $7.43, last30 $6.62, 181 subs.
- demand_h 4, comp_h 3.
- 181 subs despite tiny MRR = mostly free + IAP funnel. We replicate the funnel but fix monetization (subscription-first).

### X / web evidence
- Pain clusters on r/blackhair, r/femalehairline, X hair-tags: "I always regret my fade", "show my barber a picture", "I want to see what a buzz would look like".
- Existing tools: YouCam Makeup (women-focused), ModiFace, generic face-shape apps. **None** are vertical on Black men's fade/lineup.
- "AI haircut preview" search up 60% YoY.

### Wedge
- Audience: Black men ages 18–45, US/UK/CA.
- Inputs: 1 selfie, no angle requirement (we normalize).
- Outputs: 8 looks (buzz, low fade, mid fade, high fade, taper, lineup, frohawk, locs preview) at 512×512.
- Refuse: women haircuts, salon AI, products. Strict vertical.

## 2. Competitor table

| Layer | Name | Pricing | Why we beat |
|---|---|---|---|
| L1 direct | MyHair AI | unknown (mostly IAP) | We narrow to Black men; ship subscription not IAP. |
| L1 direct | AI Barber | (similar) | Generic, no vertical. |
| L2 adjacent | YouCam Makeup | Free + sub $4–9/mo | Women-leaning. |
| L2 adjacent | FaceApp | Free + sub $4–9/mo | Hair filters are generic. |
| L2 adjacent | ModiFace (L'Oréal) | Free, app | Beauty conglomerate, not indie-friendly. |
| L3 substitute | "Show my barber" Google image search | Free | No personalization, no face-shape fit. |

Competition score = 3. Niche is mostly generic face apps; vertical is open.

## 3. PRD MVP

### User stories
- US-01 (P0): Upload selfie, get 8 fade previews in 8s.
- US-02 (P0): Save looks to "My styles".
- US-03 (P0): Share button → "show my barber" deep-link.
- US-04 (P0): Stripe sub $7/mo Starter, $19/mo Pro (full res + history).
- US-05 (P1): "Try before you go" booking reminder push.
- US-06 (P2): Barbershop directory (affiliate).

### Epic → features
- **EPIC A: Face detection + normalization** — face-api.js or MediaPipe; align eyes + crop.
- **EPIC B: Generation** — Stable Diffusion XL fine-tuned on barbershop photo dataset (CC0 + licensed), LoRA per style.
- **EPIC C: Caching** — Same selfie → cache results for 24h (cuts GPU cost).
- **EPIC D: Auth + billing** — Supabase + Stripe.
- **EPIC E: Sharing** — Web Share API + Pinterest card.

### P0 (ship-blocker)
- US-01..04 + EPIC A/B/D (no caching yet).

### P1 (week 1 polish)
- US-05, EPIC C caching, EPIC G shot-sliders (length / how-low / texture).

### P2 (week 2)
- US-06, Pro: full history, 4K renders, barber cards.

### Non-goals
- Women haircuts (out of scope)
- Coloring (out of scope)
- Real-time AR (this is a preview, not a try-on)
- Salon / booking system (out of scope)

### Tech stack
- Next.js 14 + Tailwind + shadcn
- Supabase (auth + db + storage of selfies, encrypted)
- Replicate (Stable Diffusion XL + LoRA, $0.005–0.01 per gen)
- Stripe (billing)
- face-api.js (face detection on client)
- Cloudflare R2 (image cache)

### Data model
- `users(id, email, plan, stripe_customer_id)`
- `renders(id, user_id, style, url, created_at)` — encrypted selfie URL

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Repo, scaffold, design tokens |
| 2 | Auth (Supabase magic link) |
| 3 | Face detection + selfie normalization (client-side) |
| 4 | SDXL LoRA training: 8 fade styles (collect 100 photos each from public barbershop Instagrams) |
| 5 | Replicate API integration: 8 parallel generations |
| 6 | Result grid + save-look flow |
| 7 | Stripe pricing + checkout |
| 8 | Landing page (model headshot hero, 8-style preview, FAQ) |
| 9 | Beta: 30 friends from r/blackhair + X barber tags |
| 10 | Polish: caching, mobile UI, dark mode |
| 11 | Sharing: Web Share API + "show my barber" template card |
| 12 | Analytics: track which styles get shared |
| 13 | Public launch: Product Hunt + X thread |
| 14 | Day-2 retention: weekly "new style" email |

## 5. 30-day marketing calendar (≤ $300)

| Week | Channel | Action | Budget |
|---|---|---|---|
| 1 | X | Thread: "I built a fade preview tool — here are 8 looks" with real renders | $0 |
| 1 | r/blackhair, r/femalehairline (skip the female sub, focus male crossover) | Value post: "preview your next fade" | $0 |
| 1 | IG/TT | DM 5 Black barber IG creators ($50 micro-sponsor) | $50 |
| 2 | X | Daily demo renders, before/after | $0 |
| 2 | YouTube | Guest on 1 barber YouTube channel | $100 |
| 3 | SEO | "best fade preview tool" / "AI fade generator" | $0 |
| 3 | X ads | $50 boost on top thread | $50 |
| 4 | Newsletter | Black lifestyle newsletter ($80 guest) | $80 |
| 4 | Lifetime deal | First-200 users $29 lifetime | — |
| | | **Total** | **$280** |

**Buffer:** $20.

## 6. Unit economics to $10K MRR

- Price: $7 Starter / $19 Pro. Blended ARPU ≈ $12.
- To $10K MRR: 10,000 / 12 = **833 paying users**.
- Free → paid: 5% (style-render habit is sticky but conversion is the choke).
- Signups needed: 833 / 0.05 = **16,666 signups**.
- Visit → signup: 25%.
- Visits: 16,666 / 0.25 = **66,666 visits** ≈ 2,222/day.

CAC: $280 / 833 = **$0.34**. LTV: $12 × 6 mo = $72. LTV/CAC = 211×.

Costs: Replicate $0.01 × 833 users × 4 renders/mo = $33 + Vercel $20 + Supabase $25 + Stripe fees 3% = $300. Wait — at scale Replicate is fine; **total fixed ≈ $80/mo + variable Replicate**. Gross margin at $10K MRR ≈ 97%.

## 7. Kill criteria

- < 200 signups at day 14
- < 3% trial → paid at day 30
- LoRA quality complaints > 25% ("doesn't look like me")
- GPU cost > 40% of revenue (means ARPU too low)
- Privacy complaints (selfies leaking from stage)

## 8. (N/A — GO)

Expansion: add women's facial hair cut, beard style, kids fade preview.
