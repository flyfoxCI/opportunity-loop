---
layout: post
title: "Faith Sermon Workbench"
date: 2026-11-17T00:39:25+00:00
week: "2026-11-17_003925"
week_date: "2026-11-17T00:39:25+00:00"
slug: "faith-sermon-workbench"
permalink: /directions/faith-sermon-workbench.html
tags:
  - "AI"
  - "B2B"
  - "religion"
  - "mobile"
excerpt: "Turn a church’s sermon archive, service notes, and recurring themes into searchable sermon research and first drafts."
---

**Tier:** GO  
**Demand:** 4/5  
**Competition:** 3/5  
**Target:** $10,000 MRR  
**MVP window:** 14 days, solo  
**30-day marketing budget:** ≤ $250

## Why this direction

### TrustMRR evidence

Prior research documents Sermon Scribe at approximately $14,000 MRR with more than 2,000 paying customers. That is unusually strong evidence that churches and ministry workers will pay for AI-assisted sermon preparation. It also reveals a crowded category risk: the broad “AI sermon generator” proposition is not defensible.

The opportunity is therefore not to launch another generic text generator. It is to provide a focused workbench for one recurring church workflow:

> Move from a church’s own archive and service context to a structured, reusable sermon research draft.

The product should help ministers and ministry teams organize source material, find recurring themes, build sermon series, and preserve a record of what was preached.

### X/web evidence

Church-technology and pastor communities repeatedly discuss the friction of fragmented sermon tools: notes live in documents, old sermons are difficult to retrieve, series planning begins from a blank page, and generic AI outputs feel disconnected from the congregation’s history. The demand pattern is supported by the large TrustMRR revenue signal, while complaints about generic outputs indicate a path to differentiation through source-grounded workflows.

Validate the following before coding:

1. Ten interviews with ministers, associate pastors, or church administrators.
2. At least five use a repeatable weekly sermon-preparation process.
3. Three agree to share a redacted sermon archive or sample notes.
4. Most already use generic AI but cannot consistently incorporate prior sermons.
5. The buyer can be a minister, ministry director, or church administrator, with the pastor as user.

### Product thesis

Faith Sermon Workbench is a private, source-grounded workspace for one church:

- import approved sermon notes, transcripts, documents, and service themes;
- organize them by series, scripture, topic, and date;
- generate briefs and first drafts that cite the church’s internal source material;
- maintain a “preached” archive to avoid repetition;
- export clean outlines and drafts to the formats ministers already use.

It is an assistant for sermon research and organization, not an autonomous theologian, denominational authority, or substitute for pastoral judgment.

## Competitor table

| Level | Competitor | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Pulpit AI | Sermon preparation and biblical research assistant | Subscription, often freemium and tiered | Direct competitor. Differentiation must come from church-owned archives, structured series planning, and workflow fit. |
| L1 | Sermonary | AI-assisted sermon preparation and research | Freemium/subscription | Strong direct competitor; a generic “generate a sermon” feature is insufficient. |
| L1 | Kelsen AI | Sermon and Bible-study preparation | Subscription | Another direct AI sermon incumbent with a broad theological-research proposition. |
| L1 | Bible Chat / Chat GPT plus prompting | General-purpose AI for sermon drafting | Free to low-cost general subscriptions | Powerful substitute. The product must beat it through memory, retrieval, structure, and repeatability. |
| L1 | Ekklesia / Proclaim / Faithlife | Church presentation, media, and administration platforms | Typically $30–$150+ per month or church-based tiers | Not direct sermon-AI competitors, but they own workflows and may add AI features. |
| L2 | YouVersion | Scripture reading, notes, and sharing | Free/freemium plus institutional products | Source and habit incumbent; no complete sermon-workflow substitute. |
| L2 | Sermon notes and church-management tools | Notes, planning, and church records | $0–$100 per month | Manual substitute. Must prove measurable time savings and better recall. |
| L3 | Google Drive, Notion, and Obsidian templates | Searchable personal archives and sermon notes | $0–$20 per month | Strong low-cost alternative. Import quality and structure are the wedge. |

