---
layout: post
title: "Heritage Language Coach"
date: 2026-11-02T23:47:21+00:00
week: "2026-11-02_234721"
week_date: "2026-11-02T23:47:21+00:00"
slug: "heritage-language-coach"
permalink: /directions/heritage-language-coach.html
tags:
  - "AI"
  - "B2C"
  - "education"
  - "finance"
  - "language"
  - "mobile"
excerpt: "AI conversation coach for families learning a heritage language"
---

## Why this direction

### TrustMRR evidence

- The prior validated direction index cites **Speak Silq at approximately $12K MRR**, evidence that consumers pay for language-learning workflows, especially around underserved languages.
- The broad language-learning market is competitive, so this is a **GO_NARROW** with competition score 4.
- The wedge is not another Duolingo replacement. It is a **family heritage-language practice assistant** where one language is passed between generations, learners have varying proficiency, and conversation topics are culturally specific.
- A 14-day MVP can use structured conversation practice, pronunciation-friendly text support, role-play prompts, and family practice plans without building a complete adaptive curriculum platform.

### X/web evidence

- Heritage-language learners often report that generic apps teach modern textbook vocabulary but fail to reproduce conversations with grandparents and relatives.
- Common pain themes include:
  - shame about speaking
  - vocabulary gaps with family
  - inconsistent practice
  - difficulty getting relatives to participate
  - dialect and code-switching concerns
- Searches should be language- and family-specific:
  - `AI language coach heritage language`
  - `learn language with grandparents app`
  - `Duolingo heritage language complaint`
  - `language practice too expensive`
  - `family language app just shipped`
- The opportunity becomes stronger if one specific heritage language has a dense community and recurring cultural content needs.

### Selected initial scope

Start with **one heritage language and one family scenario**, such as adult children learning Vietnamese to speak with grandparents, or Spanish-speaking families practicing English. The final language must be selected through interviews and community validation during the first two days.

## Competitor table

| Level | Product | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Speak Silq | AI language practice, with reported demand for underserved languages | Around $12K MRR listing; verify pricing | Closest commercial proof |
| L1 | Speak (by OpenAI) | General conversational language practice | Freemium/paid tiers | Major modern conversation competitor |
| L1 | Duolingo | Gamified broad language learning | Freemium plus premium tiers | Dominant substitute and brand benchmark |
| L1 | Pimsleur | Audio-led language courses | Premium subscription | Strong immersive-learning substitute |
| L1 | Preply | Human tutor marketplace | Variable lesson pricing | Human alternative |
| L2 | italki | Human tutoring marketplace | Variable hourly pricing | Affordable human conversation option |
| L2 | Busuu, Babbel, Rosetta Stone | Structured language courses | Subscription tiers | Deep but less personalized alternatives |
| L2 | Lingoda | Courses with live teachers | Subscription | Community and live-practice alternative |
| L3 | YouTube, language Discord servers, family messaging | Free informal practice | Free | Powerful zero-price substitute |

### Competitive conclusion

Competition score is 4. The product wins only with a sharply defined cultural and family workflow: **one heritage language, family scenarios, role-play with elders, and practice plans involving relatives**.

## Wedge

### Narrow scope

- Exactly one heritage language
- One learner type: adult relatives trying to communicate with family
- One shared activity: a 10-minute family conversation practice
- Role-play characters representing common family situations
- Cultural notes that distinguish family usage from textbook usage
- One invited relative can participate via a simple share link
- Progress centered on practical phrases and family conversations, not general exam preparation

### What this product refuses to build

- No general language-learning curriculum
- No support for many languages in the MVP
- No exam-preparation system
- No formal grammar textbook
- No human marketplace or live-tutor booking
- No claim of native-level accuracy without expert review
- No automatic celebrity voice cloning
- No manipulation of family members’ audio without consent
- No broad social feed or public language marketplace
- No native mobile apps

### Why the wedge can work

- Family relationships create emotional persistence absent from generic apps.
- A single language allows deep vocabulary, role-play, and cultural curation.
- Inviting a relative creates a collaborative loop and visible weekly engagement.
- The learner can reach a meaningful family outcome before reaching broad fluency.

