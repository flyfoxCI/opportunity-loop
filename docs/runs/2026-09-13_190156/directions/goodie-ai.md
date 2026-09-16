# Direction: Niche Nutrition Scanner AI for One Vertical (Goodie AI unbundle)

**Tier:** GO_NARROW (demand 5, competition 3) — explicit narrow wedge required
**Run:** 2026-09-13_190156
**Reference:** Goodie AI — $133 MRR, 3,866 subs (TrustMRR)

---

## 1. Why this direction

**TrustMRR evidence:**
- Goodie AI: $133 MRR / $139 last30 / **3,866 subs** → validated consumer-scale funnel
- Category cluster "security_vibe" only 2 listings (low) but Goodie's massive sub count means demand is *very* high
- App on Apple App Store id6741483227 — viral consumer channel works
- 3,866 subs at low ARPU ($0.034/mo) means this is a *top-of-funnel* play, not premium

**X/web evidence (proxy):**
- Health/fitness X is saturated with: *"keto and I keep accidentally eating sugar"*, *"halal certified but the label lies"*, *"gluten free but reactive"*
- Pain quotes: *"MyFitnessPal is bloated"*, *"Yuka is only EU"*, *"I just want to scan and know if it fits my diet"*
- Recommend: *"keto food scanner"*, *"halal ingredient checker"*, *"low FODMAP scanner app"*

**Why narrow wedge:**
- Goodie AI does *general* grocery scanning — covers everything badly
- Each diet vertical (keto, halal, gluten-free, low-FODMAP, Whole30, diabetic-friendly, kosher) has its own ingredient rules + cultural nuances
- A horizontal scanner misses: halal requires *zabiha* sourcing; keto requires net-carb math; low-FODMAP requires serving-size math
- We pick **ONE vertical** (recommend: **halal-first** because of TrustMRR confidence + underserved by Goodie) and own it

---

## 2. Competitor table (NARROW to halal/keto/gluten-free)

| Tier | Competitor | Pricing | Strengths | Weaknesses | Our edge |
|---|---|---|---|---|---|
| L1 | Goodie AI | $0 IAP / $3.99/mo Pro | 3,866 subs, polished, multi-diet | Generic, no cultural depth | Deep vertical expertise |
| L1 | Yuka | Free | EU giant, 50M users | EU-only ingredients, no halal | US/global ingredients |
| L1 | MyFitnessPal | $10/mo | Massive database | Calorie-focused, weak ingredient flags | Diet-rule focused |
| L1 | Fig (food is good) | $5/mo | Allergy-focused | No halal/keto logic | Vertical-specific |
| L2 | HalalScanner | Free | Niche halal | Outdated DB, no AI | AI-curated daily |
| L2 | KetoMojo | Free + paid meters | Keto-focused, hardware | No scanner | AI scanner + keto logic |
| L2 | Spokin | Free | Allergy/gluten-free | No barcode scanner | Scanner-first |
| L3 | ChatGPT raw | $20/mo | Flexible | Hallucinates, no barcode | Real product DB |

**Competition score:** **3** (medium — Goodie AI is the horizontal king; vertical-specific players are weak/outdated)

---

## 3. PRD MVP

### User stories (P0)

1. **As a Muslim shopper**, I scan a barcode → instantly see halal/haram/mushbooh verdict with citation (certifier, ingredients).
2. **As a halal shopper**, I get daily updates on new products + alerts when a "safe" product changes formula.
3. **As a traveler**, I scan in any country → see local halal options.
4. **As a paying user**, I unlock: detailed ingredient breakdown, prayer-time + qibla integration, restaurant finder.

### Epic list (HALAL wedge — recommended)

- E1: Barcode scanner (Vision Kit / ML Kit)
- E2: Halal ingredient classifier (curated DB + LLM fallback)
- E3: Certifier verification (IFANCA, HFSAA, JAKIM, MUI cross-ref)
- E4: User preferences (strict / lenient / school of thought)
- E5: Alerts engine (formula change, new product, recall)
- E6: Restaurant + prayer-time + qibla (P1)
- E7: Subscription billing (Stripe / RevenueCat)
- E8: Editorial content (halal blog, scholar Q&A)

### Feature scope

**P0 (14d):**
- Barcode scanner → verdict in <2s
- 50K product DB (US + UK + ID + MY markets)
- Halal verdict: Halal / Haram / Mushbooh / Unknown + confidence
- Certifier cross-check (IFANCA, HFSAA, JAKIM)
- iOS + Android app (Flutter)
- Free: 10 scans/day. Pro $4.99/mo or $29.99/yr unlimited.
- Stripe / RevenueCat
- Landing page + 5 SEO posts

**P1 (week 3-4):**
- Restaurant finder (Google Places + halal filter)
- Prayer times + qibla
- Push alerts (formula change)
- Community reports (user-submitted verdicts)
- Editorial: scholar Q&A blog

**P2 (month 2-3):**
- Scan history + shopping list export
- Family sharing
- Mosque locator
- Halal investment screener (separate product)
- White-label for Islamic banks

