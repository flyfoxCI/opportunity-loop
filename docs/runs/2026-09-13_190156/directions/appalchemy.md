# Direction: AI App-from-Prompt Generator (`appalchemy` clone)

**Tier:** GO (pure — demand 3, competition 2)
**Run:** 2026-09-13_190156
**Reference:** AppAlchemy — $62 MRR, 219 subs (TrustMRR)

---

## 1. Why this direction

**TrustMRR evidence:**
- AppAlchemy: $62 MRR / $60 last30 / 219 subs → mid-tier indie revenue
- Cluster "mobile_utility" only 3 listings, low competition
- Founder @diegoroshardt active on X — solo indie in vibe-coding niche
- Category validated by adjacent "vibe coding" plays (Cursor, Bolt, Lovable) raising massive rounds, but their MRR is unproven — gap exists for "ship a real app to App Store in one click"

**X/web evidence (proxy):**
- X is saturated with "I built an app in a weekend" threads (Lovable, Bolt.new, v0 + Expo)
- Pain quotes: *"v0 looks great but I can't ship to App Store"*, *"Cursor + Expo is great but App Store rejection is a nightmare"*, *"I just want to paste my prompt and get an .ipa"*
- Recommend: *"how to ship Expo app to App Store"*, *"AI mobile app builder"*, *"no-code app store publish"*

**Why selectable:**
- 1-click publish from prompt → App Store + Play Store = niche no one owns
- Lovable/Bolt/v0 all generate *web apps*, not *native mobile apps* with real store presence
- Painful manual steps: Expo EAS → certificates → provisioning → screenshots → metadata → submit
- We automate ALL of this

**Wedge we own:** *Prompt → live native iOS + Android app on store in 7 days, no developer account needed (we manage via our org).*

---

## 2. Competitor table

| Tier | Competitor | Pricing | Strengths | Weaknesses | Our edge |
|---|---|---|---|---|---|
| L1 | Lovable.dev | $25/mo | Polished web app generation | Web only, no native app | Native mobile + store publish |
| L1 | Bolt.new | $25/mo | Full-stack web apps | Web only | Native mobile |
| L1 | v0.dev (Vercel) | $20/mo | React/Next component generation | No full app, no native | Full app + publish |
| L2 | Replit Agent | $25/mo | Full-stack + deploy | Mobile support weak | Native mobile focus |
| L2 | Cursor | $20/mo | Best IDE for AI coding | Requires dev skills | No-code for non-devs |
| L2 | FlutterFlow | $30/mo | Native mobile, no-code | Steep learning, no AI prompt | AI-prompt-first |
| L2 | Expo + EAS | Free + $99/mo | Real native, real stores | Massive dev effort | We automate everything |
| L3 | ChatGPT + Expo tutorial | Free | Cheap | Hours of work, App Store rejection | One-click |

**Competition score:** **2** (low — no one has "prompt → live native app on store" pipeline)

---

## 3. PRD MVP

### User stories (P0)

1. **As a non-technical founder**, I describe my app idea → get a working Expo/React Native app I can preview on my phone.
2. **As a founder**, I want the app live on App Store + Play Store without learning certificates, provisioning, or metadata.
3. **As a founder**, I want to update my app (change content, fix bug) by chatting with the AI.
4. **As a paying user**, I get a real, installable app URL + App Store link in 7 days.

### Epic list

- E1: Prompt → Expo app spec (JSON: screens, navigation, components, data)
- E2: Spec → React Native + Expo Router code
- E3: Preview build (Expo Go URL)
- E4: EAS Build integration (iOS .ipa + Android .apk)
- E5: App Store Connect + Play Console submission (we manage org account)
- E6: App metadata generator (title, description, screenshots via AI)
- E7: User billing + dashboard
- E8: Update flow (chat → new version → resubmit)

### Feature scope

**P0 (14d):**
- Prompt → Expo preview URL (Expo Go)
- 5 starter templates (todo, habit tracker, photo journal, simple social, calculator)
- Stripe billing: $49/mo Starter (1 app), $99/mo Pro (3 apps), $299/mo Agency (10 apps)
- Dashboard: my apps, build status, update
- Marketing site + blog

**P1 (week 3-4):**
- App Store + Play Store submission (we manage org Apple/Google dev account)
- App icon + splash generator (AI)
- Push notification setup
- In-app purchase scaffolding

**P2 (month 2-3):**
- Custom backend (Supabase per user)
- Auth (email + OAuth)
- Analytics (PostHog)
- A/B test framework
- RevenueCat integration for subscriptions

**Non-goals:**
- Web apps (Lovable/Bolt/v0 territory)
- Complex games
- AR/VR apps
- Heavy ML on-device
- HIPAA / SOC2 compliance (skip for indie launch)

