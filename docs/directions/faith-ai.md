---
layout: post
title: "Faith AI — Sermon and Ministry Study Production Assistant"
date: 2026-10-26T21:22:34+00:00
week: "2026-10-26_212234"
week_date: "2026-10-26T21:22:34+00:00"
slug: "faith-ai"
permalink: /directions/faith-ai.html
tags:
  - "AI"
  - "B2B"
  - "religion"
  - "social"
  - "mobile"
  - "vertical"
excerpt: "Help faith leaders turn services, notes, and recordings into reusable sermon and study materials."
---

## Tier

**GO**

- Demand: **4/5** (prior-research hypothesis; X verification pending)
- Competition: **2/5** (prior-research hypothesis; desktop research only)
- MVP target: **14 days, solo**
- Marketing target: **≤ $300 over 30 days**
- Revenue target: **$10K MRR**

## Why this direction

### TrustMRR evidence

The prior validated research identifies **Sermon Scribe** as a direct proof point with approximately **$14K MRR and 2,362 paid customers**. This is the strongest revenue signal in the seeded research and directly supports a $10K MRR target. The current Stage A candidate pool did not include Sermon Scribe as a GO_CANDIDATE, so this direction is used as a prior validated niche to provide the required selectable count.

### X/web evidence and validation plan

The prior research cites sermon-scribe and broad market validation, but the supplied TinyFish evidence is invalid for demand verification. Do not represent the prior desktop research as X verification.

Run these searches before implementation:

- `AI sermon preparation tool alternatives 2026`
- `sermon preparation AI pain expensive`
- `site:x.com pastor "sermon notes" AI`
- `site:x.com ministry "looking for" sermon tool`
- `site:x.com "just shipped" sermon AI`
- `site:x.com church AI "AI detector"`

Interview at least 15 ministry workers across small churches, ministry teams, and independent ministry educators. Demand score 4 requires at least 11 to report repeated pain, eight to agree to test, and five to prepay or sign a paid pilot letter. Use separate interviews for volunteer and paid ministry roles because purchasing authority differs.

### Thesis

Faith leaders repeatedly prepare sermons, lessons, devotionals, and small-group material from notes, Scripture references, prior messages, and personal theological context. Generic AI tools either lose denominational voice or create unsupported theological claims. A focused assistant should transform a pastor’s own notes into a structured outline and first draft while making source grounding and human review explicit.

The wedge is **faith-leader content preparation**, not a general theology chatbot, church-management system, or autonomous preaching generator.

## Competitor table

| Level | Competitor | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Sermon Scribe | Sermon preparation and content generation | Subscription tiers | Strongest direct benchmark; prior research indicates substantial paid traction |
| L1 | Pulpit AI | AI sermon preparation and presentation tools | Free/entry and paid tiers | Direct ministry-specific competitor; verify exact workflow and price |
| L1 | PreachingAI | AI-assisted sermon preparation | Free/entry plus paid use | Likely direct competitor for pastors; verify differentiation |
| L1 | ChatGPT / Claude | General-purpose drafting | Subscription tiers | Ubiquitous substitute; must win on ministry workflow, structure, and provenance |
| L2 | Sermonary | Sermon notes, ideas, and research for preachers | Free or freemium | Research/reference competitor and trust benchmark |
| L2 | Sermon Notes | Templated sermon-note resources | Free/freemium | Establishes expected note structure |
| L3 | YouTube, Google Docs, Evernote, Notion | Manual or generic content workflows | Free/freemium | The real incumbent is often a manual workflow |
| L3 | Faithlife, Logos, BibleHub | Scripture and theological reference | Subscription/free | Complementary rather than direct drafting competitors |
| L3 | Descript, Otter, Fireflies | Sermon recording transcription | Subscription tiers | Potentially complementary ingestion sources |
| L3 | Church Online Platform, Planning Center | Ministry operations and communications | Subscription tiers | Adjacent suites; do not attempt administration |

