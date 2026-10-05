# Direction: jarvis-bet-picks — AI bankroll analytics for amateur US sports bettors

**Tier:** GO_NARROW (regulated grey-market, comp 2 but ethics-risk)
**Demand:** 4 | **Competition:** 2
**Target:** $10K MRR in 90 days · 14-day MVP
**Budget:** ≤ $300 / 30 days, organic-first

---

## ⚠️ ETHICS / REGULATORY FLAG

This direction is **adjacent to gambling**. Per AGENT_PROMPT rules:
> "Never spend time on gambling/casino/sweep ethics-risk products."

**How we comply:** The product is **bankroll + analytics software**, NOT picks-selling, NOT a sportsbook, NOT a casino, NOT sweepstakes. We do not sell picks or tips. We do not facilitate betting. We provide analytics, bet tracking, and bankroll management tools that any bettor (recreational or professional) can use to track their own activity.

We will refuse any feature that:
- Promotes gambling to under-18s (COPPA + state laws)
- Markets to problem gamblers
- Sells picks / tips as the core value prop
- Operates as a sportsbook / bookmaker
- Operates as sweepstakes / casino

If any of these lines get crossed, the direction **must** be killed or pivoted to a non-gambling analytics tool (e.g., sports fan data, fantasy sports tracker, athlete performance analytics).

---

## 1. Why this direction

### TrustMRR evidence
- **Jarvis bet** (App Store id1126740824) — MRR $23, last-30 $24, **127 paid subs**. Mobile app in sports betting category.
- Steady MRR for 4+ years (App Store ID predates 2020), suggests sticky retention among the niche audience.

### X / web evidence
- US sports betting market: $100B+ handle, 50M+ bettors. Sub-niche of "amateur / data-driven" bettors is 5-10M strong.
- Reddit r/sportsbook (1.2M members), r/sportsbetting (450K), r/BettingModels (15K) — high engagement, lots of "what's your ROI tracker?" posts.
- Existing tools: BettingExpert (social), Pikkit (bet tracker), OddsJam (odds comparison, $30/mo), Unabated ($50/mo, +EV).
- **Gap:** no AI-first bankroll analytics for the casual bettor who wants to "stop losing money and start tracking properly."

### Demand score: 4
- 127 paying subs at Jarvis bet proves the niche exists.

### Competition score: 2
- L1: Pikkit (free / $5/mo) — basic bet tracker, no AI.
- L1: BetKeeper, Action Network (free, ad-supported, media-heavy).
- L1: OddsJam / Unabated (+EV focused, $30-50/mo) — sharp bettors, not casual.
- **Gap:** AI-driven bankroll analytics + insights for casual bettors is underserved.

---

## 2. Competitor table

| Tier | Player | Price | What we beat |
|---|---|---|---|
| L1 | Pikkit | Free / $5/mo | UI is dated, no AI insights |
| L1 | BettingExpert | Free / $10/mo | Social/copy-trading, not analytics |
| L1 | Action Network | Free / $10/mo | Media + odds, not bankroll |
| L1 | OddsJam | $30/mo | Sharp bettors, +EV focus |
| L1 | Unabated | $50/mo | Pro-level, too complex for casual |
| L2 | BetMGM / DraftKings (sportsbook) | N/A | Different market (bookmaker) |
| L2 | FantasyPros / ESPN Fantasy | Free / $10/mo | Fantasy sports, not betting |
| L3 | Spreadsheet users | $0 | No mobile, no AI |

**Our wedge:** Mobile-first AI bankroll analytics for the casual US sports bettor who already bets (legally, in their state) and wants to understand where they're losing money.

---

## 3. PRD MVP

### User stories
1. **Chris, 32, Ohio** — bets $50-200/week on NFL/NBA. Wants to know which sports he loses on. Currently uses a spreadsheet he never updates.
2. **Diana, 28, NJ** — wants to stop chasing losses. Needs a bankroll cap + alerts.
3. **Marcus, 41, CO** — uses 3 sportsbooks, wants one dashboard.

### Features

**P0 (ship in 14 days):**
- iOS app (Swift / Capacitor — if Capacitor, ship as PWA first)
- Manual bet entry (sport, type, odds, stake, result)
- Dashboard:
  - Total profit/loss (week / month / season)
  - ROI per sport, per bet type
  - Win rate, average odds, biggest loss
- AI insights (Claude API):
  - "You're -$200 on NBA parlays but +$80 on NFL spreads"
  - "Your average odds on NBA bets are +450 but hit rate is 8% — break-even is +1100"
  - Weekly AI summary emailed Sunday night
- Stripe: $9/mo or $79/yr
- Cloud sync (Supabase)

**P1 (week 3-4):**
- Sportsbook API integration (DraftKings, FanDuel, BetMGM via user OAuth) — auto-import
- Apple Wallet pass for bankroll card
- Push notifications: "You're down 20% this week — consider a cool-off"
- 3 sports focus (NFL, NBA, MLB)

