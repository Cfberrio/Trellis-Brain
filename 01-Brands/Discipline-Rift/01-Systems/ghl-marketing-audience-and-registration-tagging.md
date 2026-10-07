---
brain_note_id: "note:9f46615c-bce3-46bf-a054-d33983ca0fa5"
canonical_key: "ghl-marketing-audience-tagging"
brand_id: "discipline_rift"
---
# GHL Marketing Audience and Registration Tagging

## Canonical Statement

- **process**: Parents with a paid registration in GoHighLevel automatically receive a season-specific tag (e.g., 'fall 2026', 'winter 2026') the moment they pay.
- **rule**: Marketing emails must be sent to a 'Marketing: Not Registered' Smart List that uses a 'Tag is not [current season]' filter to exclude already registered parents.
- **fact**: Registration tags in GoHighLevel are re-checked twice daily and are automatically removed if a parent receives a refund.
- **process**: When a new season opens, the marketing audience is updated by duplicating the existing Smart List and swapping the exclusion tag for the new season's label.

## Evidence Log

- 2026-10-07T15:08:58.776Z — `clickup:86e3k1b3r`
  - `e1` (source_body): The problem: our marketing emails go to unregistered parents, which is what we want, but they also go to parents who already registered for this season. There's no tag that marks "registered this season," so there's nothing to exclude.
  - `e2` (source_child): Every parent with a paid registration automatically gets a tag with the season name, in lowercase... The tag is added the moment they pay, re-checked twice a day, and removed if they get refunded.

## Provenance

- Source: `clickup` `86e3k1b3r`
- Source hash: `f11087ad9fef2fba3ac2bd51c8324e1356c6ea5889aa39079d0d5b96646acc6c`
- Observed at: 2026-10-07T15:08:58.776Z
- Agent run: `e299a240-39e2-4143-b829-d11ed24152df`
- Validation run: `78d848c7-496a-476d-9a46-a5956df5c94e`
