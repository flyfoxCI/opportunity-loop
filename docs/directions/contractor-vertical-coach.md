---
layout: post
title: "Contractor Vertical Coach — Roofers’ Revenue Operations"
date: 2026-11-17T00:39:25+00:00
week: "2026-11-17_003925"
week_date: "2026-11-17T00:39:25+00:00"
slug: "contractor-vertical-coach"
permalink: /directions/contractor-vertical-coach.html
tags:
  - "AI"
  - "B2B"
  - "B2C"
  - "proposal"
  - "vertical"
excerpt: "Give one contractor trade an AI business coach for estimating, follow-up, and recurring revenue operations."
---

**Tier:** GO_NARROW  
**Demand:** 4/5  
**Competition:** 4/5  
**Target:** $10,000 MRR  
**MVP window:** 14 days, solo  
**30-day marketing budget:** ≤ $300

## Wedge (required for GO_NARROW)

This direction is intentionally limited to **small residential roofing contractors operating in one metro area**.

The MVP will coach one roofing company through four recurring workflows:

1. classify and prioritize incoming opportunities;
2. prepare a consistent estimate-review checklist;
3. create compliant, manual follow-up drafts;
4. review lost or stalled jobs for recurring causes.

It will not serve multiple trades, national teams, consumers, or generic contractors. The only initial ICP is an owner-operator or sales lead at a residential roofing company with 2–20 employees.

The company will refuse to build:

- an all-contractor CRM;
- automated cold calling or texting;
- automatic bid submission;
- roof-measurement computer vision;
- insurance-claim filing;
- financing brokerage;
- a general-purpose AI sales bot;
- public roofing lead marketplaces;
- general estimating, project management, accounting, or payroll tools;
- support for commercial roofing, multifamily roofing, or specialty trades in the MVP;
- autonomous claims, contracts, or safety determinations.

Competition is scored 4 because broad contractor sales and lead tools are established. The narrow wedge is “one roofing company’s revenue-operations coach,” not a general contractor platform.

## Why this direction

### TrustMRR evidence

Prior research validates contractor demand for lead generation, documenting NextjobConnect at approximately $5,000 MRR. That revenue shows commercial buyers will pay for an outcome connected to more qualified work. At the same time, contractor software and lead tools are a mature, well-funded category, so a generic entrant would fail the competition gate.

This direction turns validated demand into a narrower coaching workflow. A small roofing company does not need another database of leads. It needs help answering:

> “Which opportunities deserve attention, what should I say next, and why are we losing work?”

The product should first teach and enforce a repeatable operating process. Only later should it automate individual tasks.

### X/web evidence

Roofing and home-improvement communities repeatedly discuss inconsistent follow-up, quotes that do not convert, untracked lost jobs, estimator/customer handoff problems, and leads being handled by whoever answers first. These are operational pains distinct from consumer lead marketplaces and suitable for a focused coaching product.

Evidence to validate before implementation:

1. Ten interviews with owners or sales leads at residential roofing companies.
2. At least five use the same lead-tracking and follow-up process.
3. Three agree to import a redacted opportunity list.
4. Two agree to a 14-day paid pilot.
5. At least two confirm that poor follow-up or lost-job analysis costs meaningful revenue.

### Product thesis

Contractor Vertical Coach provides a daily operating review for a small roofing sales team:

- imports permitted CRM exports;
- identifies missing follow-up, stale opportunities, and unclear qualification;
- recommends the next action based on the company’s stage definitions;
- drafts a reply for human review;
- runs a weekly lost-job review;
- produces a simple “what to change next week” coaching note.

It is an operating coach and review layer, not an autonomous closer.

## Competitor table

