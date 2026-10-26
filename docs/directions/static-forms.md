---
layout: post
title: "Static Forms — Conversion-Focused Form Hosting for Agencies and Indie Hackers"
date: 2026-10-26T21:22:34+00:00
week: "2026-10-26_212234"
week_date: "2026-10-26T21:22:34+00:00"
slug: "static-forms"
permalink: /directions/static-forms.html
tags:
  - "AI"
  - "B2B"
  - "finance"
  - "social"
  - "mobile"
excerpt: "Launch conversion-focused static forms without a heavyweight form-builder backend."
---

## Tier

**GO**

- Demand: **4/5** (working hypothesis)
- Competition: **2/5** (working hypothesis for the narrow wedge)
- MVP target: **14 days, solo**
- Marketing target: **≤ $300 over 30 days**
- Revenue target: **$10K MRR**

## Why this direction

### TrustMRR evidence

Stage A reports Static Forms at approximately **$10 MRR**, **$8.66 in trailing-30-day revenue**, and **124 subscribers**. The product already demonstrates that a small, technically simple form product can attract an audience. The trailing-30-day amount below MRR suggests volatility or reporting timing, so revenue quality must be validated before scaling.

### X/web evidence and validation plan

The supplied TinyFish output did not contain usable web or X evidence. It returned CLI installation text for every query. Therefore, demand and competition remain provisional rather than falsely “verified.”

Run and record the following manually:

- `static website form alternatives 2026`
- `form backend alternatives 2026`
- `site:x.com static site form "looking for"`
- `site:x.com form hosting "too expensive"`
- `site:x.com agency forms "client website"`
- `site:x.com "just shipped" form builder`

Conduct ten interviews with small agencies, freelancers, and indie hackers who deployed a static or React/Next.js site in the past year. Demand score 4 requires at least seven to report a material deployment problem, five to agree to test a prototype, and three to prepay.

### Thesis

Static Forms should solve one narrow problem: **a developer or agency needs to deploy a reliable, branded lead form on a static or JavaScript site without adopting a full form builder, backend server, or heavyweight marketing automation suite.**

The differentiator is not a more flexible drag-and-drop builder. It is:

- A single embed or endpoint
- Fast, accessible forms
- Spam protection
- Webhook and email delivery
- A simple submission inbox
- Predictable pricing
- A one-file setup suitable for agency workflows

## Competitor table

| Level | Competitor | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Formspree | Backend for HTML forms | Free tier plus paid tiers | Direct infrastructure competitor; must beat setup friction and webhook quality |
| L1 | Web3Forms | Simple email-delivery forms | Free tier plus paid paid-use tiers | Strong free/cheap alternative; avoid generic cheap form hosting |
| L1 | Basin | Form endpoint for static sites | Free tier plus paid tiers | Static-site specialist; a direct benchmark |
| L1 | Getform | Form backend for static websites | Free tier plus paid tiers | Static and webhook competitor with a simple value proposition |
| L1 | Formspree-like regional hosts | Trell, FormSubmit, and similar endpoints | Often free or low-cost | Long-tail alternatives make price-only positioning untenable |
| L2 | Tally | Form builder and automations | Generous free tier plus paid tiers | More full-featured; avoid competing on builder breadth |
| L2 | Typeform | Conversational form builder | Free tier plus paid tiers | UX benchmark for conversational forms |
| L2 | Jotform | Broad form builder | Free tier plus paid tiers | Too broad; win on developer simplicity and static deployment |
| L2 | HubSpot, Mailchimp, ConvertKit | Marketing forms embedded in suites | Suite-dependent | Bundled distribution competitor; do not attempt lead management |
| L3 | Cloudflare Workers, Vercel Functions, Netlify Forms | DIY infrastructure | Often low or usage-based | Technical DIY alternative; product must save setup and maintenance time |
| L3 | Google Forms, Microsoft Forms | General free forms | Free | Suitable for simple surveys; less appropriate for branded lead capture and webhooks |

