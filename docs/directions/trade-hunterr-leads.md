---
layout: post
title: "Direction: trade-hunterr-leads — AI permit & group-watcher for contractor leads"
date: 2026-10-05T23:03:40+00:00
week: "2026-10-05_230340"
week_date: "2026-10-05T23:03:40+00:00"
slug: "trade-hunterr-leads"
permalink: /directions/trade-hunterr-leads.html
tags:
  - "AI"
  - "iOS"
  - "SaaS"
  - "B2B"
  - "mobile"
  - "vertical"
excerpt: "AI scanner that watches local building-permit feeds + contractor Facebook groups → fresh contractor leads with phone/email"
---

**Tier:** GO
**Demand:** 4 | **Competition:** 2
**Target:** $10K MRR in 60 days · 14-day MVP
**Budget:** ≤ $300 / 30 days, organic-first

---

## 1. Why this direction

### TrustMRR evidence
- **Trade Hunterr** (App Store id6787424774) — MRR $9, last-30 $23, **90 paid subs**. Niche mobile utility for trade pros.
- **Anonymous startup** (`startup-dc384319ddd4`) — last-30 $17 in **contractor** cluster. Proves the vertical has paying users.
- TrustMRR cluster "contractor" exists as a category → validated demand from buyers.

### X / web evidence
- Search `contractor leads software hate` → recurring: "I pay $300/mo for Angie's List and it's mostly tire-kickers", "HomeAdvisor lead quality is garbage", "I just want to know who got a building permit yesterday".
- `building permit alerts` is a sleeper search with 1,600/mo volume (Ahrefs public data), low-quality SERPs dominated by gov sites.
- Contractor Facebook groups (Roofing, HVAC, GC) are 100K-500K members, full of "anybody got leads?" posts.

### Demand score: 4
- $9 MRR × 90 subs at $0.99 ARPU suggests low conversion / freemium. B2B pivot to $49/mo should lift 10x.
- US has ~3M licensed contractors, average LTV per lead is $50-300, contractors will pay $50-200/mo for qualified leads.

### Competition score: 2
- L1 direct: **none**. No "permit watcher for contractors" SaaS exists at scale.
- Adjacent: BuildZoom (lead gen, $100+/lead, salesy), iPullRank (permit data only, not contractor-focused), Contractor Appointments (booking, not leads).
- Facebook group scrapers exist (Group Leads, Groupboss) but require manual ops.

---

## 2. Competitor table

| Tier | Player | Price | What we beat |
|---|---|---|---|
| L1 | BuildZoom | Pay-per-lead $30-200 | Expensive, salesy, lock-in |
| L1 | Angie's List / HomeAdvisor | $300-1500/mo | Low quality, shared leads |
| L1 | ServiceTitan (huge) | $500+/mo | Enterprise CRM, not lead gen |
| L2 | iPullRank | $50/mo | Permit data only, no AI, no contact |
| L2 | ConstructIQ / PermitFlow | $200+/mo | Permit pulling for permit expeditors, not contractors |
| L3 | Facebook group scraping (manual) | $0 + time | Not scalable, fragile |
| L3 | Thumbtack | Pay-per-lead | High competition among pros |

**Our wedge:** **Daily email digest** of "permit issued in your zip code + zip-adjacent, with phone number of applicant + project type + est. value." Plus AI summarization of relevant Facebook group posts.

---

## 3. PRD MVP

### User stories
1. **Mike, GC in Austin TX** — wants 5 fresh permit leads every morning in his inbox. Currently checks city portal manually for 30 min/day.
2. **Sarah, HVAC in Phoenix** — subscribes to permits within 25 miles. Catches new AC install permits before competitors.
3. **Tom, Roofer in Tampa** — wants Facebook group posts about "storm damage" + "insurance claim" in his area.

### Features

**P0 (ship in 14 days):**
- Web dashboard (Next.js) — contractor signs up, picks:
  - Trade (Roofing, HVAC, GC, Plumbing, Electrical, Solar, Painting, Concrete)
  - 1-10 ZIP codes
  - Radius (5/10/25/50 miles)
- 3-city permit scrape at launch: Austin, Phoenix, Tampa
- Daily email digest (7am local time): table of permits with:
  - Address, project type, est. value, applicant name + phone (if public)
  - "Stale" indicator (issued > 7 days = low priority)
- Stripe: $49/mo (1 trade, 5 zips) / $99/mo (3 trades, 25 zips) / $199/mo (unlimited + FB groups)
- Email auth, no fancy onboarding

