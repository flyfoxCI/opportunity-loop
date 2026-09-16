# Direction: Reverse Contact Lookup for Sales Reps / Recruiters (PeopleFinder unbundle)

**Tier:** GO_NARROW (demand 4, competition 2) — explicit narrow wedge required
**Run:** 2026-09-13_190156
**Reference:** Lurq By PeopleFinder — $38 MRR, 161 subs (TrustMRR)

---

## 1. Why this direction

**TrustMRR evidence:**
- Lurq By PeopleFinder: $38 MRR / $62 last30 / 161 subs → growing (last30 > MRR)
- Cluster "other" — broad
- 161 subs at $0.24 ARPU = volume play, but willing to pay proves model
- Adjacent: Apollo.io ($49/mo), ZoomInfo ($14K+/yr), Lusha ($29/mo), Seamless.AI ($79/mo)

**X/web evidence (proxy):**
- Sales X is full of: *"Apollo credits run out so fast"*, *"ZoomInfo is overpriced"*, *"Lusha returns 40% wrong numbers"*, *"I just want to look up one VP of Sales at a SaaS company"*
- Pain quotes: *"Apollo billed me $500 for 100 credits I didn't use"*, *"Seamless.AI gave me 5 wrong numbers in a row"*, *"I want pay-per-use, not subscription"*
- Recommend: *"Apollo alternative"*, *"cheap ZoomInfo"*, *"pay per lookup"*, *"reverse email lookup"*

**Why narrow wedge:**
- Lurq is consumer-facing people search (think Whitepages premium)
- B2B sales / recruiting is a *different* product (work email lookup, not personal)
- We narrow to **sales reps + recruiters ONLY** — they're the ICP with budget, urgency, willingness-to-pay

---

## 2. Competitor table

| Tier | Competitor | Pricing | Strengths | Weaknesses | Our edge |
|---|---|---|---|---|---|
| L1 | Apollo.io | $49/mo + per-credit | Massive DB, sequences | Credits run out, expensive | Unlimited or per-lookup |
| L1 | ZoomInfo | $14K+/yr | Enterprise gold standard | Way too expensive for solos | $49/mo for solos |
| L1 | Lusha | $29/mo | Browser extension | Bad accuracy (~60%) | Better accuracy via waterfall |
| L1 | Seamless.AI | $79/mo | Real-time search | Spammy reputation, accuracy | Clean data + clean UX |
| L2 | RocketReach | $50/mo | Cheap | Stale data | Real-time enrichment |
| L2 | Hunter.io | $49/mo | Domain search | Limited to email, no phone | Email + phone + LinkedIn |
| L3 | LinkedIn Sales Nav | $99/mo | Best LinkedIn data | Manual lookup, no API | API + enrichment |
| L3 | Clearbit | $99+/mo | Best enrichment API | Expensive | Lower price |

