---
brain_note_id: "note:0c4ae7a2-2587-4615-86de-b0ff4e207349"
canonical_key: "registration-payment-systems"
brand_id: "discipline_rift"
---
# Registration and Payment Systems

## Canonical Statement

- **decision**: The Discipline Rift registration platform is built as one-child-per-checkout; bundling multiple children into a single transaction requires custom development across registration, payments, and reporting.
- **rule**: Discipline Rift only accepts card payments; Klarna is not a native option. Parents using Klarna virtual cards are subject to separate credit approvals for each transaction if children are registered separately.
- **fact**: Approximately 13.5% of families (110 out of 812) register two or more children, with many performing back-to-back transactions as a manual workaround for the lack of a multi-child cart.
- **rule**: The SIBLING discount code is the current manual workaround for multi-child families until a bundled checkout is implemented.

## Evidence Log

- 2026-10-13T20:49:43.263Z — `clickup:86e2xcxd5`
  - `e1` (source_body): Currently, the workaround is: register one child → apply the SIBLING code → pay → then repeat for the next child.
  - `e2` (source_child): The platform was built one-child-per-checkout from the ground up... Klarna is not currently an option in our checkout — we only accept cards. What the parent is almost certainly using is Klarna's one-time virtual card.

## Provenance

- Source: `clickup` `86e2xcxd5`
- Source hash: `d29f0a8ff89329bbc1b1ea39389c81d46643aebf83d5d822d2d44964e67a90a5`
- Observed at: 2026-10-13T20:49:43.263Z
- Agent run: `dc1cdc83-b05c-4a22-b5da-1e8334a720a0`
- Validation run: `00cf71d4-1510-44d2-882d-ee9be253eb49`
