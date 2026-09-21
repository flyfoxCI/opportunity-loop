# Direction: sonora-ai-voice-notes (GO_NARROW)

## Why this direction

**TrustMRR evidence**
- Sonora AI: $38 MRR / $45 last30 / 190 subs — iOS voice-memo app, growing
- Stage A coarse score: demand=3, competition=2 (passes dual gate as pure GO)
- Parent cluster (ai_video_ugc) is hot: $1,960 ΣMRR from TrendStory/WhiteGlove/Vid.AI
- KILL_OR_UNBUNDLE in full-market UGC video (comp=5) → narrow wedge required

**X / web evidence (Stage A heuristic)**
- "voice memo to social clip", "turn voice notes into reels" trending creator search
- Solo creators constantly tweet: "I have 100 voice memos with great ideas, can't edit them into videos"
- Existing tools (Descript, Riverside) are desktop + expensive; mobile-first voice-note→clip is empty

**Why now**
- UGC / short-form video is the dominant creator format 2024-2026
- 80%+ of UGC ideas start as voice notes (podcasters, founders, coaches)
- Current path: voice memo → manual transcript → manual edit → post. Slow.
- Mobile-only "voice note → polished 60-sec clip" is the unbundle

## Competitor table (PARENT market — UGC video)

| Tier | Competitor | Price | Weakness |
|---|---|---|---|
| L1 direct | TrendStory | $19-99/mo | Trend-driven, not voice-first, generic |
| L1 direct | White Glove Content | $200+/mo | Human service, not self-serve |
| L1 direct | Vid.AI | $29-99/mo | Script-to-video, not voice-to-clip |
| L1 direct | Descript | $24-60/mo | Desktop-first, complex, podcast-focused |
| L2 adjacent | Riverside.fm | $19-29/mo | Recording-first, not editing |
| L2 adjacent | Captions.ai | $9-99/mo | Caption-focused, not full edit |
| L2 adjacent | Opus Clip | $19-99/mo | Long-form → short, not voice-first |

**Parent competition: 4-5** (cluster comp high)

**Our NARROW wedge competition: 2**
- Mobile-only + voice-note-first + auto-clip-to-reels = empty
- Closest: Captions.ai (captions, not edit) + Veed iOS (general video editor)
- No one owns "voice memo → 60-sec ready-to-post clip" on mobile

## PRD MVP

**User story (P0)**
> As a podcaster/founder/coach, I open the iOS app, hit record, talk for 60 seconds about an idea, and the app auto-cuts it into 3 polished 15-20 second clips with captions, B-roll, and music — ready to post to TikTok/IG/Shorts.

**Epic 1 — Voice note capture (P0)**
- In-app record (max 3 min)
- Import existing voice memos from iOS
- Auto-transcribe (Whisper API)

**Epic 2 — Auto-clip (P0)**
- LLM detects 2-3 "best moments" (interesting claim, story beat, hot take)
- Auto-cut to 15-30 sec clips
- Add captions (Burnt-in, animated)

**Epic 3 — Polish (P1)**
- Auto-B-roll from stock library (Pexels API) matched to content
- Background music (epidemicsound lite or royalty-free)
- Vertical 9:16 export

**Epic 4 — Direct post (P1)**
- Share sheet to TikTok / IG / Shorts
- (P1) API direct post

**Non-goals (MVP)**
- ❌ Desktop / web version
- ❌ Multi-track audio editing
- ❌ Long-form podcast editing (60-90 sec only)
- ❌ Android (iOS first)
- ❌ Team / collaboration
- ❌ Recording studio features (Riverside territory)

**Tech stack (solo, 14 days)**
- iOS app: SwiftUI + AVFoundation
- Backend: Python FastAPI
- Transcription: Whisper API
- LLM clip-detection: GPT-4o-mini
- Captions: CapCut-style template (or custom burned-in)
- B-roll: Pexels API
- Music: royalty-free library (or Epidemic API)
- Payments: StoreKit + Stripe (web fallback for upgrades)
- Distribution: App Store

## 14-day build plan

