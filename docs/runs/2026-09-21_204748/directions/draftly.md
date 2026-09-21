# Direction: draftly

## Why this direction

**TrustMRR evidence**
- $240 MRR / $306 last30 / 706 subscribers — real paying customers, growing
- Stage A coarse score: demand=5, competition=2 (passes dual gate as pure GO)
- Founder @piyush_sxt active on X building in public

**X / web evidence (Stage A heuristic)**
- "AI email writer" / "personalization at scale" is a top-searched indie SaaS query
- Solo creators, consultants, B2B freelancers constantly tweet: "I need to send 50 personalized cold emails and not lose my mind"
- Draftly's positioning (learns your voice from past emails) is the wedge vs. generic GPT wrappers

**Why now**
- Cold email + newsletter + sales-personalization is a $1B+ software category
- Existing players (Smartwriter, Instantly, Lemlist) are bloated and priced for teams ($30-99/mo)
- Solo creators want $10-29/mo self-serve, no setup

## Competitor table

| Tier | Competitor | Price | Weakness |
|---|---|---|---|
| L1 direct | Smartwriter.ai | $59-299/mo | Expensive, complex, requires API keys |
| L1 direct | Instantly.ai personalization | $30-97/mo | Bundled into larger cold-email tool, not standalone |
| L1 direct | Lemlist | $59-99/mo | Same — email-sender with personalization add-on |
| L2 adjacent | ChatGPT + custom prompts | $20/mo | Manual, no learning loop, no bulk send |
| L2 adjacent | Clay.com | $149-800/mo | Enterprise/SDR teams, not solo creators |
| L3 substitute | VA (virtual assistant) | $500+/mo | Slow, expensive, inconsistent voice |
| L3 substitute | Mailshake / Reply.io | $30-99/mo | Bulk sender, weak personalization |

**Competition score: 2** — many players but no one owns "personalization that learns your voice + solo-creator-priced" wedge. Direct competitors are priced 3-10x higher.

## PRD MVP

**User story (P0)**
> As a solo creator/founder, I paste 10-20 of my past emails, get a "voice profile," then paste a list of prospects (name + company + hook) and get 50 unique personalized emails I can send today — in my voice, not generic GPT.

**Epic 1 — Voice learning (P0)**
- User pastes 10+ past emails (or tweets, or LinkedIn posts)
- LLM extracts: tone (casual/formal), sentence length, vocabulary patterns, opener style, CTA style
- Returns "voice profile" JSON stored per user

**Epic 2 — Bulk personalization (P0)**
- Upload CSV: name, company, role, hook
- Output CSV: 1 personalized email per row, in user's voice
- Configurable: subject line variants, length, CTA template
- 14-day free trial: 50 emails; paid: unlimited

**Epic 3 — Send / export (P0)**
- One-click copy per email
- "Copy all to clipboard" (formatted as Gmail-pasteable)
- CSV export with subject + body columns
- (P1) Direct Gmail OAuth send
- (P1) Direct integration with Instantly / Smartlead

**Epic 4 — Templates & presets (P1)**
- Cold outreach, newsletter reply, investor update, sales follow-up
- User can save custom templates

**Non-goals (MVP)**
- ❌ Built-in email sending / warmup (use existing tools)
- ❌ Lead scraping (use Apollo/Clay/Instantly)
- ❌ CRM / pipeline management
- ❌ Multi-account / team features (solo only)
- ❌ Mobile app

**Tech stack (solo, 14 days)**
- Frontend: Next.js + Tailwind, single page app
- Backend: Next.js API routes
- DB: Supabase (Postgres + auth)
- LLM: GPT-4o-mini for voice profile + per-email gen (~$0.001/email)
- Payments: Stripe (subscription)
- Hosting: Vercel

## 14-day build plan

| Day | Task |
|---|---|
| 1 | Landing page (Vercel + Next.js), waitlist, copy from real Draftly positioning |
| 2 | Auth (Supabase email + Google), Stripe test mode |
| 3 | Voice profile: paste-text UI + GPT-4o-mini extraction + storage |
| 4 | Bulk gen: CSV upload + per-row GPT call + output table |
| 5 | Pricing page + Stripe live + trial gating |
| 6 | Polish UI, error handling, rate limits |
| 7 | **Soft launch** — post on X, IndieHackers, r/Entrepreneur |
| 8 | Iterate on user feedback, fix bugs |
| 9 | Add Gmail OAuth "copy to drafts" (P1) |
| 10 | Add 3 templates (cold / newsletter reply / investor update) |
| 11 | Add CSV export + bulk copy |
| 12 | Write SEO content: 5 blog posts (best AI email writer, etc.) |
| 13 | ProductHunt prep + assets |
| 14 | **Public launch** — ProductHunt, X thread, IH post, email list |

## 30-day marketing calendar (budget ≤ $300)

| Week | Activity | Cost |
|---|---|---|
| 1 | X thread "I built an AI that learns your email voice" (build in public) | $0 |
| 1 | IndieHackers "Made an AI email personalization tool — $0→first paying user" post | $0 |
| 1 | Cold DMs to 20 solopreneur influencers with free 3-month codes | $0 |
| 2 | 5 SEO blog posts targeting "AI email writer", "personalized cold email tool" | $0 (you write) |
| 2 | Guest post on 1 sales/marketing newsletter (free) | $0 |
| 2 | Reddit: r/sales, r/Entrepreneur, r/copywriting — value-first comments | $0 |
| 3 | ProductHunt launch (paid promo: $100 featured slot) | $100 |
| 3 | 2 micro-influencer sponsorships ($50 each, sales/AI niche, 5K-20K followers) | $100 |
| 4 | Retweet of best user testimonials, case study post | $0 |
| 4 | "Free voice profile" lead magnet landing page + email capture | $0 |
| 4 | Email 3-part nurture to leads | $0 |

**Total marketing: $200** (under $300 cap)

**KPI targets**
- Day 7: 50 signups, 5 paid
- Day 14: 200 signups, 30 paid
- Day 30: 500 signups, 100 paid @ $19/mo = $1,900 MRR
- Path to $10K: 525 paying users @ $19/mo (or fewer at $29 tier)

## Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Price | $19/mo (Pro) or $29/mo (Pro+) |
| Free trial | 14 days, 50 emails |
| Conversion (trial → paid) | 20% (industry avg for $19 SaaS) |
| LTV (12 mo avg retention) | ~$228-$348 |
| Churn | 5%/mo target |
| Gross margin | ~85% (LLM cost ~$0.50/user/mo at 50 emails) |
| CAC | ~$15-25 (mostly organic + $200 spend amortized) |
| LTV/CAC | ~12:1 |

**Path to $10K MRR**
- 525 users @ $19/mo OR 345 users @ $29/mo
- Assuming 20% trial conversion + 5%/mo churn → need ~3,000 trial signups in steady state
- Realistic at 100 signups/day from organic → ~6-9 months from MVP
- Faster path: add $29 tier, push LTV, or move upmarket ($99 for small teams)

## Kill criteria
- Day 14: <10 paid signups → pivot ICP or messaging
- Day 30: <30 paying users → kill or major pivot
- LTV/CAC < 3 by day 60 → stop paid acquisition, return to pure organic
- Voice profile accuracy <70% thumbs-up from users → rebuild extraction prompt

## Wedge
n/a (pure GO, competition ≤ 3)
