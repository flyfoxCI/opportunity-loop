---
layout: post
title: "Vertical Certification Coach — Product Direction"
date: 2026-11-05T22:33:25+00:00
week: "2026-11-05_223325"
week_date: "2026-11-05T22:33:25+00:00"
slug: "vertical-cert-coach"
permalink: /directions/vertical-cert-coach.html
tags:
  - "AI"
  - "education"
  - "mobile"
  - "vertical"
excerpt: "An AI study coach for one regulated certification, initially compounding-advisor exams"
---

## Direction summary

Build an AI study coach for **one certification with high-stakes recurring exams and a concentrated professional audience**. The initial candidate is the U.S. **Certified Public Accountant (CPA)** exam, but the package is valid only if one specific exam segment is selected during validation.

The product provides a diagnostic, daily study plan, practice-question feedback, error review, and spaced review. It does not answer exam questions live, promise passing, or attempt to reproduce copyrighted exam content.

- **Tier:** GO_NARROW
- **Demand:** 3/5
- **Competition:** 4/5
- **MVP horizon:** 14 days, solo
- **30-day marketing budget:** $0–$200
- **Target:** $10,000 MRR

## Why this direction

### TrustMRR evidence

The prior validated direction index reports a strong demand anchor for professional certification and coaching:

- **Sherpa:** approximately **$26K MRR**
- The prior research described a meaningful opportunity in vertical professional coaching and mentor products
- It also identified **Pocket Prep** and **Limmer Education** as relevant competitors

The opportunity is not a generic “AI tutor.” The defensible product is a narrow study system for one exam, one candidate segment, and one failing skill. The CPA example has a recurring professional audience, expensive preparation products, and a clear need for adaptive practice.

The Stage A candidates do not directly prove this market, so the package relies on prior validated-niche evidence and requires stronger pre-build validation than the GO products.

### X/web evidence and validation status

The supplied TinyFish output is unusable for social verification. Use:

- X searches for `CPA exam study plan`, `CPA exam app`, `CPA study help`, `accounting certification AI`, `exam practice alternative`, and `hate Pocket Prep`
- Reddit communities for accounting students and candidates
- Becker, UWorld, Roger CPA, Surgent, AICPA, and university-accounting communities
- Candidate interviews about current study stack, monthly spend, exam date, and failure reasons

Validation requirements:

1. Twenty interviews with candidates for the selected segment
2. At least ten who use a paid prep product today
3. A one-week prototype with five candidates
4. Three paid preorders at the proposed price
5. Evidence that the selected segment has repeated, concentrated search or social demand

### Why this wedge is attractive

- Study is a high-intent, deadline-driven use case.
- A focused diagnostic and review system can outperform generic chat for daily retention.
- Students already buy exam-preparation products.
- Affiliate, student-group, professor, and tutor channels can distribute the product without large ad spend.
- A narrow segment can be supported with curated question metadata and a small content library.

## Wedge (required for GO_NARROW)

### The only market served in the MVP

**U.S. CPA exam candidates in one explicitly selected segment**, for example:

- First-time candidates taking the FAR section within 90 days, or
- International candidates who have passed FAR and need targeted AUD practice

Only one segment may be selected before implementation. The founder must document it as:

> “For [specific segment], preparing for [specific exam section] within [time window], we provide [specific diagnostic/review outcome]. We do not serve candidates across multiple sections, jurisdictions, certifications, or general accounting study.”

### What this direction refuses to build

- No support for every CPA section in the MVP
- No support for other certifications, including CMA, CIA, CFP, CMA or ACCA
- No generic tutoring across careers or school subjects
- No live exam proctoring
- No guarantee of passing
- No upload or reproduction of copyrighted exam banks
- No academic-integrity features intended to help cheat during a proctored exam
- No broad course, LMS, scheduling, or community platform
- No marketplace of tutors until product–market fit is established

### Why the narrow wedge is mandatory

