# Heritage Language Coach — Voice-First Family Language Practice

## 1. Why this direction

### TrustMRR evidence

The prior validated research identifies **Speak Silq at approximately $12K MRR** as evidence that heritage and minority-language learning can support a substantial subscription business. It also notes that large language-learning products cover many languages but offer limited depth in family-specific language maintenance.

The category is especially attractive for a solo developer because:

- lessons and practice feedback can begin with templated content;
- voice practice produces visible value;
- family accounts improve retention;
- one language-family niche can be defined through structured curriculum and community content.

The first niche must be narrow enough to support specialized vocabulary, cultural context, and level progression. A sensible test is **Italian for English-speaking families**, but validate it rather than assuming it is best.

### X and web evidence

The Stage A TinyFish calls produced CLI help text only and did not return social evidence.

Conduct and archive genuine searches such as:

- `("heritage language" OR "family language") app (struggling OR tired OR "looking for")`
- `("speak Italian" parents OR children OR family) app`
- `("Italian for beginners" OR "learn Italian") Reddit`
- `"just shipped" language learning app family`
- `("heritage language learning" OR "bilingual children") competitor`

Valid evidence requires URL, date, handle, quote, and engagement. Primary interviews with heritage-language educators and families are essential.

### Customer and promise

**ICP:** English-speaking adults in mixed-language households who want a practical 20-minute daily speaking habit with culturally relevant vocabulary.

**Promise:** Learn and retain useful family and community phrases through short voice drills, spaced review, and optional family practice sessions.

## 2. Competitor table

Check regional pricing and family-plan availability before launch.

| Level | Competitor or substitute | Typical pricing | Strength | Opening for this product |
|---|---|---:|---|---|
| L1 direct | Heritage-language apps and tutoring communities | Often $5–$30/month or class-based | Cultural specificity and human support | Structured daily practice, pronunciation feedback, family mode |
| L1 direct | General language apps | $0–$20+/month | Excellent course infrastructure and brand trust | Heritage motivation, family phrases, adult heritage-learner mode |
| L1 adjacent | AI conversation tutors | $10–$25+/month | Unlimited conversational practice | Purpose-built heritage progression and memory scaffolding |
| L1 adjacent | Online tutors and communities | $10–$50+/lesson | Human correction and accountability | Lower-cost daily rehearsal before tutoring |
| L2 adjacent | Duolingo, Babbel, Busuu | $0–$20+/month | Broad language catalog and polished habit loops | Deeper, narrower heritage curriculum |
| L2 adjacent | YouTube and podcasts | Free to low cost | Authentic native speech | Structured spaced repetition and personal feedback |
| L3 substitute | Flashcards and phone notes | Free | Flexible and familiar | Speech-first practice, adaptive review, fewer setup costs |
| L3 substitute | Family members and community groups | Free | Natural interaction | Conversation prompts and progress visibility |

**Competitive score:** 4/5. General language apps and tutoring create strong substitutes, so this is **GO_NARROW**.

## 3. PRD MVP

### P0 — required for launch

1. **Onboarding**
   - heritage language;
   - native language;
   - current level;
   - family/community goal;
   - dialect preference where relevant.
2. **15-day foundation path**
   - practical phrases;
   - listening;
   - speaking;
   - micro-review;
   - one weekly conversation prompt.
3. **Voice practice**
   - browser recording;
   - speech-to-text comparison;
   - phrase-level pronunciation hints;
   - user self-rating;
   - no unreliable numerical accent score.
4. **Spaced review**
   - interval scheduling;
   - due phrases;
   - mastery states;
   - short daily session.
5. **Family mode**
   - shared phrase deck;
   - adult/child assignment;
   - no direct messaging or child chat;
   - parent-controlled privacy.
6. **Progress**
   - practice streak;
   - words/phrases practiced;
   - weekly listening and speaking minutes;
   - exportable progress.
7. **Safety**
   - no child-directed open chat;
   - minimal child data;
   - parental controls;
   - report only observed errors, not personality judgments.
8. **Billing**
   - Stripe;
   - family monthly/annual plan;
   - trial and cancellation.

### P1 — after validation

- live small-group speaking sessions;
- custom household vocabulary;
- more dialects;
- printable phrase sheets;
- spaced-review import;
- educator dashboard;
- offline audio packs.

### P2 — later

- second heritage language;
- placement assessment;
- certified-tutor referral;
- community audio submission;
- richer pronunciation models;
- school and diaspora-organization licensing.

### Non-goals

- every language at launch;
- accredited language certification;
- child-facing open-ended chat;
- human-level pronunciation judgment;
- cultural claims unsupported by educators;
- replacing tutors or community immersion;
- competing as a broad Duolingo clone;
- diagnostic claims about heritage identity or assimilation.

## 4. 14-day day-by-day build plan

