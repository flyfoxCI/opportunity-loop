---
layout: post
title: "Direction: SwapIt-like — Habit Swap Tracker w/ Smart Alternatives"
date: 2026-09-28T22:24:43+00:00
week: "2026-09-28_222443"
week_date: "2026-09-28T22:24:43+00:00"
slug: "swapit-build"
permalink: /directions/swapit-build.html
tags:
  - "AI"
  - "mobile"
  - "vertical"
excerpt: "Habit/craving swap tracker with smart alternatives (smoking, sugar, doom-scrolling)"
---

**Slug:** `swapit-build`
**Tier:** GO
**Run:** 2026-09-28_222443
**Target:** $10K MRR · 14d MVP · ≤$300/30d marketing

---

## 1. Why this direction

**TrustMRR evidence:**
- SwapIt: $11 MRR, $13 last30, 128 subs. Tiny but last30 > MRR (early growth).
- Cluster: "other" (22 listings, $459 ΣMRR) — uncategorized long tail. SwapIt stands out as the only one specifically a *behavioral swap* tool.
- Despite 128 subs at $11 MRR, the niche is structurally underserved.

**X/web evidence:**
- r/stopsmoking, r/loseit, r/nosurf, r/decidingtobebetter, r/getdisciplined all have a recurring question: *"What can I do INSTEAD of [habit] when I get the urge?"*
- Pain quote (synthesized): *"Habit trackers tell me I failed when I smoked. I need a list of things I can actually DO when the craving hits."*
- Existing apps: generic habit trackers (Streaks, Habitica), quitting apps (QuitNow, Smoke Free) — none focus on the **swap itself** as the unit of behavior change.

**Why the wedge works:**
"Stop X" is the framing of every quitting app. People fail because they have no replacement behavior. We focus on the **swap** (X → Y), with curated, ranked alternatives per craving trigger.

## 2. Competitor table

| Tier | Name | What they do | Price | Threat |
|---|---|---|---|---|
| **L1 direct** | SwapIt (the listing) | Swap-based craving tracker | $5-9/mo? | Med — first-mover, small |
| **L1 direct** | I Am Sober | Quit counter + community | Free + IAP | Med — strong community, wrong shape |
| **L2 adjacent** | Streaks / Habitica | Generic habit tracker | $5/mo or free | Med — not swap-focused |
| **L2 adjacent** | Smoke Free / QuitNow | Smoking-specific | Free + IAP | Med — vertical but narrow |
| **L3 substitute** | Reddit r/stopsmoking + willpower | $0 | — | **High** — community is the real enemy |
| **L3 substitute** | Notes app + manual list | $0 | — | High on entry tier |

**Competition score: 2** — no dominant SaaS in the "swap" framing. I Am Sober is the closest but is a counter/community, not a behavior-design tool. Window open.

## 3. PRD MVP

### P0 (must-ship Day 14)
- iOS-first (App Store, then Android in week 3)
- Sign-up: pick what you're swapping (smoking / doom-scrolling / sugar / doom-spending / late-snacking / nail-biting — 6 starter swaps)
- Each swap: curated list of 8-10 alternatives (e.g., smoking → drink water / pushups / chew gum / call friend / 4-7-8 breath / go for a walk / etc.)
- Tap alternative when craving hits → starts a 2-min timer / activity prompt / mini-game
- Streak counter, swap-by-swap stats
- IAP: $4.99/mo Pro (unlimited swaps, deeper analytics, custom swaps)

### P1 (week 3-4)
- Android
- Smart suggestions (after 7 days of use, ML ranking: which alternative you actually use)
- Community board (anonymized) — "people who swapped smoking also liked X"
- Wearable (Apple Health hook for activity alternatives)

### P2 (week 5+)
- Coach tier: $19/mo — human check-ins + AI-generated swap library
- B2B: employers buy seat licenses for wellness programs

