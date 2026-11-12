# Static Forms — Direction Package

## Why this direction

### TrustMRR evidence

- Static Forms was classified `GO_CANDIDATE` with **$10.39 MRR**, **$12.47 in last-30-day revenue**, and **134 subscribers**.
- Its demand heuristic was **4**, while its competition heuristic was **2**.
- The product has a compact outcome: a user creates a static landing page or form and receives a usable endpoint without maintaining an application server.
- The revenue signal is modest but consistent with an early-stage niche product. The important opportunity is not to copy a generic form builder; it is to own a specific workflow where users deliberately want a static deployment and minimal maintenance.

### X/web evidence

- Stage A identified the public handle **@hussainanjar** for Static Forms.
- The strongest web demand signals are the recurring needs for:
  1. zero-backend forms;
  2. static-site-compatible form handling;
  3. inexpensive client acquisition for small service businesses;
  4. forms that work inside sites hosted on platforms such as Netlify, Cloudflare Pages, GitHub Pages, and Vercel.
- The supplied TinyFish output did not expose usable result excerpts—it returned CLI installation guidance—so no specific X post is claimed as independently verified.
- Competitive interpretation: a horizontal form builder such as Formspree, Web3Forms, Basin, Getform, or a native form editor would be too broad. The selected wedge is **static landing pages with hosted form collection for service-business lead capture**, where the deployment and handoff experience can be simpler than a general-purpose form builder.
- **Final score: demand 4, competition 2 → GO.**

## Competitor table

> Pricing is directional and may change. Verify before launch.

| Level | Competitor | Pricing found or typical positioning | Strength | Opening for Static Forms |
|---|---|---:|---|---|
| L1 direct | Static Forms | Free tier indicated by public positioning; paid pricing to verify | Static-first workflow | Add one-vertical templates, lead routing, and deployment guides. |
| L1 direct | Formspree | Free tier with paid usage tiers | Mature integrations and reliability | Own static-first simplicity, transparent usage pricing, and instant deploy. |
| L1 direct | Basin | Free tier plus paid usage tiers | Form endpoint workflow and developer reputation | Faster landing-page creation and clearer SMB setup. |
| L1 direct | Web3Forms | Free tier with usage-based paid access | Very low-cost basic form endpoint | Bundle page, form, routing, and CRM handoff rather than endpoint alone. |
| L1 direct | Getform | Free tier plus paid plans | Simple embedded forms | Provide superior static-page generation and ownership portability. |
| L2 | Tally | Free tier and paid usage plans | Excellent no-code form UX | Narrow around static deploys and agency-ready lead routing. |
| L2 | Google Forms | Free | Ubiquitous and simple | Better lead delivery, branded pages, and conversion analytics. |
| L2 | HubSpot Forms | Entry tier free; paid ecosystem | CRM integration and enterprise distribution | Serve solo service providers without CRM complexity. |
| L3 | Cloudflare Pages / Netlify Forms / Vercel | Often free or low-cost deployment | Excellent hosting ecosystems | Use integrations rather than compete on hosting. |

### Competition score rationale

**2/5.** There are many substitutes, but they split across form endpoints, no-code form builders, static hosting, and all-in-one lead tools. A general-purpose form builder would be crowded. The explicit narrow implementation—static landing pages plus form collection and lead delivery for service businesses—is sufficiently focused for a solo MVP.

## PRD MVP

### Target customer

- Solo service businesses: photographers, consultants, coaches, local repair businesses, and independent agencies.
- Small agencies that need one-off campaign pages without deploying an app.
- Developers who prefer static hosting and want a simple hosted form endpoint.

### Core job

> “I want a fast, professional lead-capture page that works with my static site, routes leads where I need them, and does not require me to maintain a backend.”

### P0 — required for launch

1. **Static page builder**
   - Title, subtitle, body, image, logo, primary CTA, and FAQ blocks.
   - Mobile-first preview.
   - Editable color and typography tokens.
   - HTML/CSS export.
2. **Form builder**
   - Name, email, phone, company, budget/timeline, and message fields.
   - Required, placeholder, helper-text, and validation controls.
   - Anti-spam honeypot plus rate limiting.
3. **Hosted endpoint**
   - Published page receives submissions.
   - Submission dashboard with CSV export.
   - Email notification to the owner.
4. **Lead delivery**
   - Webhook and Zapier/Make-compatible endpoint.
   - Plain-text email fallback.
5. **Account and billing**
   - Email-based signup.
   - Workspace/project model.
   - Starter free plan and one paid usage plan.
6. **Operational basics**
   - Custom domain instructions for major static hosts.
   - Privacy consent checkbox.
   - Basic analytics: views, form starts, and submissions.
   - Deletion and data-export controls.

### P1 — after launch validation

- Saved templates for one selected vertical.
- Slack notification.
- CRM presets for HubSpot, Pipedrive, and Mailchimp.
- A/B testing of headline and CTA.
- Embed code for forms in an existing static page.
- Scheduled page expiration and draft pages.
- Appointment scheduling link.
- Team roles for agencies.

### P2 — later