### Pricing hypothesis

- **Solo minister:** $29/month.
- **Pro workspace:** $79/month with archive import, series planning, citations, and export.
- **Church team:** $149/month for up to five contributors and shared history.
- **Pilot:** 30 days free for 10 qualified churches.

At an $79 blended average, approximately 127 paying accounts are needed for $10K MRR. At $149 for church teams, 68 accounts are needed.

## PRD MVP

### Target user

A practicing minister, associate pastor, or ministry director who:

- prepares sermons weekly;
- maintains prior notes or transcripts;
- wants continuity with prior messages and the church’s current series;
- reviews and edits all generated material;
- prefers a simple browser workspace and standard document exports.

### P0 — required for launch

1. **Secure workspace**
   - One church, role-based access, passwordless email login, encrypted storage, and workspace deletion.
2. **Approved source import**
   - Upload PDF, DOCX, TXT, Markdown, and plain-text transcripts.
   - Store source title, date, Scripture references, topic, and optional series.
3. **Transcript cleanup**
   - Remove filler and repeated lines while preserving speaker meaning.
   - Always preserve the original alongside the cleaned version.
4. **Search and retrieval**
   - Keyword and semantic search across imported material.
   - Return source excerpts and links for verification.
5. **Sermon research brief**
   - Select a topic, audience, Scripture text, and desired shape.
   - Generate a sourced outline containing relevant archive excerpts, themes, questions, and references.
6. **Series workspace**
   - Build a sequence of sermon briefs with shared goals and distinct themes.
7. **Draft generation**
   - Produce an editable outline or manuscript draft from the approved brief.
8. **Citation and provenance**
   - Every archive-derived claim links back to its source.
9. **Duplicate/repetition warning**
   - Compare a proposed theme with previously preached topics and flag likely overlap.
10. **Export**
    - Markdown, plain text, and print-friendly PDF.
11. **Privacy controls**
    - No training on customer data, default private workspaces, configurable retention, and deletion controls.
12. **Safety boundary**
    - No claim of divine authority, no automated final approval, and no fabricated quotations or references.

### P1 — after activation

- Bible-version import and verse verification.
- Doctrinal or style guide supplied by the church.
- Transcript provider integration where permission allows.
- Calendar and sermon-series pipeline.
- Collaborative comments.
- Shared prayer and discussion prompts.
- Usage and editorial analytics.

### P2 — later

- Multi-week series generation.
- Integrated presentation slides.
- Volunteer/student training materials.
- Audio/video sermon indexing.
- Denomination-specific templates.
- Team approval workflows.

### Non-goals

- No public “AI preacher” persona.
- No automated publication or delivery.
- No denominational judgment.
- No mental-health or crisis counseling.
- No copyright-infringing sermon ingestion.
- No training a foundation model on customer archives.
- No full church-management-system replacement.
- No promise that generated theology is pastor-approved.
- No broad multiservice marketplace during the MVP.

### Core user story

> As a minister, I want to search our church’s previous sermons and shape a new research brief around them so that preparation starts from continuity rather than a blank page.

### Technical approach

- Next.js or a comparable web application.
- Postgres plus encrypted object storage.
- Background document parsing and transcription cleanup.
- Hybrid retrieval: database full-text search plus embeddings.
- LLM calls constrained to retrieved context and structured JSON output.
- Source citation IDs carried through every generation stage.
- Model-provider abstraction so parsing, generation, and moderation can be tested independently.
- Usage metering by workspace and month.

## 14-day day-by-day build plan

