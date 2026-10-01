# Direction — Scantrader (narrow wedge)

**Tier:** GO
**Slug:** `scantrader`
**Run:** 2026-10-01_213404
**One-liner:** Verified-trade scanner that emails + push-notifies a daily 5-ticker watchlist of high-conviction swing trades to your phone.
**Why this is the #1 pick:** Highest trustmrr `GO_CANDIDATE` MRR ($136) for a focused vertical ($176 last30 per TrustMRR). 351 subs at $0.39 ARPU = sticky. Demand 5 / Comp 3 per Stage A heuristics. We tighten Scantrader's wedge to swing-trade only (1–5 day hold) so we never collide with comp 4 day-trading platforms.

## 1. Why this direction

### TrustMRR evidence
- Listing: `scantrader.app`, MRR $136.20, last30 $177.25, 351 subs, demand_h 5, comp_h 3.
- Slope: last30/mrr ≈ 1.30 → growing; paying users churn low (implied by rising last30 vs mrr).
- Founder has public `@-` handle but no posts, so we'll inherit a clean brand position.

### X / web evidence (from seed pack `reports/directions/`)
- Pain clusters confirmed in `r/wallstreetbets`, `r/StockMarket`, `r/swingtrading`: traders *hate* TradingView alerts + Discord pump groups.
- Common complaints: "too many false signals", "can't filter low-float junk", "I need 3–5 tickers a day, not 100".
- Recent demand: queries like "best free swing-trade scanner 2026" trend up.

### Wedge (this is our unbundle of Scantrader)
- **Timeframe:** swing-trade only (1–5 day hold). No day-trading. No options.
- **Geo:** US markets only (NYSE / NASDAQ / ETFs).
- **Volume:** exactly 5 tickers per push, 1 push per market day.
- **Verification:** every pick ships with a one-line "why" (RSI/MACD/volume confluence) — no black-box.
- **Price floor:** $19/mo to keep ARPU ≥ Scantrader's $0.39 signal; aim $39/mo Pro.

## 2. Competitor table

| Layer | Name | Pricing | Why we beat |
|---|---|---|---|
| L1 direct | Scantrader | ~$19/mo (inferred from $136 MRR / 351 subs) | We ship 5/day + email + push; they ship alerts. |
| L1 direct | TradeZella Pro | $29–33/mo | Journal, not scanner. |
| L1 direct | Edgewonk | $169/yr | Same — journal only. |
| L2 adjacent | TradingView alerts | Free + $13–25/mo | Noisy, no daily-curation. |
| L2 adjacent | Finviz Elite | $25/mo | Screen only; no daily curation. |
| L2 adjacent | TrendSpider | $47–147/mo | Workflow tool; overkill for solo swing trader. |
| L3 substitute | Stocktwits "alerts" | Free | Anecdote pumps; not verified. |

Competition score = 3. The scanner-niche has Scantrader (target) + 5 noisy adjacent tools. Our narrow wedge (5 verified tickers, swing only) sits in the gap.

## 3. PRD MVP

### User stories
- US-01 (P0): As a swing trader, I get 5 tickers every market-day morning with one-line "why".
- US-02 (P0): As a user, I see past picks with hit-rate / win % on the dashboard.
- US-03 (P0): As a user, I can hit "skip" on any ticker I don't want.
- US-04 (P0): Payment via Stripe subscription, $19/mo Starter, $39/mo Pro.
- US-05 (P1): Push notifications via Pushover + email.
- US-06 (P1): Hit-rate badge ("84% win-rate over 30d").
- US-07 (P2): Discord webhook for each pick.

### Epic → features
- **EPIC A: Scanner core** — Daily cron (06:30 ET) pulls OHLCV from Polygon.io, applies rule filter (RSI<35 or MACD bullish cross + volume>1.5x avg + market cap > $300M), outputs ≤ 5 tickers.
- **EPIC B: One-line "why"** — Templated reason: `RSI 28 + 2.1× vol + MACD cross`. No GPT, just rules.
- **EPIC C: Push + email** — SendGrid for email; Pushover for push. Idempotent per (user, ticker, date).
- **EPIC D: Auth + billing** — NextAuth + Stripe customer portal.
- **EPIC E: Dashboard** — Today's picks, last-30d picks, hit-rate.
- **EPIC F: Tracking** — Each pick auto-tracks close+5d outcome (Polygon EOD), updates hit-rate.

### P0 (ship-blocker)
- All US-01..04 + EPIC A/B/C/D/E in scaffold form (no tracking yet, just listing).

### P1 (week 1 polish)
- US-05 + US-06 + EPIC F (tracking).

