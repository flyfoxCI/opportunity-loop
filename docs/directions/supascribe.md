---
layout: post
title: "Supascribe — AI Newsletter Production Workspace"
date: 2026-10-26T21:22:34+00:00
week: "2026-10-26_212234"
week_date: "2026-10-26T21:22:34+00:00"
slug: "supascribe"
permalink: /directions/supascribe.html
tags:
  - "AI"
  - "creator"
  - "social"
  - "mobile"
excerpt: "Turn source material into publish-ready newsletters, with a focused solo-creator workflow."
---

## Tier

**GO**

- Demand: **4/5** (working hypothesis)
- Competition: **2/5** (narrow workflow hypothesis)
- MVP target: **14 days, solo**
- Marketing target: **≤ $300 over 30 days**
- Revenue target: **$10K MRR**

## Why this direction

### TrustMRR evidence

Stage A reports Supascribe at approximately **$24 MRR**, **$29.93 in trailing-30-day revenue**, and **158 subscribers**. That is meaningful paid validation for a small product and demonstrates that newsletter-production software can generate revenue. It is materially smaller than the $10K MRR target, so the product must expand from a single feature into a complete, high-frequency workflow.

### X/web evidence and validation plan

The supplied TinyFish capture did not contain usable search results—it returned the TinyFish CLI documentation for every query. Therefore, no X demand score can honestly be presented as independently verified. The Stage A hypothesis of demand 4 and competition 2 is retained provisionally because TrustMRR shows real revenue and because the chosen workflow has a narrow, observable ICP.

Before implementation beyond the first three days, run these searches manually and record dated evidence:

- `AI newsletter writing tool alternatives 2026`
- `newsletter AI pain expensive`
- `site:x.com newsletter writer "looking for"`
- `site:x.com newsletter workflow "too many tools"`
- `site:x.com "just shipped" newsletter AI`

Interview at least ten newsletter operators who publish at least weekly. Ask them to demonstrate their current production workflow and identify the most expensive or most error-prone step. A demand score of 4 requires recurring pain from at least seven of ten interviewees, repeated requests from at least five, and three paid preorders.

### Thesis

Newsletter creators lose time moving between research notes, source documents, drafts, editing, and distribution. A focused workspace should turn source material into a structured, editable newsletter draft, preserve citations, and export clean Markdown or HTML. The wedge is **source-to-draft editorial workflow**, not an all-purpose AI writing assistant.

## Competitor table

| Level | Competitor | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Beehiiv | Newsletter publishing, audience, analytics, and AI features | Free; paid plans vary by audience/feature | Strong distribution competitor; avoid competing as a newsletter platform |
| L1 | Kit | Newsletter creation and subscriber growth | Free tier plus paid tiers | Creator-focused workflow competitor; AI depth must be the wedge |
| L1 | Substack | Writing, publishing, subscriptions, and network effects | Free to publish; takes a platform fee | Not a direct feature alternative, but owns the customer workflow |
| L1 | Mailchimp | Broad email marketing suite | Entry paid tier varies by region; higher tiers materially more | Too broad for the MVP; do not reproduce automations |
| L2 | Typefully | Distraction-free writing and social repurposing | Free tier plus paid tiers | Strong workflow benchmark for tone and clean UX |
| L2 | Lavender | Email coaching, deliverability, and response assistance | Entry paid tier varies; higher tiers cost more | Narrow email-specific competitor; test instead of build broad coaching |
| L2 | NewsKit | AI-assisted newsletter creation and publishing | Paid subscription | Direct AI-newsletter competitor to verify on site |
| L3 | Jasper, Copy.ai, Writesonic | General AI copy generation | Usage tiers and monthly subscriptions | Commodity generation pressure; avoid generic prompt boxes |
| L3 | Notion AI, Grammarly, Hemingway | Notes, editing, and humanization | Subscription or usage-based | Compete on workflow completeness and source fidelity, not generic polish |

Pricing and feature availability must be rechecked immediately before launch. If two or more direct alternatives already provide source upload, outline, draft, revision, citations, and export at low prices, move this direction to WATCH.

