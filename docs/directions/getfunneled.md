---
layout: post
title: "Get Funneled — Opportunity Direction"
date: 2026-11-10T00:32:56+00:00
week: "2026-11-10_003256"
week_date: "2026-11-10T00:32:56+00:00"
slug: "getfunneled"
permalink: /directions/getfunneled.html
tags:
  - "B2B"
  - "education"
  - "social"
  - "proposal"
  - "mobile"
  - "vertical"
excerpt: "A focused landing-page funnel builder that turns one service offer into a conversion-ready page, variants, and lead capture in minutes."
---

## 1. Why this direction

### Opportunity

Create a focused funnel-building product for one service business that wants to publish a landing page and collect qualified leads without managing a full marketing stack. The initial product should transform a structured offer into a responsive landing page, support a small number of page variants, capture leads, and provide a concise activity report.

### Target customer

The primary ICP is a solo consultant, agency, local professional, or small B2B service provider that:

- Sells one relatively clear service.
- Gets leads from word of mouth, outbound, directories, or social media.
- Does not want to learn a general page builder.
- Needs a useful page live within hours rather than days.
- Can be charged roughly $39–$99 per month.

The first niche should be selected before implementation. The recommended starting niche is independent B2B consultants; alternatives include local home-service providers and boutique agencies. Do not attempt to serve all three at once.

### TrustMRR evidence

Stage A reports Get Funneled at:

- MRR: **$184.06**
- Last 30 days: **$190.62**
- Subscribers: **22**
- Stage A demand score: **4**
- Stage A competition score: **2**
- Website: https://getfunneled.com
- X handle: `@claridgicus`

The approximately $190 recent revenue with only 22 subscribers implies an estimated blended revenue per subscriber of roughly $8.60 per month. This may reflect a free tier, low-priced plans, or an unusually recent revenue spike; pricing must be checked directly. Despite that ambiguity, the listing is one of the strongest Stage A candidates because it combines meaningful revenue, positive recent momentum, a named product, and a website.

### X and web evidence

The supplied automated search output is invalid for evidentiary use: all TinyFish queries returned CLI help text rather than search results. The product website and the X handle must therefore be checked manually.

Suggested verification queries:

- `"Get Funneled" (painful OR broken OR hate OR expensive)`
- `"Get Funneled" (looking for OR recommend OR alternative)`
- `"landing page" (painful OR hate OR "takes too long")`
- `"funnel builder" (painful OR broken OR hate)`
- `site:x.com "Get Funneled"`
- `site:reddit.com landing page builder agency lead capture`

Demand validation requires at least 10 dated posts from the past 12 months, including at least five explicit pain statements and at least three recommendations of alternatives. Record the URL, date, audience, and exact pain quote.

### Why it can win

The product should not attempt to reproduce a general-purpose page builder. Its wedge is the short path from a structured service offer to a published, lead-capturing page. The first release needs only templates, fields, a visual editor, publishing, and lead capture.

### Validation gate

Proceed only if:

1. Ten interviews or public pain posts confirm that page creation speed or lead capture is a frequent problem.
2. At least five interviewees agree to test a concierge-built page.
3. Three provide a real offer and current customer questions for the prototype.
4. Two agree to pay $49 or more for the first version.

Do not code until these criteria are met.

## 2. Competitor table

### L1 direct competitors

| Competitor | Typical positioning | Pricing to verify | Strength | Opening for Get Funneled |
|---|---|---:|---|---|
| Get Funneled | AI-oriented funnel creation, to verify | Unknown | Existing audience and paid revenue | Improve onboarding, offer-specific templates, and transparent pricing |
| Carrd | Simple responsive landing pages | Free plus paid plans | Speed, polish, broad awareness | Faster service-offer setup, lead capture, and experiment workflow |
| ConvertKit | Creator landing pages and email marketing | Free plus paid plans | Creator ecosystem and integrations | Focused funnel generation without requiring a full email suite |
| Kit | Creator commerce and landing pages | Paid creator plans | Strong product suite and creator distribution | Narrower, faster service-business funnel workflow |
| Unbounce | Landing-page experimentation for marketing teams | Enterprise-oriented paid plans | Established brand and experimentation features | Faster setup and accessible solo-business pricing |
| Instapage | Enterprise landing-page platform | Enterprise paid plans | Collaboration, testing, integrations | Minimal setup, fewer features, lower complexity |
| Leadpages | Landing-page templates and conversion features | Paid monthly plans | Templates, marketing ecosystem | Better service-offer defaults and faster first publish |

All pricing and feature claims must be checked on the vendor's official pricing page immediately before implementation. These are representative direct alternatives, not a final count.

### L2 alternatives

