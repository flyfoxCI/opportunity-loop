# Contractor Lead Radar

## Why this direction

### TrustMRR evidence

- The prior validated direction index cites **NextjobConnect at approximately $5K MRR**, supporting real willingness to pay for contractor-focused lead generation.
- The broader opportunity is not empty, so this is not positioned as a pure full-market GO. It is a **GO_NARROW** with competition score 4.
- The narrow wedge is one trade in one geography rather than “AI leads for contractors” in general.
- A solo MVP can deliver value by monitoring public job and permit sources, normalizing listings, qualifying them, and alerting a contractor by email or SMS. It does not need autonomous sales outreach in the first release.

### X/web evidence

- Contractors complain that generic lead services send irrelevant, duplicated, or low-intent leads and that paying per lead feels risky.
- Searches should target a selected trade, such as:
  - `contractor leads exhausted`
  - `HVAC lead service too expensive`
  - `roofing leads not worth it`
  - `electrician job leads spam`
  - `contractor leads just shipped`
- Local Facebook contractor groups, trade forums, Reddit trade communities, and home-service communities provide channels for demand discovery, but they also reveal incumbent lead brokers and marketplaces.
- The strongest opening is therefore not more lead volume; it is **cleaner local lead intelligence with transparent source attribution**.

## Competitor table

| Level | Product | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | NextjobConnect | Contractor-oriented lead/job discovery and outreach | Around $5K MRR listing; verify plan pricing | Closest commercial proof |
| L1 | Thumbtack | Local home-service marketplace and lead generation | Lead/contractor pricing varies | Major marketplace and lead source |
| L1 | Angi | Home-service marketplace | Subscription plus lead/enhancement pricing | Large incumbent with broad category coverage |
| L1 | Houzz | Home-services discovery and leads | Freemium plus marketing products | Strong marketplace and CRM alternative |
| L1 | Porch | Home-services marketplace | Marketplace and provider products | Adjacent incumbent |
| L2 | Modernize | Home-improvement lead generation | Vendor and buyer pricing varies | Focused lead marketplace |
| L2 | HomeRun | Home-improvement lead marketplace | Subscription/lead pricing | Direct category competitor |
| L2 |247 Quotes, lead brokers | HVAC, roofing, and remodeling lead networks | Per-lead or monthly plans | Crowded broker category |
| L3 | Google Business Profile, Local Services Ads, Facebook groups | Free discovery and lead channels | CPC/ad spend | Free and highly effective substitutes |

### Competitive conclusion

Competition score is 4. The product must not enter as another general contractor lead broker. Its explicit wedge is **one trade, one service area, source-attributed public leads, and no cold calling without approval**.

## Wedge

### Narrow scope

- Choose exactly one trade, such as HVAC repair.
- Choose one metropolitan service area.
- Monitor only a small set of legal, useful signals such as:
  - public permit applications
  - service-request posts in permitted community groups
  - public company job postings indicating expansion
  - selected marketplace listings, where terms permit
- Return a weekly ranked list with source, recency, location, urgency indicators, and evidence.
- Let the contractor approve an outreach draft; do not auto-send messages.

### What this product refuses to build

- No support for multiple trades in the MVP
- No nationwide coverage
- No general-purpose CRM
- No automated cold calling or mass texting
- No scraped or repackaged lead resale
- No invented lead scoring without visible evidence
- No guaranteed-job or guaranteed-revenue claims
- No consumer finance, lending, insurance, or contracting recommendations
- No general-purpose consumer home-improvement marketplace

### Why the wedge can work

- A local vertical improves relevance and source quality.
- Concentration reduces data-provider cost and integration complexity.
- Manual review and source links can produce trust before automation.
- One trade gives the product a recognizable identity and enables concentrated outreach.

## PRD MVP

### Target customer

Owner-operator or small sales manager in one selected home-service trade, ideally with 2–20 sales staff.

### Primary outcome

Receive a manageable, evidence-backed weekly lead/opportunity list without paying for opaque, duplicated leads.

