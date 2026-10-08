---
brain_note_id: "note:e6e61545-6eab-49f1-a354-9b24d9656acd"
canonical_key: "ocia-candidate-list-management"
brand_id: "st_joseph"
---
# OCIA Candidate List Management and Inline Editing

## Canonical Statement

- **process**: Staff can update OCIA candidate contact status (Not contacted, Contacted, Scheduled, Interviewed) and add notes directly from the admin candidates list (/admin/ocia-candidates) without opening individual profiles.
- **rule**: Notes edited inline on the candidates list are synchronized with the candidate profile; they include a timestamp and author attribution.
- **rule**: Changing a status to 'Interviewed' via the inline list only updates the status; specific interview metadata like date and interviewer must still be entered on the full profile to ensure accuracy.

## Evidence Log

- 2026-10-07T20:15:07.236Z — `clickup:86e3j6va7`
  - `e1` (source_body): Let staff update a candidate's contact/interview status and add notes directly from the Adults receiving sacraments (OCIA candidates) list... Status: make the Interview badge a clickable inline dropdown... Notes: add a Notes column or a small note icon per row that opens an inline popover.
  - `e2` (source_child): Contact status: the column (formerly "Interview") is now a button... Notes: new column showing each person's latest note... Choosing "Interviewed" only changes the status. The interview date and interviewer are still entered on the profile.

## Provenance

- Source: `clickup` `86e3j6va7`
- Source hash: `a469a644c5898ed3a62c60d44ce975f1633aecfffbdbdb698f805a3c9b8de20d`
- Observed at: 2026-10-07T20:15:07.236Z
- Agent run: `38713449-1190-4a5f-a9c7-9b68604fc388`
- Validation run: `04108f56-2127-4cec-84ff-a9575d487c95`
