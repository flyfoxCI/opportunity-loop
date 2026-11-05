---
layout: post
title: "Faith Sermon Assistant — Product Direction"
date: 2026-11-05T22:33:25+00:00
week: "2026-11-05_223325"
week_date: "2026-11-05T22:33:25+00:00"
slug: "faith-sermon-assistant"
permalink: /directions/faith-sermon-assistant.html
tags:
  - "AI"
  - "religion"
  - "language"
  - "mobile"
excerpt: "An AI workspace that turns a pastor’s sermon source material into reusable church communications"
---

## Direction summary

Build an AI-assisted sermon and church-communications workspace for small churches and independent ministry leaders. The MVP turns a pastor’s notes, scripture references, transcript, or voice recording into a structured sermon draft, editable outline, plain-language summary, and reusable communication drafts.

The product is an editorial aid with human review, not an autonomous theology generator. Its initial users are small, nontechnical church leaders who lack a full communications team.

- **Tier:** GO
- **Demand:** 4/5
- **Competition:** 2/5
- **MVP horizon:** 14 days, solo
- **30-day marketing budget:** $0–$150
- **Target:** $10,000 MRR

## Why this direction

### TrustMRR evidence

The prior validated direction index reports a strong paid demand anchor in the faith-AI category:

- **Sermon Scribe:** approximately **$14K MRR**
- Approximately **2,362 paying customers**
- The prior report characterized direct competition as nearly absent

That is substantially stronger proof of willingness to pay than the Stage A rows for the anonymous or ambiguously named products. The evidence suggests the category can support a meaningful solo-built business if the founder reaches church leaders directly and avoids trying to build a broad theological or church-management suite.

The proposed product narrows the validated demand to the highest-frequency workflow: preparing a weekly sermon and related communications.

### X/web evidence and validation status

The supplied TinyFish output did not contain actual search results and therefore cannot be cited as X evidence.

Use these discovery sources before building:

- X searches for `sermon AI`, `sermon notes app`, `church AI tool`, `pastor content assistant`, and competitor complaints
- Church software forums and ministry-technology communities
- Public church-technology directories
- Interviews with pastors, worship leaders, ministry administrators, and volunteer communications staff

The minimum pre-build validation is:

1. Ten interviews with church leaders
2. Three people willing to review a working weekly workflow
3. One landing-page paid-intent test with at least 10% sign-up conversion among qualified visitors
4. At least one paid pilot

### Why this wedge is attractive

- A weekly cadence supports repeat usage and retention.
- The core workflow can be shipped with forms, transcription, structured prompts, and editing rather than complex integrations.
- Users understand the outcome before seeing the AI.
- The product can acquire users through ministry communities, referrals, and founder outreach without a large advertising budget.
- Human review and editorial controls make the product safer than autonomous theological advice.

## Competitor table

### L1 — direct competitors

| Competitor | Positioning | Typical pricing | Strength | Gap to exploit |
|---|---|---:|---|---|
| Sermon Scribe | AI sermon preparation | Prior research reports about $14K MRR with 2,362 payers | Direct validation and category leadership | Opportunity for a narrower, faster, workflow-first product aimed at small churches |
| Purposeful AI / Pulpit tools | Sermon and church-content generation | Varies; verify current plans | Content generation and possibly broad integrations | AI draft quality without a complete sermon-preparation workflow |
| ChatGPT / Claude plus templates | General-purpose drafting | $20+ monthly or API usage | Familiar, flexible, inexpensive at low volume | No repeatable church workflow, source organization, editing history, or reusable communications package |
| Sermon note and presentation apps | Notes, slides, scheduling | Free to $30/month | Established habit and integrations | Not centered on AI-assisted source-to-sermon preparation |

**Evidence caution:** the supplied TinyFish data is not a usable competitor search. Before committing build time, verify at least five live L1 alternatives and current pricing. If several offer the same source-to-sermon workflow at similarly low prices, preserve only an ICP-specific wedge such as one denomination, one sermon format, or bilingual congregations.

### L2 — indirect competitors

| Competitor | Positioning | Pricing pattern | Why users may choose it |
|---|---|---:|---|
| General LLM chat | Drafting | Subscription or API | No new tool required |
| Church management suites | Members, giving, schedules | $30–$200+/month | Already bundled into church operations |
| Volunteer or paid communications staff | Finished deliverables | Labor cost | Better judgment and local tone |
| Sermon presentation software | Slides and notes | Free/entry pricing | Strong visual workflow |

### L3 — substitutes

| Substitute | Limitation |
|---|---|
| Existing sermon notes | Time-consuming to transform into reusable content |
| Copying old sermons | Repetition, weak alignment with the current message |
| Generic prompt templates | Inconsistent structure and repeated setup |

