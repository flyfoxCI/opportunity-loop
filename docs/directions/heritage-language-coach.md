---
layout: post
title: "Heritage Language Coach — Product Direction"
date: 2026-11-05T22:33:25+00:00
week: "2026-11-05_223325"
week_date: "2026-11-05T22:33:25+00:00"
slug: "heritage-language-coach"
permalink: /directions/heritage-language-coach.html
tags:
  - "AI"
  - "education"
  - "finance"
  - "language"
  - "mobile"
excerpt: "A conversation-first heritage-language coach for families reconnecting with ancestral languages"
---

## Direction summary

Build a conversation-first language coach for adults who want to reconnect with a family’s ancestral language. The MVP provides short daily speaking practice, pronunciation feedback, culturally relevant phrases, and a family “heritage mode” that balances modern conversation with family terminology.

The product is not another general Duolingo clone and does not promise native-level fluency. Its differentiation is the emotional, familial, and cultural context: learners often have existing exposure but little structured practice or vocabulary relevant to relatives.

- **Tier:** GO
- **Demand:** 4/5
- **Competition:** 2/5
- **MVP horizon:** 14 days, solo
- **30-day marketing budget:** $0–$150
- **Target:** $10,000 MRR

## Why this direction

### TrustMRR evidence

The prior validated direction index identifies a paid demand anchor in small-language learning:

- **Speak Silq:** approximately **$12K MRR**
- The prior research found that major language-learning platforms handled major international languages better than smaller heritage languages
- The opportunity was assessed as differentiated enough for a narrow heritage-language product

This is relevant because heritage-language learning is not merely a smaller Duolingo category. It combines existing emotional motivation, a defined family context, and scarce learning content. The business can target one language and one customer segment initially rather than attempting broad multilingual coverage.

### X/web evidence and validation status

The supplied TinyFish output contains no usable search results, so no social quote is represented as verified.

Discovery should focus on:

- X searches for `heritage language app`, `learn my grandparents language`, `family language learning`, `bilingual family app`, and `Duolingo alternatives`
- Diaspora and heritage-language communities
- Family-language Facebook and Reddit groups
- Language-learning subreddits and educator communities
- Schools and nonprofit family-language programs

Pre-build validation requirements:

1. Fifteen interviews with heritage-language learners or parents
2. Select one language with repeated demand and accessible reference content
3. Ten people complete a seven-day speaking prototype
4. One landing-page paid-intent test with a $15–$29 deposit
5. Three families agree to participate in a paid pilot

### Why this wedge is attractive

- The learner has a durable reason to return: speaking with relatives.
- Daily exercises can fit inside a short mobile/web session.
- A family mode creates a collaborative use case and referral loop.
- Initial content can be narrow: one language, 300–500 phrases, 30 conversations.
- No marketplace, live tutor network, or complex social graph is needed for the MVP.

## Competitor table

### L1 — direct competitors

| Competitor | Positioning | Typical pricing | Strength | Gap to exploit |
|---|---|---:|---|---|
| Speak Silq | Small/heritage language learning | Prior research reports about $12K MRR | Direct paid-demand validation | Opportunity for a more focused family/heritage workflow |
| Lingua / Speak | Heritage and multilingual conversation learning | Varies; verify | Conversation practice and broad language catalog | Heritage-specific family vocabulary and rituals |
| Pimsleur | Audio language courses | Premium pricing | Strong speech-first method and brand | Expensive for occasional family connection; less personalized to family context |
| Italki | Human tutors | Pay-as-you-go hourly | Authentic human feedback | Cost, scheduling, and inconsistent tutor availability |
| Duolingo | General language learning | Free plus paid tiers | Habit-forming product and broad catalog | Limited rare-language depth and family-specific goals |
| Busuu/Babbel | General language courses | Subscription tiers | Structured curriculum and recognized brands | Heritage motivation and family language content underserved |
| LingoRyder / small-language apps | Regional or niche languages | Free/low-cost | Local authenticity and community knowledge | Often limited practice feedback or structured progression |

**Evidence caution:** current pricing and direct substitutes must be rechecked before building. The Stage A `linguana` listing at roughly $29 MRR is only weak corroboration because its exact product is ambiguous. The prior Speak Silq evidence is the stronger anchor.

### L2 — indirect competitors

| Competitor | Positioning | Pricing pattern | Why users may choose it |
|---|---|---:|---|
| YouTube lessons | Free video instruction | $0 | Broad content and real families speaking |
| Family tutors/relatives | Free-to-low-cost | $0 | Authentic, trusted speakers |
| Discord/WhatsApp groups | Community practice | $0 | Real conversation and belonging |
| Anki decks | Flashcards | $0 | Efficient vocabulary retention |
| Generic AI tutors | Conversation practice | Subscription/API | Flexible explanations and role-play |