### P0

- Select trade and service-area configuration
- User signup and account
- Source adapter framework for at least two signal types
- Source attribution:
  - original URL
  - timestamp
  - text excerpt
  - location
  - confidence/status
- Manual review queue
- Deduplication
- Basic qualification fields:
  - trade relevance
  - geography
  - recency
  - evidence keyword
  - estimated urgency
- Weekly digest by email
- Optional daily urgent-alert email
- User feedback:
  - relevant
  - not relevant
  - contacted
  - won
  - lost
- CSV export
- Stripe subscription and plan limits
- Source-policy and prohibited-use documentation

### P1

- SMS digest
- CRM push for Zapier
- Saved searches
- Custom qualification rules
- Opportunity history and outcome analytics
- Team assignment
- Source-health reporting

### P2

- Bid/estimate integrations
- Automated outreach
- More trades and regions
- Phone enrichment
- Pipeline forecasting
- Marketplace listing

### Non-goals

- No homeowner marketplace
- No contractor directory
- No full CRM
- No mortgage, insurance, or financing products
- No unverifiable “exclusive” lead claims
- No mass-scraped directories
- No initial native mobile app

### Technical approach

- Web app and scheduled ingestion workers
- PostgreSQL for opportunities, users, and feedback
- Object storage for source snapshots where lawful and permitted
- Rule-based classification first; ML only where language volume justifies it
- Links to original evidence
- Human-review dashboard
- Idempotent adapters and deduplication hashes
- Usage-based data/API budget caps
- Privacy, retention, and deletion policies

### Pricing

- **Solo:** $49/month, one area, 25 reviewed opportunities/month
- **Pro:** $149/month, one area, 100 opportunities, multiple users
- **Pilot:** $299/month with concierge source curation during the first 20 customers

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|---|
| 1 | Select trade and metro area | One trade, one geography, and 10 source samples chosen |
| 2 | Interview 15 local contractors | One recurring lead-quality problem confirmed |
| 3 | Legal/source-policy review and adapter design | Each source has documented access and use constraints |
| 4 | Ingestion and normalization prototype | Ten records captured with evidence |
| 5 | Deduplication and relevance rules | Duplicate and out-of-area records rejected |
| 6 | Opportunity review queue | User can inspect, approve, reject, and annotate records |
| 7 | Weekly email digest | Digest includes source links and actionable fields |
| 8 | Feedback capture | Relevant/contacted/won/lost states work end to end |
| 9 | Urgent-alert workflow | One test alert is sent within five minutes |
| 10 | Signup, Stripe billing, and plan limits | Purchase and quota enforcement work |
| 11 | CSV export and outcome analytics | User can export and view simple conversion metrics |
| 12 | Onboarding and empty-state UX | A new user configures a niche in under ten minutes |
| 13 | QA, source failure handling, and cost caps | Broken adapters fail safely without misleading records |
| 14 | Pilot launch | Five local design partners receive reviewed opportunities |

## 30-day marketing calendar

**Budget: $200 maximum**