## PRD MVP

### Target customer

A pastor, ministry leader, or volunteer serving a church with roughly 30–500 regular attendees and no dedicated content team. The persona should begin with one denomination or sermon style if research indicates a shared workflow.

### User promise

“Turn one week of source material into a structured sermon draft and communications package you can edit and publish.”

### P0 — required for launch

1. **Workspace**
   - Church or ministry name
   - Tone, audience, and theological/policy notes
   - Optional scripture translation and preferred sermon format

2. **Source capture**
   - Paste notes, transcript, scripture references, or outline
   - Upload plain text, PDF, DOCX, or Markdown where feasible
   - Audio recording upload with transcription for P1

3. **Sermon workspace**
   - Select source material and sermon goal
   - Generate title options, core thesis, outline, opening, transitions, illustration prompts, application, and closing
   - Show citations or source references used
   - Mark generated passages that need human verification

4. **Editing**
   - Rich-text or block-based editor
   - Regenerate selected sections rather than the full draft
   - Version save and copy/export

5. **Communications reuse**
   - Generate a bulletin summary, social post, email, and prayer request from the approved sermon draft
   - Channel-specific length controls

6. **Trust controls**
   - “Do not invent quotations or scripture” system instruction
   - Scripture-text sourcing where licensing permits
   - Citation panel and manual verification checklist
   - Disclaimer that the user reviews theology and factual claims

7. **Billing**
   - Stripe subscription
   - One free trial with a bounded generation quota
   - Cancellation and usage visibility

8. **Privacy**
   - Delete uploaded sermons and generated drafts
   - Clear terms for processing user content
   - No training on private church material without explicit consent

### P1 — first 30-day improvements

- Audio transcription
- Calendar-aware recurring sermon workflow
- Series support and consistency across weeks
- Scripture and source citation links
- Canva, ProPresenter, and Google Docs export
- One-click social variants
- Multiple ministry seats
- Spanish or another high-value secondary language

### P2 — later

- Service planning and volunteer rosters
- Presentation generation
- Website publishing
- Prayer-request triage
- Member messaging
- Denomination-specific templates
- Private team knowledge base

### Non-goals

- Autonomous sermon publishing
- Replacing a theology degree or pastoral counseling
- Generating unreviewed factual claims
- Full church management, CRM, giving, attendance, or donor management
- Worship-song licensing
- A general-purpose social media manager
- Denomination-specific administration in the MVP

### Core data model

- **Workspace:** id, owner, name, tone, policies, language
- **SermonProject:** id, workspace_id, title, date, goal, audience, status
- **Source:** id, sermon_project_id, type, content, created_at
- **Section:** id, sermon_project_id, kind, content, order, verified
- **Citation:** id, section_id, source_id, excerpt, verified
- **Derivative:** id, sermon_project_id, channel, content, approved
- **Generation:** id, sermon_project_id, model, prompt_version, token_usage, cost

### MVP architecture

- Next.js + TypeScript
- PostgreSQL
- LLM API with structured JSON responses
- Speech-to-text API if audio is included
- Rich editor such as Tiptap
- Stripe
- Resend/Postmark
- Sentry
- Object storage for uploaded files

### Initial pricing hypothesis

- **Starter:** $19/month, limited projects and generations
- **Church:** $49/month, multiple projects and communications outputs
- **Ministry team:** $99/month, seats, branding, and integrations

Validate prices through interviews and a paid pilot; do not assume pricing from competitors.

## 14-day day-by-day build plan

| Day | Deliverable | Exit criterion |
|---:|---|---|
| 1 | Interview five pastors; define one ICP and one sermon format | Identified repeated workflow and language |
| 2 | Design the sermon project and source-capture flow | Prototype tested with two users |
| 3 | Implement accounts, workspaces, and projects | User can create and reopen a project |
| 4 | Implement text/source ingestion and structured generation | Notes become a complete draft |
| 5 | Add editable sections and targeted regeneration | User can revise one section without losing the draft |
| 6 | Add citation/verification panel and content safeguards | Every generated section exposes its source context |
| 7 | Build communications derivatives and export | Approved draft yields four usable channel drafts |
| 8 | Add Stripe, quotas, onboarding, and account deletion | Paid trial can be purchased and canceled |
| 9 | Deploy, secure uploads, add logging, privacy controls | Production smoke test passes |
| 10 | Run three supervised live sermon workflows | Three completed sermons receive user feedback |
| 11 | Fix theology/format hallucination and usability issues | Critical unsupported claims reduced to zero in test set |
| 12 | Publish demo video, landing page, and FAQ | Visitor can understand flow in under two minutes |
| 13 | Recruit 15 qualified church leaders and run paid-intent test | Three signups and one paid order |
| 14 | Final QA and launch decision | At least one paid customer and no critical trust issues |

