# Direction — `quizfunnel-creators` (unbundle of `uizze`)

> **UNBUNDLE** of Uizze ($18 MRR · 196 subs · demand 4 / comp 2).
> **Tier:** GO  ·  **MVP 14 days · solo**  ·  **$300 / 30d marketing**

---

## 1. Why this direction

**TrustMRR evidence**
- Uizze at $18 MRR / 196 subs proves there is a **creator-Economy-priced quiz/funnel tool** gathering traction in this category.
- 196 subs for a no-brand tool means there is organic pull — the category is larger than the brand.

**Web / cultural evidence**
- Interactive content (quizzes, scorecards, calculators) converts **2× to 5×** better than static landing pages. Famously: Typeform's "find your archetype" quizzes, Outgrow's "What salary should you be earning?", ScoreApp's marketing-quiz funnels.
- **For creators specifically:** "scorecard" is a hot product on Gumroad (Kate Kordsmeier, ListKit, Hannah Eve among the indie builders). Most are built on a no-code spreadsheet + checkout. Pain points: ugly templates, hardcoded results, no A/B testing, no analytics, no Stripe wiring.
- **For TikTok / IG / YouTube creators:** "comment to get the quiz" funnels drive 5–15K DMs per week for serious creators. Existing tools (Typeform → Stripe) are 8-step setups; creators want 1-step.

**Why the wedge works**
- Two ICPs in one tool:
  - **Solo creators (IG/TikTok)** want a quiz → lead-magnet → Stripe checkout in <30 min.
  - **Small agencies** want A/B testable quiz funnels with analytics and DM handoff.
- Uizze is a budding version; we beat them on (1) one-page funnel UX, (2) native Stripe checkout, (3) DM-handoff without Zapier, (4) A/B testing, (5) better templates.

---

## 2. Competitor table (L1 / L2 / L3)

| Tier | Competitor | Pricing | Why they lose |
|---|---|---|---|
| L1 direct | **Uizze** | indie pricing | Under-funded, no Stripe checkout, no DM-handoff. |
| L1 direct | **ScoreApp** | $67+/mo | Power-user; steep learning curve, ugly editor for creators, no IG-native flow. |
| L1 direct | **Typeform + Stripe + Zapier** | $25+$29+$19 = $73/mo + glue work | Composer-suite; too many subscriptions, manual wiring. |
| L1 direct | **Outgrow** | $22–220/mo | Generic, enterprise feel; not creator-first. |
| L2 adjacent | **Involve.me** | $29+/mo | Better than Outgrow but not creator-leaning. |
| L2 adjacent | **Interact** (quiz maker) | $43+/mo | Marketing teams, not individual creators. |
| L3 substitute | **Google Forms + Stripe link in bio** | free | Loses; creator wants branded domain + lead capture + scored outcome. |
| L3 substitute | **Spreadsheet + Gumroad URL** | free | Loses on automation, A/B testing. |

**Score:** competition = **2**. The creator-quiz corner has no incumbent.

---

## 3. PRD MVP (P0 / P1 / P2 + non-goals)

### P0 — must ship day 14
- **Drag-and-drop builder:** 8 question types (multiple choice, slider, image-pick, short text).
- **Branching:** based on score, route to outcome A / B / C with custom copy.
- **Stripe checkout embed** on outcome page (or button).
- **Custom domain** (CNAME) on Pro tier.
- **Analytics:** completions, drop-off per question, conversion rate, revenue.
- **A/B testing:** 2 variants of same quiz, traffic split.
- **Pre-built templates:** 12 (love calculator, brand archetype, salary, fitness score, etc.).
- **Free tier:** 1 quiz, 100 responses/mo, uizze-branded footer.
- **Pro tier:** $29/mo unlimited quizzes + responses + custom domain + A/B testing.
- **Studio tier:** $99/mo 5 client workspaces.

### P1 — month 2
- **IG / TikTok DM handoff:** webhook → Manychat integration (one-click).
- Lead export to Klaviyo, Mailchimp, ConvertKit.
- Pixel tracking (Meta + TikTok).

### P2 — month 3+
- Multi-step funnel (quiz → email → sales call booking).
- Marketplace of templates (revenue-share with creators).
- AI question-generator (paste blog URL → draft 10 questions).

### Non-goals
- **No email-sending.** Always hand to ConvertKit/Klaviyo.
- **No appointment booking (Calendy).** Out of scope.
- **No course / membership delivery.** Link to Kajabi/Thinkific.

### Tech stack
- Next.js 14 + Tailwind + shadcn/ui.
- Convex for live reactive state and storage of results.
- Stripe checkout embed (Hosted vs Custom — Hosted for speed, switch to Custom at scale).
- Resend + React Email for transactional.
- Cloudflare Pages (static on domain).
- PostHog analytics.

---

## 4. 14-day day-by-day build plan