| Alternative | Why users choose it | Disadvantage / opening |
|---|---|---|
| Webflow | Design control and flexibility | Learning curve and build time |
| Framer | High-quality sites and design freedom | Not optimized for lead funnels |
| WordPress + page builder | Familiarity and ecosystem | Maintenance and plugin complexity |
| Shopify landing pages | Existing commerce stack | Poor fit for non-commerce service offers |
| Google Forms | Extremely fast and free | Weak presentation, routing, and conversion design |
| Canva | Familiar visual creation | Not a publish-and-capture funnel system |
| Hand-coded HTML | Maximum control | Requires technical and deployment work |

### L3 substitute behavior

- Copy an existing template and edit it manually.
- Ask an agency or freelancer to build the page.
- Use a spreadsheet plus a basic form.
- Continue using a general website and route traffic to a form.
- Do nothing and rely entirely on outbound or referrals.

### Competition score

**Score: 2/5 for the narrow wedge**, contingent on the following positioning:

> A landing-page funnel builder specifically for one service-business niche, optimized from offer input to qualified-lead capture.

The general landing-page market is competitive. The score is defensible only if product scope, templates, onboarding, and messaging remain constrained to that narrow job. If broad page-building capabilities are added, raise competition to 4 and switch to `GO_NARROW`.

## 3. PRD — MVP

### Product promise

Turn a service offer into a publishable, lead-capturing landing page in under 15 minutes.

### P0 — launch-critical

1. **Offer intake**
   - Business type, service title, offer description, proof points, desired lead fields, and CTA.
   - One recommended vertical template.
   - No universal editor in the first version.

2. **Generated page**
   - Responsive single-page layout.
   - Hero, problem, offer, proof, FAQ, and CTA sections.
   - Editable text, image, color, and CTA label.
   - Preview at mobile and desktop widths.

3. **Publishing**
   - One URL under the product domain.
   - Custom-domain connection is optional or may be postponed if it threatens the 14-day limit.
   - Basic Open Graph metadata and favicon.

4. **Lead capture**
   - Name and email by default.
   - Optional phone, company, or appointment URL.
   - Consent copy, spam honeypot, and rate limiting.
   - Lead inbox with CSV export.
   - Email notification on new lead.

5. **Account and billing**
   - Email magic-link authentication.
   - One paid plan and a 7-day trial.
   - Stripe checkout and customer portal.
   - Plan limit: one active page and 50 leads/month on the MVP plan.

6. **Trust and basics**
   - Privacy policy, terms, contact route, and deleted-export path.
   - Basic analytics: page views, CTA clicks, and submissions.
   - Error monitoring and database backups.

### P1 — first 30 days

- Two niche-specific template sets.
- A/B test between two hero variants.
- Calendar or booking integration.
- Slack notification.
- More lead fields.
- Domain configuration.
- Usage and conversion dashboard.

### P2 — after product-market signal

- Team workspaces.
- Multiple pages and funnels.
- Custom JavaScript.
- Advanced integrations and API.
- Template marketplace.
- AI copy generation beyond structured offer intake.

### Non-goals

- General drag-and-drop website building.
- E-commerce, payments, or checkout.
- Native email marketing.
- CRM functionality.
- Pop-ups and complex multi-step funnels in the MVP.
- Guaranteed conversion claims.
- Domain registrar.
- Mobile applications.
- Automated outbound sales.
- Multi-language funnels before one niche is validated.
- Replacing a full CMS, experimentation suite, or agency workflow.

### Core user stories

- As a consultant, I want to describe my offer once so that I do not have to learn a page builder.
- As a consultant, I want a credible page quickly so that I can start collecting leads this week.
- As a consultant, I want every lead in one inbox so that I can respond promptly.
- As a consultant, I want to understand visits, CTA clicks, and submissions so that I can improve my page.
- As an agency, I want a repeatable niche workflow so that I can create pages for clients faster.

### MVP acceptance criteria

A first-time user can:

1. Create an account.
2. Enter an offer using the target niche template.
3. Publish a responsive page.
4. Visit the page from mobile and desktop.
5. Submit a test lead.
6. Receive the lead notification.
7. Export the lead.
8. Upgrade through Stripe.

### Technical recommendation

- Next.js or a similar TypeScript web framework.
- PostgreSQL for users, pages, leads, and events.
- Stripe Billing.
- Resend for transactional email.
- Object storage plus an image CDN.
- A component library with a constrained template system.
- Moderation and delivery safeguards for user-uploaded images.
- Deployment platform with preview environments and database backups.

The implementation must avoid building a general-purpose visual editor. Use a fixed schema, conditional sections, and typed fields so the 14-day scope remains realistic.

## 4. 14-day build plan

