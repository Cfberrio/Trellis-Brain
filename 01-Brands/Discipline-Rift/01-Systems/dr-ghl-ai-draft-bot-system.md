---
brain_note_id: "note:8a495431-7204-46fb-9247-9c030853aa0b"
canonical_key: "ghl-ai-draft-bot-system"
brand_id: "discipline_rift"
---
# DR GHL AI Draft Bot System

## Canonical Statement

- **process**: The GHL AI Draft Bot polls unread SMS and email every 2 minutes, generating internal notes for human review rather than sending direct replies to ensure zero-tolerance for error with parents.
- **rule**: The bot uses dynamic grounding via ACTIVE_PROGRAMS (team, school, session tables) and CURRENT_DATETIME to ensure it never cites stale prices, dates, or non-existent programs.
- **rule**: Bot responses are segmented by audience: Parents (empathy/resolution), Schools (professional/trust items like COI and ratios), and Staff (gratitud/date confirmation).
- **rule**: Safety gates (score < 0.75) and specific topics (refunds, behavior complaints, weather cancellations) trigger a mandatory flag_human status, suppressing the AI draft.
- **fact**: The bot includes a 10% sibling discount code (SIBLING) and specific school trust items (Level-2 screening, 1:10 ratios, Facilitron) in its knowledge base.

## Evidence Log

- 2026-10-17T22:40:52.835Z — `clickup_doc_page:8cqnrff-21997/8cqnrff-30237`
  - `e1` (source_body): bot que lee las conversaciones unread de GHL (SMS + email)... se postea como nota interna [AI DRAFT — copy/edit/send manually] — nunca envía directo; un humano revisa y envía.
  - `e2` (source_body): ACTIVE_PROGRAMS — catálogo real desde las tablas team + school + session... el prompt prohíbe citar cualquier programa/precio/fecha que no esté en este bloque.
  - `e3` (source_body): Detección de audiencia con voz por audiencia... PARENT (default): empatía primero... SCHOOL/FACULTY: profesional, organizado... COACH/STAFF: gratitud + read-back exacto.
  - `e4` (source_body): Anti-errores: refunds → siempre flag_human... quejas de comportamiento/roster → flag_human... decisiones de cancelación por clima el mismo día → flag_human.
  - `e5` (source_body): código SIBLING = 10% para hermanos... trust items que las escuelas preguntan: seguro de responsabilidad con COI... level-2 background screening de coaches, ratios ~1:10.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-21997/8cqnrff-30237`
- Source hash: `fdbc0d62bfa5a432d3ec031be019d85eefd96aa52971d3c3d9782fcbf25d4345`
- Observed at: 2026-10-17T22:40:52.835Z
- Agent run: `e2cf39d6-2367-4ce1-9aaf-50ca60d13fc4`
- Validation run: `e14081c4-135e-4f50-ad66-04d38a7294c8`