Verify exact pricing and limits before launch. Competition becomes 4 or 5 if Basin, Formspree, and Getform already offer the proposed one-file setup, spam protection, webhooks, custom domains, and comparable pricing with stronger distribution.

## PRD MVP

### Target user and job to be done

**ICP:** Solo web developers, small studios, and agencies that ship static sites and need client lead forms.

**JTBD:** “When a client needs a lead form on a static site, I want to paste one endpoint and receive clean notifications and webhooks without configuring a backend or another large SaaS suite.”

### P0 — required for launch

1. **Form creation**
   - Name, fields, required flags, placeholder, help text, and success message.
   - Text, email, phone, textarea, select, checkbox, and hidden-field types.
   - Minimum viable conditional logic only if the builder can be completed reliably by day 9.
2. **Embed modes**
   - Standard JavaScript embed.
   - Plain HTML form/action endpoint.
   - React and Next.js-compatible snippet.
3. **Submission pipeline**
   - Server-side validation.
   - Spam heuristics and honeypot.
   - Duplicate protection and submission storage.
   - Email notification containing the submission.
4. **Webhooks**
   - Signed outbound webhook with retries.
   - Destination test button and event log.
5. **Submission inbox**
   - List, search, and basic CSV export.
6. **Branding**
   - Custom domain or custom branding field where infrastructure allows.
   - Basic color, font, border-radius, and button settings.
7. **Account and billing**
   - Magic-link authentication.
   - Free usage limit.
   - Stripe subscription and usage meter.
8. **Developer controls**
   - Endpoint documentation.
   - Copy-paste HTML and React snippets.
   - Test submissions separated from production data.
9. **Privacy**
   - Data-processing disclosure.
   - Submission deletion.
   - Webhook signing secret and basic IP-abuse controls.

### P1 — after launch validation

- Domain allowlist.
- Custom email templates.
- File uploads.
- Conditional fields.
- Slack and Discord destinations.
- Zapier/Make connector.
- Multi-user access.
- Form templates for lead capture, waitlist, and support.
- Custom domains.
- Embed loading performance controls.

### P2 — later expansion

- Advanced logic and calculations.
- Partial submissions.
- Team roles.
- ABM and CRM integrations.
- A pluggable framework SDK.
- WordPress and Shopify plugins.
- Analytics dashboard.
- White-label agency mode.

### Non-goals

- Full drag-and-drop page builder.
- Surveys and complex analytics.
- CRM.
- Marketing automation.
- Payment processing.
- Native mobile apps.
- Multi-page forms.
- Hosting client websites.
- Building a general backend platform.
- Competing with every free form endpoint.
- AI-generated forms in MVP.

### Core UX

1. Create an account.
2. Choose a template.
3. Add fields.
4. Configure notifications and webhook.
5. Copy an embed snippet.
6. Test the endpoint.
7. Submit and monitor incoming leads.

Time from signup to first production embed should be under five minutes.

### Technical approach

- **Frontend:** Next.js + TypeScript + Tailwind CSS.
- **API:** Next.js route handlers plus a small dedicated submission service if separation improves reliability.
- **Database:** Managed Postgres.
- **Queue:** Managed job queue for email and webhook delivery.
- **Storage:** Encrypted submission data and optional file storage.
- **Payments:** Stripe.
- **Email:** Transactional provider with signed, templated messages.
- **Observability:** Delivery logs, endpoint latency, error rate, spam rate, and webhook attempts.

### Core data model

- `users`
- `workspaces`
- `forms`
- `form_fields`
- `submissions`
- `submission_values`
- `webhook_endpoints`
- `webhook_deliveries`
- `notifications`
- `plans`
- `usage_events`

### Security and reliability baseline

