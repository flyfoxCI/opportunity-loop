# Direction — `fastwrite-indie-seo` (unbundle of `fastwrite-io`)

> **UNBUNDLE** of fastwrite.io ($134 MRR · 616 subs · demand 4 / comp 2).
> **Tier:** GO  ·  **MVP 12 days · solo**  ·  **$300 / 30d marketing**

---

## 1. Why this direction

**TrustMRR evidence**
- fastwrite.io has 616 paid users against only $134 MRR — implying a very low ARPU ($0.22/mo average, almost certainly annual plans paid up front at low price). **What this proves:** strong pull-through at the bottom of the market, low willingness-to-pay for the current product shape.
- 616 is a *lot* of subscribers for a generic writing tool — meaning the **demand signal is unusually strong** but the **current product is under-monetized**.

**Web / cultural evidence**
- Indie SaaS founders + tiny agency owners publicly bemoan: "I keep meaning to write SEO content but never do."
- Jasper AI, Copy.ai, Writesonic — these are the household names, **but** their pricing ($49–$99/mo) and feature sprawl (brand voice, campaigns, multi-channel output) are overkill for a one-person SaaS founder who just wants **4 decent articles a month**.
- Reddit r/Entrepreneur, r/SaaS, IndieHackers threads on "best AI writing tool for SEO" are evergreen.
- A second well-documented segment: **indie hackers' "build in public" LinkedIn / X ghostwriter need** — multiple posts per week, founder has 30 min/wk, hates writing.

**Why the wedge works**
- Tightly bound to one ICP: **indie SaaS founders & solo agencies** who want to publish 4 SEO posts/mo without spending 8 hours.
- Intake = changelog, help docs, and one-line "what's your SaaS about" — output = ready-to-edit draft.
- The competitor-less zone is: **draft quality that requires < 10 min of founder editing** while staying SEO-keyword-coherent.

---

## 2. Competitor table (L1 / L2 / L3)

| Tier | Competitor | Pricing | Why they lose |
|---|---|---|---|
| L1 direct | **fastwrite.io** (listing) | Low ARPU, generic | Under-branded, no ICP focus. We win by going narrower. |
| L1 direct | **Jasper AI** | $49–125/mo | Overkill, generic brand voice, expensive for indie founders. |
| L1 direct | **Copy.ai** | $49/mo | Same problem; multi-purpose so feels generic. |
| L1 direct | **Writesonic** | $20–500/mo | SEO mode is OK; not indie-founder-aware. |
| L2 adjacent | **Surfer AI / Frase / Koala** | $89+/mo | SEO-guidance-first, founder-rare. |
| L2 adjacent | **Byword.ai** | $190+/mo | Programmatic SEO for agencies; not for solo founders. |
| L3 substitute | **ChatGPT + a spreadsheet** | $20/mo (Plus) | Free-ish but founder spends 3 hrs/draft. We win on time-to-publish. |
| L3 substitute | **Hire a VA in Philippines ($3–6/hr)** | $250–500/mo | Quality varies; 1-week lead time. We win on speed + SEO structure. |

**Score:** competition = **2**. No one owns the indie-founder-ICP corner hard.

---

## 3. PRD MVP (P0 / P1 / P2 + non-goals)