| Day | Activity | Budget | KPI |
|---:|---|---:|---|
| 1 | Publish trade-and-city-specific landing page | $0 | 75 local targeted visits |
| 2 | Post a sample anonymized opportunity digest | $0 | 10 contractor replies |
| 3 | Visit 20 local contractor websites | $0 | 15 qualified contacts |
| 4 | Send a personal comparison email | $0 | 5 replies |
| 5 | Publish “why this lead is qualified” example | $0 | 8 demo requests |
| 6 | Hold a 20-minute contractor workflow session | $0 | 8 attendees |
| 7 | Onboard five pilot contractors | $0 | 5 activated accounts |
| 8 | Ask pilots for source-quality feedback | $0 | 10 corrections |
| 9 | Publish a fixed-up delivery-process post | $0 | 10 qualified leads |
| 10 | Contact local trade associations | $0 | 3 conversations |
| 11 | Publish weekly-digest video | $0 | 100 targeted views |
| 12 | Ask five pilot customers for referrals | $0 | 4 referrals |
| 13 | Review opportunity relevance rate | $0 | ≥70% “relevant” |
| 14 | Audit source compliance | $0 | No unresolved violations |
| 15 | Add one permitted source only if needed | $0 | Stable ingestion |
| 16 | Publish anonymized outcome data | $0 | 6 qualified leads |
| 17 | Contact 20 complementary local vendors | $0 | 10 replies |
| 18 | Create a contractor Facebook-group educational post | $0 | 15 comments |
| 19 | Host a lead-quality clinic | $0 | 10 attendees |
| 20 | Review first-week usage and feedback | $0 | 60% weekly-open rate |
| 21 | Ask customers which fields they actually use | $0 | Top 3 fields identified |
| 22 | Publish contractor-specific FAQ | $0 | 8 trials |
| 23 | Contact three agency/consulting partners | $0 | 2 partner conversations |
| 24 | Ask pilots to quantify contacted/won outcomes | $0 | 5 outcome records |
| 25 | Improve scoring using feedback | $0 | Relevant rate ≥80% |
| 26 | Request paid conversion from active pilots | $0 | 3 paid accounts |
| 27 | Publish a “source transparency” case study | $0 | 10 qualified leads |
| 28 | Run a local contractor referral challenge | $0 | 5 referrals |
| 29 | Optimize pricing and onboarding | $0 | Trial-to-paid ≥10% |
| 30 | Review MRR, retention, data risk, and support load | $0 | Continue/iterate decision |

Budget allocation: $150 narrowly targeted local sponsorship, $50 outreach/design tools, $0 contingency.

### Organic channels

- Direct contractor outreach
- Local trade associations and supplier-referral networks
- Facebook contractor groups with permission
- Local SEO for “[trade] leads in [city]”
- Partner with complementary services such as inspectors or equipment suppliers
- Public sample digests that demonstrate evidence quality

## Unit economics to $10K MRR

### Base case

- Blended ARPA: $149/month
- Customers required:  
  `10,000 / 149 = 68`
- Alternative: 60 Pro customers at $149 plus 12 Solo customers at $49 = $9,528; add 3 Pro customers to exceed $10K

### Funnel

- 2,000 qualified local leads over 90 days
- 20% activate a pilot: 400
- 17% of activated users pay: 68
- Need sustained weekly engagement because this product delivers recurring intelligence, not a one-time artifact

### Cost assumptions

- Source/API and data storage: $10–$30 per customer/month
- Email/SMS and hosting: $5–$15 per customer/month
- Manual review and support: target under 20 minutes per customer/month
- Gross margin target: ≥70%
- If a source charges materially more than $40 per active customer, remove it or raise pricing

### $10K MRR mix

- 55 Pro customers at $149 = $8,195
- 15 Solo customers at $49 = $735
- 7 Pilot/Pro customers at $149 = $1,043
- Total: 77 customers and $9,973; one additional customer exceeds $10K

### Guardrails

- Never promise exclusive leads unless contractually verified.
- Track relevance and contact rate, not only MRR.
- Keep all outreach manual or user-approved in the MVP.
- Do not expand geography before the first area demonstrates retention.
- Avoid paid ad scale until one local channel shows positive contribution margin.

## Kill criteria

Kill or reposition if any of the following occurs by day 30:

- Fewer than five of 15 contractors agree that lead quality is a top-three monthly problem.
- Fewer than three pilots agree to pay at least $99/month.
- Less than 60% of delivered opportunities are rated relevant.
- Fewer than 40% of retained users open at least three of four weekly digests.
- A required source violates terms, cannot be used lawfully, or costs more than $40 per customer monthly.
- Manual review consumes more than 30 minutes per customer weekly.
- No outcome feedback is recorded for at least 30% of pilot opportunities.
- The same generic lead appears in more than 10% of weekly digests.
- Lead volume is too low to make the plan valuable at $149/month.
- The product requires a sales team, national coverage, or cold outreach before reaching repeatability.
