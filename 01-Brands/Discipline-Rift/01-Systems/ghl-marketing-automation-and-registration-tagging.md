---
brain_note_id: "note:9c3ee73f-aef8-42d2-b541-aa36b1270259"
canonical_key: "ghl-marketing-registration-tagging"
brand_id: "discipline_rift"
---
# GHL Marketing Automation and Registration Tagging

## Canonical Statement

- **process**: Parents with a paid registration automatically receive a GHL tag matching the season name in lowercase (e.g., 'fall 2026').
- **rule**: Marketing emails must be sent to a 'Marketing: Not Registered' Smart List that uses a 'Tag is not [current season]' filter to exclude already registered parents.
- **process**: The registration tag is added upon payment, re-checked twice daily, and removed automatically if a refund is processed.
- **rule**: A parent with multiple children is treated as a single contact; if any child is registered, the parent receives the exclusion tag.

## Evidence Log

- 2026-10-06T16:09:39.373Z — `clickup:86e3k1b3r`
  - `e1` (source_body): The problem: our marketing emails go to unregistered parents, which is what we want, but they also go to parents who already registered for this season. There's no tag that marks "registered this season," so there's nothing to exclude.
  - `e2` (source_child): Every parent with a paid registration automatically gets a tag with the season name, in lowercase... The tag is added the moment they pay, re-checked twice a day, and removed if they get refunded. A parent with 2 kids is 1 contact.

## Provenance

- Source: `clickup` `86e3k1b3r`
- Source hash: `bd987fb18fc7c85d8c4cced2c7fb447899d6912e5900635e791e1075a079930b`
- Observed at: 2026-10-06T16:09:39.373Z
- Agent run: `69b323db-4dea-4a86-922f-dbe06b19ebe1`
- Validation run: `138c7d75-c94d-443a-af31-96d830baa0c9`
