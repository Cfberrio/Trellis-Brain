---
brain_note_id: "note:d0a78f5e-057d-4a4f-9115-36ad90922ade"
canonical_key: "qb-cc-reconciliation-rules"
brand_id: "trellis_core"
---
# QuickBooks-Credit-Card-Reconciliation-and-Cleanup

## Canonical Statement

- **rule**: In a QuickBooks parent/sub-account credit card structure, sub-accounts must always reconcile to $0; the parent account is the only one that carries the running balance.
- **process**: To reconcile sub-accounts, use transfers between the parent (payment receiver) and the sub-account. If the sub-account difference is negative, transfer funds from parent to sub. If positive (credits), transfer from sub to parent.
- **process**: To zero out balances on old, closed credit card accounts without affecting current-year taxes, create journal entries to Opening Balance Equity dated in a historical year (e.g., 12/31/2022).

## Evidence Log

- 2026-10-16T21:21:36.798Z — `clickup_doc_page:8cqnrff-18237/8cqnrff-23037`
  - `e1` (source_body): The key rule is that sub-accounts should always reconcile to $0... the parent/master is the only account that should keep the running balance across periods.
  - `e2` (source_body): If the sub-account’s reconciliation difference is negative, you generally transfer funds into the sub-account from the parent... If the difference is positive... you transfer out of the sub-account back to the parent.
  - `e3` (source_body): Instead, they created journal entries to zero out balances (paired lines between the card and Opening Balance Equity) dated 12/31/2022, so the balance sheet is clean going forward.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-18237/8cqnrff-23037`
- Source hash: `656c72109fabe7b3014c799d26f7b9e9ce4a7c4bff09fc72f2ea0347dda56741`
- Observed at: 2026-10-16T21:21:36.798Z
- Agent run: `4c531110-eb08-4dcd-8975-d3d69f15ab6f`
- Validation run: `3d9744de-9ece-44f6-88d4-86d7a741727d`
