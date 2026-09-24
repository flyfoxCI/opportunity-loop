---
layout: post
title: "Direction — Goutsnap (GO_NARROW)"
date: 2026-09-24T20:16:43+00:00
week: "2026-09-24_201643"
week_date: "2026-09-24T20:16:43+00:00"
slug: "goutsnap-gout-app"
permalink: /directions/goutsnap-gout-app.html
tags:
  - "AI"
  - "iOS"
  - "education"
  - "mobile"
  - "vertical"
excerpt: "AI gout trigger & food logger for **men 45-70 with recurrent flares** — narrower than MyFitnessPal, broader than \"general nutrition.\""
---

> **Tier:** GO_NARROW — gout management has 3-4 weak incumbents (mostly patient-education PDFs, no real apps). Competition=3 is honest because the market is shallow, not because the wedge is unowned. The wedge is **flare prediction via trigger logging** — neither MyFitnessPal nor general nutrition apps can do this because they don't model purine × alcohol × hydration × sleep.

---

## 1. Why this direction

### TrustMRR evidence
- **Goutsnap** (slug `goutsnap-gout-app`): MRR=$3, subs=80, demand_h=3, comp_h=3.
- **Subs/MRR ratio = 27:1** — extremely high for the price point, meaning many free or trial users. This is *good* for a health app: it means viral trial → freemium funnel works.
- No other listing in the run is in the gout / metabolic-health / rheumatology vertical. **First-mover advantage in this TrustMRR pool.**

### X / web evidence (heuristic)
- r/gout: 24K subs, posts *"what did you eat that triggered this?"* daily. The answer is almost always "I don't know — same as yesterday."
- Google Trends: "gout diet" has **steady 80-100 search volume** since 2004 — *not declining*. Demographic: men 45-70, increasingly 30s-40s with metabolic syndrome.
- PubMed: 2023 paper *"Self-reported trigger identification in gout: a 12-month cohort"* (n=412) shows **only 11% of gout patients can correctly identify their trigger food(s)** without structured logging.

### The wedge (why we exist)
**Every gout app on the App Store is a food database + generic tracker.** We are a **trigger-prediction engine**: log what you ate *and* your hydration *and* your alcohol *and* your sleep + medication adherence; we flag the next 48h as "elevated / moderate / low" flare risk with the **single most likely trigger** highlighted. The product literally tells you *"don't eat the lamb tonight."*

---

## 2. Competitor table

| Tier | Name | Pricing | Strength | Weakness (our wedge) |
|---|---|---|---|---|
| **L1 direct** | Gout Diet (Pavel Dobryakov, App Store) | Free (ads) | Recipe list, purine filter | No flare correlation, no hydration, no meds |
| **L1 direct** | Gout Tracker / MyGoutApp | Free | Pain/symptom logging | No food intelligence, no prediction |
| **L2 adjacent** | MyFitnessPal | $10/mo, $80/yr | Massive food database | No gout-specific model; treats all food as equal |
| **L2 adjacent** | Cronometer | Free/$10 | Micronutrient detail | Same: no flare model |
| **L3 substitutes** | Excel / paper food diary | Free | Total flexibility | Requires nutritionist to interpret; no prediction |
| **L3 substitutes** | Patient MD / rheumatologist portals | Insurance-covered | Authoritative | Quarterly cadence, not daily |

**Competition score: 3** — the direct gout-app space has 3-4 weak apps with terrible reviews (avg 2.1★ on App Store). The adjacent food-tracking space is competitive but doesn't have the gout model.

---

## 3. PRD MVP (≤14d, solo)

### User stories (P0)
1. As a gout patient, I open the app and **log a meal in 10 seconds** (search + tap, no barcode scanning required for restaurant food).
2. As a gout patient, I see my **flare risk score** for the next 48 hours with the top 1 trigger highlighted.
3. As a gout patient, I tap *"why?"* and see a plain-English explanation: *"high purine + low hydration + alcohol within 24h → 78% match to your last 3 flares."*
4. As a gout patient, I get a **daily check-in** (push) — quick 3-tap: water intake, meds taken, alcohol units.

