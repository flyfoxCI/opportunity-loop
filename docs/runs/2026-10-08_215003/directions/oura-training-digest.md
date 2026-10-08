# Oura Training Digest

## 1. Why this direction

### TrustMRR evidence

- The current candidate list includes **Ring Widget – Oura Ring widgets**, with approximately **$1.70 MRR**, **$10.28 last-30 revenue**, and **103 subscribers**.
- The category shows that Oura users actively seek tools around their ring data, even when the listed MRR is small.
- The opportunity is not to build another ring or compete with Oura’s native product. It is to turn exported data into a useful training and recovery workflow.

### X/web evidence

The supplied evidence did not contain usable X/web results. Discovery should include:

- `Oura API alternatives`;
- `Oura export training dashboard`;
- `Oura readiness trends`;
- `Oura ring app widget`;
- `Oura data privacy`;
- `Oura training plan alternative`;
- `Oura recovery recommendations Reddit`.

The product should work from user-exported files where possible, reducing dependence on unofficial integrations and reducing privacy exposure.

### Interpretation

Oura users want interpretation, history, and actionable routines, but health advice carries safety and trust risks. The product should be positioned as an educational training digest, not medical advice, diagnosis, or treatment.

The most defensible initial wedge is a narrow workflow for people who already use Oura and want weekly summaries. It should not attempt to become a general-purpose fitness platform.

## 2. Competitor table

| Level | Competitor/type | Typical strength | Gap to exploit |
|---|---|---|---|
| L1 | Oura native app | Direct data access and strong brand | Limited user-owned export/interpretation workflows |
| L1 | Wearable analytics dashboards | Broad device support and charts | Complex setup and limited training context |
| L2 | Manual spreadsheets/notion templates | Flexible and private | Laborious, no interpretation, poor retention |
| L2 | Generic AI chat tools | Easy data questions | Hallucinations, no structured trend analysis, privacy concerns |
| L3 | Reddit/community recommendations | Peer advice and lived experience | Anecdotal, inconsistent, difficult to operationalize |
| L3 | Coach-generated static plans | Human accountability | Expensive and not continuously updated |
| L4 | Generic fitness apps | Habit and workout ecosystems | No Oura-specific data interpretation |

### Positioning

“Turn your Oura export into a transparent weekly training decision journal.”

## 3. PRD MVP

### Target ICP

1. recreational endurance athletes already using Oura;
2. people training for a 5K, half marathon, or similar event;
3. quantified-self users who export data but do not understand trends;
4. coaches who want a client-friendly weekly digest, initially manually uploaded.

Primary job:

> Upload an Oura export and receive a concise, evidence-linked weekly summary of sleep, readiness, activity, and recovery patterns.

### Wedge

The MVP is deliberately limited to **Oura Ring owners who manually upload exports and want a weekly training/recovery digest**.

It refuses:

- live Oura API integration;
- general wearable support;
- medical diagnosis or treatment;
- injury prediction;
- guaranteed performance outcomes;
- eating-disorder or obsessive-compulsive health optimization;
- training plans for minors without guardian controls;
- personalized calorie prescriptions;
- recovery scores presented as clinically validated.

The product should be informative, transparent, and easy to stop using. It must not encourage users to optimize every metric or train through warning signs.

### P0

- secure upload of a supported export file;
- file parsing and normalization;
- date-range selection;
- sleep summary;
- readiness summary;
- activity summary;
- weekly trend charts;
- plain-language “what changed” section;
- source values shown beside every generated interpretation;
- user-selected goals and training context;
- educational guidance boundaries;
- export to PDF/CSV;
- delete export and account data;
- no medical-advice disclaimer;
- support for refusal when data is incomplete or inconsistent.

### P1

- recurring export reminders;
- manual weekly check-in;
- training-load trend view;
- coach sharing link;
- multiple CSV formats;
- annotation of unusual days;
- personalized non-medical experiments;
- email digest;
- integration with calendar or training log;
- accessibility improvements.

### P2

- official Oura integration if approved;
- other wearable imports;
- adaptive training experiments;
- coach dashboard;
- anomaly detection with professional review;
- export APIs;
- longitudinal family/private sharing;
- integration with sports platforms.

### Non-goals

- no medical advice;
- no diagnosis;
- no injury-risk scoring;
- no prescription of food intake;
- no guaranteed readiness or recovery;
- no unsupported real-time data scraping;
- no social feed or leaderboard;
- no general-purpose health dashboard;
- no dark patterns around streaks or guilt.

### MVP acceptance criteria

A user can upload an Oura export, see a transparent weekly summary, inspect the underlying values, understand the limitations, export the digest, and delete their data.

## 4. 14-day build plan

| Day | Deliverable |
|---:|---|
| 1 | Interview 10 Oura users and 3 coaches; define safe scope |
| 2 | Collect representative anonymized exports and document schema |
| 3 | Write health/safety language and product refusal policy |
| 4 | Build upload, parsing, validation, and deletion flow |
| 5 | Normalize sleep, readiness, activity, and date data |
| 6 | Build deterministic weekly metrics and charts |
| 7 | Add constrained interpretation layer with evidence links |
| 8 | Build digest UI, source-value drawer, and export |
| 9 | Add account, billing, usage limits, and secure logging |
| 10 | Test with 10 users; check comprehension and unsafe advice |
| 11 | Refine medical-boundary responses and uncertainty language |
| 12 | Add accessibility, privacy controls, and retention settings |
| 13 | Private beta with athletes and coaches; collect trust feedback |
| 14 | Fix blockers, publish landing page, and invite paid cohort |