| Day | Solo deliverable |
|---:|---|
| 1 | Interview five heritage learners about retention, embarrassment, goals, and existing tools. |
| 2 | Interview five family members or educators; select one language and one learner outcome. |
| 3 | Interview five more; create and manually test a 15-day phrase curriculum. |
| 4 | Build auth, profiles, learner progress, billing skeleton, and audio storage. |
| 5 | Implement lessons, phrase playback, recording, transcription, and self-review. |
| 6 | Add spaced review, mastery states, daily session generation, and progress metrics. |
| 7 | Add family deck, assignments, parental controls, and privacy-safe profile handling. |
| 8 | Add pronunciation hints, confidence labels, feedback, and failure fallbacks. |
| 9 | Implement Stripe monthly/annual plans, trial, limits, and cancellation. |
| 10 | Complete child privacy, consent, deletion, retention, and reporting safeguards. |
| 11 | Test with 10 target learners; revise instructions and onboarding. |
| 12 | Test browser permissions, accessibility, mobile layouts, and error recovery. |
| 13 | Deliver one live speaking session and close at least 10 beta subscriptions. |
| 14 | Ship, collect week-one retention data, and repair launch blockers. |

## 5. 30-day marketing calendar

**Budget cap:** $250, with most acquisition through communities, educators, and referral.

| Day/channel | Action | Budget |
|---|---|---:|
| 1–3 | Launch one-language landing page with an actual lesson demo | $0 |
| 4 | Publish “15 phrases my Italian family never taught me” | $0 |
| 5 | Ask five educators to review the foundation curriculum | $0 |
| 6 | Share a free downloadable phrase deck in relevant communities | $0 |
| 7 | Run a 20-minute family speaking workshop | $0 |
| 8 | Personally onboard ten learners | $0 |
| 9 | Request learner recordings only with consent; publish a progress story | $0 |
| 10 | Post a spaced-repetition explainer | $0 |
| 11 | Contact five heritage-language educators and community organizers | $0 |
| 12 | Run a $100 diaspora newsletter sponsorship | $100 |
| 13 | Review day-one and day-seven activation | $0 |
| 14 | Fix onboarding or pronunciation-feedback friction | $0 |
| 15 | Publish a weekly family practice prompt | $0 |
| 16 | Run a live conversation session | $0 |
| 17 | Invite five beta families to referral | $0 |
| 18 | Publish a parent privacy explainer | $0 |
| 19 | Approach three community newsletters | $0 |
| 20 | Add household vocabulary customization based on demand | $0 |
| 21 | Compare the product honestly with general language apps | $0 |
| 22 | Interview one churned or inactive learner | $0 |
| 23 | Test annual versus monthly family pricing | $0 |
| 24 | Publish a short learner milestone story | $0 |
| 25 | Run a second educator review session | $0 |
| 26 | Launch a referral reward worth one month, not cash | $0 |
| 27 | Personally contact all highly engaged trial users | $0 |
| 28 | Review week-two retention, speech-practice rate, and support | $0 |
| 29 | Ship the most requested retention feature | $0 |
| 30 | Decide whether to retain language, narrow audience, or kill | $0 |

## 6. Unit economics to $10K MRR

### Pricing

- Individual: **$12/month**
- Family: **$19/month**
- Educator/community: **$49/month for 10 learners**

Assume average realized ARPU of **$15/month**.

| Metric | Assumption |
|---|---:|
| Speech-to-text/model allocation | $2–3 |
| CDN/storage | $1 |
| Support | $1 |
| Payment/overhead allocation | $1 |
| Contribution/account/month | about $9–10 |

- Customers needed: $10,000 / $15 = approximately **667 paid accounts**.
- At 82% gross margin, target variable cost is approximately $1,800/month.
- A 5% monthly logo churn rate requires approximately 33 new paid accounts each month merely to maintain 667 accounts.
- Annual plans can materially reduce churn and acquisition pressure; target 25% annual conversion by month three.

### Retention assumptions

A durable language product needs:

- 7-day activation above 45%;
- week-four retention above 30%;
- three voice sessions per week for at least 50% of retained learners;
- family-plan share above 25%;
- monthly churn below 5% after onboarding stabilization.

## 7. Kill criteria

Kill or re-niche if any occur by Day 30:

- fewer than 30 target-family interviews;
- fewer than 20 complete onboarding;
- fewer than 10 record three speaking drills in the first week;
- fewer than 8 pay;
- fewer than 5 return in week four;
- users prefer generic AI conversation and ignore the structured path;
- pronunciation feedback is consistently perceived as wrong or discouraging;
- educators reject the curriculum’s cultural assumptions;
- child privacy cannot be implemented safely;
- monthly churn exceeds 10%;
- gross margin falls below 70%;
- learner demand cannot be concentrated in one language with 20+ qualified interviewees.

## Wedge (required for GO_NARROW)

**Refuse to build:**

- all languages at launch;
- open-ended child chat;
- accreditation or testing;
- immigration, identity, or assimilation advice;
- unsupported dialect judgments;
- replacement for human tutors;
- a broad general-language course catalog;
- expensive 3D avatars and social features;
- claims that speech recognition establishes fluency.

The MVP serves **English-speaking heritage-language learners in one selected language**, focuses on **one practical family/community outcome**, and provides **structured voice practice and review only**.
