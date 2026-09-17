---
layout: post
title: "Direction: sonora-ai (Narrow AI Sound Utility — iOS-first, Sleep vertical)"
date: 2026-09-17T20:00:47+00:00
week: "2026-09-17_200047"
week_date: "2026-09-17T20:00:47+00:00"
slug: "sonora-ai"
permalink: /directions/sonora-ai.html
tags:
  - "AI"
  - "iOS"
  - "SaaS"
  - "language"
  - "mobile"
  - "vertical"
excerpt: "AI sound/noise app on iOS at $39 MRR / 194 subs — narrow by use case"
---

Slug: `sonora-ai`
Tier: **GO_NARROW**
Demand: 4 · Competition: 2
MRR signal: $39 / 194 subs / $44 last30
Run: 2026-09-17_200047

---

## 1. Why this direction

**TrustMRR evidence.** Sonora AI at $39 MRR with 194 paying iOS subscribers = mobile utility willingness-to-pay at low price ($0.20 ARPU suggests $1.99/mo or $4.99/mo with trial conversions). 194 subs = real audience, not a hobby app.

**Why GO_NARROW.** Mobile utility is a crowded shelf (App Store has 1.5M+ apps). To ship in 14 days *and* get found organically, we narrow by: **iOS only, one vertical (sleep), one feature (adaptive white/pink/brown noise + sleep timer)**.

**What we replicate.** The pattern from `reports/directions/04-lingua-small-language.md` — niche mobile utility for a specific use case, App Store organic ASO, subscription at $4.99/mo.

**X/web evidence.** Pain searches empty; we lean on the iOS-utility proven pattern.

---

## 2. Competitor table

| Tier | Product | Pricing | Wedge gap |
|---|---|---|---|
| L1 direct | Calm, Headspace | $14.99/mo | Full meditation suites, $15 is too much for "just noise" |
| L2 adjacent | BetterSleep, myNoise | Free + $4.99/mo IAP | Generic sound library, no AI adaptation |
| L2 adjacent | Dark Noise (iOS) | $4.99/mo | Ambient noise, good, but not adaptive |
| L3 weak | Built-in iOS White Noise | Free | Basic, no AI |
| **Our wedge** | **AdaptNoise: AI adapts sound to your sleep cycle** | **$4.99/mo or $29.99/yr** | "Sound that gets quieter as you fall asleep — verified by accelerometer" |

Competition score: **2** — many apps, but none use device sensors + AI to adapt in real time.

---

## 3. PRD MVP

### P0 (must ship in 14 days)
- iOS app (SwiftUI, single-screen)
- Sound library: 20 high-quality loops (white/pink/brown, rain, fan, etc.)
- Sleep timer (auto-fade)
- **Wedge feature**: optional accelerometer-based "did I fall asleep?" detection → fade sound out 5 min after motion stops
- Subscription via StoreKit 2 (auto-renewable)
- Basic onboarding (5 screens)

### P1 (week 3-4)
- Apple Watch app (heart-rate based adaptation)
- Custom sound mixer (user blends)
- Sleep stats dashboard

### P2 (month 2+)
- Smart alarm (wake in light-sleep window)
- Android (only if iOS MRR > $2K)

### Non-goals
- ❌ No meditation content / guided sessions
- ❌ No social / sharing features
- ❌ No Android in v1 (iOS only)
- ❌ No Apple TV / iPad-first design (iPhone-first)
- ❌ No family sharing
- ❌ No dreams journal / smart alarm in v1

### Tech stack
- Swift + SwiftUI
- StoreKit 2 for subscriptions
- CoreMotion for accelerometer
- AVAudioEngine for sound playback
- Firebase Analytics + RevenueCat (subscription tracking)
- TestFlight for beta

### Cost
- Apple Developer account: $99/yr
- Audio assets: ~$200 one-time (Epidemic Sound or AudioJungle)
- Apple takes 15-30% cut
- No backend needed in v1 (all on-device)

