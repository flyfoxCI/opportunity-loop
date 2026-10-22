# Contractor Lead Radar — Local Lead Alerts for One Trade

## 1. Why this direction

### TrustMRR evidence

The prior validated direction pack cites **NextjobConnect at approximately $5K MRR** as evidence that contractor-focused AI lead generation can monetize. The same research characterizes many players as early-stage rather than mature, while the category still requires buyers to move from vague inquiries to qualified, contactable demand.

The narrow MVP is:

- one trade: residential HVAC;
- one geography: one metropolitan area;
- one lead format: public permit/building signals enriched with business and contact context;
- one action: review and claim a qualified alert.

This avoids building a nationwide directory, cold-call system, CRM, marketplace, and automation suite at once.

### X and web evidence

The Stage A TinyFish payloads returned only CLI help text and therefore do not constitute social demand verification.

Run and archive genuine results for:

- `HVAC leads (expensive OR useless OR spam OR "looking for")`
- `("HVAC lead service" OR "contractor leads") review`
- `("home service leads" OR "HVAC leads") (Reddit OR X)`
- `"just shipped" HVAC lead software`
- `contractor "competitor hate" leads`

A valid social handle should be added only with a post URL, date, pain quote, and product/category relevance. Until then, use contractor Facebook groups, trade associations, public contractor forums, and 15 direct interviews for primary evidence.

### Customer and promise

**ICP:** owner-operators or small HVAC sales teams that currently depend on ads, marketplaces, referrals, or purchased lists.

**Promise:** Receive a short weekly list of locally verifiable HVAC opportunities with source evidence, dedupe status, and a clear confidence level.

## 2. Competitor table

Verify all pricing during Week 1. Many competitors use undisclosed quote-based pricing.

| Level | Competitor or substitute | Typical pricing model | Strength | Opening for this product |
|---|---|---:|---|---|
| L1 direct | HVAC-specific lead vendors | Often $300–$1,500+/month or per lead | Pre-sold inventory and local relationships | Transparent methodology, exclusive verified signals, contractor control |
| L1 direct | Local contractor lead marketplaces | Subscription, pay-per-lead, or auction | Large existing supply and easy discovery | Complement rather than compete with high-ticket aggregators |
| L1 direct | Permit-data resellers | $50–$500+/month depending on coverage | Rich public records | HVAC interpretation, deduplication, and action ranking |
| L2 adjacent | Generic agencies and lead brokers | Project or retainer pricing | Human curation and local sales | Automated repeatability and lower minimum order |
| L2 adjacent | Google Local Services, Angi, Thumbtack, and Nextdoor | Pay-per-lead or advertising | Existing demand and trust | First-party opportunity and account intelligence |
| L2 adjacent | CRM automation vendors | $30–$100+/seat/month | Workflow integration | Better top-of-funnel opportunity signal |
| L3 substitute | Yelp, Google search, and referrals | Often free or performance-based | Familiar and trusted | Concise alerting and source transparency |
| L3 substitute | Spreadsheet/scraping workflows | Tooling cost only | Flexible | Maintained data, quality labels, and no-code review |

**Competitive score:** 4/5. The category has meaningful providers, so the direction is **GO_NARROW**.

## 3. PRD MVP

### P0 — required for launch

1. **Service-area configuration**
   - trade fixed to HVAC;
   - postal-code list;
   - target residential/commercial mix.
2. **Signal ingestion**
   - one or two public source types;
   - source URL and retrieval timestamp;
   - jurisdiction and licensing context where available.
3. **Entity resolution**
   - company normalization;
   - deduplication;
   - prior-seen status.
4. **Qualification**
   - service-type match;
   - location match;
   - recency;
   - confidence and evidence.
5. **Lead feed**
   - claim;
   - hide;
   - annotate;
   - export;
   - “not relevant” feedback.
6. **Usage and billing**
   - Stripe;
   - 14-day trial;
   - fair-use limits;
   - self-serve cancellation.
7. **Compliance controls**
   - terms review;
   - source licensing;
   - no bypass of logins or anti-bot controls;
   - contact details only from lawful public sources;
   - no automated calling or texting.

### P1 — after validation

- more permit types;
- technician capacity and territory rules;
- CRM export;
- customer contact enrichment;
- weekly digest;
- team permissions;
- source-specific precision reports.

### P2 — later

- additional trades;
- nationwide coverage;
- automated outreach with explicit opt-in;
- contractor collaboration;
- appointment scheduling;
- AI call summaries;
- reputation and review integrations.

### Non-goals

- guaranteed jobs or revenue;
- nationwide coverage at launch;
- every contractor trade;
- brokered lead sales in MVP;
- automated cold calls or spam;
- bypass of platforms or access controls;
- private or non-public data;
- replacement for a CRM, scheduler, or marketing agency;
- unverifiable “AI score” without evidence.

## 4. 14-day day-by-day build plan

