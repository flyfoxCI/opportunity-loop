---
layout: post
title: "Direction: Amen — Faith / Religion AI co-pilot (GO)"
date: 2026-09-13T03:51:34+00:00
week: "2026-09-13_035134"
week_date: "2026-09-13T03:51:34+00:00"
slug: "amen-faith-ai"
permalink: /directions/amen-faith-ai.html
tags:
  - "AI"
  - "SaaS"
  - "B2C"
  - "religion"
  - "mobile"
  - "vertical"
excerpt: "| Tier | Competitor | What they do | Price | Threat | |---|---|---|---|---| | L1 | Sermon Scribe (TrustMRR / sermon-scribe.md) | AI sermon prep + outlines for Christian pastors | ~$6/mo + tiers | Direct. Currently the incumbent. We compete on (a) multi-faith from day 1, (b) bette"
---

> Tagline: *Sermon Scribe, but for every faith — and twice as fast.*

---

## 1. Why this direction

### TrustMRR evidence (real, not self-reported)
- **Sermon Scribe** — `demand=5, comp=2`, MRR ~$14K, 2,362 paying subscribers, growing.
  A solo founder's AI sermon-prep tool. Pricing tiers visible on the listing. This is the strongest single signal in the seed: ~$6 ARPU × 2,362 subs ≈ $14K MRR.
- **Quran Unlock** — `demand=4, comp=2`, MRR $7, last30 $8, 274 subs.
  Independent confirmation the wedge extends to Muslim vertical. Only 274 subs at <$0.10 effective ARPU suggests the product is still early / free-leaded — exactly the entry window.
- **Composer.AI / Goodie AI** — listed under `security_vibe` cluster, but the cluster tag is just TrustMRR's keyword heuristic. Both are consumer mobile AI, and Goodie AI's 3,860 subs confirm that "niche religion-adjacent mobile AI" is a viable distribution path.

### Web / category evidence (heuristic + prior research)
- Google query "AI sermon writing tool 2026" surfaces: Sermon Scribe, Sermonary, ChatGPT-as-workaround. Sermonary is a manual planning SaaS, not generative AI. There is no credible generative-AI competitor for pastors today.
- The "Pastor burnout" / "small-church pastor wears 7 hats" trope is well-documented in US seminary press (e.g. Barna, Christianity Today 2023–2025). Same dynamic for Imams serving diaspora communities.
- Vertical SaaS precedent: Tithe.ly, Pushpay, Subsplash, Planning Center dominate church *admin*, but none offer generative content. The space between Planning Center and ChatGPT is empty.

### Why it's selectable
1. Demand is empirically paid (Sermon Scribe is at scale).
2. Competition is empirically thin (no L1 generative-AI competitor for faith leaders).
3. MVP fits 14 days: prompt chains + template library + Stripe + a focused landing page.
4. Marketing is organic-first: pastors live on Facebook groups, YouTube, and a handful of conferences.
5. Wedge is intrinsically viral: every sermon output is shareable content that brings more pastors.

---

## 2. Competitor table

| Tier | Competitor | What they do | Price | Threat |
|---|---|---|---|---|
| L1 | Sermon Scribe (TrustMRR / sermon-scribe.md) | AI sermon prep + outlines for Christian pastors | ~$6/mo + tiers | **Direct.** Currently the incumbent. We compete on (a) multi-faith from day 1, (b) better outline→manuscript continuity, (c) lower price floor. |
| L1 | Quran Unlock (TrustMRR / quran-unlock.md) | Quran memorization helper (mobile, iOS App Store) | Free + IAP | Adjacent, not direct. Validates Muslim demand. |
| L2 | Sermonary | Manual sermon planning + collaboration | $12–$20/mo | Workflow tool, not generative. Coexistence. |
| L2 | ChatGPT (generic) | General-purpose LLM | $20/mo | Real competitor for "DIY" pastors. Our wedge: templates, scripture-aware quoting, citation discipline, no theological hallucination. |
| L2 | Logos Bible Software | Deep Bible study + original-language tools | $50–$400/yr | Heavy. We integrate, not replace. |
| L3 | Planning Center, Subsplash, Tithe.ly | Church admin | $0–$500/mo | Different layer. Future integration target. |
| L3 | Pulpit AI, Sermo AI (small indie attempts) | Hobby/indie projects, none scaled | Unknown | Monitor. |

**Competition score: 2.** One direct competitor (Sermon Scribe) at scale, but the category is wide (every Christian denomination + Islam + Judaism + Sikhism + Buddhism). Sermon Scribe owns ~10% of the addressable market at best.

---

## 3. PRD MVP

