---
layout: post
title: "CatalogoHoy — Opportunity Direction"
date: 2026-11-10T00:32:56+00:00
week: "2026-11-10_003256"
week_date: "2026-11-10T00:32:56+00:00"
slug: "catalogohoy"
permalink: /directions/catalogohoy.html
tags:
  - "AI"
  - "vertical"
excerpt: "A catalog-production assistant for one local-commerce niche, converting product lists into consistent print-ready and social-ready catalog layouts."
---

## 1. Why this direction

### Opportunity

Build a focused catalog-production assistant for a single local-commerce niche. A merchant uploads a structured product list and receives consistent catalog pages, social cards, and a simple PDF export. The product should solve repeat production work rather than become a general design suite.

### Target customer

The initial ICP is one of:

- A local boutique selling 20–100 products.
- A small wholesale distributor producing seasonal catalogs.
- A specialty food or beauty merchant with frequent seasonal assortments.
- A marketplace seller whose customers use catalogs for purchasing.

Choose exactly one segment. The recommended first segment is independent home and lifestyle boutiques because their products are visually coherent and catalog creation is a recurring workflow.

### TrustMRR evidence

Stage A reports CatalogoHoy at:

- MRR: **$3.59**
- Last 30 days: **$17.49**
- Subscribers: **23**
- Stage A demand score: **3**
- Stage A competition score: **2**
- Website: https://catalogohoy.com
- X handle: `@so_tic0`

Revenue is currently small but last-30-days revenue materially exceeds current MRR, suggesting a recent increase or timing volatility. The listing nevertheless confirms a functioning product and some customer interest. The stronger opportunity comes from constraining the product to one catalog workflow and one merchant niche.

### X and web evidence

The supplied Stage A search output did not contain usable search results. Run and archive:

- `"CatalogoHoy" (painful OR broken OR hate OR expensive)`
- `"CatalogoHoy" (looking for OR recommend OR alternative)`
- `"catalog maker" (painful OR expensive OR "takes too long")`
- `"product catalog" small business (Canva OR template OR manual)`
- `"seasonal catalog" merchant pain`
- `site:x.com "CatalogoHoy"`
- `site:reddit.com small business product catalog design`

Demand validation requires 10 dated posts and 10 merchant interviews, with at least five confirming recurring catalog work and at least three agreeing to pay $29–$79 for a monthly workflow.

### Why it can win

The product should not compete with Canva on general design freedom. It should turn merchant data into a finished, consistent deliverable:

1. Upload products from CSV, spreadsheet, or a structured form.
2. Select one catalog template.
3. Auto-create product spreads and social previews.
4. Correct generated copy and imagery.
5. Export print-ready PDF and social assets.

The value is saved production time and consistent output.

### Validation gate

Proceed only if:

1. Ten interviews confirm catalog production is recurring and painful.
2. Five merchants provide a real recent catalog or product feed.
3. Three agree to test a concierge catalog.
4. Two agree to pay $49 or more per month.
5. The chosen niche has no dominant vertical catalog product below $49 with materially better output quality.

## 2. Competitor table

### L1 direct competitors

| Competitor | Positioning | Pricing to verify | Strength | Opening for CatalogoHoy |
|---|---|---:|---|---|
| CatalogoHoy | Catalog creation, to verify | Unknown | Existing product and local-market fit | Specialized template, faster batch workflow, stronger data import |
| Canva | General design suite with catalog templates | Free plus paid plans | Ubiquitous, broad template library | Product-feed automation and batch catalog output |
| Adobe Express | General design and print assets | Free plus paid plans | Print ecosystem and brand controls | Faster structured generation and lower specialist overhead |
| VistaCreate | Print marketing and catalogs | Paid plans | Print-shop integration, templates | Faster catalog generation and lower design complexity |
| Marq / Brandfolder / others | Brand-governed collateral | Paid plans | Brand consistency and templates | Focus on independent merchants and product data |
| Lucidpress | Online and print design | Free plus paid plans | Familiar design workflow | Automation from product data |
| DesQgn / DSers / Sellbrite | Product and order management with some collateral | Varies | E-commerce catalog workflows | Standalone design output for non-platform merchants |

Official pricing, export formats, and print quality must be verified before implementation.

### L2 alternatives

| Alternative | Why users choose it | Opening |
|---|---|---|
| Canva catalog maker | Familiar, inexpensive, flexible | Slow manual duplication and inconsistent updates |
| Excel/PowerPoint layout | Works with existing skills | Poor print workflows and high manual effort |
| InDesign / Affinity Publisher | Professional print control | Steep learning curve for small merchants |
| Agency/freelancer | High quality and service | Expensive and slow for recurring work |
| Printing service templates | Ready for press | Generic, limited product-data automation |
| Product-feed PDF | Easy to generate | Weak visual storytelling and poor social assets |
| Marketplace-native catalog | No extra production | Locked to one channel and no custom layout |

