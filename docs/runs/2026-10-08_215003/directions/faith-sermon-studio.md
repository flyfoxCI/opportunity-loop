# Faith Sermon Studio

## 1. Why this direction

### TrustMRR evidence

- The prior validated direction index cites **Sermon Scribe at approximately $14K MRR and 2,362 paid subscribers**.
- The index reports a large opportunity around faith/religion AI and unusually limited direct competition compared with the size of the use case.
- FaithWall in the current candidate list shows consumer religious engagement, but the stronger monetization signal is the paid sermon-preparation workflow rather than a devotional widget.

### X/web evidence

The supplied evidence did not contain usable X/web results. The following discovery queries should be run before launch:

- `sermon AI alternatives`;
- `AI sermon preparation pastor`;
- `sermon notes AI hate`;
- `pastor looking for sermon help`;
- `church AI tool price`;
- `sermon research assistant`.

The product should serve the preparation workflow: scripture research, theological outline, sermon draft, illustrations, questions, and repurposeable notes.

### Interpretation

The key opportunity is not generic “AI Christian content.” It is a focused assistant that helps a pastor or volunteer move from a scripture or theme to a usable service plan while preserving editorial control.

The product must avoid presenting generated theology as authoritative. A review/edit step is central, and the user remains responsible for the final sermon.

## 2. Competitor table

| Level | Competitor/type | Typical strength | Gap to exploit |
|---|---|---|---|
| L1 | Sermon preparation AI tools | Fast generation and scripture integration | Quality variability, generic theology, limited denominational context |
| L1 | Church communication/content suites | Distribution and admin workflows | Sermon creation is not the core product |
| L2 | General ChatGPT/Claude workflows | Flexible and inexpensive | Inconsistent structure, no saved ministry context, poor privacy workflow |
| L2 | Theologian/reference libraries | Depth and credibility | Slow to turn into a service outline |
| L2 | Presentation/scripture note tools | Familiar templates | Limited drafting and repurposing |
| L3 | Pastor blogs and community templates | Authentic examples | Manual, fragmented, hard to reuse |
| L3 | Church management platforms | Central records and communication | Little focus on theological drafting |

### Positioning

“An editable sermon workspace, not an AI minister.”

## 3. PRD MVP

### Target ICP

1. Independent pastors serving 50–300 congregants;
2. Small church ministry teams without a communications department;
3. Church planters and campus ministry leaders;
4. Volunteer teachers preparing weekly lessons.

Primary job:

> Give me a structured, editable weekly sermon draft grounded in the supplied passage, theology, and ministry context.

### P0

- email/password login;
- workspace creation;
- scripture passage input;
- reference translation selection;
- theology/denomination notes;
- sermon title and thesis generation;
- structured outline;
- introduction, main points, transitions, application, and prayer;
- citations/references displayed beside generated claims;
- editable draft;
- lock/revision history;
- markdown/docx export;
- speaker notes export;
- user controls for tone, length, and audience;
- safety reminder that generated theology requires human review;
- usage metering;
- delete/export account data.

### P1

- sermon series workspace;
- recurring service calendar;
- source library;
- illustration and story bank;
- small-group discussion questions;
- children’s lesson adaptation;
- audio transcription of a pastor’s notes;
- denominational style profiles;
- collaboration for ministry teams;
- email and calendar reminders;
- public/private sharing controls.

### P2

- integrations with church management platforms;
- video/social repurposing;
- translation into additional languages;
- custom theology libraries;
- ministry analytics;
- LMS and curriculum export;
- multi-language congregations;
- denominational administration.

### Non-goals

- no autonomous sermon delivery;
- no claim that AI understands a church’s full theology;
- no substitute for pastoral care;
- no theological debate platform;
- no copyrighted sermon reproduction;
- no mass-generated public devotional spam;
- no social-media growth automation;
- no doctrinal policing without user-defined context.

### MVP acceptance criteria

A pastor can enter a passage and context, generate an editable structured draft, inspect references, revise it, and export speaker notes in under ten minutes.

## 4. 14-day build plan

| Day | Deliverable |
|---:|---|
| 1 | Interview 8 pastors, ministry leaders, and volunteer teachers |
| 2 | Define theology, tone, length, and citation requirements |
| 3 | Build reference corpus and test prompts against representative sermons |
| 4 | Implement account, workspace, and prompt settings |
| 5 | Build passage input, context form, and generation endpoint |
| 6 | Implement structured outline and draft schema |
| 7 | Build editor, citation panel, and revision history |
| 8 | Build speaker notes, markdown, and docx export |
| 9 | Add safeguards, refusals, and review reminders |
| 10 | Conduct usability tests with 5 target users |
| 11 | Improve denominational/tone controls and output structure |
| 12 | Add billing, usage limits, and error tracking |
| 13 | Private beta with 10 churches; collect quality scores |
| 14 | Fix blockers, publish landing page, and open paid trials |

