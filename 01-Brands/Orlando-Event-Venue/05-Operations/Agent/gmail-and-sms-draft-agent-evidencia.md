---
brain_note_id: "note:1cc68dd4-9d14-44ad-a707-a0823803222d"
canonical_key: "05-operations-agent-gmail-and-sms-draft-agent-evidencia"
brand_id: "orlando_event_venue"
---
# Gmail and SMS Draft Agent — Evidencia

## Canonical Statement

- **rule**: The Gmail tool 'gog' is restricted to read-only operations and creating draft replies; it is strictly forbidden from sending emails, modifying account settings, or deleting messages.
- **process**: Automated drafting for contact forms uses the query 'in:inbox newer_than:14d subject:"Contact Form -" -label:OEV_AUTODRAFTED -label:OEV_SKIPPED' and requires drafts to be created in-thread using the --reply-to-message-id flag.
- **process**: Processed threads must be marked with the label 'OEV_AUTODRAFTED' and have the 'UNREAD' label removed to ensure idempotency.
- **rule**: Human inquiries are filtered to exclude automated notifications (e.g., security alerts, OTPs, AI call recaps) and emails from specific domains like send.lcmsgsndr.com.

## Evidence Log

- 2026-10-15T00:49:23.322Z — `clickup_doc_page:8cqnrff-13217/8cqnrff-14077`
  - `e1` (source_body): Forbidden Actions: Send email (any command that transmits mail). Modify Gmail settings... Delete messages or empty trash.
  - `e2` (source_body): Q1 — Contact Forms (MUST STAY IN SAME THREAD). Query: in:inbox newer_than:14d subject:"Contact Form -" -label:OEV_AUTODRAFTED -label:OEV_SKIPPED. Create draft IN-THREAD: gog --no-input gmail drafts create --reply-to-message-id <MESSAGE_ID>
  - `e3` (source_body): Mark processed: gog --no-input gmail thread modify <THREAD_ID> --add OEV_AUTODRAFTED --remove UNREAD
  - `e4` (source_body): Q2 — Human inquiries (UNREAD-based). Query: ... -from:send.lcmsgsndr.com -subject:"AI Call Recap" -subject:"Security alert" -subject:"verification"

## Provenance

- Source: `clickup_doc_page` `8cqnrff-13217/8cqnrff-14077`
- Source hash: `151232a7bef60a476f451b5950d94ebb330d53255c8b4999f7193f61fa346dc0`
- Observed at: 2026-10-15T00:49:23.322Z
- Decision: `59b82920-efd8-4627-b5a9-2f69cf47489d`
- Upstream agent run: `52fdd64b-05c4-473f-9197-cabdb9b55c52`
- Validation run: `0c06bd61-6efb-4511-8e91-70ee5f38a5a3`
