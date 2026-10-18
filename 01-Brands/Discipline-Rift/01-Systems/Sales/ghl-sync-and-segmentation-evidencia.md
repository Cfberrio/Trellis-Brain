---
brain_note_id: "note:57bd82a9-6266-4062-b7cd-b72d58c9f723"
canonical_key: "01-systems-sales-ghl-sync-and-segmentation-evidencia"
brand_id: "discipline_rift"
---
# GHL Sync and Segmentation — Evidencia

## Canonical Statement

- **fact**: GoHighLevel automatically tags registered parents with the season name in lowercase (e.g., 'fall 2026') upon payment.
- **process**: To exclude registered parents from marketing, use a GHL contact filter where 'Tag is not' the current season tag and save it as a Smart List.
- **rule**: Season tags are automatically removed by the system if a parent is refunded.
- **rule**: Marketing emails must be sent to the 'Marketing: Not Registered' Smart List rather than raw school tags to ensure registered parents are excluded.

## Evidence Log

- 2026-10-18T16:03:18.765Z — `clickup_doc_page:8cqnrff-25317/8cqnrff-38457`
  - `e1` (source_body): Every parent with a paid registration automatically gets a tag with the season name, in lowercase... The tag is removed automatically if the parent is refunded.
  - `e2` (source_body): Send marketing only to parents who are NOT registered... Add Tag is not 'winter 2026'... Save as Smart List, named Marketing: Not Registered (Winter 2026).

- 2026-10-18T16:04:14.500Z — `clickup_doc_page:8cqnrff-25337/8cqnrff-38477` (validation `4d0f32b3-8d8e-4391-bda2-c1ea6df8a4b5`)
  - `e1` (source_body): | {{contact.first_name}} | 1,055 (100%) | | {{contact.student_names}} | 1,047 (99%) | | {{contact.school_names}} | 1,041 (99%) | | {{contact.team_names}} | 1,041 (99%) |
  - `e2` (source_body): Parent emails → section 1 fields are filled only for paid parents, and not for all of them... For the other 1,717 contacts (newsletter, abandoned, imports) they're always blank.
  - `e3` (source_body): Team Names is in ALL CAPS. Season and Team Names include past seasons. They're history, not 'the current season'.
  - `e4` (source_body): School emails → section 3. Never put school fields in a parent email: they come out blank.
  - `e5` (source_body): Pick recipients with TAGS (section 5), not with fields.
- **rule**: Use specific GHL merge fields for parent emails: {{contact.first_name}} (100% fill), {{contact.student_names}} (99%), {{contact.school_names}} (99%), and {{contact.team_names}} (99%).
- **rule**: Parent-specific fields (student names, team names, etc.) are only filled for paid parents; they remain blank for newsletter, abandoned, or imported contacts.
- **fact**: The {{contact.team_names}} field in GHL is formatted in ALL CAPS and includes historical data from past seasons, not just the current one.
- **rule**: School-specific fields (e.g., {{contact.school_type}}, {{contact.county}}) must only be used in school outreach emails; they will be blank in parent emails.
- **process**: Segment email recipients using tags (e.g., 'dr', 'volleyball', 'fall 2026') rather than relying on dynamic fields for filtering.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-25317/8cqnrff-38457`
- Source hash: `17be6ca841f3f9bcdc24adecc793fa7c7e25fc8d079701e666873df13b43cc45`
- Observed at: 2026-10-18T16:03:18.765Z
- Decision: `6435c729-09a0-4da0-9744-cc1b2bf3e6a7`
- Upstream agent run: `bccf33bb-1f33-45f4-ac5e-c36d64a4e164`
- Validation run: `d0fc7ba7-cac8-43ed-b5ac-325fee038d2c`