| Day | Objective | Deliverables | Exit criterion |
|---:|---|---|---|
| 1 | Validate niche and scope | Select one ICP; conduct three interviews; define fixed template schema; write one-page brief | Five problem confirmations or a pivot signal |
| 2 | Validate willingness to pay | Present the concierge prototype and $49 price; collect two deposits or explicit purchase commitments | Two paid commitments, otherwise stop/reframe |
| 3 | Product foundation | Auth, database schema, billing test, environments, error logging, deployment pipeline | A test user can sign up and complete a checkout sandbox flow |
| 4 | Offer input | Structured offer form, vertical defaults, validation, saved draft | A user can create a complete draft |
| 5 | Page renderer | Responsive sections, theme tokens, editable content, preview | Five test offers render without developer intervention |
| 6 | Publishing | Public URL routing, metadata, page status, basic domain abstraction | A page can be published and shared |
| 7 | Lead capture | Form, validation, consent, spam controls, database storage, email alert | End-to-end lead test passes |
| 8 | Lead management | Inbox, detail view, CSV export, search, basic analytics | Five test leads can be found and exported |
| 9 | Billing and limits | Stripe live mode, trial, plan limits, customer portal | Payment, cancellation, and webhook paths pass |
| 10 | Onboarding | Niche template, sample offer, checklist, progress state | New tester reaches published page in 15 minutes |
| 11 | Quality and safety | Accessibility pass, mobile QA, privacy policy, terms, upload limits, backup restore | No critical P0 defects; backup restore succeeds |
| 12 | Pricing and onboarding assets | Pricing page, sample page, FAQ, onboarding email sequence | Pricing and product claims are consistent |
| 13 | Pilot | Onboard 10 target users; observe sessions; fix top three friction points | Five pilot users publish without assistance |
| 14 | Release | Fix release blockers, deploy, invite waitlist, instrument funnel | Five live pages and ten real qualified leads, or an explicit no-go review |

### Daily operating rule

Every day ends with a deployable increment and one measurable outcome. New features that do not improve activation, publishing speed, or lead capture are deferred.

## 5. 30-day marketing calendar

### Budget

Total maximum: **$300**

| Activity | Budget |
|---|---:|
| Micro-incentives for research calls and pilot users | $100 |
| Domain, landing-page assets, and basic creative tools | $50 |
| Targeted sponsored posts to validated niche groups | $100 |
| Referral or customer-success reward reserve | $50 |
| **Total** | **$300** |

No broad paid search, influencer deals, or generic content sponsorship during month one.

### Organic-first plan

| Day | Activity | Channel | CTA | Success signal |
|---:|---|---|---|---|
| 1 | Publish problem statement using exact interview language | LinkedIn, founder account | Request a 15-minute workflow interview | 5 replies |
| 2 | Share anonymized “manual funnel to page” workflow | LinkedIn, niche group | Join concierge pilot | 3 signups |
| 3 | Post before/after offer-to-page walkthrough | LinkedIn, X | Use the template | 2 template uses |
| 4 | Publish a niche-specific landing-page teardown | LinkedIn, Reddit where allowed | Comment with diagnosis | 8 qualified comments |
| 5 | Run five customer interviews | Direct outreach | Validate prototype | 5 interviews |
| 6 | Release the first niche template | Product hunt / relevant community | Try free trial | 10 trials |
| 7 | Send case study from a pilot result | LinkedIn, email | View page builder | 5 qualified visits |
| 8 | Publish “five offer details your landing page needs” | Blog, LinkedIn | Start offer draft | 8 drafts |
| 9 | Post a short workflow demo | LinkedIn, X | Publish a page | 5 publishes |
| 10 | Ask pilot users for recorded walkthroughs | Email | Join referral program | 3 recordings |
| 11 | Publish objection-handling page | Blog, LinkedIn | Start trial | 6 signups |
| 12 | Contact 30 relevant consultants or agencies individually | Personalized email / LinkedIn | Request page review | 8 positive replies |
| 13 | Host a public teardown clinic | YouTube live, LinkedIn event | Bring an offer | 15 attendees |
| 14 | Release v1 to waitlist | Email, communities | Publish | 10 activations |
| 15 | Share launch metrics transparently | Founder account | Join waitlist | 5 warm leads |
| 16 | Publish a lead-capture conversion checklist | LinkedIn, blog | Use checklist | 10 downloads |
| 17 | Interview activated users | Email, call | Continue or churn | 5 responses |
| 18 | Add a niche-specific FAQ template | Product, LinkedIn | Try template | 6 uses |
| 19 | Publish a customer story | LinkedIn, case-study page | View example | 4 leads |
| 20 | Run a design-partner push with five agencies | Direct outreach | Pilot workspace | 2 commitments |
| 21 | Post a “page versus full website” explainer | Blog, LinkedIn | Start trial | 8 trials |
| 22 | Release referral credits | Email, app | Refer a colleague | 10 referral clicks |
| 23 | Publish a funnel anatomy template gallery | SEO, social | Use gallery | 15 gallery visits |
| 24 | Run a pricing objection survey | Email | Choose plan | 15 responses |
| 25 | Contact churn-risk users | Email | Schedule rescue | 5 rescues |
| 26 | Publish founder retrospective | LinkedIn, blog | Join waitlist | 8 signups |
| 27 | Co-create a page with a niche expert | Live stream | Build with template | 12 attendees |
| 28 | Announce the strongest workflow improvement | Email, LinkedIn | Upgrade | 3 upgrades |
| 29 | Offer a migration/setup session to first 20 users | Email, calls | Complete setup | 10 setups |
| 30 | Review cohort economics and publish next-month plan | Internal, email | Book next cohort | Clear keep/kill decision |

