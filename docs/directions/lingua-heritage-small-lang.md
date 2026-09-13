---
layout: post
title: "Direction: Lingua — Heritage language learning for diaspora kids (GO)"
date: 2026-09-13T03:51:34+00:00
week: "2026-09-13_035134"
week_date: "2026-09-13T03:51:34+00:00"
slug: "lingua-heritage-small-lang"
permalink: /directions/lingua-heritage-small-lang.html
tags:
  - "AI"
  - "iOS"
  - "B2C"
  - "education"
  - "finance"
  - "language"
excerpt: "| Tier | Competitor | What they do | Price | Threat | |---|---|---|---|---| | L1 | Speak Silq | Heritage-language niche player | $10–$15/mo | Direct. We compete on UX, breadth of languages, family mode. | | L1 | Duolingo, Babbel, Busuu | Big languages | Free–$15/mo | Tangential. "
---

> Tagline: *Not Duolingo. The language your grandparents speak.*

---

## 1. Why this direction

### TrustMRR evidence
- **Speak Silq** (per seed report) — MRR ~$12K. Heritage-language niche player. This is the strongest seed in this list.

### Why this wins
1. **Duolingo's blind spot.** Duolingo covers <40 languages at depth; <1M-speaker heritage languages (Tagalog, Yoruba, Hindi, Urdu, Bengali, Punjabi, Vietnamese, Haitian Creole, Hmong, Somali) get a token 5-unit course.
2. **The buyer is a parent, not the user.** Parents pay $15/mo so their kid can speak to grandma. Different motivation than "I want to learn Spanish for vacation."
3. **High emotional resonance → word-of-mouth.** Diaspora communities are dense, networked, and tight.
4. **iOS-first distribution.** App Store editorial loves heritage-language apps around cultural-heritage months.