---

## 4. 14-day day-by-day build plan

| Day | Focus | Deliverable |
|---|---|---|
| 1 | Repo: Next.js + Expo monorepo. OpenAI + Anthropic keys. Stripe + Expo accounts. | Skeleton |
| 2 | Prompt parser: GPT-4o takes "build me a habit tracker" → Expo app spec JSON | Spec engine |
| 3 | Code generator: spec → React Native + Expo Router files (templates for 5 app types) | Code gen works |
| 4 | EAS Build pipeline: spec → EAS cloud build → .ipa + .apk artifacts | Build pipeline |
| 5 | Preview URL generator (Expo Go) | Live preview |
| 6 | Dashboard: list apps, view builds, edit spec | Dashboard |
| 7 | Stripe Checkout + subscription tiers + customer portal | Billing live |
| 8 | Update flow: chat "add dark mode" → new build | Update flow |
| 9 | Template #1-2 polish (todo, habit tracker). Marketing site. | Templates + site |
| 10 | Templates #3-5. Landing page copy + pricing. | All templates |
| 11 | 3 SEO blog posts: "How to build an iOS app without coding", "AI app builder 2026", "Lovable vs Bolt vs us" | Blog live |
| 12 | Onboarding flow (5-step wizard). Email drip. | Onboarding live |
| 13 | Beta with 5 non-technical founders. Fix bugs. | Beta tested |
| 14 | Product Hunt + Show HN + IndieHackers launch | Launched 🚀 |

**Tech stack:**
- Next.js 14 (dashboard + marketing)
- Expo SDK 53 + React Native + Expo Router
- EAS Build (cloud)
- GPT-4o (spec + code gen)
- Stripe
- Supabase (Postgres + Auth)
- Vercel + Expo hosting

**Effort:** 14d × 10h = 140h. Realistic for solo with Expo experience.

---

## 5. 30-day marketing calendar (≤ $300)

### Budget allocation ($290)
- Product Hunt launch: $0
- 2 newsletter mentions: $80 each = $160 (IndieHackers digest + Lenny's Newsletter)
- 1 Twitter/X promo campaign: $50
- 1 Fiverr demo video: $80

### Calendar

**Week 1:** Build + site + 3 SEO posts ("build iOS app no code", "AI app builder", "Lovable alternative")
**Week 2:** Launch PH + HN + IH. Email 100 founder friends. Post in r/SaaS, r/startups, IndieHackers, X build-in-public threads daily.
**Week 3:** Optimize trial → paid. A/B test hero. SEO posts #4-6. Case study #1.
**Week 4:** Newsletter mentions. G2 listing. Webinar: "I built a $1K MRR app in 30 min". Testimonial collection.

### KPIs
- Free trial signups: 200 (month 1)
- Trial → paid: 15% (high-intent audience)
- Paying customers end of month 1: 30 × $49 = $1,470 MRR (target)
- X followers: 1,500

---

## 6. Unit economics to $10K MRR

### Pricing
- **Free Trial:** 7 days, 1 preview build
- **Starter:** $49/mo, 1 published app
- **Pro:** $99/mo, 3 apps + push notifications
- **Agency:** $299/mo, 10 apps + white-label
- **Annual:** save 20%

### Cost per user
- LLM (GPT-4o): ~$3/user/mo (spec + code + updates)
- EAS Build: ~$2/build (3 builds/mo = $6)
- App Store fee (Apple $99/yr per org, amortized): $0.50
- Stripe fees: ~$1.50
- **COGS:** ~$11/user/mo
- **Gross margin:** ~78%

### Path to $10K MRR

| Month | Paying subs (avg $70 ARPU) | MRR |
|---|---|---|
| 1 | 30 | $1,470 |
| 2 | 65 | $3,185 |
| 3 | 130 | $6,370 |
| 4 | 200 | $9,800 |
| 5 | 210 | $10,290 ✅ |

### CAC vs LTV
- Blended CAC: ~$40 (organic-heavy but founder/audience expensive to reach)
- LTV: avg 14mo × 78% margin × $70 = $764
- **LTV/CAC = 19x** ✓ very healthy

---

## 7. Kill criteria

Stop if:
- Day 14: <30 trial signups
- Day 30: <15 paying customers
- Day 60: trial → paid <8%
- EAS build failure rate >30%
- App Store rejection rate >50% (means spec/code quality bad)

Pivot to `magicslides-app` (GO pure) if killed.

---

## 8. Notes

- Pure GO, no narrow wedge required.
- Highest upside of all directions BUT highest technical risk (EAS + App Store is fragile).
- App Store review process is a real bottleneck — budget Day 12-14 for inevitable rejections.
