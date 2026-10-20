---
brain_note_id: "note:f6d5fa04-64d5-402d-8026-4c796213273f"
canonical_key: "google-drive-bridge-process"
brand_id: "trellis_core"
---
# Google Drive Bridge Process

## Canonical Statement

- **process**: The Google Drive Bridge system uses a two-part architecture (Control Plane via MCP for metadata/search, Data Plane via Google Drive for Desktop for byte transfer) to securely connect Google Drive assets to Trellis local workspaces.
- **rule**: All file transfers must pass verification gates (size, SHA-256, ffprobe for video) before being accepted into production, ensuring that existence in Drive does not imply successful transfer.
- **rule**: Brand isolation is enforced by restricting searches to authorized Drive roots per brand; cross-brand access is blocked.

## Evidence Log

- 2026-10-20T02:04:01.977Z — `clickup_doc_page:8cqnrff-23297/8cqnrff-35737`
  - `e1` (source_body): The Google Drive Bridge connects directly the files that the team has organized in Google Drive with the local project of Trellis Video Editor.
  - `e2` (source_body): Trellis does not trust only that “an file appeared”. Each transfer can verify: Google Drive identity + local real file + size + SHA-256 + ffprobe when it is video.
  - `e3` (source_body): One of the most important rules is: The files of one brand should not mix automatically with those of another. Trellis checks the authorized Drive roots before accepting a file.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-23297/8cqnrff-35737`
- Source hash: `f2b1308d3cbbea6cfd2e28bae5344d718ab4617ab415beebce201f9b0b34679d`
- Observed at: 2026-10-20T02:04:01.977Z
- Agent run: `b7ad504a-edab-44f2-b57a-7b1cb8218a89`
- Validation run: `2e5500ff-d359-4015-bde8-d3b5155d248e`
