# Vertical B2B White-Label — Branded Client Portal for One Specialist SaaS Niche

## Tier

**GO**

- Demand: **4/5** (prior-research hypothesis; X verification pending)
- Competition: **2/5** (prior-research hypothesis)
- MVP target: **14 days, solo**
- Marketing target: **≤ $300 over 30 days**
- Revenue target: **$10K MRR**

## Why this direction

### TrustMRR evidence

The prior validated research cites **Tradevipe** at approximately **$2.9K MRR from only 14 customers**, an implied average of roughly **$207 MRR per customer**. This is the clearest available validation of high-ACV demand for a white-label vertical SaaS product. It also shows why the target requires only tens of customers rather than hundreds.

### X/web evidence and validation plan

The supplied TinyFish capture did not contain usable X or web results. Prior research is desktop evidence, not completed X verification.

Run:

- `white label client portal alternatives 2026`
- `branded customer portal pain`
- `site:x.com SaaS "white label" client portal`
- `site:x.com agency "branded portal"`
- `site:x.com "just shipped" white-label SaaS`
- `site:x.com founder white label "looking for"`

Choose one initial vertical before coding. Recommended options are dental practices, accounting firms, mortgage brokers, and specialized service providers. Score each segment on pain, sales access, data sensitivity, implementation burden, willingness to pay, and reference value. Interview at least 15 buyers in the selected segment and secure three paid pilot agreements or deposits.

### Thesis

Vertical SaaS companies often need a branded client portal without building user accounts, permissions, files, messaging, and workflow features from scratch. A generic white-label platform is too broad, so this MVP targets **one vertical’s repeatable client workflow**.

Example wedge: **a branded document and message portal for mortgage brokers**, with client folders, file exchange, status updates, and a provider-branded login. The vertical must be selected using the interview evidence—not merely because the founder recognizes it.

## Competitor table

| Level | Competitor | Positioning | Typical pricing | Implication |
|---|---|---|---:|---|
| L1 | Tradevipe | Vertical white-label platform | Custom/enterprise pricing | Prior proof of demand; 14 customers imply strong ACV |
| L1 | Vendasta | White-label and client-platform suite | Subscription tiers plus enterprise | Broad suite; too many capabilities for MVP |
| L1 | SuiteDash | White-label client portals | Subscription tiers | Strong general benchmark for branding and permissions |
| L2 | ClientPortal | Branded client portal | Subscription tiers | Direct client-portal competitor |
| L2 | Copilot | Client portal for professional services | Subscription tiers | Strong accountability/workflow competitor |
| L2 | SimplyClient | White-label client portals | Subscription tiers | Direct branded-portal alternative |
| L2 | Zoho / monday / HubSpot | Broad work-management suites with portals | Tiered subscriptions | Bundled alternative; vertical relevance may be weak |
| L3 | WordPress + plugins | Custom branded portals using plugins | Plugin and hosting costs | Common DIY incumbent; must save setup and maintenance |
| L3 | Custom development | Bespoke portal | Project and maintenance fees | Expensive but fully customizable; sell faster setup and lower maintenance |
| L3 | Google Drive/Dropbox/Notion | Shared folders and pages | Free/freemium | Cheap incumbent with poor branded workflow and role controls |

The market is not empty. Competition 2 applies only to a narrow vertical workflow and must be confirmed. If established horizontal portal products already offer simple branding at low prices, narrow to an industry-specific compliance or handoff workflow.

## PRD MVP

### Initial ICP decision

The ICP must be selected and documented before day 3. Suggested scoring:

| Criterion | Weight |
|---|---:|
| Repeated client-portal pain | 25% |
| Budget and purchasing authority | 20% |
| Reachable communities and outbound lists | 15% |
| Repetition of document/workflow needs | 15% |
| Low implementation and compliance burden | 15% |
| Referral/reference value | 10% |

### Recommended initial product

A configurable branded portal with:

1. **Provider branding**
   - Logo, colors, domain or subdomain, email sender, and portal title.
2. **Tenant model**
   - Provider, staff, client, folder, document, message, and audit-event structure.
3. **Authentication**
   - Magic-link client login; staff role management.
4. **Client folders**
   - Status labels, assigned staff, due dates, and checklist.
5. **Secure file exchange**
   - Upload/download, file-size limits, signed URLs, and malware scanning where feasible.
6. **Messages and notifications**
   - Thread per client folder and email notifications.
7. **Activity timeline**
   - Important document, status, and message events.
8. **Custom domain/customization**
   - Custom domain support may be P1; reliable in-app branding is P0.
9. **Billing**
   - Stripe platform billing or provider-billed plans; define who pays before implementation.
10. **Admin controls**
   - Provider can manage clients, folders, templates, users, branding, and billing.

### P1 — after launch validation

- Custom domains.
- Custom fields.
- Client intake forms.
- E-signature integration.
- Task templates.
- Calendar scheduling.
- SMS notifications.
- Multi-location providers.
- API and webhooks.
- WordPress plugin.
- Branded email templates.
- Reporting dashboard.

### P2 — later expansion