### L3 substitute behavior

- Export product photos and manually arrange them in Canva.
- Use a free PDF template.
- Ask a designer for each seasonal update.
- Publish only a web storefront.
- Create a spreadsheet price list.
- Post individual products on social media.

### Competition score

**Score: 2/5 for a vertical catalog-production workflow.** General design tools are broad substitutes, but they do not automatically solve product ingestion, batch layout, and repeated seasonal updates for one vertical. Keep the scope narrow and emphasize output, not editing flexibility.

If research reveals strong vertical catalog incumbents, retain the `GO_NARROW` wedge below and keep competition at 4.

## 3. PRD — MVP

### Product promise

Turn a product list into a consistent, editable, export-ready catalog in under 30 minutes.

### Initial niche

Independent home and lifestyle boutiques selling 20–100 SKUs. Product types, image ratio, and catalog sizes should be fixed for this niche.

### P0 — launch-critical

1. **Product import**
   - CSV upload with a documented template.
   - Product name, SKU, price, short description, category, image URL, and optional dimensions.
   - Inline validation and row-level error reporting.
   - Manual entry for up to 20 products.

2. **Template system**
   - One print catalog template family.
   - Fixed page sizes, grids, typography, and image behavior.
   - Choose one visual theme.
   - Auto-generate cover, contents, category pages, and product spreads.

3. **Controlled editing**
   - Edit title, price, description, category, ordering, and visibility.
   - Replace or crop product images.
   - Reorder products and pages.
   - No arbitrary canvas manipulation in the MVP.

4. **Asset outputs**
   - Print-ready PDF with crop marks and bleed option.
   - Web PDF preview.
   - One social-card size.
   - Optional ZIP of product images and previews.

5. **Project workflow**
   - Duplicate a previous catalog when seasonal stock changes.
   - Save drafts.
   - Export history.
   - Version label and generation timestamp.

6. **Quality and brand controls**
   - Brand logo, one primary color, and one font family.
   - Currency and locale settings.
   - Preview overflow and low-resolution warnings.
   - Manual approval step before export.

7. **Account and billing**
   - Email magic-link authentication.
   - 7-day trial.
   - Starter: **$49/month**, 3 catalogs and 100 products.
   - Studio: **$99/month**, 10 catalogs and 500 products.
   - Stripe billing.

8. **Copyright and content safeguards**
   - User confirmation that images and copy are authorized.
   - No scraping from marketplaces or competitors.
   - No copyrighted music or template reuse beyond licensed assets.
   - Clear AI-assistance disclosure where text is generated.

### P1 — first 30 days

- XLSX import.
- Shopify CSV import for merchants who sell there.
- Multiple print sizes.
- More templates.
- Social carousel export.
- Shared read-only catalog link.
- QR codes.
- Bulk copy editing.
- Print-shop handoff.

### P2 — after product-market signal

- Inventory-feed synchronization.
- More vertical templates.
- Brand kits and fonts.
- Team approval workflow.
- Marketplace asset presets.
- Translation.
- API and plugin integrations.
- Background-removal and retouch options.

### Non-goals

- A general Canva-style design editor.
- Pixel-perfect free positioning.
- Logo generation.
- Product photography.
- Full inventory or ERP management.
- Automatic marketplace publishing.
- Guaranteed print-shop compatibility for every paper size.
- Video creation.
- Website building.
- Multi-tenant agency workflows in the MVP.
- Global template marketplace.

### Core user stories

- As a boutique owner, I want to upload my products once so that I do not manually rebuild every page.
- As a merchant, I want a consistent seasonal catalog so that my brand looks professional.
- As a merchant, I want to correct prices and descriptions easily so that errors do not reach customers.
- As a merchant, I want both print PDF and social previews so that I can use the same campaign across channels.
- As a merchant, I want to reuse last season’s project so that small inventory changes are quick.

### MVP acceptance criteria

A user can:

1. Import 20 products from CSV.
2. Correct any validation errors.
3. Generate a branded catalog preview.
4. Edit a product and reorder it.
5. Export a print-ready PDF and social assets.
6. Duplicate the project for the next season.
7. Upgrade through Stripe.

### Technical recommendation

- Next.js/TypeScript application.
- PostgreSQL for users, products, projects, assets, and exports.
- Object storage for source and generated images.
- Background job queue for generation and PDF rendering.
- Deterministic template rendering with React/PDF or a comparable layout engine.
- Image processing with a cloud image pipeline or Sharp.
- Stripe billing.
- Export and job logs.
- Signed URLs for private source assets.
- Automatic file-size, dimension, and malware checks.