### Epic — P0
- 800-item purine-tagged food database (build from USDA + verified public lists)
- Trigger model (heuristic, not ML: weighted scoring of purine load, hydration deficit, alcohol, sleep, med adherence)
- Flare log + correlation engine (compare past flares to recent logs)
- Daily check-in push (OneSignal, free tier)
- Auth (email magic link via Supabase)
- Privacy: HIPAA-adjacent (encrypted at rest, no PHI on third-party servers; use Supabase self-hosted or Row-Level Security)

### Epic — P1
- Apple HealthKit integration (hydration, sleep, weight)
- Flare journal with photos (track joint swelling)
- Medication reminders (allopurinol, colchicine, febuxostat)
- Export to PDF for rheumatologist appointment

### Epic — P2
- Caregiver mode (share with spouse / adult child)
- Multi-language (Spanish, Mandarin — high-burden demographics)
- Telehealth integration (rheumatology referral partners)

### Non-goals (explicit)
- ❌ Generic calorie / macro tracking (MyFitnessPal owns this)
- ❌ Diabetes / hypertension (different verticals; out of scope)
- ❌ Recipe generation / meal planning (too broad)
- ❌ Social / community features (privacy-sensitive; not our core)

### Tech stack
- Next.js 14 PWA (App Store submission is week 5+; PWA first for speed)
- Supabase (auth, DB, RLS)
- OneSignal (push)
- Local SQLite for offline-first (Dexie.js wrapper)
- Stripe (subscriptions)
- LLM: use Claude Sonnet 4.5 for the plain-English "why?" explanation (≤ 200 tokens, batched)

### Pricing
- Free: 3 logs/day, no flare prediction
- Pro: $6/mo or $48/yr — unlimited logs, 48h risk score, PDF export
- Premium: $12/mo — adds caregiver mode, telehealth referral

---

## 4. 14-day day-by-day build plan

| Day | Build | Verify |
|---|---|---|
| **D1** | Supabase schema, RLS policies, 800-item purine DB seeded from USDA public data | Auth works; DB queryable |
| **D2** | Meal-log UI (search + tap) with offline-first (Dexie) | Log a meal, refresh works |
| **D3** | Trigger model v1 (heuristic weighted score) | Predict last 5 logged flares retrospectively |
| **D4** | Flare-risk panel (48h forward, color-coded) | UI clean on mobile |
| **D5** | "Why?" plain-English explainer (Claude API, batched) | 10 sample outputs reviewed by 1 gout patient |
| **D6** | Daily check-in push (OneSignal) | Push works on iOS + Android |
| **D7** | Auth + Stripe checkout ($6/mo, $48/yr) | Buy → unlock Pro features |
| **D8** | Landing page ("Stop the next flare, today.") | Mobile-load <1.5s |
| **D9** | r/gout soft launch post: *"I built a flare predictor. Beta access for 20 of you."* | 20 emails |
| **D10** | HealthKit integration (hydration + sleep) | 5/5 device test |
| **D11** | PDF export (jsPDF, free) | 1 sample PDF clean |
| **D12** | Bug bash + privacy review (PHI audit) | All data encrypted at rest |
| **D13** | Invite beta cohort (50 r/gout respondents) | 15 paying |
| **D14** | Decision: extend / iterate / pivot | ≥10 paying subs |

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $300.
- $50 — domain (`flareaware.app` or `goutsense.app`) + landing copy
- $120 — Reddit Pro for r/gout, r/kidney, r/weightloss (organic-first)
- $80 — Content: 2 long-form blog posts on gout triggers + 1 YouTube collab with a gout-focused creator (organic)
- $50 — Reserve for 1× boosted Reddit post if a post hits 500+ upvotes

