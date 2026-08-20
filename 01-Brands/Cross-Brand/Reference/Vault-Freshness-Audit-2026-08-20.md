---
brand: Cross-Brand
area: reference
subarea: audit
note_type: inventory
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Git history of 8 repos (2026-05-21 → 2026-08-20) + ClickUp doc deltas since watermark 2026-05-21 + vault inventory"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - audit
  - vault-health
  - cross-brand
---

# Vault Freshness Audit — 2026-08-20

## Parent
- [[01-Brands/Cross-Brand/Reference/Reference-Home|Cross-Brand Reference Home]]

## Related
- [[01-Brands/Cross-Brand/Cross-Brand-Home|Cross-Brand Home]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|DR Platform Home]]

## The finding
The last comprehensive ingestion into this vault was **2026-05-21**. Between then and **2026-08-20**, roughly three months of product and operations work shipped that had **no representation here at all**.

Measured across the repos:

| Repo / brand | Commits since 2026-05-21 | Vault coverage before this audit |
|---|---|---|
| OEV-PROJECT | 167 | zero platform coverage |
| disciplinerift (DR) | ~90 | product notes frozen at the backend migration |
| TrellisEsign (TF product) | ~25 | none |
| D-space (RV) | ~25 | partial, D-space folder only |
| CheeseToShare | 3 (branding) | not affected |
| RenewalOS | ~25 (Jun 4 burst) | none |
| CLAUDE CODE (Meta Ads Intelligence) | ~20 | current — already synced |

The gap was **not** in strategy or brand notes. Those are healthy. The gap was in **how the businesses actually run now**: the software, the money flow, the automations, the measurement layer.

## Why it drifted
Documentation was written — and written well — but it was written **into the repos** (`docs/`, `docs/superpowers/specs/`) and into ClickUp, not into the vault. Two consequences:

1. Anything that reads this vault for context (including AI assistants) was answering from a May-2026 picture of DR and OEV.
2. Notes that were correct in May became **actively wrong** rather than merely incomplete — see the stale-facts list below.

## Stale facts found and corrected
| Note | Was | Now |
|---|---|---|
| [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Pop-Up-Lead-Magnet-Sequence\|OEV Pop-Up Lead Magnet Sequence]] | HOST100 / $100 credit as the live offer | marked superseded; live offer is Event Planning Kit + **PLAN50** |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Marketing-Home\|DR Marketing Home]] | "neither Pixel nor CAPI has been modified" | corrected: measurement layer shipped Aug 5–20; the ads **account** is what remains untouched |
| [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home\|OEV Brand Home]] | Marketing-Home listed as deferred / not built | Marketing and Platform hubs now active and linked |

## What was ingested in this pass

### Orlando Event Venue — 10 new notes
[[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|Platform Home]] with:
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]] — the two-axis model (operational vs financial), derived "LEAD", guards, multi-venue policy flags
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Types-and-Policies|Booking Types and Policies]] — website / internal / external, full comms matrix
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Automation-Jobs-and-Cron|Automation, Jobs and Cron]] — three layers, `pg_cron` truth, one_hour_report, July safety belts
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Payments-Invoices-and-Fees|Payments, Invoices and Fees]] — three invoice systems, Stripe Connect balance pattern, fee persistence
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Staff-Console-and-Payroll|Staff Console and Payroll]] — role-based console, payroll-item concept
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Access-Codes-and-Guest-Report|Access Codes and Guest Report]]

[[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Marketing-Home|Marketing Home]] with:
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Google-Ads-Post-Mortem-2026-06|Google Ads Post-Mortem — June 2026]] — the highest-value document recovered in this audit
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit|Lead Magnet — Event Planning Kit]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Website-One-Page-Redesign-2026-07|Website One-Page Redesign — July 2026]]

Plus [[01-Brands/Orlando-Event-Venue/05-Operations/Agent/Gmail-and-SMS-Draft-Agent|Gmail and SMS Draft Agent]].

### Discipline Rift — 10 new notes
[[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|Platform Home]] with:
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Website-Product-Standard|Website Product Standard]] — the approved copy and visual rules for the public site
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]] — OTP, re-enroll fast path, resumable checkout, 5-minute hold
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Team-Status-and-Season-Model|Team Status and Season Model]] — single status field, season model, school exceptions and exclusions
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Waitlist-System|Waitlist System]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Payments-Fees-and-Receipts|Payments, Fees and Receipts]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Admin-Dashboard|Admin Dashboard]]

