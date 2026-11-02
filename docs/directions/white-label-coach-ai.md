---
layout: post
title: "White-Label Coach AI"
date: 2026-11-02T23:47:21+00:00
week: "2026-11-02_234721"
week_date: "2026-11-02T23:47:21+00:00"
slug: "white-label-coach-ai"
permalink: /directions/white-label-coach-ai.html
tags:
  - "AI"
  - "SaaS"
  - "B2B"
  - "mobile"
  - "vertical"
excerpt: "Branded AI knowledge and client-delivery assistant for professional coaches"
---

## Why this direction

### TrustMRR evidence

- The prior validated direction index cites **Tradevipe at approximately $2.9K MRR from only 14 customers**, demonstrating meaningful B2B willingness to pay for a white-label vertical SaaS product.
- The economics are attractive because each customer can represent multiple end users while retaining recurring software revenue.
- The prior review identified a gap around narrowly branded, vertical-specific assistant products rather than generic chatbot builders.
- A smaller opportunity can still satisfy the hard target: 50 customers at $199/month reaches $9,950 MRR before expansion revenue.

### X/web evidence

- Coaches and boutique consultancies repeatedly report difficulty delivering consistent client work without becoming full-time software operators.
- Common pain themes are onboarding materials, client FAQs, document generation, progress summaries, and branded knowledge assistants.
- General-purpose builders are plentiful, so the demand signal is strongest where a buyer can deploy in one click and keep the assistant branded for their own clients.
- Pre-launch searches should target:
  - `white label AI coach`
  - `client portal AI assistant`
  - `coaching AI knowledge base`
  - `AI assistant hate pricing`
  - `white label AI just shipped`
- The MVP should solve knowledge-backed client delivery, not attempt to be a complete coaching CRM.

## Competitor table

| Level | Product | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Tradevipe | Branded vertical B2B workflow/lead product | Around $99–$199+/month inferred from prior research; verify | Commercial proof and closest benchmark |
| L1 | Botpress | Visual AI-agent builder | Paid plans plus usage-based costs | General platform; potential direct competitor |
| L1 | Tidio Lyro | Customer-service AI agent | Subscription plus message usage | Strong alternative for support use cases |
| L1 | Zendesk AI | Enterprise service AI | Tiered enterprise pricing | Powerful but expensive and complex |
| L2 | Voiceflow | Conversational agent builder | Paid plans plus usage | Broader workflow platform |
| L2 | Make / Zapier + OpenAI | DIY automation stacks | Subscription plus API costs | Strong low-code substitute |
| L2 | ManyChat | Messaging and lead automation | Subscription plus contacts/features | Adjacent marketing platform |
| L3 | ChatGPT, Claude, Google Drive, Notion | Manual content and client-delivery workflows | Subscription tiers | Low-cost substitute; export and branding are key |

### Competitive conclusion

The opportunity is narrow but viable: **one brandable client-delivery assistant for professional coaches**, beginning with one coaching niche. It avoids generic no-code agent building and focuses on content ingestion, citations, client-safe outputs, and deployment under a coach’s identity.

## PRD MVP

### Target customer

Independent coach or small consultancy with 5–50 active clients, a repeatable methodology, and recurring questions or document-delivery needs.

### Primary outcome

Deploy a branded, source-backed assistant that helps clients get answers and complete next steps without exposing the coach to repetitive work.

### P0

- Tenant onboarding:
  - business name
  - logo and colors
  - subdomain or branded share link
  - tone instructions
- Knowledge ingestion:
  - PDF, DOCX, Markdown, web URL
  - extraction, chunking, indexing
  - source citations
- Assistant experience:
  - scope-aware retrieval
  - answer with citations
  - “not in knowledge base” behavior
  - suggested next action
- Customization:
  - system instructions
  - tone
  - starter prompts
  - escalation message
- Usage:
  - message count
  - active users
  - monthly limit
  - soft quota warnings
- Billing and tenant isolation
- Admin dashboard for knowledge sources, prompts, analytics, and billing
- Embeddable widget or share-link chat
- CSV export of conversations and unanswered questions

### P1

- Document generation from approved templates
- Weekly client progress summary
- Branded email delivery
- Knowledge-source approval workflow
- Multiple coaches or admins per tenant
- Client-specific context

### P2

- Calendar integration
- Custom domain
- Zapier integration
- Program-specific workspaces
- White-label mobile wrapper
- Multi-language support

### Non-goals

- Replacing a full CRM
- Therapy, medical, legal, or financial advice
- Unrestricted autonomous outreach
- Generic chatbot-builder canvas
- Training customer-specific models
- A marketplace of templates in the MVP
- Native iOS or Android apps
- Fully automated high-stakes coaching decisions

### Technical approach

- Multi-tenant web application
- Managed authentication, database, file storage, and payments
- Retrieval with tenant-scoped access
- Answer generation with inline source links
- Usage metering and hard monthly caps
- Branded widget loaded from a first-party route
- Background jobs for document ingestion
- Daily deletion of failed or abandoned ingestion artifacts

### Pricing