| Day | Goal | Output |
|---|---|---|
| **D1 Mon** | Repo scaffold + auth + Convex schema (Quiz, Question, Response, Outcome, Stripe sub). | Auth live. |
| **D2 Tue** | Drag-and-drop builder (dnd-kit). | Builder works. |
| **D3 Wed** | Live preview renderer (responsive). | Preview works. |
| **D4 Thu** | Public quiz runner. | Public URL → renders correctly. |
| **D5 Fri** | Outcome branching logic. | Routes A/B/C work. |
| **D6 Sat** | Analytics dashboard (submissions, drop-off). | Charts render. |
| **D7 Sun** | 12 templates seeded. | Template gallery. |
| **D8 Mon** | Stripe embedded checkout on outcome page. | Payment works. |
| **D9 Tue** | A/B testing logic (2 variants, 50/50 split). | A/B live. |
| **D10 Wed** | Custom domain (CNAME + Vercel/Cloudflare). | Domain works. |
| **D11 Thu** | Polish, empty states, accessibility. | Demo-ready. |
| **D12 Fri** | Beta with 8 creators (Twitter + IndieHackers). | 8 installs. |
| **D13 Sat** | Bug bash + analytics + waitlist funnel. | Stable. |
| **D14 Sun** | **Launch on ProductHunt (Tue optimal — schedule).** | Live. |

**DoD:** Builder drag-and-drop, public runner, outcome branching, Stripe take, analytics, A/B, 12 templates, payment works, mobile responsive.

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Day | Channel | Action | Cost |
|---|---|---|---|
| D1 | X | Build @quizfunnel handle; pin "I want to ship a 1-page quiz funnel builder for creators — what's your #1 pain?" | $0 |
| D3 | TikTok | Personal account: 60-sec screen recording of building a quiz in 5 min. TikTok loves "building in public". | $0 |
| D5 | IndieHackers | Lead-magnet post: "I want to ship X, what's wrong with current tools?" | $0 |
| D7 | Reddit | Cross-post in r/creatoreconomy, r/NewTubers, r/sidehustle. | $0 |
| D10 | X | Thread: "how I shipped a quiz funnel in 14 days" with screenshots. | $0 |
| D12 | TikTok | Tutorial: "Make a $29 quiz funnel in 7 minutes" (template). | $0 |
| D14 | ProductHunt | Launch (Tue). | $0 |
| D15 | Reddit | AMA in r/creatoreconomy. | $0 |
| D17 | SEO | Publish 4 SEO pages: "scorecard maker for creators", "quiz funnel tool for IG", "tiktok lead magnet", "stripe-linked quiz". | $0 |
| D20 | X | Show 5 customer-built quizzes (with permission). | $0 |
| D22 | IndieHackers | Build log "$X MRR at day 22". | $0 |
| D24 | TikTok | New tutorial featuring a customer funnel. | $0 |
| D27 | IndieHackers | Post a free resource (Notion template "Quiz funnel copy swipe file"). Lead magnet. | $0 |
| D30 | Lifecycle | Re-engagement email to inactive free quizzes ("Your quiz stopped receiving traffic — try these fixes"). | $0 |

**Paid budget:** **Default $0.** Allocate $200 to a TikTok Spark test on the D14 demo video IF it has >10K organic views by D7.

**KPIs**
- Templates used to publish: avg 1.5 quizzes/creator.
- Free→paid ≥ 5%.
- D7 retention ≥ 30%.
- MRR by D30: ~$500–1,000 baseline.

---

## 6. Unit economics to $10K MRR

| Variable | Value | Source |
|---|---|---|
| ARPU (blend) | $35/mo | 80% Pro $29 + 15% Studio $99 + 5% free w/ future conversion → blend ≈ $35. |
| Gross margin | 80% | Convex, Stripe, email — small fixed costs. |
| Monthly churn | 6% | Creators come and go but volume is high. |
| Paid users needed for $10K MRR | ~286 | $10,000 / $35 ≈ 286. |
| New paid / month needed at 6% | ~22 | 286 × 6% ≈ 17/mo. |

**Path to $10K MRR (10 mo)**
| Month | Paid | New | Churn | Paid | MRR |
|---|---:|---:|---:|---:|---:|
| 1 | 30 | 30 | 2 | 58 | $2,030 |
| 3 | 120 | 70 | 6% | 188 | $6,580 |
| 6 | 260 | 80 | 6% | 339 | $11,865 |
| 9 | 380 | 90 | 6% | 464 | $16,240 |

> $10K MRR achievable by **month 5** with creator-Economy compounding.

**Break-even:** ~30 paid = $1,050/mo MRR.

---

## 7. Kill criteria (hard)

- **Builder completion rate < 70%** of in-progress quizzes (i.e., creators abandon before publishing) → UX is broken.
- **Free→paid < 3% by D30** → pricing or value-prop wrong.
- **< 50 new quizzes published/wk by D30** → channels wrong.
- **Stripe Connect onboarding > 24h** → push to Stripe Hosted checkout only.
- **TalentSearch:** if TikTok creator posts underperform vs X posts, double-down on the channel that converts paid signups (not views).

---

## 8. Risks specific to creator funnel tools

- **Platform policy:** TikTok/IG deprecate web-app funnels → mitigation: keep forms as web, push all conversion to Stripe (no in-app purchases).
- **"Quiz fatigue":** Trends shift (currently hot, cold cycles 12 mo). Mitigation: keep template gallery refreshed quarterly.
- **Stripe onboarding friction for non-US creators.** Mitigation: Stripe-supported countries only at MVP; expand later.
- **DMCA from template-IP owners.** Mitigation: all templates are original, copy-reviewed.
