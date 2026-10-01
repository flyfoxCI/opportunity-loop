# Direction — AppAlchemy (narrow wedge: text → Expo TestFlight build)

**Tier:** GO
**Slug:** `appalchemy`
**Run:** 2026-10-01_213404
**One-liner:** Describe a mobile app idea → get a working Expo (React Native) codebase + TestFlight / APK build in 10 minutes.
**Why this:** Demand 3 / Comp 2 per Stage A. $58 MRR + 205 subs at $0.28 ARPU = funnely. Wedge: text → Expo (not web, not Flutter, not native) → real TestFlight. The gap is no-code web (Softr, Glide) vs full mobile-build pipelines (Xcode pain). Solo mobile dev is hostile; we fill the gap.

## 1. Why this direction

### TrustMRR evidence
- Listing: `appalchemy.ai`, MRR $58, last30 $58, 205 subs.
- demand_h 3, comp_h 2.
- Founder @diegoroshardt is publicly active. Steady growth: last30 ≈ mrr → stable funnel.

### X / web evidence
- Pain clusters: r/iOSProgramming, r/reactnative, X: "I have an idea but I can't build it in Xcode", "Expo is faster but still 4 days to TestFlight".
- Existing: Softr / Glide / Bubble = web apps. FlutterFlow = mobile but slow + expensive. None ship to TestFlight in 10 minutes from a prompt.

### Wedge
- Input: text prompt (≤ 500 chars), schema hint (forms? list? auth?).
- Output: Expo repo (TypeScript) + Supabase schema + TestFlight build (via EAS).
- Refuse: web apps, native iOS Swift, Flutter, Android-only.

## 2. Competitor table

| Layer | Name | Pricing | Why we beat |
|---|---|---|---|
| L1 direct | AppAlchemy | ~$12/mo (inferred) | We ship TestFlight in 10 min, Expo route. |
| L2 adjacent | FlutterFlow | $30–70/mo | Visual, no AI; learning curve. |
| L2 adjacent | Softr | $59–$179/mo | Web only. |
| L2 adjacent | Bubble | $29–$475/mo | Web only. |
| L2 adjacent | Glide | $25–$250/mo | Spreadsheet app, web. |
| L3 substitute | v0.dev / Cursor | $20/mo | Code only, no TestFlight automation. |

Competition score = 2. The "AI → mobile App" niche has FlutterFlow and AppAlchemy. We narrow to Expo + Supabase + TestFlight.

## 3. PRD MVP

### User stories
- US-01 (P0): Type prompt, get Expo repo + TestFlight build.
- US-02 (P0): Pick schema: blank / forms / list / auth-required.
- US-03 (P0): Stripe sub $29/mo Hobby, $99/mo Studio (5 apps/mo).
- US-04 (P0): Generate new app = 1 build credit.
- US-05 (P1): Edit code in browser (Monaco).
- US-06 (P1): Push updates to existing app.

### Epic → features
- **EPIC A: Prompt → schema** — LLM (Claude Sonnet) outputs data model + screen list + navigation.
- **EPIC B: Code generator** — Templated Expo + React Native + Tailwind + Expo Router templates; LLM fills in the screen code.
- **EPIC C: Supabase auto-provisioning** — Each app gets a Supabase project, schema migrated via SQL.
- **EPIC D: EAS build + TestFlight** — Trigger EAS build, push to App Store Connect via Connect API.
- **EPIC E: Auth + billing.**

### P0 (ship-blocker)
- US-01..04 + EPIC A/B/C/D.

### P1 (week 1 polish)
- US-05, US-06.

### P2 (week 2)
- Multi-screen flow editor, image upload, theme picker.

### Non-goals
- Web apps.
- Native Swift / Kotlin.
- App Store submission review (we ship the build; user submits).
- Play Store (iOS-first).
- Multi-platform simultaneous.

### Tech stack
- Next.js 14 (admin UI)
- Expo + EAS (build pipeline)
- Supabase (per-app db)
- Claude API (code generation)
- EAS Build ($99/mo Studio, fits $300 cap)
- Apple App Store Connect API
- Stripe (billing)

### Data model
- `users(id, email, plan, credits, stripe_customer_id)`
- `apps(id, user_id, prompt, eas_project_id, supabase_project_id, build_status, last_build_id)`
- `builds(id, app_id, status, build_url, created_at)`

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Repo, scaffold, Expo template library |
| 2 | Prompt → schema LLM (Claude) with schema enum (blank/forms/list/auth) |
| 3 | Code generator: template + LLM fill |
| 4 | Supabase auto-provisioning (service-role key) |
| 5 | EAS build trigger + status polling |
| 6 | App Store Connect API integration |
| 7 | Stripe pricing + checkout + credits system |
| 8 | Admin dashboard: app list, build list |
| 9 | Landing page: 3 example apps (built with us), pricing, FAQ |
| 10 | Beta: 30 indie founders from IH, X |
| 11 | Polish: error states, retry, build queue |
| 12 | Edit-in-browser (Monaco, read-only first; later P1) |
| 13 | Public launch: IH, X, r/reactnative |
| 14 | Day-2 retention: weekly "new build" notification |

## 5. 30-day marketing calendar (≤ $300)

| Week | Channel | Action | Budget |
|---|---|---|---|
| 1 | X | Build-in-public thread: "I shipped 3 apps in 3 days using my own tool" | $0 |
| 1 | IndieHackers | Launch post | $0 |
| 1 | r/reactnative, r/expo | Value post: "I built an AI app-builder, here's a free app" | $0 |
| 2 | X | Daily app screenshots, real TestFlight links | $0 |
| 2 | YouTube | DM 5 small "build in public" YouTubers ($50 micro) | $50 |
| 3 | SEO | "AI mobile app builder 2026" | $0 |
| 3 | X ads | $50 boost on top thread | $50 |
| 3 | Reddit ads | Test r/reactnative slot | $50 |
| 4 | Newsletter | Guest on Build In Public newsletter | $80 |
| 4 | Lifetime deal | First-100 users $99 lifetime | — |
| | | **Total** | **$230** |

**Buffer:** $70.

## 6. Unit economics to $10K MRR

- Price: $29 Hobby (2 apps/mo) / $99 Studio (8 apps/mo). Blended ARPU ≈ $50.
- To $10K MRR: 10,000 / 50 = **200 paying users**.
- Free → paid: 8% (builders are willing to pay).
- Signups needed: 200 / 0.08 = **2,500 signups**.
- Visit → signup: 20% (technical audience, strong pitch).
- Visits: 2,500 / 0.20 = **12,500 visits** ≈ 417/day.

CAC: $230 / 200 = **$1.15**. LTV: $50 × 8 mo = $400. LTV/CAC = 348×.

Costs: EAS $99 + Claude API (~$0.10/build × 200 users × 4 builds/mo = $80) + Vercel $20 + Supabase $25 = **~$225/mo**. Plus Apple Developer fee $99/yr. Gross margin at $10K MRR ≈ 97%.

## 7. Kill criteria

- < 100 signups at day 14
- < 5% trial → paid at day 30
- EAS build success rate < 80%
- Apple App Store rejections > 30%
- LLM cost > 30% of revenue

## 8. (N/A — GO)

Expansion: add Flutter target, Android target, Play Store, custom domain per app.