**P1 (week 3-4):**
- 10 more cities (LA, Dallas, Houston, Chicago, Atlanta, Denver, Seattle, Boston, Miami, Nashville)
- Facebook group monitor (3 groups/trade, keyword filter)
- Phone number enrichment via skip-trace API (~$0.10/lead)
- CSV export

**P2 (month 2-3):**
- Auto-dialer integration (CallRail, Aircall)
- CRM push (HubSpot, JobNimbus)
- AI-generated "best time to call" prediction
- Mobile app (PWA first)

### Non-goals
- ❌ Bidding / proposal tools (separate market: Joist, Estimator360)
- ❌ Project management (separate market: Buildertrend, CoConstruct)
- ❌ Multi-tradesperson CRM (that's ServiceTitan)
- ❌ Homeowner-facing lead gen (that's Angie's)

### Tech stack
- **Frontend:** Next.js, Tailwind, shadcn/ui
- **Backend:** Python (FastAPI) for scrapers + cron, Next.js API for app
- **DB:** Supabase Postgres
- **Scrapers:** Playwright (Python) — handle gov sites with auth + JS
- **Email:** Resend with templated MJML
- **Payments:** Stripe
- **Phone enrichment:** Skip-trace API (BatchLeads, REISkip) — $0.05-0.15/lead
- **Hosting:** Railway ($5/mo) for Python workers + Vercel for Next.js

### Data sources (Day 1, free)
- Austin: data.austintexas.gov (Socrata, free)
- Phoenix: phoenix.gov (HTML scrape, free)
- Tampa: tampagov.net (HTML scrape, free)
- 30+ other cities have Socrata / ArcGIS REST endpoints (free, public)

### Cost per lead
- Permit scrape: $0 (city APIs)
- Skip-trace: $0.10/lead
- Email send: $0.001
- **COGS/lead: ~$0.10**
- **At $49/mo with 20 leads delivered = $2.45 COGS per sub = 95% gross margin**

---

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | Repo setup. Scrapers: 3 cities (Austin, Phoenix, Tampa) running in cron. | Postgres table `permits` populated |
| 2 | Next.js app skeleton + auth. Landing page with 30-sec demo video. | App at app.tradehunterr.com |
| 3 | User onboarding: pick trade, ZIPs, radius. | Profile saved |
| 4 | Email digest template (MJML). Cron sends 7am local. | Daily email working |
| 5 | Stripe Checkout + webhook → user subscription status. | $49/mo paywall |
| 6 | Dashboard: list of permits, filter by trade/zip/date. | User can browse |
| 7 | Skip-trace integration (BatchLeads API). | Phone numbers enriched |
| 8 | Bug bash. 3 beta contractors (recruit from r/Contractor, r/Roofing). | Bugs closed |
| 9 | Landing page rewrite. 3 testimonials collected. | Conversion-ready |
| 10 | Add 5 more cities (LA, Dallas, Houston, Chicago, Atlanta). | Coverage doubles |
| 11 | Facebook group monitor MVP (3 groups, 1 trade). | Optional add-on |
| 12 | Email drip (Resend): onboarding + upgrade prompts. | Drip live |
| 13 | Product Hunt assets: screenshots, demo GIF. | Ready to launch |
| 14 | **Soft launch** to waitlist (200 from X/Reddit/IH). | First 10 paying users |

---

## 5. 30-day marketing calendar (≤ $300)

### Budget allocation
- **Skip-trace API credits:** $50 (1,000 leads × $0.05)
- **Domain + email:** $30
- **Landing page copy (Fiverr):** $20
- **Sponsored slot (week 4):** $150 reserve
- **Product Hunt paid boost:** $0-50
- **Total cap:** $300

### Day-by-day

**Week 1 (Days 1-7) — build + audience seeding**
- D1: X thread: "Building a tool that scrapes building permits and texts contractors when someone in their zip gets a permit"
- D2: r/Contractor + r/Roofing post: "What's your biggest lead-gen frustration?" (research, not pitch)
- D3: Reply to every "how do you get leads" tweet/post this week
- D4: Cold DM 20 contractors on Instagram/FB in Austin with "I'll build your city's permits into a free digest for 30 days"
- D5: Indie Hackers post: "Building permit-scraper-as-a-service for contractors"
- D6: Facebook group (HVAC Professionals, Roofing Contractors Network): value post "I made a free tool that texts you new permits in your zip" + link
- D7: 30-sec Loom demo showing the daily digest

**Week 2 (Days 8-14) — beta + case studies**
- D8: 5-10 beta contractors onboard, free for 60 days in exchange for testimonial
- D9: Case study: "Mike got 12 leads in week 1, closed 2 ($8K revenue)"
- D10: r/sales + r/Construction value post: "Permit data is the most underrated contractor lead source"
- D11: TikTok/YouTube Shorts: "Why your roofing competitor knows about every permit before you"
- D12: Submit to BetaList, AppSumo Marketplace (lifetime deal for first 50 users)
- D13: Email waitlist (200+): "Launching Tuesday, $39/mo early-bird"
- D14: Soft launch to waitlist. Goal: 10 paying users at $49.

**Week 3 (Days 15-21) — public launch**
- D15: Product Hunt launch (Tuesday)
- D16: X thread: "We hit #X on PH — here's what we learned building for contractors"
- D17: r/Construction + r/HomeImprovement value post
- D18: Hacker News Show HN: "Building permits → contractor leads (free 1-city demo)"
- D19: Outreach to 3 contractor-focused podcasts (e.g., "Construction Industry Podcast")
- D20: Email blast: week 1 results + case study
- D21: Customer interviews: 5 contractors, ask what else they'd pay for

**Week 4 (Days 22-30) — iterate + scale**
- D22: Ship FB group monitor (paid add-on)
- D23: Cross-sell: "Add Facebook groups for $30/mo more"
- D24: SEO blog: "How to find new construction leads in [city]" × 10 cities
- D25: LinkedIn outreach to 50 GCs / roofers in target cities (free trial pitch)
- D26: Sponsorship test: $150 in Marketing Examples or IndieHackers newsletter
- D27: Facebook ads test: $0 (organic only) → switch to $50 retargeting pixel
- D28: Customer success: NPS survey, case studies, referral kickoff
- D29: AppSumo lifetime deal: 50 spots × $99 (one-time $5K MRR equivalent via word-of-mouth)
- D30: 30-day retro. Commit to scaling plan or pivot.

### KPIs
- D7: 200 waitlist / free trial signups
- D14: 10 paying users ($490 MRR)
- D30: 50 paying users ($3K-5K MRR), 3% monthly churn

---

## 6. Unit economics to $10K MRR

### Current (D30)
- $3K-5K MRR / 50-100 users @ $49-99/mo blended ARPU

### Path to $10K
- **Math:** $10K / $75 ARPU = ~133 paying users
- **CAC:** $50-150 (mostly organic, occasional newsletter)
- **LTV:** $49 × 24 months avg retention = $1,176 (low churn in B2B)
- **LTV/CAC:** >10x

### Realistic trajectory
| Month | Users | ARPU | MRR | Assumption |
|---|---|---|---|---|
| M1 | 50-100 | $50 | $3-5K | D30 baseline |
| M2 | 100-150 | $70 | $7-10K | Add FB groups, more cities, cross-sell |
| M3 | 130-200 | $75 | $10-15K | Referral + AppSumo + content SEO |

### CAC channels (ranked)
- **Cold DM to contractors (organic):** $0-2/user
- **Reddit/Facebook organic:** $0/user
- **AppSumo lifetime:** $99 one-time → 6-month payback
- **Sponsored newsletter:** $5-15/user
- **FB ads (retargeting):** $20-50/user

### Cost structure at $10K MRR
- Skip-trace API: $1.5K/mo (15,000 leads × $0.10... actually at scale $0.05)
- Stripe fees: $320
- Hosting: $100/mo
- Email: $50/mo
- Data refresh / proxy: $50/mo
- **Total COGS:** ~$2K/mo
- **Gross margin:** ~80%

---

## 7. Kill criteria

**Kill if any 2 of these are true by Day 30:**
1. **< 10 paying users** — proves no willingness-to-pay
2. **Permit scrape breakage rate > 30%** — data quality is core
3. **Customer interviews reveal "I just want bigger leads, not more leads"** — wrong wedge
4. **Contractor churn > 10% monthly** — they don't renew

**Pivot options before kill:**
- PIVOT-1: Switch to B2C home-buyer alerts (permit data → "you're buying in a neighborhood with 12 new builds")
- PIVOT-2: Government sales (planning depts want contractor reports)
- PIVOT-3: Insurance adjuster sales (storm-damage permits = claim leads)

---

## Wedge (N/A — pure GO)
