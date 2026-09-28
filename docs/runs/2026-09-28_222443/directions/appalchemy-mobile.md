# Direction: AppAlchemy-Narrow — Idea-to-TestFlight for Non-Dev Small Biz

**Slug:** `appalchemy-mobile`
**Tier:** GO
**Run:** 2026-09-28_222443
**Target:** $10K MRR · 14d MVP · ≤$300/30d marketing

---

## 1. Why this direction

**TrustMRR evidence:**
- AppAlchemy: $58 MRR, $56 last30, 206 subs. Steady.
- Cluster: `mobile_utility` (5 listings, $89 ΣMRR) — quiet but consistent.
- Real revenue at this scale in "AI app builder" suggests buyers exist, despite Bubble/Glide existing.

**X/web evidence:**
- Persistent X/Reddit signal: small biz owners (bakery, salon, dog-walker, tutor) say *"I just need a simple app for my customers to book/see my menu/track loyalty, I tried Squarespace and it doesn't feel like an app"*
- Pain quote (synthesized): *"I have an app idea but I've been quoted $15K by an agency and I have no coding skills. Glide is too 'web-app', I want a real native-feeling iOS/Android."*

**Why the wedge works:**
Glide, Bubble, FlutterFlow serve "make a web app". They produce web wrappers. AppAlchemy and our wedge serve "make a real-feeling iOS/Android for $29/mo" with AI doing the design + native-shell generation. Small biz owners will pay.

## 2. Competitor table

| Tier | Name | What they do | Price | Threat |
|---|---|---|---|---|
| **L1 direct** | Glide | No-code app builder (web → web app) | $25-99/mo | Med — wrong output (web-feel) |
| **L1 direct** | FlutterFlow | No-code native (design-y, dev-y) | $30-70/mo | Med — too technical for non-devs |
| **L1 direct** | AppAlchemy (the listing) | AI app generator | ~$20-30/mo | Med — first-mover but generic |
| **L2 adjacent** | Squarespace / Wix app builder | Web → mobile wrapper | $16-40/mo | Low — wrappers, not native-feel |
| **L2 adjacent** | BuildFire | White-label app builder | $99-499/mo | Med — too expensive for solo biz |
| **L2 adjacent** | Appy Pie | DIY app maker | $18-60/mo | Med — UX dated |
| **L3 substitute** | Hire freelancer on Fiverr | $500-5,000 one-time | — | High (entry tier) |
| **L3 substitute** | Use Squarespace mobile site | $16/mo | — | High (entry tier) |

**Competition score: 2** — first-mover advantage is real but the category is heating up fast (Cursor + Lovable + v0 all can spit out app shells in 2026). Window is open but closing.

## 3. PRD MVP

### P0 (must-ship Day 14)
- Web app: describe business in 2 sentences (e.g., "Bakery in Austin. Need menu, hours, location, online pre-order for pickup")
- AI generates: 5-screen React Native + Expo project, with placeholder content + branding (logo upload)
- Output: Expo Go preview link (works on iOS/Android immediately, no app store)
- 1 free preview; subscription to export source code: $29/mo solo / $99/mo white-label (rebrand + custom domain + publish to stores via Expo EAS)

### P1 (week 3-4)
- App Store / Play Store direct-publish integration (Expo EAS submit)
- Templates: bakery, salon, tutor, dog-walker, fitness-studio (5 starting templates)
- Analytics dashboard (visits, bookings, screen-time)

### P2 (week 5+)
- Booking / loyalty / payment integrations (Stripe, Square, Calendly)
- Push notifications
- White-label reseller program ($299/mo for agencies)