## PRD MVP

### Target user and job to be done

**ICP:** Solo newsletter operators, niche newsletter writers, and small content teams publishing at least one substantial issue per week.

**JTBD:** “When I have several articles, interviews, notes, or links, I want a reliable source-backed draft so I can edit and publish without rebuilding the outline manually.”

### P0 — required for launch

1. **Source ingestion**
   - Paste text and URLs.
   - Upload PDF, Markdown, and plain-text files.
   - Store source metadata and original excerpts.
2. **Brief and outline**
   - Audience, topic, tone, target length, CTA, and desired structure.
   - Generate an editable outline.
3. **Draft generation**
   - Generate a newsletter draft from selected sources and outline.
   - Preserve source labels and offer basic source-attribution links.
4. **Inline editing**
   - Edit sections in a clean document interface.
   - Regenerate a selected section without replacing the entire draft.
5. **Quality and safety checks**
   - Flag unsupported factual claims against source excerpts.
   - Flag missing CTA, excessive length, and repeated phrases.
   - Clearly label AI-generated text.
6. **Export**
   - Copy to Markdown and HTML.
   - Download as `.md` and `.html`.
7. **Account and billing**
   - Magic-link authentication.
   - One paid subscription with a monthly generation allowance.
   - Usage dashboard and cancellation path.
8. **Privacy controls**
   - Clear notice that sources are processed by configured AI providers.
   - No source content used to train a public model.
   - Delete source and account data on request.

### P1 — after launch validation

- References library with reusable source snippets.
- Brand voice profile.
- Multiple draft variants.
- Collaborative comments.
- CSV and Markdown import from Beehiiv, Kit, and Typefully.
- Scheduled exports where provider APIs permit it.
- Export to Mailchimp, Beehiiv, or Kit via a basic HTML clipboard flow.

### P2 — later expansion

- Publishing integrations.
- Team roles and shared workspaces.
- Multi-language newsletters.
- Analytics-informed topic recommendations.
- Repurposing into social posts.
- Enterprise controls and audit logs.

### Non-goals

- Building a newsletter ESP or subscriber database.
- Sending campaigns.
- Building drag-and-drop email design.
- Social-media scheduling.
- Full web research crawler.
- General-purpose writing suite.
- Autonomous publishing without review.
- Guaranteed factual accuracy.
- Reproducing every Beehiiv, Kit, or Mailchimp feature.

### Core UX

1. Create a draft.
2. Add or paste sources.
3. Choose a brief and outline.
4. Generate the first draft.
5. Edit and run checks.
6. Export.

The happy path should take under ten minutes from first source to editable draft.

### Technical approach

- **Frontend:** Next.js + TypeScript + Tailwind CSS.
- **Backend/API:** Next.js route handlers, initially hosted with the web app.
- **Database/Auth:** Supabase or equivalent managed Postgres plus magic-link auth.
- **AI:** Model-agnostic provider adapter; start with one reliable model and structured JSON outputs.
- **Jobs:** Database-backed queue or managed task service for document extraction and long generations.
- **Storage:** Private object storage for uploads.
- **Payments:** Stripe Checkout and billing portal.
- **Observability:** Error tracking, structured logs, latency, token usage, and generation-to-export funnel.

### Core data model

- `users`
- `workspaces`
- `drafts`
- `sources`
- `source_chunks`
- `briefs`
- `sections`
- `citations`
- `generation_jobs`
- `subscriptions`
- `usage_events`

### AI quality strategy