### L3 — substitutes

| Substitute | Limitation |
|---|---|
| Duolingo | Rare-language content and heritage motivation may be missing |
| Google Translate | No sustained learning loop |
| Family conversations | Inconsistent feedback and limited curriculum |
| Language exchange apps | Matching and safety risks; less family-specific |

## PRD MVP

### Target customer

An English-dominant adult child or grandchild who wants to speak with one elderly relative in a specific heritage language. Start with one language selected from interview demand and community accessibility.

### User promise

“Build the confidence to have a real 10-minute conversation with a relative in the language your family loves.”

### P0 — required for launch

1. **Onboarding**
   - Select language and family relationship
   - Choose dialect or region if relevant
   - Enter one relative’s name and three conversation goals
   - Set daily practice length

2. **Curriculum**
   - 300–500 high-value phrases across greetings, family, food, home, caregiving, and storytelling
   - 30 guided conversations
   - Difficulty progression from recognition to phrase to sentence
   - Cultural notes and “when to use it” guidance

3. **Speaking practice**
   - Record or hold-to-talk response
   - Speech recognition/transcription
   - Pronunciation and grammar feedback
   - Suggested corrected phrase
   - Replay model audio
   - Retry loop with spaced repetition

4. **AI conversation coach**
   - Constrained role-play using only target-language curriculum
   - Difficulty adjustment
   - English fallback option
   - Correction limit per turn to avoid overwhelming beginners
   - Safety prompt for sensitive family topics

5. **Family mode**
   - Share a topic prompt with a relative
   - Generate a 5-minute conversation card
   - Collect “we practiced together” streak
   - Do not require the relative to create an account in the MVP

6. **Progress**
   - Daily streak
   - Phrases mastered
   - Speaking confidence estimate
   - Next recommended activity

7. **Billing**
   - Stripe subscription
   - 7-day trial or $9 intro plan
   - Usage caps for speech and LLM features
   - Cancellation and data deletion

### P1 — first 30-day improvements

- Native-speaker audio recorded for core phrases
- More dialects or regional vocabulary
- WhatsApp/email conversation-card sharing
- Family dashboard for multiple learners
- Formal writing exercises
- Printable conversation sheets
- Reference grammar cards
- Human pronunciation feedback from vetted tutors

### P2 — later

- Live tutor marketplace
- Family video-call mode
- Native-speaker community corrections
- Reading and story adaptation
- Certificate or family proficiency report
- More languages
- Cultural-event and holiday modules

### Non-goals

- Replacing a full language-learning curriculum
- General-purpose translation
- Live tutoring in the MVP
- Claiming native-speaker accuracy
- Supporting every language in the MVP
- Social-network features
- Child-directed learning
- Automatic grading of cultural appropriateness
- Duplicating large, generalized language apps

### Core data model

- **Learner:** id, locale, target_language, dialect, daily_goal
- **FamilyLink:** id, learner_id, relative_alias, relationship, goals
- **Lesson:** id, language, level, type, content
- **Phrase:** id, lesson_id, text, translation, audio_url, cultural_note
- **PracticeSession:** id, learner_id, exercise_id, transcript, score, created_at
- **Conversation:** id, learner_id, topic, level, messages, feedback
- **Subscription:** id, learner_id, stripe_subscription_id, plan, status
- **FamilyStreak:** id, learner_id, date, prompt_id

### MVP architecture

- Next.js responsive web app
- PostgreSQL
- LLM API for constrained coaching
- Browser or mobile speech-recognition API
- Speech-to-text for learner recording
- Audio storage/CDN
- Stripe
- Sentry

### Initial pricing hypothesis

- **Free:** daily phrase and one short practice
- **Heritage:** $19/month
- **Family:** $29/month for up to four related learners
- **Annual:** $149–$199 prepaid

Test $19 and $29 rather than assuming a larger subscription.

## 14-day day-by-day build plan

| Day | Deliverable | Exit criterion |
|---:|---|---|
| 1 | Interview five heritage learners; select one language | Repeated phrases, pains, and willingness-to-pay emerge |
| 2 | Define 300-phrase starter curriculum and 10 conversation topics | Curriculum covers real family conversations |
| 3 | Prototype onboarding and daily lesson flow | Five learners can complete a session unaided |
| 4 | Implement learner accounts, lessons, and phrase practice | Core lesson flow works on mobile |
| 5 | Add recording, transcription, and feedback | Learner receives useful pronunciation feedback |
| 6 | Add constrained AI conversation coach | Coach stays within language and level |
| 7 | Add family conversation cards and sharing | Card works without recipient registration |
| 8 | Add progress, streaks, Stripe, quotas, and trial | Paid trial flow works end to end |
| 9 | Produce and upload model audio for core phrases | 100 priority phrases have clear native-style audio |
| 10 | Deploy, configure privacy, logs, deletion, and backups | Production test passes |
| 11 | Run a seven-day pilot with five families | Four complete at least three practice days |
| 12 | Fix pronunciation, feedback, and content problems | Completion rate above 60% in pilot |
| 13 | Publish landing page, demo, and founder-led conversion test | Three paid orders or deposits |
| 14 | Final QA and launch decision | Two paying families and no critical technical failures |