| Day | Deliverable | Exit criterion |
|---:|---|---|
| 1 | Interview three ministry professionals; map preparation and retrieval workflow | Documented ICP, recurring pain, and current tool stack |
| 2 | Interview seven more; select one initial buyer segment and content format | Ten interviews complete; three pilot commitments |
| 3 | Decide archive-first wedge; create wireframes, schema, privacy model, and safety policy | User can see a clear path from source upload to sourced brief |
| 4 | Build authentication, workspace creation, roles, and encrypted file storage | A user can create a private workspace and invite one teammate |
| 5 | Build TXT/Markdown/PDF import, parsing, progress, and error handling | Five documents import correctly with titles, dates, and metadata |
| 6 | Build DOCX support, transcript cleanup, original/clean diff, and source indexing | A sample transcript can be cleaned and reopened reliably |
| 7 | Build keyword plus semantic search with excerpts and source links | Search returns at least ten useful archive matches in pilot testing |
| 8 | Build sermon research brief generation with structured citations | Every archive-derived statement can be traced to a source |
| 9 | Build series workspace, draft editor, and Markdown/PDF export | One complete series brief can be created and exported |
| 10 | Add repetition warnings, workspace settings, and data export/delete | Privacy and deletion controls work end to end |
| 11 | Conduct five usability sessions with real ministry workflows | At least four users complete a brief without facilitator intervention |
| 12 | Add billing, trial, plan limits, usage caps, and provider failure handling | Test checkout, cancellation, and rate-limit behavior work |
| 13 | Onboard three churches; manually support their first briefs | Three pilot workspaces contain real sources and receive feedback |
| 14 | Fix critical issues, publish landing page, and invite the first 20 pilot churches | End-to-end workflow is usable and 10 pilot signups are live |

### Build discipline

- Focus on retrieval, source citation, and organization.
- Do not build a full presentation editor.
- Use only a small number of document formats.
- Do not support proprietary media without a lawful path.
- Keep editing and export simple; the product is not a publishing suite.

## 30-day marketing calendar

**Budget:** $250 maximum  
**Allocation:** $100 community partnerships and sponsorships, $100 content production, $50 pilot incentives and micro-outreach.

| Day | Activity | CTA and KPI |
|---:|---|---|
| 1 | Publish an archive-first landing page | CTA: Try your first archive brief; KPI: 15 qualified visits |
| 2 | Publish “Why generic AI forgets your church’s history” | KPI: 8 shares or replies |
| 3 | Interview five pastors using a structured form | KPI: 5 interviews and 2 pilot commitments |
| 4 | Post a sample source-grounded sermon brief in a minister community | KPI: 10 meaningful replies |
| 5 | Email 15 ministry leaders with a relevant archive pain hypothesis | KPI: 5 replies, 2 calls |
| 6 | Run a live archive-import and brief-generation demo | KPI: 10 attendees, 3 signups |
| 7 | Add the strongest onboarding question from interviews | KPI: activation above 50% |
| 8 | Publish a practical guide: “Build a searchable sermon archive” | KPI: 20 downloads, 3 signups |
| 9 | Ask pilots to review citation accuracy and time saved | KPI: 4 structured reviews |
| 10 | Record a two-minute screen demonstration | KPI: 100 views, 4 signups |
| 11 | Send a follow-up to trial workspaces with no uploaded source | KPI: reactivation above 40% |
| 12 | Publish a privacy explainer for confidential ministry notes | KPI: 8 signups |
| 13 | Reach five church-technology newsletters or communities | KPI: 2 placements |
| 14 | Host a ministry workflow roundtable | KPI: 6 attendees, 2 trials |
| 15 | Add requested export formats or series fields | KPI: four of five pilots confirm improvement |
| 16 | Publish a before/after archive-search example | KPI: 5 signups |
| 17 | Send a segmented email to ministry administrators | KPI: 3 team-plan leads |
| 18 | Run a 30-minute onboarding clinic | KPI: 8 attendees, 3 activated trials |
| 19 | Publish one congregation-specific use case | KPI: 6 signups |
| 20 | Ask satisfied pilots for permissioned testimonials | KPI: 2 testimonials |
| 21 | Review model/API cost by workspace and optimize large contexts | KPI: gross margin above 80% |
| 22 | Test $29 solo versus $79 pro packaging with a live announcement | KPI: 5 paid conversions |
| 23 | Publish a source-citation accuracy checklist | KPI: 5 signups |
| 24 | Offer a 14-day team workspace to 20 warm pilot users | KPI: 4 paid conversions |
| 25 | Conduct churn interviews with non-converting trials | KPI: top three objections identified |
| 26 | Publish an FAQ and revise landing-page copy | KPI: landing-to-trial above 10% |
| 27 | Contact five ministry consultants or denominational media groups | KPI: 2 referral partners |
| 28 | Add the most requested non-core integration, if lightweight | KPI: 3 trial activations |
| 29 | Offer annual billing only to pilots with repeated usage | KPI: 1 annual conversion |
| 30 | Review weekly briefs generated, paid conversion, retention, and support time | KPI: decide scale, narrow, or stop |

