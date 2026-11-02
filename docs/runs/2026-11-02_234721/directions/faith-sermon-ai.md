# Faith Sermon AI

## Why this direction

### TrustMRR evidence

- The prior validated direction index cites **Sermon Scribe at approximately $14K MRR and 2,362 paid subscribers**.
- This is direct revenue proof that churches and ministry workers pay for sermon-focused AI assistance at a scale sufficient to exceed the $10K MRR target.
- The existing signal is substantially stronger than the low-MRR products in the current Stage A list, although it was not itself a current Stage A candidate and therefore must be treated as prior validated evidence rather than a fresh candidate score.
- A solo founder does not need to reproduce the entire incumbent product. A narrow workflow around research, transcription, outline generation, and reusable ministry materials can be validated quickly.

### X/web evidence

- Church staff and volunteer sermon teams repeatedly describe a recurring weekly workflow: gather scripture references, research a topic, adapt prior material, prepare notes, and create announcements.
- The pain is not merely “write faster”; it is reducing preparation uncertainty while preserving a denominationally appropriate voice and keeping theological claims attributable.
- Search and social research should be repeated during pre-launch using queries such as:
  - `sermon AI pastor preparation`
  - `church AI sermon tools`
  - `pastor hates sermon AI`
  - `church announcement Canva alternative`
  - `sermon outline AI just shipped`
- Existing evidence is strongest for research-and-drafting assistance and weaker for fully autonomous preaching content. The MVP should therefore avoid positioning itself as a replacement for pastoral judgment.

## Competitor table

| Level | Product | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Sermon Scribe | Sermon preparation, research, transcription, and related ministry workflows | Public pricing may vary; verify before launch | Closest commercial proof and primary benchmark |
| L1 | Pulpit AI | AI-assisted sermon and Bible-study preparation | Verify current plan pricing | Direct category competitor |
| L1 | Sermon Outline | Sermon outline and illustration generation | Usually freemium/lower-tier | Competes on fast outlines rather than complete workflow |
| L1 | ChatGPT / Claude | General-purpose drafting and research | Subscription tiers plus API cost | Strong free substitute; differentiation must be workflow and trusted sources |
| L2 | You.com / Perplexity | General web research and citations | Freemium and subscription | Substitute for research assistants |
| L2 | Canva / Faithlife / Planning Center | Church graphics, announcements, schedules, and media | Mixed subscription models | Adjacent distribution and content competitors |
| L3 | Google Docs, Notion, Evernote | Notes, drafting, and knowledge management | Freemium and subscriptions | Low-cost substitutes that make output export essential |

### Competitive conclusion

The broad market is not empty, so the full-market label should not be claimed. However, the explicit wedge is **independent churches and small ministry teams that want a private, structured sermon-preparation workspace rather than a general chatbot**. This keeps the product to one buyer, one weekly workflow, and one primary outcome.

## PRD MVP

### Target customer

Pastor, ministry leader, or volunteer sermon-prep coordinator at an independent church with roughly 50–500 congregants.

### Primary outcome

Turn a topic, scripture reference, and existing notes into a cited, editable sermon package in under 15 minutes.

### P0

- Email/password login and one workspace
- Project creation with:
  - topic or scripture reference
  - sermon type
  - audience
  - denomination or theological style notes
  - desired length
- Source-grounded research:
  - retrieve selected public Bible and theological-reference sources
  - show source URLs and excerpts
  - distinguish retrieved evidence from generated commentary
- Sermon outline generation:
  - thesis
  - 3–5 sections
  - supporting points
  - scripture references
  - transition ideas
  - discussion questions
- Draft generator based on the approved outline
- Editing, copy, export to Markdown, PDF, and DOCX
- Denomination-specific style profile
- Usage counter and billing checkout
- Privacy controls: no training on customer content; configurable deletion

### P1

- Import of past sermon notes, PDFs, or DOCX files
- Scripture cross-reference suggestions with source citations
- Sermon series management and reusable templates
- Announcement and social-post drafts derived from the approved sermon
- Team sharing with basic roles

### P2

- Recording upload and transcription
- Presentation outline export
- Calendar integrations
- Custom knowledge-base ingestion
- Team analytics and content-library search

### Non-goals

- Replacing pastoral judgment or ministry credentials
- Generating sermons from a topic with no source review
- Full church-management, giving, CRM, or volunteer scheduling
- Video generation, websites, or social-post scheduling
- Multi-denomination marketplace templates
- Autonomous claims that generated theology is authoritative
- Native mobile apps

### Technical approach

- Web application with responsive layouts
- Authentication and billing through managed providers
- Server-side API key usage
- Retrieval layer restricted to a curated, versioned source catalog
- Structured JSON generation with schema validation
- Citation verification before export
- Usage-based cost controls
- Encryption in transit and at rest; delete uploaded content on request

### Pricing

- **Free trial:** 3 sermon projects per month
- **Solo:** $29/month
- **Ministry:** $59/month for five users
- **Early annual:** 20% discount after traction is demonstrated

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|---|
| 1 | Customer interviews and positioning | Five interviews; one recurring job and one source list confirmed |
| 2 | Clickable prototype and content schema | Testable research-to-outline workflow with three sample topics |
| 3 | Project setup, authentication, billing scaffold | A user can create a workspace and start a project |
| 4 | Curated source ingestion and retrieval | Each returned fact includes a URL and retrievable excerpt |
| 5 | Research panel and citation display | User can inspect sources and reject poor results |
| 6 | Structured outline generation | Valid outline generated for three test topics |
| 7 | Draft editor and template system | User can edit, regenerate a section, and export Markdown |
| 8 | DOCX/PDF export and error handling | Exported file preserves citations and readable formatting |
| 9 | Style profiles and guardrails | Profile changes output style without changing cited facts |
| 10 | Usage metering, limits, and spend caps | Usage cannot exceed configured budget |
| 11 | Admin diagnostics, privacy controls, deletion | Content deletion and retrieval diagnostics work |
| 12 | Landing page, checkout, onboarding | Visitor can purchase and reach first project unaided |
| 13 | End-to-end QA and load test | Ten concurrent users complete the core flow |
| 14 | Launch | Five design partners onboarded; daily metrics and feedback captured |