- Validate and sanitize every field.
- Limit request body size and upload size.
- Apply IP and form-level rate limits.
- Use signed webhooks and replay-resistant timestamps.
- Encrypt submissions at rest.
- Do not log full submission bodies.
- Protect secret keys from browser code.
- Maintain deletion workflows.
- Provide status and retry information for every webhook.
- Prevent open redirects and unsafe iframe behavior.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criteria |
|---:|---|---|
| 1 | Customer validation and competitor audit | Ten interviews; ten competitors checked; API and UX scope frozen |
| 2 | Landing-page and pricing smoke test | One page, live email capture, fake-door checkout, and five qualified leads |
| 3 | Account and workspace shell | Magic-link auth, workspace, plan state, and usage counters |
| 4 | Form schema and builder | All P0 field types; draft, edit, duplicate, and delete |
| 5 | Submission endpoint | Validation, storage, honeypot, rate limits, and test mode |
| 6 | Embeds | JavaScript, plain HTML, React, and Next.js snippets work on test pages |
| 7 | Email notifications | Templates, sender controls, retry, and delivery logs |
| 8 | Submission inbox | Search, details, deletion, and CSV export |
| 9 | Webhooks | Signed payloads, retries, test delivery, and delivery history |
| 10 | Styling and branding | Responsive theme controls and accessible defaults |
| 11 | Billing and limits | Stripe checkout, portal, quotas, upgrade/downgrade behavior |
| 12 | Abuse controls and reliability testing | Spam tests, malformed payloads, duplicate submissions, and load checks |
| 13 | End-to-end, accessibility, and docs | Agency workflow completed; keyboard and screen-reader pass; snippets copy cleanly |
| 14 | Launch readiness | 10 external test forms, monitoring, backups, status page, and support flow |

### Definition of done for day 14

A developer can create a form, paste an embed, receive a validated submission in the inbox and email, verify a signed webhook, and subscribe to a paid plan without founder help.

## 30-day marketing calendar

### Marketing thesis

The best organic channel is the existing technical audience of agencies, indie hackers, and static-site developers. Demonstrate the shortest path from `<form>` to a reliable endpoint, then invite users to embed a test form on their own sites. Avoid generic “build forms faster” copy.

### Budget: $240 maximum

| Item | Budget |
|---|---:|
| Domain, email, and demo assets | $40 |
| One narrowly targeted newsletter sponsorship | $100 |
| Developer-tool documentation or community sponsorship | $60 |
| Test/production infrastructure overage | $20 |
| Contingency | $20 |
| **Total** | **$240** |

### Calendar

| Day | Action | Target |
|---:|---|---|
| 1 | Launch “One endpoint for forms on static sites” page | 100 qualified visits |
| 2 | Publish a 60-second embed video | 8 qualified signups |
| 3 | Contact 20 static-site agencies and freelancers | 5 calls |
| 4 | Publish a comparison: form endpoint vs serverless setup | 10 discussions |
| 5 | Share a copy-paste Next.js form example | 15 trial accounts |
| 6 | Offer five free form audits | 3 agency referrals |
| 7 | Review signup → form → embed → submission funnel | Fix largest drop-off |
| 8 | Post in one static-site or indie-hacker community | 10 trials |
| 9 | Publish webhooks + signed-delivery documentation | 5 integrations |
| 10 | Add a plain HTML form example for non-React users | 8 trials |
| 11 | Interview trial users who did not embed | 5 interviews |
| 12 | Ship one-click Slack notifications | 5 paid conversions |
| 13 | Publish reliability notes and delivery metrics | 8 qualified leads |
| 14 | Mid-month review | Activation ≥25%; paid conversion ≥3% |
| 15 | Contact 20 agency owners | 8 demos |
| 16 | Publish a white-label agency workflow | 3 agency trials |
| 17 | Create a lead-capture form template | 10 starts |
| 18 | Run a live build-along | 15 attendees, 5 trials |
| 19 | Offer a two-week Pro trial to qualified agencies | 5 paid conversions |
| 20 | Publish a founder teardown of setup time | 6 leads |
| 21 | Add webhook event history and replay | 5 activations |
| 22 | Contact developers of static-site plugins | 3 integration conversations |
| 23 | Publish a migration guide from another form backend | 8 trials |
| 24 | Review support tickets and delivery failures | Resolve top two classes |
| 25 | Create referral credits for successful embed | 10 referred trials |
| 26 | Publish a customer implementation story | 5 leads |
| 27 | Test annual plan with retained users | 3 upgrades |
| 28 | Improve onboarding for framework choice | Activation +10% |
| 29 | Publish a transparent uptime/reliability report | 6 qualified leads |
| 30 | Month-two review and decision | 20 active accounts; $500+ MRR |

