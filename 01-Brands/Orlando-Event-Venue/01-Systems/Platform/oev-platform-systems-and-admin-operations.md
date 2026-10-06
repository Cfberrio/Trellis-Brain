---
brain_note_id: "note:2616824d-8dfd-4865-b5c4-7387f2df7862"
canonical_key: "oev-platform-systems"
brand_id: "orlando_event_venue"
---
# OEV Platform Systems and Admin Operations

## Canonical Statement

- **rule**: The booking system enforces business rules including Monday–Thursday availability constraints, minimum hour requirements, space-specific capacity limits, and non-overlapping reservation logic.
- **fact**: The OEV booking database uses a 'two-axis' model tracking both event status and payment status, secured with Row Level Security (RLS) and server-side pricing calculations.
- **process**: The Admin Dashboard provides operational management for daily events, task queues, monthly revenue tracking, and a multi-view calendar (week/month/day) color-coded by space and status.
- **process**: Website leads are captured via a popup and automatically synchronized to GoHighLevel (GHL) CRM.

## Evidence Log

- 2026-10-05T03:16:11.322Z — `clickup_chat_thread:8cqnrff-2077/80170034978403`
  - `e1` (source_body): Esquema completo en Supabase: modelo de "dos ejes" (estado del evento + estado del pago), reglas de negocio (solo Lun–Jue, horas mínimas, capacidad por espacio, no solapamiento), precios server-side, y endurecimiento de seguridad (RLS).

## Provenance

- Source: `clickup_chat_thread` `8cqnrff-2077/80170034978403`
- Source hash: `f6c7c3b9623dde49d12e3710c1f78a3369b4d22095af1ea0b4928abed79015ae`
- Observed at: 2026-10-05T03:16:11.322Z
- Agent run: `d507a9c3-29c7-499c-ba5c-0f8c68c9940b`
- Validation run: `773b49d2-dbe9-4881-9b22-a6a59eee6038`
