# Direction: Publbee-Narrow — Indie Newsletter AI Localization (2-4 langs)

**Slug:** `publbee-narrow`
**Tier:** GO_NARROW
**Run:** 2026-09-28_222443
**Target:** $10K MRR · 14d MVP · ≤$300/30d marketing

---

## 1. Why this direction

**TrustMRR evidence:**
- Publbee: $31 MRR, $29 last30, 91 subs. Steady, small, real.
- Cluster: `other` — long-tail. Publbee specifically is newsletter/content localization, not generic translation.

**X/web evidence:**
- Indie newsletter operators (substack, beehiiv) repeatedly tweet: *"I want to translate my newsletter into Spanish/French/Japanese but DeepL + manual copy-paste is killing me. Beehiiv doesn't localize. Substack doesn't localize."*
- Pain quote (synthesized): *"I have 8K subs, 30% would read in Spanish if I translated, but every translation costs me 2 hours and breaks my voice."*
- Existing solutions: DeepL API (raw, no newsletter context), Lokalise (enterprise, $$$), ChatGPT-paste (DIY mess). No indie-tool for newsletter specifically.

**Why the wedge works:**
Publbee proves the market exists at $31 MRR. But "translation/localization" is a huge surface (apps, websites, games, etc.). We narrow to: **solo newsletter writers, 2-4 languages, tone-preserving AI translation with one-click publish to Substack/Beehiiv**. This slice has zero incumbent.

## 2. Competitor table

| Tier | Name | What they do | Price | Threat |
|---|---|---|---|---|
| **L1 direct** | Publbee (the listing) | Generic content localization | €15-40/mo | Med — broader surface, slower focus |
| **L1 direct** | Lokalise / Crowdin | Enterprise localization platform | $80+/mo | High on enterprise; Low on indie |
| **L2 adjacent** | DeepL API + Zapier | DIY translation pipeline | $25/mo + setup time | Med — too technical for indie writers |
| **L2 adjacent** | ChatGPT-paste workflow | Manual | $20/mo | **High** — this is the real enemy; indie writers will DIY for free |
| **L2 adjacent** | Beehiiv / Substack native | No localization | included | Low (no solution) |
| **L3 substitute** | Hire translator on Fiverr | $0.05-0.20/word | — | High (entry tier) |

**Competition score: 3** — Publbee is the L1, not strong, not focused. The bigger threat is the manual DIY workflow. Wedge is "less than 5 minutes per newsletter, in your voice, published to Substack/Beehiiv directly."

## 3. PRD MVP

### P0 (must-ship Day 14)
- Connect Substack OR Beehiiv (OAuth or RSS-pull)
- Paste newsletter draft (or sync latest draft)
- Pick target languages (max 4 at MVP)
- AI translates preserving: your voice (paste 3 past issues as calibration), formatting, links, footnotes
- Side-by-side preview + 1-click publish to each locale (creates new substack publication OR beehiiv segment)
- Stripe: $19/mo solo (2 langs, 1 newsletter) / $49/mo pro (4 langs, 3 newsletters)

### P1 (week 3-4)
- Ghost integration
- Tone presets (formal, casual, technical) + override per-language
- Translation memory (your past translations inform future ones)
- Analytics: open rates by language, which locales are growing

### P2 (week 5+)
- Revenue share with translators for languages where AI tone is weak (e.g., literary Japanese)
- Co-marketing: "Get more readers" plug into partner newsletters

### Non-goals (WEDGE — refuse to build these)
- ❌ Generic website/app localization
- ❌ Enterprise translation management
- ❌ Human translator marketplace (we AI-only at MVP)
- ❌ More than 4 languages
- ❌ Non-newsletter content (blogs, docs, videos)
- ❌ Substack/Beehiiv as publishers — we integrate, not replace

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | Substack OAuth + RSS pull of latest issue | Substack connect works |
| 2 | Tone calibration: paste 3 issues → extract voice profile | Calibration works |
| 3 | AI translator (Claude API): voice-preserving, format-preserving | Translation works |
| 4 | Side-by-side preview UI; locale selector | UX done |
| 5 | Publish to Substack (new publication per locale) | Publish works |
| 6 | Beehiiv integration (segment-based locale publish) | Beehiiv connect works |
| 7 | Stripe wiring; paywall on >2 locales | Billing done |
| 8 | Landing page: 1 hero, before/after sample, 1 CTA | Public URL |
| 9 | Onboarding: connect → calibrate → translate → publish | First-run UX |
| 10 | Outreach: 20 indie newsletters on X offering free 30-day Pro in exchange for honest tweet | 20 signups |
| 11 | Bug bash; test 10 newsletters end-to-end | Stable |
| 12 | IndieHackers launch post + X thread | Live |
| 13 | First 15 paid; 3 testimonials | $285-735 MRR |
| 14 | Iterate AI quality for French/Spanish (most common pairs) | Loop |