Competition is scored 4 because established exam-prep products, tutoring marketplaces, flashcard apps, and general AI tutors already serve the broad market. A broad “certification coach” launch would therefore fail the competition gate. The MVP is permitted only if its segmentation is concrete enough to create a distinct acquisition message, diagnostic, content set, and retention loop.

## Competitor table

### L1 — direct competitors

| Competitor | Positioning | Typical pricing | Strength | Gap to exploit |
|---|---|---:|---|---|
| Pocket Prep | Certification exam practice and learning | Entry/low-cost through premium plans | Purpose-built content, mobile habit, large question bank | Generic across many certifications; less adaptive error diagnosis |
| Limmer Education | Free exam-preparation content | Free with paid course/products | Strong free content and SEO | Less personalized than an AI coach |
| UWorld | Question bank and explanations | Premium subscription | Deep question bank and explanations | Expensive; broad interface; weak adaptive coaching layer |
| Roger CPA | CPA course and question bank | Premium | Trusted education brand and comprehensive curriculum | Expensive and not narrowly optimized for one weak section |
| Becker | CPA course and study tools | Premium | Established brand and content | High price and broad course structure |
| Surgent | CPA course | Premium | Course-focused exam prep | Large commitment and less flexible low-cost wedge |
| StudyFetch / Quizlet / Anki | AI or flashcard study tools | Freemium/subscription | Flexible, familiar study behavior | Not exam-specific in feedback and progression |
| ChatGPT/Claude | Generic tutoring | $20+ or API cost | Flexible explanation and role-play | No structured diagnostic, error taxonomy, or exam tracking |

**Pricing caveat:** verify all current prices during the competitor pass. The table describes market patterns, not guaranteed 2026 quotes.

### L2 — indirect competitors

| Competitor | Pricing pattern | Why users may choose it |
|---|---:|---|
| Professor-led tutoring | $30–$100+/hour | Human reassurance and accountability |
| Student study groups | Free | Peer support and shared materials |
| AICPA/community resources | Free to low-cost | Credible official guidance |
| Course forums and YouTube | Free | Low price and abundant explanations |

### L3 — substitutes

| Substitute | Limitation |
|---|---|
| Reading notes repeatedly | Weak feedback loop and weak error identification |
| Random question banks | Users do not know what they have not mastered |
| Generic flashcards | High cognitive load and weak concept remediation |

## PRD MVP

### Target customer

One selected CPA candidate segment with an exam date within 90 days, a current baseline score, and a recurring weekly study plan. The persona must state target score, section, exam date, current materials, weekly study hours, and primary failure category.

### User promise

“Find the exact topics costing you points, turn them into a daily review plan, and make every study session target the next highest-value fix.”

### P0 — required for launch

1. **Onboarding diagnostic**
   - Segment and exam-section selection
   - Exam date and target score
   - 25–40 original or properly licensed diagnostic questions
   - Skill-tagged results

2. **Question engine**
   - Original practice questions only
   - Multiple-choice and short-response items where appropriate
   - Four skill categories per selected section
   - Step-by-step reasoning and source references to public accounting standards

3. **Feedback**
   - Correctness
   - Concept-level explanation
   - Misconception classification
   - Worked solution
   - Related weak-topic links

4. **Adaptive daily plan**
   - 20–40 minute plan
   - Prioritizes weak skills and recent mistakes
   - User can adjust daily time
   - Plan regenerates after completed sessions

5. **Error notebook**
   - Automatic capture of mistakes
   - Tags for concept and misconception
   - Spaced review schedule
   - User notes

6. **Progress dashboard**
   - Skill mastery
   - Predicted readiness band, explicitly non-guaranteed
   - Questions completed
   - Accuracy trend
   - Days to exam

7. **Account and billing**
   - Stripe subscription
   - 7-day trial
   - Subscription usage terms
   - Cancellation and deletion

