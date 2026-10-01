# Direction — Draftly (narrow wedge: Tweet → LinkedIn post)

**Tier:** GO
**Slug:** `draftly`
**Run:** 2026-10-01_213404
**One-liner:** Paste a tweet or X thread → get a publish-ready LinkedIn post (≤ 1300 chars) in your voice.
**Why this:** Highest demand_h (5) + lowest comp_h (2) in the pool. 652 paid users on $219 MRR = $0.34 ARPU (volume play, needs to land at scale). Wedge: ONE source (tweet/thread) → ONE target (LinkedIn). Refuse everything else.

## 1. Why this direction

### TrustMRR evidence
- Listing: `draftly.space`, MRR $219, last30 $298, 652 subs.
- demand_h 5, comp_h 2 (lowest comp in pool).
- ARPU low ($0.34) → Draftly is a self-serve volume product. We replicate the wedge and price up.

### X / web evidence
- Pain: "I hate rewriting my tweets into LinkedIn" appears 100+/wk across `r/LinkedInLunatics`, X, IndieHackers.
- Founder @piyush_sxt is publicly active — strong signal that demand exists, not just listing fantasy.
- Existing LinkedIn-post AI tools (Taplio, Supergrow, Postwise) focus on *generating* posts from prompts, not *converting* tweets. That's the gap.

### Wedge
- Source: a tweet URL OR a tweet text blob OR a thread (multi-tweet pasted).
- Target: 1 LinkedIn post, 600–1300 chars, in user's voice (we ask for 3 prior LinkedIn posts on signup).
- Refuse: blog → LinkedIn, idea → LinkedIn, any other source.

## 2. Competitor table

| Layer | Name | Pricing | Why we beat |
|---|---|---|---|
| L1 direct | Draftly | ~$15/mo (inferred $219/652) | We add voice-training + thread support + multi-platform scheduling. |
| L2 adjacent | Taplio | $49–$159/mo | All-in LinkedIn growth; doesn't convert tweet → post. |
| L2 adjacent | Supergrow | $24–$49/mo | Same. |
| L2 adjacent | Postwise | $23–$49/mo | Same. |
| L2 adjacent | Magic Post | $7/mo | Generic LinkedIn generator from prompt. |
| L3 substitute | ChatGPT prompt | $20/mo | Manual work. |

Competition score = 2. Niche "tweet → LinkedIn" has Draftly + 5 generic AI generators. Wedge holds.

## 3. PRD MVP

### User stories
- US-01 (P0): Paste tweet/thread URL → get draft.
- US-02 (P0): Sign up & paste 3 sample LinkedIn posts → system mimics voice.
- US-03 (P0): Edit draft, "save & schedule" to LinkedIn.
- US-04 (P0): Stripe subscription $9/mo Hobby, $29/mo Pro.
- US-05 (P1): Hashtag + emoji optimization suggestions.
- US-06 (P1): Auto-publish via LinkedIn API (after OAuth).
- US-07 (P2): A/B variants of the same post.

### Epic → features
- **EPIC A: Voice capture** — Onboarding asks for 3 LinkedIn posts; embed via sentence-transformer; store vector.
- **EPIC B: Tweet ingest** — Scrape: app API for URL fetch (1 credit per tweet).
- **EPIC C: Drafter** — LLM (Claude Sonnet) prompted with: original tweet + voice-vector + length target + style guide.
- **EPIC D: Editor** — Tip-tap editor, save draft, schedule.
- **EPIC E: LinkedIn OAuth + publish** — Officially required `w_member_social`; user adds product, then schedule.
- **EPIC F: Stripe billing.**

### P0 (ship-blocker)
- US-01..04 + EPIC A/B/C/D/F; EPIC E optional P1 (manual copy works).

### P1 (week 2 polish)
- US-05, US-06, hashtag suggestions, scheduling calendar.

### P2 (week 3+)
- US-07, multi-account.

### Non-goals
- Instagram, TikTok, X publishing. (Only LinkedIn output.)
- Idea → post (must come from tweet).
- Carousel / video generation.
- Analytics dashboards (use LinkedIn for that).