### User story
> *I'm a bi-vocational pastor of a 90-person church. I have 8 hours a week to prep Sunday's sermon plus a midweek Bible study and a parents' newsletter. I want a single AI workspace that knows my denomination, remembers my past sermons, and gives me a polished draft I can actually preach from.*

### Epics
- **E1 — Onboarding & tenant.** Email signup → Stripe customer → 2-question faith/tradition picker → first project.
- **E2 — Sermon / khutbah / dvar torah generator.** Input: passage + occasion + length + audience. Output: outline → manuscript → social clip → discussion guide.
- **E3 — Study tool.** Verse lookup with cross-references and original-language footnotes.
- **E4 — Library.** Search past outputs. Tag, favorite, export Markdown / PDF / DOCX.
- **E5 — Billing.** Stripe subscriptions, free tier (3 runs/mo), paid ($9/mo individual, $29/mo church, $79/mo multi-staff).

### P0 (must-ship, days 1–10)
- Auth (email magic link, password fallback).
- Stripe Checkout + customer portal.
- 5 faith presets: Christian (Reformed, Evangelical, Catholic), Sunni Islam, Shia Islam, Orthodox Judaism, Reform Judaism.
- 1 core flow per preset: "sermon/khutbah/dvar torah from passage".
- Outlines + full manuscript generation.
- Export Markdown and DOCX.
- Single landing page + pricing.
- Plausible analytics + Stripe webhook → customer table.

### P1 (days 11–14)
- Bible/Quran/Torah text corpus with citation discipline (we do not hallucinate chapter:verse).
- Discussion guide generator for small groups.
- Email drip (Day 0, 3, 7, 14).
- Basic admin dashboard (users, MRR, churn).

### P2 (post-MVP, days 15–30)
- Social clip generator (short-form text for IG/X — *not* video).
- Church-plan seat pricing.
- Webhooks for Planning Center / Tithe.ly.
- Multilingual UI (Spanish, Bahasa Indonesia, Turkish, Arabic).

### Non-goals (we will *not* build in MVP)
- Video generation. (Margins die. TrustMRR `muxa-ai` shows video is a different game.)
- Live-streaming or church-website hosting. (Subsplash owns that.)
- Donations / giving. (Tithe.ly owns that. We do not touch money flows except our own.)
- Mobile native app. (Web responsive only for MVP; PWA later.)
- Theological-council or doctrinal arbitration features. (High liability, low margin.)

### Pricing (final)
- **Free:** 3 generations/mo, watermark on exports.
- **Solo ($9/mo):** Unlimited generations, 1 faith preset, DOCX export.
- **Church ($29/mo):** Up to 3 seats, all faith presets, study tool.
- **Multi-staff ($79/mo):** Up to 10 seats, shared library, admin roles.

---

## 4. 14-day day-by-day build plan

| Day | Owner | Output |
|---|---|---|
| 1 | solo | Lock the 5 faith presets' prompt chains in `prompts/`. Build landing copy. Buy domain (`amencopilot.ai` etc.). Set up Cloudflare + Vercel. |
| 2 | solo | Auth (Clerk or self-hosted NextAuth). Magic link + password. Postgres (Supabase). |
| 3 | solo | Stripe Checkout integration. Webhook → `subscriptions` table. Customer portal link. |
| 4 | solo | Generator core: passage input → outline → manuscript. Christian Reformed preset end-to-end. |
| 5 | solo | Add Evangelical + Catholic presets. Build citation-discipline guard (chapter:verse validator against local corpus). |
| 6 | solo | Add Sunni + Shia presets. Manual review of 10 sample khutbahs for tone and accuracy. |
| 7 | solo | Add Orthodox + Reform Judaism presets. Sample dvar torahs reviewed by a friendly rabbi (offer a $50 honorarium via the "Reviewer" Stripe Connect). |
| 8 | solo | Export pipeline: Markdown / DOCX (use `docx` npm package). Email the result. |
| 9 | solo | Free-tier metering (3/mo soft cap). Plausible events on key actions. |
| 10 | solo | Pricing page + 3 testimonials from friendly pastors (do this by giving them free year-1 access in exchange for an honest quote). |
| 11 | solo | Discussion guide generator (study tool P1). |
| 12 | solo | Admin dashboard (Next.js route, restricted). |
| 13 | solo | Email drip via Resend (Day 0 / 3 / 7 / 14). Bug bash. Lighthouse pass. |
| 14 | solo | Public launch: Product Hunt draft ready, IndieHackers post ready, pastor Facebook groups queued. |

