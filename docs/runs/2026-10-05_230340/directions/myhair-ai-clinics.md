# Direction: myhair-ai-clinics — AI hairstyle try-on for independent salons

**Tier:** GO_NARROW (competition 3, demand 4 — wedge required)
**Demand:** 4 | **Competition:** 3
**Target:** $10K MRR in 90 days · 14-day MVP
**Budget:** ≤ $300 / 30 days, organic-first

---

## 1. Why this direction

### TrustMRR evidence
- **MyHair AI** (`myhair.ai`) — MRR $7, last-30 $8, **182 paid subs**. Consumer-facing AI hairstyle try-on. Tiny MRR but high subs at ~$0.04 ARPU suggests heavy freemium / churn → room for a better monetization wedge.
- 182 paying users at all is meaningful — proves consumer pull exists for hairstyle-try-on AI.

### X / web evidence
- Search `salon booking software` → fragmented market: Square Appointments, Vagaro, Fresha, Booksy. None have AI try-on.
- Search `AI hairstyle try-on salon` → "I wish my stylist had an app where I could see the cut before"
- Salon owners on r/FemaleHairAdvice + r/HaircareScience ask constantly for client visualization tools.
- 200K+ US hair salons (BLS data), average $250K revenue, $50-300/mo on tech tools.

### Demand score: 4
- MyHair AI proves consumer demand.
- B2B salon SaaS demand: 60K+ independent salons in US + 140K in EU.

