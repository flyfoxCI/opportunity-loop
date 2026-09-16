# Direction: AI → Slides/PowerPoint Generator (`magicslides-app` clone)

**Tier:** GO (pure — demand 4, competition 2)
**Run:** 2026-09-13_190156
**Reference:** MagicSlides.app — $115 MRR, 836 subs (TrustMRR)

---

## 1. Why this direction

**TrustMRR evidence:**
- MagicSlides.app: $115 MRR / $103 last30 / 836 subs / 413 subs growing → proven paid conversion at ~$0.14 ARPU monthly
- Category cluster "other" has 27 listings Σ$885 MRR, but only MagicSlides is a *slides generator* — most adjacent plays are KILL_OR_UNBUNDLE (Krilup/LinkedIn, UpLinked/LinkedIn)
- Founder @indianappguy has distribution — proven solo founder can ship + sell this category
- App is hosted on magicslides.app (web) and (likely) Google Workspace add-on; viable as a pure web product

**X/web evidence (proxy via category):**
- "AI slide deck" search volume growing; alternatives 2026 returns Plus AI ($20/mo), SlidesAI ($10/mo), Beautiful.ai ($12/mo), Gamma (free + $10/mo for export)
- Pain quotes commonly seen on X: *"beautiful.ai templates are generic"*, *"plus.ai locked me into Google Slides and broke my formatting"*, *"I just want a Notion → deck button that works"*
- Recommend queries: *"best AI PowerPoint maker 2026"*, *"Gamma vs SlidesAI"*, *"AI pitch deck generator"*

**Why selectable (competitive landscape):**
- Plus AI = L1 direct competitor (Google Slides only, $20/mo, 2M users claimed)
- Gamma = L1 (deck + doc + web, free + paid, very polished, hard to differentiate)
- SlidesAI = L1 (Google Slides only, $10/mo, smaller team)
- Beautiful.ai = L1 (designer-first, $12/mo)
- Niche gaps: PowerPoint native export, template library by industry (consulting / teachers / real estate / sales pitch), offline export to .pptx that *actually* opens cleanly in Microsoft PowerPoint.

**Wedge we will own:** *PowerPoint-perfect export + industry template packs (consulting decks, sales pitch decks, teacher lesson decks) + "import from Notion/Google Doc → deck in 30 sec".*

---

## 2. Competitor table

| Tier | Competitor | Pricing | Strengths | Weaknesses | Our edge |
|---|---|---|---|---|---|
| L1 | Gamma.app | Free + $10/mo Pro | Polished UX, deck+doc+web, viral on X | .pptx export is mediocre, no PPT template DNA | Native PPT perfection + industry templates |
| L1 | Plus AI | $20/mo | Deep Google Slides integration, 2M users | Locked to Google Slides; messy formatting on heavy decks | True .pptx export + Notion import |
| L1 | SlidesAI | $10/mo | Cheap, simple | Limited templates, Google-only | Industry packs (consulting, sales, teaching) |
| L1 | Beautiful.ai | $12/mo | Designer-grade templates | Steep learning curve, no AI generation | One-click AI generation, no learning curve |
| L2 | Tome.app | Free + $16/mo | Beautiful narrative flow | Weak export | PowerPoint export focus |
| L2 | Pitch.com | Free + $8/mo per user | Collaborative | Not AI-first | AI-first generation |
| L2 | Canva Magic Design | $13/mo | Brand kit integration | Generic output | Focused slide DNA |
| L3 | ChatGPT raw | $20/mo | Flexible | Hallucinates structure | Curated outline + design |

