---
brand: Orlando-Event-Venue
area: systems
subarea: platform
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT repo docs/ tree (commits 2026-05-22 → 2026-08-20) + ClickUp OEV/SOFTWARE/AUTOMATIONS"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: system-hub
tags:
  - oev
  - platform
  - canonical
---

# OEV Platform Home

## Parent
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|OEV Brand Home]]

## Children
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Types-and-Policies|Booking Types and Policies]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Automation-Jobs-and-Cron|Automation, Jobs and Cron]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Payments-Invoices-and-Fees|Payments, Invoices and Fees]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Staff-Console-and-Payroll|Staff Console and Payroll]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Access-Codes-and-Guest-Report|Access Codes and Guest Report]]

## Related
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-Admin-Command-Center|OEV Admin Command Center]]
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-Staff-Operations-Console|OEV Staff Operations Console]]
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Operating-System|OEV GoHighLevel Operating System]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Marketing-Home|OEV Marketing Home]]

## What this section is
The OEV product is not just a website. It is a booking platform with an admin dashboard, a staff console, a payment engine, and an automation backbone. This hub is the entry point for anything that touches how the software actually behaves.

Route here before changing checkout logic, booking states, staff assignment, invoices, payroll, access codes, reminders or any scheduled communication.

## Stack (as of 2026-08-20)
- React 18 + TypeScript + Vite, shadcn/ui + Tailwind, TanStack Query, React Router v6.
- Supabase: Postgres, Edge Functions (Deno), Storage, `pg_cron`.
- Stripe Checkout + Stripe Connect for payments and transfers.
- GoHighLevel as CRM / calendar / messaging surface, synced from the platform.
- Repo: `OEV-PROJECT`. Docs live in `docs/` (features, automation, testing, deployment, marketing).

## Three surfaces
| Surface | Who uses it | Where |
|---|---|---|
| Public site + booking wizard | Clients | `/` one-page + `/book` |
| Admin dashboard | Luis / managers | `/admin/*` |
| Staff console | Production, Assistant, Custodial, Bar Vendor | `/staff/*` |

## Operating rules that carry across the platform
- The booking has **two independent state axes** (operational and financial). Never merge them. See [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]].
- Almost nothing executes inline. Events **schedule** future work in `scheduled_jobs`, and a cron drains it. See [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Automation-Jobs-and-Cron|Automation, Jobs and Cron]].
- Booking behaviour is driven by **policies per booking origin**, not by branching code. See [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Types-and-Policies|Booking Types and Policies]].
- Money is the only motor of the financial axis. The calendar never moves it.

## Next step
When a platform change lands, update the matching child note the same week. The 2026-05 → 2026-08 gap in this vault happened because product shipped and documentation stayed in the repo.