---

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Xcode project, SwiftUI skeleton, audio engine POC |
| 2 | Sound library integration (20 loops), basic player UI |
| 3 | Sleep timer + auto-fade logic |
| 4 | CoreMotion integration, motion-detection algorithm |
| 5 | StoreKit 2 subscription integration, paywall UI |
| 6 | Onboarding flow (5 screens) |
| 7 | App icon, screenshots, ASO metadata |
| 8 | TestFlight beta (50 external testers) |
| 9 | Iterate on beta feedback, fix top 3 bugs |
| 10 | App Store submission (review ~24-48h) |
| 11 | App Store live; ASO keyword research + iteration |
| 12 | Reddit launch: r/iosapps, r/sleep, r/insomnia |
| 13 | X thread: "I built an adaptive sleep sound app" |
| 14 | First paying user; review funnel |

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Week | Channel | Action | Cost |
|---|---|---|---|
| 1 | Reddit | Lurk + contribute on r/sleep, r/insomnia, r/iosapps | $0 |
| 1 | ASO | Keyword research (AppFollow, Sensor Tower free tier) | $0 |
| 2 | Reddit | "I built this" launch post on r/iosapps | $0 |
| 2 | Indie Hackers | Build log post | $0 |
| 2 | Product Hunt | iOS app launch | $0 |
| 3 | Apple Search Ads | $100 trial (small budget, low CPT) | $100 |
| 3 | Reddit | "What I learned shipping an iOS app in 14 days" | $0 |
| 4 | Apple Search Ads | $100 more on best keywords | $100 |
| 4 | Referral | "Share with a friend who can't sleep, get 1 week free" | $0 |
| 4 | Influencer | Reach out to 3 sleep/ASO YouTubers | $0 |
| **Total** | | | **$200** |

Target Week 4: 200 paying users × $4.99 (after Apple cut, ~$3.74 net) = **$748 gross / $560 net MRR**.

---

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Price | $4.99/mo or $29.99/yr |
| Net ARPU (after Apple 15-30%) | $3.74/mo monthly, $2.08/mo annual |
| Blended ARPU | $2.80/mo |
| Gross margin | 95% (no backend, no AI cost in v1) |
| Target MRR (gross) | $10,000 |
| Required gross revenue | $10,000 → ~2,100 monthly subscribers |
| Monthly churn (consumer utility) | 12% |
| New subs/mo to hit steady state | ~280/mo (steady + growth) |
| Conversion (download → paid) | 2-3% |
| Downloads needed | ~12K/mo from organic + ASA |
| CAC (organic ASO) | ~$0.50-2 |
| CAC (ASA) | ~$3-7 |

**Path to $10K MRR: ~12-18 months.** App Store organic growth is slow; ASA is the lever.

---

## 7. Kill criteria

- Week 2: < 100 TestFlight signups → kill (no audience)
- Week 4: < 50 paid subs → kill or pivot vertical (focus? study?)
- Week 8: Day-7 retention < 20% → product fit issue, kill
- Week 12: ASA CPI > $7 unprofitable → reduce budget or kill

---

## Wedge (required for GO_NARROW)

### What we REFUSE to build (the wedge is what you don't ship)

- ❌ **No Android in v1.** iOS only. Apple Watch is the only allowed extension.
- ❌ **No meditation / breathing content.** Sleep sound utility. Calm/Headspace own that.
- ❌ **No smart alarm in v1.** That's Oura / Bedtime+ territory. We do sound + sleep timer only.
- ❌ **No family / shared plans.** Solo subscription only.
- ❌ **No social / dreams journal.** Privacy-first, on-device only.
- ❌ **No localization beyond English** in v1 (ship en-US, expand month 3+).
- ❌ **No iPad-first UI** (universal binary, but iPhone-optimized layout).

### What we WILL build (focused feature set)

- ✅ 20 hand-curated sound loops
- ✅ Sleep timer with auto-fade
- ✅ Motion-adaptive fade (accelerometer-based)
- ✅ StoreKit 2 subscription ($4.99/mo, $29.99/yr)
- ✅ 5-screen onboarding
- ✅ Apple Watch app (month 2+, if MRR > $2K)

### Why the wedge matters

Without the wedge, this becomes "another sleep app" and dies in the App Store. The wedge is: **AI + CoreMotion makes the sound ADAPT to your body, not just play on a timer.** That's a defensible technical claim, not a feature checkbox.
