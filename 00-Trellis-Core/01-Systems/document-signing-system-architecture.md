---
brain_note_id: "note:1eb2866e-ca84-48c4-bf35-378d5f53a6db"
canonical_key: "document-signing-architecture"
brand_id: "trellis_core"
---
# Document Signing System Architecture

## Canonical Statement

- **fact**: The system uses a public schema with core tables: profiles (account limits/status), documents (lifecycle states), signers (token hashes), fields (positioning), audit_events, and usage_counters.
- **rule**: Security is enforced via RLS: owners manage their own data, admins have global SELECT access, and signers access via Edge Functions using service-role after token validation.
- **rule**: A trigger prevents users from escalating their own privileges by blocking changes to columns like is_admin, plan, status, and monthly_limit.
- **process**: Legal evidence for signatures includes explicit consent, SHA-256 hashes of original/final PDFs, and identity metadata (IP, user agent, timestamps) printed on a Certificate of Completion.
- **process**: Automated expiration is handled by pg_cron running hourly, marking documents as expired after 14 days and invalidating their tokens.

## Evidence Log

- 2026-10-18T04:52:42.760Z — `clickup_doc_page:8cqnrff-22317/8cqnrff-30997`
  - `e1` (source_body): Tablas principales (schema public) profiles — perfil de cuenta... documents — estados draft → sent → viewed → partial → completed → expired → voided... signers — token_hash... fields... audit_events... usage_counters.
  - `e2` (source_body): Seguridad (RLS) El dueño ve/gestiona solo lo suyo... El admin tiene SELECT global... El firmante no usa auth: accede solo vía Edge Function... Trigger anti-escalación: bloquea que un usuario cambie sus propias columnas privilegiadas.
  - `e3` (source_body): Evidencia legal por firma Consentimiento explícito · intención ("I Agree and Sign") · integridad (hash SHA-256 del PDF original y final) · identidad (email + IP + user agent + timestamps) · audit trail completo.
  - `e4` (source_body): PDF final + Certificado El PDF final es aplanado (no editable) con firmas/campos embebidos + una página de Certificado de Completado con: título, ID del documento, dueño, firmante(s), método de firma, todos los timestamps.
  - `e5` (source_body): Expiración automática (pg_cron) Los documentos reciben expires_at (+14 días) al enviarse. Un job de pg_cron corre cada hora (expire_stale_documents()): marca expired los documentos vencidos.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22317/8cqnrff-30997`
- Source hash: `b90af93553c2c160a90b4a65c73bd22bc07cdef5166b63c6751db35a768ebe89`
- Observed at: 2026-10-18T04:52:42.760Z
- Agent run: `ed89b12b-50e8-41fe-a84d-d98c5d7fb09f`
- Validation run: `bb85414d-376b-4ea6-887c-39fe17d7bc5e`
