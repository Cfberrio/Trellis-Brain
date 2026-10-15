---
brain_note_id: "note:8aa080e0-4712-4d14-85fb-0b87030ce9e0"
canonical_key: "ocia-database-reconciliation-process"
brand_id: "st_joseph"
---
# OCIA Database Reconciliation and Participant Management

## Canonical Statement

- **process**: Reconcile OCIA attendance by matching ClickUp attendance lists with the St. Joseph database, recording attendance against specific session dates and adding participant comments to staff-only profile notes.
- **rule**: When processing withdrawals, only remove participants who have explicitly confirmed they will no longer attend via email; a missed class or lack of reply is not sufficient for removal.
- **process**: New registrants from Microsoft Forms or QR codes must be added to the database by creating missing profiles and enrolling them in the appropriate OCIA/adult-sacrament group while preserving baptism-based classifications.
- **rule**: Staff must identify attendees with incomplete names (e.g., first name only) by cross-referencing their provided email addresses.

## Evidence Log

- 2026-10-15T07:35:01.036Z — `clickup:86e3pxguj`
  - `e1` (source_body): Review withdrawal replies in both mailboxes... Match each confirmed withdrawal to the correct database profile and document the reply/date before removing them as Luis requested. A missed class or no reply is not confirmation of withdrawal.
  - `e2` (source_child): Lo que cada persona escribió o marcó quedó como nota de staff en su perfil (solo la ve el staff)... Los que pusieron solo el primer nombre ("Keaton", "Ethan", "Alejandra", "DEMI") se identificaron por su email.

- 2026-10-15T21:33:04.652Z — `clickup:86e3pxguj` (validation `e3bb8f5e-06f7-4f2e-b32a-37b8a2f539dc`)
  - `e3` (source_child): Move: la persona sigue con nosotros, pero en otro grupo... Archive: la persona confirmó que ya no viene. Faltar a clase o no contestar no cuenta... En "Why" escribes el motivo (es obligatorio) y confirmas... En su perfil queda una nota de staff: "Moved from A..."
- **process**: Use the 'Move' button to transfer a participant to a different parish group (e.g., Adult Faith Formation, Marriage, Bible Study) while they remain active in the parish.
- **rule**: When moving a participant to another group, providing a reason in the 'Why' field is mandatory.
- **process**: Use the 'Archive' button only when a participant has explicitly confirmed they are no longer attending; this action removes them from active lists and counts.
- **fact**: Moving a participant automatically generates a staff note in their profile documenting the transfer (e.g., 'Moved from Adult Sacraments to...').

## Provenance

- Source: `clickup` `86e3pxguj`
- Source hash: `7547d45bcc61358f06f8c924eb312d40f0f9006b6c530d701abcbb5a9ced98c6`
- Observed at: 2026-10-15T07:35:01.036Z
- Agent run: `a19fea38-6d14-45ff-bbac-8e780d654a15`
- Validation run: `24525a4d-711f-4b6a-b28c-9f8578963ed4`
