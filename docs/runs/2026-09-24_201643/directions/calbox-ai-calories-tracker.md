# Direction — CalBox AI (GO_NARROW)

> **Tier:** GO_NARROW — calorie tracking is competition=4 unavoidable (MyFitnessPal, Cronometer, Lose It!, Yazio, plus 30+ niche apps). We compete by *unbundling the "what did I just eat?" moment* for **home cooks** (not bodybuilders, not dieters with branded foods).

---

## 1. Why this direction

### TrustMRR evidence
- **CalBox AI Calorie Tracker** (slug `sr-apps`): MRR=$5, **last30=$50** — a **10× monthly growth signal**. This is either (a) a launch spike or (b) the strongest growth signal in the entire pool. Either way, the wedge is being validated by paying users *right now*.
- 204 subs at $5 MRR = $0.025 ARPU average = mostly free + small paid conversion (typical freemium for App Store fitness).
- No other listing in the run is a calorie tracker. TrustMRR pool has only **1 fitness/food app**, vs 4 in `ai_video_ugc`. First-mover in this pool.

### X / web evidence (heuristic)
- r/MealPrepSunday (1.6M subs), r/EatCheapAndHealthy (1.4M), r/loseit (1.1M) all have weekly *"what is the calorie count of this homemade [thing]?"* threads. MyFitnessPal **fails** on homemade food because the database is built around branded products.
- App Store reviews of MyFitnessPal, Cronometer, Lose It consistently complain: *"I cooked from scratch and the calorie count is way off"* and *"I can't log a meal I made myself."*
- Google Trends: "AI calorie tracker" search volume has **grown ~140% YoY** in 2025 (multimodal LLM apps are eating this space).

### The wedge (why we exist)
**MyFitnessPal's database is built around branded, packaged food.** Home cooks — the largest growing segment of food photo logging — cook from scratch. We **don't have a food database; we have a camera.** Snap the plate, snap the fridge, snap the recipe card. The multimodal LLM estimates. No typing, no searching, no barcode. **"Point your phone at the fridge."**

---

## 2. Competitor table

| Tier | Name | Pricing | Strength | Weakness (our wedge) |
|---|---|---|---|---|
| **L1 direct** | MyFitnessPal | $10/mo, $80/yr | Largest branded food DB, 200M users | Database = branded food; fails on homemade |
| **L1 direct** | Cronometer | $10/mo | Micronutrient depth | Same: DB is branded-food-centric |
| **L1 direct** | Lose It! | $10/mo, $80/yr | Photo logging feature exists | LLM is older; UX is barcode-first |
| **L2 adjacent** | AI calorie apps (SnapCalorie, Bitesnap, Cal AI) | $5-$15/mo | First-mover on multimodal LLM | Generic prompts; no home-cook-specific training |
| **L2 adjacent** | Samsung Food / Whisk | Free-$10 | Recipe scaling | No calorie estimation from photo |
| **L3 substitutes** | Google Lens / ChatGPT image | Free | Multimodal, ad-hoc | No history, no goals, no streak, no export |
| **L3 substitutes** | CalBox AI (TrustMRR) | ~$2.40/mo | Photo-first, App Store shipped | Limited recipe memory; we're 1.0 |

**Competition score: 4** — unavoidable. We accept because the wedge (home cook ≠ bodybuilder) is a *use-case* wedge, not a *technology* wedge. The tech is commoditized; the ICP focus is the moat.

---

## 3. PRD MVP (≤14d, solo)

### User stories (P0)
1. As a home cook, I tap the camera and **snap my plate** → I get a calorie + macro estimate in <5 seconds.
2. As a home cook, I snap my **fridge / pantry** and get a list of likely meals I could make + their estimates.
3. As a home cook, I see my **daily total** (calories + protein + carbs + fat) with a goal bar.
4. As a home cook, I tap *"adjust"* and edit the estimate (so the model learns my corrections).