### What we ship
A mobile-first iOS app with:
- Daily 5-minute heritage lessons (gamified, voice-first, not flashcards).
- Family mode: up to 4 kid profiles under one parent account.
- "Call Grandma" prompts — situational scripts for kids to actually use the language in their lives.
- Live pronunciation feedback via on-device ASR.
- Cultural mini-stories (not Duolingo's sterile sentences).

---

## 2. Competitor table

| Tier | Competitor | What they do | Price | Threat |
|---|---|---|---|---|
| L1 | Speak Silq | Heritage-language niche player | $10–$15/mo | Direct. We compete on UX, breadth of languages, family mode. |
| L1 | Duolingo, Babbel, Busuu | Big languages | Free–$15/mo | Tangential. Their Tagalog course has 20 units. |
| L2 | Mango Languages, Rosetta Stone | 60+ languages including some small ones | $8–$20/mo | Older demos, no kid mode. |
| L2 | italki, Preply | Tutor marketplace | $15–$60/hr | Different model. We are async + on-device. |
| L3 | YouTube channels, free podcasts | Free | $0 | Real but unstructured. We package and gamify. |
| L3 | Heritage Facebook groups | Free community | $0 | We market there, don't compete. |

**Competition score: 2.** Speak Silq is real but small relative to market; Duolingo is broad but shallow in our vertical.

---

## 3. PRD MVP

### User story
> *I'm a Filipino-American mom in Jersey City. My 7-year-old speaks English at school and barely understands Tagalog when Lola calls. I want an app he opens 5 minutes a day, in Tagalog, with the words Lola actually uses ("kumain ka na?", "mag-ingat", "tulog na"), not "the cat is on the table".*

### Epics
- **E1 — Language packs.** 6 launch languages: Tagalog, Yoruba, Hindi, Urdu, Vietnamese, Bengali.
- **E2 — Daily lesson engine.** Voice-first, 5-minute, kid-paced.
- **E3 — Family mode.** Up to 4 profiles per parent.
- **E4 — Pronunciation feedback.** On-device ASR (Apple Speech Analyzer on iOS 17+).
- **E5 — Cultural stories.** 30 mini-stories per language.
- **E6 — Billing.** StoreKit 2 (App Store IAP) + RevenueCat.
- **E7 — Push.** Daily reminder at parent's chosen time.

### P0 (days 1–10)
- iOS app scaffold (SwiftUI).
- 1 language (Tagalog) end-to-end: 14 days of content, ASR feedback, daily push.
- RevenueCat IAP ($14.99/mo, $99.99/yr).
- App Store Connect listing with screenshots.

### P1 (days 11–14)
- Add 2 more languages (Yoruba, Hindi). Native-speaker review via Upwork (~$300 total).
- Family mode (up to 4 profiles).
- Onboarding survey (kid age, parent's heritage, learning goal).

### P2 (post-MVP, days 15–30)
- Add Urdu, Vietnamese, Bengali.
- "Call Grandma" prompts (situational roleplay).
- Web companion for parents to track progress.
- Apple Watch glance.

### Non-goals
- Tutors / live classes. (Different model.)
- 50+ languages. (Six at launch; ten by day 60.)
- Teacher dashboards. (B2C only at MVP.)
- Android. (iOS-first; ship Android P2.)

### Pricing
- **Free:** 1 lesson/day, 1 language, with ads.
- **Plus ($14.99/mo):** Unlimited lessons, all languages, family mode, no ads.
- **Year ($99.99/yr):** Plus features, 30% off.

---

## 4. 14-day day-by-day build plan

| Day | Output |
|---|---|
| 1 | Lock languages (start with Tagalog). Buy app name. Set up RevenueCat. |
| 2 | SwiftUI scaffold, navigation, login (Sign in with Apple). |
| 3 | Lesson engine: prompt → audio → user response → ASR feedback. |
| 4 | Tagalog content: 14 days × 5 lessons = 70 lessons. (Hand-write with native-speaker review.) |
| 5 | ASR integration (Speech framework + Whisper fallback). |
| 6 | Daily push (UserNotifications). |
| 7 | RevenueCat IAP wired. Free vs Plus gating. |
| 8 | Onboarding (age, heritage, goal). |
| 9 | Screenshots, App Store metadata, privacy nutrition label. |
| 10 | TestFlight beta (20 families from personal network). |
| 11 | Add Yoruba + Hindi content + reviews. |
| 12 | Family mode (up to 4 profiles). |
| 13 | Bug bash + App Store submission. |
| 14 | Launch (week 3 of the 30-day calendar). |

**Stack:** SwiftUI + RevenueCat + Firebase (analytics) + Apple Speech + Whisper (fallback) + Cursor for content authoring.

**Infra cost at MVP:** ~$30/mo.

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget allocation**
- $120 — Apple Search Ads (US, $4/day)
- $80 — Sponsorship of 4 diaspora Facebook groups (Filipino, Nigerian, Indian, Pakistani in US)
- $50 — Influencer gifting: 10 micro-creators in diaspora TikTok (free product + $5 stipend)
- $30 — Canva Pro for cultural graphics
- $20 — Boost a launch post in r/filipino, r/india, r/nigeria

**Daily calendar (organic + App Store SEO is the spine)**

| Wk | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| 1 | TikTok: "I'm building an app so my kids speak Tagalog with Lola" | Post in Filipino-American FB groups | X thread: why Duolingo fails diaspora kids | TikTok demo (in Tagalog) | Reddit: r/filipino, r/asianamerican | Apple Search Ads live ($4/day) | Rest |
| 2 | App Store launch | Press release to 5 Pinoy news outlets (free) | TikTok creator outreach (10 gifts) | FB group post: Tagalog lessons | Reddit: r/asianamerican, r/hapas | Push for App Store editorial | First weekly TikTok |
| 3 | Add Yoruba + Hindi | TikTok: Nigerian creator gift #1 | FB group post: Yoruba lessons | Reddit: r/nigeria | TikTok: Hindi lessons | Apple Search Ads $5/day | Press release for Hindi edition |
| 4 | TikTok: "5 words Lola actually says" | Email blast to diaspora newsletter list | FB group post: Hindi lessons | Reddit: r/india | X thread: cultural stories | Push for #2 App Store editorial (Heritage Month tie-in) | Wrap-up |

**Targets (week 4):**
- 2,000 App Store impressions/day via Search Ads + organic
- 200 free downloads
- 10% free → paid = 20 paid
- 20 × $14.99 = **~$300 MRR by day 30**
- Realistic month-1 MRR: $200–$400.

**Channel diversification:** no >40% on Apple Search Ads. We lean heavily on organic diaspora Facebook + TikTok because those are the trust channels.

---

## 6. Unit economics to $10K MRR

| Metric | Value | Source |
|---|---|---|
| ARPU | $13/mo | 80% monthly at $14.99, 20% annual at $99.99 ÷ 12 ≈ $8.33 |
| Gross margin (after Apple 30% / 15% for small biz) | 70% | Apple takes 30% on monthly, 15% on annual after $1M |
| Monthly churn | 8% | Consumer education apps churn hard |
| Net new paid subs/mo (steady state) | 250 | Slower than B2B; relies on viral diaspora networks |
| Months to $10K MRR | ~6 | (10,000 / 13) / (250 × 0.92) ≈ 5.6 months |

**Sensitivity:**
- If churn is 12% (consumer norm) → ~10 months.
- If annual mix rises to 40% → ARPU drops, time stretches to ~8 months.
- If a diaspora creator with 1M+ followers organically posts → time to $10K can compress to 4 months.

**Worst case (churn 12%, ARPU $11):** ~14 months. Outside the 12-month window. The plan B is to exit at $3–5K MRR or pivot to B2B school district sales.

---

## 7. Kill criteria

- **Day 14:** If App Store conversion (impression → download) <3%, kill. ASO is wrong.
- **Day 30:** If free → paid conversion <5%, kill. Product doesn't earn its keep.
- **Day 60:** If MRR < $400, kill. The diaspora funnel isn't producing.
- **Day 90:** If churn >15%, kill. Consumer education isn't the right shape for this product.
- **Hard kill:** Duolingo launches a "heritage mode" and our download rate drops >50% in 7 days.

---

## 8. Founder fit notes

- **Best for:** founder who is themselves heritage-bilingual, or has deep ties to one diaspora. Bonus: native content writer on retainer.
- **Bad fit if:** you have no connection to any diaspora community and can't hire native reviewers cheaply.
- **Extension path after $10K MRR:** add more languages (Hmong, Somali, Haitian Creole), B2B school-district sales for heritage-language programs, sell the brand to a language-learning roll-up.