### Organic-first rules

- Build relationships with ministry communities rather than purchase broad email lists.
- Never present generated theology as authoritative.
- Do not quote customer sermons publicly without explicit permission.
- Use anonymized examples unless the church approves attribution.

## Unit economics to $10K MRR

### Revenue scenarios

| Plan | Price | Customers | MRR |
|---|---:|---:|---:|
| Solo | $29 | 345 | $10,005 |
| Pro | $79 | 127 | $10,033 |
| Church team | $149 | 68 | $10,132 |
| Blended | $89 | 113 | $10,057 |

### Cost assumptions

| Cost item | Per active account/month |
|---|---:|
| Hosting, database, object storage, email | $4–$7 |
| Parsing, embeddings, retrieval, LLM calls | $8–$20 |
| Moderation and source verification | $1–$3 |
| Support and document cleanup | $3–$6 |
| **Total variable cost** | **$16–$36** |

At an $89 blended price and $25 variable cost:

- Contribution: $64.
- Gross margin: about 72%.
- $10K MRR requires approximately 113 active accounts.

At a $149 team plan and $25 variable cost:

- Contribution: $124.
- Gross margin: about 83%.
- $10K MRR requires approximately 68 active teams.

### Acquisition assumptions

If paid conversion from qualified trials is 12%:

- 113 customers require roughly 942 qualified trial starts.
- The strategy should target 20–30 weekly qualified signups and improve activation before scaling.

If churn is 8% monthly:

- Approximately nine new accounts per month are needed to maintain 113 active accounts.
- If churn exceeds 15%, tighten the audience, improve archive value, or stop.

### Break-even

At $89 ARPA and $25 variable cost:

- $300 marketing is recovered after approximately five acquired customers.
- At 113 customers, estimated gross profit is about $7,232 before founder labor, taxes, and overhead.

## Kill criteria

Stop or materially narrow the product if any occur by day 30:

1. Fewer than 5 of 10 interviewees report recurring difficulty finding or reusing prior sermon material.
2. Fewer than 3 agree to provide a real archive or pilot the workflow.
3. Fewer than 2 of 5 activated pilots generate a brief weekly.
4. Fewer than 30% of users rate cited output as useful without substantial rewrite.
5. Zero paid conversions after 30 qualified workspaces receive an offer.
6. Paid conversion remains below 8% after two focused landing-page iterations.
7. Week-4 weekly active retention is below 40%.
8. More than 30% of outputs contain a material citation or quotation accuracy issue.
9. Median support exceeds 30 minutes per workspace per week.
10. Gross margin falls below 65% without a clear price or scope correction.
11. Users mainly request denominational compliance, presentation generation, or pastoral counseling—not archive-grounded preparation.
12. Privacy, copyright, or theological-safety review reveals an unmanageable blocker.
