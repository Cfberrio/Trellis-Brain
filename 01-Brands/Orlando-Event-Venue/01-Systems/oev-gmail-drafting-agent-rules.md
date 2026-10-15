---
brain_note_id: "note:05d89374-905d-49e3-9c9a-b773eacaa11e"
canonical_key: "gmail-drafting-agent-rules"
brand_id: "orlando_event_venue"
---
# OEV Gmail Drafting Agent Rules

## Canonical Statement

- **rule**: The Gmail Drafting Agent must only create drafts and never send emails; it uses MEMORY.md as the single source of truth for venue facts and policies.
- **process**: The agent follows a strict eligibility gate: it must draft for website contact forms (identified by specific subject/body strings) and human inquiries, but must skip system, security, and automated emails.
- **rule**: Drafts must lead with capacity (up to 90 guests) if asked, use plain text, include a 50% deposit requirement, and ask a maximum of 1–3 concise questions if details are missing.
- **process**: For contact forms, the agent must create in-thread replies using the Reply-To header or extracted body email, applying the OEV_AUTODRAFTED label upon completion.

## Evidence Log

- 2026-10-15T00:48:20.914Z — `clickup_doc_page:8cqnrff-13217/8cqnrff-14057`
  - `e1` (source_body): Draft only: Create Gmail drafts; never send email. Source of truth: Use MEMORY.md for business facts/policies. If not in MEMORY.md → treat as UNKNOWN/TBD.
  - `e2` (source_body): Treat as Contact Form if ANY is true: Subject starts with: "Contact Form -" Body contains: "New Contact Form Submission"
  - `e3` (source_body): ALWAYS SKIP — System/Security/OTP/Automations (no draft) Skip if ANY is true AND it is NOT a Contact Form: From contains: no-reply | noreply | mailer-daemon | postmaster
  - `e4` (source_body): “Capacity first” rule: If asked about capacity, lead with: “Capacity: up to 90 guests.” ... Ask when missing: If the email lacks key details, ask 1–3 short questions (max).
  - `e5` (source_body): Include only what’s in MEMORY.md: Deposit 50%; balance due 15 days before; access instructions sent ~72 hours prior.
  - `e6` (source_body): For Contact Forms, ALWAYS create the draft as an IN-THREAD reply... After creating the draft: gog --no-input gmail thread modify <THREAD_ID> --add OEV_AUTODRAFTED --remove UNREAD

## Provenance

- Source: `clickup_doc_page` `8cqnrff-13217/8cqnrff-14057`
- Source hash: `b77f959f3af323e2a1541fcb8db3870ca15100f0719453f7cbc4ff1ba0afe998`
- Observed at: 2026-10-15T00:48:20.914Z
- Agent run: `b02eb090-11ef-4f48-ba54-234c5fca3951`
- Validation run: `6d0a7036-a81b-43f8-a566-747d01cb32c1`
