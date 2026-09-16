# Direction: JobRadar — AI lead gen + permit monitor for solo contractors (GO)

> Tagline: *Permits, leads, and callback reminders — without the $400/mo CRM tax.*

---

## 1. Why this direction

### TrustMRR evidence
- **NextjobConnect** (per seed report) — MRR ~$5K, contractor-focused AI lead gen. Validates willingness to pay.
- **Tradevipe** — $2.9K MRR / 14 customers. Same vertical, different wedge (admin not leads). Together they prove the market is real and underserved.

### Why this wins
1. **Contractors don't want CRMs.** They want *phone calls*. Our product outputs calls, not dashboards.
2. **Permit pulls are public-record gold.** Most counties publish building permits daily. Nobody is monitoring them as a subscription service for solo contractors.
3. **AI summarization beats raw data.** A roofer doesn't want "permit #2025-12345 issued at 142 Main St" — they want "New roof, $28K scope, owner is GC-able, call today."
4. **Sales is one industry at a time.** Land HVAC in 5 counties, then plumbers, then electricians. Each cohort is a $20/mo subscriber base of ~5,000.

---

## 2. Competitor table

| Tier | Competitor | What they do | Price | Threat |
|---|---|---|---|---|
| L1 | NextjobConnect | AI lead gen for contractors | $99+/mo | Direct. We differentiate on permit-monitor + AI call-summary, not generic lead gen. |
| L1 | ServiceTitan, Housecall Pro, Jobber | Field-service CRM for contractors | $65–$500/mo | Real but bloated. Our buyers are the 60% of contractors who refuse to adopt these. |
| L2 | Angi Leads, HomeAdvisor | Pay-per-lead marketplaces | $30–$150/lead | Different model. We win on "passive" leads via permits, not "marketplace" leads. |
| L2 | BuildZoom, Construction Monitor | Permit-data providers (B2B) | $200+/mo | Real incumbent for raw permit data. We are the AI-summary layer on top. |
| L3 | Google Alerts | Free | $0 | Yes, contractors use it today. We beat it on summarization, ranking, and SMS delivery. |
| L3 | Generic CRMs with permit integrations (JobNimbus) | Mixed | $100–$300/mo | Niche overlap. |

**Competition score: 2.** Direct lead-gen competitor exists (NextjobConnect), permit-data incumbents exist (BuildZoom), but no one is selling AI-curated, SMS-delivered, pay-per-lead permits for solo contractors.

---

## 3. PRD MVP

### User story
> *I'm a one-truck roofer in Maricopa County. I want to know the moment a permit is pulled for a re-roof in my service area, with the homeowner's name, the estimated scope, and the GC's name if any. I want it on my phone within 30 minutes of the permit hitting the county portal, and I want a weekly digest for everything else.*

### Epics
- **E1 — Permit ingestion.** Daily cron against county permit portals (where available) + partner data feeds where portals are paywalled.
- **E2 — AI summarization.** Convert raw permit rows → "Who, what, where, scope $, GC?, urgency".
- **E3 — User preferences.** Service area, trade, scope range, alert threshold.
- **E4 — Delivery.** SMS (Twilio) + email. Weekly digest.
- **E5 — Billing.** Stripe Checkout, $29/mo Solo, $79/mo Pro (multi-trade).
- **E6 — Admin.** Users, MRR, permits delivered, top trades.

### P0 (days 1–10)
- 1 county, 1 trade (roofers in Maricopa County, AZ).
- Daily permit scrape (manual CSV at first; partner API if available).
- AI summarization via OpenAI.
- SMS + email delivery.
- Stripe Checkout + webhook.
- Landing page + 1 case study (a friendly roofer will trade a year for a testimonial).

### P1 (days 11–14)
- Add 2 more counties (Harris County TX, Cook County IL).
- Add 1 more trade (HVAC).
- Weekly digest email.
- Customer dashboard with search.

### P2 (post-MVP, days 15–30)
- Lead-score model (high/medium/low).
- Twilio two-way SMS: contractor replies "more" and gets the full record.
- "I want this lead" one-click → $5/lead upsell.
- Add plumbers and electricians.