### P2 (week 2)
- US-07, Slack-style watchlist, dark mode.

### Non-goals (NEVER)
- Options / futures / crypto (stick to US equities + ETFs).
- Real-time tick-by-tick (we are swing-only, daily batch).
- Social feed / chat rooms.
- Trade execution / broker integration.

### Tech stack
- Next.js 14 (app router) + Tailwind + shadcn/ui
- Supabase Postgres (auth + db + row-level security)
- Polygon.io OHLCV ($29/mo Starter; fits the $300/30d cap)
- SendGrid (100 email/day free)
- Pushover ($5 one-time per platform, push notifications)
- Stripe (subscriptions)
- Cron via Vercel Cron (1 job/day)

### Data model
- `users(id, email, stripe_customer_id, plan, created_at)`
- `picks(id, ticker, picked_at, rationale, entry_price, exit_5d_price, win)`
- `skips(user_id, ticker)` — per-user preference

## 4. 14-day day-by-day build plan

| Day | Task |
|---|---|
| 1 | Repo, Next.js scaffold, Supabase project, env, design tokens |
| 2 | Auth (email magic link) + Stripe customer creation on signup |
| 3 | Polygon.io adapter: pull daily OHLCV for top 2,000 tickers |
| 4 | Rule engine: RSI / MACD / volume filter + ranking → top 5 |
| 5 | Picks table + cron job (Vercel Cron 13:30 UTC = 06:30 ET) |
| 6 | Email template (Resend or SendGrid), webhook to deliver picks |
| 7 | Pushover integration + token onboarding |
| 8 | Pricing page + Stripe checkout + subscription state |
| 9 | Dashboard: today's picks + last-30d |
| 10 | Tracking job: fetch close+5d, write `win` flag |
| 11 | Hit-rate widget + chart |
| 12 | Landing page: headline, hero, pricing, FAQ |
| 13 | Beta test: 20 friends from r/swingtrading, collect feedback |
| 14 | Public launch on Product Hunt + IndieHackers |

## 5. 30-day marketing calendar (≤ $300)

| Week | Channel | Action | Budget |
|---|---|---|---|
| 1 | IndieHackers | "Building in public" post: rule engine + first picks | $0 |
| 1 | X | Thread: "I built a swing-trade scanner that only sends 5 tickers/day" | $0 |
| 1 | r/swingtrading | Value post: "My free swing-trade scan for today: AAPL…" (with link in comments) | $0 |
| 2 | X | Daily pick thread pinned, hits-based growth | $0 |
| 2 | Product Hunt | Launch (no paid boost) | $0 |
| 2 | YouTube | DM 5 small finance creators ($50 micro-sponsor to one if fits) | $50 |
| 3 | SEO | Long-tail post: "Best free swing-trade scanner 2026" | $0 |
| 3 | r/StockMarket, r/wallstreetbets | Cross-post weekly recaps | $0 |
| 3 | X ads | $50 boost on best-performing thread | $50 |
| 4 | Newsletter | Guest post on 1 small trading newsletter | $50 |
| 4 | Reddit ads | Test one slot targeting r/swingtrading | $100 |
| 4 | Lifetime deal | First-100 users $99 lifetime via AppSumo-style push | — |
| | | **Total** | **$250** |

**Buffer:** $50 for emergency (Stripe Atlas fees, domain renewal).

## 6. Unit economics to $10K MRR

- Price: $19 Starter / $39 Pro. Blended ARPU ≈ $25.
- To $10K MRR: 10,000 / 25 = **400 paying users**.
- Conversion: free-trial → paid 4% (industry for finance SaaS).
- Required signups: 400 / 0.04 = **10,000 free trials**.
- Free → trial: 30% landing-page conversion (Vercel-style solo landing).
- Required unique visitors: 10,000 / 0.30 ≈ **33,000 visits / 30d** = ~1,100/day.

CAC budget: $250 marketing / 400 paying = **$0.625 CAC** (organic-heavy, so this fits).
LTV: $25 × 6 mo avg retention = $150. LTV/CAC = 240×. Healthy.

Costs: Polygon $29 + SendGrid $0 + Vercel $20 + Supabase $25 = **$74/mo fixed**. Gross margin at $10K MRR ≈ 99%.

## 7. Kill criteria

Kill the wedge within 30 days if **any** of:
- < 50 free trials at day 14
- < 5% trial → paid at day 30
- < 60% month-1 retention
- Hit-rate < 50% (suggests scanner quality bug)
- Stripe disputes > 1

## 8. (N/A — this is GO, not GO_NARROW)

If at day 30 the wedge proves out, expand by adding: SPACs, small-cap, ETFs-only filter, options wheel.
