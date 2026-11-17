---
layout: post
title: "JobRadar — Contractor Lead Qualification"
date: 2026-11-17T00:39:25+00:00
week: "2026-11-17_003925"
week_date: "2026-11-17T00:39:25+00:00"
slug: "jobradar-contractor-leads"
permalink: /directions/jobradar-contractor-leads.html
tags:
  - "AI"
  - "B2B"
  - "mobile"
excerpt: "Rank and qualify local contractor leads from public job-board data without replacing the contractor’s existing sales process."
---

**Tier:** GO  
**Demand:** 4/5  
**Competition:** 3/5  
**Target:** $10,000 MRR  
**MVP window:** 14 days, solo  
**30-day marketing budget:** ≤ $300

## Why this direction

### TrustMRR evidence

The prior opportunity research identifies contractor AI lead generation as a validated but still early market. NextjobConnect was documented at approximately $5,000 MRR, while competing contractor-market products showed that buyers will pay for lead-related outcomes. That is meaningful revenue evidence for a narrow, outcome-based product, although it does not prove that the exact MVP below will convert.

The economics are favorable:

- A contractor can justify $100–$300 per month if the tool helps turn a small number of overlooked jobs into booked work.
- A $149 plan needs about 68 paying contractors to reach $10,000 MRR.
- A $249 plan needs about 41 paying contractors.
- The initial product can remain useful without replacing a CRM, booking system, or lead marketplace.

### X/web evidence

Relevant communities and workflows include contractor and trade groups, home-service marketing discussions, and complaints about slow lead response, scattered lead sources, inconsistent qualification, and difficulty knowing which opportunity deserves a callback. The recurring job-board signals imply a persistent pool of public demand, but the MVP must avoid scraping any source whose terms prohibit it.

Evidence to validate before implementation:

1. Interview at least 10 contractors across one trade.
2. Confirm which sources they legally use and which are already automated.
3. Confirm that speed-to-lead and qualification matter more to buyers than another generic CRM.
4. Recruit three pilot users willing to provide feedback and weekly opportunities.
5. Manually test a daily lead brief before automating the workflow.

### Product thesis

Contractors do not need another lead database. They need a dependable daily answer to:

> “Which available jobs should I call first, and why?”

JobRadar collects permitted public job-posting data, deduplicates and normalizes listings, scores them against a contractor’s trade, service area, minimum project value, and recent work capacity, then produces a ranked callback brief.

## Competitor table

| Level | Competitor | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Thumbtack | Consumer request marketplace with contractor leads | Free listing/promotion model plus lead or advertising economics | Strong incumbent, but requests differ from persistent public job listings and generally require marketplace participation. |
| L1 | Angi | Home-services marketplace | Subscription leads and advertising; pricing varies by market and category | Trust and coverage are advantages, but the product is marketplace-centered rather than a neutral qualification workspace. |
| L1 | Houzz | Home-design and home-services marketplace | Advertising and premium leads; pricing varies | Broad home-services demand, but not focused on ranking public job opportunities. |
| L1 | BuildZoom | Construction lead platform | Subscription pricing varies by product and market | Direct competitor for contractor opportunities; differentiation must be faster setup, narrower workflow, or better transparent ranking. |
| L1 | ConstructionJobs / ZipRecruiter / Indeed | Job boards and marketplaces | Free postings, subscriptions, and paid placement | Sources of demand rather than qualification tools; some protected or automated workflows make naive mirroring unattractive. |
| L2 | Jobber / ServiceTitan / Housecall Pro | CRM and field-service platforms | Commonly $50–$300+ per month depending on users, add-ons, and market | Strong workflow incumbents; an opportunity exists when they do not capture the user’s external job-board opportunities. |
| L2 | Local business directories and lead-aggregator tools | Directory visibility and appointment leads | Usually $50–$500+ per month | Adjacent rather than identical, but easy for buyers to compare against. |
| L3 | Spreadsheet + saved searches + notification tools | Manual qualification workflow | $0–$30 per month | A meaningful low-cost substitute. JobRadar must prove it saves meaningful time and improves qualification, not merely sends notifications. |

### Pricing hypothesis