### Non-goals
- Doing the contracting work ourselves. (We never show up with a hammer.)
- Replacement for the contractor's CRM. (We send leads; they manage jobs elsewhere.)
- General-purpose lead-gen for non-trade verticals.
- Building permit *filing* (we read, we don't write).

### Pricing
- **Solo ($29/mo):** 1 trade, 1 county, SMS alerts.
- **Pro ($79/mo):** Up to 3 trades, 5 counties, email digest, lead score.
- **Pay-per-lead (add-on):** $5/lead when contractor taps "I want this."

---

## 4. 14-day day-by-day build plan

| Day | Output |
|---|---|
| 1 | Lock trade + county (roofer + Maricopa). Buy domain. Landing page + pre-sell 5 pilots. |
| 2 | Permit data source: Maricopa publishes daily CSVs. Cron fetches them. |
| 3 | AI summarization prompt + per-row scoring. |
| 4 | User onboarding: trade, county, phone, email. |
| 5 | Stripe Checkout + customer portal. |
| 6 | Twilio SMS integration + email (Resend). |
| 7 | Alert rules engine (high-scope → instant SMS, low-scope → weekly digest). |
| 8 | Customer dashboard with last 30 days of leads. |
| 9 | Seed 50 historical permits so the dashboard looks alive. |
| 10 | First 5 pilots onboard (manual, friendly roofers). |
| 11 | Add Harris County (TX). |
| 12 | Add Cook County (IL). |
| 13 | Add HVAC trade. |
| 14 | Public launch in r/Roofing, r/HVAC, contractor Facebook groups. |

**Stack:** Next.js + Postgres + Stripe + Twilio + Resend + OpenAI.

**Infra cost at MVP:** ~$100/mo.

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget allocation**
- $120 — Google Ads "permit leads for roofers" (exact match, $5/day cap)
- $80 — Direct-mail postcard to 500 roofers in Maricopa + Harris (8×10 postcard via Lob.com)
- $50 — Sponsorship of 2 contractor Facebook groups (one boost each)
- $30 — Trade-show booth at a local builders' association meeting
- $20 — Canva Pro

**Daily calendar (organic + paid mix)**

| Wk | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| 1 | Cold-email 50 roofers from a purchased list | Post in r/Roofing | LinkedIn post | Direct-mail 250 postcards | Cold-email 50 more | Cold-email 50 more | Cold-email 50 more |
| 2 | First Google Ads live ($5/day) | X thread: 7 things I learned scraping permits | Cold-email 50 more | Cold-email 50 more | Direct-mail 250 more | Cold-email 50 more | Cold-email 50 more |
| 3 | Cold-email 50 more | Case-study writeup from pilot roofer | Cold-email 50 more | Cold-email 50 more | First FB boost ($25) | Cold-email 50 more | Cold-email 50 more |
| 4 | Cold-email 50 more | Email blast to 200-person list | Cold-email 50 more | Cold-email 50 more | Second FB boost ($25) | Local builders' assoc meetup ($30) | Wrap-up |

**Targets (week 4):**
- 1,000 cold emails sent, 4% reply → 40 replies
- 25% reply → meeting → 10 meetings
- 40% close → 4 new roofers
- 4 new × $29 = $116 + 5 pilots × $29 = $145 = **~$260 MRR by day 30**
- Realistic month-1 MRR: $200–$300.

---

## 6. Unit economics to $10K MRR

| Metric | Value | Source |
|---|---|---|
| ARPU (Solo vs Pro) | $42/mo | 70% Solo ($29), 30% Pro ($79) |
| Gross margin | 80% | OpenAI + Twilio + infra |
| Monthly churn | 5% | Contractor churn is real; product has to keep delivering |
| Net new subs/mo (steady state) | 80 | Slower than whitelabel because per-customer price is lower |
| Months to $10K MRR | ~5 | (10,000 / 42) / (80 × 0.95) ≈ 5.2 months |

**Sensitivity:**
- If churn is 8% → ~8 months.
- If Pro ARPU drops to $50 blended → ~7 months.
- If we add pay-per-lead ($5/lead, 8 leads/mo each = +$40/customer) → ARPU jumps to $82, time to $10K drops to ~3 months.

**Worst case (churn 8%, ARPU $42, no upsell):** ~10 months. Right at the edge.

---

## 7. Kill criteria

- **Day 14:** If pilot conversion (free trial → paid) <20%, kill. Contractors are notoriously hard to convert.
- **Day 30:** If MRR < $300, kill the channel. The outbound engine isn't working.
- **Day 60:** If monthly churn >10%, kill. Product-market fit is wrong.
- **Day 90:** If MRR < $2,000, kill. Market is fundamentally too small at this price point.
- **Hard kill:** BuildZoom drops their price to under $100/mo and bundles AI summary. We can't win that fight.

---

## 8. Founder fit notes

- **Best for:** founder who likes sales, can read a county permit portal CSV without flinching, and is comfortable with low-ARPU high-volume SaaS. Bonus: a relative who is a contractor.
- **Bad fit if:** you hate phone calls, you can't physically visit a county office, or you need $50K MRR in 60 days.
- **Extension path after $10K MRR:** add more trades (HVAC, plumbing, electrical), add more states, sell pay-per-lead on top, exit to a vertical SaaS roll-up.