8. **Academic integrity**
   - No live-answer or exam-cheating features
   - Original questions and licensed content only
   - Clear study-use terms
   - No collection of exam content that users upload unlawfully

### P1 — first 30-day improvements

- Written-response grading with transparent rubric
- Weak-topic flashcards
- Performance graph by question type
- Custom study calendar
- Spaced-repetition algorithm improvements
- PDF study-plan export
- Integrations with calendar and note tools

### P2 — later

- Second segment only after product-market fit
- Mock exam engine
- Live tutor matching
- Peer discussion groups
- Instructor dashboard
- Institution licensing
- Additional certifications only after the vertical playbook is proven

### Non-goals

- No broad multi-certification catalog
- No complete CPA curriculum in the MVP
- No copyrighted UWorld/Becker/Surgent material
- No guarantee of exam passage
- No generic schoolwork assistant
- No live exam-answer assistance
- No large social community
- No full LMS
- No AI-generated explanations without citation/verification

### Core data model

- **Learner:** id, segment, section, exam_date, target_score, study_minutes
- **Question:** id, skill, difficulty, prompt, choices, explanation, source_reference, status
- **Attempt:** id, learner_id, question_id, answer, correct, duration, created_at
- **SkillMastery:** id, learner_id, skill, score, confidence, updated_at
- **Misconception:** id, learner_id, skill, label, evidence, resolved
- **StudyPlan:** id, learner_id, date, blocks, status
- **ReviewItem:** id, learner_id, question_id, due_at, interval
- **Subscription:** id, learner_id, stripe_subscription_id, status

### MVP architecture

- Next.js + TypeScript
- PostgreSQL
- Question and skill-tag authoring pipeline
- LLM only for explanations, candidate rephrasing, and tutoring—not for unreviewed scoring
- Stripe
- Sentry
- Basic scheduling worker

### Initial pricing hypothesis

- **Exam Pass:** $29/month for one section and up to 500 questions
- **Exam Pass Plus:** $49/month with written-response grading and mock sets
- **Annual:** $199 prepaid

Do not launch until three paid preorders validate willingness to pay.

## 14-day day-by-day build plan

| Day | Deliverable | Exit criterion |
|---:|---|---|
| 1 | Select one candidate segment and one exam section | Written segment definition and exclusion list |
| 2 | Interview five candidates and map study workflows | Two recurring pain points and one current spend pattern |
| 3 | Define skill taxonomy and build 30 original diagnostic questions | Every question has a skill tag and reviewed explanation |
| 4 | Implement onboarding, diagnostic, and results | User receives scored skill map |
| 5 | Build question engine, answer capture, and explanations | Full practice loop works |
| 6 | Implement error notebook and misconception tags | Misses become structured review items |
| 7 | Build adaptive daily plan and progress dashboard | Plan prioritizes weak skills |
| 8 | Add Stripe, trial, account deletion, and content licensing record | Paid trial flow works |
| 9 | Expand to 75–100 reviewed questions across all diagnostic skills | Question bank passes editorial QA |
| 10 | Deploy production, logging, backups, and monitoring | Production smoke test passes |
| 11 | Run supervised sessions with five pilot candidates | Each candidate completes diagnostic and daily plan |
| 12 | Fix scoring, explanations, mobile UX, and accessibility issues | No critical content or scoring errors |
| 13 | Publish landing page, demo, and waitlist; recruit candidates | Three paid preorders |
| 14 | Final QA and launch decision | Three paid users and content review complete |

### MVP technical stack

- Next.js + TypeScript
- PostgreSQL
- Author-reviewed question bank
- LLM API with constrained prompts
- Stripe
- Sentry
- Simple cron/job worker

## 30-day marketing calendar

**Budget: $200 maximum, organic-first**

