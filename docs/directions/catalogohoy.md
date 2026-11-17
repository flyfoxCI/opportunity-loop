---
layout: post
title: "CatalogoHoy — Spanish-Language Product Catalog Builder"
date: 2026-11-17T10:32:16+00:00
week: "2026-11-17_103216"
week_date: "2026-11-17T10:32:16+00:00"
slug: "catalogohoy"
permalink: /directions/catalogohoy.html
tags:
  - "AI"
  - "B2C"
  - "language"
  - "mobile"
  - "analytics"
excerpt: "Turn a product link into a conversion-ready Spanish-language catalog page with consistent output."
---

**Tier:** GO_NARROW  
**Demand:** 3/5  
**Competition:** 3/5  
**Target:** $10,000 MRR  
**MVP:** 14 days, solo  
**Marketing budget:** ≤ $300 for 30 days  

## 1. Why this direction

### TrustMRR evidence

- CatalogoHoy reports approximately **$4.67 MRR**, **$21.77 in last-30-day revenue**, and **31 subscribers**.
- Last-30 revenue is substantially above current MRR, which may indicate recent conversions, prepaid plans, or timing effects; the discrepancy requires verification before relying on it.
- The product appears to address catalog creation for Spanish-speaking merchants or consumers.
- The revenue is small, so the strongest signal is the existence of a localized workflow rather than proven scale.
- The narrow opportunity is not “another catalog builder.” It is a repeatable import-to-catalog output for one platform and one merchant type.

### X/web evidence

- The identified X handle is `@so_tic0`.
- The supplied TinyFish output did not expose result bodies, so no quotes or engagement metrics are claimed.
- The public social hypothesis is that independent merchants want product descriptions and catalogs in natural Spanish without rebuilding each listing manually.
- Direct outreach to Spanish-speaking merchants is essential because generic web demand will not validate this localization wedge.

### Thesis

Build a **Spanish-language catalog generator for independent sellers**. A merchant imports a CSV or pastes a product list, selects a brand style, and receives a clean, shareable catalog with:

- natural Spanish descriptions;
- consistent formatting;
- product images;
- prices and optional contact links;
- PDF/online catalog export;
- one-click updates.

The product’s value is linguistic consistency plus operational speed, not proprietary AI technology.

### Initial ICP

- Independent Latin American or Spanish-speaking sellers with 10–100 products.
- Start with one commerce workflow: **CSV to shareable catalog** for Instagram, WhatsApp, or a simple hosted link.
- Do not promise synchronization with every marketplace in the MVP.

### Validation questions

1. Are merchants copying the same products into multiple formats?
2. Which output is used most often: PDF, image carousel, WhatsApp list, or hosted link?
3. Are natural Spanish descriptions worth paying for?
4. How often does the catalog change?
5. Can one import workflow replace a recurring manual task?

## 2. Competitor table

### L1 — direct alternatives

| competitor | likely offer/pricing | strength | weakness / opening | evidence confidence |
|---|---|---|---|---|
| CatalogoHoy | Localized catalog product with approximately $5 MRR and 31 subscribers | Existing localization focus and audience | Opportunity to specialize by merchant type and output channel | High for metrics; medium for feature set |
| Canva | General catalog and brochure templates | Familiar editing and strong templates | Requires manual product copy, layout, and multilingual consistency | High |
| Adobe Express | Catalog/product-list templates | Polished assets and broad brand tools | General-purpose and not optimized for Spanish product copy | High |
| Paperless / PDF catalog tools | Generate product PDFs | Efficient PDF output | Often require manual content preparation and lack language workflows | Medium |
| Shopify catalog tools | Create and manage storefront product data | Integrated commerce ecosystem | Heavier setup, monthly platform cost, and broader scope | High |
| Product-data feed tools | Normalize and publish product information | Reliable catalog structures | Technical, implementation-heavy, and not creator-friendly | High |

### L2 — adjacent substitutes