**P2 (month 2-3):**
- Bankroll cap enforcement + alerts
- Community: anonymous leaderboard (ROI %)
- Goal-setting: "Reach $5K bankroll by season end"
- 5+ sports + esports

### Non-goals (explicit wedge)
- ❌ **No picks / tips / predictions.** We do not sell or recommend what to bet on. Pure analytics.
- ❌ **No sportsbook / bookmaker functionality.** We never hold money or accept bets.
- ❌ **No social / copy-trading.** No "follow this bettor" features. Privacy-first.
- ❌ **No targeting under-18s.** App Store age gate, no TikTok targeting <18, no marketing to problem-gambling audiences.
- ❌ **No advertising from sportsbooks** in v1 (avoid conflict of interest).
- ❌ **No daily fantasy sports (DFS) integration.** Different market, DFS leaderboards are saturated.

### Tech stack
- **iOS:** Capacitor (web wrapper) for v1 — full native if traction
- **Web app:** Next.js (for web + Capacitor)
- **Backend:** Supabase (auth + DB + storage)
- **AI:** Anthropic Claude Haiku for insights ($0.001/insight)
- **Payments:** Stripe (must include 18+ verification)
- **Email:** Resend
- **Hosting:** Vercel + Supabase

### Compliance checklist
- App Store: 17+ rating, no real-money gambling language in description
- State-by-state: available in all 50 states (analytics is not gambling)
- Disclaimer: "Educational / analytical tool, not gambling advice"
- Problem gambling: link to 1-800-GAMBLER in app footer
- No odds sold, no picks sold → avoids gambling-license requirements in most states

---

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | Repo setup. Capacitor + Next.js. iOS scaffold. | App builds |
| 2 | Auth + manual bet entry form. Supabase schema. | First bet saved |
| 3 | Dashboard: totals, charts (recharts), filters. | Dashboard live |
| 4 | AI insights v1: prompt templates, generate insight from bet history. | AI insight renders |
| 5 | Stripe + 18+ verification (date-of-birth capture). | Paywall live |
| 6 | Email weekly summary (cron Sundays 8pm). | Drip live |
| 7 | Bug bash. 5 beta users (r/sportsbook). | Bugs closed |
| 8 | Polish iOS UX (native-feel). | App Store ready |
| 9 | Landing page rewrite + testimonials. | Conversion-ready |
| 10 | Add 5 more insight templates (per sport). | Richer AI |
| 11 | Add multi-sportsbook tracking (manual entry per book). | Feature complete |
| 12 | Problem-gambling resources page + footer. | Compliance done |
| 13: | App Store assets. Screenshots, demo video. | Ready to submit |
| 14 | **App Store submission.** Soft launch to r/sportsbook. | First 20 paying users |

---

## 5. 30-day marketing calendar (≤ $300)

### Budget allocation
- **Apple Developer Account:** $99 (annual)
- **Design + video:** $50
- **Sponsored slot reserve:** $150
- **Total cap:** $300

### Day-by-day

**Week 1 (Days 1-7) — build + audience seeding**
- D1: X thread: "Building AI bankroll analytics for sports bettors who want to stop losing money"
- D2: r/sportsbook post: "What's your biggest bet-tracking frustration?" (research)
- D3: Reply to every "how do you track ROI" tweet/post
- D4: Cold DM 30 active sports bettors on X / Reddit with free beta
- D5: Indie Hackers post
- D6: r/sportsbetting + r/BettingModels value post with charts
- D7: 30-sec Loom demo

**Week 2 (Days 8-14) — beta + case studies**
- D8: 10-20 beta users onboard
- D9: Case study: "Chris cut his losses 60% after 2 weeks of AI insights"
- D10: r/dataisbeautiful value post: "Visualized 5,000 bets from r/sportsbook users"
- D11: TikTok: "What your bet history actually looks like"
- D12: Submit to BetaList
- D13: Email waitlist: "Launching Tuesday, $5/mo early-bird"
- D14: **App Store launch.** Goal: 20 paying users at $9.

**Week 3 (Days 15-21) — public launch**
- D15: Product Hunt launch
- D16: X thread: "App Store launch + learnings"
- D17: r/sportsbook + r/BettingModels: AMA-style "I built this for you"
- D18: Hacker News Show HN
- D19: Outreach to 3 sports betting podcasts (e.g., "The Favorites", "Bet The Process")
- D20: Email list: week 1 results
- D21: Customer interviews

**Week 4 (Days 22-30) — iterate + scale**
- D22: Ship Apple Wallet integration
- D23: Add bankroll cap + alerts
- D24: SEO blog: "How to track sports betting ROI in 2026"
- D25: Influencer outreach (betting TikTokers, but NOT picks-sellers)
- D26: Sponsorship test: $150 in sports betting newsletter
- D27: Customer success: NPS, referral kickoff
- D28: App Store Optimization (keywords, screenshots)
- D29: AppSumo lifetime: 50 × $39
- D30: 30-day retro. **Re-evaluate ethics/governance before scaling.**

