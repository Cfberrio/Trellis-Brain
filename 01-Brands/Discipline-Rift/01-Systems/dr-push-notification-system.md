---
brain_note_id: "note:e92d7d77-c6e7-4642-b8c4-fbbf133bdc94"
canonical_key: "dr-push-notification-system"
brand_id: "discipline_rift"
---
# DR Push Notification System

## Canonical Statement

- **process**: The Discipline Rift push notification system uses specific templates for chat messages, weekly practice reminders, and escalations. Reminders are sent at 3 PM the day before practice, and content is managed via the 'App Reminders' admin section.
- **rule**: Push notifications require the app to be installed, a logged-in session, and notification permissions enabled. Duplicates are prevented by a registration check before sending, and failed sends are not retried after the initial attempt.

## Evidence Log

- 2026-11-18T04:23:55.343Z — `clickup_doc_page:8cqnrff-27437/8cqnrff-40857`
  - `e1` (source_body): Los textos entre llaves se llenan solos: {child} = nombre del niño, {sport} = deporte, {time} = hora de la práctica, {school} = escuela. ... Sin duplicados: cada push se registra antes de enviarse, así que nadie recibe dos veces el mismo.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-27437/8cqnrff-40857`
- Source hash: `777fb35e1aef210522095278043493e6db5f999e826261679ddf788d58dce27e`
- Observed at: 2026-11-18T04:23:55.343Z
- Agent run: `529e6b98-a467-4c2f-994e-bf224fd1bdcb`
- Validation run: `5138be95-037e-4261-bf10-427c586cd2d0`
