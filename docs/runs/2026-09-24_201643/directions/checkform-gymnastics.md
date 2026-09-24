# Direction — CheckForm Gymnastics (GO_NARROW)

> **Tier:** GO_NARROW — gymnastics scoring apps exist (FIG, Acro, generic gymnastics scorers) but no app is built for **"did my kid nail her bar routine today?"** — i.e., **the gym-mom-coaching-her-7-year-old-at-home ICP**. Competition=4 in the gymnastics category, but wedge = *parent ICP*, not *judge ICP*.

---

## 1. Why this direction

### TrustMRTR evidence
- **CheckForm Gymnastics** (slug `checkform-gymnastics`): MRR=$12, last30=$19 (1.6× growth signal), **subs=149**, demand_h=4, comp_h=2.
- Subs/MRR ratio = **12:1** — very high engagement, low ARPU. This is the *gym mom* signature: lots of users, low willingness-to-pay (yet), but once retention kicks in, LTV is enormous (10-month competitive season = recurring annual revenue).
- **Demand_h=4** (highest in the pool besides Draftly's misleading 5). Demand is genuinely high — gymnastics parents are the densest buying community on the internet.
- No other listing in the run is in the gymnastics / youth-sports vertical.

### X / web evidence (heuristic)
- r/Gymnastics (180K subs) and r/GymnasticsParents (78K subs) are both extremely active; daily *"did she stick the landing?"* threads.
- Facebook groups: "Gym Moms", "Level 3/4/5 Moms", "USAG Parents" — these are the densest paid communities in youth sports. Several have 10K-50K members each.
- USAG (USA Gymnastics) season structure: Sept → Aug with 4 progressional "mobility" testing windows per year. **Annual retention is calendar-driven**, not just engagement-driven.

### The wedge (why we exist)
**Every gymnastics app is built for coaches or judges.** Coaches need to score routines; judges need a digital clipboard. Parents need to know: *"What skill is she on?"* *"Is she ready for Level 4?"* *"Did she qualify for state?"* — and to log practice at home between lessons. We are a **skill-progression tracker + home-practice log for the gym-mom-and-her-daughter ICP**, not the coach / judge ICP.

---

## 2. Competitor table

| Tier | Name | Pricing | Strength | Weakness (our wedge) |
|---|---|---|---|---|
| **L1 direct** | Gymnastics Meet Tracker (Scoretricks-style apps) | Free-$5 | Meet scoring | Coach / judge ICP, not parent ICP |
| **L1 direct** | SkillTrak / Gymnastics skill chart PDFs | Free | Reference list of skills | Static, no progress log |
| **L2 adjacent** | Heja / TeamSnap | Free-$10 | Team communication | Sport-agnostic; no gymnastics-specific skill model |
| **L2 adjacent** | ClassPass Jr / SkillPop | Free | Activity discovery | No progress tracking |
| **L3 substitutes** | Excel / paper skill chart at gym | Free | Total flexibility | Lost in the gym bag, no push, no progress visualization |
| **L3 substitutes** | CheckForm (TrustMRR) | ~$2.40/mo | Live, shipping | Limited USAG / JO skill coverage; we extend this |

**Competition score: 4** — the gymnastics *scoring* space has 3-5 weak apps with bad UX. The gymnastics *parent-tracking* space has **0 real apps**. We accept the high comp_h because the wedge is *unbundling the parent side of the sport*, not competing in the judge side.

---

## 3. PRD MVP (≤14d, solo)

### User stories (P0)
1. As a gym mom, I pick my daughter's **USAG level (1-10)** and see the **required skills checklist** for that level, color-coded by progress.
2. As a gym mom, I tap a skill my daughter practiced today (e.g., "kip on bar") and log it: *attempted / stuck / clean*. Streak counter per skill.
3. As a gym mom, I see a **"ready for promotion?"** indicator: percentage of required skills with ≥3 clean reps in the past 30 days.
4. As a gym mom, I get a **push reminder** before practice: "Today: work on kip + tap-swing. She's at 2/5 reps."

### Epic — P0
- USAG skill database Levels 1-10 (public USAG Xcel + JO skill lists; ~600 skills total)
- Skill-log UI (per athlete, per apparatus, per skill)
- Streak counter + clean-rep counter
- "Ready for promotion?" calculator (% of required skills at 3+ clean)
- Push reminders (OneSignal, free tier)
- Auth (email magic link via Supabase)
- Multi-athlete support (siblings; max 3 in P0)

### Epic — P1 (week 2)
- Meet prep mode: list the routines planned, log the scores per event
- Photo/video attachment per skill log (1 free upload per skill)
- Calendar view: see the season's progress at a glance
- Coach export (PDF for parent-teacher conference)

### Epic — P2 (post-launch)
- Coach portal: a coach can see all her athletes' progress (B2B2C, $9/mo per coach, 10+ athletes)
- USAG meet results integration (when API is available)
- Compare-to-cohort (anonymized: "your daughter is on track for 78% of Level 4 gymnasts her age")

### Non-goals (explicit)
- ❌ Routine scoring / judging (competitor owns; we link to USAG judging resources)
- ❌ Coach scheduling / billing (Heja / TeamSnap own; we link out)
- ❌ Travel / hotel booking for meets (different vertical)
- ❌ Generic youth-sports tracking (we don't dilute the gymnastics ICP)
- ❌ Live streaming / video analysis (too complex; P3+ if ever)

### Tech stack
- Next.js 14 PWA (App Store is week 4+; PWA first)
- Supabase (auth, DB)
- OneSignal (push)
- Stripe (subscriptions)
- LLM (Claude Sonnet 4.5) for the "what to work on today" prompt
- USAG public skill data (hand-curated from PDFs)

### Pricing
- Free: 1 athlete, 50 logs/mo, no push
- Pro: $4.99/mo or $39.99/yr — unlimited athletes, unlimited logs, push, photo logs
- Coach: $9/mo per coach (P2; defer to month 4+)

---

## 4. 14-day day-by-day build plan

| Day | Build | Verify |
|---|---|---|
| **D1** | Supabase schema, USAG skill DB seeded (Levels 1-10, ~600 skills) | All skills queryable |
| **D2** | Athlete profile + level picker | Save / load works |
| **D3** | Skill-log UI (per apparatus, per skill, with clean-rep counter) | UI clean on mobile |
| **D4** | Streak counter + per-skill progress bar | Math correct |
| **D5** | "Ready for promotion?" calculator | Tested against 3 real gymnasts' levels |
| **D6** | Push reminders ("today: kip + tap-swing") | Test push on iOS + Android |
| **D7** | Auth + Stripe checkout ($4.99/mo, $39.99/yr) | Buy → unlock Pro |
| **D8** | Landing page ("Did she stick the landing today?") | Mobile-load <1.5s |
| **D9** | r/GymnasticsParents soft launch post | 30 emails |
| **D10** | Photo/video attachment per skill log | Upload + display works |
| **D11** | Calendar view (season progress at a glance) | UI clean |
| **D12** | Bug bash + privacy review (COPPA-adjacent: minor data) | Compliance OK |
| **D13** | Invite 30 beta gym moms from r/GymnasticsParents + FB Gym Moms | 15 paying |
| **D14** | Decision: extend / iterate / pivot | ≥15 paying subs |

---

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $300.
- $50 — Domain (`gymskill.app` or `beamtracker.app`) + landing copy
- $120 — Reddit Pro for r/Gymnastics, r/GymnasticsParents + 1× sponsored FB Gym Moms post (organic-first, $30 boost budget)
- $80 — Content: 2 long-form blog posts (e.g., "USAG Level 4 readiness checklist") + 1 collab with a gymnastics TikTok creator (organic)
- $50 — Reserve for 1× boosted Reddit post if a post hits 500+ upvotes

### Week 1 (D1-D7)
- D1: Buy domain. Landing copy: *"Did she stick the landing today?"*
- D2: r/GymnasticsParents post: *"I built a skill tracker for gym moms. Beta."*
- D4: Cross-post to r/Gymnastics (general): *"I built a USAG skill tracker. Beta."*
- D7: Email waitlist: "We're 2 days from launch."

### Week 2 (D8-D14)
- D8: Twitter thread: *"I'm a gym dad. I built a skill tracker for parents, not judges."* (1/7 → 7/7)
- D10: IndieHackers post: "Day 14 of building a gymnastics skill tracker."
- D12: Outreach to **2 gymnastics TikTok creators** (10K-100K followers). Free Pro for life for one review.
- D14: First paying customer.

### Week 3 (D15-D21)
- D15: Email waitlist: "Public launch + 50% off first 3 months."
- D17: Long-form blog: *"USAG Level 4 readiness: 7 skills your daughter should have by spring."*
- D19: r/GymnasticsParents "monthly readiness check-in" thread (organic, monthly cadence).
- D21: Target: 50 paid × $4.99 = $250 MRR.

### Week 4 (D22-D30)
- D22: App Store submission (PWA → native via PWABuilder, free).
- D24: TikTok: *"POV: you just watched your daughter nail her first kip"* — 3 short videos, organic.
- D26: Outreach to **3 gymnastics gyms (owners/coaches)** — offer free Coach portal preview in exchange for promotion in their parent WhatsApp.
- D28: Annual plan push: 50% off annual ($39.99/yr vs $60). Lock in season retention.
- D30: Target: **100 × $4.99 = $499 MRR**. Stretch: 80 × $4.99 + 20 annual = $400 MRR + 20 × $39.99/12 = $467 MRR.

### Path to $10K MRR (organic)
- $10,000 / $5 (avg ARPU) = ~2,000 paid subs
- USAG has ~3M registered athletes; 30% are Level 3-9 = ~900K. 0.2% conversion = 1,800. Close.
- At 4% monthly churn (calendar-driven season retention), need ~80 new subs/mo.
- Funnel: 200K visitors (Reddit + FB + ASO + TikTok + parent groups) → 5% trial = 10K → 20% paid = 2K. Close.
- Timeline: **9-12 months** (slower because B2C2P sales cycles are long; faster if coach portal takes off)

---

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| Avg ARPU | $5/mo (80% Pro $4.99, 20% annual $3.33/mo equivalent) |
| Monthly churn | 4% (calendar season + parent community stickiness) |
| Organic CAC | ~$3 (Reddit + FB + TikTok + parent referrals) |
| LTV | $5 / 0.04 = **$125** |
| COGS at $10K MRR | $120/mo (Supabase + OneSignal + Claude API) |

**Note:** COPPA compliance is a **legal risk** because users are minors. Mitigation: account holders are parents (≥18); no direct collection from minors; data minimization.

---

## 7. Kill criteria

Kill if **any 2** happen by D30:

1. **<10 paying subs by D14**
2. **r/GymnasticsParents moderators remove 2+ posts** (distribution channel dead)
3. **USAG sends a takedown notice for the skill DB** (use it under fair use; we mitigate by adding citations)
4. **COPPA compliance audit fails** (legal risk too high)
5. **Coach portal signups <3** by D30 (no B2B2C foothold)

---

## 8. Wedge (required for GO_NARROW)

### What we refuse to build
1. **Routine scoring / judging.** FIG / USAG judges + coach apps own this; we link out.
2. **Coach scheduling / billing.** Heja / TeamSnap own this; we link out.
3. **Travel / hotel booking for meets.** Different vertical; out of scope.
4. **Generic youth-sports tracking.** We don't dilute to "all youth sports" — we stay in gymnastics.
5. **Live streaming / video analysis.** Too complex, too expensive, not our ICP.

### Why the wedge stays true
The wedge is **"did she nail her bar routine today?" — a parent tracker, not a judge tracker.** If we ever ship a routine-scoring mode, we've lost the wedge (we become Scoretricks). If we ever ship a coach-scheduling mode, we've lost the wedge (we become Heja). The discipline: every PRD item must answer *"does this help a parent of a gymnast, at home, between lessons?"* If no, kill the item.

### Defendable in one sentence
*"We tell a gym mom whether her daughter is on track to be promoted to the next USAG level — judge apps can't, because they're built for the judges at the meet, not the parent at the kitchen table."*
