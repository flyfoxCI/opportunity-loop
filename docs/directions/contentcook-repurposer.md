---
layout: post
title: "Direction — Long-Form to 30-Platform Repurposer"
date: 2026-10-19T21:20:28+00:00
week: "2026-10-19_212028"
week_date: "2026-10-19T21:20:28+00:00"
slug: "contentcook-repurposer"
permalink: /directions/contentcook-repurposer.html
tags:
  - "AI"
  - "creator"
  - "social"
  - "video"
excerpt: "Long-form → 30-platform repurposer with human-in-loop"
---

Slug: `contentcook-repurposer` · Tier: **GO** · Run: 2026-10-19_212028

## 1. Why this direction
**TrustMRR evidence:** `thecontentcook` MRR $4 / last30 $22 / 29 subs. Auto shows demand_h 3, comp_h 2. Description was a content repurposing product.

**Why this is a real opening:**
- Repurpose.io ($24/mo) — exists but is video-focused and 6-platform cap
- Buffer / Hootsuite — social schedulers, no AI rewrite
- Substack / Beehiiv newsletters — they push to email only
- OpusClip, Chopcast — do video clips
- **Nobody** owns **blog-post → 30 output formats** in one click for the indie newsletter writer

**The wedge:** Drop in any long-form URL (blog post, Substack, LinkedIn post, podcast show notes). Get back 30 outputs: 5 tweet threads, 5 LinkedIn posts, 5 IG captions, 5 FB posts, 5 Reddit hooks, 5 newsletter CTAs — each formatted native to platform.

**ICP:** Solo newsletter writers, indie consultants, ghostwriters (substack-heavy). 50K subs and under.

## 2. Competitor table (L1/L2/L3)

| Tier | Name | Price | Why we win |
|---|---|---|---|
| L1 | Repurpose.io | $24/mo | Video-only |
| L1 | Hootsuite | $99+/mo | Scheduling, $99 floor |
| L2 | Taplio / Supergrow | $30+/mo | LinkedIn-only |
| L2 | Tweet Hunter | $49/mo | Twitter-only |
| L2 | Missinglettr | $19/mo | Has AI but 1 platform |
| L3 | ChatGPT prompts | $20/mo DIY | Manual process |
| L3 | Buffer | Free / $6 | Schedules, no rewrite |

**Score:** competition = **2**

## 3. PRD MVP

**Non-goals:**
- No scheduling/auto-post (differentiator: we are the writer, not the scheduler)
- No image generation
- No multi-user org accounts in v1
- No analytics / tracking pixels

**P0 (day 1–14):**
- Paste URL or text input
- Fetch + clean text (readability parser)
- AI rewrite into 30 outputs via prompt templates (Claude or GPT-4-mini)
- Tone presets: professional, witty, contrarian, founder
- Length presets: short / medium / long
- CSV export + copy-to-clipboard per output
- Account via magic-link
- Pricing: Free = 1 url/wk, Pro = $14/mo or $99/yr (50 URL/wk), Indie = $7/mo (10 URL/wk, no CSV)
- Landing page + 30-day playbook PDF (lead magnet)

**P1 (week 3–4):**
- Webhook delivery to Zapier/Make
- Brand voice fine-tuning (save 3 voice presets)
- Saved library of past outputs

**P2:**
- Auto-schedule to Buffer
- Multi-account workspaces

## 4. 14-day day-by-day build plan

| Day | Deliverable |
|---|---|
| 1 | Repo + Next.js + Convex/Supabase + auth |
| 2 | URL fetch + readability extractor (Mozilla Readability) |
| 3 | Prompt template v1 (30 outputs, 5 tones, 3 lengths) |
| 4 | Output UI: 5 tabs × 6 outputs, copy button per output |
| 5 | CSV export |
| 6 | Stripe live mode, subscription tiering |
| 7 | Landing page (3 sections: hero, demo, pricing) |
| 8 | Lead magnet: "30-Day Content Repurpose Playbook" PDF |
| 9 | Email capture on landing + welcome sequence (3 emails) |
| 10 | Onboarding: 1 sample URL preloaded |
| 11 | Public beta in IndieHackers / r/Blogging |
| 12 | Bug bash + output quality review |
| 13 | 5 SEO landing pages: "blog to tweets", "newsletter to social", etc. |
| 14 | Launch: Product Hunt + IndieHackers + tweet thread |

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $0 baseline. $100 reserved for 2× paid newsletter placements (e.g., Marketing Brew, $50 each). $200 reserved for 1× podcast sponsor or Product Hunt booster.

| Week | Channel |
|---|---|
| 1 | IndieHackers "building in public" thread, r/Blogging, r/Newsletter, 3 launch tweets (with before/after output samples) |
| 2 | 5 reply tweets daily to content marketers; 1 LinkedIn post with carousel |
| 3 | 5 SEO pages; 1 YouTube short demo |
| 4 | 1 newsletter placement ($50); 1 podcast pitch |

## 6. Unit economics to $10K MRR
- Price: Indie $7/mo / Pro $14/mo; mix 60% Pro / 40% Indie
- Blended ARPU: ~$11/mo
- Need **~910 paying**
- Gross margin: ~75% (AI API costs ~$1–2/user/mo at scale)
- CAC: $0 organic, ~$10 paid
- LTV (12-mo avg for indie tools): ~$130
- LTV/CAC: ~13×

**Path to 910 paying:**
- Month 1: 80 paid → ~$880 MRR
- Month 2: 200 paid → ~$2,200 MRR
- Month 3: 350 paid → ~$3,850 MRR
- Month 4: 550 paid → ~$6,050 MRR
- Month 5: 750 paid → ~$8,250 MRR
- Month 6: 920 paid → ~$10,120 MRR

## 7. Kill criteria (day 30)
- < 30 paid by day 30 → output not differentiated enough; rewrite prompts + double-check tone controls
- AI cost > 35% of revenue → switch to lower-cost model + cache outputs
- Churn > 25% by day 60 → onboarding quality issue; add sample URL

## 8. Re-verify before code (day 1–3)
1. `r/Newsletter "repurpose" recent` — confirm pain
2. `"@repurpose_io" OR "@taplio" hate OR broken twitter`
3. `"post to 30 platforms" reddit OR indiehackers`
4. Search: `content repurposing AI 2026`

## 9. If GO_NARROW (n/a — this is full GO)
