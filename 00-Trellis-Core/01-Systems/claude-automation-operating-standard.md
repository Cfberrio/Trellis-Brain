---
brain_note_id: "note:5179b88b-7b53-4106-a9cc-2588b0f101b7"
canonical_key: "claude-automation-operating-standard"
brand_id: "trellis_core"
---
# Claude-Automation-Operating-Standard

## Canonical Statement

- **decision**: The standard operating procedure for Claude-assisted web tasks is: 1) Use connectors or APIs first if available. 2) Use the Claude Chrome extension for tasks requiring the user's active session (e.g., GHL, Meta Ads, Stripe). 3) Use Playwright for isolated testing, QA, or flows requiring a clean state.
- **rule**: Playwright should be used with the --isolated flag for QA and unknown sites to prevent session contamination.
- **rule**: To mitigate security risks, sensitive sites like Stripe and Gmail should be removed from the Claude extension's approved list, requiring manual intervention for sensitive actions.

## Evidence Log

- 2026-11-11T20:17:58.084Z — `clickup_doc_page:8cqnrff-27057/8cqnrff-40377`
  - `e1` (source_body): Uso la extensión de Claude en Chrome cuando la tarea necesita una sesión ya abierta. Uso Playwright para probar nuestras apps y para flujos que hay que repetir desde cero. Si existe conector o API, no uso ninguno de los dos

## Provenance

- Source: `clickup_doc_page` `8cqnrff-27057/8cqnrff-40377`
- Source hash: `c8d8eb4ceb162216b10475650a1ff61b0280ed231e616eac18ac673021d56155`
- Observed at: 2026-11-11T20:17:58.084Z
- Agent run: `ffce9557-cc03-4495-bc3d-1274fb1419dd`
- Validation run: `d2fde54d-89ab-4605-b162-a05c71255abd`
