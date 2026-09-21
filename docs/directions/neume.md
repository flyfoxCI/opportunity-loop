---
layout: post
title: "Direction: neume"
date: 2026-09-21T20:47:48+00:00
week: "2026-09-21_204748"
week_date: "2026-09-21T20:47:48+00:00"
slug: "neume"
permalink: /directions/neume.html
tags:
  - "AI"
  - "creator"
  - "vertical"
  - "analytics"
excerpt: "Substack/newsletter analytics + growth"
---

## Why this direction

**TrustMRR evidence**
- $10 MRR / $15 last30 / 110 subscribers — early traction
- Stage A coarse score: demand=3, competition=2 (passes dual gate as pure GO)
- Founder @abh1nash — public builder
- Adjacent: anonymous-startup-42 ($17 MRR / 104 subs in same newsletter analytics cluster) validates demand

**X / web evidence (Stage A heuristic)**
- "Substack analytics", "newsletter growth tool", "Substack SEO" all trending creator-search terms
- Substack itself ships minimal analytics — opportunity for indie layer
- Ghost, Beehiiv, ConvertKit have built-in but lack Substack-specific depth

**Why now**
- Substack has 3M+ active newsletters and is the default for solo writers in 2026
- Substack's own analytics is bare-bones (subs, open rate only)
- No indie tool owns "Substack-first growth analytics + AI recommendations"

## Competitor table

| Tier | Competitor | Price | Weakness |
|---|---|---|---|
| L1 direct | SubstackStats (3rd-party) | $0-10/mo | Basic, no AI |
| L1 direct | NoteStack (TrustMRR-listed, $0 MRR) | early | No traction yet |
| L1 direct | Beehiiv / ConvertKit analytics | bundled | Platform-locked, not Substack |
| L2 adjacent | SparkLoop / Referral programs | $20+/mo | Referral-only, not analytics |
| L2 adjacent | Plausible / Fathom | $9-19/mo | Web analytics, not newsletter-specific |
| L3 substitute | Manual spreadsheet | $0 | Tedious, no insights |

**Competition score: 2** — niche is open. "Substack-specific growth analytics + AI writer assistant" is the wedge.

## PRD MVP

**User story (P0)**
> As a Substack writer with 500-50,000 subs, I want to see which posts drove the most new subs, what subjects convert best, and get AI suggestions for next week's topic.

**Epic 1 — Connect Substack (P0)**
- OAuth or RSS-based scrape (since Substack has no public analytics API for 3rd parties)
- Pull: post metadata (title, date, URL, word count), subscriber-count snapshots over time
- Daily refresh

**Epic 2 — Growth analytics (P0)**
- Net new subs per post
- Top-performing posts by growth rate
- Subject-line A/B comparison
- Best day/time to publish (recommendation)

**Epic 3 — AI assistant (P1)**
- Topic generator: "Based on your last 20 posts, suggest 5 topics likely to grow"
- Subject-line scorer: rate open-probability before send
- (P1) Repurpose to Twitter / LinkedIn

**Epic 4 — Competitor tracking (P1)**
- Track similar newsletters (manual input)
- Compare growth rates

**Non-goals (MVP)**
- ❌ Ghost / Beehiiv / ConvertKit support (Substack only)
- ❌ Email-sending (you send from Substack)
- ❌ Monetization / paid-sub features (Substack-native)
- ❌ Mobile app (web only)

**Tech stack (solo, 14 days)**
- Frontend: Next.js + Tailwind + Recharts
- Backend: Next.js API routes + cron job
- Data: scrape Substack RSS + Wayback Machine snapshots for subscriber-count history
- LLM: GPT-4o-mini for topic gen
- DB: Supabase
- Payments: Stripe
- Hosting: Vercel

## 14-day build plan

| Day | Task |
|---|---|
| 1 | Landing page + waitlist |
| 2 | Substack OAuth (or RSS auth) + data pipeline |
| 3 | Subscriber-count history (scrape Wayback + daily snapshots) |
| 4 | Growth analytics dashboard (post-level + aggregate) |
| 5 | Auth + Stripe test |
| 6 | AI topic generator (MVP) |
| 7 | **Soft launch** — IH, X, r/Substack, r/newsletters |
| 8 | Polish UI, fix bugs |
| 9 | Add subject-line scorer |
| 10 | Add "best publish time" recommender |
| 11 | SEO blog: "Substack analytics", "newsletter growth tools" |
| 12 | Affiliate for newsletter communities |
| 13 | ProductHunt assets |
| 14 | **Public launch** — PH + X + IH |

## 30-day marketing calendar (budget ≤ $300)

| Week | Activity | Cost |
|---|---|---|
| 1 | X thread: "I built a Substack analytics tool" + free tier demo | $0 |
| 1 | IndieHackers post (newsletter-creator audience) | $0 |
| 1 | DM 30 Substack creators with 1K-50K subs (free 3-mo codes) | $0 |
| 2 | 5 SEO posts: "Substack analytics", "newsletter growth", etc. | $0 |
| 2 | Sponsor 1 newsletter Twitter account (10K-30K) — $80 | $80 |
| 2 | Guest post on 1 newsletter about newsletters (free) | $0 |
| 3 | ProductHunt launch — $100 featured | $100 |
| 3 | 2 micro-influencer sponsorships ($40 each, newsletter niche) | $80 |
| 4 | "Free Substack audit" lead magnet (signup → instant report) | $0 |
| 4 | User showcase: retweet best dashboards | $0 |
| 4 | Email nurture → paid | $0 |

**Total: $260**

**KPI targets**
- Day 7: 50 signups, 8 paid
- Day 14: 200 signups, 30 paid
- Day 30: 600 signups, 110 paid @ $19/mo = $2,090 MRR
- Path to $10K: 525 @ $19 OR 345 @ $29

## Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Price | $19/mo (Writer) or $29/mo (Pro, multiple newsletters) |
| Free tier | 1 newsletter, 7-day history |
| Conversion | 15% |
| LTV (10 mo avg retention) | ~$190-$290 |
| Gross margin | ~88% (mostly LLM + storage) |
| CAC | ~$15 |
| LTV/CAC | ~12:1 |

**Path to $10K MRR**
- 525 @ $19 OR 345 @ $29
- Newsletter creators are sticky (low churn) → realistic in 9-12 months

## Kill criteria
- Day 14: <5 paid → pivot or kill
- Day 30: <30 paid → kill or major pivot
- Data accuracy (subscriber counts) off by >10% → rebuild scrape
- LTV/CAC < 3 by day 60 → stop paid

## Wedge
n/a (pure GO)