### MVP technical stack

- Next.js + TypeScript
- PostgreSQL
- Drizzle or Prisma
- Tiptap
- Anthropic/OpenAI structured output
- Whisper-compatible transcription
- Stripe
- Sentry
- Cloudflare R2 or S3-compatible object storage

## 30-day marketing calendar

**Budget: $150 maximum, organic-first**

| Day/channel | Action | Goal |
|---|---|---|
| Days 1–3 | Publish before/after demo: raw notes to editable sermon and social drafts | Establish the product’s concrete outcome |
| Days 4–6 | Personally interview 15 pastors and ministry leaders | Identify strongest denomination, format, and objections |
| Days 7–9 | Share demo in permitted ministry-technology communities | 150 qualified visits |
| Days 10–12 | Publish a free “sermon workflow checklist” and email template | 25 email signups |
| Days 13–15 | Invite first 10 churches to a guided pilot | Five completed workflows |
| Days 16–18 | Publish one before/after case study with approval | Credibility and referral requests |
| Days 19–21 | Ask pilot churches for testimonials and referrals | Two referrals or case-study quotes |
| Days 22–24 | Publish “How to review AI-generated sermons” educational content | Trust-led organic acquisition |
| Days 25–27 | Test $19 versus $49 checkout with qualified users | Five paid accounts |
| Days 28–30 | Review retention intent, output quality, cost, and support | Decide whether to scale, narrow, or kill |

### Channel mix

- Founder interviews and outreach: 35%
- Ministry communities: 25%
- Educational SEO content: 20%
- Customer referrals and case studies: 15%
- Small paid test: 5% ($50 maximum), only after landing-page intent is proven

### 30-day targets

- 50 qualified visitors
- 15 completed interviews or pilots
- 10 activated workspaces
- 5 paid customers
- At least $95–$145 MRR depending on plan mix
- 70% of pilots complete a second weekly workflow
- Median generation time below 90 seconds

## Unit economics to $10K MRR

### Base case

- Blended ARPA: **$49/month**
- Gross margin: **75%** after model, transcription, infrastructure, and email costs
- Monthly gross profit per customer: **$36.75**
- Monthly churn assumption: **6%**

Required customers:

**$10,000 ÷ $49 ≈ 204 customers**

At 75% gross margin, 204 customers provide approximately **$7,500 monthly gross profit** before salaries, support, and marketing.

### Pricing mix scenario

| Plan | Customers | Price | MRR |
|---|---:|---:|---:|
| Starter | 70 | $19 | $1,330 |
| Church | 104 | $49 | $5,096 |
| Ministry team | 30 | $99 | $2,970 |
| **Total** | **204** | — | **$9,396** |

Add 15 Pro accounts at $89/month to exceed the target:

- 70 × $19 = $1,330
- 110 × $49 = $5,390
- 25 × $99 = $2,475
- 15 × $89 = $1,335
- **Total MRR = $10,530**

### Cost assumptions

- LLM generation: approximately $8–$20 per active account depending on use
- Transcription: usage-based
- Infrastructure: $50–$200/month
- Email and monitoring: $20–$100/month
- Support: primarily founder time
- Payment fees: approximately 3%

### CAC constraint

With gross profit near $37 per account, a sustainable paid CAC should generally remain below **$50–$70** after accounting for churn. Organic referrals and ministry-community distribution are therefore important.

### Path to 204 customers

- 20 pilot churches
- 60 founder-assisted conversions
- 70 self-serve/community conversions
- 39 referral, partner, or ministry-network conversions
- 15 team-plan expansions

### Expansion revenue

- Additional seats and ministry teams
- Series and archive management
- Presentation/export integrations
- Website publishing
- Additional languages
- Denomination or organization templates
- Annual prepayment

## Kill criteria

Kill or pause if any of the following occurs by day 30:

- Fewer than 5 paid churches
- Fewer than 10 users complete a sermon workflow
- Fewer than 50% of pilots express intent to use it the following week
- Unsupported quotations or fabricated sources occur repeatedly after mitigation
- Median generation cost exceeds 25% of plan revenue
- Users prefer generic AI tools and will not switch
- The ICP fragments into many incompatible sermon workflows without a common dominant segment
- The product cannot be delivered safely without creating misleading religious or factual claims

### Decision checkpoints

- **Day 7:** one ICP, repeatable workflow, acceptable trust model
- **Day 14:** one paid customer and three complete workflows
- **Day 21:** five paid customers and stable generation cost
- **Day 30:** 10 active churches, 5 paid accounts, and credible path to 204 customers
