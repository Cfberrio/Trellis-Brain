---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/meta-tracking.md + commits 2026-08-05 → 2026-08-20 (tracking, CAPI, attribution chain)"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - marketing
  - tracking
  - meta
---

# Meta Tracking and Attribution

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Marketing-Home|DR Marketing Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Retargeting-and-Audiences|Meta Retargeting and Audiences]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Admin-Dashboard|Admin Dashboard]]

## The rule above all others
> Source of truth for revenue is **always** `payment.status = 'paid'` in the database. Meta is an attribution and optimization layer, **never** the ledger.

Dataset: **Discipline Rift Website**, Pixel id `1053126587366635`.

## Event map
| Event | Exact trigger | Browser | Server | DB source of truth | Value |
|---|---|---|---|---|---|
| `PageView` | every SPA route change | yes | — | — | — |
| `register_started` *(internal)* | first real school/team pick on `/register`, once per tab | — | ledger | `tracking_event` | — |
| `CompleteRegistration` | enrollment row persisted as `pending_payment` | yes | yes | `enrollment` | post-coupon subtotal |
| `InitiateCheckout` | Stripe Checkout Session actually created | yes | yes | `payment` (pending) | charged total |
| `Purchase` | `mark_payment_paid` flipped the row to `paid` | yes | yes | `payment.status='paid'` | `payment.amount`, USD |

An `otp_sent` funnel step was added in August 2026 to expose losses at the identity gate.

Browser `eventID` and server `event_id` are the **same string**, derived from the business object, so a reload, a back-navigation, a webhook retry and a verify-payment race all recompute one id and Meta deduplicates.

**`CompleteRegistration` is a diagnostic milestone only.** The campaign optimizes for `Purchase` — a parent can complete registration and never pay.

## Idempotency
- The `payment` row is reused per enrollment, so there is one checkout event id.
- `mark_payment_paid` is atomic and returns true only for the call that performed the flip, so the purchase event fires exactly once.
- `meta_event_delivery.meta_event_id` is UNIQUE — a resend is journaled as `duplicate` and never re-posted. Only a previous `error` or `skipped_no_secrets` is retried.
- The success page also guards on a local flag per payment id.

## Attribution
Captured on landing: `utm_source`, `utm_medium`, `utm_campaign`, `utm_term` (ad set / GEO), `utm_content` (creative), `meta_campaign_id`, `meta_adset_id`, `meta_ad_id`, `meta_placement`, `fbclid`, plus landing URL, referrer and timestamps.

- **First touch** is written once and never overwritten.
- **Last touch** moves only on a new *paid* click — a Meta object id, an `fbclid`, or a paid `utm_medium`. A direct or organic return never erases the ad that acquired the parent.
- Identity chain: anonymous cookie → `tracking_visitor` → `user_id` + `parent_id` (linked server-side once the parent signs in after OTP) → `enrollment` → `payment`. Reporting joins payment → parent → visitor, so attribution survives a return days later.

## Privacy — non-negotiable
- Advertising is **opt-in**. The Pixel script does not load and no Meta call is made until the visitor accepts advertising cookies. Server events for non-consented parents are journaled as `skipped_no_consent` — a correct outcome, not a bug.
- First-party analytics is opt-out and independent of Meta consent, so the internal funnel is always complete.
- **No child data ever reaches Meta.** Payloads carry the parent's hashed email / phone / name / external id, browser identifiers, IP and user agent, plus program context (sport, school name, price). Never student name, date of birth, age, grade, level, medical information or student id.

## Reporting views
| View | Answers |
|---|---|
| `v_paid_registration_attribution` | one row per paid registration with first/last touch and Meta delivery status |
| `v_meta_creative_performance` | paid registrations and revenue by creative |
| `v_meta_geo_performance` | paid registrations and revenue by ad set / GEO |
| `v_meta_creative_geo_performance` | creative × GEO matrix |
| `v_registration_funnel_daily` | landing → register_started → CompleteRegistration → InitiateCheckout → Purchase |

ROAS is **not** computed here. The database owns registrations and revenue; Meta Ads Manager owns spend. Joining the two is a reporting decision, made deliberately.

## Why this matters
DR can now answer "which ad paid for this registration" from its own database. That is the exact capability whose absence made the OEV June Google Ads campaign unmeasurable — see [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Google-Ads-Post-Mortem-2026-06|OEV Google Ads Post-Mortem]].
