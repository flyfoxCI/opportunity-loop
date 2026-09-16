# Direction: publbee — Blog-to-Social Repurposing for Newsletter Publishers

**Tier:** GO
**Slug:** publbee
**TrustMRR evidence:** Publbee, $35 MRR, $32 last30, 102 subs, founder @nezirbasar1, https://www.publbee.com
**Demand / Competition (heuristic, not X-verified):** 4 / 2

## 1. Why this direction

**TrustMRR evidence:**
- $35 MRR on 102 subs = ~$4 ARPU = annual plan mix, real paying users
- Founder actively shipping (recent last30 $32 vs $35 MRR shows growth)
- Category "other" is broad but the URL publbee.com + founder name implies newsletter/marketing repurpose
- 102 subs is small but growing — pre-mainstream window

**X/web evidence (heuristic):**
- Founder @nezirbasar1 is a known builder in indie/solopreneur Twitter
- Newsletter space (beehiiv, Substack, Ghost) growing fast → tooling demand follows
- "Repurpose blog to social" is a top-5 ask in every newsletter operator survey

**Why GO not GO_NARROW:**
- Demand signal is broad (every newsletter publisher needs this)
- Competition is genuinely low for the specific "blog-post-in, multi-platform-drafts-out" combo
- Buffer / Hypefury / Repurpose.io exist but are either scheduling-only or platform-specific
- Wedge is the *input*: a full blog post → not just a tweet thread

## 2. Competitor table

| Tier | Competitor | What they do | Pricing | Why we don't collide |
|---|---|---|---|---|
| L1 direct | Repurpose.io | Long-form → short clips for video | $15-29/mo | Video-first, doesn't write text drafts |
| L1 direct | Hypefury | Twitter threads + scheduling | $9-29/mo | Twitter-only, requires you to write |
| L1 direct | Buffer | Cross-post scheduling | $6-120/mo | Scheduling only, no AI writing |
| L2 adjacent | Taplio | LinkedIn growth + AI posts | $40+/mo | LinkedIn-only, no blog input |
| L2 adjacent | Tweet Hunter | Tweet ideas + scheduling | $12-49/mo | Twitter-only |
| L2 adjacent | beehiiv AI | Newsletter subject + body AI | $1-99/mo | Tied to beehiiv hosting only |
| L3 distant | Jasper | General marketing AI | $49+/mo | General purpose, not repurposing |
| L3 distant | Zapier + ChatGPT DIY | Manual workflow | $20+/mo | Effort = friction |

**Competition score: 2.** No one owns "blog post in → 4 social drafts out with UTMs + canonical link."

## 3. PRD MVP

### User story
As a newsletter publisher, I want to paste a Substack/blog URL → get a LinkedIn post, X thread, Threads post, and Bluesky post — all with the canonical URL embedded — in 30 seconds.

### Epic E1: URL input + extraction (P0)
- Paste blog URL (Substack, Ghost, Medium, WordPress, custom)
- Fetch HTML, extract title, body, meta description
- Show extracted content for user to confirm/edit

### Epic E2: Platform drafts (P0)
- Generate 4 drafts: LinkedIn (1300 chars), X thread (5-8 tweets), Threads (500 chars), Bluesky (300 chars)
- Each draft includes: hook, summary, CTA, canonical URL with `?utm_source={platform}`
- Voice toggle: professional / casual / contrarian

### Epic E3: Editor + export (P0)
- Side-by-side editor for each draft
- Copy-to-clipboard for each platform
- "Open in [platform]" deep-link when possible

### Epic E4: History (P1)
- Last 20 repurposings saved per user
- Re-export or iterate on past drafts

### Epic E5: Scheduling (P2 — explicit non-goal for v1)
- Native scheduling = feature-creep, defer or integrate Buffer/Hypefury

### Non-goals (P2 / OUT)
- ❌ Image/video generation — defer
- ❌ Direct publishing — defer (legal + ToS risk)
- ❌ LinkedIn / X / Threads official APIs — too restricted; copy-paste is fine
- ❌ Multi-blog aggregation
- ❌ Team workspaces
- ❌ Analytics — defer to platform native

### Tech stack
- Frontend: Next.js + Tailwind, hosted on Vercel
- Backend: Supabase (auth, db) + Next.js API routes
- Scraping: Firecrawl ($0-50/mo based on volume) or simple cheerio for supported hosts
- AI: OpenAI gpt-4o-mini (well-suited for short copy)
- Payments: Stripe
- Email: Resend (transactional)
- Analytics: Plausible

### Data model