- Full CRM.
- Automations.
- Payments.
- Accounting integrations.
- Mobile applications.
- Custom portal layouts.
- Audit exports.
- HIPAA, SOC 2, and data-residency options.
- Industry benchmark reports.
- Partner marketplace.

### Non-goals

- Horizontal white-label platform for every industry.
- General project-management suite.
- Full CRM.
- Document e-signature.
- Payment processing.
- Website builder.
- Marketing automation.
- Native mobile applications.
- Multi-industry feature sprawl.
- Building custom integrations during MVP.
- Becoming a general file-sharing service.
- Healthcare or legal workflows until compliance is validated.

### Core UX

1. Provider signs up and chooses vertical template.
2. Provider configures branding and default folder template.
3. Staff creates a client and folder.
4. Provider invites the client.
5. Client uploads a document or sends a message.
6. Staff updates status and sends a notification.
7. Provider audits activity and exports the folder.

Time from provider signup to first client invitation should be under ten minutes.

### Technical approach

- **Frontend:** Next.js + TypeScript + Tailwind CSS.
- **Backend:** Next.js route handlers or a small Node service.
- **Database:** Managed Postgres with tenant-scoped row-level policies.
- **Auth:** Managed authentication with organization memberships and magic links.
- **Storage:** Private object storage with signed URLs and scanning.
- **Email:** Transactional provider and provider-customized templates.
- **Jobs:** Managed queue for email, scanning, and retries.
- **Payments:** Stripe; choose provider-billed versus platform-billed billing.
- **Observability:** Tenant-scoped logs, delivery failures, upload errors, and audit events.

### Core data model

- `organizations`
- `memberships`
- `clients`
- `folders`
- `folder_templates`
- `documents`
- `threads`
- `messages`
- `tasks`
- `branding_themes`
- `custom_domains`
- `notifications`
- `audit_events`
- `subscriptions`
- `usage_events`

### Security and tenancy baseline

- Strict tenant authorization on every query.
- Server-side role checks for provider, staff, and client.
- Private storage; no public object URLs.
- Signed, short-lived download URLs.
- Audit events for sensitive actions.
- Rate limits and malware scanning for uploads.
- No sensitive client content in logs or analytics.
- Encryption in transit and at rest.
- Documented retention and deletion.
- Data export for portability.
- Tested restoration and tenant-isolation tests.

## 14-day day-by-day build plan

| Day | Deliverable | Acceptance criteria |
|---:|---|---|
| 1 | Vertical discovery and competitor audit | Fifteen interviews; three segment scorecards; ten alternatives checked |
| 2 | ICP lock and scope freeze | One vertical, workflow, buyer, price, and non-goals documented |
| 3 | Landing-page smoke test and deposit offer | Five paid deposits or signed pilot agreements |
| 4 | Auth and tenant model | Organization, memberships, staff/client roles, tenant isolation tests |
| 5 | Branding and portal shell | Logo, colors, title, portal navigation, responsive layouts |
| 6 | Clients and folders | Create/search clients, templates, assignments, statuses, due dates |
| 7 | File exchange | Upload/download, signed URLs, validation, scanning, error handling |
| 8 | Messaging and notifications | Threads, email notifications, retries, delivery log |
| 9 | Activity timeline and admin | Audit timeline, member management, templates, core settings |
| 10 | Billing and packaging | Stripe, trial, billing portal, provider-vs-client billing decision implemented |
| 11 | Security and reliability test | Tenant-isolation tests, upload abuse, rate limits, restore test |
| 12 | UX polish and onboarding | Five-minute setup path, templates, empty states, accessibility pass |
| 13 | End-to-end pilot rehearsal | One complete provider-client workflow; onboarding documentation |
| 14 | Launch readiness | Three pilot onboarding checklists, monitoring, backups, support, legal copy |

### Definition of done for day 14

A provider can brand a portal, invite a client, create a standard folder, exchange files and messages, track activity, subscribe, and administer users. A client can complete the workflow without receiving founder assistance.

## 30-day marketing calendar

### Marketing thesis

Sell directly to a tightly defined vertical using a concierge-built portal, not to “SaaS companies.” The first ten prospects should receive a personalized mock portal and workflow map. This can be delivered organically through targeted communities, founder networks, and direct outreach while staying below the $300 marketing cap.

### Budget: $300 maximum

| Item | Budget |
|---|---:|
| Domain, email, mockup tools, and demo assets | $60 |
| One vertical-community or newsletter sponsorship | $120 |
| Targeted workshop or meetup | $80 |
| Customer pilot incentives | $20 |
| Contingency | $20 |
| **Total** | **$300** |

### Calendar