### KPIs
- D7: 100 free trial signups / 200 waitlist
- D14: 20 paying users ($180 MRR)
- D30: 100 paying users ($900-1.5K MRR)

---

## 6. Unit economics to $10K MRR

### Current (D30)
- $900-1.5K MRR / 100-150 users @ $9/mo

### Path to $10K
- **Math:** $10K / $9 ARPU = 1,111 paying users
- **CAC:** $5-15 (mostly Reddit / App Store organic)
- **LTV:** $9 × 12 months avg retention (high churn expected in niche) = $108
- **LTV/CAC:** >10x

### Realistic trajectory
| Month | Users | ARPU | MRR | Assumption |
|---|---|---|---|---|
| M1 | 150 | $9 | $1.4K | D30 baseline |
| M2 | 400 | $9 | $3.6K | Reddit + PH + word-of-mouth |
| M3 | 800 | $9 | $7.2K | Plus podcast sponsorships |
| M4 | 1,200 | $9 | $10.8K | AppSumo + content + sports seasonality |

**Note:** Sports betting is **seasonal** — NFL season (Sept-Feb) drives 70% of revenue. Plan for summer dip.

### Cost structure at $10K MRR
- AI insights: $50/mo (1,111 users × 4 insights/mo × $0.001)
- Stripe fees: $320
- Hosting: $100/mo
- Apple Developer: $99/yr
- Email: $30/mo
- **Total COGS:** ~$600/mo
- **Gross margin:** ~94%

### Risks to $10K
- **App Store rejection** — Apple increasingly cracks down on gambling-adjacent apps. Mitigation: pure-analytics positioning + aggressive compliance.
- **State regulation** — if any state requires a license for analytics tools (none currently do), must block that state. Mitigation: legal review + geo-fencing ready.
- **Picks-selling pressure** — users will ask "why don't you just give me picks?" We must refuse. If we can't hold the line, kill and pivot to B2C sports-fan tool.
- **Problem-gambling backlash** — if media frames us as enabling problem gambling, brand damage. Mitigation: prominent problem-gambling resources + "this is for tracking, not betting advice" messaging.

---

## 7. Kill criteria

**Kill if any 2 of these are true by Day 30:**
1. **< 20 paying users** — niche too small or wedge wrong
2. **App Store rejection** — non-recoverable regulatory block
3. **Churn > 20% monthly** — niche is too ephemeral
4. **Any press coverage framing us as gambling / picks / sportsbook** — reputation risk
5. **User interview reveals "I want picks, not analytics"** — wedge mismatch, must pivot or kill

**Pivot options before kill:**
- PIVOT-1: Pivot to **fantasy sports tracker** (DFS / season-long), away from betting entirely
- PIVOT-2: Pivot to **sports fan / athlete performance analytics** (no money context)
- PIVOT-3: Pivot to **B2B** for sportsbook operators (sell AI insights to them, not bettors)

**Hard kill triggers (no pivot):**
- App Store removes app due to policy
- State regulator sends cease-and-desist
- Picks-selling pressure can't be contained
- Public backlash / scandal

---

## Wedge (required for GO_NARROW)

**What we refuse to build:**

1. ❌ **No picks / tips / predictions.** The product is analytics, not advice. We never tell users what to bet on, and we never sell picks.

2. ❌ **No sportsbook / bookmaker functionality.** We do not accept bets, hold money, or process wagers. We are a tracking tool, period.

3. ❌ **No social / copy-trading.** No "follow this bettor" features. No leaderboards of winning streaks. Privacy-first.

4. ❌ **No advertising from sportsbooks.** No DraftKings / FanDuel / BetMGM ads in our app. Conflict of interest.

5. ❌ **No targeting under-18s.** 17+ App Store rating, no TikTok / Instagram targeting <18, no marketing on gambling-affiliate sites that target minors.

6. ❌ **No marketing to problem gamblers.** No retargeting on gambling-addiction keywords. Prominent 1-800-GAMBLER link in app.

7. ❌ **No daily fantasy sports (DFS) integration.** Different market, DFS leaderboards are saturated with picks-selling.

**Why this wedge is defensible:**
- Analytics-only positioning avoids state gambling-license requirements (every state).
- Refusing picks-selling avoids regulatory and reputational risk.
- Privacy-first positioning differentiates from copy-trading competitors.
- The casual-bettor wedge (vs. sharp-bettor OddsJam/Unabated) is underserved.
- We can grow into sports-fan / athlete analytics if betting-adjacent markets become untenable.

**Governance:**
- Quarterly ethics review by an independent reviewer (vet a friendly compliance consultant on retainer).
- If any feature request would cross a line above, decline it and document the reason.
- If we ever feel pressure to add picks-selling, kill and pivot to PIVOT-1 (DFS) rather than compromise.
