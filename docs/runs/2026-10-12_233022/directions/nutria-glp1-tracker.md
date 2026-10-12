# Direction — `nutria-glp1-tracker` (unbundle of `nutria-9e3eaa`)

> **UNBUNDLE** of Nutria / Calyra ($461 MRR · 14,488 subs) — see `candidates.csv`.
> **Tier:** GO  ·  **demand 4 · competition 2**  ·  **MVP 12 days · solo**  ·  **$300 / 30d marketing cap**

---

## 1. Why this direction

**TrustMRR evidence**
- Nutria (Calyra AI calorie tracker) shows real consumer willingness to pay for an AI calorie-tracking mobile utility at a tiny ARPU. 14k subs against ~$461 MRR implies roughly $0.03–0.05 ARPU blended — meaning most revenue comes from new-trial conversions at $4.99–9.99/mo or one-time unlocks.
- The fact that 26 separate "other"-category listings match this shape (low MRR, high subs) tells us the demand profile is durable across the calorie / wellness mobile utility space.

**Web / cultural evidence**
- GLP-1 receptor agonists (Ozempic, Wegovy, Mounjaro, Zepbound) crossed into mainstream in 2023–2025. US prescriptions crossed 15M annually in 2025; spend >$1.3B/mo.
- Reddit r/Ozempic ~60K members, r/Mounjaro ~50K, r/GLP1 ~10K — **massive organic gathering points**.
- "Ozempic tracker app" / "GLP-1 food log" are searched but no dominant tool exists. Most users bolt MyFitnessPal or Cronometer onto their GLP-1 journey and complain that *neither* is built for the new physics (severely reduced appetite, side effects, low protein floor, muscle-loss concern).
- Common complaints we will copy from MyFitnessPal app-store reviews and r/Ozempic threads:
  - "Logging is tedious when you only eat 600 kcal a day."
  - "Doesn't show protein-to-calorie ratio, which my dietician wants."
  - "No way to log injection site + side effects together with food."
  - "Wants me to weigh in daily; on GLP-1 my weight stalls for weeks and I feel like I'm failing."

**Why the wedge works**
- General AI calorie trackers optimize for **weight loss speed**. GLP-1 users are on a medical protocol with a fundamentally different optimization function: **protein floor + lean-mass preservation + side-effect minimization + sustainable habit formation** (they cannot "go faster" — the drug does the work).
- Almost no app is built for this.

---

## 2. Competitor table (L1 / L2 / L3)

| Tier | Competitor | Pricing | Why they lose |
|---|---|---|---|
| L1 direct | **Nutria / Calyra** (iOS) | $4.99–9.99/mo or one-time unlocks | Generic AI-calorie; no GLP-1 awareness. Reviews ask for protein + side-effect tracking. |
| L1 direct | **Pep / Pep.ai** (iOS) | $9.99/mo | Has GLP-1 mode but storage and chat-only UX; poor retention per app-store reviews. |
| L2 adjacent | **MyFitnessPal** | $9.99–19.99/mo or $79.99/yr | Massive, but built for calorie deficit, not medical protocol. Stigma + cluttered UX turns GLP-1 users off. |
| L2 adjacent | **Cronometer** | $2.99–9.99/mo | Built for micronutrient density. Better fit than MFP, but no AI, no chat, no GLP-1 framing. |
| L2 adjacent | **Shotsy** (iOS, Ozempic-specific) | $4.99–7.99/mo | Tracks injections + side effects but does **not** track food. We eat the adjacent. |
| L3 substitute | **Pen + paper + ChatGPT prompt** | free | Real competitor for the cost-conscious. We win on speed + memory + sharing with dietician. |

**Score:** competition = **2** (a few generic tools, one shallow Ozempic-only tracker, no integrated incumbent).

---

## 3. PRD MVP (P0 / P1 / P2 + non-goals)

### Personas
- **P0 — "GLP-1 starter" (week 1–4 of protocol).** Wants reassurance, low-effort logging, side-effect watch.
- **P1 — "Plateau warrior" (week 5+).** Wants protein floor, lean-mass signals, weekly trend explainers.
- **P2 — "Long-game maintainer" (month 6+).** Taper/dose-adjustment tools, share-with-clinician PDF.

### P0 — must ship day 12
- **Onboarding (≤ 60 seconds)** captures: drug (Ozempic/Wegovy/Mounjaro/Zepbound/compounded), current dose, start date, goal (lose / maintain).
- **One-tap meal log.** Photo → AI estimates calories + protein + carbs + fat + fiber; user confirms in ≤2 taps. (Backed by GPT-4o vision + USDA database.)
- **Daily protein floor ring.** Distinct visual from calorie ring. Default 90g (or computed from lean mass).
- **Side-effect log.** Nausea, constipation, sulfur burps, fatigue, mood — slider 0–3 with timestamp.
- **Injection log.** Site rotator visual (8 sites), dose mg, next-dose countdown.
- **Weekly AI recap** every Sunday: protein floor hits, side-effect pattern, weight trend *contextualized* (reminds user weight stalls are normal on GLP-1).
- **Paywall:** 7-day trial → $9.99/mo or $69.99/yr.

