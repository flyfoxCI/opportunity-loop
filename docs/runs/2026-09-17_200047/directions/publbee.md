# Direction: publbee (Indie Newsletter Ops — narrow by ICP)

Slug: `publbee`
Tier: **GO_NARROW**
Demand: 4 · Competition: 2
MRR signal: $34 / 100 subs / $33 last30
Run: 2026-09-17_200047

---

## 1. Why this direction

**TrustMRR evidence.** Publbee at $34 MRR with 100 subscribers = newsletter-publishing-platform with real paying writers. ARPU ≈ $0.34/mo suggests a low price tier ($3-5/mo) or a $9-19/mo with annual prepay.

**Why GO_NARROW.** Newsletter platforms (Substack, Beehiiv, Ghost) are saturated at the top. We narrow by ICP: **indie newsletter writers earning $0-2K/mo from their list** — the segment Substack ignores (no analytics, no automation) and Beehiiv over-prices (their $49/mo tier is overkill for $500/mo earners).

**What we replicate.** Pattern from `reports/directions/02-whitelabel-vertical-saas.md` (vertical B2B SaaS white-label) — pick one ICP, ship the 5 features they actually use, ignore the rest.

**X/web evidence.** Pain searches empty; we lean on TrustMRR signal + validated-pack pattern.

---

## 2. Competitor table

| Tier | Product | Pricing | Wedge gap |
|---|---|---|---|
| L1 direct | Substack | Free (10% rev share) | No analytics, no automations, locked to Substack network |
| L1 direct | Beehiiv | Free - $99/mo | Overkill for small lists, $49+ tiers feel enterprise |
| L2 adjacent | Ghost | $9-25/mo | Self-host required at $25, technical barrier |
| L2 adjacent | ConvertKit | $9-25/mo | Email-first, not newsletter-first |
| L2 adjacent | MailerLite | $10-30/mo | Cheap but no native newsletter publishing |
| L3 weak | WordPress + MailPoet | $0 + plugin | Setup hell |
| **Our wedge** | **Publlite: Newsletter ops for writers earning < $2K/mo** | **$9/mo (1 newsletter, 5K subs)** | "Beehiiv's analytics without the $99 price" |

Competition score: **2** — incumbents exist but ignore the indie-earning segment.

---

## 3. PRD MVP

### P0 (must ship in 14 days)
- Newsletter publishing (rich-text editor + image embed)
- Subscriber management (import CSV, double opt-in)
- Basic analytics (open rate, click rate, subscriber growth)
- Stripe subscriptions for paid newsletters (5% fee)
- 1 custom domain support
- Email delivery via Resend or Postmark

### P1 (week 3-4)
- Automation (welcome series, re-engagement)
- A/B test subject lines
- Subscriber segmentation
- Referral program

### P2 (month 2+)
- API + webhooks
- Multi-author / team
- Paid courses integration
- Podcast hosting

### Non-goals
- ❌ No enterprise / team plans in v1 (solo writers only)
- ❌ No podcast hosting in v1 (Substack territory)
- ❌ No AI writing assistant in v1
- ❌ No ad network / sponsored content
- ❌ No mobile app

### Tech stack
- Next.js 14 + Tailwind
- Postgres + Drizzle
- Stripe Connect (paid newsletters)
- Resend (transactional + broadcast)
- Cloudflare (DNS + email routing)
- Vercel + Sentry

### Cost per writer
- Email delivery: $0.40 / 1K emails (Resend)
- At 1K subs × 4 newsletters/mo = $1.60/mo per writer
- At $9/mo price = 82% gross margin

---

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Repo init, Next.js, DB schema, Stripe Connect setup |
| 2 | Auth, newsletter editor (TipTap), draft/publish flow |
| 3 | Subscriber import (CSV), double opt-in email |
| 4 | Email broadcast (Resend batch), queue worker |
| 5 | Stripe Connect paid newsletter flow (5% fee) |
| 6 | Analytics: open, click, growth charts |
| 7 | Custom domain setup (Cloudflare API), SSL |
| 8 | Landing page, pricing, signup flow |
| 9 | Onboarding wizard (5 steps), Stripe webhook testing |
| 10 | Beta: 10 indie writers from r/NewsletterGrowers |
| 11 | Iterate, fix top 3 bugs |
| 12 | Public launch on r/NewsletterGrowers + Indie Hackers |
| 13 | X thread: "I built a $9/mo Substack alternative" |
| 14 | First paying user; review funnel |

