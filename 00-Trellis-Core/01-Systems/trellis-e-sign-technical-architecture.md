---
brain_note_id: "note:349c7f17-fe2b-4ca8-ba9b-a4081e27d498"
canonical_key: "trellis-e-sign-technical-architecture"
brand_id: "trellis_core"
---
# Trellis E-Sign Technical Architecture

## Canonical Statement

- **decision**: The trellis-e-sign tech stack consists of TanStack Start (React 19 SSR), Tailwind 4, and shadcn/ui for the frontend, with Lovable Cloud (Supabase) for the backend (Postgres, Auth, Storage, Deno Edge Functions).
- **decision**: Sensitive logic is handled via Deno Edge Functions, including 'create-signature-request' (token generation/emailing), 'submit-signature' (server-side validation/audit), and 'finalize-document' (PDF flattening/certification).
- **process**: The deployment workflow involves local development pushed to GitHub (main branch), which Lovable synchronizes to publish the frontend and deploy Edge Functions; SQL migrations are stored in supabase/migrations/.
- **fact**: Email communication uses Gmail SMTP via denomailer, requiring GMAIL_USER and GMAIL_APP_PASSWORD secrets.

## Evidence Log

- 2026-10-18T04:52:09.711Z — `clickup_doc_page:8cqnrff-22317/8cqnrff-30977`
  - `e1` (source_body): Frontend: TanStack Start (React 19 SSR) + Tailwind 4 + shadcn/ui. Backend: Lovable Cloud = Supabase (Postgres + Auth + Storage + Edge Functions en Deno). Edge Functions (lógica sensible, nunca en el cliente): create-signature-request, submit-signature, finalize-document...

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22317/8cqnrff-30977`
- Source hash: `9957a05e20c0e0b8f57cfdd91def84d82bd5459c85700087aa7a02ff2ec436cd`
- Observed at: 2026-10-18T04:52:09.711Z
- Agent run: `d1cfd103-bd61-452d-a03a-b8d97ed3f9d5`
- Validation run: `81e61805-beff-40e6-b6ed-90345a6f3a64`