**Competition score:** **2** (low — Lurq is the only TrustMRR-listed "people finder" but it's consumer; B2B players (Apollo/ZoomInfo) are tier-1 but expensive and have accuracy/UX complaints)

---

## 3. PRD MVP

### User stories (P0)

1. **As a sales rep**, I paste a LinkedIn URL → get verified work email + direct phone + title + company.
2. **As a recruiter**, I upload 100 LinkedIn URLs → get CSV with email + phone for each.
3. **As a user**, I want pay-per-lookup ($0.50/lookup) OR a flat $49/mo for 200 lookups (no surprise overage).
4. **As a user**, I get a "confidence score" on each result + a "report bad data" button.

### Epic list

- E1: LinkedIn URL parser (extract name, company, title)
- E2: Email finder (waterfall: Apollo → Hunter → Snovio → pattern guess)
- E3: Phone finder (waterfall: Lusha → Seamless → direct dials)
- E4: Confidence scoring (number of sources, recency)
- E5: Bulk upload (CSV in, CSV out)
- E6: Stripe billing (pay-per-lookup + subscriptions)
- E7: Browser extension (LinkedIn → one-click lookup)
- E8: User dashboard + lookup history

### Feature scope

**P0 (14d):**
- LinkedIn URL → email + phone lookup
- Waterfall across 3-4 data providers
- Confidence score + source attribution
- Pay-per-lookup $0.50 OR $49/mo for 200 lookups
- Bulk upload (CSV)
- Browser extension (Manifest V3)
- Dashboard + history
- Landing page + 5 SEO posts

**P1 (week 3-4):**
- CRM integrations (HubSpot, Pipedrive, Salesforce)
- Sequence integration (Auto-mailer, Instantly, Smartlead)
- Auto-enrich on import
- Team seats ($99/mo for 5 seats)
- API access ($99/mo for 1K lookups)

**P2 (month 2-3):**
- Intent data (Bombora-style signals)
- Job change alerts
- Tech stack detection (BuiltWith-style)
- AI personalized opener generator
- White-label for agencies

**Non-goals:**
- Consumer people search (Lurq, Spokeo, Whitepages territory — explicitly out)
- Outreach sending (Instantly / Smartlead territory)
- Lead database (Apollo / ZoomInfo territory — we enrich, we don't store)
- Free tier (data costs money; we charge from lookup #1)

---

## 4. 14-day day-by-day build plan

| Day | Focus | Deliverable |
|---|---|---|
| 1 | Repo: Next.js + Supabase. Apollo + Hunter + Snovio API keys. | Skeleton |
| 2 | LinkedIn URL parser → name + company + title extraction. | Parser works |
| 3 | Email waterfall: Apollo → Hunter → Snovio → pattern-guess | Email waterfall |
| 4 | Phone waterfall: Lusha → Seamless → dials verification | Phone waterfall |
| 5 | Confidence scoring + source attribution | Scoring v1 |
| 6 | UI: paste LinkedIn URL → result in 5 sec with confidence bar | Core UX |
| 7 | Stripe billing: pay-per-lookup + subscription tiers | Billing live |
| 8 | Bulk upload: CSV in, CSV out with results | Bulk works |
| 9 | Browser extension (Manifest V3, LinkedIn sidebar) | Extension v1 |
| 10 | Marketing site: hero, how-it-works, pricing, comparison vs Apollo | Site live |
| 11 | 5 SEO posts: "Apollo alternative 2026", "ZoomInfo cheaper", "Lusha vs us", "free reverse email lookup", "sales navigator API" | Blog live |
| 12 | Onboarding drip. Free 5-lookup trial. Founding member pricing. | Onboarding |
| 13 | Beta with 10 sales reps / 5 recruiters. Fix bugs. | Beta |
| 14 | IndieHackers + Sales Hacker + r/sales launch | Launched 🚀 |

**Tech stack:**
- Next.js 14 + TypeScript + Tailwind
- Supabase
- Apollo API + Hunter API + Snovio + Lusha + Seamless (waterfall)
- Stripe (metered billing for pay-per-lookup)
- Chrome Extension (Manifest V3)
- Vercel

**Effort:** 14d × 10h = 140h.

---

## 5. 30-day marketing calendar (≤ $300)

### Budget allocation ($280)
- 2 sales/marketing newsletter mentions ($80 each = $160)
- 1 X promo campaign targeting sales/recruiting ($50)
- 1 Fiverr demo video ($40)
- Apollo comparison page SEO content ($30 — writing fee)

### Calendar

**Week 1:** Site + blog + comparison pages ("Apollo alternative", "ZoomInfo cheaper", "Lusha vs Lurq"). Warm 50 sales/recruiting influencers on X.
**Week 2:** Launch on IH + Sales Hacker + r/sales. Email 100 SDRs personally. Post in r/sales, r/recruiting, r/sysadmin, IH Slack, X sales hashtag.
**Week 3:** Optimize conversion (free trial → paid). A/B test landing. 1 newsletter mention. Case study: "saved $400/mo vs Apollo."
**Week 4:** 1 newsletter mention. G2 listing. Webinar: "Outbound without ZoomInfo". Testimonial collection.

### KPIs
- Free trial signups (5 free lookups): 300 (month 1)
- Free → paid: 20% (very high intent B2B)
- Paying users end of month 1: 60 × $30 ARPU = $1,800 MRR
- Lookups completed: 5,000+ (data flywheel)

---

## 6. Unit economics to $10K MRR

### Pricing
- **Pay-per-lookup:** $0.50/lookup (no subscription)
- **Starter:** $49/mo for 200 lookups ($0.245/lookup)
- **Pro:** $99/mo for 500 lookups ($0.198/lookup)
- **Team:** $199/mo for 5 seats, 1,500 lookups
- **API:** $99/mo for 1,000 lookups

### Cost per lookup (waterfall avg)
- Apollo/Hunter/Snovio/Lusha/Seamless API fees: ~$0.10-0.20/lookup (we eat this)
- Hosting + Stripe: ~$0.05
- **COGS:** ~$0.20/lookup
- **Gross margin:** ~60-90% (depends on tier)

### Path to $10K MRR

| Month | Paid subs (avg $50 ARPU) | MRR |
|---|---|---|
| 1 | 60 | $1,800 |
| 2 | 140 | $4,200 |
| 3 | 240 | $7,200 |
| 4 | 330 | $9,900 |
| 5 | 340 | $10,200 ✅ |

### CAC vs LTV
- Blended CAC: ~$25 (targeted B2B audience)
- LTV: avg 14mo × 75% × $50 = $525
- **LTV/CAC = 21x** ✓ excellent

---

## 7. Kill criteria

Stop if:
- Day 14: <100 trial signups after launch
- Day 30: <30 paying customers
- Day 60: free → paid <10%
- Accuracy below 50% (we must beat Apollo/Lusha or we're dead)
- Provider API costs spike (must renegotiate or pivot to single-provider)

Pivot to `appalchemy` (GO pure) if killed.

---

## 8. Wedge (required for GO_NARROW)

**Our wedge — what we REFUSE to build:**

- ❌ **Consumer people search.** No "find my ex" or "find anyone's address." Lurq owns that. We're B2B-only.
- ❌ **Outreach sending.** No email sequencer, no dialer. Instantly/Aipharma/Orum territory.
- ❌ **Lead database storage.** We don't build a DB. We enrich on-demand via waterfall.
- ❌ **Free tier beyond 5 trial lookups.** Data is expensive; we charge from lookup #1.
- ❌ **Enterprise / SOC2.** We're solo-founder-priced. ZoomInfo owns enterprise.
- ❌ **Personal data broker.** We don't sell consumer data. GDPR/CCPA-friendly B2B only.

**What we WILL build:**

- ✅ **Sales rep + recruiter ICP only.** SDRs, BDRs, AEs, founders doing outbound, agency recruiters, in-house recruiters.
- ✅ **LinkedIn URL → verified email + phone in 5 seconds.** Core promise.
- ✅ **Waterfall enrichment** (best-of-breed providers, not locked-in).
- ✅ **Confidence scoring** — we tell you when data is old vs fresh.
- ✅ **Pay-per-lookup option** — no surprise overage bills.
- ✅ **Browser extension** — one-click from LinkedIn.
- ✅ **Bulk upload** — 100 LinkedIn URLs → CSV in 60 sec.

**Why this wedge wins:** Apollo is bloated and expensive for solos. Lusha has accuracy issues. ZoomInfo is enterprise-only. We sit in the solo-founder / small-team gap with better UX, transparent pricing, and B2B-only data hygiene. Solo founder can ship this in 14d.
