# Get Funneled — Funnel Repair for Service SMBs

**Tier:** GO  
**Demand:** 3/5  
**Competition:** 2/5  
**Target:** $10,000 MRR  
**MVP:** 14 days, solo  
**Marketing budget:** ≤ $300 for 30 days  

## 1. Why this direction

### TrustMRR evidence

- Get Funneled reports approximately **$191 MRR** and **$207 in last-30-day revenue**.
- Its 22 subscribers indicate real paid conversion from a relatively small audience.
- The listing appears to address a website-to-lead funnel problem, which is outcome-oriented and can be sold around recovered appointments, calls, or qualified inquiries rather than generic analytics.
- Revenue is materially larger than most non-AI SaaS products in this run, which is evidence that SMB buyers can pay for lead-generation support.
- The signal is not treated as proof of product-market fit: gross MRR, revenue quality, churn, and attribution still require verification.

### X/web evidence

- The identified X handle is `@claridgicus`.
- The supplied search run reported 12 results per query, but its stdout contained TinyFish CLI help rather than the underlying result bodies. Therefore, no unsupported quotes or social metrics are claimed.
- Observable evidence is stronger in TrustMRR revenue and subscription data than in public social discussion.
- The immediate validation hypothesis is that service-business owners have a recurring pain around low-contact-rate websites and do not want a complex marketing suite.

### Thesis

Build a narrow **funnel diagnostic and repair assistant for one service SMB segment**. It ingests a URL and a few conversion facts, detects the highest-confidence leak, generates a prioritized repair brief, and creates ready-to-publish landing-page copy plus one follow-up sequence.

The product should not attempt to replace analytics, CRM, ad platforms, and full website builders. Its promise is: **find the leak and deliver the repair in one session**.

### Initial ICP

Start with one ICP rather than “small businesses” generally:

- Independent dental, aesthetic, home-service, legal, or accounting practices would have different compliance and sales considerations.
- For the first 14-day MVP, choose **local home-service businesses**—for example, roofers, HVAC contractors, or cleaners—because leads can be attributed quickly and the workflow is easy to explain.
- Exclude regulated high-stakes diagnosis, medical treatment, and legal advice.

### Validation questions

1. Which service segment spends enough on leads but converts poorly?
2. Can a prospect grant access to a simple form, page, or pasted analytics screenshot?
3. Does the buyer trust a ranked diagnosis without a black-box score?
4. Can the recommended repair be implemented in one hour or less?
5. Would the buyer pay $49–$149/month for continuous diagnosis and repair assets?

## 2. Competitor table

### L1 — direct alternatives

| competitor | likely offer/pricing | strength | weakness / opening | evidence confidence |
|---|---|---|---|---|
| Get Funneled | Funnel-focused growth/lead-conversion product; current listing indicates approximately $191 MRR | Existing paid validation and category focus | Opportunity to specialize by ICP and deliver a more concrete repair workflow | High for revenue; medium for exact feature set |
| FunnelKit | Funnel-building and optimization suites; commonly positioned from free tiers to premium plans | Broad templates and funnel-building depth | Heavier product; opportunity for diagnosis-first workflow and service-business specialization | Medium |
| ClickFunnels | Funnel builder, commonly priced by tier | Mature ecosystem and templates | General builder rather than guided diagnosis; potentially excessive for a solo owner | Medium |
| Leadpages | Landing-page and funnel creation platform with paid plans | Strong landing-page ecosystem | Creation-heavy; may leave a non-technical owner without diagnosis and repair priorities | Medium |
| ThriveCart | Checkout/cart and funnel tooling for established offers | Commerce strength | Not a lightweight lead-repair assistant; broader scope | Medium |

### L2 — adjacent substitutes

| competitor/substitute | why buyers use it | opportunity |
|---|---|---|
| Google Analytics / GA4 | Diagnose traffic and conversion behavior | Complex analysis and weak implementation guidance |
| Hotjar | Session recordings and feedback | High setup effort and no prioritized repair workflow |
| HubSpot / Pipedrive | Capture and manage leads | CRM overhead before a website problem is diagnosed |
| Agency or freelancer | Diagnose and implement conversion work | Cost and latency; useful for high-value or complex accounts |
| DIY templates | Repair landing pages manually | No tailored diagnosis; templates can feel generic |