## PRD MVP

### Target customer

Adult heritage-language learner who wants to communicate more naturally with parents, grandparents, or extended family.

### Primary outcome

Complete a culturally specific family conversation practice and leave with a short, realistic action for the next real interaction.

### P0

- One selected language and locale
- Onboarding:
  - proficiency self-rating
  - goals
  - family relationship
  - comfort level
- Scenario library with 10–15 family situations:
  - greeting elders
  - asking about health
  - meal invitations
  - holidays
  - family news
- Voice-based role-play with text fallback
- Slow and natural replay controls
- Phrase explanations and cultural notes
- Corrections that distinguish errors from regional variation
- Weekly personal practice plan
- Progress dashboard for practiced scenarios
- Share link allowing one relative to join a practice session
- Subscription checkout and usage limits
- Explicit consent for recording and deletion

### P1

- Family practice assignment
- Favorites and saved phrases
- Text-message prompt templates
- Relative-side prompt support
- Pronunciation feedback
- Dialect preference setting

### P2

- More scenarios and languages
- Live conversation with a coach
- Printed family phrase cards
- Curriculum partnerships
- Community stories
- Calendar reminders

### Non-goals

- No broad language course
- No academic test preparation
- No formal certification
- No human tutor marketplace
- No generic travel phrasebook
- No full social network
- No autonomous claims about cultural correctness
- No voice cloning

### Technical approach

- Responsive web app
- Speech-to-text and text-to-speech APIs
- Server-side scenario and phrase content
- LLM constrained to an approved scenario and cultural reference set
- Text-first fallback for poor connectivity or privacy-sensitive users
- Explicit recording consent and short retention
- Locale-aware pronunciation dictionary
- Subscription metering
- Human cultural review before scenario publication

### Pricing

- **Free:** three scenarios
- **Family:** $14/month
- **Family Plus:** $24/month with shared practice and downloads
- One-time family practice pack: $19

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|---|
| 1 | Select one heritage language and interview 10 learners | One family communication job and one scenario confirmed |
| 2 | Recruit two native/cultural reviewers | Review and correction workflow established |
| 3 | Prototype first conversation | User completes a family role-play and sees feedback |
| 4 | Create 10 scenario definitions | Each scenario has goals, phrases, and cultural notes |
| 5 | Authentication, onboarding, and billing | User can start a selected scenario |
| 6 | Speech input/output with text fallback | Both modalities complete successfully |
| 7 | LLM conversation state and constrained responses | Model stays within scenario and level |
| 8 | Cultural notes and correction UX | Feedback distinguishes error from regional usage |
| 9 | Weekly plan and progress tracking | User receives and completes a practice assignment |
| 10 | Relative share-link experience | Relative can join one assisted practice flow |
| 11 | Recording consent, deletion, and usage caps | Privacy and cost controls pass |
| 12 | Landing page, checkout, and onboarding polish | Visitor can purchase and start within five minutes |
| 13 | Language/cultural QA and mobile test | Two expert reviewers approve all launch scenarios |
| 14 | Pilot launch | Ten learners complete at least two sessions |

## 30-day marketing calendar

**Budget: $220 maximum**

