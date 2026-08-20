---
brand: Discipline-Rift
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/admin-dashboard-resumen.md + docs/superpowers/specs (admin-dashboard series, Jun 2026) + commits Jul–Aug 2026"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - platform
  - admin
---

# Admin Dashboard

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|DR Platform Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Admin-Operations-App-Home|DR Admin Operations App Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Sales/GHL-Sync-and-Segmentation|GHL Sync and Segmentation]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Team-Status-and-Season-Model|Team Status and Season Model]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Tracking-and-Attribution|Meta Tracking and Attribution]]

## What it is
The full admin panel that replaced the legacy "admindr". Access is admin-only; everything else is blocked, fail-closed, with the same admin-gated edge-function pattern used across the app.

## Sections
| Section | What it does |
|---|---|
| Teams and Sessions | Create/edit teams with multi-day sessions, filters, enrolled list, PDF download (per-practice schedule PDF added Aug 2026) |
| Clone Season | Copy an entire season — teams + sessions — into a new one, with bulk date adjustment |
| Schools | Create/edit/search. Cannot delete a school with active teams |
| Coaches (Staff) | Create/edit/search. Cannot delete a coach with assigned sessions |
| Discount Coupons | Percentage or fixed amount, usage limits, date windows, activate/deactivate. Validated automatically at checkout |
| Certificates | Generates a personalized PDF per student, by sport and level, downloadable as a ZIP |
| Email Campaigns | Personalized emails to the parents of a team. Four-step wizard, 17 auto-filled variables, brand template or free HTML |
| Applications | Coach application intake and review |
| GHL Sync | Push paid parents to GoHighLevel as contacts — see [[01-Brands/Discipline-Rift/01-Systems/Sales/GHL-Sync-and-Segmentation\|GHL Sync and Segmentation]] |
| Manage Roster | Roster with parent contact columns, refund-and-remove, and the team waitlist |
| Meta Ads | Ad performance without writing SQL (added 2026-08-20) |

## Additions after the initial build
- **Meta Ads page** — reads the attribution views so ad performance is answerable in the dashboard instead of in SQL. See [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Tracking-and-Attribution|Meta Tracking and Attribution]].
- **Email Campaigns brought back** after being parked, with test sends routed to a field the sender controls (defaulting to the DR ops inbox) so a test can never reach real parents.
- **Roster payments** visible on the roster, plus refund-and-remove in one action.
- **Season ordering and a default season** so admin screens open on the right data.
- **Session edit fixed** — editing a session silently kept the old `day_of_week`, which quietly corrupted schedules.
- **DR branding** applied to admin and coach shells (logo, blue accents) in August 2026.

## Security posture
- Admin-gated edges verify the caller's token, then re-check the `user_role` admin + brand with the service role. Fail closed on 401/403.
- Leftover backup tables were being served to the anon role and were locked down (2026-08-20). When a migration leaves a backup table behind, revoke it in the same migration.

## Next step
The dashboard is now the operational surface for a business running 55 schools. Any new section should be added to this table on the day it ships, with its access rule stated.
