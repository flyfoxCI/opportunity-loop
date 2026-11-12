# Amen Faith AI — Direction Package

## Why this direction

### TrustMRR evidence

- The prior validated direction pack identifies **Sermon Scribe** as a high-confidence niche with approximately **$14K MRR and 2,362 paying users**.
- The prior research found that sermon and ministry AI tooling had unusually low competition despite demonstrated willingness to pay.
- The opportunity is not a generic theology chatbot. It is a narrow workflow for ministers and small ministry teams: turn sermon ideas, scriptures, notes, and previous messages into organized drafts and derivative content while retaining human review.
- Revenue evidence in this niche is substantially stronger than in most Stage A candidates and provides a credible base for a $10K MRR plan.

### X/web evidence

- The prior pack did not provide a stable verified handle for the target customer, so no specific X account or post is presented as independently verified.
- Public ministry-community pain signals include:
  1. weekly sermon preparation consumes many hours;
  2. pastors need outlines, illustrations, discussion questions, and social derivatives from the same source;
  3. generic AI tools produce theologically shallow or culturally inappropriate material;
  4. churches need privacy and control over pastoral source material;
  5. volunteer teams need reusable templates and consistent voice.
- Competitive interpretation: generic ChatGPT, sermon-preparation apps, church-management suites, and design tools are broad substitutes. A narrow wedge is **source-grounded sermon preparation for independent pastors and small churches**, with reusable house style, citations, and human approval checkpoints.
- **Final score: demand 3, competition 2 → GO.**

## Competitor table

> Pricing is directional and must be verified before launch.

| Level | Competitor | Pricing found or typical positioning | Strength | Opening for Amen |
|---|---|---:|---|---|
| L1 direct | Sermon Scribe | Publicly validated at roughly $14K MRR in prior research | Direct sermon-drafting workflow and proven demand | Focus on one underserved ministry segment with house style, citations, and derivative assets. |
| L1 direct | Pulpit | Freemium/paid sermon tools | Sermon outline and preparation features | Faster source-grounded iteration and ministry-team templates. |
| L1 direct | Preaching | Subscription AI sermon tools | Focused sermon workflow | Transparent theological sources and reusable church voice. |
| L1 direct | Sermonary | Freemium/paid | Established sermon resources and community | End-to-end own-content workflow and structured exports. |
| L2 | ChatGPT / Claude / Gemini | $20–$100+/month | Flexible generation and strong reasoning | Domain controls, source citations, review workflow, and reusable ministry context. |
| L2 | Planning Center / Breeze | Free or paid church operations suites | Church relationships and workflow context | Preparation layer that integrates with existing ministry operations rather than replacing them. |
| L2 | Proclaim | Per-seat paid presentation/media | Excellent production output | Text-first preparation before slides and video. |
| L3 | Canva for churches / social tools | Free/paid | Design and distribution | Complete source-to-sermon-to-social workflow without requiring design skills. |

### Competition score rationale

**2/5.** A proven direct player exists, which confirms demand, but the broader niche remains fragmented and has historically had low competition. The new product must select a narrower segment—such as sermon-first workflows for small bilingual churches or sermon-to-community content for independent pastors—rather than market an undifferentiated theology chatbot.

### Initial wedge

The recommended first wedge is:

> **Sermon workspace for independent pastors: import a sermon idea, scripture notes, or prior message; produce a structured draft, discussion guide, and five channel-specific derivative posts; every theological claim links to user-selected sources and requires minister review.**

This avoids direct dependence on sermon-note style alone and allows a narrow segment without claiming a broad theology product.

## PRD MVP

### Target customer

- Independent pastors and bi-vocational ministers.
- Small churches without dedicated communications staff.
- Church planters and ministry leaders preparing weekly messages.
- Secondary segment: faith-based small-group or nonprofit leaders.

### Core job

> “Help me turn my sermon notes into a coherent, reusable weekly content package without losing my voice or inventing theology.”

### P0 — required for launch

1. **Ministry workspace**
   - Church or solo workspace, brand voice, audience, tone, and recurring series context.
   - Team seats may remain read-only in MVP.
2. **Source ingestion**
   - Paste notes, upload DOCX/PDF, enter scripture references.
   - User-selectable theological sources and preferred translations.
   - Source excerpts remain linked to generated claims.
4. **Sermon outline**
   - Theme, scripture, big idea, three-point outline, transitions, and supporting passages.
   - Claims tagged as user-provided, sourced, or assistant-generated.
5. **Draft generation**
   - Editable sermon draft with explicit review checklist.
   - User’s house style and doctrinal guardrails.
   - No impersonation of a named pastor or denomination without an explicit opt-in.
6. **Derivative content**
   - Discussion questions.
   - Prayer prompts.
   - Five social posts and a newsletter outline.
   - Content can be edited and exported.
7. **Human approval**
   - Every draft is marked “needs minister review.”
   - Citations can be checked against imported source material.
   - Publication requires user confirmation.