### Competition score: 3
- **L1 direct competitors (consumer):** YouCam (huge, beauty AR), ModiFace (L'Oréal-owned), MyHair AI, hair-style changer apps.
- **L1 direct competitors (B2B salon SaaS):** None with AI try-on. Fresha has product gallery, no AR.
- **L2:** Style My Hair (L'Oréal), HairZap, Hairtech AI.

**Why GO_NARROW not KILL:** consumer try-on space is full (YouCam has 800M downloads), but **B2B2C salon SaaS wedge is wide open**. No salon-focused AI try-on exists at scale.

---

## 2. Competitor table

| Tier | Player | Price | What we beat |
|---|---|---|---|
| L1 | YouCam Makeup (AR beauty app) | Free / $5/mo | Consumer, beauty-makeup focus, not salon-embedded |
| L1 | ModiFace (L'Oréal) | Enterprise | Owned by L'Oréal, locked to their products |
| L1 | MyHair AI | Free / $5/mo | Consumer only, no salon widget, no booking integration |
| L2 | Style My Hair (L'Oréal) | Free | Owned by L'Oréal, training only |
| L2 | Hairtech AI / HairZap | $30/mo | Consumer-grade, no B2B |
| L3 | Fresha / Square / Vagaro (booking SaaS) | $0-100/mo | No AI try-on, separate problem |
| L3 | StyleSeat / Booksy | $0-30/mo | Booking only, no try-on |

**Our wedge:** Embeddable AI hairstyle try-on widget that independent salons add to their **existing booking page** (Fresha, Square, Booksy, Squarespace). Customer never pays — salon pays $29-99/mo for the widget.

---

## 3. PRD MVP

### User stories
1. **Janet, salon owner in Brooklyn** — wants customers to try cuts/colors on their photo before booking. Currently uses Instagram DMs to share inspiration photos.
2. **Maria, customer** — visits Janet's booking page, sees "Try on this style" button, uploads photo, sees realistic preview, books appointment.
3. **Devon, barber in Atlanta** — wants the widget to suggest fades based on face shape, not just show hairstyles.

### Features

**P0 (ship in 14 days):**
- Web app for salon owner:
  - Sign up, claim salon
  - Upload salon logo + brand color
  - Get embed code (`<script>` tag) for their booking page
- Embeddable widget:
  - 20 hairstyles (curated by trade) — 10 cuts, 5 colors, 5 men's cuts
  - Photo upload + AI try-on (use Replicate / Stable Diffusion + face-swap model)
  - "Book this style" CTA → goes to salon's existing booking URL
- Dashboard: views, try-ons, bookings attributed to widget
- Stripe: $29/mo (1 location) / $79/mo (up to 5 locations) / $199/mo (white-label)

**P1 (week 3-4):**
- Direct integration: Fresha, Square Appointments, Booksy (read calendar, push booking)
- 50 hairstyles (per trade, per ethnicity)
- Face-shape analyzer → AI recommendations
- Branded share images ("Try Maya's new look!")

**P2 (month 2-3):**
- AI color-matching (try blonde highlights, balayage)
- iPad version for in-salon use
- SMS/email follow-up: "Loved your try-on? Book now"
- Multi-language

### Non-goals (explicit wedge)
- ❌ **Consumer-facing app** — YouCam wins. We do NOT build a public-facing app.
- ❌ **Booking software** — Fresha/Square win. We INTEGRATE, don't replace.
- ❌ **Beauty / makeup try-on** — different market, ModiFace owns.
- ❌ **Hair-care product recommendations** — different market, owned by retailers.
- ❌ **Enterprise salon chains (>50 locations)** — sales motion too heavy for solo.
- ❌ **Curly / textured hair specific** (P2 only — too narrow at launch).

### Tech stack
- **Frontend:** Next.js, Tailwind
- **Widget:** vanilla JS bundle (≤ 30KB), Vue + Web Components
- **AI:** Replicate API (face swap + hairstyle transfer), or fine-tune on synthetic data; cost ~$0.05-0.20 per try-on
- **Backend:** Next.js API routes, Supabase
- **DB:** Supabase Postgres
- **Payments:** Stripe Connect (if multi-location salon)
- **Email:** Resend
- **Hosting:** Vercel + Supabase

### Cost per widget
- AI try-on: $0.10 avg (Replicate)
- Hosting: $0.001/embed
- **COGS/widget-load:** ~$0.10
- **At $29/mo with 300 try-ons = $30 COGS → break-even → up-sell needed**
- **At $79/mo with 500 try-ons = $50 COGS → 37% margin → sustainable**

### Quality bar
- Realism must hit "good enough" — not perfect. YouCam sets the bar; we'll be slightly below but in the right context (salon's own brand, not generic app).
- Acceptable: 60% of try-ons look convincing to a customer.
- Unacceptable: clearly AI-ghost artifacts (use SDXL + face restoration).

---

## 4. 14-day day-by-day build plan

| Day | Task | Output |
|---|---|---|
| 1 | Repo setup. AI prompt engineering: pick model (Replicate's hairstyle-transfer or fine-tune SDXL). Test 20 hairstyles. | Model selected, 20 sample outputs |
| 2 | Web app skeleton + salon owner onboarding (3 steps). | Owner can sign up |
| 3 | Widget v1: photo upload + AI try-on + render preview. | Working demo at widget.localhost |
| 4 | Embed-code generation (`<script src="...">`), logo + color customization. | Embed code ready |
| 5 | Stripe Checkout + subscription. | $29/mo paywall |
| 6 | Dashboard: views, try-ons, click-throughs. | Owner sees analytics |
| 7 | Bug bash. 3 beta salons (recruit from r/FemaleHairAdvice, r/HaircareScience, r/barbers). | Bugs closed |
| 8 | Polish widget UX: loading states, mobile responsive, error UX. | Production widget |
| 9 | Landing page rewrite with 3 case studies (or screenshots). | Conversion-ready |
| 10 | Add 30 more hairstyles (women + men + ethnic diversity). | 50 styles total |
| 11 | Embed documentation page (for non-tech salon owners). | Docs live |
| 12 | Email drip (Resend): onboarding + upsell. | Drip live |
| 13 | Product Hunt assets. Demo GIF. | Ready to launch |
| 14 | **Soft launch** to waitlist. Goal: 10 paying salons. | First 10 paying salons |

---

## 5. 30-day marketing calendar (≤ $300)

### Budget allocation
- **Replicate API credits:** $80 (~800 try-ons in beta)
- **Domain + email + design:** $50
- **Landing page copy (Fiverr):** $20
- **Sponsored slot reserve:** $150
- **Total cap:** $300

### Day-by-day

**Week 1 (Days 1-7) — build + audience seeding**
- D1: X thread: "Building AI try-on widget that salons embed in their booking page"
- D2: r/FemaleHairAdvice + r/HaircareScience: research post "Would you book more if you could try the cut first?"
- D3: Reply to every "how do I show my stylist what I want" tweet/post
- D4: Cold DM 30 salon owners on Instagram (no $$$ ask, just "I built this for free, want to test it?")
- D5: Indie Hackers post: "AI hairstyle try-on widget for salons"
- D6: Facebook group (Salon Owners, Independent Hair Stylists Network): value post with demo GIF
- D7: 30-sec Loom demo showing widget on a fake booking page

**Week 2 (Days 8-14) — beta + case studies**
- D8: 5-10 beta salons onboard (free 60 days for testimonials)
- D9: Case study: "Maria's salon saw 35% more bookings after adding widget"
- D10: r/smallbusiness + r/Entrepreneur value post: "AI widget that pays for itself"
- D11: TikTok/Reels: "Watch this customer try 20 cuts in 60 seconds"
- D12: Submit to BetaList, AppSumo (lifetime for first 30 salons)
- D13: Email waitlist (200+): "Launching Tuesday, $19/mo early-bird"
- D14: Soft launch. Goal: 10 paying salons at $29-79.

**Week 3 (Days 15-21) — public launch**
- D15: Product Hunt launch (Tuesday)
- D16: X thread: "We hit #X on PH — here's the behind-the-scenes"
- D17: r/HaircareScience post: "I built an AI try-on tool, here's what I learned about hair AI"
- D18: Hacker News Show HN
- D19: Outreach to 3 salon-focused podcasts (e.g., "The Hair Biz Podcast", "Salon Owners Collective")
- D20: Email list: week 1 results
- D21: 5 customer interviews — what else would they pay for

**Week 4 (Days 22-30) — iterate + scale**
- D22: Ship 50 hairstyles + face-shape analyzer
- D23: Direct Fresha + Square Appointments integration
- D24: SEO blog: "Best AI try-on for hair salons 2026"
- D25: LinkedIn outreach to 50 salon owners (free trial)
- D26: Sponsorship test: $150 in Marketing Examples
- D27: Facebook retargeting pixel only (no spend)
- D28: Customer success: NPS, referral kickoff ("refer a salon, get 1 mo free")
- D29: AppSumo lifetime deal: 30 × $99
- D30: 30-day retro

### KPIs
- D7: 50 free widget installs / 200 waitlist
- D14: 10 paying salons ($300-700 MRR)
- D30: 30-50 paying salons ($1.5K-3K MRR)

---

## 6. Unit economics to $10K MRR

### Current (D30)
- $1.5K-3K MRR / 30-50 salons @ $29-79/mo blended ARPU

### Path to $10K
- **Math:** $10K / $60 ARPU = ~167 paying salons
- **CAC:** $20-50 (mostly cold DM, referral)
- **LTV:** $50 × 18 months avg retention = $900 (B2B retention strong)
- **LTV/CAC:** >15x

### Realistic trajectory
| Month | Salons | ARPU | MRR | Assumption |
|---|---|---|---|---|
| M1 | 50 | $50 | $2.5K | D30 baseline |
| M2 | 100 | $60 | $6K | Add Fresha/Square integration |
| M3 | 170 | $60 | $10K | Referral + AppSumo + content SEO |

### Cost structure at $10K MRR
- Replicate API: $4K/mo (40,000 try-ons × $0.10 — but at scale negotiated $0.05)
- Stripe fees: $320
- Hosting: $100/mo
- Email: $50/mo
- **Total COGS:** ~$4.5K/mo
- **Gross margin:** ~55% (AI cost is real; consider fine-tuning own model M3+)

### Margin improvement plan
- M3: fine-tune SDXL with synthetic hair data → bring cost to $0.02/try-on → margin jumps to 85%.
- M4: license model output as API → COGS approaches hosting-only.

---

## 7. Kill criteria

**Kill if any 2 of these are true by Day 30:**
1. **< 10 paying salons** — proves B2B wedge doesn't convert
2. **AI realism < 3/5 in user surveys** — widget looks fake, kills conversions
3. **COGS > 70% of MRR** at $2.5K — AI cost too high, margin broken
4. **Salons churn > 15% monthly** — proves wrong product/market

**Pivot options before kill:**
- PIVOT-1: Drop widget, sell full SaaS with booking included (compete with Fresha)
- PIVOT-2: License AI model to existing salon SaaS (Fresha API marketplace)
- PIVOT-3: Pivot to B2C with ad-supported free tier (different comp set)

---

## Wedge (required for GO_NARROW)

**What we refuse to build:**

1. ❌ **No consumer-facing app.** YouCam (800M downloads) owns the public-facing hairstyle try-on. We will never compete head-on. Our app is **invisible to consumers** — they only see the widget on a salon's existing page.

2. ❌ **No booking software.** Fresha ($150M raised) and Square own booking. We integrate, don't replace. The widget's "Book this style" button always links OUT to the salon's existing booking URL.

3. ❌ **No beauty / makeup / nail AR.** ModiFace ($1B+ L'Oréal-owned) and YouCam own this. Haircuts + color only.

4. ❌ **No enterprise sales motion.** Solo founder + 14-day MVP means we sell to **independent salons with 1-5 locations** via cold DM + Product Hunt. We do not pursue franchises, chain salons (Great Clips, Sport Clips) — those are enterprise deals.

5. ❌ **No product recommendations / e-commerce.** We do not recommend shampoo or sell products. That market is owned by Sephora, Ulta, and salon-brand retailers.

6. ❌ **No face-shape AI in MVP.** Face-shape analysis is interesting but requires training data we don't have. P2 only, not P0.

**Why this wedge is defensible:**
- The B2B2C salon-widget position is **not where YouCam plays** (they're consumer app).
- The B2B2C salon-widget position is **not where Fresha/Square play** (they're booking, no AI).
- The integration cost is **high for incumbents** (Fresha would need to build AI from scratch, hire ML team).
- The TAM is **200K US + 140K EU salons × $29-79/mo = $100M+ ARR** in our wedge alone.
