---
layout: post
title: "CanvasNinja — Direction Package"
date: 2026-11-12T22:35:11+00:00
week: "2026-11-12_223511"
week_date: "2026-11-12T22:35:11+00:00"
slug: "canvasninjaapp"
permalink: /directions/canvasninjaapp.html
tags:
  - "AI"
  - "education"
  - "finance"
excerpt: "Turn lesson content into polished classroom worksheets and visual learning packs."
---

## Why this direction

### TrustMRR evidence

- CanvasNinja was classified `GO_CANDIDATE` with **$15.81 MRR**, **$21.42 in last-30-day revenue**, and **105 subscribers**.
- Its demand heuristic was **4**, while its competition heuristic was **2**.
- The strongest signal is revenue velocity: last-30-day revenue exceeded reported MRR, indicating recent subscriber growth rather than a static legacy base.
- The product opportunity is not “another AI course generator.” It is a narrow transformation job: turn source material into a visually coherent, classroom-ready worksheet or learning pack.

### X/web evidence

- Stage A did not provide a public X handle for CanvasNinja.
- The supplied TinyFish output contained CLI installation instructions rather than usable result excerpts, so no individual X post is claimed as verified.
- Recurrent public pain signals in educator and tutor communities include:
  1. time spent differentiating the same source material for different learners;
  2. low-quality PDFs that require hours of formatting;
  3. difficulty maintaining consistent answer keys and difficulty levels;
  4. a shortage of ready-to-print materials for tutors and micro-schools;
  5. privacy concerns when uploading student information to generic AI tools.
- Competitive interpretation: general lesson-plan generators, presentation builders, and AI PDF tools are broad substitutes. A defensible initial wedge is **source-to-differentiated worksheet packs for tutors and small learning centers**, with answer keys and export to printable PDF.
- **Final score: demand 4, competition 2 → GO.**

## Competitor table

> Pricing is directional and must be checked before launch.

| Level | Competitor | Pricing found or typical positioning | Strength | Opening for CanvasNinja |
|---|---|---:|---|---|
| L1 direct | Canva Education / Canva | Free tier; paid Canva Pro/Teams offers | Brand assets, templates, broad familiarity | Faster structured source-to-worksheet generation and automatic answer keys. |
| L1 direct | Education.com | Free/paid educational content | Large worksheet library and marketplace | Personalized materials from a teacher’s own source and differentiated student versions. |
| L1 direct | Twinkl | Subscription and per-resource licensing | Large teacher marketplace and polished resources | Rapid personalization without per-resource marketplace complexity. |
| L1 direct | Teacher Created Resources | Marketplace/free and paid resources | Deep teacher supply variety | Narrow source transformation workflow and tutor-ready bundles. |
| L2 | LessonPlans.ai | Freemium/paid AI lesson tools | AI-native educational generation | Focus on worksheets, answer keys, and print quality rather than broad lesson planning. |
| L2 | MagicSchool | Freemium/paid teacher AI suite | Popular teacher workflow and broad feature set | One focused transformation job with fewer steps and transparent pricing. |
| L2 | Diffit | Free/paid differentiated resources | Strong differentiation concept | Competitor validates demand; CanvasNinja must own tutors and printable packs. |
| L3 | Schoolhouse.net | Subscription | Marketplace for teachers | Efficient private personalization and export. |
| L3 | Microsoft/PDF/Word generators | Free or low-cost | Ubiquitous and flexible | Automatic structure, answer keys, and quality checks. |

### Competition score rationale

**2/5.** Direct horizontal substitutes are plentiful, but the end-to-end source-to-printable-differentiated-pack workflow is fragmented across content generators, generic AI tools, and manual formatting. The MVP should deliberately exclude a general-purpose lesson marketplace and broad teacher suite.

## PRD MVP

### Target customer

- Independent tutors serving primary, middle, or high-school students.
- Small learning centers with 2–20 instructors.
- Homeschool teachers and curriculum co-ops.
- Later expansion: exam-prep tutors and corporate trainers.

### Core job

> “Give me one source document and quickly produce a polished student worksheet set with different difficulty levels, an answer key, and a printable PDF.”

### P0 — required for launch

1. **Source ingestion**
   - PDF, DOCX, pasted text, and image upload.
   - Extract headings, paragraphs, and key concepts.
   - Clear error handling and source preview.
2. **Learning-objective extraction**
   - Generate a concise objective list from the source.
   - Allow the tutor to edit objectives.
3. **Worksheet generation**
   - Multiple-choice, short-answer, matching, ordering, and fill-in-the-blank item types.
   - Difficulty levels: support, core, stretch.
   - Math notation rendering and grammar-safe generation.
4. **Differentiation**
   - One source can produce a support, core, and extension version.
   - Tutor-controlled readability and prompt complexity.
5. **Answer key**
   - Separate instructor answer key.
   - Answers mapped to worksheet items.
   - Explanations optional for selected question types.
6. **Editing and layout**
   - Inline editing.
   - Page breaks, headers, school name, student fields, and answer-space control.
   - Print-safe typography.
7. **Export**
   - Printable PDF.
   - Editable DOCX where feasible.
   - Individual student files generated from a roster CSV.