The category is not empty. Treat the prior competition score of 2 as a hypothesis for a narrow, non-hallucinating workflow—not a claim that no alternatives exist. If two direct tools provide source-grounded sermon outlines, theological review, and denomination-aware voice at comparable prices, narrow further to a specific ICP such as volunteer-led small churches or multilingual ministry teams.

## PRD MVP

### Target user and job to be done

**ICP:** Working pastors, ministry leaders, and volunteer sermon-preparation teams at independent churches and small ministries.

**JTBD:** “When I am preparing a message or lesson, I want to turn my notes and approved sources into a structured first draft so I can spend more time on pastoral care and less time organizing material.”

### P0 — required for launch

1. **Project setup**
   - Title, audience, ministry context, tradition, tone, length, and theological boundaries.
2. **Source ingestion**
   - Paste notes, transcripts, Bible passages, and links.
   - Upload Markdown, PDF, and plain-text files.
   - Label source type and attribution.
3. **Outline generation**
   - Big idea, purpose, scripture references, introduction, main points, transitions, application, and close.
   - Editable section-by-section outline.
4. **First-draft generation**
   - Generate prose from the approved outline and selected sources.
   - Maintain a user-selected voice profile.
5. **Grounding panel**
   - Link draft passages to source excerpts.
   - Flag claims not supported by the supplied sources.
   - Mark Scripture references for manual verification.
6. **Editing**
   - Section-level rewrite, expansion, shortening, and alternate examples.
   - Autosave and version history.
7. **Export**
   - Markdown, plain text, and PDF-friendly HTML.
   - Speaker notes and copy-ready outline.
8. **Account and billing**
   - Magic-link authentication.
   - Free allowance and Stripe subscription.
9. **Privacy and safeguards**
   - Explicitly state that the tool does not provide pastoral, doctrinal, or legal advice.
   - No public training on user content.
   - Delete sources and drafts on request.
   - Provide a visible “review Scripture and sources before use” disclaimer.

### P1 — after launch validation

- Denomination-aware tone templates.
- Recurring series templates.
- Transcript import from supported sources.
- Scripture-reference verification against an approved translation.
- Prayer and discussion-question generation.
- Small-group guide export.
- Bilingual output.
- Reusable ministry voice profile.
- Team comments and shared projects.
- Calendar and recurring project template.

### P2 — later expansion

- Presentation slides.
- Video and social repurposing.
- Liturgical calendar support.
- Team and denomination workspaces.
- Reading plans.
- Youth and children’s ministry variants.
- Integrations with church software.
- Private institutional knowledge bases.
- Multi-speaker sermon series planning.

### Non-goals

- Church management.
- CRM or member records.
- Attendance tracking.
- Giving or donations.
- Song-selecting software.
- General theological advice.
- A substitute for biblical study or pastoral discernment.
- Autonomous sermon publication.
- Claims of theological accuracy.
- Denominational judgment.
- Large model training from private ministry material.
- Broad all-audience AI content suite in MVP.

### Core UX

1. Create a project.
2. Add the minister’s notes and approved sources.
3. Choose structure and tone.
4. Review the outline.
5. Generate the first draft.
6. Inspect grounding warnings.
7. Edit and export.

The minimum useful path should take under 15 minutes.

### Technical approach

- **Frontend:** Next.js + TypeScript + Tailwind CSS.
- **API:** Next.js route handlers and a managed job queue.
- **Database/Auth:** Managed Postgres and magic-link authentication.
- **AI:** One provider with strong long-context and structured-output support; provider abstraction retained.
- **Retrieval:** Source chunking, citations, and per-section grounding.
- **Storage:** Private object storage.
- **Payments:** Stripe.
- **Observability:** Generation latency, source failures, hallucination-review outcomes, export events, and support errors.

### Core data model

- `users`
- `ministry_profiles`
- `projects`
- `sources`
- `source_chunks`
- `outlines`
- `sections`
- `draft_versions`
- `citations`
- `generation_jobs`
- `subscriptions`
- `usage_events`

### AI quality strategy

