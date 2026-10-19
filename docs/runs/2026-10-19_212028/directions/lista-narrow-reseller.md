# Direction — Reseller AI Crosslister (Narrow Wedge of Lista)

Slug: `lista-narrow-reseller` · Tier: **GO_NARROW** · Run: 2026-10-19_212028

## 1. Why this direction
**TrustMRR evidence:** `Lista: AI Crosslisting & Tools` is at $10.36 MRR / $9 last30 / 113 subs doing AI crosslist. But `Lista` is general (Mercari/Poshmark/eBay/etc.), and `ShopTok`, `Vidoo`, `UltraWideo` show 4+ comp_h on broad listing/deal tools.

**Demand signal:** Resellers spend 30–60 min per item copying title/desc/price to 3–5 marketplaces. $9/mo crosslisters save real hours. Subscription willingness proven by Lista $10K-class MRR.

**The wedge we keep:** Reseller-specific, multi-marketplace with **3 marketplaces only** (Poshmark + eBay + Depop), **vintage clothing / Y2K / curated thrift ICP only**. No Mercari. No Facebook Marketplace. No Etsy.

**Why this is GO_NARROW not KILL:**
- Comp_h = 4 on broad listing tools → too crowded
- Comp_h = 2 on **narrow vintage-reseller crosslister** → uncontested
- Demand_h = 3 on reseller pain → daily pain, weekly search

## 2. Competitor table (L1/L2/L3)

| Tier | Name | Price | Why we win in niche |
|---|---|---|---|
| L1 | Lista | $7/mo (free tier 2 listings) | Generic, 6+ marketplaces → bad at vintage copy |
| L1 | Crosslist.com | $24.99/mo | Expensive, no AI copy |
| L1 | List Perfectly | $29.99/mo | Squarespace-built, $30 floor |
| L2 | Vendoo | $11.99/mo | Resellers love, but no AI description rewrite tuned for vintage |
| L2 | PrimeLister | $10/mo | Buggy, 4-marketplace only |
| L3 | DIY spreadsheets | $0 | Time cost = real |

**Score (vintage-reseller narrow):** competition = **2**

## 3. PRD MVP

**Wedge (what we REFUSE to build):**
- ❌ Mercari, Facebook Marketplace, Etsy integration
- ❌ Bulk CSV import for enterprise resellers
- ❌ Multi-user / team accounts
- ❌ NFT / digital collectibles
- ❌ B2B wholesale

**P0 (day 1–14):**
- 3-marketplace bridge: Poshmark + eBay + Depop
- Photo-first listing: take 4 photos, AI writes the vintage-flavored title + description tuned for Y2K/thrift/curated
- Price suggestion based on category + condition (categorical model, not ML heavy)
- Dashboard: inventory list, multi-list button, "relist dropped" reminder
- iOS app OR PWA (resellers are mobile-first — depot/prep at home)
- Pricing: Free = 5 listings/mo, Pro = $9/mo unlimited, Reseller = $19/mo (Pro + bulk relist + analytics)

**P1 (week 3–4):**
- Brand-name detection (e.g., "Kate Spade" → flags as luxury → suggests higher price floor)
- "Share of closet" analytics
- Vintage keyword enrichment (era tags)

**P2:**
- Shopify Lite integration
- Discord community for resellers

## 4. 14-day day-by-day build plan

| Day | Deliverable |
|---|---|
| 1 | Repo + Expo/React Native starter; auth (magic-link) |
| 2 | Inventory CRUD + SQLite; iOS-first UI |
| 3 | Camera capture + EXIF strip |
| 4 | AI description generator (Claude/GPT-4-mini prompt tuned for vintage) |
| 5 | Poshmark integration (manual share-sheet first; deep API 2nd) |
| 6 | eBay integration via eBay Trading API sandbox |
| 7 | Depop integration (Depop has no API — use share sheet + manual) |
| 8 | Pricing page + Stripe |
| 9 | PWA fallback for Android (Resellers are iOS-heavy, but coverage helps) |
| 10 | Docs + onboarding flow |
| 11 | Closed beta: 20 vintage resellers in r/Flipping, r/EtsySellers, r/Poshmark |
| 12 | Bug bash + Stripe live |
| 13 | Pricing live, paid landing |
| 14 | Launch: r/Flipping launch post + 5 tweets + IndieHackers |

**Stack:** React Native (Expo) or PWA + Node/Express + SQLite + Claude API + eBay API.

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $0 baseline. $100 reserved for "1 niche newsletter placement" (e.g., Flipper University, $50 pitch + $50 followup). $200 reserved for Product Hunt or Flippa flipper community sponsorship if ROI positive.

| Week | Channel |
|---|---|
| 1 | r/Flipping announcement post (Tuesday 9am ET), r/Poshmark "I built this" Tuesday, r/EtsySellers, 3 launch tweets with photos |
| 2 | 1 YouTube short demo (post in r/Flipping), reply to 10 reseller tweets daily |
| 3 | 3 SEO blogs: "poshmark to ebay crosslist 2026", "vintage listing AI description", "crosslist without listperfectly" |
| 4 | 1 podcast pitch (Flipper University / Reseller Round Up), 1 newsletter (PoshSide Hustle / ThriftFlip newsletter) |

## 6. Unit economics to $10K MRR
- Price: $9/mo Pro, $19/mo Reseller; mix target = 70% Pro / 30% Reseller
- Blended ARPU: ~$12/mo
- Need **833 paying** to hit $10K
- Gross margin: ~88% (API costs)
- CAC: ~$0 organic, $7 paid (newsletter)
- LTV (~10 mo, reseller churn is real): ~$120
- LTV/CAC: ~17×

**Path to 833 paying:**
- Month 1: 50 paid (Beta+launch)
- Month 2: 120 paid
- Month 3: 250 paid
- Month 4: 400 paid
- Month 5: 600 paid
- Month 6: 800 paid → ~$9.6K MRR

## 7. Kill criteria (day 30)
- < 20 paid by day 30 → ICP wrong (try sneaker resellers or general instead)
- Reseller churn > 30% by month 3 → economics broken; kill or pivot to free-only
- eBay API rate-limit blocks P0 launch → switch to share-sheet-only

## 8. Re-verify before code (day 1–3)
1. `r/Flipping "crosslist" recent` — confirm pain
2. `"listperfectly alternative" reddit` — confirm defectors
3. Search Twitter: `"@crosslisthq" OR "@vendoolisting" hate OR broken`
4. Read Lista reviews for feature gaps

## 9. Wedge (required for GO_NARROW)
**We are NOT building a general crosslister.** We are the AI crosslister tuned for **vintage / Y2K / curated thrift resellers** on **Poshmark + eBay + Depop only**. We refuse Mercari, Facebook Marketplace, Etsy (until P2), and B2B wholesale. If a paying customer asks for "support Mercari" they get a "we don't support Mercari; here's why" form letter. This keeps our TAM smaller but our wedge defensible against Crosslist.com / Vendoo / List Perfectly which all spread thin across 6+ marketplaces and break on vintage language.