---

## 5. 30-day marketing calendar (budget ≤ $300)

| Week | Channel | Action | Cost |
|---|---|---|---|
| 1 | Reddit | Lurk + contribute on r/NewsletterGrowers, r/Substack, r/Beehiiv | $0 |
| 1 | X | 2 posts/day: #newsletter #indiehackers | $0 |
| 2 | Reddit | "I built this" + comparison post (vs Substack/Beehiiv) | $0 |
| 2 | Indie Hackers | Build log post | $0 |
| 2 | SEO | 2 posts: "Substack alternative 2026", "newsletter platform for small lists" | $0 |
| 3 | Paid | $100 Reddit ads (r/NewsletterGrowers promoted) | $100 |
| 3 | Partnerships | Reach out to 5 newsletter-about-newsletters creators | $0 |
| 4 | Paid | $100 Reddit ads + $50 X promote | $150 |
| 4 | Referral | "Refer a newsletter friend, get 1 month free" | $0 |
| **Total** | | | **$250** |

Target Week 4: 30 paying writers × $9 = **$270 MRR** (pure subscription; paid-newsletter rev share is bonus).

---

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Price | $9/mo (1 newsletter, 5K subs) |
| Blended ARPU | $9/mo (no annual tier in v1) |
| Gross margin | 82% |
| Target MRR | $10,000 |
| Required paying users | 1,111 writers |
| Monthly churn (B2C prosumer) | 5% |
| New users/mo to hit steady state | ~60/mo (steady + growth) |
| Conversion (free → paid) | 4% (Beehiiv/Substack benchmark) |
| Free writers needed | 1,500/mo from organic |
| CAC (organic) | ~$5-15 |

**Path to $10K MRR: ~18-24 months** at organic pace (B2C prosumer is slow).
**Bonus revenue:** 5% fee on paid newsletters = passive income as writers grow. At 100 writers × $500/mo subscriber revenue × 5% = $2,500/mo bonus MRR.

---

## 7. Kill criteria

- Week 2: < 30 beta signups → kill (no ICP-product fit)
- Week 4: < 10 paying writers → kill or pivot ICP
- Week 8: churn > 10%/mo → product fit issue, kill
- Week 12: < 50 paying writers → not on $10K MRR trajectory, kill

---

## Wedge (required for GO_NARROW)

### What we REFUSE to build (the wedge is what you don't ship)

- ❌ **No team / multi-author plans.** Solo newsletter writers only.
- ❌ **No enterprise features** (SSO, SAML, audit logs).
- ❌ **No podcast hosting.** Substack owns that.
- ❌ **No AI writing assistant.** That's Beehiiv's AI tier territory; clutters UX.
- ❌ **No course / digital product selling.** That's Kajabi/Gumroad; out of scope.
- ❌ **No ad network / sponsorship marketplace.** Out of scope.
- ❌ **No mobile app.** Web-first; writers don't need mobile.
- ❌ **No "Substack import" magic.** Manual CSV import only; we don't compete on migration.

### What we WILL build (focused feature set)

- ✅ Rich-text editor + image embed
- ✅ Subscriber import + double opt-in
- ✅ Broadcast emails (Resend)
- ✅ Stripe Connect paid newsletters (5% fee)
- ✅ Basic analytics (open, click, growth)
- ✅ 1 custom domain
- ✅ 1 newsletter per writer

### Why the wedge matters

Without the wedge, this becomes "yet another newsletter platform" and dies against Substack's network effects. The wedge is: **indie writers earning < $2K/mo from their list have no good $9/mo option** — they're forced to choose between Substack (locked ecosystem, 10% fee) and Beehiiv ($49+ overkill). We fill that exact gap.