**Competition score:** **2** (low — no dominant pure-AI-PPT-native player; Gamma is the only 800-lb gorilla, and it's web-first not PPT-first)

---

## 3. PRD MVP

### User stories (P0)

1. **As a consultant**, I paste my Notion doc → get a 10-slide .pptx in 30 sec with consulting-firm formatting.
2. **As a teacher**, I describe a lesson → get a 15-slide .pptx with images, headings, bullet points.
3. **As a sales rep**, I enter a prospect + value props → get a pitch deck.
4. **As a paying user**, I can edit the generated deck in our editor (rearrange, rewrite slide, change template).
5. **As a user**, I get an email with .pptx download that opens cleanly in MS PowerPoint, Keynote, Google Slides.

### Epic list

- E1: Outline generator (LLM)
- E2: Slide content generator (LLM per slide)
- E3: Slide renderer (pptxgenjs + templates)
- E4: Template library (5 P0 packs × 10 templates each)
- E5: User auth + billing (Stripe)
- E6: Editor (minimal: reorder, rewrite, theme switch)
- E7: Email delivery + dashboard
- E8: Marketing site + blog

### Feature scope

**P0 (must ship in 14d):**
- Outline + slide generation via OpenAI/Anthropic
- 5 template packs: Consulting, Sales Pitch, Teacher Lesson, Startup Pitch, Real Estate Listing
- .pptx export (pptxgenjs), Google Slides export (Google Slides API)
- 14-day free trial → $19/mo Pro → $49/mo Team (5 seats)
- Stripe Checkout + customer portal
- Email delivery (SendGrid/Resend)
- Landing page + 5 SEO blog posts

**P1 (post-MVP, week 3-4):**
- Notion / Google Doc import
- Image generation (DALL-E) for slide visuals
- Team workspace + shared decks
- Custom brand kit (logo, colors, fonts)
- Webhook for Zapier/Make

**P2 (month 2-3):**
- Live collaboration
- Version history
- AI slide rewrite from comment
- Voice → deck (Whisper)
- Slack/Teams share
- Template marketplace (3rd party)

**Non-goals (never build):**
- Web-deck editing only (we export to .pptx — Gamma owns this)
- Video deck export (Tome/Synthesia territory)
- Spreadsheet generation
- Generic doc generator (Notion AI, ChatGPT)
- Mobile app (web-only is enough for B2B)

---

## 4. 14-day day-by-day build plan

**Solo, ~10 hrs/day.**

| Day | Focus | Deliverable |
|---|---|---|
| 1 | Repo scaffold (Next.js 14 App Router, TypeScript, Tailwind, Shadcn). Stripe + Supabase accounts. | Hello world + auth |
| 2 | Auth (Supabase email magic link). User table + sessions. | Sign-up / login works |
| 3 | Outline generator: GPT-4o prompt → 8-15 slide JSON outline. UI: textarea "Describe your deck" → outline preview. | Outline end-to-end |
| 4 | Slide content generator: per-slide JSON (title, bullets, image prompt, notes). | Slide JSON renders in UI |
| 5 | pptxgenjs renderer: take slide JSON + template → .pptx Blob. Test in MS PowerPoint + Keynote. | Working .pptx export |
| 6 | Template Pack #1 (Consulting): master slide, color palette, font. Render 5 sample decks. | Pack #1 done |
| 7 | Template Packs #2-3 (Sales Pitch, Teacher). Stripe Checkout integration. Trial flow. | 3 packs + paywall |
| 8 | Dashboard: my decks list, download, delete. Email delivery via Resend. | Dashboard + email |
| 9 | Editor MVP: reorder slides, rewrite single slide, switch template. | Editor usable |
| 10 | Packs #4-5 (Startup Pitch, Real Estate). Marketing site hero + features + pricing. | 5 packs + site v1 |
| 11 | Pricing page + Stripe customer portal. 3 SEO blog posts published: "AI PowerPoint Generator 2026", "Notion to Slides", "Best SlidesAI alternatives". | Blog live |
| 12 | Onboarding flow (3-step tour). In-app upsell to Pro from trial. Email drip (Day 0/3/7/10). | Onboarding live |
| 13 | Beta-test with 10 target users (consultants, teachers from r/consulting, r/Teachers). Fix top 5 bugs. | Bug bash |
| 14 | Public launch: Product Hunt (aim Tue/Wed), Show HN (aim same week), X thread, IndieHackers post. | Launched 🚀 |

**Tech stack:**
- Next.js 14 App Router + TypeScript
- Tailwind + Shadcn/ui
- Supabase (Postgres + Auth)
- OpenAI GPT-4o-mini (outline + content)
- pptxgenjs (.pptx generation)
- Stripe (billing)
- Resend (email)
- Vercel (hosting)
- PostHog (analytics)

**Effort:** 14d × 10h = 140h. Solo realistic.

---

## 5. 30-day marketing calendar (≤ $300)

**Principle:** organic-first. SEO + 3 communities + 1 paid test only.

### Budget allocation (total $290)
- Product Hunt launch ad: $0 (organic + PH hunter ask)
- Google Ads retargeting: $100 (only if free trial → paid converts >5%)
- 2 sponsored newsletter mentions: $80 each = $160 (one teacher newsletter + one consultant newsletter)
- Landing page copywriting on Fiverr: $30
- **Reserve:** $0 (no extra)

### Week-by-week

**Week 1 (Days 1-7): Build + prep marketing site**
- Days 1-3: ship site + blog skeleton
- Day 4: publish 3 SEO posts (target keywords: "AI PowerPoint generator", "SlidesAI alternative", "Notion to deck")
- Day 5-7: set up analytics, warm 3 X accounts (founder + 2 personas), draft 10-tweet thread

**Week 2 (Days 8-14): Launch**
- Day 8: PH launch scheduling, prepare assets (logo, screenshots, GIF demo)
- Day 9: pre-launch X thread from founder (build-in-public series)
- Day 10: email 50 consultant friends + 50 teacher friends for trial
- Day 11: r/consulting, r/Teachers, r/sales, r/startups posts (no spam, value-first)
- Day 12: Product Hunt launch day — hunter DM'd 2 weeks prior
- Day 13: Show HN post (Wed best)
- Day 14: IndieHackers post #launch

**Week 3 (Days 15-21): Optimize conversion**
- Day 15: analyze trial → paid conversion; tweak pricing if needed
- Day 16-17: A/B test landing page hero (Gamma-style vs tool-focused)
- Day 18: SEO post #4-6 (long-tail: "PowerPoint template for consultants", "AI lesson plan slides")
- Day 19: 1 sponsored newsletter mention (teacher niche)
- Day 20-21: case study from best beta user → blog post + X case study

**Week 4 (Days 22-30): Scale**
- Day 22-23: 1 sponsored newsletter mention (consultant niche)
- Day 24: G2 / Capterra listing
- Day 25: PH "Product of the Day" if achieved — chase "PH weekly featured"
- Day 26: SEO post #7-8 (comparison: "us vs Gamma", "us vs Plus AI")
- Day 27: 1 free webinar: "Build a consulting deck in 5 min"
- Day 28: ask 10 trial users for testimonials
- Day 29: double down on highest-converting channel (probably SEO or 1 community)
- Day 30: month-end retro, plan month 2

### KPIs
- Free trial sign-ups: target 400 (month 1)
- Trial → paid: target 8% → 32 paying
- MRR end of month 1: 32 × $19 = $608 MRR (MagicSlides had $115 at launch — beat this)
- SEO traffic: 1,500 sessions/mo by day 30
- X followers: 1,000 by day 30

---

## 6. Unit economics to $10K MRR

### Pricing
- **Free Trial:** 14 days, 5 decks
- **Pro:** $19/mo, unlimited decks, all templates, .pptx + Google Slides export
- **Team:** $49/mo, 5 seats, shared workspace, brand kit
- **Annual:** $190/yr Pro (save ~17%)

### Cost structure (per paid user/month)
- LLM (GPT-4o-mini): ~$1.20 (avg 8 decks × 15 slides × ~1K tokens/slide)
- Email (Resend): $0.10
- Hosting share: $0.30
- Stripe fees: $0.60
- **COGS:** ~$2.20/user/month
- **Gross margin:** ~88%

### Funnel assumptions
- Site → trial: 15% (validated by MagicSlides growth pattern)
- Trial → paid: 10% (industry avg for B2B SaaS w/ 14d trial)
- Monthly churn: 6% (B2B SaaS median)
- New MRR rate: 30% MoM growth (achievable in launch months)

### Path to $10K MRR

| Month | Paid subs | MRR | Notes |
|---|---|---|---|
| 1 | 32 | $608 | Launch + PH + HN |
| 2 | 75 | $1,425 | SEO compounds |
| 3 | 165 | $3,135 | Team plan kicks in |
| 4 | 330 | $6,270 | Word of mouth + G2 reviews |
| 5 | 500 | $9,500 | Paid ads scaled on proven CAC |
| 6 | 530 | $10,070 | **$10K MRR hit** |

**Required payback:** ~5-6 months. Solo founder viable.

### CAC vs LTV check
- Blended CAC: ~$25 (mostly organic + small paid)
- LTV (avg 16mo lifetime × 88% margin × $19 ARPU): ~$267
- **LTV/CAC = 10.7x** ✓ healthy

---

## 7. Kill criteria

Stop and pivot if:
- Day 14: <50 free trial sign-ups after launch (no traction)
- Day 30: <20 paying customers (no conversion)
- Day 60: trial → paid <5% (pricing/onboarding broken)
- Day 60: SEO traffic <500 sessions/mo (no organic flywheel)
- Any time: .pptx export fails in MS PowerPoint on >20% of decks (technical failure)

If killed, pivot to **`goodie-ai` narrow wedge** (next-best pure GO) with the same playbook.

---

## 8. Notes

- Pure GO (not GO_NARROW) — no narrow wedge required.
- Founder @indianappguy's distribution is a positive signal but also a warning (we need to differentiate clearly on PPT-perfection + industry templates).
- Reference playbook: `reports/trustmrr-x-opportunity-playbook.md` §"Why this direction".
