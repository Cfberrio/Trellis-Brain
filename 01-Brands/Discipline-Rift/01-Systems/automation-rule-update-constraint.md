---
brain_note_id: "note:c29e31c4-c9d4-46dc-b786-620f7db7871f"
canonical_key: "automation-rule-update-constraint"
brand_id: "discipline_rift"
---
# Automation Rule Update Constraint

## Canonical Statement

- **rule**: Automation rule changes only apply to new events created after the change; they do not retroactively update or reschedule existing events already in the system's queue.

## Evidence Log

- 2026-10-27T02:13:22.567Z — `clickup_chat_thread:8cqnrff-9037/80170044749807`
  - `e1` (source_body): cambiar la regla no mueve las alarmas que ya estaban puestas. La alarma vieja sigue guardada en la base de datos con su hora vieja escrita a mano. La regla nueva solo aplica a reservas que entren de ahí en adelante.

## Provenance

- Source: `clickup_chat_thread` `8cqnrff-9037/80170044749807`
- Source hash: `6fef430ea3a0e5881f4e994c056cffd374a63d540c078a83ff67a850ed594f12`
- Observed at: 2026-10-27T02:13:22.567Z
- Agent run: `da451248-50f4-41a8-9c1f-c4babeaff259`
- Validation run: `a22649af-34f8-4825-84c5-a1a9c2ca7d65`