Marketing: [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Tracking-and-Attribution|Meta Tracking and Attribution]] · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Retargeting-and-Audiences|Meta Retargeting and Audiences]]
Sales: [[01-Brands/Discipline-Rift/01-Systems/Sales/GHL-Sync-and-Segmentation|GHL Sync and Segmentation]]
Ops: [[01-Brands/Discipline-Rift/05-Operations/SOPs/Season-Schedule-Load-SOP|Season Schedule Load SOP]]

### Trellis Fields — 1 new note
- [[01-Brands/Trellis-Fields/04-Projects/Trellis-eSign/Trellis-eSign-Home|Trellis e-Sign]] — a shipped product with zero prior vault coverage.

## Backlog — identified, not yet ingested
Everything below was located during the audit and is real, useful material. It is queued, not lost.

### Priority 1 — meetings (12 docs, ClickUp)
Dev SyncUps and founder sessions from **2026-05-26 through 2026-08-18** are absent; the vault's meeting record stops at 2026-05-21. Sequence: 05/26, 06/04, 06/10, 06/11, 06/12 (Trelling Creative), 07/30, 08/04, 08/05, 08/14, 08/18, plus the two RenewalOS blocks of 05/26.
Route per [[01-Brands/Cross-Brand/Meetings/Meetings-Home|Meetings Home]] rules.

### Priority 2 — ClickUp docs with no vault note
- **DR:** `DISCIPLINERIFT.COM` (FRONTEND, DATABASE, /ADMIN, /COACHES, /PARENTS, NOTIFICATIONS, SPORT DESCRIPTIONS), `INTERVIEW SOP` + `INTERVIEW TRAINING` (a full interview training manual plus three candidate analyses), `EMAIL AUTOMATION` tonality examples, `REPLIELS` v3, School Profiles / registration exclusions doc.
- **OEV:** `AUTOMATIONS` (BOOKING, AI AGENT), `EMAILS` (EMAIL REPLIES, SMS REPLIES), `Email Extraction (GMAIL + GHL)`, `GOOGLE ADS` KEYWORDS.
- **RV:** 3D virtual tour photo specs, `LOGICA A IMPLEMENTAR`, `PENDIENTES POR REALIZAR`, D'SPACE ARCHITECTURE + UPDATES.
- **Cross-brand / Claude space:** `SKILLS` (all skills), `AI EDITING` prompts per brand, `AE EDITING`, `USAGE` + usage dashboard tutorial, `Remote control`, `MCP / COMPOSIO`, **`Auditoria CREDITOS LOVABLE`**.
- **CTS:** AI Gmail draft agent CTS, SMS + Email drafts v3 (ORDER_CONTEXT), customer inquiry examples.
- **ROS / RenewalOS:** PLANNING/MVP, ARCHITECTURE (USER, PROPERTIES) — a whole product line with no vault presence. Decide whether RenewalOS becomes a brand folder before ingesting.

### Priority 3 — repo material not yet lifted
- OEV: reschedule feature, revenue report schema, external booking summary, GA4/Google Tags setup, venue onboarding provisioning runbook, virtual tour photo specs.
- DR: parent dashboard, coach dashboard, coach messaging, parent absence reporting, certificates, coupons, email campaigns, GSAP motion redesign, production SSR runbook.
- D-space: pricing split model (20% as RV management fee via Connect, not a markup) and the WF2 remaining-balance build — partially covered, needs reconciliation with the [[01-Brands/Reliable-Venues/D-space/Logica-de-Estados|D-space state logic]] notes.

## The process fix
The gap is a workflow problem, not a diligence problem. Two changes stop it recurring:

1. **Definition of done includes the vault.** A feature is done when the repo spec exists *and* the matching vault note is created or updated. The specs already get written; they just stop at the repo boundary.
2. **Monthly sync run**, not quarterly. Three months of drift produced roughly 20 notes of catch-up work and, worse, three notes that were confidently wrong. A monthly pass keeps each run small enough to actually happen.

Owner: Cristian. Next run due: **2026-09-20**.