| Level | Competitor | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Jobber | CRM for home-service and specialty trades | Commonly $29–$100+ per month, add-ons and higher tiers available | Direct workflow incumbent with broad features. Differentiation must be roofing-specific coaching, not CRM breadth. |
| L1 | Housecall Pro | CRM, scheduling, dispatch, payments, and marketing for home services | Commonly $50–$300+ per month depending on users and add-ons | Strong integrated incumbent; generic follow-up automation is not enough. |
| L1 | ServiceTitan | Deep enterprise software for home-service contractors | Commonly high-tens to hundreds per month; exact pricing varies | Powerful but heavier and expensive for small roofers. |
| L1 | JobNimbus | CRM and workflow platform for specialty trades | Subscription with product and user tiers | Strong roofing/home-improvement fit; differentiation must be lighter and outcome-focused. |
| L2 | Buildertrend | Construction management and sales CRM | Premium subscription | More construction-operations oriented than small-roofing sales coaching. |
| L2 | AccuLynx | Roofing CRM, measurements, production, and reporting | Subscription and premium tiers | Roofing-specific incumbent. Must avoid competing on broad CRM or measurement features. |
| L2 | CompanyCam | Visual documentation and project communication | Free entry plus paid tiers | Adjacent workflow product with roofers already in the category. |
| L3 | Spreadsheet, shared inbox, and task list | Manual pipeline and follow-up tracking | $0–$30 per month | The key substitute. Product must visibly improve consistency and weekly review. |
| L3 | General ChatGPT / Claude | Draft follow-ups and coaching advice | Free to $20+ per month | Powerful low-cost substitute. The wedge must be structured context from the company’s own pipeline and stage definitions. |

### Pricing hypothesis

- **Solo coach:** $79/month — one user, imports, review, and drafts.
- **Roofing team:** $149/month — up to five users and shared review.
- **Setup package:** $299 one-time for workflow configuration and CSV import, with no promise of leads.

At $149, approximately 68 paying roofing companies are needed for $10K MRR.

## PRD MVP

### Target user

Owner, sales manager, or estimator at a residential roofing company with:

- 2–20 employees;
- 10–100 opportunities per month;
- a CRM or spreadsheet containing opportunity data;
- one founder-controlled decision about follow-up priorities;
- no need for full dispatch, production, or accounting replacement.

### P0 — required for launch

1. **Workflow setup**
   - Service area, roof types, minimum viable job, qualification criteria, stages, and close definition.
2. **CSV import**
   - Customer-safe fields, validation, preview, duplicate detection, and error report.
3. **Opportunity normalization**
   - Stage, date, value if known, source, last activity, assigned owner, and next action.
4. **Daily review**
   - Ranked opportunities needing attention, stale records, missing next steps, and uncontacted leads.
5. **Reason explanation**
   - Every recommendation states the underlying rule and source fields.
6. **Follow-up drafts**
   - Email or SMS text draft for human review.
   - No automatic sending.
7. **Stage guardrails**
   - Do not recommend sending if required context is missing.
8. **Weekly lost-job review**
   - Categorize loss reasons, surface recurring patterns, and generate a short coaching note.
9. **Company playbooks**
   - Keep tone, qualification rules, and common answers in a private workspace.
10. **Weekly report**
   - Review completion, response lag, stage movement, and one recommended process change.
11. **Billing and data controls**
   - Trial, checkout, plan limits, export, and workspace deletion.
12. **Compliance**
   - Respect consent, do-not-contact, state roofing-solicitation rules, and applicable messaging consent requirements.
    - Never make a roofing, safety, insurance, financing, or contract determination autonomously.

### P1 — after activation

- CSV export and comments.
- User-defined follow-up sequences with manual approval.
- Missed-call and appointment reminders.
- Lost-reason analytics.
- Call-summary import.
- Custom coaching cadence.
- Slack or email notifications.

### P2 — later

- CRM read-only API integrations.
- Proposal and inspection workflow.
- Team leaderboards.
- Local weather and permit context.
- Local referral-partner directory.
- Job-cost review after roofing work is completed.
- Additional contractor trades only after a separate opportunity assessment.

### Non-goals

- No automatic outreach.
- No lead purchase or resale.
- No CRM replacement.
- No proposal generation or contract drafting.
- No roof measurement or photo analysis.
- No insurance, financing, safety, or code-compliance advice.
- No consumer marketplace.
- No support for multiple trades or geographies.
- No claim that the coach replaces an experienced roofing operator.

### Core user story

> As the owner of a small roofing company, I want a daily review of my pipeline and a weekly explanation of lost jobs so that my team follows up consistently and improves one operating metric at a time.

