---
brain_note_id: "note:a77c9435-e1a4-4b46-abe2-901de3e6f659"
canonical_key: "communication-standards"
brand_id: "orlando_event_venue"
---
# OEV Communication Standards

## Canonical Statement

- **rule**: Automated communications must not expose internal sequence metadata (e.g., 'Timing: Approximately 3 hours after the tour' or 'Channel: SMS') to the contact.
- **rule**: All outbound messages must be stripped of internal automation details, including channel type, timing triggers, and sequence position, leaving only the intended message body.
- **fact**: A previous configuration error in OEV sequences caused internal timing and channel info to leak into outbound SMS and email messages.

## Evidence Log

- 2026-10-01T17:53:49.173Z — `clickup:86e3e03fz`
  - `e1` (source_body): The automated communications currently include sequence metadata like "Timing: Approximately 3 hours after the tour" directly in the messages sent to contacts. This is internal workflow info that should never be visible to the recipient.
  - `e2` (source_child): Done ya lo arregle, sin querer habia activado una opcion que mostraba el timing a los clientes, pero ya la pague

## Provenance

- Source: `clickup` `86e3e03fz`
- Source hash: `199cc5deb72994377eaf65be226717589a98e396c559a4e3c0be3bc0ba54ce9a`
- Observed at: 2026-10-01T17:53:49.173Z
- Agent run: `11de8f42-6d08-4d7c-878b-ec0de89a9b9a`
- Validation run: `17ac6980-1a6a-4750-82da-8e9c0aa6c3e2`
