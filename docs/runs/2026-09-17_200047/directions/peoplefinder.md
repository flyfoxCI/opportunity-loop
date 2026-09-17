# Direction: peoplefinder (People Lookup Utility)

Slug: `peoplefinder`
Tier: **GO**
Demand: 4 · Competition: 2
MRR signal: $42 / 176 subs / $66 last30
Run: 2026-09-17_200047

---

## 1. Why this direction

**TrustMRR evidence.** Lurq (PeopleFinder) at $42 MRR with 176 paying subscribers proves willingness-to-pay for a narrow people-lookup utility. ARPU ≈ $0.24/mo suggests an ultra-low price point ($2-3/mo) at high volume, OR a $5-9/mo price with many free users. Either way, the demand signal is real.

**Why this is buildable in 14 days.** No AI required for v1. People lookup = aggregate public records (court records, social profiles, business registries, address history). API integrations exist (open data sources + a few paid APIs). A solo founder can ship a working lookup tool in 14 days.

**X/web evidence.** Pain searches returned CLI help text. We rely on the TrustMRR signal + the validated pattern from `reports/directions/` (white-glove-content $601 MRR = same shape: subscription utility serving pros).

**Wedge we're picking.** "Find anyone's business email + LinkedIn in 10 seconds." We target sales reps + recruiters + journalists — clear ICP, clear ROI on $9/mo.

---

## 2. Competitor table

| Tier | Product | Pricing | Wedge gap |
|---|---|---|---|
| L1 direct | Apollo.io, ZoomInfo, Lusha | $49-99/mo (Apollo free tier limited) | Enterprise pricing; overkill for solo SDRs |
| L2 adjacent | Hunter.io | $49/mo (50 credits) | Email-only, no phone/address |
| L2 adjacent | RocketReach | $60/mo | Same as Apollo |
| L2 adjacent | Clearbit | $99+/mo | Enterprise |
| L3 weak | Manual Google + LinkedIn | $0 | Time cost = $20+/search |
| **Our wedge** | **Lurq-lite: Email + Phone + Address lookup** | **$9/mo (100 lookups)** | "Cheap Apollo for solo reps" |

Competition score: **2** — incumbents are enterprise-priced; no clean $9/mo tier exists.

---

## 3. PRD MVP

### P0 (must ship in 14 days)
- Single search box: name + company OR email OR LinkedIn URL
- Result card: email, phone (if available), company, title, source links
- 100 lookups/mo on $9 plan, 500 on $29 plan
- Stripe subscriptions
- Simple dashboard: usage meter, search history
- Auth (email + password)

### P1 (week 3-4)
- CSV export
- Bulk search (paste 50 names)
- Browser extension (read DOM, lookup highlighted text)
- API access (with API key)

### P2 (month 2+)
- CRM sync (HubSpot, Pipedrive)
- Team plans (5 seats)
- Verified email badge (SMTP check)

### Non-goals
- ❌ No enterprise SSO / SAML
- ❌ No dialer / outreach sequencing (that's Apollo territory)
- ❌ No intent data / Bombora-style signals
- ❌ No mobile app

### Tech stack
- Next.js 14 + Tailwind
- Postgres + Drizzle
- Stripe
- Data sources: Hunter.io API (reseller), Apollo API (reseller, with ToS check), public court records scrapers
- Vercel + Sentry

### Cost per lookup
- Hunter.io: $0.01/lookup (reseller margin)
- Apollo: $0.02/lookup
- Our cost: ~$0.03/lookup
- At $9/mo / 100 lookups = $0.09/lookup revenue → 3× margin

---

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Repo init, Next.js, DB schema, Stripe test mode |
| 2 | Auth, single-search UI, backend API stub |
| 3 | Hunter.io API integration, result card UI |
| 4 | Apollo API integration, dedupe across sources |
| 5 | Usage meter, dashboard, search history |
| 6 | Pricing page, Stripe webhook, plan enforcement |
| 7 | Landing page, FAQ, signup flow |
| 8 | Apollo data caching layer (24h TTL) |
| 9 | Error handling, rate limiting, Sentry |
| 10 | Beta: 10 free users from r/sales |
| 11 | CSV export, bulk search |
| 12 | Public launch on r/sales + Indie Hackers |
| 13 | X thread: "I built a $9/mo Apollo alternative" |
| 14 | First paying user; review funnel; plan P1 |

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Week | Channel | Action | Cost |
|---|---|---|---|
| 1 | Reddit | Lurk + contribute on r/sales, r/salesforce, r/recruiting | $0 |
| 1 | X | 2 posts/day on #saleslife #sdr | $0 |
| 2 | Reddit | "I built this" launch post | $0 |
| 2 | Indie Hackers | Build log post | $0 |
| 2 | SEO | 2 posts: "Apollo alternative 2026", "cheap B2B email lookup" | $0 |
| 3 | Paid | $100 Reddit ads (r/sales promoted post) | $100 |
| 3 | Partnerships | Reach out to 5 sales-coach newsletters for review | $0 |
| 4 | Paid | $100 Reddit ads + $50 X promote | $150 |
| 4 | Referral | "Refer a rep, get 1 month free" | $0 |
| **Total** | | | **$250** |

Target Week 4: 30 paying users × $9 = **$270 MRR** + some $29 upsells.

---

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Price | $9/mo (100 lookups) or $29/mo (500 lookups) |
| Blended ARPU | $14/mo |
| Gross margin | 70% (data cost $0.03/lookup, blended 30 lookups/mo = $0.90) |
| Target MRR | $10,000 |
| Required paying users | 715 |
| Monthly churn (B2B utility) | 4% |
| New users/mo to hit steady state | ~30/mo (steady) |
| Conversion (free trial → paid) | 8% |
| Free trialists needed | 375/mo from organic |
| CAC (organic) | ~$5-10 |

**Path to $10K MRR: ~12-18 months** at organic pace.
**Risk:** data ToS (Hunter/Apollo reseller limits). Mitigation: build own scrapers from public sources.

---

## 7. Kill criteria

- Week 2: < 30 beta signups → kill (no ICP-product fit)
- Week 4: < 10 paying users → kill or pivot ICP
- Week 8: churn > 8%/mo → product-market fit issue, kill
- Week 12: Hunter.io / Apollo cuts reseller access → pivot to own scrapers or kill

---

## 8. Why this is "GO" not "GO_NARROW"

Competition score is 2 (low) — Apollo/Hunter exist but price out solo reps. We don't need a narrow wedge to compete; we need clean execution. The wedge is already implicit in price ($9 vs $49).