### Technical approach

- frontend/backend: TypeScript or Python;
- parsing: robust CSV/JSON import with schema validation;
- analytics: deterministic calculations before LLM interpretation;
- model layer: tightly constrained summarization only;
- storage: encrypted, short-lived file storage;
- deployment: simple containerized web service;
- observability: privacy-safe logs and prompt/output auditing;
- safety: refusal tests, human-readable limitations, emergency guidance, no diagnosis claims.

## 5. 30-day marketing calendar

### Budget

Total: **$250**.

- Content and sample digest: $60
- Design/video assets: $40
- Community and email tools: $30
- Paid smoke tests: $80
- Beta incentives: $40

### Calendar

| Day | Activity | CTA |
|---:|---|---|
| 1 | Publish landing page with sample weekly digest | Upload export |
| 2 | Invite 15 Oura users for interviews | Join research |
| 3 | Publish “what your Oura export does and does not show” | Read guide |
| 4 | Share an anonymized digest walkthrough | Try beta |
| 5 | Reach 10 endurance coaches | Pilot coach |
| 6 | Publish privacy and deletion policy | Read policy |
| 7 | Run $20 search test for Oura export analysis | Analyze week |
| 8 | Email beta users for comprehension survey | Complete feedback |
| 9 | Publish readiness-trend visualization | View sample |
| 10 | Reach Oura and running communities | Invite |
| 11 | Publish non-medical boundary explainer | Try digest |
| 12 | Run $20 ad test for wearable trend dashboard | Upload export |
| 13 | Host “how to read Oura trends” session | Register |
| 14 | Send beta users updated explanation | Continue beta |
| 15 | Publish coach sharing workflow | Invite coach |
| 16 | Reach 20 recreational athletes | Pilot call |
| 17 | Publish CSV export troubleshooting guide | Upload file |
| 18 | Post short demo clip | Start digest |
| 19 | Run $20 retargeting test | Continue beta |
| 20 | Request permissioned testimonial | Share experience |
| 21 | Publish “do not optimize every metric” article | Read guide |
| 22 | Reach training-plan creators | Partner |
| 23 | Add waitlist for approved integrations | Request feature |
| 24 | Interview five more users | Validate price |
| 25 | Launch referral invitation | Invite athlete |
| 26 | Publish weekly-digest template | Use template |
| 27 | Run final $20 ad test | Start free digest |
| 28 | Email inactive users with delete-or-return CTA | Resume |
| 29 | Review retention, safety incidents, and support | Decide wedge |
| 30 | Publish transparency update | Join paid cohort |

### KPIs

- 100 qualified visits;
- 25 uploaded exports;
- 15 completed digest views;
- 8 day-seven users;
- 5 paid pilots;
- ≥80% comprehension of source values;
- zero unsafe medical claims in review;
- ≥40% week-four retention.

## 6. Unit economics to $10K MRR

### Pricing hypothesis

- Free: one weekly digest with limited history;
- Plus: $12/month;
- Coach plan: $39/month;
- Annual: $99/year.

At $12/month, $10K MRR requires approximately 834 subscribers. At $39/month, 257 coach/team subscriptions. The coach route may be more efficient than consumer acquisition because each subscription can cover several athletes.

### Cost model

Assume:

- parsing and deterministic analytics: $0.10–$0.40 per weekly export;
- constrained summarization: $0.10–$0.50;
- hosting/storage: $0.20–$0.50;
- support: $0.50–$2;
- payment fees: 3%.

Target contribution margin: ≥60%. Process only the data needed for the requested digest and expire raw files quickly.

### Growth levers

- quantified-self communities;
- running and triathlon groups;
- coaches;
- privacy-first positioning;
- export-first workflow;
- educational content;
- referrals from coaches;
- annual plans.

## 7. Kill criteria

Stop or reposition if:

1. fewer than 4 of 10 interviewees report a recurring interpretation problem;
2. fewer than 25% of beta users return weekly;
3. fewer than 3 of 10 users understand that outputs are not medical advice;
4. users demand diagnosis, injury prediction, or calorie prescriptions;
5. safety reviewers find recurring unsafe recommendations;
6. export formats are too unstable or unsupported to maintain;
7. paid conversion is below 2% after 100 qualified visitors;
8. variable costs prevent ≥55% contribution margin;
9. data deletion/privacy expectations cannot be met;
10. no coach or community distribution channel appears by day 30.

## 8. Expansion path

1. coach dashboard;
2. official approved integrations;
3. additional wearable exports;
4. longitudinal trend journaling;
5. training and recovery experiments;
6. calendar integration;
7. athlete sharing with explicit consent;
8. clinician-reviewed educational content;
9. export API;
10. broader personal data ownership tools only after strong safety and retention evidence.