8. **Account, billing, and privacy**
   - Workspace/project model.
   - Usage-based plan with monthly generation limits.
   - Explicit deletion of uploaded sources and generated student materials.
   - No student names required; optional first-name fields only.
   - Consent notice that the service is not a substitute for teacher review.

### P1 — after validation

- Question-type generator and difficulty editor.
- Standards or learning-objective tagging.
- Version history.
- Shared templates for a learning center.
- Rubric generator.
- Reusable question bank.
- Parent progress summary from teacher-approved results.
- Spanish and other heritage-language worksheet variants.
- Human educator review checklist.

### P2 — later

- Student login and adaptive practice.
- Marketplace of vetted worksheets.
- District administration.
- LMS integrations.
- Automatic curriculum ingestion.
- Multimedia worksheets.
- Full automated grading.
- Parent messaging and payments.

### Explicit non-goals for the first 14 days

- No student-facing adaptive-learning platform.
- No lesson-plan marketplace.
- No live tutoring marketplace.
- No school administration.
- No automated grading of free-form responses.
- No claims that generated content is pedagogically validated.
- No student uploads in the MVP.
- No broad document editor.
- No video generation.
- No full LMS, attendance, or payment features.

### Technical approach

- Frontend: Next.js/TypeScript with an editor-based workflow.
- Backend: serverless functions or a small Node/Python service.
- Database: PostgreSQL with encrypted source and project metadata.
- File storage: private object storage with signed URLs.
- Extraction: PDF/DOCX parser plus OCR fallback.
- Generation: structured JSON schema enforced by a validation library.
- Mathematics: KaTeX or MathJax-compatible rendering.
- PDF: server-side browser rendering with deterministic print CSS.
- Quality checks: answer-reference validation, item count, duplicate detection, source-coverage check, and answer-key consistency.

### Pricing hypothesis

- **Free:** 3 worksheet generations/month, one student version.
- **Tutor — $19/month:** 40 generations, three difficulty levels, answer keys, PDF/DOCX export.
- **Center — $49/month:** five instructors, 150 generations, reusable templates, branding.
- **Pro — $89/month:** 400 generations, individual student files, version history, priority processing.
- Overage priced per generation pack only after usage is understood.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|
| 1 | Scope lock and curriculum sample | Select one tutor segment, grade band, and 20 representative source documents. |
| 2 | Schema and data models | Source, objective, worksheet, item, answer, export, and usage schemas finalized. |
| 3 | Ingestion | PDF, DOCX, text, and image uploads parse; failures are visible and recoverable. |
| 4 | Objective generation | Structured objectives can be reviewed, edited, and accepted. |
| 5 | Question generation | All five MVP item types render with validated references and correct answers. |
| 6 | Differentiation | Support/core/stretch packs generated from the same source with distinct prompts. |
| 7 | Editor | Tutor can edit prompts, choices, ordering, and answer-space instructions. |
| 8 | Answer key | Instructor key maps exactly to items and can be regenerated after edits. |
| 9 | Print layout | Student and key PDFs render cleanly at A4 and US Letter with page-break checks. |
| 10 | Roster and exports | CSV roster creates labeled student files; PDF and DOCX exports work. |
| 11 | Accounts, billing, and limits | Checkout, quotas, cancellation, and generation history work; sources remain private. |
| 12 | Safety and quality checks | Duplicate detection, answer consistency, source coverage, upload limits, and deletion are tested. |
| 13 | Dogfooding | Five tutors generate, print, and use real packs; usability issues are prioritized. |
| 14 | Launch | Production deploy, onboarding, support flow, sample library, demo video, and launch posts. |

### Launch-readiness checklist

- A tutor can move from upload to corrected printable PDF in under 15 minutes.
- Every generated answer key matches its worksheet after manual edits.
- The system visibly warns when source coverage may be incomplete.
- Student files contain no unintended source data.
- Uploaded files and generated materials can be deleted.
- Five target tutors have printed or reviewed a real pack.

## 30-day marketing calendar

### Budget

| Channel | 30-day budget |
|---|---:|
| Educator creator collaborations and print samples | $100 |
| Selective paid tests for proven pages | $120 |
| Templates, file hosting, and production services | $80 |
| **Total** | **$300 maximum** |

### Weekly calendar

#### Days 1–7: establish the workflow

| Day | Action |
|---:|---|
| 1 | Publish a before/after PDF showing manual worksheet work versus the proposed workflow. |
| 2 | Recruit 10 tutors or learning-center owners for interviews and screen recordings. |
| 3 | Post a founder build diary and collect the five most common worksheet types. |
| 4 | Release a free sample pack generated from a public lesson source. |
| 5 | Answer tutor questions in relevant educator communities without posting generic links. |
| 6 | Run a small live “source to printable worksheet” session. |
| 7 | Launch the v1 landing page and founder-led announcement. |

#### Days 8–14: target one segment

