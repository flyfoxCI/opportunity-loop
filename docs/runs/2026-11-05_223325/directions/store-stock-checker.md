# Store Stock Checker — Product Direction

## Direction summary

Build a narrowly focused stock-monitoring service for independent retailers who need to act quickly when a high-demand product returns to stock. The MVP should let an operator connect a small set of retail URLs, configure SKU/product monitoring, receive restock notifications, and manage a lightweight watchlist.

This direction is intentionally not a universal competitor intelligence platform, a full price-history database, or an enterprise procurement system. It is a fast “tell me when this item is available again” tool for small Shopify and WooCommerce merchants.

- **Tier:** GO
- **Demand:** 4/5
- **Competition:** 2/5
- **MVP horizon:** 14 days, solo
- **30-day marketing budget:** $0–$100
- **Target:** $10,000 MRR

## Why this direction

### TrustMRR evidence

The Stage A report records Store Stock Checker at approximately:

- **$274.26 MRR**
- **$274.76 revenue in the prior 30 days**
- **3,594 subscribers**
- Stage A demand score of **4**
- Stage A competition score of **2**

That is one of the strongest named Stage A candidates by subscriber count and one of the strongest by MRR. The near-match between MRR and trailing-30-day revenue suggests a coherent recurring-revenue business rather than a one-off launch spike.

The key strategic implication is not “copy Store Stock Checker.” It is that buyers have demonstrated willingness to subscribe for inventory/restock intelligence. The opportunity is to win a smaller, clearly defined merchant segment with a simpler workflow and more actionable alerts.

### X/web evidence and validation status

The supplied TinyFish evidence did not return usable search results; its stdout contains only TinyFish CLI instructions. Therefore no social quote is represented as independently verified evidence.

Relevant validation and discovery paths include:

- Shopify app marketplaces and app review pages mentioning stock monitoring
- X searches for `back in stock app`, `Shopify stock checker`, `restock alert`, `WooCommerce inventory alert`, and `site:x.com restock app`
- Merchant communities, including Shopify forums, Indie Hackers, Reddit r/shopify, and retail-operator groups

Before implementation, conduct at least:

1. Five interviews with Shopify or WooCommerce merchants
2. One landing-page smoke test with a waitlist or paid deposit
3. A manual concierge test against 20 live SKUs

The implementation decision gate is at least three merchants saying they would replace an existing spreadsheet or browser extension, plus one merchant willing to pay $19–$39 per month.

### Why the wedge is attractive

- The job is frequent and operationally valuable.
- The user can understand the value proposition in seconds.
- A solo founder can build URL/SKU monitoring with scheduled jobs and notifications.
- Early users can be recruited manually through founder-led outreach and merchant communities.
- The product can begin without building a large retail catalog.

## Competitor table

### L1 — direct competitors

| Competitor | Positioning | Typical pricing | Strength | Gap to exploit |
|---|---|---:|---|---|
| Store Stock Checker | Stock/product monitoring and availability alerts | Stage A implies a subscription product; public price should be rechecked | Direct category validation and apparent scale | Opportunity for a simpler onboarding and merchant-first workflow |
| Back-in-Stock apps on Shopify App Store | Restock alerts for store products | Commonly free to low-cost app pricing; verify by app | Native ecommerce integration and broad catalog | Alert quality, shorter setup, faster time-to-value, and explicit support for multiple stores |
| Inventory tracking/restock tools | Inventory dashboards plus low-stock notifications | Entry tiers commonly free; paid tiers vary | Inventory management depth | Those tools often solve stock control rather than competitor/SKU availability monitoring |

**Important constraint:** the prior research index says “Back-in-Stock — Shopify 10+ App — already established.” That conflicts with the Stage A competition estimate. This package preserves the Stage A GO only because it narrows the product to independent merchants and must pass the smoke-test gate. If research confirms ten or more strong direct substitutes with routine low-stock alerts, downgrade this direction to WATCH rather than building the broad version.

### L2 — indirect competitors

| Competitor | Positioning | Pricing pattern | Why users may choose it |
|---|---|---:|---|
| Spreadsheet plus manual checks | Free inventory monitoring | $0 | No new tool to learn |
| Browser extensions/bookmarklets | Manual product-page checks | Often free | Quick one-off checks |
| Store notification apps | Alerts for promotions or back-in-stock events | Free/entry-level | Existing app relationship |
| Email and Discord bots | Scraped availability alerts run by communities | Free or sponsorship-funded | Low acquisition friction, less support |

### L3 — substitutes

| Substitute | Cost | Limitation |
|---|---:|---|
| Staff checking inventory manually | Labor time | Does not scale and creates missed opportunities |
| Supplier notifications | Often included with suppliers | Supplier-specific and often incomplete |
| Marketplace seller messages | No dedicated software cost | Slow and fragmented |

