---
brain_note_id: "note:27fd7dc3-bb85-4a36-97cb-fad6d8a3bb24"
canonical_key: "04-training-call-communication-approach-evidencia"
brand_id: "orlando_event_venue"
---
# Call Communication Approach — Evidencia

## Canonical Statement

- **process**: The OEV AI agent handles all unanswered calls to collect the caller's name, email, phone number, and preferred event date. It does not schedule tours or check availability. After collection, it sends the OEV booking website via SMS and ends the call.
- **process**: For missed calls where no conversation occurs, an immediate SMS (M01) is sent within 60 seconds asking for the preferred event date. A follow-up (M02) is sent after 20 minutes if there is no reply, after which communication stops.

## Evidence Log

- 2026-10-22T01:44:53.242Z — `clickup_doc_page:8cqnrff-4977/8cqnrff-31557`
  - `e1` (source_body): The AI agent does not check availability, schedule tours, offer appointment times, or explain the tour process. Its only job is to collect the caller’s information and preferred event date, send the Orlando Event Venue website, and end the call.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-4977/8cqnrff-31557`
- Source hash: `5edbdbb9d712b615524b24c053b154feffd7439f90b59dbfe59145aab1733613`
- Observed at: 2026-10-22T01:44:53.242Z
- Decision: `d323f3ca-7be7-46ef-93e4-98096e1c8b9f`
- Upstream agent run: `bb21d6b2-67a8-4ef9-8241-61fd5a098fe8`
- Validation run: `aae8de03-32b1-440c-8587-8ee88ae06d7b`