### L3 — low-end alternatives

| alternative | weakness |
|---|---|
| Copywriting templates | No diagnosis or implementation sequence |
| Static landing-page builders | Faster production but not ongoing funnel diagnosis |
| ChatGPT/manual review | Inconsistent inputs, no account history, and no structured prioritization |
| Spreadsheet audits | Laborious, weak prioritization, difficult to repeat |

### Competition conclusion

**Score: 2/5.** Funnel tools are numerous, but the narrow combination of **one service vertical + diagnosis + prioritized repair assets** creates a focused wedge. The market is not empty; validation must show a buyer prefers this workflow to a builder, agency, or general analytics workflow.

## 3. PRD MVP

### Target outcome

A service-business owner can submit a URL plus a short qualification form and receive:

1. A funnel health summary with at most three issues.
2. A prioritized 24-hour repair plan.
3. A revised headline, CTA, proof block, and objection-handling copy.
4. One short SMS/email follow-up sequence.
5. A downloadable action checklist.

### P0 — required for launch

- URL and business-input form:
  - website URL;
  - service type;
  - target customer;
  - primary conversion goal;
  - monthly visitor range, optionally entered manually;
  - current inquiry volume, optionally entered manually.
- URL ingestion and page-text extraction.
- Rule-based diagnostic checks:
  - unclear or generic value proposition;
  - weak or missing CTA;
  - missing trust/proof elements;
  - no objection handling;
  - form friction or missing contact options;
  - missing qualification fields.
- Ranked diagnostic report with evidence excerpts from the page.
- Repair brief prioritizing P0, P1, and P2 actions.
- Copy generator for the page’s primary conversion block.
- Follow-up sequence generator for email and SMS-style copy.
- Export to PDF and copyable text.
- Authentication and account pages.
- Usage limits and billing integration.
- Source attribution and “generated draft—review before publishing” warning.
- Analytics events for submitted URL, report generated, report viewed, copy copied, export, and upgrade clicked.

### P1 — after initial validation

- Scheduled monthly re-scan.
- Before/after page comparison.
- Template library by service vertical.
- CSV import of leads and optional CRM connection.
- Saved benchmarks by vertical.
- Team sharing with roles.

### P2 — later expansion

- Multi-page journeys.
- Ad-to-page message-match analysis.
- A/B test planner and result interpretation.
- Agency white-label reporting.
- Additional vertical-specific benchmarks.

### Non-goals

- No general-purpose analytics platform.
- No replacement for GA4, HubSpot, Pipedrive, or an ad platform.
- No autonomous website editing in the MVP.
- No guaranteed lead or revenue claims.
- No paid ad-management integration.
- No enterprise integrations.
- No broad all-industry knowledge base before one vertical is validated.
- No mass outreach or automated spam.

### MVP user story

> As a home-service business owner, I can submit my website and receive a prioritized repair brief with usable copy so that I can improve lead conversion without learning analytics or hiring an agency.

### Technical approach

- Next.js or a similarly simple authenticated web application.
- Backend: TypeScript service with PostgreSQL and a simple job queue.
- Extraction: server-side fetch plus readability-style HTML extraction, with safety controls against private/internal addresses.
- Initial diagnosis: deterministic checks before any model call.
- Generation: a structured prompt that uses only extracted evidence and owner-provided facts.
- Output schema: issue, evidence, confidence, impact hypothesis, repair instruction, and generated asset.
- Billing: Stripe checkout and webhook-driven entitlements.
- Deployment: one lightweight application stack; no microservices.

### Pricing hypothesis

- **Free diagnostic:** one URL, limited issues.
- **Starter:** $49/month, one site, monthly rescans, exportable repair assets.
- **Growth:** $99/month, five sites, competitor comparison, monthly action plan.
- **Agency:** $199/month for ten client sites and white-label PDF export.

Pricing should not be final until five prospects are shown the sample report and asked to choose a plan.

## 4. 14-day day-by-day build plan