- **Solo:** $49/month — one trade, one service area, daily brief.
- **Pro:** $149/month — multiple service areas, multiple opportunity sources, saved filters, and lead notes.
- **Agency/coach:** $299/month — up to 10 contractor seats with shared reporting.
- **Pilot:** free for 20 qualified pilots for 30 days in exchange for weekly feedback.

Do not launch variable per-lead pricing. It creates disputes about attribution and complicates the MVP.

## PRD MVP

### Target user

Owner-operator or small residential/commercial contractor in one initial trade who:

- monitors several public job sources;
- receives opportunities that are poorly qualified;
- wants a daily shortlist;
- can verify that a listing is real;
- is willing to correct classifications and filters.

### Initial trade

Choose one based on pilot interviews. Recommended starting trade: **residential roofing** or **HVAC repair** because job descriptions tend to contain service area, urgency, scope, and project value. If interviews do not support either, select the trade with the strongest pilot commitment.

### P0 — required for launch

1. **Workspace setup**
   - Company name, trade, service ZIP codes, minimum project value, project types, current capacity, and “do not call” filters.
2. **Permitted source connectors**
   - At least one source with explicit permission for automated collection, plus CSV/manual import for user-provided links or exports.
   - Respect robots directives, terms, rate limits, attribution, and deletion requirements.
3. **Normalization**
   - Parse title, location, description, date, project value when disclosed, source URL, and contact route.
4. **Deduplication**
   - Detect likely cross-posts and keep one canonical listing with source references.
5. **Qualification**
   - Rule-based score for service area, trade match, stated project value, recency, clarity, and capacity.
   - Explain every scoring factor in plain language.
6. **Daily ranked brief**
   - Top opportunities, reason for ranking, source link, age, and suggested action.
7. **Status workflow**
   - New, reviewing, contacted, won, lost, irrelevant.
8. **Feedback loop**
   - Mark irrelevant, already handled, wrong trade, outside area, or valuable opportunity.
9. **Email digest**
   - Daily or weekday schedule with concise top opportunities.
10. **Compliance and safety**
   - No bypassing CAPTCHAs, logins, paywalls, or access controls.
   - No purchase of personal data.
   - Respect applicable do-not-call and outreach rules.
   - Include source attribution and an opt-out/suppression mechanism where required.

### P1 — after initial activation

- Browser extension that saves a job link manually.
- Saved search presets.
- CSV export.
- Opportunity status history.
- Team sharing with read-only access.
- Weekly performance summary.
- Duplicate and stale-listing moderation.

### P2 — later

- Website and social-post monitoring.
- CRM integrations.
- Automated estimate drafting.
- Bid/no-bid recommendation trained from customer feedback.
- Team performance analytics.
- Additional trades.

### Non-goals

- No guaranteed leads.
- No consumer marketplace.
- No automated cold calling, text messaging, or spam.
- No scraping prohibited sources.
- No CRM replacement.
- No autonomous bidding.
- No claim that a listing is guaranteed genuine or available.
- No general-purpose “AI lead generator” breadth.
- No multi-trade onboarding during the MVP.

### Core user story

> As a contractor, I want a short daily list of relevant public jobs with transparent qualification so I can call the best opportunities first without maintaining multiple saved searches.

### Technical approach

- Web application with responsive email-linked access.
- PostgreSQL for users, opportunities, normalized listings, subscriptions, and feedback.
- Background worker for permitted-source ingestion and scheduled briefs.
- Rule-based scoring first; use AI only for optional classification or structured extraction.
- Provider abstraction for email, hosting, and AI APIs.
- Store source identifiers, fetch timestamps, content hashes, and deletion/status records.
- Keep every ranking factor inspectable.

## 14-day day-by-day build plan

