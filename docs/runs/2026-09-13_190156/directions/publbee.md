# Direction: Newsletter Cross-Promo for Indie Hackers / Solo Creators (Publbee unbundle)

**Tier:** GO_NARROW (demand 4, competition 3) — explicit narrow wedge required
**Run:** 2026-09-13_190156
**Reference:** Publbee — $35 MRR, 103 subs (TrustMRR)

---

## 1. Why this direction

**TrustMRR evidence:**
- Publbee: $35 MRR / $32 last30 / 103 subs → small but real revenue
- Founder @nezirbasar1 active — solo founder in newsletter space
- Category: "other" cluster — broad cross-promo
- Adjacent: Substack, Beehiiv, ConvertKit all have recommendations but no dedicated cross-promo swap network

**X/web evidence (proxy):**
- X is full of: *"looking for newsletter swaps"*, *"anyone want to do a newsletter cross-promo?"*, *"Substack recommendations are dead"*
- Pain quotes: *"I tried newsletter swaps manually, took 3 hours per week"*, *"Substack recs feature buries small creators"*, *"I want to swap with creators in my niche only"*
- Recommend: *"newsletter swap service"*, *"Substack cross-promo tool"*, *"Beehiiv boost alternative"*

**Why narrow wedge:**
- Publbee serves all newsletter creators — horizontal
- Each niche has its own rhythm, audience overlap, and "complementary not competitive" rules
- We narrow to **indie hackers / solo creators / bootstrapped founders** — single, well-defined ICP with high overlap (IH reader also reads other IH writers)

---

## 2. Competitor table

| Tier | Competitor | Pricing | Strengths | Weaknesses | Our edge |
|---|---|---|---|---|---|
| L1 | Publbee | $25/mo | Niche cross-promo | Generic, manual matchmaking | Algorithmic matching |
| L1 | Substack Recommendations | Free | Built-in, big network | Buries small creators, no curation | Curated for ICP |
| L1 | Beehiiv Boost | Free + paid | Network effects | New, generic | ICP-focused |
| L2 | Swapstack | $50/mo | Premium swaps | Expensive, no ICP filter | ICP filter + lower price |
| L2 | Newsletters.com | Free | Directory | No swap automation | Automated swap matching |
| L3 | Manual DMs | Free | Free | Hours/week, ghosting risk | We automate outreach |

**Competition score:** **3** (medium — Publbee exists, but horizontal; Swapstack is premium-priced; Substack recs are weak)

---

## 3. PRD MVP

### User stories (P0)

1. **As an indie hacker with a 2K-sub newsletter**, I want to auto-match with 5 other IH newsletters of similar size for cross-promo.
2. **As a user**, I want to schedule swaps in advance and see analytics (clicks, subs gained, list health impact).
3. **As a user**, I want to filter by niche (SaaS, AI, no-code, bootstrapping, devtools).
4. **As a paying user**, I unlock unlimited swaps + auto-send.

### Epic list

- E1: Newsletter profile (size, niche, audience demo, swap preferences)
- E2: Matching algorithm (size parity, niche overlap, audience complementarity)
- E3: Swap scheduler (when, which issue, what slot)
- E4: Auto-email-send via ESP integration (Beehiiv, ConvertKit, Substack, Mailchimp)
- E5: Analytics (clicks, subs gained, unsub impact)
- E6: User billing
- E7: Curated weekly digest of best swaps
- E8: Editorial content (IH newsletter playbook)

### Feature scope

**P0 (14d):**
- Profile onboarding (10-question form)
- Matching algo v1 (size + niche overlap, cosine similarity)
- Manual swap request (send a swap to a specific creator)
- Analytics dashboard (clicks, subs gained — via UTM)
- Stripe billing: $19/mo Starter (4 swaps/mo), $49/mo Pro (unlimited swaps + auto-send)
- Landing page + 5 SEO posts

**P1 (week 3-4):**
- ESP integrations (Beehiiv, Substack, ConvertKit, Mailchimp, Ghost)
- Auto-send (we send the swap on your behalf)
- Weekly curated swap digest
- "Featured swap" marketplace

**P2 (month 2-3):**
- AI copy suggestions for swap block
- Audience quality scoring (engagement rate, open rate)
- Premium "guaranteed growth" tier
- White-label for newsletter agencies

**Non-goals:**
- Newsletter authoring (Substack/Beehiiv territory)
- Paid newsletter platform (Ghost/Substack paid territory)
- Sponsorship marketplace (Swapstack/Sponsor Gap territory)
- General newsletter directory (we focus on swaps, not discovery)

---

## 4. 14-day day-by-day build plan

