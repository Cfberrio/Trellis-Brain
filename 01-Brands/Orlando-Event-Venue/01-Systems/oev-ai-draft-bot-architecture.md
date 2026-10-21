---
brain_note_id: "note:3d6255b6-b802-4076-9241-1a7090baff17"
canonical_key: "oev-ai-draft-bot-architecture"
brand_id: "orlando_event_venue"
---
# OEV AI Draft Bot Architecture

## Canonical Statement

- **process**: OEV AI draft bot architecture uses a polling-based system (2-min interval) to generate internal GHL comments, ensuring human review before sending. Grounding is dynamic, injecting live booking/availability data from the database, while stable facts (pricing/policies) are hardcoded in prompts. Security gates (score < 0.75) are enforced in code, not prompts. Founder voice is derived from verbatim threads, not brand adjectives.

## Evidence Log

- 2026-10-21T01:56:45.471Z — `clickup_doc_page:8cqnrff-22037/8cqnrff-30277#brand=orlando_event_venue`
  - `e1` (source_body): el bot postea [AI DRAFT — copy/edit/send manually] como InternalComment en GHL; un humano copia/edita/envía. ... cada llamada inyecta datos vivos: ACTIVE_PROGRAMS ... VENUE_AVAILABILITY + BOOKING_CONTEXT ... los prompts v2 se construyeron desde ~60 threads verbatim extraídos de los inboxes reales

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22037/8cqnrff-30277#brand=orlando_event_venue`
- Source hash: `af1301a3168bf1287525031c703b5abe0d7db3e39a5a8a3b99bfe6617309f3cd`
- Observed at: 2026-10-21T01:56:45.471Z
- Agent run: `21ae76be-ed07-462b-a62d-3964eb091916`
- Validation run: `111f2b69-1205-4b4e-a905-02a7eea2b8ea`