- White-label agency mode.
- Custom domains.
- Approvals and client sign-off.
- Multiple team members.
- AI-assisted page copy.
- Native integrations with selected static hosts.
- CRM two-way sync.

### Explicit non-goals for the first 14 days

- No general-purpose drag-and-drop app builder.
- No payment processing.
- No native mobile apps.
- No enterprise SSO.
- No custom code execution.
- No complex workflow automation.
- No claims that generated pages maximize conversion.
- No rebuilding of a full CRM or email-marketing platform.
- No HIPAA, financial, or legal compliance positioning.

### Technical approach

- Frontend: Next.js/TypeScript or a similarly simple full-stack framework.
- Database: PostgreSQL.
- Authentication: passwordless email link or hosted auth.
- File storage: object storage with signed uploads.
- Email: transactional provider.
- Deployment: one public app plus optional static export; a serverless function handles form submissions and webhooks.
- Data model: `User`, `Workspace`, `Project`, `Page`, `FormField`, `Submission`, `Notification`, `Webhook`, `Domain`.
- Security controls: parameterized queries, encrypted secrets, rate limits, hashed one-time links, spam heuristics, and signed file URLs.

### Pricing hypothesis

- **Free:** one page, 25 submissions/month, basic notifications.
- **Starter — $19/month:** three active pages, 500 submissions, custom branding, webhooks.
- **Growth — $49/month:** ten active pages, 2,000 submissions, integrations, multiple domains.
- **Agency — $99/month:** 25 projects, client workspaces, higher limits, priority support.
- Optional submission overages are acceptable, but the first version should favor simple subscription predictability.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criterion |
|---:|---|---|
| 1 | Scope lock and design system | One vertical selected; page schema, form schema, and analytics events finalized. |
| 2 | Project scaffolding | Auth, database migrations, workspace/project models, and local development environment work. |
| 3 | Page builder | Add/edit/reorder blocks; autosave; mobile preview; exportable HTML. |
| 4 | Form schema and validation | Required fields, email/phone validation, conditional display, and error states. |
| 5 | Public publishing | Slug routing, HTTPS, immutable publish version, and indexable/noindex control. |
| 6 | Submission pipeline | Form endpoint, database write, anti-spam, rate limit, and confirmation state. |
| 7 | Submission dashboard | Filter/search, detail view, CSV export, retention setting, and delete action. |
| 8 | Lead delivery | Transactional email, webhook signing/retry, and delivery logs. |
| 9 | Billing | Checkout, subscription state, plan limits, cancellation, and upgrade path. |
| 10 | Templates and onboarding | One vertical template, copyable starter project, import sample submissions, and guided setup. |
| 11 | Analytics and landing | Page views, starts, submissions, conversion rate, pricing page, and activation funnel. |
| 12 | Reliability and security | Rate-limit tests, webhook retries, backup/restore check, data export, and dependency audit. |
| 13 | Dogfooding and UX fixes | Publish five real service-business pages, submit forms, onboard five testers, and fix blockers. |
| 14 | Launch | Production deploy, domain and email checks, support flow, changelog, demo video, and founder launch posts. |

### Launch-readiness checklist

- A new user can publish a lead page in under 10 minutes.
- A submission appears in the dashboard and email within 30 seconds.
- Webhook delivery can be retried without losing the submission.
- Export and deletion work.
- No known critical security or billing defect.
- Five target users have submitted or scheduled a real test.

## 30-day marketing calendar

### Budget

| Channel | 30-day budget |
|---|---:|
| Content, creator partnerships, and micro-incentives | $120 |
| Selective paid tests for proven organic landing pages | $120 |
| Tools, domain, and production services | $60 |
| **Total** | **$300 maximum** |

Organic-first rule: paid campaigns are unlocked only after an organic page has received qualified visits or signups.

### Weekly calendar

#### Days 1–7: message and proof

| Day | Action |
|---:|---|
| 1 | Publish comparison page: static hosting versus a full app stack; collect email addresses. |
| 2 | Post a founder build diary showing a page built in under 10 minutes. |
| 3 | Publish a technical guide for Netlify, Cloudflare Pages, GitHub Pages, and Vercel. |
| 4 | Recruit 10 photographers or consultants as design partners. |
| 5 | Publish “10 lead-capture page blocks that convert,” with a live demo. |
| 6 | Share five before/after screenshots and collect objections. |
| 7 | Release the v1 landing page and founder-led launch post. |

#### Days 8–14: templates and community

| Day | Action |
|---:|---|
| 8 | Release a free photographer lead-page template. |
| 9 | Post a short video: static page plus form submission to Google Sheets/email. |
| 10 | Participate in relevant no-code, static-site, and agency communities; answer questions without spam. |
| 11 | Publish a tiny agency case study with anonymized results. |
| 12 | Add a second vertical template only if message clarity remains high. |
| 13 | Host a 30-minute workflow clinic showing page setup and lead routing. |
| 14 | Send a segmented email to waiting users and request referrals. |

#### Days 15–21: proof and conversion