**Stack (chosen for 14-day feasibility, not beauty):**
- Next.js 14 (App Router) + TypeScript
- Tailwind + shadcn/ui
- Postgres on Supabase
- Stripe Checkout + customer portal
- OpenAI gpt-4o-mini (primary) + gpt-4o (fallback for paid)
- Plausible (self-hosted or hosted, $9/mo)
- Resend for email
- Vercel hosting (free → pro at MRR)

**Estimated infra cost at MVP:** <$50/mo.

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget allocation**
- $150 — Boosted Facebook posts in 4 pastor groups (one boost per week)
- $80 — Logos / Crosswalk / Islamicity display ads (CPC ~$0.40)
- $40 — Product Hunt launch day boost (graphic design via Canva Pro)
- $30 — Conference: one in-person visit to a local pastor network meetup (gas + coffee)

**Daily calendar (organic is the spine, paid only on days 7, 14, 21, 28)**

| Wk | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| 1 | Ship landing page, email list form | Post in r/Reformed, r/Pastors | X thread: "I built an AI sermon tool — here's what 50 pastors told me" | LinkedIn long-form post | TikTok: 60-sec "How I prep a sermon in 20 min" | YouTube Short: side-by-side ChatGPT vs Amen | Rest (publish) |
| 2 | IndieHackers post + PH draft | Cold-email 20 seminary professors (free seats) | X thread: theology guardrails | Facebook pastor group post | First paid FB boost ($40) | PH launch | Sunday — observe sermon-day virality |
| 3 | Outreach to 5 small-church networks | X thread: 7 free prompt templates | Email blast to list | TikTok: "what AI gets wrong about preaching" | Reddit: r/Christianity, r/Islam (genuine value posts, no spam) | Crosswalk display ads on ($30) | Guest post on a pastor blog |
| 4 | Cold-email 30 district superintendents | X thread: customer results | Email blast #2 | Second paid FB boost ($40) | Logos display ads on ($50) | Wrap-up retrospective | Final email: case studies |

**KPI dashboard (week 4 target)
- 2,000 unique landing visitors
- 250 email signups (12.5% conversion)
- 40 paid conversions ($9 × 40 = $360 MRR)
- 6 church-plan conversions ($29 × 6 = $174 MRR)
- **MRR ≈ $534 by day 30** (running 30-day, not annualized)

**Channel diversification rule:** never >50% of paid spend on a single platform. We keep it spread across Meta, Google Display, and one direct conference touch.

---

## 6. Unit economics to $10K MRR

| Metric | Value | Source / Assumption |
|---|---|---|
| ARPU (blended Solo + Church) | $14/mo | Weighted: 70% Solo ($9), 25% Church ($29), 5% Multi ($79) |
| Gross margin | ~82% | Stripe 2.9% + 0.3%, OpenAI ~$0.40/gen, Resend $0.0001/email |
| Monthly logo churn | 4% | SaaS consumer median; faith audience tends to be sticky |
| Net new MRR / month (steady state) | ~$2,800 | 200 net new subs/mo at $14 ARPU, minus churn |
| Months to $10K MRR | ~3.5 | (10,000 / 2,800) = 3.6 months from launch |

**Sensitivity:**
- If churn is 6% instead of 4% → ~5 months to $10K.
- If ARPU falls to $10 (more Solo, fewer Church) → ~5 months.
- If a paid acquisition channel collapses → switch fully organic (still 8–10 months).

**Worst-case (no paid, 6% churn, $10 ARPU):** $10K MRR in ~12 months. Still inside the year window.

---

## 7. Kill criteria

- **Day 14:** If landing conversion (visitor → email) is <3%, kill or pivot the value prop. Means copy or audience is wrong.
- **Day 30:** If free → paid conversion is <2%, kill. Means the product doesn't earn its keep.
- **Day 60:** If MRR < $300 and weekly growth < 10%, kill. Means no organic engine.
- **Day 90:** If MRR < $1,500 despite 3 paid channels tried, kill. Means the market is fundamentally small or Sermon Scribe's moat is real.
- **Hard kill triggers:**
  - A well-funded entrant (>$5M raised) ships a comparable tool and our organic growth flatlines for 14 days.
  - Theological-correctness complaints cluster (we cannot defend our prompts).

---

## 8. Founder fit notes

- **Best for:** solo founder who can write English + reads theology. Pastors trust people who sound like insiders; even one seminary contact helps.
- **Bad fit if:** you have zero faith-community network and no interest in writing/editorial. The product is 50% prompt engineering, 50% audience trust.
- **Extension path after $10K MRR:** add Hindu and Buddhist presets (huge diaspora), add team accounts, build a "devotional generator" for small groups, sell via church-plan distribution (Tithe.ly, Pushpay marketplace listings).
