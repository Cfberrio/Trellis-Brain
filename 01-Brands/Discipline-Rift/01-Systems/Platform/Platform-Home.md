---
brand: Discipline-Rift
area: systems
subarea: platform
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift repo (docs/, PRODUCT.md, docs/superpowers specs) + commits 2026-05-22 → 2026-08-20"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: system-hub
tags:
  - dr
  - platform
  - canonical
---

# DR Platform Home

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Systems-Home|DR Systems Home]]

## Children
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Website-Product-Standard|Website Product Standard]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Team-Status-and-Season-Model|Team Status and Season Model]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Waitlist-System|Waitlist System]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Payments-Fees-and-Receipts|Payments, Fees and Receipts]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Admin-Dashboard|Admin Dashboard]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Parent-App-Home|DR Parent App Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Coach-Portal-Home|DR Coach Portal Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Admin-Operations-App-Home|DR Admin Operations App Home]]
- [[01-Brands/Discipline-Rift/01-Systems/DR-Backend-Migration|DR Backend Migration]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Tracking-and-Attribution|Meta Tracking and Attribution]]

## Why this hub exists
[[01-Brands/Discipline-Rift/01-Systems/Systems-Home|DR Systems Home]] splits DR into three user-facing surfaces (parent, coach, admin). This hub documents the **shared platform underneath** them: the registration funnel, the team and season data model, payments, the waitlist, tracking, and the admin dashboard that runs the business.

Everything here reflects what shipped between June and August 2026. Before this pass, the vault's product notes described the state as of the Supabase → Lovable Cloud migration and nothing after it.

## Architecture snapshot (2026-08-20)
- One monolith, one domain, routed surfaces (`/`, `/register`, `/dashboard`, coach and parent areas). See [[01-Brands/Discipline-Rift/01-Systems/DR-Backend-Migration|DR Backend Migration]].
- Lovable Cloud project `d555121b-31c3-4c00-96a8-7ac15612143e` (Supabase ref `hvgcxtawrditxvgvqfxb`). DR brand id `3a7a48c0-f66b-4c8c-8d46-60d9acb08e0b`.
- Stripe Checkout Sessions for payments, with a visible processing fee line item.
- GoHighLevel receives paid parents as contacts via a direct, silent upsert. See [[01-Brands/Discipline-Rift/01-Systems/Sales/GHL-Sync-and-Segmentation|GHL Sync and Segmentation]].
- Meta Pixel + Conversions API for consent-gated ad measurement, with the database as the revenue ledger.

## Core invariants
- **The database is the source of truth for revenue.** `payment.status = 'paid'`. Meta and Google are attribution layers, never the ledger.
- **`team.status` is the only source of truth for team availability.** The old `is_ongoing` / `is_active` booleans are retired.
- **No child data ever leaves the platform to an ad network.**
- **Registration must never tell a parent "already enrolled" when they have an unpaid, resumable checkout.**

## Next step
When a feature ships in the `disciplinerift` repo, the matching child note here is part of the definition of done. The repo `docs/superpowers/specs/` tree is the raw source; these notes are the operator-readable version.