| Day | Action | Target |
|---:|---|---|
| 1 | Launch the vertical-specific “branded client workflow” page | 75 qualified visits |
| 2 | Contact 20 providers in the chosen vertical | 6 calls |
| 3 | Build and send one personalized portal mockup | 2 paid intents |
| 4 | Run a 30-minute workflow-design clinic | 8 attendees |
| 5 | Share an anonymized before/after workflow | 5 qualified leads |
| 6 | Offer five free workflow audits | 3 pilot agreements |
| 7 | Review objections and pilot-fit criteria | Update sales page and scope |
| 8 | Contact 20 adjacent providers | 6 additional calls |
| 9 | Publish a vertical compliance/workflow checklist | 8 downloads |
| 10 | Demonstrate tenant separation and audit history | 3 technical buyers |
| 11 | Onboard the first pilot provider | One live client folder |
| 12 | Interview the pilot user within 48 hours | Five usability findings |
| 13 | Add the top requested template | One template shipped |
| 14 | Mid-month review | 3 signed pilots, $500+ pipeline MRR |
| 15 | Contact 20 local or regional providers | 8 calls |
| 16 | Publish a customer implementation story | 4 referrals |
| 17 | Run a second workflow clinic | 10 attendees |
| 18 | Create an agency/consultant referral partner | 2 partners |
| 19 | Send a vertical ROI calculator | 15 qualified uses |
| 20 | Improve onboarding to a 15-minute setup | Pilot activation +20% |
| 21 | Add branded email templates | 5 client activations |
| 22 | Publish a security and data-isolation explainer | 5 procurement conversations |
| 23 | Offer annual pricing to pilot customers | 2 annual prepayments |
| 24 | Contact 20 former trial or mockup recipients | 6 calls |
| 25 | Add a referral credit for provider referrals | 4 referred demos |
| 26 | Publish a “why not generic client portal” comparison | 8 qualified leads |
| 27 | Run a vertical-specific case-study teardown | 6 sales conversations |
| 28 | Improve the highest-friction setup step | Setup time −30% |
| 29 | Review implementation hours, margins, and churn risk | Resolve top three delivery risks |
| 30 | Month-two review | 5 live provider accounts and $1,000+ MRR or pipeline |

### Weekly content pillars

1. **Vertical workflow education:** what the portal must do for this industry.
2. **Concierge implementation:** before/after setup examples.
3. **Security and trust:** tenant isolation, audit trails, and data ownership.
4. **ROI:** reducing status calls, chasing files, and manual onboarding.

### Activation and funnel targets

- Qualified contact → demo: **≥25%**
- Demo → paid pilot/deposit: **≥20%**
- Pilot → first live client folder: **≥70%**
- Pilot → paid conversion: **≥60%**
- Active provider → second client folder: **≥70%**
- Monthly provider churn: **<5%**

## Unit economics to $10K MRR

### Pricing

- **Launch:** $199/month plus a $500 onboarding fee
- **Growth:** $399/month
- **Network:** $799/month
- **Enterprise/partner:** $1,500–$2,500/month

The price must follow the selected vertical’s willingness to pay. Do not compete with horizontal portals at $30/month.

### Revenue mix at target

| Plan | Customers | MRR |
|---|---:|---:|
| Launch | 20 | $3,980 |
| Growth | 12 | $4,788 |
| Network | 2 | $1,598 |
| **Total** | **34** | **$10,366** |

Round the plan to **33 customers at approximately $10K MRR** using a mix of approximately 20 Launch, 11 Growth, and 2 Network customers.

### Cost assumptions

- Platform infrastructure and third-party services: **$25–$60/customer/month**
- Payment fees: roughly 3%
- Onboarding/support target: no more than two hours per account in month one and one hour per month thereafter
- Founder labor during pilot: track separately at a conservative internal rate of $75/hour

Illustrative variable cost excluding founder labor: **$50/customer/month**.

### Gross margin and acquisition

- MRR: approximately $10,000
- Variable cost: approximately $1,650 at 34 customers
- **Gross margin:** approximately 83%
- Maximum CAC for three-month gross-margin payback: approximately **$250**
- Target blended CAC: **≤$150**
- Required monthly paid acquisitions: approximately **8–12 providers**

One-time onboarding revenue improves early cash flow but should not conceal weak recurring economics.

### Validation milestone

Reach **five live paying providers, $1,000 MRR, and fewer than two support hours per account per month** before acquiring more customers. If custom work per tenant exceeds 30% of total revenue, enforce templates and narrow the product.

## Kill criteria

Kill or reposition the direction if:

1. Fewer than **3 paid deposits or signed pilot agreements** from 30 qualified vertical buyers.
2. Fewer than **20%** of qualified prospects agree to a demo.
3. Demo-to-paid conversion remains below **20%** after three pitch iterations.
4. Median onboarding exceeds **four hours** after the third customer.
5. More than **30%** of revenue depends on one-off custom engineering.
6. Median monthly support exceeds **two hours per account**.
7. Gross margin falls below **75%**.
8. Effective CAC exceeds **$250**.
9. Monthly logo churn exceeds **7%**.
10. Prospective customers demand full CRM, e-signature, billing, or project management as table stakes.
11. Security requirements cannot be met responsibly for the chosen vertical within the MVP constraints.
12. No single vertical contains at least 15 reachable, high-intent prospects and three references willing to speak publicly.
13. A horizontal competitor offers the selected vertical’s required workflow at a materially lower total cost.
14. The sales cycle exceeds 45 days for small providers; if so, move downmarket or change the niche.
