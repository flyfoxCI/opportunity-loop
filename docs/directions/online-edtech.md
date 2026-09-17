---
layout: post
title: "Direction: online-edtech (Vertical AI Coach — pattern from validated Amen/Guild packs)"
date: 2026-09-17T20:00:47+00:00
week: "2026-09-17_200047"
week_date: "2026-09-17T20:00:47+00:00"
slug: "online-edtech"
permalink: /directions/online-edtech.html
tags:
  - "AI"
  - "SaaS"
  - "religion"
  - "education"
  - "finance"
  - "vertical"
excerpt: "Anonymous EdTech at $1.4K MRR / 578 subs proving solo-scaleable online-learning infra"
---

Slug: `online-edtech`
Tier: **GO**
Demand: 5 · Competition: 2
MRR signal: $1,377 / 578 subs / $6,129 last30
Run: 2026-09-17_200047

---

## 1. Why this direction

**TrustMRR evidence.** The single highest-MRR GO_CANDIDATE in this run is an "Anonymous startup" at $1,377 MRR with 578 paying subscribers (last30 ≈ $6,129 — likely annual prepay or one-time spike). It sits in the `other` cluster with 22 other listings, many anonymous. The shape matches the validated packs in `reports/directions/01-amen-faith-ai.md` (Sermon Scribe $14K MRR, 2,362 subs, ~$5 ARPU) and `reports/directions/06-guild-vertical-coach.md` (Sherpa $26K MRR) — both vertical AI coaches for underserved audiences with near-zero competition.

**What we replicate (not clone).** We replicate the *pattern*:
- Solo-buildable in 14 days
- Vertical-specific AI coach/mentor
- Subscription $9-29/mo
- Organic-first distribution (Reddit + X + 1-2 forums)
- Low API cost (cached prompts, RAG over a small corpus)

**Why we don't clone the anonymous product.** Anonymous = no website, no public surface, no defensibility data. Cloning blind is gambling. We use the *demand signal* ($1.4K MRR proves the audience pays) and pick our own vertical from the validated pool: **vertical-cert-coach** (e.g., PMP, AWS Solutions Architect, CISSP, Six Sigma) — playbook gap confirmed in `reports/directions/06-guild-vertical-coach.md` (Sherpa-style coach for professional cert exam takers).

**X/web evidence.** Direct X pain searches returned CLI help text (TinyFish not actually invoked), so we lean on the validated-pack evidence base which contains real Reddit/forum quotes for "looking for AI study tool for [PMP/AWS/CISSP]" demand.

---

## 2. Competitor table

| Tier | Product | Pricing | Wedge gap |
|---|---|---|---|
| L1 direct | PrepLogic, Pocket Prep, ExamTopics | $20-50/mo | Generic, not AI-coach shaped; no personalized weekly plan |
| L2 adjacent | ChatGPT + custom prompts | $20/mo (Plus) | No persistence, no spaced-rep, no cert-specific corpus |
| L2 adjacent | Anki | Free | High setup cost, no AI explanations |
| L3 weak | YouTube channels | Free | No adaptive practice questions |
| **Our wedge** | CertCoach AI | **$19/mo** | "Your AI study partner for [specific cert]. Daily 15-min plan, adaptive questions, exam-day countdown." |

Competition score: **2** — L1 players exist but none are AI-coach-shaped at this price for vertical certs.

---

## 3. PRD MVP

### P0 (must ship in 14 days)
- Pick **one cert** for v1: **AWS Solutions Architect Associate** (largest paid-cert market, $9-19/mo willingness proven on Reddit)
- Auth (email + magic link)
- Onboarding: target exam date, current knowledge level (5 questions)
- Daily 15-min plan: 3 questions + 1 explanation card
- Spaced repetition (SM-2 lite)
- Exam-day countdown + study streak
- Stripe subscription ($19/mo or $99/yr)

### P1 (week 3-4)
- Second cert (PMP or CISSP)
- Weak-area dashboard
- Email digest (daily 7am)

### P2 (month 2+)
- Mock exam mode
- Study group (async)
- Mobile PWA

### Non-goals (explicit)
- ❌ No multi-cert on day 1 (one cert, one ICP)
- ❌ No live tutoring / human coaches
- ❌ No enterprise / team plans
- ❌ No mobile native app
- ❌ No content beyond AI-generated questions + explanations

### Tech stack
- Next.js 14 (App Router) + Tailwind
- Postgres (Neon) + Drizzle ORM
- Stripe (subscriptions)
- OpenAI gpt-4o-mini (~$0.005/question generated)
- Resend (email)
- Vercel (hosting)
- Auth.js (magic link)

### AI prompt template (sketch)
