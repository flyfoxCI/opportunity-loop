# Direction: quran-unlock — Heritage-Language Scripture Companion

**Tier:** GO_NARROW
**Slug:** quran-unlock
**TrustMRR evidence:** Quran Unlock, $7 MRR, $7 last30, 275 subs, iOS app, X @iamyacine
**Demand / Competition (heuristic, not X-verified):** 4 / 2

## 1. Why this direction

**TrustMRR evidence:**
- 275 paying subs on a $7/mo product = $1,925 ARR per listing → strong willingness-to-pay in a narrow audience (Muslims wanting to learn Quran in their native language)
- Active founder @iamyacine shipping on iOS — confirms product is buildable solo
- Subscription model with low churn inferred from religious-content pattern

**Prior validated evidence (from `reports/directions/04-lingua-small-language.md`):**
- "Heritage language learning" niche was rated 7/10 in prior research
- Speak Silq validated at $12K MRR on similar small-language wedge
- Duolingo explicitly weak on small/heritage languages
- 14-day MVP is feasible because content is bounded (Quran corpus, finite)

**Wedge rationale (GO_NARROW justification):**
Full "religion AI" market has Sermon Scribe at $14K MRR (validated) plus dozens of Christian apps. Pure GO would compete with those. The narrow wedge is:
- **One scripture** (Quran, not Bible/Torah/Gita)
- **One job-to-be-done** (learn recitation + meaning in your native language)
- **One ICP** (non-Arabic-speaking Muslims aged 18-40, English/Urdu/French/Bahasa first)
- **Refuse:** Hadith search, fiqh rulings, prayer-time widgets, halal-scanners — anything Sermon Scribe or other Muslim apps do

## 2. Competitor table

| Tier | Competitor | What they do | Pricing | Why we don't collide |
|---|---|---|---|---|
| L1 direct | Quran.com | Web Quran reader + translations | Free | No AI, no recitation coaching, no spaced repetition |
| L1 direct | Tarteel AI | Real-time Quran recitation feedback | $10/mo | Audio-only, English-first, no translation/meaning drills |
| L1 direct | Bayyinah TV (Zaid Ali) | Video-based Arabic learning | $15-30/mo | Not app-first, not on-demand, course format |
| L2 adjacent | Duolingo Arabic | Tiny Arabic course | Free/$14 | Doesn't teach Quran vocabulary; gamified, not scripture |
| L2 adjacent | Muslim Pro | Prayer times + Quran + Qibla | Free w/ads | Multi-purpose, weak on learning loop |
| L3 distant | Sermon Scribe (Christian) | Sermon writing AI | $30/mo | Different religion, but validates "faith AI" willingness-to-pay |
| L3 distant | Hallow (Catholic) | Prayer/meditation app | $10/mo | Audio devotionals, not scripture learning |

**Competition score: 2.** Tarteel is the only true direct competitor, and they don't do translation/meaning drill. Web Quran readers are free but lack the learning loop.

## 3. PRD MVP

### User story
As a non-Arabic-speaking Muslim, I want to read 1 ayah per day, hear correct Arabic recitation, learn 3 new vocabulary words, and review yesterday's words — in a 5-minute daily session.

### Epic E1: Daily Ayah (P0)
- Pick from 3 ayahs/day based on user level (beginner/intermediate)
- Show Arabic text + transliteration + chosen translation (EN/Urdu/French/Bahasa)
- Tap-to-hear correct recitation (use everyayah.com API — free)
- "I learned this" button → moves to review queue

### Epic E2: Vocabulary SRS (P0)
- Spaced repetition for word-level learning (SM-2 algorithm)
- 5 new words/day target, reviews prioritized
- Word card: Arabic + transliteration + meaning + example ayah
- Streak tracking with Islamic-themed rewards (no gambling imagery)

### Epic E3: Audio check-in (P1)
- Record yourself reciting the daily ayah
- Compare duration only (not tajweed — out of scope for MVP)
- "Submitted" badge for accountability

### Epic E4: Progress dashboard (P1)
- Total ayahs completed, words learned, streak
- Calendar view of consistency

### Epic E5: Push notifications (P1)
- Daily 6am local reminder (configurable)
- Streak-saver notification 2h before reset

### Non-goals (P2 / OUT)
- ❌ Tajweed rules coaching — too complex for 14d MVP, and Tarteel owns this
- ❌ Hadith search
- ❌ Fiqh / rulings / halal scanner
- ❌ Prayer time / Qibla / mosque finder
- ❌ Community features / friends
- ❌ Multiple Qurans / translations beyond top 4 languages
- ❌ Web app (iOS only for MVP)
- ❌ Arabic-script learning (separate product)

### Tech stack
- Frontend: React Native (Expo) — iOS only for MVP
- Backend: Supabase (Postgres + Auth + Edge Functions)
- Audio: everyayah.com for recitation (free CDN)
- AI: OpenAI gpt-4o-mini for translation paraphrase + word explanations (≤$5/mo at 100 users)
- Notifications: Expo push
- Payments: RevenueCat (App Store IAP, $7/mo or $60/yr)

### Data model