### P1 — ship day 14 (soft launch with testers)
- "Plateau explainer" — when weight is flat 14+ days, AI generates a supportive plain-English paragraph (food quality, sleep, hydration check).
- Export PDF for dietician/doctor (PDFKit).
- WhatsApp quick-log (text a meal → bot parses → log entry).

### P2 — months 2–3
- Apple Health two-way sync (weight + steps).
- Lean-mass-preservation check (warns if losing >1% body weight / week).
- CGM integration (Lingo, Stelo) — large price tag, only after MRR justifies.

### Non-goals (explicitly out)
- **No telemedicine, no prescriptions.** We do not give medical advice. Disclaimer banner on every screen.
- **No weight-loss coach chat.** We surface data + short AI recaps. No chat-with-AI-coach threads (legal + scope risk).
- **No social feed, no community.** GLP-1 shaming is real; community is moderation burden.
- **No meal-planning wizard.** Generic, fat feature, regret at MVP stage.

### Pricing model
- Free: 3 logs/day, 7-day history.
- Pro: **$9.99/mo** or **$69.99/yr** (save 41%). Target 3% free→paid conversion, blended ARPU $4–5/mo.

### Tech stack (lean)
- Next.js 14 (App Router) + Tailwind + shadcn/ui.
- Expo / React Native for iOS+Android (one codebase).
- Supabase (Postgres + Auth + Storage).
- GPT-4o-mini for image parsing (~$0.0008/image) — cost-fits margins.
- Stripe via RevenueCat for subscriptions.
- Posthog for events.

---

## 4. 14-day day-by-day build plan

| Day | Goal | Output |
|---|---|---|
| **D1 Mon** | Repo scaffold, Next.js + Expo + Supabase. Auth flow (magic link). | Login works locally. |
| **D2 Tue** | Schema: users, drug_profiles, meals, side_effects, injections, weights. | Migrations + seed. |
| **D3 Wed** | Onboarding screens (drug pick, dose, goal). | Onboarding → dashboard. |
| **D4 Thu** | Meal log: photo + AI estimate + confirm. GPT-4o-mini integration. | Photo → log saved. |
| **D5 Fri** | Protein floor ring + side-effect log + injection log. | Three inputs on dashboard. |
| **D6 Sat** | Streaks, history view, daily totals. | History page working. |
| **D7 Sun** | Weekly recap cron (Sunday email). | First recap generated. |
| **D8 Mon** | Paywall (RevenueCat) + trial gating. | Free vs Pro UI. |
| **D9 Tue** | Apple Health read (weight). | Weight import daily. |
| **D10 Wed** | Polish, empty states, error handling, loading skeletons. | Demo-ready. |
| **D11 Thu** | TestFlight + Google internal track. 10 beta testers onboarded. | First 10 installs. |
| **D12 Fri** | Pricing live, paywall tested, analytics wired (Posthog). | RevenueCat live mode. |
| **D13 Sat** | Marketing assets: landing page v1, Loom demo, 4 Reddit posts drafted. | Landing live. |
| **D14 Sun** | Soft launch: post in r/Ozempic + r/Mounjaro + IndieHackers. | Public launch. |

**Definition of done:** P0 features tested by ≥3 testers, payment works, landing page load <2 s Lighthouse mobile ≥85, crash-free ≥99.5% over 24h.

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Day | Channel | Action | Cost |
|---|---|---|---|
| D1 | Reddit | Lurk r/Ozempic, r/Mounjaro, r/GLP1. Reply to 5 threads/day with genuine help (no plugs). | $0 |
| D3 | X / Twitter | Build @handle, pin bio, post "I built an AI food tracker for people on Ozempic — here's what I learned" thread (no link first). | $0 |
| D4 | Reddit | First post (showcase): "I built a free tracker focused on protein + side effects because MFP felt wrong on Ozempic." Sticky post with screenshots. | $0 |
| D5 | ProductHunt | "Coming soon" page up. | $0 |
| D7 | IndieHackers | Build log post #1: "Building in public: day 7, $0 MRR." | $0 |
| D10 | Reddit | Cross-post in 2 subreddits (build-in-public, sidehustle). | $0 |
| D12 | SEO | Publish 3 long-tail articles: "best food tracker for ozempic" / "ozempic protein calculator" / "wegovy meal log app". | $0 |
| D14 | X | Post a 30-sec screen recording demo. | $0 |
| D15 | Reddit AMA in r/GLP1 | Wait until product is live. Offer free Pro for first 50. | $0 |
| D17 | ProductHunt | Launch (Tue/Wed optimal). Get 5 friends + 2 indie partners to commit. | $0 (organic) |
| D18 | X | Founder thread: "what I learned shipping an AI tracker in 14 days" — tag relevant builders. | $0 |
| D20 | Reddit | Post before/after of weekly recap email screenshot. Pin to profile. | $0 |
| D22 | SEO | Publish 2 more keywords: "side effects log ozempic" / "wegovy plateau week 3". | $0 |
| D24 | IndieHackers | Build log #2: "$X MRR at day 24". | $0 |
| D26 | Reddit | Answer 10 threads/week with app mention when genuinely useful. | $0 |
| D28 | X | Two customer screenshots (with permission) + quote. | $0 |
| D30 | Lifecycle | Win-back email series (3 emails) for trial-expired users. | $0 |