### Acquisition targets

By day 30:

- 100 qualified landing-page visits.
- 30 trials.
- 15 activated users.
- 8 paid customers.
- $392 MRR at a $49 monthly price.
- At least 10 customer interviews and five public pain quotes captured.

## 6. Unit economics to $10K MRR

### Proposed pricing

- Trial: 7 days.
- MVP plan: **$49/month**.
- Optional later Pro tier: $99/month after usage limits become clear.

Do not price solely from the existing listing's implied revenue. Validate willingness to pay first.

### Conservative initial model

At $49/month:

| Metric | Conservative | Target | Strong |
|---|---:|---:|---:|
| MRR needed for $10K | $10,000 | $10,000 | $10,000 |
| Customers | 205 | 205 | 205 |
| Gross margin | 85% | 90% | 93% |
| Gross profit/customer/month | $41.65 | $44.10 | $45.57 |
| Acquisition allowance/customer | $75 | $100 | $125 |
| Months to $10K at constant acquisition | 40.4 | 35.3 | 32.3 |
| Churn assumption | 6% | 4% | 3% |

At a blended $79/month from a mix of $49 and $99 plans, 127 customers produce $10,033 MRR.

### Required efficiency

- Trial-to-paid: at least 20%.
- Activation, defined as published page plus one real lead: at least 50% of trials.
- Monthly logo churn: below 6%.
- Gross margin: at least 85%.
- Fully loaded CAC: below $125.
- Payback: under six months.
- LTV at $79 ARPA, 90% gross margin, and 4% churn: approximately **$1,421**; CAC:LTV should exceed 5:1.

### Budget reality

A $300 marketing budget cannot directly acquire 205 customers. The path is:

1. Founder-led outreach and community distribution.
2. Organic content and reusable templates.
3. Referral loops.
4. A high-retention product that generates customer stories.
5. Partner or agency channels where the product saves enough time to earn a referral fee.

The $10K MRR objective is a 3–6 month target after validation, not a claim that the first $300 will generate all customers.

### Scenario checkpoints

At month 3:

- Fewer than 5 paying customers: stop broad scope and interview churn/non-activation.
- 5–14 customers: keep the niche, improve activation, and double down on direct outreach.
- 15+ customers and positive retention: prepare self-serve onboarding and begin a partner channel.

## 7. Kill criteria

Stop or materially reframe if any of the following occurs:

1. Fewer than 5 of 20 qualified prospects report the problem as important.
2. No prospect agrees to pay $49 or more after a concierge demonstration.
3. First-time users cannot publish in 20 minutes without assistance.
4. Activation remains below 30% after two onboarding iterations.
5. Trial-to-paid remains below 10% after 50 qualified trials.
6. Monthly churn exceeds 10% for two cohorts.
7. No channel can produce qualified traffic below $150 per customer.
8. Two customers with the same core requirement still need substantially different product concepts.
9. Competitor research reveals more than three entrenched direct alternatives with the exact niche workflow and acceptable pricing.
10. Scope expands toward a general page builder, forcing a competition score of 4 or 5.
11. Liability, spam, accessibility, or security issues cannot be resolved within the MVP scope.
12. The founder cannot deliver ten personal outreach conversations per week.

## Wedge (required for GO_NARROW)

Not applicable: this direction is tier **GO** under the stated narrow positioning. If demand validation reveals that the broad landing-page category has competition 4, retain only this wedge:

> Build landing pages for one service-business niche, with fixed offer structure, one responsive template family, lead capture, and conversion reporting. Refuse custom layouts, multi-page sites, ecommerce, native email marketing, and general-purpose drag-and-drop editing.
