---
brain_note_id: "note:45ea7e46-14fe-4819-a25e-8fcd0b0136b2"
canonical_key: "st-joseph-systems-data-sources"
brand_id: "st_joseph"
---
# St. Joseph Systems and Data Sources

## Canonical Statement

- **fact**: The St. Joseph email account currently uses Luis's parish account, with a planned transition to an Adult Formation address.
- **fact**: Data integration involves pulling Excel links from a shared OneDrive/SharePoint formation folder via authenticated browser sessions.
- **fact**: The system utilizes data from a live catechist Excel and OCIA master lists (including Candidate Form and retreat exports).
- **fact**: Mobile applications are managed via Apple Business Developer and Google Play accounts.
- **rule**: Credentials must be stored in the password manager and never in ClickUp.

## Evidence Log

- 2026-10-07T20:18:09.855Z — `clickup:86e3etj2r`
  - `e1` (source_body): St. Joseph email account: Luis's parish account exists and is the sending account for now (the parish is moving to an Adult Formation address)
  - `e2` (source_body): OneDrive / SharePoint shared formation folder: Luis sends the links to every Excel; Cristian pulls them with an authenticated browser session
  - `e3` (source_body): Live catechist Excel: received and imported
OCIA master list plus registration form exports: received and imported
  - `e4` (source_body): Apple business developer account + Google Play account (for the mobile apps)
  - `e5` (source_body): Credentials are kept in the password manager, never in ClickUp.

## Provenance

- Source: `clickup` `86e3etj2r`
- Source hash: `404679c993ac0a80084b9ed99509aa7f38c8475ae17e55a943064a4097438692`
- Observed at: 2026-10-07T20:18:09.855Z
- Agent run: `51b954d4-7e74-46ad-8368-3945e7b76066`
- Validation run: `d21cf388-f7c8-4df6-b711-7d91d6f69bb1`