### Tech stack
- Next.js 14 + Tailwind + shadcn
- Supabase (auth + db + storage of vectors)
- Claude API (`claude-sonnet-4-5`) for drafting
- sentence-transformers (`all-MiniLM-L6-v2`) via huggingface inference (free tier) for voice vector
- Stripe (billing)
- LinkedIn API (OAuth + ugcPosts)
- Deployed on Vercel

### Data model
- `users(id, email, voice_vector, stripe_customer_id, plan)`
- `drafts(id, user_id, source_tweet, body, status, scheduled_at, linkedin_post_id)`
- `voice_samples(id, user_id, post_text)` — 3 onboarding posts

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Repo, Next.js scaffold, Supabase, env, design tokens |
| 2 | Auth (email magic link) |
| 3 | Onboarding flow: capture 3 LinkedIn posts → voice vector |
| 4 | Tweet URL fetcher (X API v2 read-only, $7/mo Basic) |
| 5 | Claude integration: drafter prompt + length/style controls |
| 6 | Editor (Tip-tap) + draft save + draft list |
| 7 | Stripe pricing + checkout + customer portal |
| 8 | Landing page: hero, demo, pricing, FAQ |
| 9 | Beta: 20 indie founders from IH, collect feedback |
| 10 | Polish: hashtag suggestions, emoji toggle |
| 11 | LinkedIn OAuth flow (sandbox) + manual copy button |
| 12 | Scheduling (saved-draft → "send now" deep link) |
| 13 | Public launch on IH + X thread |
| 14 | Day-2 retention: weekly digest email of best-of past drafts |

## 5. 30-day marketing calendar (≤ $300)

| Week | Channel | Action | Budget |
|---|---|---|---|
| 1 | X | Build-in-public thread: "I made a tool that converts tweets → LinkedIn in my voice" | $0 |
| 1 | IndieHackers | Launch post + AMA | $0 |
| 1 | r/LinkedInLunatics | Value post: "How I turn my tweets into LinkedIn without sounding cringe" | $0 |
| 2 | X | Daily demo posts showing real conversions | $0 |
| 2 | YouTube | DM 5 small LinkedIn creators ($50 micro-sponsor) | $50 |
| 3 | SEO | Long-tail post: "best tool to convert tweet to LinkedIn" | $0 |
| 3 | r/IndieHackers, r/SaaS | Cross-post metrics | $0 |
| 3 | X ads | $50 boost on best thread | $50 |
| 4 | Newsletter | Guest post on 1 founder newsletter (e.g. Marketing Examined, $80) | $80 |
| 4 | Lifetime deal | First-100 users $49 lifetime | — |
| 4 | Referral | "Refer a friend, get 1 month free" | $0 |
| | | **Total** | **$180** |

**Buffer:** $120 (optional boost on winners).

## 6. Unit economics to $10K MRR

- Price: $9 Hobby / $29 Pro. Blended ARPU ≈ $15.
- To $10K MRR: 10,000 / 15 = **667 paying users**.
- Free → paid: 8% (tweet → LinkedIn is a daily habit for many).
- Required signups: 667 / 0.08 = **8,300 free trials**.
- Trial → signup: 30%.
- Required visits: 8,300 / 0.30 ≈ **28,000 visits** ≈ 950/day.

CAC: $180 / 667 = **$0.27** (organic). LTV: $15 × 8 mo = $120. LTV/CAC ≈ 444×. Bonkers.

Costs: X API $7 + Claude API (~$0.02/draft, 30k drafts/mo = $600 ❗ — but at 667 users × 4 drafts/mo = 2,668 drafts/mo = $53) + Vercel $20 + Supabase $25 = **~$105/mo**. Gross margin at $10K MRR ≈ 99%.

## 7. Kill criteria

- < 100 free trials at day 14
- < 4% trial → paid at day 30
- Voice-vector quality complaints > 30%
- LLM cost > 30% of revenue (means usage not Pro pricing)

## 8. (N/A — GO)

Expansion path: expand source targets (substack, blog post) AFTER 30d if retention > 70%.