| Day | Action |
|---:|---|
| 15 | Publish a transparent launch retrospective with activation and failure data. |
| 16 | Reach out to 20 small agencies with a personalized sample page. |
| 17 | Release a consultant template and product-update email. |
| 18 | Publish “Why your form endpoint is not a CRM” with an export workflow. |
| 19 | Run a 45-minute live build session for freelance developers. |
| 20 | Offer assisted onboarding to the first 20 workspaces. |
| 21 | Publish a migration guide from a heavyweight form builder. |

#### Days 22–30: retention and selective scaling

| Day | Action |
|---:|---|
| 22 | Add a high-value onboarding email sequence. |
| 23 | Interview every retained user and every churned user. |
| 24 | Publish fixes and a measured reliability report. |
| 25 | Create a referral loop: share a published page and invite collaborators. |
| 26 | Test a $50 paid landing-page variant against organic traffic; stop if CAC exceeds threshold. |
| 27 | Contact inactive workspaces with a one-click template migration. |
| 28 | Publish the best agency case study and a 60-second demo. |
| 29 | Run a limited promotion for annual Starter plans; retain no more than $50 of incentives. |
| 30 | Review MRR, activation, conversion, retention, support load, and decide whether to continue, narrow, or stop. |

### KPIs

- Visitor-to-signup: target 8%.
- Signup-to-publish: target 40% within seven days.
- Publish-to-first-submission: target 30%.
- Free-to-paid: target 5% after activation.
- Month-one paid retention: target 85%.
- Support requests per paid account: below 0.5/month.
- Paid CAC target: under $60.
- Paid MRR by day 30: target $1,500 as an early validation milestone.

## Unit economics to $10K MRR

### Base case

Assume blended ARPU of **$39/month** and gross margin of **85%**.

- Customers required: `$10,000 / $39 ≈ 257`.
- Monthly gross profit: `$10,000 × 85% = $8,500`.
- Monthly variable infrastructure cost at scale: approximately **$500**.
- Monthly contribution after infrastructure: approximately **$8,000** before founder labor, refunds, and taxes.

### Conservative plan

| Customers | Blended ARPU | MRR | Use |
|---:|---:|---:|---|
| 85 | $19 | $1,615 | Starter users |
| 120 | $49 | $5,880 | Growth users |
| 45 | $99 | $4,455 | Agency users |
| **250** | **$47.80** | **$11,950** | $10K-MRR threshold exceeded |

### Acquisition plan within the $300 launch cap

The first 30 days validate demand rather than purchase growth. Thereafter, assume an allowable 90-day blended CAC ceiling of **$120**.

- 250 customers × $120 CAC = **$30,000** total acquisition spend.
- At a target 3-month gross-margin payback, LTV must exceed approximately **$360**.
- With $47.80 blended ARPU and 85% gross margin, monthly gross profit is approximately **$40.63**.
- Required gross-margin LTV/CAC is **3.0x**.
- A conservative 12-month retention profile supports LTV of approximately `$40.63 × 8 retained months ≈ $325`; this is close but not comfortably above the target.
- Therefore, scale only if retention improves, ARPU rises, agency referrals become material, or CAC falls below $100.

### Pricing and cost controls

- Use usage limits to prevent hostile or runaway form traffic.
- Cache public pages at the edge.
- Batch submission emails and analytics writes.
- Keep image assets outside the application bundle.
- Offer annual prepayment only after retention is observed.
- Do not include unlimited submissions in the entry plan.

## Kill criteria

Kill or pause the direction if any of the following occurs by the stated checkpoint:

1. **Message failure:** fewer than 10 qualified interviews in 14 days show that static-first form collection is a meaningful purchase criterion, not merely a preference.
2. **Activation failure:** fewer than 30% of activated accounts publish a page within seven days after onboarding is streamlined.
3. **Submission failure:** fewer than 20% of published pages receive their first real submission within 14 days, excluding internal test submissions.
4. **Conversion failure:** fewer than 3 paid customers from at least 100 qualified signups after two conversion iterations.
5. **Retention failure:** more than 20% of paying accounts cancel or fail to publish in their first billing month.
6. **Economics failure:** CAC exceeds $120 without agency referrals, or gross margin falls below 80% after infrastructure review.
7. **Reliability failure:** a serious data-loss, cross-tenant exposure, or systematic form-loss defect remains unresolved for 48 hours.
8. **Scope trap:** implementing the MVP requires a visual app builder, CRM replacement, or native app integrations.
9. **Distribution failure:** after 30 days of organic-first execution and 100 qualified outreach messages, fewer than 10 target customers agree to a paid pilot.
10. **Compliance trigger:** the product becomes tied to sensitive data categories requiring legal review beyond ordinary lead information.

Decision rule: if activation and first-submission targets miss by more than 50%, stop adding features and retest the message. If two consecutive 14-day validation sprints fail, kill the direction.

## Research caveats

- The supplied TinyFish search output contained CLI installation instructions rather than result excerpts, so it did not independently verify X demand.
- Competitor prices are directional and should be checked immediately before pricing publication.
- Anonymous Stage A rows were excluded because their category could not be responsibly inferred.
- The GO decision applies to the static-first service-business lead-capture wedge, not to a generic form builder.
