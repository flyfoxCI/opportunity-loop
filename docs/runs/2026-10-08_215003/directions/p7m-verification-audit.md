# P7M Verification Audit

## 1. Why this direction

### TrustMRR evidence

- P7M.io is listed at approximately **$4.48 MRR**, **$47.82 last-30 revenue**, and **253 subscribers**.
- The product description identifies a specific Italian digital-signature reader workflow rather than a generic document AI category.
- The relatively strong recent revenue compared with stated MRR suggests either a pricing/reporting mismatch, a burst of activity, or an opportunity to monetize a professional verification workflow more clearly.

### X/web evidence

The supplied Stage B evidence did not contain usable X/web results. The relevant discovery queries are:

- `P7M alternatives`;
- `verifica firma digitale p7m`;
- `file p7m non si apre`;
- `CAdES firma non valida commercialista`;
- `verifica firma digitale allegato PEC`;
- `P7M painful OR broken OR expensive`.

The opportunity should not be based on the claim that signatures are universally invalid. It should be based on the narrower claim that accountants, notarial offices, procurement teams, and small businesses need a fast, understandable way to inspect a signed file and produce an audit trail.

### Interpretation

This is a professional workflow, not a generic PDF tool. The likely value is reducing uncertainty: what was signed, by whom, whether the signature structure validates, when validation should be re-run, and which files need escalation.

The product should be framed as **verification assistance**, not legal advice or a substitute for a certified trust service provider.

## 2. Competitor table

The category is fragmented across native desktop utilities, browser PDF tools, certificate inspectors, and manual professional workflows. Verify current pricing and features manually before launch.

| Level | Competitor/type | Typical strength | Gap to exploit |
|---|---|---|---|
| L1 | Native Italian e-signature/P7M tooling | Deep local compatibility and established users | Desktop-only, opaque results, limited batch workflow |
| L1 | Commercial PDF signature validators | Familiar interface and broad document support | Often general-purpose and weak on Italian CAdES terminology |
| L1 | Accountancy/legal service providers | Human interpretation and trust | Expensive per document and slow for repeated checks |
| L2 | Open-source PDF/certificate inspection tools | Flexible and inexpensive | Requires technical knowledge and command-line work |
| L2 | General browser PDF editors | Easy upload/download | Signature validation is not the core workflow |
| L3 | Manual certificate/profile viewers | Technical authority | Not a business workflow and difficult to interpret |
| L3 | Email/PEC support channels | Human fallback | No centralized status, report, or repeatability |

### Positioning

“Do not replace your e-signature stack. Make every signed file easy to verify.”

## 3. PRD MVP

### Target ICP

Primary:

1. Italian accounting firms with 2–20 staff;
2. notarial offices handling incoming signed documents;
3. procurement/legal operations staff at small B2B companies;
4. consultants who repeatedly receive signed PDFs.

Primary job:

> Upload a signed PDF/P7M file, understand the validation status, and export a concise verification report for the file.

### P0

- Drag-and-drop upload for a single PDF/P7M file;
- file size limit and malware/document safety checks;
- PDF structure extraction;
- visible detection of supported signature profiles and signature fields;
- certificate subject, issuer, validity dates, and chain summary;
- timestamp and revocation-related metadata display where available;
- clear status vocabulary: `Verified`, `Needs review`, `Invalid/unreadable`, `Unsupported`;
- human-readable report export to PDF and plain text;
- copyable evidence summary;
- no permanent file retention by default;
- deletion action;
- usage metering;
- admin-free single-tenant MVP;
- audit event for upload, report export, and deletion.

### P1

- batch upload up to 20 files;
- saved verification templates;
- PDF/A and Italian long-term validation presets;
- organization history with configurable retention;
- CSV result export;
- email report delivery;
- API endpoint for one verification job;
- multilingual Italian interface;
- structured JSON result.

### P2

- integrations with accounting/document-management systems;
- scheduled re-verification;
- certificate monitoring;
- team approval workflows;
- enterprise SSO;
- custom report branding;
- on-premise deployment.

### Non-goals

- no legal certification of validity;
- no guarantee that a document is enforceable;
- no replacement for qualified legal advice;
- no certificate issuance;
- no full PDF editor;
- no unrestricted document storage;
- no government identity verification;
- no broad OCR/document extraction product;
- no promise to fix malformed documents;
- no cryptocurrency or blockchain workflow.

### MVP acceptance criteria

A user can:

1. upload a supported signed file;
2. see a status and the reasons behind it;
3. inspect certificate and timestamp evidence;
4. download a report;
5. delete the file;
6. receive a clear warning when the result cannot be trusted or the format is unsupported.

## 4. 14-day build plan

| Day | Deliverable |
|---:|---|
| 1 | Interview 5 accountants/notarial/procurement users; confirm exact file types, language, and legal boundaries |
| 2 | Write test corpus of signed PDFs, malformed files, unsupported profiles, and chain failures |
| 3 | Define status taxonomy and report template with domain reviewer |
| 4 | Build upload, storage encryption, file retention, and deletion endpoints |
| 5 | Implement PDF parsing and signature/certificate discovery |
| 6 | Implement certificate chain and timestamp extraction |
| 7 | Implement deterministic status engine with unsupported/error states |
| 8 | Build upload/results/report UI in Italian and English |
| 9 | Add PDF/HTML report export and copyable evidence summary |
| 10 | Add authentication, usage limits, error monitoring, and security headers |
| 11 | Run the full test corpus; compare results with native tools and domain reviewers |
| 12 | Fix false positives/negatives; improve unsupported-format explanations |
| 13 | Private beta with 10 professionals; observe task completion and trust objections |
| 14 | Fix blockers, publish landing page, and begin paid pilots |

