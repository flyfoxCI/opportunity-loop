---
layout: post
title: "Direction: WhiteLabel — Vertical AI co-pilot, sold to agencies & course creators (GO)"
date: 2026-09-13T03:51:34+00:00
week: "2026-09-13_035134"
week_date: "2026-09-13T03:51:34+00:00"
slug: "whitelabel-vertical-saas"
permalink: /directions/whitelabel-vertical-saas.html
tags:
  - "AI"
  - "SaaS"
  - "B2B"
  - "B2C"
  - "creator"
  - "mobile"
excerpt: "A chat assistant trained on the agency's knowledge base (PDFs, Notion exports, website crawl). - A lead-capture widget for the agency's site (drops into Webflow, WordPress, Shopify, Framer). - A simple CRM that captures, tags, and emails leads back to the agency. - A billing + ad"
---

> Tagline: *One AI platform, a thousand niche brands.*

---

## 1. Why this direction

### TrustMRR evidence
- **Tradevipe** (per seed report) — MRR ~$2.9K, 14 customers → ~$207 ARPU. A vertical SaaS for trade businesses sold by an agency-style operator. Almost no direct competitors.
- **Orion AI Solutions Inc.** — $409 MRR, 267 subs, `demand=4, comp=2`. A "done-for-you AI delivery" shop on TrustMRR. Sits exactly in this unbundle: operators who *use* AI for clients are the natural channel.
- **AppAlchemy** — $62 MRR, `demand=3, comp=2`. Mobile-utility builder for SMBs. Confirms small businesses will pay for AI plumbing they can't build themselves.