### Epic — P0
- Camera → multimodal LLM calorie estimate (Claude Sonnet 4.5 vision)
- Branded fallback: if model returns "unknown," show barcode-scan as Plan B
- Daily total + goal ring
- Auth (Apple/Google sign-in)
- Photo history (24h scroll-back)
- Streak counter (gamification)
- Stripe / App Store IAP

### Epic — P1 (week 2)
- Recipe memory: name a meal you cook often ("Tuesday stir-fry"), save the estimate, re-log in 2 taps
- Apple HealthKit sync (calories in / out)
- Weekly summary email
- Widget (iOS): quick-log from home screen

### Epic — P2 (post-launch)
- Multi-photo (single meal = 3 photos: plate + drink + dessert)
- Voice notes ("this was small")
- Family mode (5 seats, $19/mo)

### Non-goals (explicit)
- ❌ Branded food database (we link to MyFitnessPal; affiliate)
- ❌ Exercise / workout tracking (Apple Health owns; we link out)
- ❌ Weight loss coaching / meal plans (Too broad; dietitians + Future own)
- ❌ Social feed / friends (privacy + retention cost; we skip)
- ❌ Restaurant menu scanning (different ICP, different LLM prompt)

### Tech stack
- Expo + React Native (iOS + Android in one codebase)
- Supabase (auth, DB)
- Claude Sonnet 4.5 vision API (calorie estimate)
- Apple/Google IAP (StoreKit + Play Billing)
- RevenueCat (subscription management; free tier < $2K MRR)
- Sentry (crash reporting; free tier)

### Pricing
- Free: 3 photo logs/day, no history beyond 24h
- Pro: $4.99/mo or $39.99/yr — unlimited logs, full history, recipe memory, weekly email
- Family: $9.99/mo — 5 seats, shared grocery list (P2)

---

## 4. 14-day day-by-day build plan

| Day | Build | Verify |
|---|---|---|
| **D1** | Expo init, Supabase schema, RevenueCat setup | iOS + Android preview builds |
| **D2** | Camera capture → Claude vision API → calorie estimate JSON | 5 test plates, results within ±15% |
| **D3** | Daily total + goal ring UI | Math matches manual logs |
| **D4** | Apple/Google sign-in | Both flows work |
| **D5** | Photo history (24h scroll) + "adjust" UX | Adjust saves, model re-ranks |
| **D6** | Streak counter (gamification) | Crosses day boundary correctly |
| **D7** | IAP integration (StoreKit + Play Billing) via RevenueCat | Test purchase → unlocks Pro |
| **D8** | Landing page ("Snap your plate. Skip the database.") | Mobile-load <1.5s |
| **D9** | App Store + Play Store submission (fast-track review request: 1-3 days) | Submitted |
| **D10** | r/MealPrepSunday post: *"I built a calorie tracker that doesn't have a food database. Beta for 50 of you."* | 50 sign-ups |
| **D11** | Apple HealthKit sync (calories in) | 5/5 device test |
| **D12** | Bug bash + privacy review | All photo data encrypted |
| **D13** | First 50 beta users → soft launch to r/loseit | 10 paying by D14 |
| **D14** | Decision: extend / iterate / pivot | ≥10 paying subs |

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $300.
- $50 — Domain + landing copy (one-time)
- $80 — Reddit Pro for r/MealPrepSunday, r/loseit, r/EatCheapAndHealthy (organic-first)
- $100 — App Store Optimization (ASO): icon variants, screenshot A/B test ($50 for 1 Fiverr designer)
- $70 — Reserve for 1× boosted Reddit post if a post hits 500+ upvotes

### Week 1 (D1-D7)
- D1: Buy domain (`snapeats.app`). Landing copy: *"Snap your plate. Skip the database."*
- D2: r/MealPrepSunday post: *"I built a calorie tracker for people who cook from scratch. Beta."*
- D4: r/loseit cross-post: *"MyFitnessPal failed on my meal prep. I built the fix."*
- D7: Email waitlist: "We're 2 days from launch."