### Technical approach

- Web app with CSV-first workflow.
- Postgres for workspaces, opportunities, recommendations, drafts, and coaching events.
- Rule engine for stage, staleness, and next-action recommendations.
- Optional LLM for rewriting drafts and summarizing recurring loss reasons.
- Human approval state on every outbound message.
- No CRM integration required for launch.
- Usage metering and audit trail for recommendations and approvals.
- Provider abstraction for email, LLM, hosting, and analytics.

## 14-day day-by-day build plan

| Day | Deliverable | Exit criterion |
|---:|---|---|
| 1 | Interview three residential roofing owners or sales leads | Documented ICP, workflow, and recurring pain |
| 2 | Interview seven more; choose one roofing segment and metric | Ten interviews complete; three pilot commitments |
| 3 | Create workflow, import, and review wireframes; define schema and safeguards | A user can configure stages and import a pipeline |
| 4 | Build auth, workspace, company rules, and subscription state | User can create a roofing workspace |
| 5 | Build CSV upload, mapping, validation, preview, and error report | 50-record sample imports correctly |
| 6 | Build opportunity normalization, stages, dates, values, and stale detection | Imported records become reviewable opportunities |
| 7 | Build daily ranked review with transparent explanations | Top actions match pilot expectations in eight of ten cases |
| 8 | Build manual follow-up draft generation and approval states | Drafts use company tone and contain no unsupported claims |
| 9 | Build weekly lost-job categorization and coaching note | Five lost records produce a useful recurring-pattern summary |
| 10 | Add company playbook, weekly metrics, export, and delete | Core privacy and reporting workflows work |
| 11 | Run five usability sessions with real redacted CSVs | Four users complete a daily review without assistance |
| 12 | Add billing, checkout, trial, usage cap, and provider failure handling | Test purchase, cancellation, and degraded mode work |
| 13 | Onboard three roofing pilots and support their first daily and weekly reviews | Three pilots use the product twice and provide structured feedback |
| 14 | Fix critical issues, publish one-metro landing page, and open a 20-company cohort | Ten activated workspaces and two paid-pilot commitments |

### Build discipline

- CSV first; no CRM integration.
- One roofing segment and one core metric.
- Human approval for every message.
- Do not build proposal, measurement, or dispatch functionality.
- Keep the recommendation rules inspectable and editable.

## 30-day marketing calendar

**Budget:** $300 maximum  
**Allocation:** $120 roofing-community sponsorships, $90 content and local SEO, $60 micro-creator demonstrations, $30 pilot incentives.

| Day | Activity | CTA and KPI |
|---:|---|---|
| 1 | Publish a roofing-specific landing page | CTA: Review your pipeline; KPI: 15 qualified visits |
| 2 | Post “Why your CRM is not a follow-up system” in a roofer group | KPI: 8 useful replies |
| 3 | Interview five roofing sales leaders | KPI: 5 interviews, 2 pilot commitments |
| 4 | Publish a lost-job review template | KPI: 20 downloads |
| 5 | Run a live CSV-to-daily-review demonstration | KPI: 10 attendees, 3 trials |
| 6 | Personally email 20 local roofing operators | KPI: 5 replies, 2 calls |
| 7 | Review activation and CSV-import failures | KPI: activation above 50% |
| 8 | Post a sample daily pipeline review | KPI: 10 shares or replies |
| 9 | Publish “10 roofing lead stages your team should actually use” | KPI: 15 downloads, 3 signups |
| 10 | Ask pilots for structured time-saved feedback | KPI: 4 responses |
| 11 | Host a 30-minute lost-job review workshop | KPI: 12 attendees, 3 trials |
| 12 | Add the most requested CSV field or rule | KPI: four of five pilots confirm improvement |
| 13 | Send a follow-up to trial users without an imported pipeline | KPI: 30% reactivation |
| 14 | Publish a verified pilot workflow story | KPI: 5 signups |
| 15 | Approach five roofing-booking and sales consultants | KPI: 2 referral partners |
| 16 | Publish a short daily-review screen recording | KPI: 100 views, 5 signups |
| 17 | Test $79 solo versus $149 team positioning | KPI: 4 paid conversions |
| 18 | Invite five roofers to a closed onboarding clinic | KPI: 5 activated trials |
| 19 | Send targeted follow-up to active trial users | KPI: 3 paid conversions |
| 20 | Publish a compliance-safe follow-up checklist | KPI: 8 signups |
| 21 | Review support and AI cost per workspace | KPI: gross margin above 75% |
| 22 | Offer a $299 setup package to five high-intent pilots | KPI: 2 purchases |
| 23 | Conduct objections calls with non-buyers | KPI: top three objections identified |
| 24 | Revise the landing page with verified customer language | KPI: trial-to-paid above 10% |
| 25 | Post a weekly roofing operations question | KPI: 10 replies and 3 signups |
| 26 | Ask satisfied pilot users for permissioned testimonials | KPI: 2 testimonials |
| 27 | Publish a one-page weekly scorecard template | KPI: 20 downloads, 5 signups |
| 28 | Add one CRM CSV variant used by the target segment | KPI: activation above 60% |
| 29 | Offer a founding-team plan only to pilots with repeated weekly use | KPI: 4 team upgrades |
| 30 | Review activation, weekly usage, paid conversion, churn risk, and support time | KPI: decide scale, narrow, or stop |

