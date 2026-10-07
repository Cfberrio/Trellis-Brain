---
brain_note_id: "note:396024d4-ecf2-495d-b959-82cae3fc1599"
canonical_key: "parent-portal-login-gmail-logic"
brand_id: "discipline_rift"
---
# Parent Portal Login and Gmail Dot Logic

## Canonical Statement

- **fact**: The parent portal login system (Supabase) is dot-sensitive for Gmail addresses, treating 'user@gmail.com' and 'u.s.e.r@gmail.com' as distinct accounts, whereas Gmail treats them as the same inbox.
- **process**: If a parent experiences a login loop or 'another active session' error, verify if they have multiple accounts (with/without dots). Resolve by renaming the unused account and linking the child to the email address matching the GHL record.
- **rule**: The parent portal login screen must display the specific email address associated with the active session to help users identify which account they are logged into.

## Evidence Log

- 2026-10-07T15:09:55.891Z — `clickup:86e3k6nhw`
  - `e1` (source_child): 2 cuentas de login (gmail con y sin puntos), solo una ligada a su fila de padre. Entraba con la otra y el aviso "another session" la mandaba a salir y volver a entrar con el mismo correo, en bucle. Lydia: paid y activa en VOLLEYBALL BLANKNER.
  - `e2` (source_child): Para Gmail son el mismo correo: todo le llega a la misma bandeja. Para nuestro sistema son dos personas distintas. Lydia quedó conectada a la cuenta con puntos.
  - `e3` (source_child): Decidí: renombrar la cuenta suelta (reversible, 0 datos) y pasar la cuenta ligada al correo sin puntos (= parent.email = GHL). Verificado con su sesión simulada: 1 hija, 4 mensajes visibles.

## Provenance

- Source: `clickup` `86e3k6nhw`
- Source hash: `bd021f5915ebca3662961158bc1a82cfdde1bc7841ec8f4d66b642206dd574ae`
- Observed at: 2026-10-07T15:09:55.891Z
- Agent run: `87251c25-265b-49cc-89af-ea0eab7a36c5`
- Validation run: `8f4eeed2-bfee-46d8-8866-4e937d180ef8`
