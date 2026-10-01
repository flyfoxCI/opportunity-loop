---
layout: post
title: "Direction — FaithWall (GO_NARROW: lock-screen Bible verse widget for Gen-Z Christians)"
date: 2026-10-01T21:34:04+00:00
week: "2026-10-01_213404"
week_date: "2026-10-01T21:34:04+00:00"
slug: "faithwall"
permalink: /directions/faithwall.html
tags:
  - "AI"
  - "iOS"
  - "Android"
  - "religion"
  - "creator"
  - "video"
excerpt: "Lock-screen Bible verse wallpaper for Gen-Z Christians"
---

**Tier:** GO_NARROW
**Slug:** `faithwall`
**Run:** 2026-10-01_213404
**One-liner:** Pin a daily Bible verse to your iOS / Android lock screen with a custom typography style. One widget, one job.
**Why this is GO_NARROW, not GO:** the broader "Bible app" market is comp 4 (YouVersion = 100M+ MAU, Glorify, Abide, First5). To pass the dual gate we must lock to **one specific wedge** — the lock-screen widget, Gen-Z only. Anything broader ⇒ KILL.

## 1. Why this direction

### TrustMRR evidence
- Listing: iOS app store, MRR $1.86, last30 $9.02, 105 subs.
- demand_h 4, comp_h 2 (mobile lock-screen wedge).
- Founder @karchijr active on X with related content.

### X / web evidence
- Pain: "I want a daily Bible verse on my lock screen" appears 50+/wk on r/Christian, X, TikTok ChristianTok.
- Existing: YouVersion widget (clunky, ad-supported), Glorify (full app, $5/mo), Abide (sleep + meditation, $3/mo).
- TikTok: "Bible aesthetic" / "lock screen prayer" tags have 2B+ views. Gen-Z is the audience.

### Wedge (REQUIRED — see § 8)
The full-market Bible app category is comp 4+ (YouVersion 100M MAU, Glorify $7M ARR, Abide, First5, etc.). We cannot pass the dual gate in that category. Therefore we lock to:
- **Platform:** iOS + Android lock-screen widget ONLY. No in-app reading, no plans, no devotional library.
- **Audience:** US Gen-Z Christians (18–28), gender-neutral.
- **Frequency:** Daily push at user's chosen time (default 6am).
- **Style:** 6 curated typography themes (Y2K, minimalist, cyberpunk-prayer, cottagecore, gothic, sunset).

## 2. Competitor table

| Layer | Name | Pricing | Why we beat |
|---|---|---|---|
| L1 direct | FaithWall (target) | sub unknown | We narrow further; add 6 styles + Gen-Z aesthetic. |
| L1 direct | Lock-screen Bible widgets (small) | Free | None combine aesthetic + daily + sub. |
| L2 adjacent (comp 4 if we expanded) | YouVersion | Free + IAP | Massive app; lock-screen widget is buried. |
| L2 adjacent | Glorify | $5–7/mo | Full meditation app; lock-screen not the focus. |
| L2 adjacent | Abide | $3/mo | Sleep + meditation. |
| L2 adjacent | First5 | Free | Morning devotional (text); no widget. |
| L3 substitute | iOS shortcut + wallpaper | Free | DIY, ugly, churns. |

Competition score = 2 in the **lock-screen widget wedge** (our scoped market). If we expanded to "Bible app", comp = 4 (KILL).

## 3. PRD MVP

### User stories
- US-01 (P0): Pick a typography style from 6 themes.
- US-02 (P0): Set daily delivery time + verse translation (NIV default).
- US-03 (P0): Add lock-screen widget on iOS / Android.
- US-04 (P0): Stripe sub $2.99/mo, $19.99/yr.
- US-05 (P1): 12 styles (rotate).
- US-06 (P1): Custom verse (paste your own).
- US-07 (P2): Streak counter on widget.

### Epic → features
- **EPIC A: Verse pipeline** — Daily cron (5am ET) selects verse-of-day; supports 5 translations (NIV, ESV, KJV, NRSV, NLT).
- **EPIC B: Rendering** — Templated SVG → PNG, sized to widget.
- **EPIC C: iOS widget** — WidgetKit + App Group + shared container.
- **EPIC D: Android widget** — Glance (Jetpack Glance).
- **EPIC E: Auth + billing** — RevenueCat (handles iOS + Android sub state).
- **EPIC F: Push** — Daily local notification; user taps → opens app + widget update.

### P0 (ship-blocker)
- US-01..04 + EPIC A/B/C/E.

### P1 (week 1 polish)
- US-05, US-06, EPIC D (Android).

### P2 (week 2)
- US-07, custom typography uploads.