## 5. 30-day marketing calendar (≤ $300)

| Day | Channel | Action | Budget |
|---|---|---|---|
| 1-5 | X | DM 50 indie newsletter writers (substack 1k-20k subs) offering free Pro + tweet | $0 |
| 7 | IndieHackers | Launch post: "I built a tool that translates my newsletter into 3 languages in 4 minutes" | $0 |
| 8 | Substack | Cross-post in 5 newsletter-writer communities | $0 |
| 10 | r/Newsletter | Launch post | $0 |
| 12 | Product Hunt | Submit | $0 |
| 14 | Beehiiv newsletter | Pitch "tool of choice" mention (1 free Pro year) | $0 |
| 18 | X | Founder thread: "I translated my 5K-sub newsletter into Spanish — here's what happened to growth" | $0 |
| 21 | Paid | **One** $100 X ad targeting "substack OR beehiiv" followers IF MRR > $400 by day 21 | $100 |
| 24 | Partnership | Free Pro to 10 newsletter creators with bilingual audiences | $0 |
| 28 | SEO | "Best AI translator for newsletters", "Substack multi-language" | $0 |
| 30 | Referral | 1-month-free-for-1-referral loop | $0 |
| | | **Buffer** | $200 |
| | | **Total cap** | **$300** |

## 6. Unit economics to $10K MRR

| Metric | Value |
|---|---|
| ARPU | $29/mo blended (heavy $19, some $49 pro) |
| Gross margin | 87% (Claude API ~$0.10/issue × 4 issues/mo × 3 langs = $1.20; Stripe 3%) |
| Logo churn | 7%/mo (newsletter writers are sticky once set up) |
| Net new paid/mo for $10K | ~400 |
| Free → paid | 8% (high intent; paid newsletter writers are B2B-ish) |
| Required trials/mo | 5,000 |
| TOFU visitors/mo | 25,000 (X DMs + IH + Reddit) |
| CAC paid cap | $15 |
| Time to $10K MRR | 6-9 months |

**Trajectory:**
- Month 1: $400 (X DM wave + IH launch)
- Month 2: $1,200 (Product Hunt + content)
- Month 3: $2,500 (referral compounding)
- Month 6: $6,500
- Month 9: $10,200 ✓

## 7. Kill criteria

| Signal | Threshold | Action |
|---|---|---|
| Day 14 paid users | <10 | Kill — no willingness to pay |
| Day 30 MRR | <$300 | Kill — niche too narrow |
| Trial → paid after 200 trials | <6% | Kill — UX or AI quality broken |
| Day 60 churn | >15%/mo | Kill — LTV broken |
| Substack ships native localization | — | Pivot to translation memory / ghostwriters marketplace |
| 3+ indie writers say "DeepL is good enough" | — | Re-examine AI quality bar |
| Beehiiv / Substack / Ghost cut API access | — | Kill (no workaround exists) |

## 8. Wedge (required for GO_NARROW)

**What we REFUSE to build:**
- ❌ Generic website localization
- ❌ App / game localization
- ❌ Enterprise translation management
- ❌ Human translator marketplace
- ❌ More than 4 languages at MVP
- ❌ Non-newsletter content types (blogs, docs, videos)
- ❌ Becoming a publishing platform (we integrate; we don't replace Substack/Beehiiv)

**Who we serve (and only them):**
- Solo or 2-person newsletter team
- Already publishing in English, ≥1,000 subscribers
- Wants to publish to 2-4 additional languages
- Currently doing manual DeepL/ChatGPT + copy-paste
- Voice matters to them (they have a recognizable style)

**What we promise (and nothing more):**
"You'll publish to 4 languages in 4 minutes, in your voice, without leaving Substack."

**Why the wedge is non-negotiable:**
The competition score is 3, not 2. The full market ("localization tooling") is owned by Lokalise, Crowdin, Smartling — billion-dollar players. If we build a generic localization tool, we lose. The newsletter-only, ≤4-langs, voice-preserving, direct-publish wedge is the only slice where a solo founder can win against Publbee and DIY workflows.

If a customer asks for any refused feature, we say no and refer them to Lokalise/Crowdin.

---

*Direction prepared by agent stage. Run: 2026-09-28_222443.*