### Quality requirements

- No text overflow.
- No low-resolution product image below a documented threshold without warning.
- Correct PDF dimensions and bleed.
- Consistent fonts embedded in the PDF.
- Accessible web preview.
- Reproducible export from stored project version.
- Clear separation between source asset and generated output.

## 4. 14-day build plan

| Day | Objective | Deliverables | Exit criterion |
|---:|---|---|---|
| 1 | Validate niche and pain | Select boutique segment; interview ten merchants; map output formats | Five recurring-work confirmations |
| 2 | Validate payment | Produce one concierge catalog; offer $49/month | Two paid commitments |
| 3 | Foundation | Auth, database, file storage, jobs, environments, logging | End-to-end placeholder project works |
| 4 | Product import | CSV schema, upload, validation, error report, manual entry | Twenty-product import succeeds |
| 5 | Template engine | Fixed layout schema, themes, image fitting, typography | Three page types render correctly |
| 6 | Catalog generation | Cover, contents, categories, product pages, page breaks | Full catalog generates from seed data |
| 7 | Editing | Product fields, reorder, hide, image replace, brand controls | Changes persist and regenerate cleanly |
| 8 | Export | Print PDF, web preview, social images, background jobs | Exports open in target applications |
| 9 | Project reuse | Duplicate project, versioning, export history, draft/publish states | Seasonal update workflow works |
| 10 | Quality safeguards | Overflow checks, image warnings, font embedding, export validation | Automated QA catches seeded defects |
| 11 | Billing | Stripe, trial, plan quotas, customer portal | Billing and quota paths pass |
| 12 | UX and onboarding | Sample project, guided import, error recovery, pricing | Five testers complete without help |
| 13 | Pilot | Ten merchants import real products and export catalogs | Five usable catalogs and ten exports |
| 14 | Release | Fix blockers, deploy, launch, instrument funnel | Five live catalogs, ten exports, three paying users, otherwise review |

### Daily operating rule

Use real merchant product files in development. A template that only works with sanitized seed data is not complete.

## 5. 30-day marketing calendar

### Budget

Total maximum: **$300**

| Activity | Budget |
|---|---:|
| Merchant research and pilot incentives | $75 |
| Niche community or newsletter sponsorship | $75 |
| Sample catalogs and creative assets | $75 |
| Print/export testing allowance | $25 |
| Referral credits | $50 |
| **Total** | **$300** |

### Organic-first plan

| Day | Activity | Channel | CTA | Success signal |
|---:|---|---|---|---|
| 1 | Publish “your seasonal catalog is costing 12 hours” post | LinkedIn, Instagram | Comment with catalog | 8 replies |
| 2 | Interview 10 boutique owners | Direct outreach | Share last catalog | 10 interviews |
| 3 | Publish a before/after manual catalog workflow | LinkedIn, blog | Upload product list | 5 imports |
| 4 | Create one free niche template guide | Blog | Download template | 15 downloads |
| 5 | Show a concierge catalog example | LinkedIn, portfolio | Request sample | 8 requests |
| 6 | Post a 30-second generation demo | Instagram, TikTok, LinkedIn | Try beta | 15 waitlist leads |
| 7 | Recruit 10 boutique pilots | Instagram, niche groups | Join pilot | 10 pilots |
| 8 | Publish a seasonal-update checklist | Blog | Join checklist | 20 downloads |
| 9 | Share a customer catalog before/after | LinkedIn, Instagram | Create catalog | 6 creations |
| 10 | Teach CSV product-feed preparation | YouTube, blog | Import products | 12 imports |
| 11 | Run catalog critique office hours | Instagram live, Zoom | Bring catalog | 12 attendees |
| 12 | Ask pilots for structured feedback | Email | Book interview | 6 replies |
| 13 | Publish print-export comparison guide | Blog | Export PDF | 10 exports |
| 14 | Launch beta publicly | Founder account, niche groups | Subscribe | 15 trials |
| 15 | Share a seasonal restock workflow | Instagram, email | Duplicate project | 8 duplicates |
| 16 | Publish social-card reuse workflow | LinkedIn, blog | Generate social assets | 8 uses |
| 17 | Interview activated merchants | Email | Continue | 5 responses |
| 18 | Offer a free catalog audit to 20 merchants | Direct outreach | Book audit | 8 audits |
| 19 | Publish “Canva vs automated catalog” comparison | Blog | Try import | 12 trials |
| 20 | Add one popular niche template | Product | Use template | 10 uses |
| 21 | Partner with one boutique owner for workflow story | Joint post | Try beta | 15 visits |
| 22 | Publish image-resolution and bleed guide | Blog | Export safely | 15 visits |
| 23 | Ask pilot users for referrals | Email | Refer merchant | 10 referral clicks |
| 24 | Run a product-feed setup clinic | Live event | Bring CSV | 15 attendees |
| 25 | Contact local maker associations | Partnership email | Run workshop | 3 partnerships |
| 26 | Improve import errors from ten real files | Product | Import a file | 80% import completion |
| 27 | Publish a brand-consistency template update | Email, social | Update brand | 15 updates |
| 28 | Announce saved-version reuse | Product, email | Duplicate a catalog | 10 duplicates |
| 29 | Rescue inactive trials with personal setup | Email | Complete one catalog | 8 rescues |
| 30 | Publish cohort results and template roadmap | Blog, founder account | Join next cohort | Clear keep/kill decision |