| substitute | why buyers use it | opportunity |
|---|---|---|
| Excel/Google Sheets | Maintain products and descriptions | No polished catalog output or translation consistency |
| Copywriter/freelancer | Write product descriptions | Cost and turnaround for ongoing catalogs |
| WhatsApp product lists | Share products with customers | Inconsistent formatting and no downloadable catalog |
| Marketplace listings | Publish each product | Duplicated work across channels and languages |

### L3 — low-end alternatives

| alternative | weakness |
|---|---|
| Machine translation | Often unnatural, inconsistent, and unstructured |
| Copy-paste templates | Slow and visually inconsistent |
| Free PDF generators | No content transformation or brand flow |

### Competition conclusion

**Score: 3/5.** General catalog and e-commerce tools are established, but localized Spanish output for a narrow merchant workflow remains a plausible niche. The product must avoid competing on general design capability and compete on **import speed + natural Spanish + ready-to-share output**.

## 3. PRD MVP

### Target outcome

An independent Spanish-speaking seller can upload a product CSV and receive a branded, consistent catalog they can send to customers or publish online.

### P0 — required for launch

- CSV import with validation:
  - name;
  - description;
  - price;
  - image URL or uploaded image;
  - optional SKU/category.
- Basic setup wizard:
  - language: Spanish;
  - catalog name;
  - brand color;
  - logo;
  - contact method.
- Natural-Spanish description normalization:
  - preserve facts;
  - improve grammar and consistency;
  - never invent specifications.
- Template-based catalog generation:
  - cover;
  - category headings;
  - product cards;
  - price;
  - image;
  - optional contact CTA.
- Outputs:
  - hosted shareable link;
  - downloadable PDF;
  - mobile-friendly vertical catalog.
- Manual product edit and regenerate.
- Re-upload/replace list workflow.
- Branding and pagination.
- Authentication, usage limits, Stripe billing.
- Export analytics and download tracking.
- Human-review notice for generated descriptions.

### P1 — after validation

- Reusable saved brands and templates.
- WhatsApp-friendly image catalog.
- Spanish regional variants.
- Inventory and “hide sold-out item” controls.
- Duplicate-product detection.
- CSV round-trip export with normalized copy.

### P2 — later expansion

- Marketplace connectors.
- Team approval.
- Inventory synchronization.
- Multi-language catalogs.
- Agency white-label catalog builder.
- Printable price-list variants.

### Non-goals

- No full storefront or checkout in the MVP.
- No inventory synchronization with Shopify, WooCommerce, or marketplaces at launch.
- No marketplace scraping.
- No universal PDF-design editor.
- No bulk WhatsApp automation.
- No claims of perfect regional idiomaticity without review.
- No agency workflow until individual merchants retain.

### MVP user story

> As an independent Spanish-speaking seller, I can import my product list and receive a consistent branded catalog quickly so that I can sell without rebuilding every product post.

### Technical approach

- Next.js application with server-side CSV parsing.
- Product model with source facts and generated fields kept separate.
- Generation: constrained structured rewrite preserving names, prices, dimensions, materials, and SKUs.
- Rendering: deterministic HTML templates for hosted output and PDF generation.
- Hosted catalog URLs use public IDs and expiration/republish controls.
- Storage: PostgreSQL plus object storage.
- Billing: Stripe with monthly catalog and export limits.

### Pricing hypothesis

- **Free:** one catalog, 10 products.
- **Vendedor:** $19/month, 100 products, three templates, hosted link and PDF.
- **Negocio:** $49/month, 500 products, saved brand, regional variants, and bulk update.
- **Agencia pilot:** $99/month, 10 client brands and reusable templates.

## 4. 14-day day-by-day build plan

