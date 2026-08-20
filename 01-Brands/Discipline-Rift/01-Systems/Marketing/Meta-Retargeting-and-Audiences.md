---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: playbook
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/meta-retargeting.md + docs/meta-audience-extraction.md (audience snapshot 2026-08-18) + ClickUp DR/ADS 'SOP: Sistema de Retargeting, First-Party Data y Meta Ads'"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - marketing
  - meta
  - retargeting
---

# Meta Retargeting and Audiences

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Marketing-Home|DR Marketing Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Tracking-and-Attribution|Meta Tracking and Attribution]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Experiments|DR Meta Ads Experiments]]

## Audience state (snapshot 2026-08-18)
| Audience | Type | Size | Status | Retargeting use |
|---|---|---|---|---|
| DR - Web Visitors 30d | Website | below 1k | ready | yes |
| DR - ViewContent 30d | event-based | below 1k | populating | yes |
| DR - Lead 30d | event-based | below 1k | populating | yes |
| DR - InitiateCheckout 14d | event-based | ~85 | ready | **use** |
| DR - Purchase 180d | event-based | ~107 | ready | **exclude** |
| DR HISTORIC | IG engagement | ~50k | ready | fallback |
| Lookalike 1% (DR HISTORIC) | lookalike | ~1.2M | ready | **use** |

**Problem:** all five pixel/CAPI audiences are below 1k — too small to sustain retargeting on their own.
**Opportunity:** the DR HISTORIC lookalike, plus a lookalike built from the uploaded customer list, provide the volume.

## Audience design
Retargeting custom audiences, source = website/dataset:
- Visitors 7 / 14 / 30 days (PageView).
- ViewContent 30d (team selected).
- Lead 30d without Purchase.
- **InitiateCheckout 14d excluding Purchase 180d** — the recovery audience, the highest-intent group DR has.

Exclusions: Purchase 180d + CompleteRegistration 180d, plus an employee list once one exists.

Lookalike: source Purchase once there is volume, ideally ≥100 purchases in a 30–90 day window. Until then, use the DR HISTORIC and customer-list lookalikes.

## Customer list
A hashed customer list of **721 parents** was extracted from the database and uploaded to Meta as the seed for a lookalike. Hashing is done before upload; raw contact data does not leave the platform. `_fbp` / `_fbc` cookies are **not** uploaded — they are browser-side identifiers used in event matching, not list fields.

Rule of thumb learned here: a source audience under 100 people cannot produce a reliable lookalike. Feeding the customer list is what moves it into the hundreds of thousands.

## Implementation decisions (deviations from the original doc)
- Table names are prefixed `tracking_` because `session` was already taken by team practices.
- CAPI runs in Supabase Edge Functions, where the Stripe webhook already lives, instead of Cloudflare Workers. Same guarantee, fewer moving pieces.
- Purchase / Lead / InitiateCheckout via CAPI require `ad_consent = true` on the linked visitor. Deliberately conservative; can be relaxed if legal approves.
- First-party analytics is on by default with opt-out (US); advertising is opt-in. **Legal review still pending.**
- Stable school URLs (`/schools/<slug>`) and QR tracking links (`/r/<code>`) are deferred to a later phase.

## Troubleshooting checklist
- No events in Test Events → confirm the pixel actually loaded (a `facebook.com/tr` request returning 200 and an `_fbp` cookie), confirm the CAPI token and pixel id are set, and confirm cookies were accepted. Without consent the pixel does not load, by design.
- Lookalike under 10k → the source audience is too small. Upload the customer list.

## Next step
Legal review of the consent model is the open blocker. Everything else is live and populating.