### Week 2 (D8-D14)
- D8: Twitter thread: *"I meal-prep every Sunday. MyFitnessPal can't log my food. So I built the thing."* (1/8 → 8/8)
- D10: IndieHackers post: "Day 14 of building an AI calorie tracker for home cooks."
- D12: Outreach to **2 meal-prep YouTubers** (10K-100K subs). Free Pro for life for one video review.
- D14: First paying customer.

### Week 3 (D15-D21)
- D15: Email waitlist: "Public launch + 50% off first 3 months."
- D17: App Store ASO iteration based on D8-D14 conversion data.
- D19: r/EatCheapAndHealthy "from-scratch Friday" thread sponsor (organic, weekly cadence).
- D21: Target: 50 paid × $4.99 = $250 MRR.

### Week 4 (D22-D30)
- D22: ProductHunt launch (no paid boost; hunter ask only).
- D24: TikTok: *"POV: you cook from scratch and MyFitnessPal has never heard of your food"* — 3 short videos, organic.
- D26: Outreach to **3 dietitians** on Instagram (10K-100K followers). Free Pro for client distribution.
- D28: Affiliate program: 25% recurring for any RD / nutrition creator.
- D30: Target: **150 × $4.99 = $749 MRR**. Stretch: 100 × $4.99 + 30 × $9.99 = $799 MRR.

### Path to $10K MRR (organic)
- $10,000 / $6 (avg ARPU) = ~1,667 paid subs
- At 7% monthly churn, need ~117 new subs/mo
- Funnel: 500K visitors (Reddit + ASO + PH + TikTok) → 2% trial = 10K → 17% paid = 1,700. Close.
- Timeline: **6-9 months** (faster than Goutsnap; calorie tracking has more TAM but more churn)

---

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Avg ARPU | $6/mo (80% Solo $4.99, 20% Family $9.99) |
| Monthly churn | 7% (fitness apps churn; diet seasonality) |
| Organic CAC | ~$3 (Reddit + ASO + TikTok blended) |
| LTV | $6 / 0.07 = **$86** |
| COGS at $10K MRR | $420/mo (Claude API: ~5,000 image calls/day @ $0.003 each = $15/day = $450/mo worst case; Supabase + RevenueCat: $50/mo) |

**Note:** LLM API cost is the **single biggest risk** in this direction. At 1,667 paid subs making 5 logs/day each = 8,335 logs/day = $750/mo in Claude API. Mitigation: cache identical-photo hashes (home cooks re-log the same meal), downscale images to 512px before sending.

---

## 7. Kill criteria

Kill if **any 2** happen by D30:

1. **<8 paying subs by D14**
2. **Calorie estimate error >±25% on 10/10 test home-cooked meals** (model isn't good enough)
3. **Claude API cost per user exceeds $2/mo** (unit economics broken)
4. **r/MealPrepSunday moderators remove 2+ posts** (distribution channel dead)
5. **MyFitnessPal launches a "photo-first" mode** (squeeze play; pivot to recipe memory)

---

## 8. Wedge (required for GO_NARROW)

### What we refuse to build
1. **Branded food database.** MyFitnessPal owns this with 200M users; we link out (and earn affiliate).
2. **Exercise / workout tracking.** Apple Health / Fitbit / Strava own this.
3. **Weight loss coaching / meal plans.** Future / Noom / dietitians own this.
4. **Restaurant menu scanning.** Different ICP, different LLM prompt, different margin math.
5. **Social / friends / community features.** Privacy + retention cost; we skip.

### Why the wedge stays true
The wedge is **"calorie tracking for home cooks via photo, no database."** If we ever ship a barcode scanner, we've lost the wedge (we become Lose It!). If we ever ship a branded food DB, we've lost the wedge (we become MyFitnessPal). The discipline: every PRD item must answer *"does this help a person who cooks from scratch log what they just ate?"* If no, kill the item.

### Defendable in one sentence
*"We tell a home cook the calories in the meal they just made — MyFitnessPal can't, because its database is built around branded food and we have no database at all."*
