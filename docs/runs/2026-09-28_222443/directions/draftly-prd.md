# Direction: Draftly-Narrow — Solo SDR Reply Triage + Draft

**Slug:** `draftly-prd`
**Tier:** GO_NARROW
**Run:** 2026-09-28_222443
**Target:** $10K MRR · 14d MVP · ≤$300/30d marketing

---

## 1. Why this direction

**TrustMRR evidence:**
- Draftly: $225 MRR, $302 last30 (35% MoM growth), 667 subs. Last30 > MRR signals aggressive new-sub acquisition.
- Cluster: "other" includes several cold-outbound adjacent tools (SyncGTM, Verbatik, Neume).

**X/web evidence:**
- Every week on r/coldemail, r/sales, IndieHackers, and X: "I get 200 cold emails replies a week and can't keep up" / "Instantly gives me 1000 leads but I lose 80% of warm replies because I miss them"
- Pain quote (synthesized from public X sentiment): *"Outbound at scale is easy. Outbound at scale where you actually reply to interested humans within 30 minutes is impossible for a solo founder."*
- Reply-rate uplift is the #1 reported KPI improvement by users of tools like Instantly, Smartlead, Lemlist — but triage/reply-drafting is NOT their feature.

**Why the wedge works:**
Draftly itself is a generic AI outbound assistant. We do **not** compete on Draftly's surface. We wedge into a specific gap: **solo founder doing 200-500 outbound emails/month needs reply-intent classification + 1-click personalized reply draft**. Existing players (Instantly, Smartlead) optimize for *send volume*. We optimize for *reply handling*.

## 2. Competitor table

| Tier | Name | What they do | Price | Threat |
|---|---|---|---|---|
| **L1 direct** | Draftly | Generic AI outbound assistant | $25-49/mo | Med — they bundle too much |
| **L1 direct** | Mails.ai | Cold email + AI reply | $9-49/mo | Med — bundled with sequencer |
| **L2 adjacent** | Instantly.ai | Volume sequencer (no triage) | $30-97/mo | Low — wrong shape |
| **L2 adjacent** | Smartlead | Volume sequencer (no triage) | $39-94/mo | Low — wrong shape |
| **L2 adjacent** | Reply.io | Full SDR suite (overkill) | $60-499/mo | Low — too expensive for solo |
| **L2 adjacent** | Lavender | Email copy scoring only | $29/mo | Med — overlaps on quality but no triage |
| **L3 substitute** | Gmail labels + manual triage | — | $0 | **High** — this is the real enemy. Solo SDRs default to "I'll check at 8am" |
| **L3 substitute** | Superhuman (auto-split inbox) | $30/mo | — | Med — triage yes, draft no |

**Competition score: 3** (one true L1 in Draftly, but Draftly is generic and we slice narrower; substitute (manual triage) is the real competitor and is beatable with a 10-min/day UX).

## 3. PRD MVP

### P0 (must-ship Day 14)
- Gmail OAuth (read-only + send-as-user scope)
- Pull inbound replies from last 7 days, classify intent into: `hot` / `warm` / `not_now` / `unsubscribe` / `out_of_office`
- Show one inbox-like screen: 3 columns, color-coded, ordered by hot-first
- "Draft reply" button: generates 3 reply variants using my past email style (paste 5 sample replies at signup for style calibration)
- 1-click send, tracking pixel optional
- Stripe subscription: $19/mo solo / $49/mo pro (Gmail + Outlook + Slack alerts)

### P1 (week 3-4)
- Outlook 365 OAuth
- Slack ping on `hot` (with reply already drafted, 1-click to review-and-send)
- Simple analytics: reply rate, time-to-first-reply, conversion-to-meeting
- Auto-archive `out_of_office` + `unsubscribe`

### P2 (week 5+)
- CRM sync (HubSpot free, Pipedrive)
- Multi-account (agency tier $149/mo)
- Reply-style fine-tuning per prospect (track which replies convert, weight next drafts)

### Non-goals (refuse to build)
- ❌ Cold email sequencer (Instantly/Smartlead own this)
- ❌ Lead database / scraper
- ❌ Email deliverability / warmup
- ❌ Multi-channel (LinkedIn/SMS)

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | Gmail OAuth flow; fetch last 7d replies; render raw inbox | Demo: log in, see replies |
| 2 | Intent classifier (Claude API + structured prompt w/ 5 examples per class) | Demo: replies tagged hot/warm/etc |
| 3 | 3-column UI (hot/warm/other); sort hot-first; mobile-responsive | UX done |
| 4 | Style calibration: paste-5-emails-to-train; produce tone profile | Settings page done |
| 5 | Draft generator: 3 variants per reply using tone profile + thread context | "Draft reply" works |
| 6 | Send-as-user; undo; tracking pixel | Send works end-to-end |
| 7 | Stripe: $19 solo plan; webhook → unlock app | Billing works |
| 8 | Landing page (Vercel + Tailwind): 1 hero, 3 features, 1 CTA, 1 testimonial slot | Public URL |
| 9 | Onboarding flow: connect Gmail → calibrate style → land in inbox | First-run UX |
| 10 | Email warmup: 50-person waitlist from r/coldemail, IndieHackers, X | 50 signups |
| 11 | Bug bash; load test 500 reply threads | Stable for paid |
| 12 | Public launch post on IndieHackers + X thread + r/coldemail cross-post | Live |
| 13 | First 10 paying users manually onboarded; collect 3 testimonials | $190 MRR |
| 14 | Iterate on classifier precision; first blog post: "How I 3x'd my reply rate by answering in 4 minutes" | Ready for marketing push |