| Day | objective | deliverables | acceptance test |
|---:|---|---|---|
| 1 | Validate vertical and message | Select home services as initial ICP; write 15 interview questions; draft sample report using 3 public service sites | Three distinct report examples expose a clear, ranked diagnosis |
| 2 | Clickable prototype | Landing page, intake form, sample report, pricing outline, and checkout mock | A stranger can complete the flow without help |
| 3 | Five buyer interviews | Test existing alternatives, recent lead loss, and willingness to pay | At least 3 of 5 confirm a recent problem; collect 2 permissioned URLs or screenshots |
| 4 | Extraction spike | Fetch and safely parse title, headings, CTA, forms, proof, and page text | 10/10 test pages produce structured fields without manual editing |
| 5 | Deterministic diagnostics | Implement six checks with evidence, severity, confidence, and priority | Each check has positive and negative fixtures and deterministic output |
| 6 | Report generation | Create issue summary, repair brief, page-copy prompt, and structured response | Report never invents facts and cites source excerpts |
| 7 | Authentication and persistence | Signup/login, account, report list, source URLs, saved output | User can revisit and export a prior report |
| 8 | Billing and limits | Stripe checkout, webhooks, plan limits, free quota | Successful payment unlocks access; failed/cancelled state behaves correctly |
| 9 | Report UX | Improve evidence display, fix ordering, copy/export, mobile layout | Five usability sessions complete without facilitator assistance |
| 10 | Repair assets | Add headline, CTA, proof block, objection copy, email, and SMS generator | Assets cite the diagnosed issue and are editable |
| 11 | Reliability and safety | SSRF protection, retries, prompt-injection filtering, URL validation, error monitoring | Malicious/private URLs are rejected and no source instruction is executed |
| 12 | Pilot conversion | Add monitoring, invite 10 prospects, activate founder-assisted reports | At least 3 complete a report and 2 click a paid plan |
| 13 | Pricing and onboarding | Add checkout, onboarding email, sample report, FAQ, refund policy | New user can go from URL to report without founder help |
| 14 | Release | Fix blockers, deploy, record demo, publish SEO pages, launch founder outreach | 99% job success, no P0 bugs, and first paid conversion is available |

### Solo-build controls

- Use one deployment stack and one billing provider.
- Do not implement scheduled rescans before launch.
- Use deterministic checks before AI to control cost and improve trust.
- Cap daily report generation per account.
- Use the first ten users manually to identify issues.

## 5. 30-day marketing calendar

### Budget

| channel | 30-day spend |
|---|---:|
| Micro-influencer/creator seeding or small paid boosts | $120 |
| Search-intent content production and one small sponsored post | $60 |
| Tooling, domain, and creative snippets | $30 |
| Incentives for customer interviews/demo referrals | $90 |
| **Total** | **$300** |

### Calendar

| day | activity | organic action | paid action | KPI |
|---:|---|---|---:|---|
| 1 | Publish landing page | Homepage and sample report | None | 200 qualified visits |
| 2 | Founder post | Personal LinkedIn pain story | None | 10 replies or 3 calls |
| 3 | Publish case study | Before/after diagnostic from a sample site | None | 30 report views |
| 4 | Interview outreach | Contact 15 home-service owners | None | 5 interviews |
| 5 | Short demo | Record 60-second workflow clip | None | 25% landing-to-start rate |
| 6 | ICP landing page | Publish HVAC/roofing-specific variant | None | 15 qualified signups |
| 7 | Review | Fix conversion and onboarding friction | None | 8 activated reports |
| 8 | Partner outreach | Pitch 10 local marketing agencies | None | 2 calls |
| 9 | Educational post | “Five website leaks costing service leads” | None | 2 sales conversations |
| 10 | Agency pilot | Offer white-label report pilot | None | 1 paid agency pilot |
| 11 | Customer voice | Publish one anonymized result | None | 3 trial-to-paid conversions |
| 12 | Local outreach | Comment on agency and contractor groups with useful checklists | None | 20 inbound conversations |
| 13 | Retention review | Interview first paid users | None | 70% weekly active usage |
| 14 | Product iteration | Implement top reported friction | None | Time-to-report under 3 minutes |
| 15 | Comparison content | Publish alternatives page: GA4, agency, DIY | $20 post | 30 landing visits |
| 16 | Creator seeding | Send tool to 10 micro-creators | $60 | 3 creator posts |
| 17 | Live demo | Host a 30-minute funnel audit session | None | 10 registrants |
| 18 | Template launch | Publish one vertical-specific repair pack | None | 40 downloads |
| 19 | Review | Diagnose onboarding drop-off | None | 60% report completion |
| 20 | Founder outreach | Send 25 tailored examples to service firms | None | 10% positive reply |
| 21 | Referral prompt | Ask successful users to refer one peer | $25 incentive | 5 qualified referrals |
| 22 | Localized SEO | Publish city/service landing pages for two markets | None | 20 organic visits |
| 23 | Founder post | Publish transparent build log and failure lessons | None | 5 sales calls |
| 24 | Paid test | Promote best-performing demo | $35 | CAC and activation by source |
| 25 | User interview | Interview five paid or trial users | None | One dominant reason to cancel |
| 26 | Pricing test | Test $49/$79/$99 landing-page plans | None | Checkout conversion |
| 27 | Customer proof | Publish quote and quantified result | None | 3 paid conversions |
| 28 | Channel review | Pause channels with no qualified trials | None | CAC below $60 |
| 29 | Automation | Add onboarding and report-summary email sequence | None | 35% reply rate |
| 30 | Monthly review | Reconcile MRR, churn, support, acquisition | $5 boost | 8+ paid accounts or clear pivot evidence |