### Non-goals
- ❌ Generic SaaS app builder
- ❌ Native Swift/Kotlin tooling
- ❌ Backend-as-a-service for engineers
- ❌ Marketplace / discovery

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | LLM prompt + template engine: business description → Expo project structure | Prompt + 1 template |
| 2 | Build pipeline: generate Expo project, run Expo Go preview | Demo works |
| 3 | Logo upload + basic theming (colors, fonts) | Branding works |
| 4 | 5 templates: bakery, salon, tutor, dog-walker, fitness-studio | Template picker works |
| 5 | Stripe + paywall: 1 free preview, then subscribe to export | Billing done |
| 6 | Export: generate downloadable Expo project (.zip) + Expo Go link | Export works |
| 7 | Landing page: 1 hero, 5 template previews, 1 CTA | Public URL |
| 8 | EAS Submit integration: push to App Store TestFlight | Direct publish works |
| 9 | Onboarding: 5-step wizard (describe → brand → template → preview → pay) | First-run UX |
| 10 | SEO + community seeding (r/smallbusiness, IndieHackers, FB small-biz groups) | 100 signups |
| 11 | Bug bash; test 10 templates end-to-end | Stable |
| 12 | Public launch: IndieHackers + X thread | Live |
| 13 | First 10 paying users; 3 testimonials | $290 MRR |
| 14 | Iterate AI quality; ship template #6 | Ready for marketing push |

## 5. 30-day marketing calendar (≤ $300)

| Day | Channel | Action | Budget |
|---|---|---|---|
| 1-5 | SEO | 5 posts: "app for my bakery", "no-code app for small business", "TestFlight without dev account", "Glide vs native-feel", "app builder for non-coders" | $0 |
| 7 | Reddit | r/smallbusiness, r/Entrepreneur, r/SaaS launch post | $0 |
| 8 | IndieHackers | "I built an AI that turns a sentence into an iOS app" | $0 |
| 10 | YouTube | Pitch 3 "small biz tech" channels for a video | $0 |
| 12 | Product Hunt | Submit | $0 |
| 14 | FB groups | 20 small-biz owner groups; offer 10 free templates | $0 |
| 18 | X | Demo thread: 30-sec screen recording of "I made an app for my fake bakery in 4 minutes" | $0 |
| 21 | Paid | **One** $100 Instagram ad to small-biz owners (interest: Square, Shopify POS) IF MRR > $300 by day 21 | $100 |
| 24 | Affiliate | 25% recurring for agencies that resell | $0 |
| 28 | SEO post #6 | "How to publish your first app to the App Store without code (2026)" | $0 |
| 30 | Referral | 1-month-free-for-1-referral loop | $0 |
| | | **Buffer** | $200 |
| | | **Total cap** | **$300** |

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| ARPU | $39/mo blended (heavy $29, some $99 white-label) |
| Gross margin | 90% (compute + Expo EAS submission, no per-user AI cost at scale) |
| Logo churn | 9%/mo (small biz churn hard; but $29 is low enough to not be a "decision") |
| Net new paid/mo for $10K | ~290 |
| Free → paid | 4% (consumer-grade, high intent) |
| Required free signups/mo | 7,250 |
| TOFU visitors/mo | 35,000 |
| CAC paid cap | $10 |
| Time to $10K MRR | 7-9 months |

**Trajectory:**
- Month 1: $300
- Month 2: $900
- Month 3: $2,000 (Product Hunt + community)
- Month 6: $5,500
- Month 9: $10,500 ✓

## 7. Kill criteria

| Signal | Threshold | Action |
|---|---|---|
| Day 14 paid users | <10 | Kill — no willingness to pay beyond novelty |
| Day 30 MRR | <$400 | Kill — too niche OR wrong wedge |
| Trial → paid after 300 trials | <3% | Kill — output quality not "native-feel" enough |
| Day 60 churn | >20%/mo | Kill — customers churning after novelty |
| Lovable / Cursor / v0 ships same feature | Public release | Pivot to "white-label for agencies" only |
| App Store rejection rate | >40% of submissions | Fix templates, not the funnel |

## 8. Wedge (N/A — this is GO)

Direction passes strict dual gate (demand 3, competition 2). The "non-dev small biz" ICP is already naturally narrow. No additional wedge required at MVP. May add wedge in month 4 if competition increases.

---

*Direction prepared by agent stage. Run: 2026-09-28_222443.*