- Chunk and label each source separately.
- Require the model to cite supporting source IDs for factual passages.
- Run a second structured verification pass that classifies claims as supported, contradicted, or unsupported.
- Store prompts, model version, source IDs, and generation metadata for debugging.
- Test against a fixed set of 30 newsletters and maintain a weekly quality rubric.
- Never silently fabricate citations.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criteria |
|---:|---|---|
| 1 | Customer validation and competitor spot-check | Ten interviews scheduled/completed where possible; ten direct workflows manually checked; wedge documented |
| 2 | Scope lock and prototype | Clickable source-to-export flow; P0 list frozen; three sample newsletters selected as fixtures |
| 3 | Landing-page smoke test | One-page site with email capture and fake-door checkout; visit-to-signup target ≥8% |
| 4 | Authentication and project shell | Magic-link login; workspace creation; empty and populated project states |
| 5 | Source ingestion | Text, URL, PDF, Markdown, and file upload; private storage; per-source status and deletion |
| 6 | Extraction and retrieval | Source chunks, labels, metadata, and retrieval tests against five fixture documents |
| 7 | Brief, outline, and first draft | Structured brief form; editable outline; reliable first-draft generation with citations |
| 8 | Editing and section regeneration | Section-level edits, regenerate, undo, and autosave work without corrupting references |
| 9 | Verification and export | Claim checks, CTA/length checks, Markdown and HTML export; sample output reviewed manually |
| 10 | Billing, quotas, and telemetry | Stripe subscription, usage limits, cancellation, generation and export events |
| 11 | Reliability and abuse controls | Retry logic, rate limits, upload validation, prompt-injection boundaries, deletion workflow |
| 12 | UX polish and accessibility | Keyboard navigation, focus states, mobile layout, loading/empty/error states |
| 13 | End-to-end and security test | New user completes source-to-paid-export path; billing webhooks, permissions, and uploads tested |
| 14 | Launch readiness | 10 dogfood issues, backups configured, monitoring live, landing copy and onboarding final |

### Definition of done for day 14

A new user can sign up, import at least two sources, generate and edit a cited draft, pass quality checks, export HTML/Markdown, subscribe, and later cancel without founder intervention.

## 30-day marketing calendar

### Marketing thesis

Organic-first distribution should focus on operators who publicly discuss newsletter production, not generic AI audiences. Lead with a free “source bundle to newsletter brief” workflow, publish transparent output examples, and ask every satisfied user for a referral.

### Budget: $200 maximum

| Item | Budget |
|---|---:|
| Domain, email, and demo assets | $40 |
| Newsletter/community sponsorship of one highly targeted creator | $100 |
| Micro-creator content swaps and product seeding | $40 |
| Contingency | $20 |
| **Total** | **$200** |

No paid ads during the first 30 days.

### Calendar

| Day | Action | Target |
|---:|---|---|
| 1 | Launch “From messy sources to a cited newsletter draft” landing page | 100 qualified visits |
| 2 | Publish a before/after sample issue | 10 qualified comments or replies |
| 3 | Contact 20 solo newsletter writers with a personalized workflow example | 5 conversations |
| 4 | Share founder teardown: three draft-quality failures and fixes | 5 qualified signups |
| 5 | Post in one carefully selected newsletter-operator community | 10 trial starts |
| 6 | Offer five free on-brand source-to-draft productions | 5 testimonials or permission requests |
| 7 | Review signup-to-export funnel and fix the largest drop-off | ≥25% source-to-export rate |
| 8 | Publish a comparison against generic prompt-based workflows | 8 qualified leads |
| 9 | Contact five creator educators or newsletter consultants | 2 referral partnerships |
| 10 | Add one-click import from a Markdown or PDF workflow | 10 more trials |
| 11 | Publish a benchmark: cited versus uncited draft accuracy | 3 shareable quotes |
| 12 | Run a live 30-minute source-to-draft workshop | 10 attendees, 3 trials |
| 13 | Send an in-product prompt to complete the second draft | ≥30% second-project rate |
| 14 | Review activation, quality, and support burden | Fix top two defects |
| 15 | Publish five niche-specific prompt templates | 8 signups from templates |
| 16 | Partner with one newsletter educator | Co-branded demo |
| 17 | Publish a customer teardown | 5 referral conversations |
| 18 | Add a free output-quality report to exports | Increase sharing |
| 19 | Contact 20 former trial users who did not export | 5 interviews |
| 20 | Publish the findings from those interviews | 10 qualified discussions |
| 21 | Run a second workshop with a different vertical | 5 paid conversions |
| 22 | Launch a referral loop: export credit for both sides | 10 referred trials |
| 23 | Create a public comparison against email-coaching tools | 8 qualified leads |
| 24 | Improve onboarding based on day-14 cohort behavior | Activation +10% |
| 25 | Publish founder notes on source fidelity and citations | 5 inbound leads |
| 26 | Offer a limited annual-plan discount to active trials | 3 paid conversions |
| 27 | Recruit two micro-creators for documented workflows | 2 posts published |
| 28 | Publish the strongest customer before/after result | 10 qualified signups |
| 29 | Review conversion, retention intent, and support load | Kill/pivot decision on target metrics |
| 30 | Plan month two from retained-user feedback | 20 qualified pipeline leads |