### Organic-first content pillars

- “Why service leads leave your website.”
- Free mini audits of public local-business websites.
- Before/after landing-page examples.
- Founder build-in-public posts.
- Comparison pages against analytics, templates, and agencies.
- Short checklists for contractors, cleaners, and clinics.

## 6. Unit economics to $10K MRR

### Target mix

| plan | price | customers | MRR |
|---|---:|---:|---:|
| Starter | $49 | 100 | $4,900 |
| Growth | $99 | 45 | $4,455 |
| Agency | $199 | 5 | $995 |
| **Total** |  | **150** | **$10,350** |

### Cost model

Assume:

- Blended report generation and extraction cost: **$1.20/report**.
- Reports per customer per month: **3**.
- Payment and infrastructure cost: **3% of revenue**.
- Support/retention allowance: **$8/customer/month**.
- Fixed solo operating cost: **$1,500/month** before founder salary.

At 150 customers:

- Revenue: **$10,350/month**.
- Variable AI/inference cost: approximately **$540/month**.
- Payment/infrastructure: approximately **$311/month**.
- Support allowance: approximately **$1,200/month**.
- Contribution before fixed cost: approximately **$8,299/month**.
- After $1,500 fixed cost: approximately **$6,799/month** before taxes and founder compensation.

### CAC and payback assumptions

- Organic-first blended CAC target: **≤ $75**.
- Gross-margin-adjusted CAC payback: under one month at Starter/Growth pricing.
- 30-day marketing budget supports the first 3–5 customers, not the full scale-up.
- Scaling to 150 customers likely requires partnerships, a marketplace, an agency channel, or additional founder-led outbound; this must be tested rather than assumed.

### Sensitivity

- At 100 customers and $75 average MRR, MRR is $7,500.
- At 150 customers and $69 average MRR, MRR is $10,350.
- At 200 customers and $50 average MRR, MRR is $10,000.
- If gross margin falls below 70%, pricing or usage limits must change before scaling.
- If monthly logo churn exceeds 8%, the product is not reaching $10K sustainably.

## 7. Kill criteria

Pause or kill the direction if any of the following occurs:

1. Fewer than 2 of 10 interviewed ICP owners report a recent, material lead-conversion problem.
2. No prospect agrees to receive a free diagnostic for a real website.
3. Fewer than 30% of sample reports are rated “useful” or “very useful.”
4. No one commits to a paid pilot after the report is delivered.
5. After 30 days, fewer than 5 paid accounts or fewer than 2 agency/consultant referrals.
6. Blended CAC exceeds $150 for an account whose first-year gross profit is below $300.
7. Median time-to-value exceeds 10 minutes.
8. Report output repeatedly invents claims or requires extensive manual correction.
9. Retention is below 70% after the first 30 days of paid use.
10. The product requires integrations or a custom onboarding process that prevents same-day activation.

### Decision checkpoints

- **Day 3:** continue only with at least three pain confirmations and two permissioned sites.
- **Day 7:** continue only if reports produce actionable issues and users request fixes.
- **Day 14:** continue only if the end-to-end product works and at least one paid conversion is possible.
- **Day 30:** scale only if retention and acquisition support a credible path to $10K MRR.