### Technical approach

- frontend/backend: TypeScript;
- model layer: provider-agnostic LLM interface;
- retrieval: curated public-domain/reference material with source metadata;
- storage: relational database for workspaces and drafts;
- exports: markdown and docx;
- safety: prompt constraints, source display, review reminder, abuse monitoring;
- deployment: managed web app with encrypted storage.

## 5. 30-day marketing calendar

### Budget

Total: **$250**.

- Content and visual assets: $60
- Email/domain/community tools: $40
- Paid smoke tests: $100
- Beta incentives: $50

### Calendar

| Day | Activity | CTA |
|---:|---|---|
| 1 | Publish landing page with editable sample sermon | Draft a sermon |
| 2 | Personally invite 20 pastors | Try beta |
| 3 | Publish “AI sermon tool privacy and review” guide | Read policy |
| 4 | Share a before/after outline demo | Join waitlist |
| 5 | Reach 20 church planters and ministry volunteers | Invite |
| 6 | Publish passage-to-outline workflow | Start draft |
| 7 | Run $20 search ad for sermon preparation software | Try it |
| 8 | Email beta users for quality feedback | Rate draft |
| 9 | Publish sermon-series workflow article | Create series |
| 10 | Reach church communication leaders | Demo |
| 11 | Publish review checklist for AI-generated theology | Download checklist |
| 12 | Run $20 ad test on pastor workflow terms | Start free draft |
| 13 | Host pastor office-hours Q&A | Invite pastor |
| 14 | Send beta users updated editor | Share feedback |
| 15 | Publish example from Baptist/evangelical/free Methodist context only if validated | Request access |
| 16 | Reach 30 small-church administrators | Pilot call |
| 17 | Publish export and collaboration walkthrough | Try export |
| 18 | Post short demo clips in ministry communities | Join beta |
| 19 | Run $30 ad test on “sermon outline AI” | Generate outline |
| 20 | Request case-study permission from active users | Share testimonial |
| 21 | Publish anonymized quality comparison | Try workspace |
| 22 | Reach ministry coaches and denominational consultants | Partner |
| 23 | Publish privacy FAQ | Read FAQ |
| 24 | Interview five more users | Validate pricing |
| 25 | Launch referral invitation for beta users | Invite pastor |
| 26 | Publish sermon-series template | Use template |
| 27 | Run final $30 ad test on best query | Start trial |
| 28 | Email non-converters with one CTA | Draft sermon |
| 29 | Review retention, quality, and support metrics | Choose segment |
| 30 | Publish transparency update | Join pilot |

### KPIs

- 100 qualified visits;
- 20 completed sermon drafts;
- 10 interviews;
- 5 activated accounts;
- 3 paid pilots;
- 50% of pilots use the tool weekly;
- median edit time under 10 minutes;
- quality rating at least 3.5/5.

## 6. Unit economics to $10K MRR

### Pricing hypothesis

- Solo pastor: $19/month;
- ministry team: $49/month;
- church/denomination pilot: $149/month;
- annual plan: two months free.

### Cost model

Assume 20–40% variable model cost depending on context and output length, with compression and caching reducing it over time.

At $49 average revenue:

- 205 paying teams reach $10K MRR;
- at $149 average revenue, 68 teams;
- at $19 average revenue, 527 individual pastors.

Target gross margin is ≥70% after model, hosting, support, and payment costs. Do not use an unlimited generation promise; use monthly credits or fair-use limits.

### Growth assumptions

Organic-first growth can come from:

- pastor communities;
- church-resource creators;
- ministry coaches;
- denomination-specific content;
- referrals from ministry teams;
- church communication consultants.

## 7. Kill criteria

Stop or reposition if:

1. fewer than 5 of 10 interviewed users report weekly sermon preparation pain;
2. fewer than 3 of 8 beta users rate output quality above 3/5;
3. users spend more time correcting output than drafting manually;
4. the product attracts content-farm users rather than working ministry teams;
5. paid conversion is below 2% after 100 qualified visitors;
6. model costs prevent ≥65% gross margin;
7. theological or copyright concerns cannot be addressed with clear safeguards;
8. retention below 25% by week four;
9. no distribution partner or community channel emerges by day 30;
10. target users insist that AI-generated theology is unacceptable in all workflows.

## 8. Expansion path

1. sermon-series library;
2. small-group and student curriculum;
3. bilingual sermon support;
4. transcription of research and sermons;
5. church-specific collaboration;
6. pastoral-content repurposing;
7. denominational templates;
8. archive and retrieval across years of ministry;
9. optional coaching/review marketplace only after product retention.
