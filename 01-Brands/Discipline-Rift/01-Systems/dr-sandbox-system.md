---
brain_note_id: "note:14f5e569-3f29-49bd-9eb7-382f384451c5"
canonical_key: "dr-sandbox-system"
brand_id: "discipline_rift"
---
# DR Sandbox System

## Canonical Statement

- **decision**: Discipline Rift maintains a live sandbox environment at https://disciplinerift.com/demo for sales and system demonstrations.
- **rule**: The sandbox must run on the same live code as production but use data tagged 'sandbox' to ensure zero visibility of real parent, child, or payment data.
- **rule**: Demo users and actions must never trigger real side effects, including GoHighLevel emails, SMS, push notifications, or real Stripe charges.
- **fact**: The sandbox includes five demo roles: Admin dashboard, Coach dashboard, Parent portal, Registration, and Public website, with auto-login functionality.

## Evidence Log

- 2026-10-07T19:55:10.652Z — `clickup:86e3m8qbh`
  - `e1` (source_body): Build a Discipline Rift sandbox: one link that opens a demo hub where anyone we're presenting to can jump into every DR dashboard we've built, logged in as a demo user for each role. It must run on the same live code as production
  - `e2` (source_child): Discipline Rift sandbox is live at https://disciplinerift.com/demo... one link, five tiles: Admin dashboard, Coach dashboard, Parent portal, Registration, Public website. One click logs in as the demo user for that role.

## Provenance

- Source: `clickup` `86e3m8qbh`
- Source hash: `27864011e2e405908f0c2386e439f84d0a19dbe8fd4bfc91a80f45216633e3c3`
- Observed at: 2026-10-07T19:55:10.652Z
- Agent run: `d712aadf-317b-471c-8283-0ae0aa686912`
- Validation run: `e740352c-32bd-4a11-a931-a295c9aee796`
