---
brand: Discipline-Rift
area: systems
subarea: sales
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/superpowers/specs/2026-06-24-admin-dashboard-ghl-sync-design.md + commits 2026-08-15 → 2026-08-16 (sync hardening)"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - ghl
  - crm
---

# GHL Sync and Segmentation

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Sales/Sales-Home|DR Sales Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Sales/GHL-CRM-Pipeline-Spec|DR GHL CRM Pipeline Spec]]
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|DR GHL Marketing and Registration Automations]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Admin-Dashboard|Admin Dashboard]]

## What it does
Pushes DR parents who have at least one **paid** enrollment into GoHighLevel as contacts, from the admin dashboard (`/dashboard/ghl`). Full Sync (all paid) and Incremental Sync (recent window).

## Decisions that define the design
1. **Direct Contacts API upsert**, not webhook replay. Replaying webhooks would re-fire parent-facing GHL automations — an accidental mass send.
2. **Scope is paid only.** Parents with at least one enrollment whose `payment.status = 'paid'`, aggregated to **one GHL contact per parent**.
3. **Custom fields are auto-detected by name**, case-insensitive and normalized, by fetching the location's custom fields from the API. No hardcoded field ids. Missing fields are skipped rather than failing the sync.
4. **Secrets live in the environment**, never in code or chat. If they are absent the edge returns a clear "GHL not configured" error instead of failing silently.
5. **Admin-gated edge**, fail-closed, mirroring the campaign-email pattern.

Scale at design time: 1168 paid payments → **592 distinct parents with a paid enrollment**; 674 parents contactable in total.

## Hardening, August 2026
Each of these was a real production failure:
- **Stop erasing contact data on every sync.** The upsert was overwriting fields with blanks when the source value was absent.
- **Find the contact before overwriting it.** Matching had to be resolved first, otherwise the upsert created or clobbered the wrong record.
- **Keep the tags GHL owns.** A rewrite was dropping tags added inside GHL by the team; the sync now preserves them.
- **Page past PostgREST's 1000-row cap** on the enrollment query, which had been silently truncating the sync.
- **Report drift** so a broken sync stops being invisible, and **alert only on the nightly run**, not on manual syncs, so the alert keeps meaning something.

## Segmentation
Contacts are segmented **by school and by team without cross-season false matches** — the same school name in two seasons must not merge into one segment. This is what makes a targeted campaign to "volleyball parents at one school this season" possible.

## Operating rule
GHL is the CRM and messaging surface. The DR database remains the source of truth for who paid. When they disagree, the database wins and the sync is the thing to fix.