| Day | objective | deliverables | acceptance test |
|---:|---|---|---|
| 1 | Validate ICP | Select independent home/food/cosmetic sellers; prepare CSV samples | 10 prospects agree to test workflow |
| 2 | Prototype | Build import-to-catalog clickable flow and sample PDF | A seller can complete the flow in 5 minutes |
| 3 | Interviews | Interview 10 sellers and collect source CSVs | 5 report repetitive catalog work and 3 share files |
| 4 | Import | CSV parser, field mapping, validation, image handling | 10/10 sample lists import with clear errors |
| 5 | Description generation | Spanish normalization with fact preservation | 50 descriptions pass human quality/fact checks |
| 6 | Templates | Build cover, grid, and list templates | 20 products render cleanly on mobile and PDF |
| 7 | Hosting and export | Public catalog URL, PDF render, download tracking | Links work on mobile and regenerate deterministically |
| 8 | Editor | Edit title, price, description, image, and reorder products | Common corrections require no support |
| 9 | Branding | Logo, color, catalog metadata, contact CTA | Branding appears consistently on all templates |
| 10 | Account and billing | Authentication, limits, Stripe checkout, webhooks | Paid plans unlock exports and catalog counts |
| 11 | Reliability | Image fallback, parser errors, generation retries, sanitization | Large/broken CSVs fail gracefully |
| 12 | Pilot | Onboard 10 sellers with real product lists | 7 generate and 5 share/download catalogs |
| 13 | Pricing and UX | Add plan comparison, feedback form, onboarding | 2 users state intent to purchase and checkout works |
| 14 | Release | Deploy, publish gallery, record demo, start outreach | 99% import success and first paid conversion available |

### Solo-build controls

- Support CSV only in the MVP.
- Use three fixed templates.
- Keep hosted output read-only.
- Do not build storefront checkout.
- Limit the catalog size per account.

## 5. 30-day marketing calendar

### Budget

| channel | 30-day spend |
|---|---:|
| Spanish-language creator partnerships | $120 |
| Search/social content and small boosts | $60 |
| Translation/review tooling | $40 |
| Customer referral/incentives | $80 |
| **Total** | **$300** |

### Calendar

| day | activity | organic action | paid action | KPI |
|---:|---|---|---:|---|
| 1 | Launch | Publish homepage and three sample catalogs | None | 150 qualified visits |
| 2 | Founder post | Publish a Spanish-language workflow demo | None | 10 comments |
| 3 | Seller outreach | Contact 20 independent Spanish-speaking sellers | None | 6 interviews |
| 4 | Free artifact | Publish free CSV catalog template | None | 30 downloads |
| 5 | Demo video | Show 20 products to a branded catalog | None | 20% import-start rate |
| 6 | Pilot offer | Generate five catalogs manually | None | 5 completed catalogs |
| 7 | Review | Fix description and image issues | None | 80% first-render success |
| 8 | Spanish SEO | Publish “catálogo de productos en PDF” page | None | 25 organic visits |
| 9 | Creator outreach | Send tool to 10 Spanish-language creators | None | 3 creator posts |
| 10 | Merchant groups | Share checklist and free generation slot | None | 10 inbound conversations |
| 11 | Case study | Publish time-saved seller story | None | 4 trials |
| 12 | User calls | Interview five users | None | 5 completed calls |
| 13 | Product iteration | Add regional variants and manual editor | None | 70% satisfaction |
| 14 | Pricing test | Add $19/$49 plan choices | None | 6% checkout start |
| 15 | Template gallery | Publish food, beauty, and home templates | None | 20 template uses |
| 16 | Paid creator | Promote catalog workflow | $60 | CAC below $30 |
| 17 | Live session | Build a catalog live from a seller CSV | None | 10 registrants |
| 18 | WhatsApp asset | Release vertical image sequence | None | 20 exports |
| 19 | Review | Analyze activation and output type | None | Identify strongest niche |
| 20 | WhatsApp business outreach | Contact 10 boutique owners | $20 | 2 calls |
| 21 | Referral | Ask buyers to refer one seller | $25 | 5 referrals |
| 22 | Tutorial | Publish complete import tutorial | None | 40 organic visits |
| 23 | Founder post | Explain Spanish quality and fact preservation | None | 8 sales conversations |
| 24 | Paid retarget | Retarget sample visitors | $15 | 3 trials |
| 25 | Retention | Review catalog update frequency | None | 40% second export within 14 days |
| 26 | Upgrade prompt | Prompt saved brand and bulk update | None | 3 upgrades |
| 27 | Customer proof | Publish seller testimonial | None | 5 checkout starts |
| 28 | Channel review | Pause weak sources | None | CAC below $30 |
| 29 | Automation | Send update-reminder and re-export email | None | 30% open rate |
| 30 | Monthly review | Reconcile MRR, churn, generation cost, and CAC | $0 | 15+ paid accounts or pivot |