8. **Account, billing, and privacy**
   - Email authentication.
   - Monthly generation quotas.
   - Workspace data isolation, export, and deletion.
   - Retention controls for pastoral and confidential notes.

### P1 — after launch

- Series calendar.
- Scripture and commentary library integrations.
- Bilingual generation.
- Clip and reel script variants.
- Reusable sermon templates.
- Small-group discussion generator.
- Prayer-request workflow.
- Custom theological-source packs.
- Team comments and approvals.

### P2 — later

- Church management integrations.
- Automatic presentation and video generation.
- Membership, giving, or donor management.
- Community app.
- Audio transcription of sermons.
- Many-denomination curriculum marketplace.
- Pastor coaching marketplace.

### Explicit non-goals for the first 14 days

- No counseling, pastoral care, crisis intervention, or mental-health advice.
- No automated church publishing.
- No doctrinal authority claim.
- No impersonation of a real pastor or denomination.
- No scraping copyrighted sermons, commentaries, or translation texts.
- No full church-management system.
- No social-media autoposting in MVP.
- No prayer claims about divine outcomes or healing.
- No gambling, casino, or prosperity-product functionality.
- No demographic profiling of congregants.

### Technical approach

- Frontend: Next.js/TypeScript.
- Backend: serverless functions or a small Node/Python service.
- Database: PostgreSQL with tenant isolation.
- Storage: private object storage with signed URLs.
- Generation: structured model output with schema validation.
- Retrieval: user-provided and licensed source excerpts only.
- Citation display: source title, reference, and excerpt linked to the relevant passage.
- Review workflow: draft states `draft → needs_review → approved`.
- Safety: domain-specific escalation for counseling or medical/legal claims; explicit refusal and resource language.
- Billing: Stripe-like recurring subscription with generation quotas.

### Pricing hypothesis

- **Free:** two sermon workspaces or packages/month.
- **Pastor — $19/month:** 20 packages, source citations, exports, house style.
- **Ministry — $39/month:** 60 packages, series calendar, bilingual drafts, team review.
- **Church — $79/month:** five seats, 200 packages, shared sources, priority support.
- No usage metering based on spiritual content; quota limits protect cost only.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|---|
| 1 | Scope lock and ministry research | One initial segment, theology boundaries, source policy, and supported languages defined. |
| 2 | Data model and auth | Workspace, member, source, sermon, derivative, approval, and quota models work. |
| 3 | Source ingestion | Text, DOCX/PDF, and scripture references import with excerpt traceability. |
| 4 | Outline generation | Structured outline includes big idea, points, passages, and source tags. |
| 5 | Draft generation | Editable, house-style-aware draft generated from user sources with review marker. |
| 6 | Citation and claim review | Unsupported claims are flagged; links lead to imported source excerpts. |
| 7 | Derivatives | Discussion guide, prayer prompts, newsletter outline, and five social variants work. |
| 8 | Editor and export | User edits regenerate dependent assets and export without losing approvals. |
| 9 | Billing and quotas | Subscription state, limits, upgrade, cancellation, and free tier work. |
| 10 | Privacy and safety | Confessional-content controls, crisis-topic refusals, and deletion flows are tested. |
| 11 | UX and mobile | Source-to-draft workflow is understandable to five test ministers. |
| 12 | Quality fixtures | Twenty theology and language test cases produce acceptable outputs or safe failures. |
| 13 | Dogfooding | Five ministers prepare and review a full weekly package with facilitator notes. |
| 14 | Launch | Production deploy, sample package, support process, privacy policy, demo video, and launch posts. |

### Launch-readiness checklist

- A minister can create a reviewable sermon package in under 20 minutes.
- Every source-dependent claim links to an imported source or is clearly marked unverified.
- The product never presents an unreviewed draft as approved theology.
- Private ministry notes can be exported and deleted.
- Crisis and counseling topics produce a safe response rather than spiritual advice.
- Five ministers complete a real weekly package with the tool.

## 30-day marketing calendar

### Budget

| Channel | 30-day budget |
|---|---:|
| Ministry creator partnerships and printed sample packs | $100 |
| Selective paid tests for proven pastoral-workflow pages | $120 |
| Production, privacy review, and operational tools | $80 |
| **Total** | **$300 maximum** |

### Weekly calendar

#### Days 1–7: learn the ministry workflow

| Day | Action |
|---:|---|
| 1 | Publish a transparent “what AI should not do in ministry” position. |
| 2 | Interview 10 pastors or church planters about weekly preparation bottlenecks. |
| 3 | Publish a before/after preparation workflow with a full source-to-package example. |
| 4 | Share a sample discussion guide and show every citation. |
| 5 | Post a founder diary about grounding claims in user-selected sources. |
| 6 | Offer 20 assisted pilots to independent pastors. |
| 7 | Launch the landing page and founder-led announcement. |

#### Days 8–14: sharpen the segment