- **Starter:** $99/month, one coach, 1,000 messages
- **Professional:** $199/month, three coaches, 5,000 messages
- **Scale:** $399/month, ten coaches, custom usage allowance
- One-time setup fee of $299, waived for the first five design partners

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|---|
| 1 | Interview five coaches and select one niche | One repeated client-delivery job confirmed |
| 2 | Prototype branded assistant workflow | Testable chat with visible citations |
| 3 | Tenant model, authentication, and billing scaffold | Two isolated tenants cannot access each other’s data |
| 4 | File upload and extraction | PDF, DOCX, and Markdown upload successfully |
| 5 | Tenant-scoped retrieval | Retrieval never returns another tenant’s document |
| 6 | Cited answer generation | Every factual answer links to an approved source |
| 7 | Branding and tone controls | Three brands visibly render correctly |
| 8 | Starter prompts and refusal behavior | Unsupported questions are escalated safely |
| 9 | Usage metering and quota enforcement | Usage reaches the limit and additional requests are blocked |
| 10 | Admin dashboard and source management | Coach can add, inspect, and disable sources |
| 11 | Share-link/embed and responsive UI | Client can use the assistant on mobile and desktop |
| 12 | Checkout, onboarding, and data deletion | New customer can deploy and delete content |
| 13 | End-to-end QA and penetration spot-check | Tenant isolation and billing flows pass |
| 14 | Pilot launch | Five design partners deploy real client assistants |

## 30-day marketing calendar

**Budget: $280 maximum**

| Day | Activity | Budget | KPI |
|---:|---|---:|---|
| 1 | Publish narrow-ICP landing page | $0 | 100 targeted visits |
| 2 | Record two-minute branded assistant demo | $0 | 10 product-qualified leads |
| 3 | Personally contact 20 coaches in selected niche | $0 | 8 replies |
| 4 | Publish knowledge-base setup guide | $0 | 5 demos |
| 5 | Run a live client-onboarding simulation | $0 | 8 attendees |
| 6 | Offer five design-partner seats | $0 | 5 onboarded pilots |
| 7 | Publish pilot before/after metrics | $0 | 12 qualified leads |
| 8 | Ask pilots for quantified time-saved evidence | $0 | 3 case studies |
| 9 | Publish use-case page for the chosen niche | $0 | 8 demos |
| 10 | Contact 15 relevant professional associations | $0 | 4 conversations |
| 11 | Send setup checklist to interested coaches | $0 | 15 activations |
| 12 | Publish security and tenant-isolation explainer | $0 | 5 objections resolved |
| 13 | Host onboarding clinic | $0 | 5 paid conversions |
| 14 | Review activation by source | $0 | 40% activated-to-deployed |
| 15 | Publish first customer case study | $0 | 10 qualified leads |
| 16 | Ask five customers for referrals | $0 | 4 referrals |
| 17 | Sponsor a niche coaching newsletter | $75 | 8 demo requests |
| 18 | Publish “why not Zapier + ChatGPT” comparison | $0 | 6 leads |
| 19 | Contact 10 consultants who serve coaches | $0 | 5 agency conversations |
| 20 | Add a 10-minute setup video | $0 | 75 targeted views |
| 21 | Review unanswered-question reports | $0 | 10 content improvements |
| 22 | Invite agency partners to resell | $0 | 2 active partners |
| 23 | Publish escalation workflow template | $0 | 8 trials |
| 24 | Sponsor a second narrow newsletter placement | $75 | 8 leads |
| 25 | Run a portfolio-building workshop | $0 | 12 attendees |
| 26 | Request annual-plan commitment from pilots | $0 | 3 annual conversions |
| 27 | Publish migration guide from generic bots | $0 | 7 demos |
| 28 | Collect testimonials and objections | $0 | 3 testimonials |
| 29 | Optimize pricing page and onboarding | $0 | Trial-to-paid ≥10% |
| 30 | Review MRR, retention, and support load | $0 | Continue/iterate decision |

Budget allocation: $225 newsletter placements, $55 demo/production tools, $0 contingency.

### Organic channels

- Direct outreach to coaches and consultants
- Professional associations for the selected niche
- Partnership with coaches who already advise other coaches
- LinkedIn demonstrations and founder teardown posts
- Referral program for paid coaches
- Short video walkthroughs of knowledge ingestion and branding

## Unit economics to $10K MRR

### Base case

- Blended ARPA: $199/month
- Customers required:  
  `10,000 / 199 = 51`
- Scenario: 50 Professional customers at $199 = $9,950, plus one Scale customer at $399 = $10,349 MRR

### Funnel

- 1,500 qualified leads over 90 days
- 35% demo rate: 525
- 50% demo-to-paid: 263 theoretical, adjusted for capacity and trust
- Realistic target: 51 paying customers

### Cost model

- Hosting, database, storage, email, and observability: $15–$30 per tenant/month
- Retrieval/model usage at 5,000 messages: target ≤$35 per tenant/month
- Payment processing: approximately 3%
- Gross margin target: ≥70%
- Human support target: under 30 minutes per customer per month

### $10K MRR mix

- 40 Professional customers at $199 = $7,960
- 8 Starter customers at $99 = $792
- 3 Scale customers at $399 = $1,197
- Total: 51 customers and $9,949 MRR
- 51 Scale customers would produce $20,349 MRR but is not required

### Guardrails

- No broad drag-and-drop bot builder in the MVP.
- Cap included usage so token costs cannot erase margin.
- Do not count setup fees in recurring MRR.
- Do not scale paid ads before retention is demonstrated.
- Verify that end users perceive clear value, not merely that the coach does.

## Kill criteria

Kill or reposition if any of the following occurs by day 30:

- Fewer than five of 20 coaches share the same high-frequency client-delivery job.
- Fewer than three design partners upload their own real methodology.
- Fewer than 60% of deployed assistants receive a second weekly session.
- Trial-to-paid conversion is below 8% after 50 qualified demos.
- More than 30% of conversations require immediate coach intervention.
- Median first useful response exceeds 10 seconds.
- Blended variable cost exceeds $55 per customer at the $199 tier.
- Ten prospects reject the product because of setup friction rather than feature gaps.
- Fewer than 10 customers remain active after 30 days.
- No agency or coach will pay at least $99/month.
- Security testing finds a material cross-tenant data exposure that cannot be fixed before launch.
