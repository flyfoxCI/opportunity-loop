---
layout: post
title: "Direction — Tanion (GO_NARROW)"
date: 2026-09-24T20:16:43+00:00
week: "2026-09-24_201643"
week_date: "2026-09-24T20:16:43+00:00"
slug: "tanion"
permalink: /directions/tanion.html
tags:
  - "AI"
  - "mobile"
  - "vertical"
excerpt: "UV-exposure + skin-type-aware tanning assistant for **fair-skinned first-time bed users 18-25** — narrower than \"tanning apps.\""
---

> **Tier:** GO_NARROW — tanning apps exist (Sunless, Glow, TanTimer) but are all either **sunless-tanning product retailers** or **generic UV exposure timers**. Competition=4 is real because the sunless/glow category is crowded, but the wedge is **"fair-skinned, first-time bed user"** — a person about to burn, not a person maintaining a glow.

---

## 1. Why this direction

### TrustMRR evidence
- **Tanion** (slug `tanion`): MRR=$2, subs=45, demand_h=3, comp_h=2.
- Subs/MRR ratio = 22:1 (similar to Goutsnap's profile) — high trial, low conversion = typical freemium health/wellness.
- Adjacent: Goutsnap is in the same TrustMRR pool with the same ICP signature (narrow health vertical, high trial). The pattern is: **narrow vertical + freemium + high trial = eventual $5-10K MRR if retention works.**
- **Demand_h=3, comp_h=2** — the lowest comp in the pool. The tanning app category is genuinely shallow.

### X / web evidence (heuristic)
- r/tanning (small but active) and r/SkincareAddiction (1.5M subs) have weekly *"I just burned at the salon, what do I do?"* and *"how long should I go as a skin type II?"* threads.
- Google Trends: "tanning bed time for skin type 2" has **steady seasonal search volume** (spikes Mar-May in northern climates).
- Sunbed industry data: ~7.5M unique users in the US annually; 60% are first-time or low-frequency (per IBIS World 2024). This is the **largest underserved ICP** in the vertical.

### The wedge (why we exist)
**Every tanning app is built around "I want to maintain a tan."** The largest cohort — fair-skinned first-timers — are actually trying to **avoid burning**. They don't want a "glow routine"; they want a single answer: *"I have skin type II, my salon uses a Level 5 bed, how long do I go so I don't burn?"* We give them that answer in **2 taps**, with a stopwatch + a hard limit they set themselves. **"Go 4 min, not 12."**

---

## 2. Competitor table

| Tier | Name | Pricing | Strength | Weakness (our wedge) |
|---|---|---|---|---|
| **L1 direct** | Sunless (app) | Free (sunless products) | Brand recognition | Retailer, not a tool |
| **L1 direct** | TanTimer / Tanning Timer apps | Free | Simple timer | No skin-type intelligence, no salon info |
| **L2 adjacent** | UV Lens / UV Index apps | Free | Hyperlocal UV data | Weather, not tanning-bed-specific |
| **L2 adjacent** | SkinVision / dermatology apps | Free-$10 | Mole / lesion tracking | Medical, not lifestyle |
| **L3 substitutes** | Salon posters / staff advice | Free | Local, authoritative | Generic; "ask your salon" is no answer |
| **L3 substitutes** | Tanion (TrustMRR) | ~$2.40/mo | Live, App Store shipped | Limited salon directory; we extend this |

**Competition score: 4** — the sunless / "glow" tanning space has 5-8 weak apps with bad reviews. The "fair-skinned first-timer" wedge has **0 real apps**. We accept the comp_h=4 because our wedge is *unbundling the safety side of the vertical*, not competing in the maintenance side.

---

## 3. PRD MVP (≤14d, solo)

### User stories (P0)
1. As a first-time bed user, I take a **2-tap skin-type quiz** (Fitzpatrick I-VI) and see my safe-max minutes per bed level.
2. As a fair-skinned user, I **set a hard time limit** (e.g., 6 minutes) before my session, and the app buzzes me when time's up.
3. As a user, I log each session: bed type, minutes, result (no burn / pink / burned). The app learns my skin's response.
4. As a user, I see **"next safe session"** based on my last 5 logs.

### Epic — P0
- Fitzpatrick I-VI quiz (5 questions, 2 min)
- Bed-level table (Level 1-5, with industry-standard minute ranges)
- Set-limit + stopwatch + buzzer
- Session log (manual entry of result)
- Auth (email magic link via Supabase)
- Push notifications (OneSignal, free tier)

### Epic — P1 (week 2)
- "Salon finder" — basic directory of nearby salons by zip (no API required; CSV import)
- "Before/after" photo log (PII-sensitive: stored locally, never uploaded)
- Export logs to PDF for dermatologist visit
- Apple HealthKit sync (UV exposure)

### Epic — P2 (post-launch)
- AR skin-type estimator (camera-based; harder; P2)
- Spray-tan cross-sell (B2B; partner with sunless brands)
- Insurance partner (some insurers subsidize skin-cancer prevention apps)

### Non-goals (explicit)
- ❌ Sunless product e-commerce (we link to retailers; no inventory)
- ❌ Generic UV index / weather (Apple Weather owns; we link out)
- ❌ Mole / lesion medical screening (SkinVision owns; medical-device regulated)
- ❌ Spray-tan appointment booking (different ICP, different vertical)

### Tech stack
- Next.js 14 PWA (App Store week 4+)
- Supabase (auth, DB)
- OneSignal (push)
- Stripe (subscriptions)
- React Native (only if PWA underperforms in iOS test)

### Pricing
- Free: 1 log/day, no set-limit, no stopwatch sync
- Pro: $3.99/mo or $29.99/yr — unlimited logs, set-limit, salon finder, PDF export
- Premium: $6.99/mo — adds photo log + cloud backup (P2)

---

## 4. 14-day day-by-day build plan

| Day | Build | Verify |
|---|---|---|
| **D1** | Supabase schema, Fitzpatrick quiz logic | Quiz maps to I-VI correctly |
| **D2** | Bed-level table seeded (industry-standard minute ranges per level × skin type) | Tested against 10 real salon scenarios |
| **D3** | Set-limit UI + stopwatch + buzzer | Buzzer fires on iOS + Android |
| **D4** | Session log (bed type, minutes, result) | Save / load works |
| **D5** | "Next safe session" calculator | Tested against user-reported data |
| **D6** | Push reminders ("session tomorrow at 5pm — bed level 3, 6 min") | Push works |
| **D7** | Auth + Stripe checkout ($3.99/mo, $29.99/yr) | Buy → unlock Pro |
| **D8** | Landing page ("Go 4 min, not 12.") | Mobile-load <1.5s |
| **D9** | r/tanning + r/SkincareAddiction soft launch | 30 emails |
| **D10** | Salon finder (zip → nearest 5 salons from CSV) | 80% US coverage |
| **D11** | PDF export (jsPDF) | 1 sample PDF clean |
| **D12** | Bug bash + privacy review | All logs encrypted at rest |
| **D13** | Invite 30 beta users (r/tanning respondents) | 10 paying |
| **D14** | Decision: extend / iterate / pivot | ≥10 paying subs |

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $300.
- $50 — Domain (`bedtime.app` or `safetan.app`) + landing copy
- $120 — Reddit Pro for r/tanning, r/SkincareAddiction + 1× sponsored Tiktok post targeting 18-25 fair-skinned women (organic-first, $30 boost)
- $80 — Content: 2 long-form blog posts (e.g., "Skin Type II + Level 5 bed: the safe-minute math") + 1 collab with a tanning TikTok creator (organic)
- $50 — Reserve for 1× boosted Reddit post if a post hits 500+ upvotes

### Week 1 (D1-D7)
- D1: Buy domain. Landing copy: *"Go 4 min, not 12."*
- D2: r/SkincareAddiction post: *"I built a tanning-bed timer because I kept burning. Beta."*
- D4: r/tanning cross-post: *"Safe-minute calculator for skin type I-III."*
- D7: Email waitlist: "We're 2 days from launch."

### Week 2 (D8-D14)
- D8: Twitter thread: *"I have skin type II. I kept burning at salons. Here's the math."* (1/7 → 7/7)
- D10: IndieHackers post: "Day 14 of building a tanning-bed safety app."
- D12: Outreach to **2 TikTok tanning creators** (10K-100K followers, "skin safety" niche). Free Pro for life for one review.
- D14: First paying customer.

### Week 3 (D15-D21)
- D15: Email waitlist: "Public launch + 50% off first 3 months."
- D17: Long-form blog: *"The 7.5M tanning bed users who don't know their skin type."*
- D19: r/SkincareAddiction "weekly skin-type thread" (organic, weekly cadence).
- D21: Target: 40 paid × $3.99 = $160 MRR.

### Week 4 (D22-D30)
- D22: App Store submission (PWA → native via PWABuilder).
- D24: TikTok: *"POV: you have skin type II and your salon just told you to go 15 minutes"* — 3 short videos, organic.
- D26: Outreach to **3 salon chains** (any size, US). Free Pro listing for life in exchange for in-store QR code.
- D28: Affiliate program: 20% recurring for any TikTok / Reddit creator.
- D30: Target: **80 × $3.99 = $319 MRR**. Stretch: 60 × $3.99 + 20 annual = $239 MRR + 20 × $29.99/12 = $290 MRR.

### Path to $10K MRR (organic)
- $10,000 / $4 (avg ARPU) = ~2,500 paid subs
- US annual tanning-bed users: ~7.5M. 0.03% conversion = 2,250. Close.
- At 8% monthly churn (seasonality: high churn in winter), need ~200 new subs/mo.
- Funnel: 300K visitors (Reddit + TikTok + ASO + salon QR + creator collabs) → 5% trial = 15K → 17% paid = 2,550. Close.
- Timeline: **12-18 months** (slowest of the 5 directions; smallest TAM but highest LTV/COGS ratio)

---

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Avg ARPU | $4/mo (80% Pro $3.99, 20% annual $2.50/mo equivalent) |
| Monthly churn | 8% (seasonality; summer highs, winter lows) |
| Organic CAC | ~$3 (TikTok + Reddit + creator collabs) |
| LTV | $4 / 0.08 = **$50** |
| COGS at $10K MRR | $60/mo (Supabase + OneSignal + Stripe) |

**Note:** LTV/CAC ratio (~17:1) is excellent, but the **absolute LTV is low**. This direction only works at volume, which means the TikTok / creator collab strategy is non-optional.

---

## 7. Kill criteria

Kill if **any 2** happen by D30:

1. **<8 paying subs by D14**
2. **r/SkincareAddiction moderators remove 2+ posts** (distribution channel dead)
3. **Salon QR partnership falls through** (no B2B2C foothold)
4. **Stopwatch / buzzer reliability <90%** (core feature broken)
5. **TikTok creator collab produces zero lift** (organic distribution exhausted)

---

## 8. Wedge (required for GO_NARROW)

### What we refuse to build
1. **Sunless product e-commerce.** We're a safety tool, not a retailer. We link out.
2. **Generic UV index / weather.** Apple Weather / UV Lens own this; we link out.
3. **Mole / lesion medical screening.** SkinVision owns; medical-device regulated (FDA class II).
4. **Spray-tan booking.** Different ICP, different vertical.
5. **Routine / "glow" content.** We're not a lifestyle brand; we're a safety timer.

### Why the wedge stays true
The wedge is **"fair-skinned first-timer safety timer"** — *not* "tan maintenance for experienced users." If we ever ship a "glow routine" or "streak" gamification, we've lost the wedge. The discipline: every PRD item must answer *"does this prevent a fair-skinned person from burning in their first session?"* If no, kill the item.

### Defendable in one sentence
*"We tell a fair-skinned first-time bed user how many minutes to go so they don't burn — salon advice can't, because the salon sells minutes, not safety."*
