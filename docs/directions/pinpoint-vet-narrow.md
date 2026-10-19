---
layout: post
title: "Direction — Pet Med Dose Calculator + Reminder"
date: 2026-10-19T21:20:28+00:00
week: "2026-10-19_212028"
week_date: "2026-10-19T21:20:28+00:00"
slug: "pinpoint-vet-narrow"
permalink: /directions/pinpoint-vet-narrow.html
tags:
  - "AI"
  - "SaaS"
  - "B2C"
  - "mobile"
excerpt: "Vet med dose calculator + reminder for pet owners (NOT human Rx)"
---

Slug: `pinpoint-vet-narrow` · Tier: **GO_NARROW** · Run: 2026-10-19_212028

## 1. Why this direction
**TrustMRR evidence:** `PinPoint` ($1.49 MRR / $4.84 last30 / 27 subs at pinpointdose.com) is a medication dose reminder/timing app. Demand_h 3, comp_h 2.

**The opportunity:** Human medication reminders (Medisafe, Mango Health, MyTherapy) are saturated. But **pet medication reminders are NOT** — vet prescriptions are 2–4× daily, owners struggle, and there's no Pet Medisafe equivalent.

**The wedge we keep (GO_NARROW):** Pet (dog + cat only) medication reminders + vet-written dose calculator. NOT human Rx. NOT exotic pets.

**Why GO_NARROW:** Human med reminders have compliance, FDA, and Medisafe incumbents. Pet meds avoid all of that, and pet owners spend $30B/yr on vet care in the US alone.

## 2. Competitor table (L1/L2/L3)

| Tier | Name | Price | Weakness vs us |
|---|---|---|---|
| L1 | Medisafe | Free / $10/mo | Human-only |
| L1 | PetDesk | Free (vet SaaS) | Push, not consumer |
| L1 | Pill Reminder (apps) | Free | Generic, no pet filter |
| L2 | MyTherapy | Free | Human, German origin |
| L2 | Pawprint | Free | Pet health record, no reminders focus |
| L3 | Google Calendar | Free | Works but no dose calc, no vet med knowledge |

**Score (pet-narrow):** competition = **2**

## 3. PRD MVP

**Wedge (what we REFUSE to build):**
- ❌ Human medication reminders
- ❌ Exotic pets / livestock
- ❌ Vet practice EHR / EMR (we are consumer)
- ❌ Prescription shipping / pharmacy
- ❌ AI diagnostic (regulatory nightmare)
- ❌ Insurance integration

**P0 (day 1–14):**
- iOS + Android app (Flutter)
- Pet profile: name, species (dog/cat), weight (kg/lb), age, conditions
- Drug database: 200 most common vet meds (Rimadyl, Apoquel, Vetmedin, Convenia, Cerenia, etc.) — dose per kg, frequency, interactions, withdrawal times
- Reminder push at dose time (with log of "given / skipped / vomited")
- Refill warning at 7 days remaining
- Share with vet: PDF export of dose log
- Pricing: Free = 1 pet, 2 meds, no PDF; Pro $4.99/mo or $29.99/yr per pet, all meds, PDF, multi-caregiver

**P1 (week 3–4):**
- Drug interaction checker (within active meds)
- Web dashboard for caregivers (kids at college giving pills to dog)
- Vet-clinic promo page

**P2:**
- Apple Watch / Wear OS quick-log
- Auto-import from PetDesk if user opts in

## 4. 14-day day-by-day build plan

| Day | Deliverable |
|---|---|
| 1 | Flutter repo + auth (Supabase magic-link) |
| 2 | Pet schema + add-pet flow |
| 3 | Drug database seed (top 100 dog, 100 cat meds) — sourced from published FDA-CVM labels |
| 4 | Dose calc: weight × mg/kg → ml or tablet count |
| 5 | Reminder engine + push (FCM/APNs) |
| 6 | Dose log: given/skipped/vomited + timestamp |
| 7 | Refill warning logic |
| 8 | PDF export of dose log for vet visit |
| 9 | Pricing + Stripe |
| 10 | Landing page + App Store screenshots |
| 11 | Beta to 50 pet owners (r/dogs, r/CatAdvice, r/dogtraining) |
| 12 | App Store + Play Store submission prep |
| 13 | Bug bash + drug-data accuracy review |
| 14 | Soft launch in r/puppy101, r/dogs, r/CatAdvice |

## 5. 30-day marketing calendar (budget ≤ $300)

**Budget:** $0 baseline. $200 reserved for 1× weekend App Store feature pitch + $100 for 1× small newsletter sponsorship (PetMd newsletters or similar).

| Week | Channel |
|---|---|
| 1 | "I built this" post in r/dogs, r/CatAdvice, r/puppy101 with screenshots |
| 2 | Reply to 10 posts daily in r/dogs about "vet meds" pain |
| 3 | 5 SEO blog posts: "rimadyl dose calculator", "apoquel reminder app", "convenia timer", "dog medication tracker app" |
| 4 | 1 newsletter pitch (PetMD, VetStreet), 1 vet-clinic partnership pitch (free clinic version) |

**Channel-specific KPIs:**
- Week 1: 200 free downloads, 5 paid
- Week 2: 600 free cumulative, 25 paid
- Week 3: 1,200 free, 75 paid
- Week 4: 2,000 free, 200 paid = **$1,000 MRR**

## 6. Unit economics to $10K MRR
- Price: $4.99/mo per pet, or $29.99/yr (most users go annual ~$2.50/mo blended)
- Blended ARPU: ~$3/mo per pet
- Need **~3,333 paying users** (≈ 10K monthly downloads → 33% Pro conversion at peak)
- Gross margin: ~92%
- CAC: ~$0 organic, ~$2 paid
- LTV (24-mo avg for pet apps — high retention because pets live long): ~$60
- LTV/CAC: ~30×

**Path to 3,333 paying:**
- Month 1: 200 paid → $600 MRR
- Month 2: 500 paid → $1,500 MRR
- Month 3: 1,000 paid → $3,000 MRR
- Month 4: 1,600 paid → $4,800 MRR
- Month 5: 2,400 paid → $7,200 MRR
- Month 6: 3,400 paid → **$10,200 MRR**

## 7. Kill criteria (day 30)
- < 50 paid by day 30 → ICP wrong; consider dropping to "dog-only" or trying equine
- Dog dose calc lands wrong (1 critical bug from a vet review) → halt + retry
- App Store rejects > 2× → pivot to PWA

## 8. Re-verify before code (day 1–3)
1. `r/dogs "vet medication" OR "rimadyl" recent` — confirm pain
2. `"@medisafe" OR "@medisafeapp" twitter complaints` — confirm human med reminder is crowded (justifies wedge)
3. Search App Store for "pet medication reminder" — check for entrenched players
4. `@rahulnk` (PinPoint founder) tweets — look for clues about why it's at $1.49 MRR despite 27 subs (broken funnel? pricing wrong?)

## 9. Wedge (required for GO_NARROW)
**We are NOT building a generic med reminder.** We are the pet-medicine dose calculator + reminder for dogs and cats. We refuse human prescriptions, exotic pets, EHR features, AI diagnostics, pharmacy, and insurance integration. The wedge is "vet-med-first, narrow scope, no FDA risk." This keeps us out of Medisafe/MyTherapy's lane while giving us a defensible niche where pet owners pay $5/mo without hesitation — vet bills are $500+/visit, so $5 feels like rounding error.
