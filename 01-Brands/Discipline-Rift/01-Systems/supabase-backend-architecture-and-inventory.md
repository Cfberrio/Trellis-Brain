---
brain_note_id: "note:fd2cebbd-d7f4-4c83-8544-a930119aa394"
canonical_key: "supabase-backend-inventory"
brand_id: "discipline_rift"
---
# Supabase Backend Architecture and Inventory

## Canonical Statement

- **fact**: The Discipline Rift backend is hosted on Supabase (Postgres 17.4.1) and serves as the data engine for the Admin Dashboard.
- **fact**: The data model follows a hierarchy of school > team > session/enrollment > student > parent.
- **fact**: Automations are handled via three routes: DB Triggers to Edge Functions, pg_cron scheduled jobs, and external webhooks (Meta/GHL).
- **process**: Edge Functions manage CRM sync with GoHighLevel for newsletter signups, paid registrations, and abandoned cart recovery (triggered after 60 minutes of inactivity).
- **rule**: AI-assisted SMS responses use Claude (claude-haiku-4-5) to generate drafts based on brand-specific prompts stored in the brand_prompts table.

## Evidence Log

- 2026-10-17T18:49:03.701Z — `clickup_doc_page:8cqnrff-21437/8cqnrff-29157`
  - `e1` (source_body): Un barrido completo del proyecto Supabase que alimenta el Dashboard DisciplineRift: tablas, relaciones, funciones de base de datos, triggers, Edge Functions, trabajos programados (cron)... Postgres: 17.4.1
  - `e2` (source_body): El núcleo del negocio sigue la jerarquía escuela → equipo → sesión / inscripción → estudiante → padre.
  - `e3` (source_body): Las tres rutas de automatización: 1. Triggers de DB → Edge Function... 2. Cron (pg_cron) → Edge Function / App... 3. Webhook externo → Edge Function.
  - `e4` (source_body): dr_ghl_abandoned_cron... busca inscripciones isactive=false, sin notificar... más viejas que ABANDONED_AFTER_MINUTES (default 60) y sin pago; envía a GHL_ABANDONED_WEBHOOK.
  - `e5` (source_body): ghl-sms-draft... llama a Claude (claude-haiku-4-5) con el prompt activo de brand_prompts, y según la decisión... publica un comentario interno en GHL.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21437/8cqnrff-29157`
- Source hash: `9fe7acfbe08af7915147f3533ccb83f5c23a758e43a1c428766f345c943ff267`
- Observed at: 2026-10-17T18:49:03.701Z
- Agent run: `f21e4096-867b-4ba9-9118-b8a30cded397`
- Validation run: `307855e2-63fc-41de-a25e-8631c2919f57`