| Day | Solo deliverable |
|---:|---|
| 1 | Interview 5 HVAC owners about current lead sources, losses, geography, and qualification criteria. |
| 2 | Interview 5 more; select one metro and one signal type; manually assemble 20 sample opportunities. |
| 3 | Ask five prospects to rank and explain the sample; define confidence labels and exclusions. |
| 4 | Build auth, database, billing skeleton, service-area configuration, and source adapters. |
| 5 | Add entity normalization, deduplication, source URL, timestamps, and raw-record snapshots. |
| 6 | Add deterministic qualification rules plus model-assisted categorization with citations. |
| 7 | Build claim/hide/export/annotate feed, feedback capture, and audit history. |
| 8 | Add Stripe, trial, limits, cancellation, admin controls, and usage metering. |
| 9 | Complete compliance review, privacy terms, source-attribution display, and deletion workflow. |
| 10 | Run source failures, duplicate, stale-data, and provider outage tests. |
| 11 | Deliver 20 concierge weekly alerts manually and observe contractor behavior. |
| 12 | Fix relevance and UX based on at least eight users; add quality dashboard. |
| 13 | Close five paid design-partner accounts or collect explicit no-go decisions. |
| 14 | Ship only if precision, compliance, and willingness-to-pay criteria pass; otherwise pivot the signal or kill. |

## 5. 30-day marketing calendar

**Budget cap:** $250, including a small contractor-community sponsorship test.

| Day/channel | Action | Budget |
|---|---|---:|
| 1–3 | Publish one-page offer with real sample signals and transparent methodology | $0 |
| 4 | Interview prospects about “leads I paid for but could not use” | $0 |
| 5 | Post a sanitized sample feed in relevant HVAC groups | $0 |
| 6 | Personally deliver a free HVAC permit/opportunity audit | $0 |
| 7 | Publish source-by-source quality comparison | $0 |
| 8 | Run a live teardown of ten sample records | $0 |
| 9 | Contact five local HVAC associations or trainers | $0 |
| 10 | Ask every activated user to label relevance | $0 |
| 11 | Add the strongest user quote to landing page | $0 |
| 12 | Launch a $75 local newsletter sponsorship | $75 |
| 13 | Onboard every trial manually | $0 |
| 14 | Review precision, claims, and feedback by source | $0 |
| 15 | Publish “why cheap HVAC leads are expensive” with measurable examples | $0 |
| 16 | Approach ten owner-operators with a personalized source audit | $0 |
| 17 | Add source freshness and confidence explanations | $0 |
| 18 | Seek a contractor-community or vendor partnership | $0 |
| 19 | Request case study from first paying account | $0 |
| 20 | Review false positives and complaints | $0 |
| 21 | Contact prior design partners who did not convert | $0 |
| 22 | Publish weekly aggregate signal report | $0 |
| 23 | Test a $99 starter plan against a $199 quality plan | $0 |
| 24 | Build referral loop for contractors | $0 |
| 25 | Run a second source-quality teardown | $0 |
| 26 | Close ten qualified personal outreach conversations | $0 |
| 27 | Restrict geography or source if economics fail | $0 |
| 28 | Publish compliance and sourcing policy | $0 |
| 29 | Review retention, lead usefulness, support load, and margins | $0 |
| 30 | Make continue/narrow/kill decision | $0 |

## 6. Unit economics to $10K MRR

### Pricing hypothesis

- Local: **$149/month**
- Pro territory: **$299/month**
- small team: **$499/month for 5 users**

Average realized ARPU assumption: **$220/month**.

### Cost and margin

| Metric | Assumption |
|---|---:|
| Data acquisition/API allocation | $25/customer/month |
| Enrichment and infrastructure | $20 |
| Support and operations | $15 |
| Payments and overhead allocation | $10 |
| Contribution/customer/month | about $150 |

Target gross margin: approximately 82%.

### Customers required

- $10K MRR / $220 ARPU = **46 customers**.
- At 5% monthly churn, gross additions must exceed roughly 2.3 customers per month to hold a 46-customer base.
- Early target: 3–5 HVAC firms in one metro area, then expand only after precision is proven.

### CAC and payback

Assumptions:

- founder-led outreach CAC: $150–$250;
- referral CAC: $75–$150;
- paid CAC may exceed $400;
- contribution: $150/month;
- paid CAC payback at $250 CAC: 1.7 months.

Do not scale paid acquisition until qualified-opportunity rate, source licensing, and user retention are established.

## 7. Kill criteria

Kill or re-niche if any occur by Day 30:

- fewer than 20 qualified HVAC interviews;
- fewer than 10 users inspect sample signals;
- fewer than 4 pay;
- fewer than 3 report the feed as useful in the next four weeks;
- fewer than 40% of delivered opportunities pass user relevance review;
- no source can be used lawfully and economically at launch;
- median customer records reviewed per week is too low to justify price;
- each customer requires manual data repair beyond 20 minutes weekly;
- gross margin falls below 70%;
- the product depends on scraped personal data or access-control circumvention;
- users primarily demand guaranteed jobs or managed appointment setting rather than qualified signals.

## Wedge (required for GO_NARROW)

**Refuse to build:**

- every trade at launch;
- nationwide coverage before local retention;
- guaranteed leads or appointment outcomes;
- lead brokerage;
- automated cold calling, texting, or email;
- private databases;
- scraping behind logins or bypassing platform controls;
- replacement CRM, scheduler, website, or ads platform;
- AI scores without visible evidence.

The MVP covers **one HVAC trade in one metropolitan area**, uses **publicly and lawfully accessible building or permit signals**, and delivers **evidenced alerts only**.
