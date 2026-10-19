# Direction — Static Forms (Privacy-First Form Backend)

Slug: `static-forms` · Tier: **GO** · Run: 2026-10-19_212028

## 1. Why this direction
**TrustMRR evidence:** `static-forms` has $9.88 MRR / $9.65 last30 / 123 subs — a real paying form-backend micro-SaaS already shipping. Demand_h 4, comp_h 2 from auto pass.

**Why a new entrant can win:**
- Formspree (L1) charges $8–$59/mo and tracks submissions for "abuse prevention"
- Web3Forms, Basin, FormSubmit all either: (a) log IP, (b) require JS, (c) cap free tier to 250/mo and shame you on the upgrade
- Privacy-first + self-hostable + zero-JS required = uncontested wedge
- Static Forms is solo-built — copy the spec, ship a polished v2

**Pain hypotheses to verify in day 1–3 (search/X):**
- "Formspree too expensive for landing page"
- "Form backend without tracking / GDPR-friendly"
- "Self-host form backend alternative"
- "Static site form submission netlify form replacement"

**MVP wedge:** Single-binary (Go or Rust) form backend. 1 Docker command. Zero tracking. Proxies to your email / Discord / Slack / webhook. Free tier: 1000 submissions/mo. Pro: $9/mo unlimited.

## 2. Competitor table (L1/L2/L3)

| Tier | Name | Price | Weakness vs us |
|---|---|---|---|
| L1 | Formspree | $8–$59/mo | Tracks IP, JS required on free |
| L1 | Web3Forms | Free / $8/mo | Requires JS, has analytics |
| L1 | Basin | $9–$49/mo | Email-locked, no webhook-only |
| L2 | FormSubmit | Free | Email-only, no dashboard |
| L2 | Netlify Forms | Free / Pro | Locked to Netlify hosting |
| L2 | Getform | $7–$39/mo | Limited Zapier, tracks |
| L3 | Plunk (self-host) | $0 self-host | Self-host only, harder setup |
| L3 | Listmonk-style DIY | $0 | You build it |

**Score:** competition = **2** (fragmented, no privacy leader, no "1 binary" leader).

## 3. PRD MVP

**Non-goals (P-out):**
- No form builder UI (we are backend)
- No webhooks beyond Discord/Slack/email
- No payment collection (use Stripe/Formspree for that)
- No multi-tenant org accounts in v1

**P0 (must ship day 1–14):**
- Single static binary: `forgeform serve` runs the backend
- 3 endpoints: POST `/submit` (public), GET `/dashboard` (auth), POST `/forms` (CRUD)
- 3 delivery channels: email (SMTP), Discord webhook, Slack webhook
- Anti-spam: honeypot field + rate limit + optional Turnstile (no Cloudflare lock-in)
- Dashboard: submissions list, CSV export, mark-as-spam
- Free tier: 1000 submissions/mo per domain, no signup required (API key per domain)
- Pro tier: $9/mo unlimited, custom domain keys
- Auth: magic-link email
- Landing page + docs + 5 integration snippets (Astro/Next/HTML/Hugo/11ty)

**P1 (post-MVP week 3–4):**
- Webhook-only mode (no email needed)
- File uploads to S3/R2
- Zapier/Make.com partner program
- White-label option for agencies ($49/mo)

**P2 (post-MRR):**
- Form analytics dashboard
- A/B form variants
- Multi-user org accounts

## 4. 14-day day-by-day build plan

| Day | Deliverable |
|---|---|
| 1 | Repo + Go module + `forgeform serve` boots health route; landing page skeleton |
| 2 | POST `/submit` with JSON + form-encoded; SQLite schema; persistence |
| 3 | Honeypot + rate limit + storage in SQLite |
| 4 | Email channel (SMTP via env), Discord webhook, Slack webhook |
| 5 | Magic-link auth, dashboard skeleton (HTMX, no SPA) |
| 6 | Submission list + CSV export |
| 7 | Stripe + Lemon Squeezy Pro tier, webhook → entitlement |
| 8 | Docs site (Astro) with 5 snippets, OpenAPI spec |
| 9 | Landing page copy, pricing, social proof slot |
| 10 | Bring-your-own-Docker install doc + `docker run` one-liner |
| 11 | Public beta: post on HN Show, r/selfhosted, IndieHackers |
| 12 | Bug bash, fix abuse vectors |
| 13 | Stripe live mode, pricing live, dashboard polish |
| 14 | Launch on Product Hunt + IndieHackers "launched" + 3 launch tweets |

**Stack:** Go (chi router + sqlx) + SQLite + HTMX + Pico.css + Stripe. ~2k LOC.

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $0 paid. $200 reserved for day 30 Product Hunt ad ($200–300 booster is optional, fits cap). $100 reserved for 2× small dev tool newsletter placements ($50 each if rejected/refunded in week 2).

| Week | Channel | Action |
|---|---|---|
| 1 (day 11–14) | HN Show, r/selfhosted, IndieHackers Launched, 3 launch tweets | Free |
| 2 | Changelog tweet thread (3 posts), reply to 5 IndieHackers comments, 1 podcast pitch (free indie podcasts), 1 newsletter pitch (GitHub Trending feed, SaaS weekly free listings) | Free |
| 3 | 5 SEO pages: "formspree alternative", "self-hosted form backend", "gdpr-friendly form", "static site contact form", "nocode form backend" — each ~600 words, internal links | Free |
| 4 | 1 guest post on dev.to or freecodecamp (formspree-privacy angle), Product Hunt launch with $200 boost | $200 (optional) |

**Channel-specific KPIs:**
- Week 1: 50 signups free, 5 paid
- Week 2: 150 free cumulative, 15 paid
- Week 3: 300 free, 30 paid
- Week 4: 600 free, 60 paid = **$540 MRR**

## 6. Unit economics to $10K MRR

- Price: $9/mo Pro per domain
- Need **1,111 paying domains** → $9,999 MRR
- ARPU: $9/mo
- Gross margin: ~96% (SMTP free tier OK, Turnstile free, Stripe fee 2.9%)
- CAC: ~$0 organic, ~$5 if any paid
- LTV (12 mo avg retention for indie tools): ~$108
- LTV/CAC: ~21×

**Path to 1,111 domains in 6 months (organic-only baseline):**
- Month 1: 60 paid → $540 MRR
- Month 2: +120 paid (HN/Reddit compounding) → $1,620 MRR
- Month 3: +250 paid (SEO kicks in) → $3,870 MRR
- Month 4: +400 paid → $7,470 MRR
- Month 5: +250 paid → $9,720 MRR
- Month 6: +100 paid (steady state) → $10,620 MRR

**Risk:** privacy-only wedge might be too narrow; fix by adding "static-first" to positioning.

## 7. Kill criteria (revisit by day 30)
- < 30 free signups by day 14 → reposition (drop privacy, lead on "1 binary")
- < 5 paid by day 30 → pricing wrong; A/B $5 vs $9
- Churn > 25% by day 60 → on-prem too easy; remove self-host feature
- Spam wave overwhelms inbox → add Turnstile mandatory

## 8. Re-verify before code (day 1–3)

Searches to run before commit:
1. `formspree alternative 2026 reddit` — confirm complaints
2. `"self-hosted form backend" site:news.ycombinator.com` — confirm demand
3. `form backend gdpr privacy` — confirm ICP
4. `@hussainanjar twitter` — read static-forms founder tweets for hints

If any of these return > 5 high-quality hits, ship. If empty, pivot angle.

## 9. If GO_NARROW (n/a — this is full GO)