### Acquisition targets

By day 30:

- 200 targeted merchant visits.
- 40 trials.
- 20 activated projects.
- 8 paying merchants.
- $392 MRR if half use the $49 plan and half the $99 plan; otherwise report the actual mix.
- Ten captured pain posts and five completed case studies.

## 6. Unit economics to $10K MRR

### Proposed pricing

- Starter: **$49/month**, 3 catalogs and 100 products.
- Studio: **$99/month**, 10 catalogs and 500 products.
- Optional paid one-off catalog: $39 for occasional merchants, but cap this to avoid cannibalizing subscription intent.

At $49/month, 205 customers produce $10,045 MRR. At $79/month blended, 127 customers produce $10,033 MRR.

### Model

| Metric | Conservative | Target | Strong |
|---|---:|---:|---:|
| Blended ARPA | $49 | $79 | $99 |
| Customers for $10K | 205 | 127 | 102 |
| Gross margin | 80% | 86% | 90% |
| Gross profit/customer/month | $39.20 | $67.94 | $89.10 |
| CAC allowance | $80 | $125 | $175 |
| Months to $10K at constant CAC | 104.6 | 58.4 | 46.1 |
| Monthly churn | 8% | 5% | 3% |

At $79 ARPA, 86% gross margin, and 5% churn:

- LTV = **$1,358.80**.
- A $125 CAC gives an LTV:CAC ratio of approximately 10.9:1.
- Payback is about 1.8 months.

This attractive model assumes the product saves several hours of merchant or contractor labor each month. Validate that time-saving claim with customers before treating the model as credible.

### Cost controls

- Generate standard previews at lower resolution.
- Use expensive rendering only for final PDF export.
- Compress and resize uploaded product images.
- Batch operations and cap quota use.
- Track storage and generation cost per catalog.
- Avoid per-seat complexity in the MVP.
- Use templates to minimize prompt and rendering cost.

### Distribution requirement

The budget cannot directly acquire 127 customers. Build distribution through:

1. Niche templates and seasonal keyword content.
2. Local maker and boutique associations.
3. Print-shop and ecommerce-service partnerships.
4. Agencies serving a narrow merchant category.
5. Referral from catalog and branding freelancers.
6. Productized “seasonal catalog refresh” services that upsell subscriptions.

### Scenario checkpoints

- Month 1: 8 paying merchants and approximately $390–$790 MRR depending on mix.
- Month 3: 30 paying merchants and $1,470–$2,370 MRR.
- Month 6: 70 paying merchants and $3,430–$5,530 MRR.
- Month 9: 127 paying merchants and approximately $10K MRR at $79 blended ARPA.

## 7. Kill criteria

Stop or materially reframe if:

1. Fewer than 5 of 20 merchants report recurring catalog production as a meaningful pain.
2. No merchant agrees to pay $49 or more for the workflow.
3. Users only want one-off templates and do not renew after the first export.
4. First-time users cannot import products and export a catalog in 30 minutes.
5. Fewer than 50% of trials produce a completed export.
6. Manual correction takes more than 20% of the time saved.
7. Export quality is judged materially below a Canva template by more than 30% of pilot users.
8. Monthly churn exceeds 12% for two cohorts.
9. No partnership or content channel produces customers below $150 CAC.
10. Competitor research reveals a dominant vertical catalog product below $49 with better output.
11. Copyright or image-rights risk cannot be controlled.
12. The product expands into a general design editor and loses the narrow workflow.
13. The founder cannot source ten relevant merchants or five pilot files per week.

## Wedge (required for GO_NARROW)

Not applicable under the scoped positioning. If current research raises the general catalog/design competition score to 4, retain this wedge:

> One merchant vertical, one catalog template family, structured product-data import, fixed print/social outputs, and fast seasonal reuse. Refuse arbitrary canvas editing, general branding suites, video, website building, product-photography generation, ERP/inventory management, and marketplace publishing.