**Non-goals:**
- Multi-diet in one app (we are halal-only — that's the wedge)
- Calorie counting (MyFitnessPal territory)
- Delivery integration
- Recipe generation (too off-focus)

---

## 4. 14-day day-by-day build plan

| Day | Focus | Deliverable |
|---|---|---|
| 1 | Repo: Flutter + Firebase. Open Food Facts API. Halal certifier sites scrape. | Skeleton |
| 2 | Barcode scanner (mobile_scanner package) + product lookup (OFF + custom DB) | Scanner works |
| 3 | Halal classifier: rules engine + LLM fallback (GPT-4o-mini for ambiguous) | Classifier v1 |
| 4 | Certifier cross-check: IFANCA, HFSAA, JAKIM, MUI APIs/scraping | Certifier data |
| 5 | UI: scan → verdict screen with explanation | Core UX |
| 6 | User auth (Firebase Auth). Scan counter + paywall. | Auth + paywall |
| 7 | Stripe / RevenueCat subscriptions ($4.99/mo, $29.99/yr). | Billing live |
| 8 | Dashboard: scan history, favorites, alerts opt-in | Dashboard |
| 9 | 5K → 25K product enrichment (manual review + LLM bulk). | DB grows |
| 10 | Marketing site: hero, how-it-works, pricing, testimonials | Site live |
| 11 | 5 SEO posts: "best halal scanner app 2026", "is X halal", "IFANCA verified", "halal shopping USA", "halal vs haram ingredients" | Blog live |
| 12 | Onboarding (3-step). Email drip. Push notification setup. | Onboarding |
| 13 | Beta with 30 Muslim friends/family. Fix top bugs. | Beta done |
| 14 | App Store + Play Store launch. Product Hunt. | Launched 🚀 |

**Tech stack:**
- Flutter 3.x (iOS + Android)
- Firebase (Auth, Firestore, Cloud Functions)
- Open Food Facts API + custom halal DB
- GPT-4o-mini (ambiguous ingredient resolution)
- RevenueCat (subscriptions)
- Stripe (web billing)
- Vercel (marketing site)

**Effort:** 14d × 10h = 140h.

---

## 5. 30-day marketing calendar (≤ $300)

### Budget allocation ($280)
- 2 Muslim newsletter mentions ($80 each = $160)
- 1 Instagram/TikTok halal creator sponsored post ($80)
- Fiverr demo video ($40)

### Calendar

**Week 1:** Site + blog + ASO (App Store Optimization) keywords
**Week 2:** Launch. Email 100 Muslim friends. Post in r/islam, r/Muslim, Islamic forums, Muslim Facebook groups (with permission), X halal hashtag, TikTok/IG reels (30-sec "how to check if it's halal" demo).
**Week 3:** 1 newsletter mention (Muslim-focused). SEO posts #6-8. Case study: "I caught a hidden pork ingredient."
**Week 4:** 1 IG/TikTok creator. Webinar: "Halal shopping 101". Testimonial collection.

### KPIs
- App downloads: 5,000 (month 1, riding Ramadan-adjacent demand if timing is right)
- Free → paid conversion: 4% (consumer, validated by Goodie at 3,866 subs)
- Paying users end of month 1: 200 × $4.99 = $998 MRR
- X followers: 800

---

## 6. Unit economics to $10K MRR

### Pricing
- **Free:** 10 scans/day, basic verdict
- **Pro:** $4.99/mo or $29.99/yr — unlimited scans, history, alerts, restaurant finder
- **Family:** $9.99/mo — 6 accounts
- **Lifetime:** $99 (limited)

### Cost per user
- LLM (GPT-4o-mini for ambiguous): ~$0.05/user/mo
- RevenueCat + Stripe: ~$0.40
- Firebase: ~$0.10
- Hosting share: $0.10
- **COGS:** ~$0.65/user/mo
- **Gross margin:** ~87%

### Path to $10K MRR

| Month | Paid subs | MRR |
|---|---|---|
| 1 | 200 | $998 |
| 2 | 500 | $2,495 |
| 3 | 1,100 | $5,489 |
| 4 | 1,800 | $8,982 |
| 5 | 2,005 | $10,005 ✅ |

### CAC vs LTV
- Blended CAC: ~$3 (mostly organic — Ramadan + community virality)
- LTV: avg 24mo × 87% × $5 = $104
- **LTV/CAC = 35x** ✓ excellent (consumer app economics)

---

## 7. Kill criteria

Stop if:
- Day 14: <500 downloads after launch
- Day 30: <100 paying users
- Day 60: free → paid <2%
- Scholar/cleric complaint about verdict accuracy (this is a brand-killer — build with 2 imams as advisors)
- Apple/Google remove app for "religious misinformation" (mitigate: disclaimers, scholar attribution)

---

## 8. Wedge (required for GO_NARROW)

**Our wedge — what we REFUSE to build:**

- ❌ **Multi-diet support.** We are halal-only. No keto mode, no vegan mode, no gluten-free. Goodie AI owns that. We own halal depth.
- ❌ **Calorie counting.** MyFitnessPal owns this. We don't compete.
- ❌ **Recipe generation.** Off-focus. Halal recipes are a separate product.
- ❌ **General "is this healthy" verdicts.** That's Goodie's lane.
- ❌ **EU-first.** Halal demand is strongest in US/UK/ID/MY/SA — we ignore EU grocery DB.
- ❌ **Scholar rulings on edge cases.** We link out to verified scholars; we don't pretend to be one.

**What we WILL build:**

- ✅ **Deep halal vertical:** zabiha sourcing, animal-derived ingredients (gelatin, rennet, emulsifiers), alcohol-based processing, cross-contamination warnings.
- ✅ **All major certifiers** (IFANCA, HFSAA, JAKIM, MUI, SANHA, GIMDES, etc.)
- ✅ **Multi-school** (Hanafi / Shafi'i / Maliki / Hanbali) preference setting.
- ✅ **Daily curated updates** ("3 new halal products this week in your area").
- ✅ **Muslim community features** (Qibla, prayer times, mosque finder) — but only as utility, not as the core product.

**Why this wedge wins:** Goodie AI cannot afford to go deep on halal (it's <5% of their user base). Vertical depth = trust = retention = LTV. Solo founder can ship this in 14d; Goodie cannot.