### Weekly content pillars

1. **Short setup demos:** plain HTML, React, and Next.js.
2. **Reliability engineering:** signed webhooks, retries, spam, and uptime.
3. **Agency workflows:** reusable templates, client handoff, and white-label potential.
4. **Build notes:** public decisions, failures, and speed improvements.

### Activation and funnel targets

- Visitor → signup: **≥12%**
- Signup → form created: **≥60%**
- Form created → embedded: **≥45%**
- Embedded → first submission: **≥80%**
- Qualified visitor → paid: **≥3%**
- Paid → second form or second month: **≥70%**
- Monthly logo churn: **<6%**

## Unit economics to $10K MRR

### Pricing

- **Free:** 1 form, 50 submissions/month, basic email notification
- **Pro:** $19/month — 5 forms, 2,000 submissions, webhooks, custom branding, remove branding
- **Studio:** $49/month — 20 forms, 10,000 submissions, 5 users, agency features
- **Business:** $99/month — 100 forms, 50,000 submissions, higher limits and priority support

### Revenue mix at target

| Plan | Customers | MRR |
|---|---:|---:|
| Pro | 300 | $5,700 |
| Studio | 70 | $3,430 |
| Business | 9 | $891 |
| **Total** | **379** | **$10,021** |

Round the plan to **380 paying customers for approximately $10K MRR**.

### Cost assumptions

Typical Pro account:

- 1,000 submissions/month
- Validation, storage, email, and webhook cost: approximately $1.20/month
- Infrastructure and processing: approximately $1.80/month
- Gross contribution: approximately $16 before acquisition

Illustrative blended variable cost: **$2.50/customer/month**.

### Gross margin and acquisition

- MRR: approximately $10,000
- Variable cost: approximately $950
- **Gross margin:** approximately 90%
- Maximum blended CAC for three-month payback: approximately **$90**
- Target blended CAC: **≤$40**
- Required paid acquisitions: approximately **55–75 per month**

The plan must not rely on paid ads to reach the target. If organic activation and referral loops cannot produce at least 25 qualified trials per week, reassess the market or pricing.

### Validation milestone

Reach **30 paid accounts and $500 MRR** before investing in broader acquisition. Recalculate gross margin from actual email, storage, support, and infrastructure costs.

## Kill criteria

Kill or reposition the direction if:

1. Fewer than **3 paid preorders** from 30 qualified users.
2. Fewer than **20%** of qualified visitors create a form within 30 days.
3. Fewer than **40%** of created forms reach a first submission.
4. Paid conversion remains below **2%** after two onboarding changes.
5. Trial-to-paid conversion remains below **3%** after 100 activated accounts.
6. Monthly paid churn exceeds **8%** in the first 50-account cohort.
7. Effective CAC exceeds **$90**.
8. Delivery or spam-control failures produce more than **1%** of form submissions being falsely blocked.
9. Webhook success is below **99.5%** after retries.
10. Gross margin falls below **80%** due to volume-dependent email, storage, or abuse costs.
11. Agencies primarily demand a full page builder, CRM, or marketing suite; that would invalidate the narrow wedge.
12. Basin, Getform, Formspree, and Web3Forms collectively already provide materially better developer workflow and pricing.