### Organic-first rules

- Focus on roofing groups, local contractor associations, and practitioner newsletters.
- Never purchase contact lists or upload third-party lead data.
- Use customer data only after explicit authorization.
- Keep every message human-reviewed and locally compliant.

## Unit economics to $10K MRR

### Revenue scenarios

| Plan | Price | Customers | MRR |
|---|---:|---:|---:|
| Solo | $79 | 127 | $10,033 |
| Team | $149 | 68 | $10,132 |
| Blended plus setup revenue | $135 average | 74 | about $9,990 recurring, plus setup revenue |

### Cost assumptions

| Cost item | Per active account/month |
|---|---:|
| Hosting, database, email, analytics | $3–$6 |
| LLM drafting and coaching | $2–$6 |
| Support and import assistance | $5–$12 |
| **Total variable cost** | **$10–$24** |

At a $149 team price and $17 variable cost:

- Contribution: $132.
- Gross margin: about 89%.
- $10K MRR requires approximately 68 active teams.

At a $79 solo price and $17 variable cost:

- Contribution: $62.
- Gross margin: about 78%.
- $10K MRR requires approximately 127 solo accounts.

### Acquisition assumptions

With a 12% qualified-visit-to-paid conversion rate:

- 68 team customers require approximately 567 qualified visits.
- The narrow audience makes highly specific communities and referrals more efficient than broad contractor directories.

With 12% monthly churn:

- Approximately eight new customers per month are needed to maintain 68 active accounts.
- If churn exceeds 25%, the coaching workflow is not becoming habitual and should be narrowed further.

### Break-even

At $149 ARPA and $17 variable cost:

- $300 marketing is recovered after roughly three acquired customers.
- At 68 customers, estimated gross profit is about $8,976 before founder labor, taxes, and overhead.

## Kill criteria

Stop or materially narrow the product if any occur by day 30:

1. Fewer than 5 of 10 roofing interviewees report stale follow-up or lost-job analysis as a weekly problem.
2. Fewer than 3 agree to provide redacted pipeline data.
3. Fewer than 2 complete a paid pilot.
4. Fewer than 60% of activated pilots use the daily review in week 2.
5. Fewer than 40% complete a weekly lost-job review.
6. Zero paid conversions after 30 qualified workspaces receive an offer.
7. Paid conversion remains below 8% after two focused landing-page iterations.
8. Median support exceeds 45 minutes per account per month.
9. More than 25% of recommendations are considered irrelevant or incorrect.
10. Gross margin falls below 70%.
11. Users demand full CRM, dispatch, proposal, financing, or lead-generation functionality rather than a coaching workflow.
12. A referral partner or roofing community repeatedly confirms that the wedge is too narrow.
13. Legal/compliance review prevents a safe human-in-the-loop outreach model.
14. The company cannot reach 50 active qualified workspaces through organic distribution within 60 days.