## PRD MVP

### Target customer

Independent Shopify and WooCommerce merchants, usually with 20–1,000 products, who lose meaningful revenue when popular SKUs sell out. The best initial persona is a small apparel, beauty, collectible, or home-goods retailer with a small high-velocity catalog.

### User promise

“See your high-velocity SKUs the moment they return, without checking every storefront.”

### P0 — required for launch

1. **Workspace and URL management**
   - Create one workspace
   - Add a monitored product URL
   - Name the product
   - Add optional expected price, variant, and stock threshold
   - Delete or pause a watch

2. **Manual refresh**
   - Fetch product availability on demand
   - Show current status: in stock, out of stock, unavailable, or check failed
   - Record the last checked time

3. **Scheduled monitoring**
   - Check active watches at a tier-appropriate interval
   - Respect robots directives, rate limits, and site terms
   - Use a compliant data source or approved partner feed where available
   - Retry transient failures

4. **Alerts**
   - Email notification on transition into stock
   - Optional webhook for P1
   - Include product name, URL, detected time, and current displayed price

5. **Watchlist dashboard**
   - Sort by status and last check
   - Show healthy, error, and paused watches
   - Filter out repeated notifications

6. **Billing**
   - Stripe checkout
   - Starter plan with a defined watch limit
   - Customer portal for cancellation and plan management
   - Clear failed-payment handling

7. **Compliance and safety**
   - No bypassing CAPTCHAs, authentication, paywalls, or technical access restrictions
   - Store only data needed for the service
   - Provide a deletion workflow
   - Publish a clear acceptable-use policy

### P1 — first 30-day improvements

- Slack and Discord notifications
- Shopify app installation
- Product catalog import
- Restock history and time-to-restock charts
- Low-stock and price-change notifications
- Custom check intervals
- Team seats
- API key and webhook documentation

### P2 — later

- Supplier CSV imports
- Multi-store analytics
- Competitor pricing history
- Buy recommendations
- Team approval workflows
- Warehouse and inventory sync
- Custom scrapers for sites with permitted feeds

### Non-goals

- Full inventory-management or ERP replacement
- Automated purchasing or supplier ordering in the MVP
- Scraping sites that prohibit it or require bypassing protections
- A universal competitor database
- AI-generated merchandising advice
- Mobile apps
- Multi-country tax or fulfillment management
- Guaranteeing stock accuracy where the retailer has no reliable feed

### Core data model

- **Workspace:** id, owner, plan, created_at
- **ProductWatch:** id, workspace_id, url, product_name, variant, expected_price, status, last_checked_at, next_check_at, active
- **AlertEvent:** id, watch_id, previous_status, new_status, observed_price, created_at
- **NotificationDelivery:** id, alert_event_id, channel, status, delivered_at
- **Subscription:** id, workspace_id, stripe_customer_id, stripe_subscription_id, plan, status
- **CheckLog:** id, watch_id, outcome, response_code, duration_ms, checked_at

### MVP architecture

- Next.js application and dashboard
- PostgreSQL database
- Background job queue or scheduled worker
- Product-specific adapters for one approved platform first
- Email provider such as Resend/Postmark
- Stripe billing
- Sentry or equivalent error monitoring

### Initial pricing hypothesis

- **Starter:** $19/month, up to 25 active watches
- **Growth:** $49/month, up to 150 watches
- **Pro:** $99/month, up to 500 watches and multiple stores

The first pricing is a hypothesis, not a validated fact. Test $19 and $39 in the landing-page smoke test.

## 14-day day-by-day build plan

| Day | Deliverable | Exit criterion |
|---:|---|---|
| 1 | Select the initial platform and legal monitoring method; interview two merchants | One permitted data path and two confirmed user workflows |
| 2 | Create landing page, pricing choice, and onboarding prototype | Headline, CTA, and checkout path are live |
| 3 | Implement accounts, workspace, and product-watch CRUD | A user can create a workspace and watch |
| 4 | Implement compliant fetcher for the first platform | Ten test URLs produce accurate status in manual tests |
| 5 | Add scheduler, retry logic, and state-transition detection | Repeated checks do not produce duplicate alerts |
| 6 | Build email alert templates and delivery logs | In-stock transition reliably reaches the inbox |
| 7 | Build dashboard, pause/delete controls, and billing integration | End-to-end subscription flow works in test mode |
| 8 | Deploy production infrastructure, secrets, backups, and monitoring | Production smoke test passes |
| 9 | Recruit 10 merchants from communities and direct outreach | At least 10 product interviews or onboardings recorded |
| 10 | Onboard five design partners and manually verify alerts | At least three live watches generate correct alerts |
| 11 | Fix onboarding, checkout, and false-positive issues | Fewer than one false positive across 20 test checks |
| 12 | Add onboarding emails, privacy terms, AUP, and status page | New user can self-serve from landing page to watch |
| 13 | Run a pricing smoke test with at least 10 qualified merchants | One paid order or three explicit $19+ purchase commitments |
| 14 | Final reliability pass, founder interviews, and launch decision | MVP meets reliability and willingness-to-pay thresholds |

