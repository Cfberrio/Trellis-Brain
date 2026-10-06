---
brain_note_id: "note:373a53b3-10cf-487e-9077-552d007b6451"
canonical_key: "lovable-migration-plan"
brand_id: "discipline_rift"
---
# DR Lovable Migration and App Unification Plan

## Canonical Statement

- **decision**: Rebuild the Discipline Rift software ecosystem as a single Lovable app (React + Vite + Tailwind + shadcn + native Supabase) with role-gated surfaces for parents, coaches, and admins to eliminate logic duplication.
- **process**: Execute 'Workstream 0' backend hardening before any Lovable build: enable RLS on all 20 exposed tables, rotate plaintext secrets, lock public storage buckets, and fix broken cron jobs to prevent public data exposure.
- **rule**: Consolidate duplicated logic (recurring session calculators, auth flows, messaging) into single canonical sources within the unified app architecture.
- **process**: Normalize the Supabase data model during migration by enforcing snake_case naming conventions and moving backup tables out of the public schema.

## Evidence Log

- 2026-10-03T20:34:52.448Z — `clickup_chat_thread:8cqnrff-2077/80170035584177`
  - `e1` (source_body): Recommendation: rebuild as ONE Lovable app, one Supabase, role-gated into three surfaces (parent / coach / admin)... You stop maintaining the same feature three times.
  - `e2` (source_body): Workstream 0 — Backend hardening (blocker, do BEFORE any Lovable build)... Enable RLS + real policies on all 20 exposed tables... Fix the data layer first or you ship a breach.
  - `e3` (source_body): Four pieces of logic are duplicated across surfaces. Each becomes one canonical source in the rebuild
  - `e4` (source_body): Normalize naming: Newsletter, Drteam, Partners_Program, Level (capitalized, mixed-case) → consistent snake_case. Pick a convention, apply once.

## Provenance

- Source: `clickup_chat_thread` `8cqnrff-2077/80170035584177`
- Source hash: `5c2f66a6bd8f6258b26d2967e1245f69edf33323cbd12669216042b0de10f164`
- Observed at: 2026-10-03T20:34:52.448Z
- Agent run: `29684dfa-76a2-433b-8983-5654151e77fe`
- Validation run: `acc29bed-be58-4609-9028-b81fffdf6422`