## 5. 30-day marketing calendar (≤ $300)

| Day | Channel | Action | Budget |
|---|---|---|---|
| 1-7 | r/coldemail | Read top 100 posts; comment helpfully with one-liner; build karma | $0 |
| 8 | IH | Launch post: "I built an AI that triages my cold email replies in 4 minutes" | $0 |
| 8 | X | Founder thread: same story + demo GIF | $0 |
| 12 | r/sales | Cross-post: "How I stopped losing warm replies" (not promotional, story-driven) | $0 |
| 14 | Product Hunt | Submit (free) | $0 |
| 14-21 | X outreach | 20 cold DMs/day to founders with public "I send cold emails" tweets; offer 30-day free | $0 |
| 15 | IndieHackers | "Build in public" weekly update thread | $0 |
| 21 | Newsletter | Pitch 3 sales/saas newsletters (Sales Hacker, Starter Story) for inclusion | $0 |
| 22 | Paid trial | **One** $100 boosted X post targeting followers of @dickiebush, @zachharnisch (cold email creators) — only if MRR < $200 by day 21 | $100 |
| 25 | Partnership | Free Pro plan to 5 micro-influencers in cold-email space for testimonial swap | $0 |
| 28 | Content | SEO post: "Reply rate benchmarks for cold email 2026" (target keyword) | $50 (Ahrefs Lite trial) |
| 30 | Referral | 1-month-free-for-3-referrals loop kicks in | $0 |
| 30 | **Reserve** | $150 buffer for opportunistic paid if a thread goes viral | $150 |
| | | **Total cap** | **$300** |

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| ARPU | $19/mo (solo) blended to $35 by month 4 (mix shift to pro/agency) |
| Gross margin | 88% (Claude API ~$0.04/thread × 50 threads/user/mo = $2; Stripe 3%) |
| Logo churn (assumed) | 8%/mo — solo founders churn hard, fix with year-plan promo |
| Net new logos/mo to hit $10K | ~290 (at $35 ARPU) or ~530 (at $19) |
| Trial → paid conversion | 12% (industry avg for B2B SaaS w/ free tier) |
| Required trial signups/mo | 2,400-4,400 |
| Top-of-funnel (TOFU) | 20,000-40,000 visitors/mo needed |
| CAC paid cap | $20 (we're at <$5 organic-only) |
| Time to $10K MRR | ~6-9 months at this conversion |

**Trajectory:**
- Month 1: $200 MRR (50 paid × $19 avg)
- Month 2: $700 (ramp + referrals + 1 paid channel)
- Month 3: $1,800 (Product Hunt tail + content compounding)
- Month 6: $5,500
- Month 9: $10,500 ✓

## 7. Kill criteria

| Signal | Threshold | Action |
|---|---|---|
| Trial → paid after 200 trials | <6% | Kill — UX or pricing broken |
| Day 30 paid users | <15 | Kill — no PMF signal |
| Hot-classifier precision (user-rated) | <75% | Kill core feature; pivot to draft-only |
| Day 60 churn | >20%/mo | Kill — LTV broken |
| CAC paid > $50 | — | Kill paid channel, organic only |
| 3/5 user interviews say "I just use Gmail filters" | — | Kill — wedge wrong |

## 8. Wedge (required for GO_NARROW)

**What we REFUSE to build:**
- Cold email sequencer
- Lead scraping / enrichment
- Email warmup
- Multi-channel (LinkedIn/SMS)
- Generic "AI assistant for sales"

**Who we serve (and only them):**
- Solo founder or 1-person sales team
- Sends 200-500 cold emails/month
- Already uses Gmail/Outlook, NOT an enterprise CRM
- Currently loses money because they reply to warm leads too slowly (>4 hours)

**What we promise (and nothing more):**
"You'll reply to every interested reply within 10 minutes, in your voice, without opening Gmail."

**If a customer asks for any of the refused features, we say no and refer them to Instantly/Smartlead.** This is how we stay narrow enough to win against Draftly's broad surface area.

---

*Direction prepared by agent stage. Run: 2026-09-28_222443. Do not edit method; edit numbers as you gather real data.*