### Technical approach

- Backend: TypeScript/Node or Python depending on available PDF libraries;
- parser: a maintained PDF parser plus OpenSSL/ASN.1 tooling;
- frontend: responsive web app;
- deployment: simple cloud VM/serverless containers;
- storage: encrypted object storage with short default retention;
- observability: structured logs, error tracking, and audit events;
- security: isolate document processing, limit file sizes, avoid executing embedded content, and never log document contents by default.

## 5. 30-day marketing calendar

### Budget

Total: **€250 / $270 maximum**.

- Content/design: €80
- Domain, email, and landing-page tooling: €30
- Paid smoke tests: €100
- Beta/customer incentives: €40

### Organic-first plan

| Day | Activity | CTA |
|---:|---|---|
| 1 | Publish landing page with sample report and explicit legal disclaimer | Upload a test file |
| 2 | Contact 20 Italian accounting firms personally | 10-minute workflow interview |
| 3 | Publish “When P7M validation fails” explainer | Try a sample |
| 4 | Post a sanitized before/after verification demo | Join beta |
| 5 | Reach 20 notarial offices and procurement managers | Beta invite |
| 6 | Publish FAQ: what a signature validator can and cannot prove | Read FAQ |
| 7 | Run a €20 search-ad smoke test for “verifica firma p7m” | Start free check |
| 8 | Email beta users with feedback survey | Submit test document |
| 9 | Publish a comparison guide versus native desktop software | Request demo |
| 10 | Contact accounting communities and professional associations | Ask for distribution |
| 11 | Publish batch-processing workflow article | Join waitlist |
| 12 | Run second €20 ad experiment on high-intent Italian terms | Verify file |
| 13 | Host a 30-minute Italian compliance Q&A | Invite accountant |
| 14 | Email pilot users with updated report format | Upgrade |
| 15 | Publish “certificate expired vs signature invalid” explainer | Try checker |
| 16 | Contact 30 procurement teams that receive signed PDFs | Pilot call |
| 17 | Publish privacy and deletion policy explainer | Read policy |
| 18 | Post short workflow clips on LinkedIn and relevant professional forums | Try tool |
| 19 | Run €30 retargeting/search test with verified sample report | Start check |
| 20 | Ask satisfied pilot users for one case study quote | Permission request |
| 21 | Publish case study with redacted evidence | Contact sales |
| 22 | Reach software/accounting consultancies | White-label discussion |
| 23 | Publish API/batch-use waitlist page | Request API access |
| 24 | Conduct 5 additional user interviews | Validate wedge |
| 25 | Launch referral loop for existing beta users | Invite colleague |
| 26 | Publish report schema documentation | Build integration |
| 27 | Run final €30 ad test on the best keyword | Start pilot |
| 28 | Email non-converted users with a single clear CTA | Try sample |
| 29 | Review activation, task completion, and support requests | Product decision |
| 30 | Publish transparency update and choose next ICP | Join pilot |

### Acquisition KPIs

- ≥100 qualified landing-page visits by day 30;
- ≥20 completed sample verifications;
- ≥10 interviews;
- ≥5 activated professional accounts;
- ≥3 paid pilots;
- ≥40% week-four pilot retention;
- median time to first useful result under 2 minutes.

## 6. Unit economics to $10K MRR

### Pricing hypothesis

- Solo/professional: €19/month, 50 checks;
- Small firm: €59/month, 300 checks;
- Pilot/API: €149/month, 1,000 checks;
- Custom retention or branded reports: €199/month.

### Cost model

Assume:

- payment fees: 3%;
- parser/storage/compute: €0.20–€0.70 per verification depending on size;
- support: €1–€3 per active account per month at low volume;
- no paid acquisition required for the first 10 customers.

At €59 average monthly revenue:

- gross margin before support: approximately 90–97%;
- after variable processing and support: target ≥75%;
- $10K MRR / €59 requires approximately 170 paying firms;
- at €149 average revenue, approximately 67 paying firms.

This is achievable only with a strong professional channel, partnerships, or repeatable organic content. Do not assume consumer-style viral acquisition.

### Key economic levers

- short processing times;
- compressed reports;
- batch limits rather than unlimited processing;
- prepaid pilot plans;
- optional annual plans;
- partner/reseller revenue;
- self-serve report export;
- no storage-heavy free tier.

## 7. Kill criteria

Stop or reposition if any of the following occurs:

1. fewer than 3 of 10 interviewed professionals agree this is a frequent painful task;
2. fewer than 2 of 5 pilot accounts report weekly value;
3. fewer than 25% of test files can be classified with acceptable confidence;
4. native tools are perceived as materially better despite the new workflow;
5. users require legal certification rather than workflow assistance;
6. payment conversion is below 2% after 100 qualified visitors;
7. support burden exceeds 20 minutes per active account per week;
8. a security or legal review identifies unacceptable document-handling risk;
9. processing cost prevents ≥70% gross margin;
10. no clear repeatable acquisition channel appears by day 30.

## 8. Expansion path

After validation:

- batch and API workflows;
- recurring re-verification;
- accounting-firm white-label reports;
- document-management integrations;
- certificate and timestamp monitoring;
- sector-specific templates;
- multi-country compliance modules.

Do not expand into general document AI before the verification workflow has paid retention.
