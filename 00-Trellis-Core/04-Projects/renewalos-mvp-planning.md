---
brain_note_id: "note:35b867fb-b63c-4403-b885-28cb986b08fd"
canonical_key: "renewalos-mvp-planning"
brand_id: "trellis_core"
---
# RenewalOS MVP Planning

## Canonical Statement

- **decision**: RenewalOS is a web platform for property owners to manage insurance policies, receive automated renewal reminders, and compare competing offers from brokers.
- **definition**: The platform uses three personas: Holder (customer/owner), Provider (external broker), and Admin (Toveros/CV Financial staff).
- **rule**: Policies are structured hierarchically: General Property (Grandfather), related policies like Flood/Liability (Children), and Endorsements (Grandchildren).
- **process**: Renewal reminders fire by default at 90, 60, and 30 days before expiration; the 90-day reminder automatically triggers the Request for Quote (RFQ) workflow.
- **definition**: Quotes are requested in three tiers: Silver (same coverage, market price), Platinum (same coverage, lower premium), and Gold (improved coverage and lower premium based on analysis).

## Evidence Log

- 2026-10-17T00:41:15.148Z — `clickup_doc_page:8cqnrff-19237/8cqnrff-25137`
  - `e1` (source_body): A web platform that lets property owners (especially those who own many properties) upload their insurance policies, get automated reminders before each policy expires, and — when a renewal is approaching — receive three competing offers automatically
  - `e2` (source_body): Three personas — who uses RenewalOS and why each one exists... The Holder — our customer... The Provider — the broker... The Admin — us
  - `e3` (source_body): Think of it as a family tree: Grandfather = the main policy... Children = related policies... Grandchildren = endorsements — changes made to a policy mid-cycle
  - `e4` (source_body): The default is 90, 60, and 30 days before expiration... For MVP, only the 90-day reminder needs to be the one that fires the quote workflow.
  - `e5` (source_body): We're shipping it as Silver, Platinum, Gold... Silver is the floor, Gold is the prize... Silver: exact same coverage... Platinum: same coverage... lower premium... Gold: improves coverage and lowers the premium

## Provenance

- Source: `clickup_doc_page` `8cqnrff-19237/8cqnrff-25137`
- Source hash: `be47fb084a724c71e375c231689e6e46e490e5be61b4b010ec403754c493d09c`
- Observed at: 2026-10-17T00:41:15.148Z
- Agent run: `fa896ec0-c90e-4dcd-885e-5b089c8319d1`
- Validation run: `4d1df796-d4f7-4ccd-89da-e555ffe94f87`