### Weekly content pillars

1. **Workflow teardown:** how a messy source bundle becomes a structured issue.
2. **Quality proof:** citations, claim verification, and editorial control.
3. **Founder build notes:** transparent failures and workflow discoveries.
4. **Customer stories:** time saved without abandoning the writer’s voice.

### Activation and funnel targets

- Visitor → email signup: **≥8%**
- Signup → source added: **≥60%**
- Source added → draft generated: **≥50%**
- Generated → export: **≥50%**
- Activated visitor → paid: **≥5%**
- Paid → second export within 30 days: **≥60%**
- Paid monthly logo churn: **<8%**

## Unit economics to $10K MRR

### Pricing

- **Starter:** $15/month — 10 documents, 30 generations, Markdown/HTML export
- **Pro:** $39/month — 40 documents, 150 generations, brand profile, priority processing
- **Studio:** $79/month — shared workspace, 100 documents, 400 generations, comments

### Revenue mix at target

| Plan | Customers | MRR |
|---|---:|---:|
| Starter | 140 | $2,100 |
| Pro | 180 | $7,020 |
| Studio | 11 | $869 |
| **Total** | **331** | **$9,989** |

Round the plan to **332 paying customers for approximately $10K MRR**.

### Cost assumptions

For a typical Pro customer:

- 60 generations/month
- Average blended model cost: $0.035/generation
- Model cost: $2.10/month
- Storage and extraction: $0.50/month
- Email, monitoring, and payment processing before payment fees: $0.40/month
- Gross contribution before acquisition: approximately $36

Illustrative blended infrastructure and processing cost: **$3.00/customer/month**.

### Gross margin and acquisition

At the target mix, estimated MRR is approximately $10,000 and estimated variable processing cost is approximately $996.

- **Gross margin:** approximately 90%
- **Allowable blended CAC:** use a 3-month gross-margin payback ceiling of about **$90**
- **Target blended CAC:** **≤$45**
- **Required monthly paid acquisitions:** approximately 50–75, depending on churn and conversion

Organic-first economics depend on referrals, community distribution, creator partnerships, and founder-led outreach. If effective CAC exceeds $90 or three-month retention is under 55%, do not scale paid acquisition.

### Validation milestone

Before treating the plan as viable, acquire at least **30 paid customers** and observe at least **$1,000 MRR**. At that point, projected CAC and retention should be computed from actual cohort data rather than assumptions.

## Kill criteria

Kill or reposition the direction if any of the following occurs:

1. Fewer than **3 paid preorders** from 30 qualified interviewees.
2. Fewer than **20 activated users** from 300 qualified landing-page visitors within 30 days.
3. Activated-to-paid conversion below **3%** after two onboarding iterations.
4. More than **20%** of generated drafts require complete manual rewrite because of factual or structural errors.
5. Source-grounding or citation tests fall below **85%** supported-claim accuracy.
6. Paid monthly churn exceeds **10%** in the first 50-customer cohort.
7. Effective CAC exceeds **$90**, or three-month gross-margin payback exceeds 120 days.
8. A direct low-price alternative already provides materially better source-grounded drafting and editing.
9. API and infrastructure costs exceed **15% of revenue**.
10. Users primarily want autonomous publishing or a full ESP; that would invalidate the narrow wedge.