### Non-goals
- ❌ Generic habit tracker
- ❌ Therapy / mental-health treatment (medical-grade)
- ❌ Nutrition / fitness coaching
- ❌ Social-network-first design

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | iOS app shell (React Native or SwiftUI), 6 starter swaps seeded | App runs |
| 2 | Swap picker UX; alternative list UX | Core flow works |
| 3 | "Tap to swap" action: 2-min timer + activity prompt + completion | Swap logged |
| 4 | Streak counter + swap-by-swap stats | Stats screen |
| 5 | IAP wiring ($4.99/mo Pro) | Paywall works |
| 6 | Landing page (web): 1 hero, 3 swaps demoed, 1 CTA | Public URL |
| 7 | App Store submission (TestFlight first) | Beta ready |
| 8 | r/stopsmoking, r/loseit, r/nosurf research: top pain threads | Content plan |
| 9 | Content: 3 short-form videos for TikTok/Reels (relatable: "the craving hit, here's what I did instead") | 3 videos shot |
| 10 | Submit App Store review (day 7 already in review usually) | Submitted |
| 11 | Launch day on r/stopsmoking (genuine post, not promo) | 5k views |
| 12 | IndieHackers launch post + X thread | Live |
| 13 | First 50 Pro conversions; 3 testimonials | $250 MRR |
| 14 | Android build starts; iterate alternative library | Ready for marketing push |

## 5. 30-day marketing calendar (≤ $300)

| Day | Channel | Action | Budget |
|---|---|---|---|
| 1-5 | Reddit | Authentic participation in r/stopsmoking, r/loseit, r/nosurf, r/decidingtobebetter; no promotion | $0 |
| 7 | Reddit | r/stopsmoking: "I made an app for the 4am craving. Here's what's in my swap list." (genuine, demo in comments) | $0 |
| 8 | TikTok / Reels | Post 3 short-form videos | $0 |
| 10 | IndieHackers | Launch post (story-driven, not promotional) | $0 |
| 12 | Product Hunt | Submit | $0 |
| 14 | Reddit | Cross-post r/loseit + r/nosurf (adapted) | $0 |
| 18 | TikTok | 5 more videos: "I tried 10 swaps for late-night snacking — here's the only one that worked" | $0 |
| 21 | Paid | **One** $100 TikTok ad IF organic views > 50k by day 21 | $100 |
| 24 | Partnership | Free Pro to 5 quit-coaches / wellness influencers | $0 |
| 28 | SEO | "Best app to quit smoking 2026", "what to do instead of late-night snacking" | $0 |
| 30 | Referral | 1-month-free-for-1-referral loop | $0 |
| | | **Buffer** | $200 |
| | | **Total cap** | **$300** |

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| ARPU | $5/mo blended (mostly IAP, some $19 coach tier in month 6+) |
| Gross margin | 95% (no AI cost, App Store 30% take on first year, 15% after) |
| Logo churn | 12%/mo (consumer apps churn hard; but habit apps retain via streak-loss-aversion) |
| Net new paid/mo for $10K | ~2,400 |
| Free → paid | 4% (consumer IAP conversion avg) |
| Required downloads/mo | 60,000 |
| TOFU visitors/mo | 200,000 (TikTok + Reddit + App Store search) |
| CAC paid cap | $2 |
| Time to $10K MRR | 8-10 months |

**Trajectory:**
- Month 1: $300 (App Store organic + 1 Reddit thread)
- Month 2: $800 (TikTok compounding)
- Month 3: $2,000 (Product Hunt + content loop)
- Month 6: $5,500
- Month 10: $10,500 ✓

## 7. Kill criteria

| Signal | Threshold | Action |
|---|---|---|
| Day 14 Pro IAPs | <30 | Kill — no willingness to pay |
| Day 30 MRR | <$200 | Kill — viral ceiling too low |
| Day 30 D7 retention | <15% | Kill — habit loop broken |
| App Store rejection | 2+ times | Pivot web-first |
| 70%+ of churn surveys say "I just used the free version" | — | Kill free tier; pivot to hard paywall |
| QuitGenius / Pelago launches swap framing | — | Pivot to "swap library content" (sell to those apps) |

## 8. Wedge (N/A — this is GO)

Direction passes strict dual gate (demand 3, competition 2). The "swap" framing is already the wedge. No further narrowing needed at MVP.

---

*Direction prepared by agent stage. Run: 2026-09-28_222443.*