### MVP technical stack

- Next.js + TypeScript
- PostgreSQL
- Browser SpeechRecognition where supported
- Whisper-compatible transcription fallback
- LLM API for constrained role-play
- Object storage/CDN for audio
- Stripe
- Sentry

## 30-day marketing calendar

**Budget: $150 maximum, organic-first**

| Day/channel | Action | Goal |
|---|---|---|
| Days 1–3 | Publish a short “speak with your grandparent” demo and landing page | Qualified signup and emotional clarity |
| Days 4–6 | Interview and onboard five pilot families | Five activated learners and detailed feedback |
| Days 7–9 | Share story in relevant family-language and diaspora communities | 150 qualified visits |
| Days 10–12 | Publish a free printable conversation-card pack | 40 email or WhatsApp signups |
| Days 13–15 | Ask pilot families to share one completed conversation | Five authentic testimonials or clips |
| Days 16–18 | Publish a family story and founder learning | Build trust and referral intent |
| Days 19–21 | Run a $19 monthly checkout test and annual preorder | Five paid learners |
| Days 22–24 | Approach language teachers and family-learning organizers as channel partners | Two partner conversations |
| Days 25–27 | Publish “10 phrases to use with a grandparent this week” | Search and community traffic |
| Days 28–30 | Review day-7 retention, speech usage, referrals, and support | Decide whether to scale, narrow, or kill |

### Channel mix

- Founder interviews and direct outreach: 35%
- Heritage-language communities: 30%
- Educational content and printable resources: 20%
- Family referrals: 15%
- Paid test: 0% initially; reserve up to $50 only for proven landing-page intent

### 30-day targets

- 60 qualified visitors
- 15 interviews
- 10 activated learners
- 7-day day-7 retention of at least 50%
- 5 paid subscribers
- At least $95–$145 MRR
- Three family referrals

## Unit economics to $10K MRR

### Base case

- Blended ARPA: **$24/month**
- Gross margin: **70%**
- Monthly gross profit per account: **$16.80**
- Monthly churn assumption: **8%**
- Annual-plan share: 20%

Required customers:

**$10,000 ÷ $24 ≈ 417 subscribers**

At 70% gross margin, 417 subscribers produce approximately **$7,000 monthly gross profit** before operating costs.

### Pricing mix scenario

| Plan | Customers | Price | MRR |
|---|---:|---:|---:|
| Heritage monthly | 260 | $19 | $4,940 |
| Family monthly | 80 | $29 | $2,320 |
| Heritage monthly | 45 | $19 | $855 |
| Annual equivalent | 32 | $59.25 | $1,896 |
| **Total** | **417** | — | **$10,011** |

The annual-equivalent row represents prepaid annual plans recognized monthly.

### Cost assumptions

- Speech and LLM inference: $3–$8 per active monthly learner
- Audio/CDN/storage: $0.50–$1.50 per learner
- Infrastructure: $75–$250/month
- Payment fees: approximately 3%
- Community support and content maintenance: founder time plus occasional native-speaker review

### CAC constraint

At $16.80 gross profit per account, paid CAC should remain below approximately **$25–$35** if churn is 8%. This favors community-led and referral acquisition over paid ads.

### Path to 417 subscribers

- 40 pilot learners
- 100 community-acquired learners
- 120 self-serve learners
- 77 referral and family-network learners
- 80 partner/community learners

### Expansion revenue

- Family plans
- Annual plans
- Additional languages
- Premium audio and native-speaker corrections
- Human tutor sessions
- School/library partnerships
- Printed conversation guides

## Kill criteria

Kill or pause if any of the following occurs by day 30:

- Fewer than 5 paid subscribers
- Fewer than 10 activated learners
- Day-7 retention below 35%
- Users treat the product as a novelty rather than practicing weekly
- Speech recognition fails too often for the selected language
- The phrase corpus cannot be licensed or produced reliably
- Users demand a broad all-language curriculum before the narrow experience retains them
- Partner communities reject the product or show weak referral behavior
- Unit contribution margin falls below 50% after native-speaker review and support

### Decision checkpoints

- **Day 7:** one language and one family-use case are clear
- **Day 14:** two paying families and functional speech practice
- **Day 21:** five paying learners and at least 50% day-7 retention
- **Day 30:** 10 active learners, 5 paid subscribers, and a credible path to 417 accounts