### Non-goals
- In-app Bible reading (use YouVersion).
- Devotionals / plans.
- Social / sharing feed.
- Audio narration.
- Prayer journaling.

### Tech stack
- React Native (Expo)
- WidgetKit (iOS) + Jetpack Glance (Android) — via Expo native modules
- RevenueCat (sub state)
- Supabase (verse selection log, user prefs)
- Render: serverless Node + sharp (SVG → PNG)
- EAS Build (CI)

### Data model
- `users(id, device_id, plan, style, translation, push_time)`
- `verse_of_day(date, verse_id, translation)`
- `renders(id, user_id, verse_id, style, png_url)`

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Repo, RN scaffold, design tokens (6 styles) |
| 2 | Verse pipeline: DB table, cron job, 5 translations |
| 3 | SVG template engine (1 style) + 5 more styles |
| 4 | iOS WidgetKit integration |
| 5 | RN app: style picker + settings |
| 6 | RevenueCat + Stripe link |
| 7 | Push notification schedule |
| 8 | Landing page: 6 style previews, pricing |
| 9 | Beta: 30 friends from r/Christian + ChristianTok |
| 10 | Polish: onboarding, error states |
| 11 | Android Glance widget |
| 12 | TestFlight + Play Console upload |
| 14 | Public launch on r/Christian, IH, X Christian-creator DMs |

## 5. 30-day marketing calendar (≤ $300)

| Week | Channel | Action | Budget |
|---|---|---|---|
| 1 | TikTok | Demo: 6 styles, lock-screen reveal | $0 |
| 1 | r/Christian | Value post: "I made a lock-screen verse widget — free for a week" | $0 |
| 1 | X | Daily style posts | $0 |
| 2 | YouTube | DM 5 small Christian YouTubers ($50 micro) | $50 |
| 2 | TikTok | DM 3 ChristianTok creators ($30 micro) | $30 |
| 3 | SEO | "Bible verse lock screen widget" | $0 |
| 3 | X ads | $50 boost on top post | $50 |
| 3 | Reddit ads | r/Christian slot | $50 |
| 4 | Newsletter | Christian newsletter guest post | $50 |
| 4 | Lifetime deal | First-100 users $19.99 lifetime | — |
| | | **Total** | **$230** |

**Buffer:** $70.

## 6. Unit economics to $10K MRR

- Price: $2.99/mo, $19.99/yr. Blended ARPU ≈ $2.50 (mostly monthly).
- To $10K MRR: 10,000 / 2.50 = **4,000 paying users**.
- Free → paid: 4% (faith apps convert; Gen-Z likes low-fee).
- Signups: 4,000 / 0.04 = **100,000 signups**.
- Visit → signup: 30% (App Store organic for "Bible lock screen").
- Visits: 100,000 / 0.30 ≈ **333,000 visits** (App Store + landing combined) over 30d ≈ 11,000/day.

CAC: $230 / 4,000 = **$0.06**. LTV: $2.50 × 9 mo (faith apps retain well) = $22.50. LTV/CAC = 375×.

Costs: RevenueCat free ≤ $2.5K MRR, then 1% = $100 at $10K. Vercel $20 + Supabase $25 + Apple $99/yr + Play $25 one-time = **~$50/mo + $124/yr**. Gross margin at $10K MRR ≈ 99%.

## 7. Kill criteria

- < 5,000 signups at day 14
- < 3% trial → paid at day 30
- Day-30 retention < 25% (typical faith app is 35–45%)
- App Store rejection on religion grounds (low risk; lock-screen widget is benign)
- Verse-render failures > 5%

## 8. Wedge (required for GO_NARROW — what we refuse to build)

To stay in the dual gate, we **refuse** to build any of the following even if users ask:

- ❌ In-app Bible reading or verse search (use YouVersion)
- ❌ Devotionals / reading plans (use First5 / Glorify)
- ❌ Audio narration / TTS (use Abide / Dwell)
- ❌ Prayer journaling / streaks-as-social
- ❌ Social / community / comments
- ❌ Live wallpaper (battery-drain risk)
- ❌ Multiple translations selectable per verse (one per user is enough)
- ❌ "Premium Bible translations" paywall (illegal + ethics)
- ❌ Christian nationalism / political content of any kind
- ❌ Targeting minors under 13 (COPPA)

**The wedge is the lock-screen widget, daily, one verse, six styles.** Every feature that crosses that line is a separate product we do not build. If a roadmap item requires a feature on this list, we **kill** the project before we add it — because by doing so we'd re-enter the comp 4 zone and fail the dual gate.

Expansion path (only if MRR is 2× the kill threshold and comp stays ≤ 3): add a separate app in the seed `Amen/Sermon Scribe` vertical for sermon-note AI; do not stretch FaithWall.