| Day | Action |
|---:|---|
| 8 | Publish a tutor-specific landing page with the exact 15-minute workflow. |
| 9 | Offer 20 assisted pilot conversions for learning centers. |
| 10 | Share three student, parent, and instructor samples with review notes. |
| 11 | Publish a quality checklist for AI-generated worksheets. |
| 12 | Release a differentiation template for the selected grade band. |
| 13 | Post a short screen-recording of edits, answer keys, and PDF export. |
| 14 | Email all qualified leads with a personalized sample pack and onboarding slot. |

#### Days 15–21: prove outcomes

| Day | Action |
|---:|---|
| 15 | Publish a tutor case study including preparation-time comparison. |
| 16 | Reach out to 20 learning centers with a center-branded sample. |
| 17 | Add version history only if users request it; otherwise improve reliability. |
| 18 | Publish a rubric and answer-key checklist for teacher review. |
| 19 | Host a live Q&A about differentiation and classroom use. |
| 20 | Send a re-engagement email to users who generated but did not export. |
| 21 | Ask 20 active tutors to refer another tutor. |

#### Days 22–30: monetize and selectively scale

| Day | Action |
|---:|---|
| 22 | Release a $49 center-plan onboarding guide. |
| 23 | Interview paid, unpaid, and churned users. |
| 24 | Publish reliability and content-quality fixes. |
| 25 | Test a $50 paid landing-page campaign only against a page with organic signups. |
| 26 | Create a reusable center template and invite collaboration. |
| 27 | Publish an agency or tutoring-center case study. |
| 28 | Launch an annual Tutor plan only if monthly cancellation data is acceptable. |
| 29 | Remove friction from export and invite a referral after successful export. |
| 30 | Review activation, paid conversion, generation quality, support load, retention, and MRR. |

### KPIs

- Upload-to-export: target 25% within seven days.
- Median generation-to-export time: under 15 minutes.
- Paid conversion after three exports: target 12%.
- Paid retention after first billing month: target 90%.
- Support or correction requests per 100 packs: under 10.
- Paid CAC target: under $80.
- Day-30 MRR validation target: **$1,500–$3,000** from early paid accounts.

## Unit economics to $10K MRR

### Base case

Assume blended ARPU of **$42/month** and gross margin of **80%**.

- Customers required: `$10,000 / $42 ≈ 239`.
- Monthly gross profit: `$10,000 × 80% = $8,000`.
- Inference, OCR, document parsing, and file storage should remain under **$1,000 per month** at this scale, or be constrained through per-generation quotas.

### Customer mix

| Customers | Blended ARPU | MRR | Use |
|---:|---:|---:|---|
| 100 | $19 | $1,900 | Tutor |
| 105 | $49 | $5,145 | Center |
| 34 | $89 | $3,026 | Pro |
| **239** | **$41.84** | **$10,000** | Target threshold |

### CAC and LTV

- Target CAC ceiling: **$100**.
- Gross profit per customer per month at $42 ARPU and 80% margin: **$33.60**.
- Target gross-margin LTV/CAC: **3x**, requiring at least **$300 LTV**.
- At 12 months of revenue and an average retained life of approximately nine months, contribution LTV is about `$33.60 × 9 = $302`.
- This meets but barely clears the target. The business becomes attractive if average retained life exceeds 11 months, ARPU exceeds $50, or referral CAC falls below $60.
- Initial paid acquisition: 239 × $100 = **$23,900** over the scaling period, funded from revenue rather than the initial $300 validation budget.

### Cost controls

- Use OCR only when text extraction is weak.
- Cache source extraction and reuse it for multiple difficulty levels.
- Cap document size and generation count.
- Charge for generation packs, not individual renders.
- Use asynchronous processing and rate limits.
- Require teacher review; never let the product imply that automated output is fully reliable.

## Kill criteria

Kill or pause if any of the following occurs:

1. **Demand failure:** fewer than 10 of 15 interviewed tutors report repeatedly preparing differentiated worksheets from source material.
2. **Time-to-value failure:** fewer than 30% of activated users export a worksheet within seven days.
3. **Quality failure:** more than 20% of sampled packs require major factual, mathematical, or answer-key correction.
4. **Paid conversion failure:** fewer than 5 paid accounts from 50 activated users after two onboarding improvements.
5. **Retention failure:** more than 10% of paying accounts churn in their first billing month.
6. **Economics failure:** blended CAC exceeds $100 without referral traction, or gross margin remains below 75%.
7. **Safety failure:** private student/source data is exposed, or the workflow requires ingesting identifiable student records.
8. **Scope trap:** success depends on becoming a full LMS, lesson marketplace, or human tutoring service.
9. **Distribution failure:** after 30 days and 100 qualified outreach messages, fewer than 10 target tutors agree to a paid pilot.
10. **Liability trigger:** customers expect certified curricula, automatic grading, or guaranteed learning outcomes without teacher review.

Decision rule: if factual or answer-key errors remain above 10% after two focused quality iterations, constrain the MVP to one subject/grade band or kill it. Do not solve quality by hiding the review requirement.

## Research caveats

- No verified public X handle was supplied for CanvasNinja.
- The supplied TinyFish output did not include usable search result excerpts.
- Competitor pricing and product scope should be reconfirmed before launch.
- The GO applies to tutor/small-center worksheet packs, not broad AI lesson generation.