| Day | Deliverable | Exit criterion |
|---:|---|---|
| 1 | Choose one trade; interview three contractors; confirm recurring pain and source list | Written ICP, source constraints, and willingness-to-pay signal from three people |
| 2 | Interview seven more contractors; select the initial source and manual import fallback | Ten interviews completed; one source approved for implementation; three pilot commitments |
| 3 | Create wireframes, schema, auth, workspace settings, and legal/compliance checklist | A user can register and configure trade, service area, minimum value, and capacity |
| 4 | Build ingestion adapter for the approved source plus CSV import | At least 20 permitted test opportunities enter the database with source metadata |
| 5 | Build normalization, deduplication, trade classification, and value extraction | Duplicate test set is correctly merged; classifications can be manually corrected |
| 6 | Implement transparent scoring and service-area filtering | Every listing has a score, component breakdown, and exclusion reason |
| 7 | Build daily brief, listing detail, status workflow, and email delivery | A pilot receives a useful top-10 brief with working links |
| 8 | Add feedback controls, relevance labels, daily preferences, and loading/error states | Pilot can mark results and preferences persist reliably |
| 9 | Conduct five usability sessions; instrument activation and brief-open events | Top workflow issues are ranked; analytics capture signup, source, and engagement |
| 10 | Implement billing checkout, trial, plan limits, cancellation, and account deletion | Test purchase succeeds and cancellation removes access correctly |
| 11 | Add monitoring, backups, rate-limit handling, source outage fallback, and support workflow | Failed ingestion produces a useful fallback brief and alert rather than silent failure |
| 12 | Harden privacy, retention, terms, acceptable-use, and outreach-compliance language | Legal copy and data-deletion path are reviewed before public access |
| 13 | Onboard three pilot contractors; manually inspect their first two briefs | At least three pilots receive relevant briefs and provide structured feedback |
| 14 | Fix high-severity issues, publish pricing, and launch the first 20-account cohort | Paid conversion attempt, onboarding flow, and support process work end to end |

### Build discipline

- Use managed Postgres and a simple application framework.
- Build one source adapter, not a generic scraping platform.
- Prefer deterministic parsing and rules over an AI-heavy architecture.
- Use synthetic or explicitly permitted data during development.
- Do not spend the build window on a mobile app, browser extension, marketplace, or automated outreach.

## 30-day marketing calendar

**Budget:** $240 maximum  
**Allocation:** $120 content/community tools, $60 targeted sponsorship in one trade community, $60 micro-outreach and pilot incentives.

| Day | Activity | CTA and KPI |
|---:|---|---|
| 1 | Publish the landing page with one-trade positioning and sample daily brief | CTA: Get the first brief; KPI: 10 qualified visits, 2 signups |
| 2 | Post a “why most contractor lead alerts are unusable” teardown in one contractor group | CTA: Reply with the worst lead; KPI: 8 useful replies |
| 3 | Recruit two micro-creators in the selected trade for demonstrations | KPI: 2 commitments |
| 4 | Run a 45-minute interview clinic and record it | CTA: Join pilot; KPI: 5 attendees, 2 pilot requests |
| 5 | Send a personal email to 20 local operators describing the qualifying logic | KPI: 5 replies, 2 calls |
| 6 | Publish a sample ranked brief using public, permitted listings | KPI: 100 qualified page views, 5 signups |
| 7 | Review onboarding funnel; fix the largest drop-off | KPI: activation rate above 50% |
| 8 | Publish “10 filters for a roofing contractor” or equivalent trade-specific resource | KPI: 20 downloads, 3 signups |
| 9 | Host a 30-minute pilot feedback call | KPI: 3 pilot users active |
| 10 | Ask satisfied pilots for a short video testimonial with permission | KPI: 2 testimonials |
| 11 | Publish a before/after workflow comparison | KPI: 3 signups |
| 12 | Send a segmented email to trial users who did not activate | KPI: reactivation above 30% |
| 13 | Partner with one trade-specific newsletter, podcast, or community | KPI: 25 qualified visits |
| 14 | Publish the first weekly ranking-brief benchmark | KPI: 20 signups and 30% brief-open rate |
| 15 | Approach 20 complementary local sales or marketing consultants | KPI: 3 referral partners |
| 16 | Add frequently requested filters based on pilot feedback | KPI: 80% of pilots confirm relevance improvement |
| 17 | Post a short “how the score works” walkthrough | KPI: 8 signups |
| 18 | Run a live 20-minute product demo | KPI: 10 attendees, 3 trials |
| 19 | Email the trial cohort with scarcity based on real capacity | KPI: 4 paid conversions |
| 20 | Publish a pilot case study with verified metrics | KPI: 5 signups |
| 21 | Conduct churn-save calls with non-converting users | KPI: identify top 2 objections |
| 22 | Publish an FAQ responding to those objections | KPI: 8 signups |
| 23 | Ask referral partners to introduce one contractor each | KPI: 3 qualified referrals |
| 24 | Test a $149 founding plan against $99 founding plan | KPI: 5 conversions, no support burden increase |
| 25 | Improve onboarding email sequence | KPI: trial-to-paid above 15% |
| 26 | Create a short screen recording of daily operation | KPI: 50 views, 4 signups |
| 27 | Contact warm users who viewed pricing but did not buy | KPI: 3 sales conversations |
| 28 | Publish an honest limitations and source-coverage page | KPI: reduced sales objections |
| 29 | Convert the strongest pilot to an annual plan offer only if retention is healthy | KPI: 1 annual conversion without aggressive discounting |
| 30 | Review demand, activation, retention, support load, and unit economics | KPI: documented decision: scale, narrow, or stop |