**Paid budget usage:** reserve $200 for an *optional* Reddit ad test on Day 21 IF organic CAC is below $3. If not, the $200 rolls into a small Meta retargeting campaign Day 25–30 to people who visited landing. **Hard cap: $300. Default: $0.**

**KPIs tracked in Posthog + Stripe dashboard**
- D7 retention ≥ 25%.
- Free→paid ≥ 3%.
- Blended CAC < $5 by D30 (organic).
- MRR by D30: ~$300 (3% of 100 paid × $9.99 ≈ $300 baseline; stretch $600).

---

## 6. Unit economics to $10K MRR

| Variable | Value | Source |
|---|---|---|
| ARPU (blend of mo+yr) | $6.50/mo | $9.99/mo, 60% monthly / 40% annual at $69.99/yr/12 = $5.83, weighted ≈ $6.50 blended after year 2 carryover. |
| Gross margin | 82% | GPT-4o-mini ≤$0.20/mo/user at 8 logs/day; Stripe 2.9% + 30¢; Apple/Google 15%. |
| Monthly churn (consumer) | 6% (start), 4% by month 6 | GLP-1 protocols are 6–12+ months — built-in tenure. |
| Paid users needed for $10K MRR | ~1,540 | $10,000 / $6.50 ≈ 1,538 |
| New paid / month needed at 4% steady churn | ~62 | (1,540 × 4%) ≈ 62 new paid/mo to keep flat line. |

**Path to $10K MRR (12 mo)**
| Month | Paid users (start) | New paid | Churn | Paid users (end) | MRR end |
|---|---:|---:|---:|---:|---:|
| 1 | 30 | 30 | 2 | 58 | $377 |
| 3 | 110 | 80 | 4% | 178 | $1,157 |
| 6 | 350 | 110 | 4% | 478 | $3,107 |
| 9 | 700 | 140 | 4% | 870 | $5,655 |
| 12 | 1,100 | 180 | 4% | 1,255 | $8,158 |
| **13** | 1,255 | 220 | 4% | **1,538** | **$10,000** |

**Sensitivity:** if ARPU lands $5 instead of $6.50, need 2,000 paid by month 13 — same shape, 30% more users, totally achievable off subreddit compounding.

**Break-even:** at ~80 paid users (~$520/mo MRR) SaaS ops cost is covered with $0 salary to solo founder.

---

## 7. Kill criteria (hard)

- **D7 retention < 15%** after 100 installs → product is not sticky; pivot messaging not product.
- **Free→paid < 1.5%** after 200 installs → pricing or value-prop mismatch.
- **Organic CAC > $12** by day 30 → channels are wrong; pause paid, re-pick subreddit/SEO keywords.
- **Any clinical liability event** (user claims harm) → pull the product, add medical disclaimer, refactor.
- **< 1 paying user by D30** despite 100+ installs → kill this direction; pick a `fastwrite` or `sketchup` direction at D31.
- **Sustained NSFW / shame in target subreddit** (e.g. class-action talk) → pause Reddit ads.

---

## 8. Risks specific to GLP-1 verticals

- **Regulatory creep.** FDA may at some point restrict consumer apps making health claims around GLP-1 use. Mitigation: keep disclaimer prominent, never advise dosing, never diagnose.
- **Drug patent cliff / pricing.** GLP-1 oral generics are coming; user base grows but per-customer spend may compress. Mitigation: be at the food/logging layer (drug-agnostic), pivot to broader "metabolic-health tracker" if needed.
- **Brand safety.** Reddit GLP-1 subs swing between pro and anti medication. Mitigation: only post helpful content, never shill.
- **LTV drag from "starter" users.** 30–40% of new users stop their protocol in <3 months (cost + side effects). Mitigation: design for taper/maintain persona as well (P2), and run a "What happened?" exit survey.