| Day | Action |
|---:|---|
| 8 | Publish a landing page for bi-vocational pastors with a shorter weekly workflow. |
| 9 | Run a live sermon-package demonstration. |
| 10 | Publish a house-style and theological-guardrail guide. |
| 11 | Add a bilingual sample after confirming demand with target users. |
| 12 | Release a ministry review checklist as a lead magnet. |
| 13 | Request a testimonial and short workflow video from two pilot users. |
| 14 | Email qualified users with a personalized sample package. |

#### Days 15–21: prove repeat usage

| Day | Action |
|---:|---|
| 15 | Publish a case study showing preparation time and review workflow. |
| 16 | Reach out to 20 ministry leaders or communication volunteers. |
| 17 | Fix the most common editorial and citation issues. |
| 18 | Publish a transparency page describing source limits and human review. |
| 19 | Add a reusable sermon-series template if requested by five users. |
| 20 | Re-engage users who generated a draft but did not export it. |
| 21 | Ask users to invite a second pastor or volunteer. |

#### Days 22–30: retention and selective scale

| Day | Action |
|---:|---|
| 22 | Add team review if five target workspaces request it. |
| 23 | Interview retained and churned users. |
| 24 | Publish a quality and safety update. |
| 25 | Test a $50 paid landing-page campaign only against a page with organic signups. |
| 26 | Add bilingual controls and source-language labeling if validated. |
| 27 | Publish an anonymized ministry-team case study. |
| 28 | Test annual pricing only if monthly churn remains below 10%. |
| 29 | Trigger a referral prompt after a minister exports a complete package. |
| 30 | Review MRR, weekly activation, retention, content corrections, safety escalations, and CAC. |

### KPIs

- Signup-to-first-package: target 50% within seven days.
- Package export rate: target 60% among package starters.
- Paid conversion after three packages: target 8%.
- Month-one paid retention: target 92%.
- Material factual correction rate: below 5%.
- Safety incidents involving pastoral advice: zero.
- Paid CAC target: under $80.
- Day-30 MRR validation target: **$2,000–$4,000**.

## Unit economics to $10K MRR

### Base case

Assume blended ARPU of **$32/month** and gross margin of **82%**.

- Customers required: `$10,000 / $32 ≈ 313`.
- Monthly gross profit: `$10,000 × 82% = $8,200`.
- Inference, storage, email, and payment costs should remain below **$1,800/month** at this scale.

### Customer mix

| Customers | Blended ARPU | MRR | Use |
|---:|---:|---:|---|
| 190 | $19 | $3,610 | Pastor |
| 95 | $39 | $3,705 | Ministry |
| 28 | $79 | $2,212 | Church |
| **313** | **$30.42** | **$9,521** | Near threshold; add 16 Pastor seats to exceed $10K |

### CAC and LTV

- Target CAC ceiling: **$90**.
- Gross profit per customer per month at $32 ARPU and 82% margin: **$26.24**.
- Target gross-margin LTV/CAC: **3x**, requiring **$270 LTV**.
- At a 12-month horizon and average retained life of about 11 months, contribution LTV is approximately **$289**.
- This clears the target modestly. Organic referral distribution and annual prepayment can improve cash efficiency, but annual discounts should not undermine gross margin.
- Initial scaling acquisition: 313 × $90 = **$28,170** over the growth period, funded from operating revenue.

### Cost controls

- Use structured generation and smaller models for derivative assets.
- Generate one canonical sermon package and reuse approved content for derivatives.
- Cache repeated source extraction.
- Set package-level quotas.
- Store source excerpts privately and delete them on request.
- Avoid costly real-time voice/video features in the MVP.
- Do not use per-token pricing as the primary customer-facing metric.

## Kill criteria

Kill or pause if any of the following occurs:

1. **Niche failure:** fewer than 10 of 15 interviewed ministers report regular weekly sermon-preparation pain.
2. **Activation failure:** fewer than 40% of signups create a first package within seven days.
3. **Export failure:** fewer than 50% of package creators export or reuse a complete weekly package.
4. **Quality failure:** more than 10% of reviewed packages contain a material unsupported theological or scriptural claim.
5. **Paid conversion failure:** fewer than 5 paid accounts from 50 activated workspaces after two iterations.
6. **Retention failure:** paid churn exceeds 8% in the first billing month.
7. **Safety failure:** the product repeatedly gives counseling, medical, legal, or deterministic spiritual outcomes without escalation.
8. **Trust failure:** users will not provide notes or scriptures because privacy or source handling is unacceptable.
9. **Economics failure:** CAC exceeds $90 without referral traction, or gross margin falls below 75%.
10. **Scope trap:** success requires becoming a church-management, social-management, counseling, or fundraising platform.

Decision rule: if material scriptural or theological errors remain above 5% after two quality iterations, narrow the supported use case further or kill it. Do not conceal errors behind vague disclaimers.

## Research caveats

- The strongest evidence is the prior validated pack and TrustMRR validation of the niche, not a current verified X thread.
- The supplied TinyFish output did not expose usable result excerpts.
- Competitor pricing and features must be checked before launch.
- The direction’s strongest defensibility comes from the chosen sub-niche, workflow depth, source grounding, and trust—not from the existence of AI alone.