| Day | Task |
|---|---|
| 1 | Landing page + App Store pre-launch waitlist |
| 2 | iOS app skeleton (SwiftUI) + auth (Sign in with Apple) |
| 3 | In-app record + import voice memos |
| 4 | Whisper transcription pipeline + display |
| 5 | LLM "best moment" detection |
| 6 | Auto-clip + captions burned-in |
| 7 | **Soft launch** — post on X, IH, r/podcasting, r/newtubers |
| 8 | App Store submission (TestFlight beta) |
| 9 | B-roll integration (Pexels) |
| 10 | Music layer + 3 presets |
| 11 | Vertical export + share to TikTok/IG |
| 12 | App Store listing copy + screenshots |
| 13 | Influencer outreach (10 creators, free 1-year code) |
| 14 | **Public launch** — App Store + X thread + ProductHunt |

## 30-day marketing calendar (budget ≤ $300)

| Week | Activity | Cost |
|---|---|---|
| 1 | X thread: "I built a voice-memo → reel app in 14 days" | $0 |
| 1 | r/podcasting, r/newtubers, r/ContentCreation — value posts | $0 |
| 1 | DM 30 podcasters/coaches with free 1-year codes | $0 |
| 2 | 5 SEO posts: "voice memo to reel", "turn voice notes into short videos" | $0 |
| 2 | Sponsor 2 mid-tier creator YouTubers ($50 each) | $100 |
| 2 | Guest on 1 creator podcast | $0 |
| 3 | App Store feature pitch (small indie section) — $0 cost | $0 |
| 3 | 3 micro-influencer sponsorships ($40 each, creator niche) | $120 |
| 4 | ProductHunt launch — $80 featured | $80 |
| 4 | "Free 5-clip trial" lead magnet + email | $0 |
| 4 | User showcase: retweet best clips made | $0 |

**Total: $300** (at cap)

**KPI targets**
- Day 7: 200 downloads, 20 paid
- Day 14: 800 downloads, 80 paid
- Day 30: 3,000 downloads, 350 paid @ $9.99/mo = $3,500 MRR (iOS pricing)
- OR web upgrade $19/mo for power users
- Path to $10K: 1,000 iOS subs @ $9.99 OR 525 web subs @ $19

## Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Price (iOS) | $9.99/mo or $79.99/yr |
| Price (web) | $19/mo Pro |
| Free tier | 5 clips/mo, no card |
| Conversion (free → paid) | 8% (mobile app avg) |
| LTV (8 mo avg retention, iOS) | ~$80 |
| Gross margin | ~70% (Whisper + LLM + storage) |
| CAC | ~$10 (mostly organic) |
| LTV/CAC | ~8:1 |

**Path to $10K MRR**
- 1,000 iOS @ $9.99 OR mix iOS + web
- iOS churn is higher → need constant acquisition
- Realistic in 9-12 months

## Kill criteria
- Day 14: <10 paid subs → pivot ICP (founders vs. podcasters)
- Day 30: <80 paid → kill or major pivot
- App Store rating <4.0 → UX rebuild
- LTV/CAC < 3 by day 60 → stop paid spend

## Wedge (required for GO_NARROW)

**What we refuse to build** (deliberate narrowing):

1. ❌ **No desktop / web-first version** — mobile-only, voice-first. If a user wants a desktop NLE, they should use Descript. We own mobile voice-memo → clip.

2. ❌ **No long-form podcast editing** — 60-90 sec clips max. Riverside / Descript own that. We own the *opposite*: short, immediate, idea-to-clip.

3. ❌ **No multi-track / studio recording** — single voice, no remote guests. We are not a recording platform.

4. ❌ **No script-to-video** (Vid.AI territory) — we are voice-FIRST. If you wrote a script, you don't need us.

5. ❌ **No Android for v1** — iOS only. Resist the temptation to "expand the market."

6. ❌ **No team / agency plans** — solo creators only. Resist B2B "agency seat" expansion for 6 months minimum.

**The wedge, in one sentence:**
> "For solo creators who think in voice memos, Sonora is the fastest path from idea to posted short-form video — mobile-only, voice-only, 60 seconds max."

If you can describe your use case without the words "voice memo" or "phone," Sonora is not for you.