### Organic-first rules

- Do not buy broad search ads.
- Never scrape competitor audiences or purchase lead lists.
- Keep every outreach personalized and relevant.
- Do not claim exclusivity over public listings.
- Obtain permission before using customer names or testimonials.

## Unit economics to $10K MRR

### Revenue scenarios

| Plan | Price | Customers | MRR |
|---|---:|---:|---:|
| Pro | $149 | 68 | $10,132 |
| Agency | $299 | 34 | $10,166 |
| Blended | $199 average | 51 | $10,149 |

### Cost assumptions

| Cost item | Per active account/month |
|---|---:|
| Hosting, database, email, observability | $3–$6 |
| Permitted source/API usage and processing | $3–$8 |
| AI extraction, if used | $0–$5 |
| Support and data correction | $4–$8 |
| **Total variable cost** | **$10–$27** |

At a $149 Pro price and $20 variable cost:

- Gross margin: $129.
- Gross-margin contribution: about 86%.
- $10K MRR at roughly 68 Pro accounts.

At $199 blended ARPA and $20 variable cost:

- Gross margin: $179.
- Gross-margin contribution: about 90%.
- $10K MRR at roughly 51 accounts.

### Acquisition assumptions

With a 12% landing-page-to-paid conversion rate:

- 68 customers require about 567 qualified site visitors.
- A focused community-led funnel can plausibly produce this over 60–90 days, but the first 30 days should validate activation and willingness to pay rather than claim immediate scale.

With a 3-month paid churn assumption of 15%:

- Roughly 12 new paid accounts per month are needed to maintain 68 active accounts, depending on the starting base and growth rate.
- If churn exceeds 25%, reduce scope or improve workflow value before increasing spend.

### Break-even

At $149/month and $20 variable cost:

- Contribution per customer: $129.
- $300 total marketing spend is recovered after roughly 3 acquired customers, assuming no other launch costs.
- At 68 customers, estimated monthly gross profit is about $8,772 before founder labor, taxes, and general overhead.

## Kill criteria

Stop or materially narrow the product if any of these occur by the end of day 30:

1. Fewer than 5 of 10 interviewed contractors report the problem at least weekly.
2. Fewer than 3 contractors agree to pilot with real workflow access.
3. Fewer than 2 of 5 activated pilots use the daily brief on at least 8 of 10 weekdays.
4. Zero paid conversions after 30 qualified pilot users receive the offer.
5. Paid conversion remains below 8% after two landing-page iterations with qualified traffic.
6. Median weekly retention is below 50% by week 4.
7. Median customer support exceeds 30 minutes per account per week.
8. The approved data source cannot be used reliably or economically, and permitted alternatives do not retain the same value.
9. Gross margin falls below 70% at the proposed price.
10. Customers primarily request a generic CRM, auto-bidding, cold outreach, or guaranteed leads—evidence that the wedge is wrong.
11. More than 20% of rankings are reported as irrelevant after the feedback loop is applied.
12. Compliance review cannot establish a lawful, respectful operating model.