## 30-day marketing calendar

**Budget: $250 maximum**

| Day | Activity | Budget | KPI |
|---:|---|---:|---|
| 1 | Publish problem-focused landing page | $0 | 100 targeted visits |
| 2 | Post a before/after sermon outline demonstration | $0 | 20 qualified comments/DMs |
| 3 | Send personal outreach to 20 small-church leaders | $0 | 10 replies |
| 4 | Publish source-citation explainer | $0 | 5 demo requests |
| 5 | Host a 30-minute preparation workflow session | $0 | 8 attendees |
| 6 | Send onboarding workflow to interested users | $0 | 10 activated trials |
| 7 | Publish founder retrospective | $0 | 15 product-qualified leads |
| 8 | Ask five satisfied users for case-study interviews | $0 | 3 interviews |
| 9 | Publish anonymized case study | $0 | 8 qualified leads |
| 10 | Create a denomination-specific example page | $0 | 6 demo requests |
| 11 | Contact 20 church-content agencies | $0 | 8 replies |
| 12 | Publish a “what this tool will not do” trust post | $0 | 10 signups |
| 13 | Run a live sermon-outline clinic | $0 | 5 paid conversions |
| 14 | Review activation and interview feedback | $0 | 3 fixes prioritized |
| 15 | Publish changelog addressing objections | $0 | 8% trial-to-paid improvement |
| 16 | Reach 20 volunteer sermon coordinators | $0 | 10 replies |
| 17 | Publish short “prepare a series” video | $0 | 100 targeted views |
| 18 | Partner with one church communications newsletter | $50 | 50 new visitors |
| 19 | Run a referral prompt for existing users | $0 | 5 referrals |
| 20 | Publish FAQ from objection themes | $0 | 5 demo requests |
| 21 | Review channel cohorts and churn signals | $0 | Activation ≥50% |
| 22 | Contact five ministry coaches | $0 | 3 referral conversations |
| 23 | Publish comparison against generic AI workflows | $0 | 10 qualified leads |
| 24 | Sponsor one narrowly targeted church-ops newsletter | $100 | 8 demo requests |
| 25 | Offer annual-plan founding pricing | $0 | 3 annual conversions |
| 26 | Publish customer workflow video | $0 | 75 targeted views |
| 27 | Run a second live clinic | $0 | 10 attendees |
| 28 | Ask users for public testimonials | $0 | 3 usable testimonials |
| 29 | Optimize landing page from conversion data | $0 | Trial-to-paid ≥10% |
| 30 | Review MRR, retention, support load, and costs | $0 | Clear continue/iterate decision |

Budget allocation: $200 newsletters, $50 domain/creative tooling, $0 contingency required within the $300 cap.

### Organic channels

- Church founder and ministry-operations groups
- Direct outreach to independent pastors and volunteer coordinators
- YouTube demonstrations showing research, citations, and editing
- Partnerships with ministry coaches and church newsletter authors
- Public case studies with source-quality and time-saved metrics

## Unit economics to $10K MRR

### Conservative base case

- ARPA: $39/month blended
- Required paying customers:  
  `10,000 / 39 = 257`
- At $29/month only: 345 customers
- At $59/month only: 170 customers

### Illustrative funnel

- 10,000 qualified visitors over 90 days
- 5% activated trial: 500 users
- 12% trial-to-paid: 60 customers
- 25% referral-assisted: 15 additional customers
- Additional sales/outbound and audience expansion: 182 customers
- Result: approximately $10,011 MRR at $39 ARPA

### Cost assumptions

- Blended hosting, database, email, retrieval, and model cost: $4–$8 per active paid account per month
- Gross margin target: ≥70%
- Payment processing: approximately 3%
- Monthly paid-user support goal: under 15 minutes per account
- Target payback: under 60 days

### $10K MRR mix

- 150 Ministry accounts at $59 = $8,850
- 70 Solo accounts at $29 = $2,030
- 42 additional paid accounts at an average $27 = $1,134  
- Total: 258 customers and $12,014 MRR, providing margin against churn

### Sensible guardrails

- Do not promise $10K MRR within 14 days.
- No paid acquisition until activation and retention are proven.
- If paid CAC exceeds $150, rely on partnerships and referrals rather than scaling paid spend.
- Keep model cost below 20% of revenue.

## Kill criteria

Kill or materially reposition if any of the following occurs by day 30:

- Fewer than five of 20 target users report the same core preparation pain.
- Fewer than 30% of activated users generate a second project.
- Trial-to-paid conversion remains below 5% after 100 qualified trials.
- More than half of users prefer a general-purpose AI tool after seeing the product.
- Median generation time exceeds 90 seconds without an explanation.
- Citation accuracy is below 95% on a 100-point audit.
- Blended variable cost exceeds $12 per paying account per month.
- No design partner will prepay at least $29/month.
- The first 90 days produce fewer than ten paid customers despite 100 qualified conversations.
- Legal or theological-review concerns prevent the product from serving its intended audience.