| Day/channel | Action | Goal |
|---|---|---|
| Days 1–3 | Publish diagnostic landing page and sample results | Qualified signups with one segment |
| Days 4–6 | Interview 20 candidates and recruit five pilots | Five activated pilots and documented objections |
| Days 7–9 | Share targeted study-planning content in candidate communities | 200 qualified visitors |
| Days 10–12 | Offer free diagnostic to first 100 candidates | 30 completed diagnostics |
| Days 13–15 | Convert completed diagnostics to paid accounts | Five paying candidates |
| Days 16–18 | Publish an anonymized error-pattern report | Authority and qualified traffic |
| Days 19–21 | Ask pilot candidates for testimonials and referrals | Three testimonials or referral commitments |
| Days 22–24 | Reach accounting tutors, professors, and student groups | Three partnership conversations |
| Days 25–27 | Test $29 versus $49 plans | Eight paid accounts |
| Days 28–30 | Review retention, score improvement, content cost, and support | Decide whether to scale, narrow further, or kill |

### Channel mix

- Candidate interviews and direct outreach: 35%
- Student and exam communities: 25%
- Free diagnostic as a lead magnet: 20%
- Tutors, professors, and student groups: 15%
- Paid test: 5% ($50 maximum), only after the diagnostic converts

### 30-day targets

- 100 qualified visitors
- 30 completed diagnostics
- 15 activated users
- 8 paid accounts
- At least $232 MRR at an average of $29
- Day-14 retention above 50%
- At least two weekly practice sessions per retained learner

## Unit economics to $10K MRR

### Base case

- ARPA: **$39/month**
- Gross margin: **78%**
- Monthly gross profit per account: **$30.42**
- Monthly churn assumption: **7%**
- Annual-plan share: 20%

Required customers:

**$10,000 ÷ $39 ≈ 257 customers**

At 78% gross margin, 257 customers provide approximately **$7,818 monthly gross profit** before operating costs.

### Pricing mix scenario

| Plan | Customers | Price | MRR |
|---|---:|---:|---:|
| Exam Pass monthly | 170 | $29 | $4,930 |
| Exam Pass Plus monthly | 65 | $49 | $3,185 |
| Annual equivalent | 22 | $85.75 | $1,887 |
| **Total** | **257** | — | **$10,002** |

### Cost assumptions

- LLM explanations and tutoring: $2–$6 per active account
- Infrastructure and hosting: $100–$300/month
- Original content creation and review: $0.50–$2 per new account initially
- Payment fees: approximately 3%
- Support and content QA: founder time plus occasional subject-matter reviewer

### CAC constraint

With about $30 gross profit per monthly account, paid CAC should stay below roughly **$45–$65**. The strongest channel is likely a free diagnostic plus community distribution, not broad paid ads.

### Path to 257 customers

- 25 pilot and referral students
- 80 community-sourced candidates
- 75 free-diagnostic conversions
- 42 tutor/professor/student-group referrals
- 35 annual-plan buyers

### Expansion revenue

- Written-response grading
- Mock exams
- One additional segment or section only after fit
- Tutor/institution accounts
- Annual plans
- Partnerships with accounting programs

## Kill criteria

Kill or pause if any of the following occurs by day 30:

- Fewer than 3 paid preorders before implementation
- Fewer than 8 paid subscribers by day 30
- Fewer than 15 activated learners
- Day-14 retention below 35%
- Question-content creation exceeds two hours per useful question
- No licensed or original content strategy is viable
- Candidates perceive the product as inferior to established question banks
- The narrow segment does not show independently measurable demand
- AI explanations introduce materially incorrect accounting guidance
- The product attracts broad certification requests that cannot be served without expanding beyond the wedge

### Decision checkpoints

- **Day 3:** one segment and one section are documented
- **Day 7:** 30 reviewed questions and five pilot candidates
- **Day 14:** three paid users and no critical scoring defects
- **Day 21:** eight paid users, day-14 retention above 50%
- **Day 30:** 15 active users and a credible path to 257 customers