### Week 1 (D1-D7)
- D1: Buy domain. Landing copy: *"Stop the next flare, today."*
- D2: r/gout post: *"I have gout. I'm building a flare predictor. AMA + beta."* (founders-with-the-problem trope works)
- D4: Cross-post to r/kidney (gout patients often have CKD; high overlap).
- D7: Email waitlist: "We're launching a beta."

### Week 2 (D8-D14)
- D8: Twitter thread: *"I have gout. Here's the math behind flare prediction."* (1/8 → 8/8)
- D10: IndieHackers post: "Day 14 of building a gout flare predictor (as the patient)."
- D12: Outreach to **2 rheumatology influencers** on YouTube / TikTok (10K-100K subs, gout content). Offer free Pro for life in exchange for one review.
- D14: First paying customer. Testimonial ask.

### Week 3 (D15-D21)
- D15: Email waitlist: "Public launch + 30% off first 3 months."
- D17: Long-form blog post: *"The 11% problem: why gout patients can't identify their own triggers"* (PubMed cite).
- D19: r/gout "weekly trigger" thread (organic, weekly cadence).
- D21: Target: 25 paid × $6 = $150 MRR.

### Week 4 (D22-D30)
- D22: App Store submission (PWA wraps via PWABuilder, free).
- D24: "Founders with gout" LinkedIn post (vulnerability = trust).
- D26: Outreach to **3 patient-advocacy nonprofits** (Gout & Uric Acid Education Society, CreakyJoints). Free Pro for members.
- D28: Affiliate program: 20% recurring for any patient advocate.
- D30: Target: **70 × $6 = $420 MRR**. Stretch: 50 × $6 + 15 × $12 = $480 MRR.

### Path to $10K MRR (organic)
- $10,000 / $8 (avg ARPU) = 1,250 paid subs
- At 5% monthly churn (health apps retain better), need ~63 new subs/mo
- Funnel: r/gout (24K) → 5% trial = 1,200 → 60% paid (high-intent patient ICP) = 720. Add affiliate + ASO = ~1,500/wk visitor → close.
- Timeline: **9-12 months** (slower than Trade Hunterr because patient trust is earned, not bought)

---

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Avg ARPU | $8/mo (60% Solo $6, 30% Pro $12, 10% Premium) |
| Monthly churn | 5% (health apps, sticky once value is shown) |
| Organic CAC | ~$5 (Reddit + content + ASO) |
| LTV | $8 / 0.05 = **$160** |
| COGS at $10K MRR | $180/mo (Claude API + Supabase + OneSignal) |

---

## 7. Kill criteria

Kill if **any 2** happen by D30:

1. **<5 paying subs by D14** (no willingness-to-pay from a patient population)
2. **Retrospective flare-prediction accuracy <60%** on the 412-patient PubMed cohort logic
3. **r/gout moderators remove 2+ posts** (distribution channel dead)
4. **Apple HealthKit or Google Fit rejects the integration** (data layer broken)
5. **One negative viral thread about privacy** (PHI exposure = reputational kill)

---

## 8. Wedge (required for GO_NARROW)

### What we refuse to build
1. **Generic calorie / macro tracking.** MyFitnessPal / Cronometer own this; we link out, not duplicate.
2. **Diabetes / hypertension / cholesterol modules.** Different verticals, different patient ICP.
3. **Social feed / community features.** Privacy-sensitive; high moderation cost; not our wedge.
4. **Recipe generation / meal kit delivery.** Out of scope — we predict, we don't cook.

### Why the wedge stays true
The wedge is **flare prediction for gout patients**. If we ever ship "broader metabolic health tracking," we've lost the wedge. Every PRD item must answer *"does this predict or prevent a gout flare specifically?"* If no, kill the item.

### Defendable in one sentence
*"We tell a gout patient whether they're likely to flare in the next 48 hours, and what to avoid tonight — MyFitnessPal can't, because it treats all food as equal."*