| Day | Focus | Deliverable |
|---|---|---|
| 1 | Repo: Next.js + Supabase. Profile schema. | Skeleton |
| 2 | Onboarding form (10 questions). Auth (magic link). | Profile done |
| 3 | Matching algo v1: size parity + niche tag overlap + audience geography | Matching works |
| 4 | Manual swap request: creator A picks creator B → email sent to B → accept/decline | Request flow |
| 5 | Swap confirmation + scheduling (pick date + issue) | Scheduling |
| 6 | UTM analytics: click tracking + sub attribution via ESP webhook | Analytics |
| 7 | Stripe billing. Free tier (1 swap/mo) + Pro $19/mo + Power $49/mo | Billing live |
| 8 | Dashboard: matches, pending swaps, completed swaps, analytics | Dashboard |
| 9 | ESP integration #1 (Beehiiv API). Auto-pull sub count + open rate | Beehiiv live |
| 10 | Marketing site: hero, how-it-works, pricing, testimonials | Site live |
| 11 | 5 SEO posts: "newsletter cross-promo 2026", "Substack recs alternative", "Beehiiv boost vs us", "indie hacker newsletter growth", "swapstack alternative" | Blog live |
| 12 | Onboarding drip. Founding member pricing ($9/mo for first 100 users). | Drip + founder pricing |
| 13 | Beta with 20 IH newsletter writers. Fix bugs. | Beta |
| 14 | IndieHackers launch + X thread + Product Hunt | Launched 🚀 |

**Tech stack:**
- Next.js 14 + TypeScript + Tailwind + Shadcn
- Supabase (Postgres + Auth)
- Beehiiv API + Substack RSS + ConvertKit
- Stripe
- Resend (transactional)
- Vercel

**Effort:** 14d × 10h = 140h.

---

## 5. 30-day marketing calendar (≤ $300)

### Budget allocation ($280)
- 2 IH/Lenny-style newsletter mentions ($80 each = $160)
- 1 X promo campaign ($50)
- Fiverr demo video ($40)
- Founding-member badge / swag ($20 — domain only)

### Calendar

**Week 1:** Site + blog + warm 50 IH newsletter writers personally (DM them on X).
**Week 2:** Launch on IH + X + PH. Email 200 IH creators personally. Post in r/IndieHackers, r/SaaS, IH Slack.
**Week 3:** Optimize conversion (free → Pro). A/B test landing. 1 newsletter mention. Case study from top swapper.
**Week 4:** 1 newsletter mention. G2 listing. "Top 10 IH newsletter swaps this month" report (viral content).

### KPIs
- Free signups: 250 (month 1)
- Free → paid: 12% (high-intent audience)
- Paying users end of month 1: 30 × $19 = $570 MRR
- Newsletter swaps completed: 100+ (social proof for month 2)

---

## 6. Unit economics to $10K MRR

### Pricing
- **Free:** 1 swap/mo, manual request
- **Starter:** $19/mo, 4 swaps/mo
- **Pro:** $49/mo, unlimited swaps + auto-send + analytics
- **Power:** $99/mo, priority matching + featured slots + AI copy

### Cost per user
- LLM (AI copy suggestions): ~$0.50/user/mo
- ESP API calls: ~$0.20
- Stripe + Resend: ~$1.00
- Hosting: ~$0.30
- **COGS:** ~$2.00/user/mo
- **Gross margin:** ~89% (Pro) / 96% (Power)

### Path to $10K MRR

| Month | Paid subs (avg $30 ARPU) | MRR |
|---|---|---|
| 1 | 30 | $570 |
| 2 | 80 | $1,920 |
| 3 | 180 | $4,500 |
| 4 | 350 | $8,750 |
| 5 | 400 | $10,000 ✅ |

### CAC vs LTV
- Blended CAC: ~$15 (organic IH community is hyper-targeted)
- LTV: avg 18mo × 89% × $30 = $480
- **LTV/CAC = 32x** ✓ very healthy

---

## 7. Kill criteria

Stop if:
- Day 14: <40 free signups after launch
- Day 30: <15 paying customers
- Day 60: free → paid <6%
- Swap completion rate <50% (matching algo or trust broken)
- IH community backlash (e.g., "this is spam") — pivot to permission-only mode

Pivot to `magicslides-app` if killed.

---

## 8. Wedge (required for GO_NARROW)

**Our wedge — what we REFUSE to build:**

- ❌ **All newsletters.** We are IH / solo creator / bootstrapped founder only. Lifestyle writers, finance bros, politics — out.
- ❌ **Paid newsletter platform.** Substack/Beehiiv/Ghost own this.
- ❌ **Sponsorship marketplace.** Swapstack, Paved, Sponsor Gap territory.
- ❌ **Generic newsletter directory.** Newsletters.com territory.
- ❌ **Substack-only.** We support Beehiiv, ConvertKit, Mailchimp, Ghost, *and* Substack via RSS — we don't pick sides.

**What we WILL build:**

- ✅ **IH / bootstrapped founder newsletter writers only.** ICP filter from day 1.
- ✅ **Curated matching** — we hand-pick top swaps weekly in our digest.
- ✅ **Cross-promotion as a growth lever**, not just discovery.
- ✅ **Analytics that matter** — sub gained, list churn impact, open rate preservation.
- ✅ **Community play** — IH Slack channel, weekly office hours, founder Q&A.

**Why this wedge wins:** Publbee is horizontal and small. Swapstack is premium-priced and ad-focused. IH community is the highest-LTV newsletter niche (B2B readers, high engagement, willing to pay for tools). Solo founder can dominate this niche in 90 days.
