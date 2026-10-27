---
brain_note_id: "note:dc9635cd-9db5-414a-a22b-bb79d334c9e8"
canonical_key: "dr-ghl-dynamic-fields-process"
brand_id: "discipline_rift"
---
# DR GHL Dynamic Fields Process

## Canonical Statement

- **process**: Dynamic fields in GHL are placeholders that automatically populate with contact-specific information (e.g., student names, school names) from the DR app sync.
- **rule**: Always use double curly braces ({{contact.field_name}}) for GHL merge fields; single braces are reserved for the Admin Dashboard and will not work in GHL.
- **rule**: If a dynamic field has no value for a contact, it renders as a blank space; write sentences to remain readable if the field is empty.
- **rule**: SMS fields (e.g., {{contact.sms_parent}}) are not filled automatically and must be manually populated for specific campaigns before use.

## Evidence Log

- 2026-10-27T18:46:50.339Z — `clickup_doc_page:8cqnrff-25337/8cqnrff-39637`
  - `e1` (source_body): A dynamic field is a placeholder you put in an email or text. When the message goes out, GoHighLevel (GHL) replaces it with each person's own information. ... If the contact has no value, the code turns into nothing. ... Always do a test send.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-25337/8cqnrff-39637`
- Source hash: `a93f1be9c9f7e1f644460c92af516395b248d3e2b91af60f91698d3334c5262c`
- Observed at: 2026-10-27T18:46:50.339Z
- Agent run: `b907eaeb-a6ae-4585-b14d-3674f38ab470`
- Validation run: `827edcfe-8a30-4439-8532-44e5b05819e4`