### P0 — must ship day 12
- **ICP intake form** (<2 min): SaaS name, one-line value-prop, target ICP, 3 keywords, sample tone preference (paste 1 past post).
- **Research:** scrape top-10 SERP for each keyword; pull outline + People Also Ask + competitor word counts.
- **Draft generation:** 1,000–1,500 word SEO-structured post (H2/H3, FAQ, summary block, internal link suggestions to user's own site).
- **Editor:** inline editor + suggestion mode + "make it sound less AI" button.
- **Auto-publish to WordPress + Ghost + Webflow (via API)** with one toggle.
- **4 posts/mo** quota on $19/mo plan; unlimited on $39/mo agency plan.

### P1 — month 2
- Internal-link planner (you own your site's URL; we crawl 2 levels, suggest related anchors).
- "Repurpose" — turn one post into 5 LinkedIn / X / Threads posts.
- Style trainer: founder pastes 5 past posts, we fine-tune style.

### P2 — month 3+
- Programmatic SEO mode (upload CSV of variants) — moves into the agency tier.
- Multi-language (es/de/fr).
- Human editor add-on ($99/post, marked-up).

### Non-goals
- **No general "AI image generation."** Stay text.
- **No marketing automation (email, social scheduling).** Cross-link to Buffer/Later.
- **No multi-channel campaign brief system.** Out of scope for solo founder.

### Pricing
- Free: 1 draft/mo, watermarked with "drafted with FastWrite".
- **Indie plan: $19/mo** — 4 drafts/mo, auto-publish enabled.
- **Pro plan: $39/mo** — unlimited drafts + internal-link planner + style trainer.
- **Agency plan: $99/mo** — 5 sites, 50 drafts/mo, programmatic SEO.

### Tech stack
- Next.js 14 + Tailwind + shadcn/ui.
- Supabase (auth + db + posts).
- Postgres + pgvector for tone/style retrieval.
- GPT-4o (drafts), Claude Sonnet (edits), Perplexity API (research).
- Stripe for payments.
- WordPress/Ghost/Webflow REST API clients.

---

## 4. 14-day day-by-day build plan

| Day | Goal | Output |
|---|---|---|
| **D1 Mon** | Repo scaffold + auth (magic link) + multi-tenant data model. | Login + project model. |
| **D2 Tue** | ICP intake form + project dashboard. | Onboarding flow. |
| **D3 Wed** | Keyword research via Perplexity + top-10 SERP scrape. | Research component. |
| **D4 Thu** | Outline generator (Claude Sonnet). | Outline view. |
| **D5 Fri** | Draft generation (GPT-4o, 1,200-1,500 words, structured). | First draft works. |
| **D6 Sat** | Inline editor + "sounds less AI" rewriter + diff view. | Editable drafts. |
| **D7 Sun** | WordPress / Ghost / Webflow API clients (one path each, max 1 site/connection). | Publish to 3 platforms. |
| **D8 Mon** | Stripe + quota gates. | Paywall live. |
| **D9 Tue** | Polish + empty states + error handling + keyboard shortcuts. | Demo-ready. |
| **D10 Wed** | Beta with 8 indie founders from IndieHackers. | 8 installs. |
| **D11 Thu** | Bug bash, draft quality improvements. | Stable. |
| **D12 Fri** | Marketing assets + landing page v2. | Public launch. |
| **D13 Sat** | IndieHackers launch post + X thread. | Launched. |
| **D14 Sun** | Reddit r/SaaS + LinkedIn founder feed. | Live. |

**DoD:** Draft quality at "founder-edits in ≤10 min" bar (validated with 5 testers), auto-publish works to WordPress, payment works.

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Day | Channel | Action | Cost |
|---|---|---|---|
| D1 | IndieHackers | Lurk + comment helpfully on 5 build-logs/day. | $0 |
| D3 | X | Build @fastwrite handle; first thread on "why I hate SEO writing". | $0 |
| D5 | IndieHackers | "I'm building a content writer for indie founders — what would make you actually publish?" (lead-magnet post). | $0 |
| D7 | SEO | Publish 3 SEO articles on the *target audience's* keywords: "best ai writer for indiehackers", "ai seo post writer for saas", "indie hacker linkedin ghostwriter". | $0 |
| D10 | Reddit | Cross-post in r/SaaS, r/Entrepreneur, r/copywriting. | $0 |
| D12 | IndieHackers | Build log #1. | $0 |
| D14 | X | Demo GIF: "Look how empty my drafts folder is now." | $0 |
| D15 | ProductHunt | Launch (Tue). | $0 |
| D18 | Reddit | AMA in r/SaaS. | $0 |
| D21 | LinkedIn | Repurpose own posts + tag indie founders. | $0 |
| D24 | IndieHackers | "$X MRR by day 24" post + first customer screenshot. | $0 |
| D27 | SEO | Add 2 more long-tail pages: "chatgpt vs jasper for indies", "fastwrite review". | $0 |
| D30 | Lifecycle | Win-back email + referral discount (give 1 mo, get 1 mo). | $0 |

**Paid budget:** **Default $0.** If D21 organic stalls, allocate $200 to LinkedIn ad targeted at "Indie Hacker / SaaS Founder / Writer" ($10/day, 20 days).

**KPIs**
- Time-to-publish (from intake → first draft) < 60 sec.
- Founder edit time per draft < 10 min.
- Free→paid ≥ 4%.
- MRR by D30: ~$500–800.

---

## 6. Unit economics to $10K MRR

| Variable | Value | Source |
|---|---|---|
| ARPU (blend) | $24/mo | 70% Indie $19 + 20% Pro $39 + 10% Agency $99 → weighted ≈ $28 → with intro discounts year-1 ≈ $24 blended. |
| Gross margin | 70% | GPT-4o + Claude + Perplexity ≈ $0.05/draft. Stripe 2.9%. Stripe + LLM ≈ 30% at low scale, 18% at scale. |
| Monthly churn (B2C indie) | 5% | Solo founders churn a lot; we offset with agency tier. |
| Paid users needed for $10K MRR | ~420 | $10,000 / $24 ≈ 417. |
| New paid / month needed | ~25 | 417 × 5% ≈ 21/mo. |

**Path to $10K MRR (12 mo)**
| Month | Paid | New | Churn | Paid | MRR |
|---|---:|---:|---:|---:|---:|
| 1 | 25 | 25 | 1 | 49 | $1,176 |
| 3 | 100 | 60 | 5% | 157 | $3,768 |
| 6 | 260 | 90 | 5% | 346 | $8,304 |
| 9 | 430 | 100 | 5% | 526 | $12,624 |
| 12 | 600 | 110 | 5% | 706 | $16,944 |

> Note: at $24 ARPU and IndieHackers + X compounding, $10K MRR is achievable by **month 5–6**. Plan for $10K MRR by month 9 with conservative assumptions.

**Break-even:** ~10 paid = ~$240/mo MRR (covers API costs).

---

## 7. Kill criteria (hard)

- **Founder edit time > 15 min/draft** after 3 rounds of prompting → AI output quality is below the bar; rewrite the system prompt + add retrieval over the founder's existing posts.
- **Free→paid < 2% by D30** → ICP/positioning mismatch; consider narrowing more.
- **< 50 free drafts/wk by D30** → channels wrong.
- **GA4 → LinkedIn auto-publish fails 1+ times/wk** → platform-capability risk; cut Webflow first.
- **Duplicate-content SEO penalty** → use proper canonical, ensure human-pass edits >20%.

---

## 8. Risks specific to AI SEO writers

- **Google "Helpful Content" algorithm.** Mitigation: editor requires founder-final-edit before publish; UI forces "I have read & edited" checkbox.
- **AI fatigue / "sounds like AI" stigma.** Mitigation: the "rewrite to sound less AI" button and the style-trainer feature.
- **LLM API price spikes.** Mitigation: cache common outlines, batch prompting, route cheap drafts to GPT-4o-mini by default.
- **WordPress/Ghost pluggable plugin churn.** Mitigation: simple REST only, no deep integration.