- Require every factual assertion to carry source IDs or be marked as a user-supplied claim.
- Use a two-pass workflow: generate from approved sources, then verify against source chunks.
- Separate Scripture quotations from paraphrases.
- Never invent quotations or page references.
- Provide a warning rather than a definitive theological judgment.
- Maintain a test corpus of 30 sermons across traditions with a human-review rubric.
- Require explicit user approval of the outline before long-form generation.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criteria |
|---:|---|---|
| 1 | Pastoral customer discovery | Fifteen interviews, five paid-intent signals, and exact workflow mapping |
| 2 | Ethical and scope review | Denominational boundaries, content policy, prohibited use cases, and competitor map agreed |
| 3 | Landing-page smoke test | Two clearly separated ICP variants; email capture and paid-intent form live |
| 4 | Auth and project shell | Magic-link auth, profile, project creation, and autosave |
| 5 | Notes and source ingestion | Text, URL, PDF, Markdown, upload, source labels, and private storage |
| 6 | Extraction and grounding pipeline | Chunking, retrieval, citation IDs, and fixtures from five sermons |
| 7 | Outline generation | Editable structured outline with purpose, points, transitions, and application |
| 8 | Draft generation | Reliable long-form generation; section controls; no unsupported quotation policy |
| 9 | Grounding review | Source comparison, unsupported-claim flags, Scripture reference verification list |
| 10 | Editing and export | Rewrite controls, version history, Markdown/text/HTML export |
| 11 | Billing, quotas, and email | Stripe, free allowance, usage meter, invoices, cancellation, passwordless email |
| 12 | Reliability and privacy testing | Prompt-injection checks, file validation, deletion, backup, and failure recovery |
| 13 | Accessibility and pastoral review | Keyboard/screen-reader pass; five outputs reviewed by actual ministry users |
| 14 | Launch readiness | Ten end-to-end tests, monitoring, support playbook, ethics copy, and demo content |

### Definition of done for day 14

A ministry leader can create a project, import notes and sources, review an editable outline, generate a grounded first draft, inspect warnings, edit it, export it, subscribe, and delete their data.

## 30-day marketing calendar

### Marketing thesis

Ministry buyers trust peer recommendations, denominational communities, and transparent demonstrations more than generic AI ads. Use the product to solve one workflow—first draft and outline—rather than claiming theological authority.

### Budget: $280 maximum

| Item | Budget |
|---|---:|
| Domain, email, and sample audio/video assets | $50 |
| One ministry newsletter or podcast sponsorship | $120 |
| Ministry community or creator sponsorship | $60 |
| Production/design help | $30 |
| Contingency | $20 |
| **Total** | **$280** |

### Calendar

| Day | Action | Target |
|---:|---|---|
| 1 | Launch “sermon notes to a grounded first draft” page | 80 qualified visits |
| 2 | Publish a complete before/after example | 8 ministry conversations |
| 3 | Contact 20 independent pastors | 6 calls |
| 4 | Post in one pastor or ministry community | 10 signups |
| 5 | Run a 30-minute sermon-prep workshop | 12 attendees, 4 trials |
| 6 | Offer five free sermon workflow reviews | 3 testimonials |
| 7 | Review activation and pastoral trust feedback | Fix top two issues |
| 8 | Publish “what the tool does—and does not—do” | 10 qualified leads |
| 9 | Contact ministry educators and podcasters | 2 partnerships |
| 10 | Add a recurring sermon-series template | 8 activated users |
| 11 | Share a transparent source-grounding demo | 6 signups |
| 12 | Interview five users who generated but did not export | 5 interviews |
| 13 | Add speaker-notes export | 5 exports |
| 14 | Mid-month review | 20 activated accounts, 2 paid conversions |
| 15 | Publish a sermon-series planning example | 8 qualified leads |
| 16 | Sponsor a ministry newsletter segment | 300 targeted impressions |
| 17 | Contact 20 volunteer ministry leaders | 8 calls |
| 18 | Publish “voice profile” case study | 4 referrals |
| 19 | Offer a two-week paid pilot to high-intent users | 5 paid conversions |
| 20 | Run a second workshop for ministry educators | 10 attendees |
| 21 | Improve source-warning workflow | Export completion +10% |
| 22 | Publish a failure-analysis post about hallucination prevention | 8 shares |
| 23 | Contact church-resource creators | 3 collaboration offers |
| 24 | Review retention intent and trust concerns | Resolve top three objections |
| 25 | Add a small-group discussion-guide export | 5 activations |
| 26 | Publish a customer workflow story | 6 leads |
| 27 | Run referral program for ministry teams | 10 referred trials |
| 28 | Improve first-project onboarding | Activation ≥35% |
| 29 | Offer annual pricing to paid users | 2 upgrades |
| 30 | Month-two review | 30 activated accounts and $500 MRR |