### Why B2B whitelabel wins
1. **High ARPU, low churn.** $99–$499/mo with 12-month contracts is normal in this lane.
2. **Channel-free distribution.** The buyer is the agency; they already have the end-user relationship.
3. **Sales motion is one-to-many.** Land one agency, sign up their 10 clients via "powered by" branding.
4. **Real moat.** Once an agency re-platforms onto you, switching cost is painful (their data, their customer's habits, their billing).

### What we sell
A whitelabel AI platform that an agency / consultant / course creator can rebrand as their own and resell to their niche SMB clients. Concretely:

- **A chat assistant** trained on the agency's knowledge base (PDFs, Notion exports, website crawl).
- **A lead-capture widget** for the agency's site (drops into Webflow, WordPress, Shopify, Framer).
- **A simple CRM** that captures, tags, and emails leads back to the agency.
- **A billing + admin** dashboard so the agency can re-price, suspend, and onboard their own customers.
- **Multi-tenant from day 1.** Each agency is its own org; each end-client is a sub-tenant.

---

## 2. Competitor table

| Tier | Competitor | What they do | Price | Threat |
|---|---|---|---|---|
| L1 | Tradevipe (TrustMRR / tradevipe.md) | Vertical SaaS for trades, sold by agency | $200+/mo per client | Indirect. Validates the *demand*. |
| L1 | Botpress, Voiceflow (whitelabel tiers) | Chatbot platforms with agency programs | $400+/mo + per-seat | Real. But they sell *platform* not *vertical product*. We win on the niche vertical templates and the reseller dashboard. |
| L1 | CustomGPT.ai, ChatBase | "ChatGPT trained on your docs" tools | $49–$499/mo | Adjacent. They sell knowledge-base bots. We sell the whole reseller stack. |
| L2 | HighLevel (white-label SaaS for agencies) | Full marketing platform | $97–$497/mo | Real incumbent, but generic. We win on vertical templates. |
| L2 | Whitelabel Suite, Vendasta | Whitelabel marketplaces for agencies | $250+/mo | Real. But they're marketplaces; we are a focused vertical toolkit. |
| L3 | Custom dev shops (every agency has one) | Bespoke builds | $10K+ | Slow and expensive. We are the cheap, fast version. |
| L3 | Bento.io, Stacked, individual agency-built tools | One-off | n/a | We commoditize. |

**Competition score: 2.** Many named competitors, none in the exact slot of "agency-resold vertical AI assistant with reseller billing". HighLevel is the closest but is a generic platform, not a focused product.

---

## 3. PRD MVP

### User story
> *I'm the founder of a 6-person marketing agency that serves 30 dental practices. Each client wants an "AI receptionist" on their site that answers FAQs and books appointments. I can't build 30 separate bots. I want a single dashboard where I can drop in a client, upload their PDFs, brand the chat widget, set the price I charge them ($200/mo), and have Stripe send me the money.*

### Epics
- **E1 — Agency onboarding.** Sign up → Stripe Connect onboarding → create org.
- **E2 — Tenant creation.** Each tenant = 1 client. Upload docs, configure persona, set branding.
- **E3 — Knowledge ingestion.** Crawl tenant's site + ingest PDFs/Notion. Vector store per tenant.
- **E4 — Chat widget.** Embeddable JS, brand-themed, captures emails.
- **E5 — Lead pipeline.** Email notifications + simple CSV export. No full CRM in MVP.
- **E6 — Billing.** Stripe Connect (agency gets paid directly; we take 20% platform fee).
- **E7 — Admin.** Agency dashboard: tenants, MRR, churn, usage.

### P0 (days 1–10)
- Auth + multi-tenant data model.
- Stripe Connect Express onboarding.
- Doc upload + simple retrieval (no fancy vector DB; start with chunked keyword search).
- Embeddable chat widget (1 file: `amen-chat.js`).
- Agency dashboard (tenants list, per-tenant MRR).
- One pricing page, one demo video.

### P1 (days 11–14)
- Per-tenant custom domain support (`chat.client.com` via Cloudflare for SaaS).
- Email lead notifications.
- Usage-based billing guard (so a tenant can't run up $5K of OpenAI in a night).
- Plausible + Sentry.

### P2 (post-MVP, days 15–30)
- Site crawler with respect for robots.txt.
- Appointment booking (Cal.com embed).
- "Agency in a box" template packs (dental, legal, real estate).
- Marketplace listing on HighLevel's app directory.

### Non-goals
- Voice / phone. (Twilio integration is doable but high support cost.)
- Custom model fine-tuning. (Retrieval only in MVP.)
- Mobile app.
- Agency-to-agency resale.
- White-glove onboarding service. (Self-serve only.)

### Pricing
- **Starter ($99/mo):** Up to 5 tenants, 1,000 chats/mo.
- **Growth ($299/mo):** Up to 25 tenants, 10,000 chats/mo, custom domain.
- **Scale ($699/mo):** Unlimited tenants, 50,000 chats/mo, priority support.
- **Platform fee:** 20% of agency revenue billed to end-clients (passes through Stripe Connect).

---

## 4. 14-day day-by-day build plan

| Day | Output |
|---|---|
| 1 | Domain + landing page. Pre-sell 5 agency pilots at $99/mo with 30-day refund. |
| 2 | Auth + Stripe Connect onboarding flow (Express). |
| 3 | Multi-tenant Postgres schema. RLS policies. |
| 4 | Tenant creation flow. Doc upload to S3. |
| 5 | Retrieval: chunk docs, keyword search index per tenant. (Skip vector DB until week 2.) |
| 6 | Chat API: OpenAI call with tenant context. |
| 7 | Embeddable widget: `<script src="amen-chat.js" data-tenant="...">` |
| 8 | Per-tenant branding (logo upload, primary color). |
| 9 | Agency dashboard: tenants, MRR, chats-this-month. |
| 10 | Usage metering + soft cap at plan limit. |
| 11 | Custom domain via Cloudflare for SaaS. |
| 12 | Email lead notifications (Resend). |
| 13 | Demo video (Loom, 8 min). Test with 3 friendly agencies. |
| 14 | Public launch: IndieHackers, agency Facebook groups, cold email blast. |

**Stack:** Next.js + Postgres (Supabase) + Stripe Connect + OpenAI + Cloudflare + S3 (Backblaze B2 to start).

**Infra cost at MVP:** ~$80/mo.

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget allocation**
- $120 — Apollo.io / Instantly credits for cold email (8,000 sends)
- $80 — Sponsorships of 3 agency newsletters (each ~$25 CPM)
- $50 — One Loom ad in the HighLevel app directory (sponsored slot)
- $30 — Canva Pro for one month (sales collateral)
- $20 — LinkedIn Premium trial for prospecting

**Daily calendar (organic + cold outbound is the spine)**

| Wk | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| 1 | Cold-email 100 agencies (Apollo) | IndieHackers post: "I built AI plumbing for agencies" | Cold-email 100 more | X thread: 7 lessons from agency owners | LinkedIn post | Cold-email 100 more | Rest |
| 2 | Cold-email 100 agencies | Podcast guest: "AI for agencies" (any niche podcast) | Cold-email 100 more | Reddit: r/agency, r/marketing (genuine value) | Cold-email 100 more | First agency sponsor ($30) | Apply to HighLevel marketplace |
| 3 | Cold-email 100 agencies | Case-study writeup from pilot agency #1 | Cold-email 100 more | X thread: pricing math | Cold-email 100 more | Second sponsor ($30) | Loom ad live ($50) |
| 4 | Cold-email 100 agencies | Case-study writeup from pilot #2 | Cold-email 100 more | Email blast to list | Cold-email 100 more | Third sponsor ($25) | Wrap-up |

**Targets (week 4):**
- 500 cold emails sent, 5% reply rate → 25 replies
- 8% reply → meeting rate → 2 meetings
- 50% close rate on meetings → 1 new agency
- 1 new agency @ $99/mo = $99 MRR + the seed pilots = ~$700 MRR by day 30
- Realistic month-1 MRR: $400–$700.

**Why cold email is OK here:** agencies *expect* to be pitched tools. They are buyers, not consumers. This is the exception to "organic-only" because the unit economics force it; we still cap paid spend at $300 and the channel is direct-response.

---

## 6. Unit economics to $10K MRR

| Metric | Value | Source |
|---|---|---|
| ARPU (blended Growth + Scale) | $380/mo | 60% Growth, 35% Scale, 5% Starter |
| Gross margin | 78% | OpenAI + Stripe + infra per agency |
| Monthly churn | 3% | B2B SaaS median for agency-channel products |
| Net new customers/mo (steady state) | 12 | 1 every 2.5 days from cold email + referrals |
| Months to $10K MRR | ~3 | (10,000 / 380) × 1 / (12 × 0.97) ≈ 2.7 months |

**Sensitivity:**
- If cold email reply rate falls to 2% → ~5 months.
- If churn rises to 6% → ~5 months.
- If ARPU drops to $200 (more Starter, less Scale) → ~6 months.

**Worst case (churn 6%, ARPU $200, 6 new/mo):** ~10 months to $10K. Still inside year window.

---

## 7. Kill criteria

- **Day 14:** If landing conversion (visitor → demo booked) <1.5%, kill. The pitch isn't landing.
- **Day 30:** If pilot conversion (demo → paid) <10%, kill. The product isn't worth it to agencies.
- **Day 60:** If MRR < $1,000, kill. The cold-email engine isn't producing.
- **Day 90:** If monthly churn >8%, kill. The product isn't sticky enough.
- **Hard kill:** HighLevel launches a similar template-pack product and agencies churn out within 30 days.

---

## 8. Founder fit notes

- **Best for:** founder who enjoys cold outbound and understands agency economics (rev share, churn by tenant). A former agency operator is ideal.
- **Bad fit if:** you can't send 50 cold emails a day for 30 days without burning out. Sales is the bottleneck.
- **Extension path after $10K MRR:** sell the platform itself as an acquisition target to HighLevel or Vendasta. Or build vertical SaaS products on top of the platform and sell direct.