| Day | Activity | Budget | KPI |
|---:|---|---:|---|
| 1 | Publish one-language, one-family landing page | $0 | 100 targeted visits |
| 2 | Post a real family-role-play clip | $0 | 20 comments |
| 3 | Reach 20 heritage-language communities | $0 | 10 replies |
| 4 | Publish “textbook versus family speech” example | $0 | 15 signups |
| 5 | Host a family conversation practice circle | $0 | 10 attendees |
| 6 | Onboard ten pilot learners | $0 | 10 activated users |
| 7 | Ask learners which scene matters most | $0 | Top 5 scenarios identified |
| 8 | Publish a learner story | $0 | 15 qualified visits |
| 9 | Post a culturally specific phrase card | $0 | 20 shares |
| 10 | Ask native speakers to review the experience | $0 | 5 reviewer comments |
| 11 | Contact heritage-language educators | $0 | 3 conversations |
| 12 | Share a before/after confidence poll | $0 | 8 trial activations |
| 13 | Publish a family-conversation guide | $0 | 12 signups |
| 14 | Review week-two retention | $0 | ≥40% second session |
| 15 | Add one requested scenario | $0 | 70% scenario completion |
| 16 | Ask 5 pilots to invite relatives | $0 | 5 shared sessions |
| 17 | Publish a family-participation workflow | $0 | 10 signups |
| 18 | Contact community administrators | $0 | 3 placements |
| 19 | Run a live pronunciation practice session | $0 | 12 attendees |
| 20 | Review speech-failure and fallback rates | $0 | <10% session failure |
| 21 | Publish a trust/privacy explainer | $0 | 5 objections resolved |
| 22 | Sponsor one relevant community newsletter | $60 | 30 targeted visits |
| 23 | Create a family challenge template | $0 | 15 referrals |
| 24 | Publish a scenario-specific demo | $0 | 10 signups |
| 25 | Ask satisfied users for testimonials | $0 | 3 testimonials |
| 26 | Offer annual plan to active users | $0 | 3 annual conversions |
| 27 | Sponsor one relevant cultural publication | $60 | 30 targeted visits |
| 28 | Publish a community-partner spotlight | $0 | 8 trials |
| 29 | Optimize paywall and onboarding | $0 | Trial-to-paid ≥8% |
| 30 | Review MRR, retention, and cultural accuracy | $0 | Continue/iterate decision |

Budget allocation: $120 community newsletter placements, $50 voice/demo tools, $50 contingency.

### Organic channels

- Heritage-language Facebook and Reddit communities
- Family and diaspora cultural organizations
- Language educators and cultural associations
- Short videos using authentic family scenarios
- Referral loop between learners and relatives
- User-generated scenario requests
- Partnerships with cultural newsletters and diaspora media

## Unit economics to $10K MRR

### Base case

- Blended ARPA: $19/month
- Customers required:  
  `10,000 / 19 = 527`
- This is the highest top-of-funnel requirement of the four directions and requires strong retention.

### Funnel

- 8,000 qualified visitors over 90 days
- 12% signup: 960
- 50% activate a scenario: 480
- 8% of activated users pay: 38 in 30 days; a 90-day mature cohort can support 527 subscribers if weekly retention and referral rates hold.

### Cost assumptions

- Speech, language model, hosting, and storage: $2–$5 per active paid user/month
- Payment processing: approximately 3%
- Content review and support: target under $1 per paid user monthly
- Gross margin target: ≥70%
- Audio caching must prevent repeated model calls for the same phrases

### $10K MRR mix

- 450 Family users at $14 = $6,300
- 150 Family Plus users at $24 = $3,600
- 42 additional paid users at $14 = $588
- Total: 642 subscribers and $10,488 MRR

### Guardrails

- Do not scale acquisition until four-week paid retention is measured.
- Keep cultural review cost explicit.
- Do not add languages until the first language reaches at least 100 paying users.
- If voice usage causes contribution margin below 60%, gate or price it separately.
- Track “family conversation attempted,” not merely minutes learned.

## Kill criteria

Kill or reposition if any of the following occurs by day 30:

- Fewer than five of 10 interviewed learners report a frequent family-conversation problem.
- Fewer than three native/cultural reviewers validate the initial scenarios.
- Fewer than 40% of activated learners complete a second session.
- Weekly retained cohort falls below 25% by week four.
- Paid conversion remains below 5% after 200 activated learners.
- Variable cost exceeds $6 per paying subscriber monthly.
- Users prefer generic AI practice and show little interest in family-specific scenarios.
- A relative-sharing flow produces less than 10% participation.
- Cultural inaccuracies create recurring user harm or expert-review failures.
- The product requires more than $300 monthly marketing spend to acquire the first 50 users.
- Expansion to a second language is necessary before the first language has 100 paid subscribers.