### Weekly content pillars

1. **Workflow demos:** notes to outline to editable draft.
2. **Trust and grounding:** how citations and review warnings work.
3. **Ministry efficiency:** time saved without implying replacement of pastoral judgment.
4. **User stories:** real preparation workflows and their limitations.

### Activation and funnel targets

- Visitor → signup: **≥10%**
- Signup → source added: **≥65%**
- Source added → outline generated: **≥55%**
- Outline approved → draft generated: **≥75%**
- Draft generated → export: **≥50%**
- Activated → paid: **≥5%**
- Paid monthly churn: **<7%**

## Unit economics to $10K MRR

### Pricing

- **Free:** 1 project/month, limited sources and generations
- **Solo:** $19/month — 10 projects, source uploads, grounded drafting, exports
- **Pro:** $49/month — 40 projects, voice profile, recurring templates, priority processing
- **Team:** $99/month — shared projects, comments, roles, and team templates

### Revenue mix at target

| Plan | Customers | MRR |
|---|---:|---:|
| Solo | 280 | $5,320 |
| Pro | 75 | $3,675 |
| Team | 10 | $990 |
| **Total** | **365** | **$9,985** |

Round the plan to **366 paying customers for approximately $10K MRR**.

### Cost assumptions

Typical Solo customer:

- 12 generations/month
- Average cost per long generation: $0.10–$0.25 depending on context length
- Model and extraction cost: approximately $1.80/month
- Storage, email, and processing: approximately $0.70/month
- Gross contribution: approximately $16.50

Illustrative blended variable cost: **$3.00/customer/month**.

### Gross margin and acquisition

- MRR: approximately $10,000
- Variable cost: approximately $1,098
- **Gross margin:** approximately 89%
- Three-month gross-margin CAC ceiling: approximately **$89**
- Target blended CAC: **≤$40**
- Required monthly paid acquisitions: approximately **50–70**

Do not rely on paid ads. Ministry communities and peer referrals are the intended low-cost channels. If community distribution cannot produce 20 qualified trials per week, reconsider the niche or identify a more specific ministry segment.

### Validation milestone

Reach **25 paid customers and $500 MRR**. Before scaling, confirm that at least 70% of drafts are edited rather than discarded and that grounding warnings are considered useful rather than noisy.

## Kill criteria

Kill or reposition the direction if:

1. Fewer than **5 paid or signed pilot commitments** from 30 qualified ministry interviews.
2. Fewer than **15%** of qualified visitors activate within 30 days.
3. Activated-to-paid conversion remains below **3%** after two onboarding iterations.
4. Fewer than **50%** of paid users export at least two projects in 30 days.
5. Monthly churn exceeds **10%** in the first 50-customer cohort.
6. Effective CAC exceeds **$90**.
7. Grounding tests show less than **90%** supported-claim accuracy, including Scripture references.
8. Users frequently request doctrinal guidance, pastoral counseling, or church administration that the product cannot safely support.
9. Model and processing costs exceed **15% of revenue**.
10. Denominational or theological objections cannot be resolved with a narrower ICP and clearer boundaries.
11. A direct competitor offers the same grounding, editing, and export workflow at lower prices with stronger ministry distribution.
12. The founder cannot recruit and review outputs with actual ministry professionals.