### Organic-first content pillars

- Spanish-language catalog templates.
- CSV-to-PDF workflows.
- Seller interviews.
- WhatsApp and Instagram selling tips.
- Natural versus literal translation examples.
- Founder build-in-public content in Spanish.

## 6. Unit economics to $10K MRR

### Target mix

| plan | price | customers | MRR |
|---|---:|---:|---:|
| Vendedor | $19 | 180 | $3,420 |
| Negocio | $49 | 100 | $4,900 |
| Agencia | $99 | 17 | $1,683 |
| **Total** |  | **297** | **$10,003** |

### Cost model

Assumptions:

- Product-description generation: **$0.03/product**.
- Import, PDF rendering, and storage: **$0.12/catalog**.
- Average 50 products and 3 catalog updates per account per month:
  - generation cost: $1.50/account/month;
  - rendering/storage cost: $0.36/account/month.
- Payment and infrastructure: **4% of revenue**.
- Support allowance: **$3/account/month**.
- Fixed solo operating cost: **$1,200/month**.

At 297 accounts:

- Revenue: approximately **$10,003/month**.
- Generation/rendering: approximately **$553/month**.
- Payment/infrastructure: approximately **$400/month**.
- Support: approximately **$891/month**.
- Contribution before fixed cost: approximately **$8,159/month**.
- After fixed cost: approximately **$6,959/month** before taxes and founder compensation.

### CAC and payback assumptions

- Target blended CAC: **≤ $30**.
- At $19/month, estimated contribution before fixed cost is approximately:
  - $19 revenue;
  - $1.86 generation/rendering;
  - roughly $0.76 infrastructure;
  - $3 support;
  - approximately $13.38 contribution.
- One-month payback is possible at the target CAC.
- Spanish-language creator distribution can improve trust and keep paid acquisition low.

### Sensitivity

- 204 customers at $49 produce approximately $10K MRR.
- If every customer is on the $19 plan, 527 customers are needed.
- A partner or agency channel is therefore important for efficient scale.
- If generation cost or support rises sharply, the low tier may need a lower quota or annual prepayment.

## 7. Kill criteria

Pause or kill if:

1. Fewer than 4 of 10 interviewed sellers report repetitive catalog production.
2. No pilot seller will provide a real product list.
3. Fewer than 5 catalogs are generated in the first 30 days.
4. More than 25% of descriptions require material factual correction.
5. Users primarily want storefront synchronization rather than a shareable catalog.
6. Fewer than 5 paid accounts after 30 days.
7. Blended CAC exceeds $30 for Vendedor or $75 for Negocio without adequate gross profit.
8. Median import-to-export time exceeds 10 minutes.
9. Monthly churn exceeds 12%.
10. The product requires multi-platform marketplace connectors to be useful.

## Wedge (required for GO_NARROW)

### Narrow wedge

The product serves **independent Spanish-speaking sellers with 10–100 products**, not broad e-commerce teams and not marketplace sellers requiring synchronization.

### What the product refuses to build

- No Shopify, WooCommerce, MercadoLibre, or Etsy synchronization.
- No full storefront, payments, or inventory warehouse.
- No general-purpose design editor.
- No marketplace scraping.
- No bulk WhatsApp outreach.
- No multi-tenant agency approval suite at launch.
- No generic global catalog platform before one seller niche validates retention.

### Explicit expansion condition

Add connectors or agency features only after at least 25 paid sellers have activated, repeat monthly, and identify synchronization as their leading blocker.