### MVP technical stack

- Next.js + TypeScript
- PostgreSQL
- Prisma or Drizzle
- Vercel plus a separately schedulable worker
- Stripe
- Resend or Postmark
- Sentry

## 30-day marketing calendar

**Budget: $100 maximum, organic-first**

| Day/channel | Action | Goal |
|---|---|---|
| Days 1–3 | Publish one demo video and a concise “restock monitoring” landing page | Explain the job and collect qualified email addresses |
| Days 4–6 | Manually onboard 15 Shopify/WooCommerce merchants | Five retained watches and three interviews |
| Days 7–9 | Post the demo in Shopify and Indie Hackers communities where promotion is allowed | 100 qualified landing-page visits |
| Days 10–12 | Publish “5 products a store owner should monitor” content | Search traffic and email signups |
| Days 13–15 | Run a free watch-limit trial and founder-assisted onboarding | Ten activated workspaces |
| Days 16–18 | Send personalized onboarding videos to high-intent prospects | Three paid conversions |
| Days 19–21 | Ask successful users for short case studies and referrals | Two case studies |
| Days 22–24 | Publish the first case study with actual recovery/alert metrics | Trust and conversion lift |
| Days 25–27 | Run a $49 “Growth” pricing test versus $19 where appropriate | At least five paid subscribers |
| Days 28–30 | Review activation, false positives, retention intent, and support burden | Decide whether to scale, narrow, or kill |

### Channel mix

- Founder-led outreach: 40%
- Shopify/WooCommerce communities: 25%
- Short-form demo content: 20%
- Referral and customer case studies: 15%
- Paid spend: 0% initially; up to $100 only if a landing page already converts

### 30-day targets

- 50 qualified landing-page visitors
- 20 activated workspaces
- 10 paid customers
- At least $190 MRR
- Fewer than 3% false-positive alerts
- At least 3 retained users at day 30

These are leading indicators, not a guarantee of $10K MRR.

## Unit economics to $10K MRR

### Conservative base case

- Average revenue per account: **$39/month**
- Gross margin: **80%**
- Monthly churn: **5%**
- Monthly gross profit per account at steady state: **$31.20**

Required ending customers:

**$10,000 ÷ $39 ≈ 257 customers**

At 80% gross margin, 257 customers generate approximately **$8,034 gross profit per month** before operating and marketing costs. The $10K MRR target therefore requires roughly 257 customers on the base price mix.

### Pricing mix scenario

| Plan | Customers | Price | MRR |
|---|---:|---:|---:|
| Starter | 120 | $19 | $2,280 |
| Growth | 110 | $49 | $5,390 |
| Pro | 27 | $99 | $2,673 |
| **Total** | **257** | — | **$10,343** |

### Cost assumptions

- Infrastructure: $50–$150/month initially
- Email and monitoring: usage-dependent, budget $50–$200/month
- Support: founder time plus occasional contractor
- Payment fees: approximately 3%
- No paid acquisition requirement in the first 30 days

### Customer acquisition constraint

With a $99 blended monthly gross profit of roughly $79, a sustainable paid CAC ceiling should be around **$40–$60** after allowing for churn and support. Validate this with a small paid test only after organic activation shows at least 20% trial-to-paid conversion.

### Path to 257 customers

- 50 design partners → 10 paying
- 100 customer-led/referral customers
- 80 self-serve or community-sourced customers
- 27 partner/reseller customers

### Expansion revenue

After the base workflow proves reliable, add annual plans, more platforms, Shopify-native install, multi-store support, historical analytics, and webhook/API access. Expansion should be sold only after the core alert workflow retains customers.

## Kill criteria

Kill or pause the direction if any of the following occurs by day 30:

- Fewer than 10 qualified merchants complete onboarding
- Fewer than 3 merchants agree to pay
- Blended trial-to-paid conversion below 15%
- False-positive rate above 5% after adapter fixes
- Median onboarding time above 20 minutes
- Any legal, terms-of-service, or retailer-policy risk cannot be resolved
- Users primarily want a full inventory-management system rather than availability monitoring
- Ten or more strong direct substitutes appear to satisfy the same core job for comparable or lower prices

### Weekly decision checkpoints

- **Day 7:** validate demand and monitoring feasibility
- **Day 14:** require three live customers and one paid order
- **Day 21:** require five paying customers and acceptable alert accuracy
- **Day 30:** require 10 paying customers, 20 activated workspaces, and a credible path to 257 total accounts
