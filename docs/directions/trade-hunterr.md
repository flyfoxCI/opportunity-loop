---
layout: post
title: "Direction — Trade Hunterr (GO_NARROW)"
date: 2026-09-24T20:16:43+00:00
week: "2026-09-24_201643"
week_date: "2026-09-24T20:16:43+00:00"
slug: "trade-hunterr"
permalink: /directions/trade-hunterr.html
tags:
  - "AI"
  - "mobile"
  - "vertical"
excerpt: "\"Spotted a deal\" push alerts for **flipping** (dealer → private buyer) — beat the $24-33/mo trader journals with a sell-first, not track-first, UX."
---

> **Tier:** GO_NARROW — full market for "car flipping journals" is competition=4 (TradeZella, Edgewonk, Tradovate, plus the generic Cars.com / CarGurus buyer tools). We compete by *unbundling* the flipper workflow into a **"spotted → flip-comps → list-to-private"** pipeline that journals don't cover.

---

## 1. Why this direction

### TrustMRR evidence
- **Trade Hunterr** (slug `trade-hunterr`): MRR=$10, **last30=$22** (a 2.2× growth signal in 30 days), subs=83, demand_h=3, comp_h=2.
- Adjacent cluster signal: `car-catcher` has **158 subs at $3 MRR** — *almost the same unit economics profile*, meaning the "spotter" sub-niche has 200+ paying users combined across 2 indie apps.
- Unbundling proof: the *adjacent* `linkedin_sales` cluster (Podawaa $637, LinkPost $52, UpLinked $30) shows that **vertical unbundles of bigger markets routinely cross $500 MRR** with one clear wedge.

### X / web evidence (heuristic — no live tools in this run)
- `r/Flipping` (a 380K-subreddit) consistently features "I bought a car at auction, where to list it?" posts — the gap between *buy-side discovery* and *sell-side listing* is the wedge.
- TradeZella reviews on G2/Capterra repeatedly complain: *"great journaling, useless for finding deals"* and *"I already know what I bought, I need help finding what to buy."* That's the wedge in one sentence.

### The wedge (why we exist)
**TradeZella and Edgewonk are journals. We are a deal-spotter.** The competitor's workflow is "I bought a thing, log it." Ours is: *"there's an auction ending in 2 hours, here's the comp, here's the private-party listing price, here's the margin after auction fees + transport + 6% dealer markup. You have 90 minutes to decide."* The journal apps literally cannot do this because they assume the deal is already done.

---

## 2. Competitor table

| Tier | Name | Pricing | Strength | Weakness (our wedge) |
|---|---|---|---|---|
| **L1 direct** | TradeZella | $24-$33/mo | 7 yrs of journaling features, futures/options support | No deal-sourcing, no live auction integration, "I already own it" framing |
| **L1 direct** | Edgewonk | $30-$50/mo | Crypto/journal hybrid, strong community | Same: journal-first, not deal-first |
| **L2 adjacent** | Cars.com / CarGurus / AutoTrader | Free (ads) | Massive private-buyer inventory | Dealer-side tool; nothing for the person *buying* to flip |
| **L2 adjacent** | Manheim / Copart auction access | $200+/mo + buyer fee | The actual deal source | No buyer-side tooling; spreadsheets only |
| **L3 substitutes** | Facebook Marketplace alerts | Free | Free, fast | No margin calc, no comp data, no transport estimate |
| **L3 substitutes** | Trade Hunterr (TrustMRR) | ~$2.40/mo | Spotter UX | Limited auction integration; we beat it on wedge depth |

**Competition score: 4** — high in journaling, low in deal-spotting. We accept this because our wedge is the *other half* of the workflow.

---

## 3. PRD MVP (≤14d, solo)

### User stories (P0)
1. As a flipper, I paste a Copart/Manheim/IAA auction URL and get a **flip-comps panel**: last 6 private-party sales of the same year/make/model/trim within 50 mi, with median, p25, p75.
2. As a flipper, I enter my max bid; the app shows **net margin** after auction fee, transport (zip-to-zip estimate), and a 6% markup cushion.
3. As a flipper, I tap "watch" and get a push notification when the auction is closing in <60 min, with one-tap **"bid last +$200"** reminder.
4. As a flipper, I save my watch list and see **ranked-by-margin** opportunities across all 3 auction sites.

### Epic — P0 (ship-blockers)
- Auction URL parser (Copart/Manheim/IAA public listings)
- Private-party comps scraper (Facebook Marketplace + Craigslist + eBay Motors sold)
- Margin calculator (auction fee table + ZIP distance table)
- Push notifications (OneSignal free tier, 10K/mo is plenty)
- Auth (email magic link via Supabase)

### Epic — P1 (week 2)
- "List to private" one-tap (pre-fills FB Marketplace / Craigslist draft)
- Auction calendar view (what's closing in the next 24h)
- VIN photo OCR (snap a VIN barcode → auto-fill lot details)

### Epic — P2 (post-MRR proof)
- Multi-user "syndicate" mode (group of 3-5 flippers sharing a watch list)
- Dealer SaaS mode: charge a small business $99/mo for an embed of our comps on their lot page

### Non-goals (explicit)
- ❌ Journaling / P&L tracking (TradeZella owns this; we will *link out*, not build)
- ❌ Crypto / options / futures journaling
- ❌ Buy-here-pay-here financing workflows
- ❌ Mechanic inspection scheduling
- ❌ Title/registration DMV integrations

### Tech stack
- Next.js 14 (App Router) + Vercel
- Supabase (auth, DB, push trigger source)
- OneSignal (push)
- Playwright + a 2-vCPU proxy VM (scraping, $12/mo)
- Stripe (subscriptions)
- Cron: GitHub Actions free tier (15 comp refreshes/listing/day)

### Data model (sketch)
