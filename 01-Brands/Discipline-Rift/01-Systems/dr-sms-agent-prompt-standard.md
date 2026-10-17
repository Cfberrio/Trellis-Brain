---
brain_note_id: "note:5aa0e728-65f2-4646-be58-23755cae12b1"
canonical_key: "dr-sms-agent-prompt-standard"
brand_id: "discipline_rift"
---
# DR SMS Agent Prompt Standard

## Canonical Statement

- **rule**: SMS operators must use a specific decision logic: 'draft' for safe replies, 'skip' for spam/opt-outs, and 'flag_human' for complaints, refunds, injuries, or legal threats.
- **rule**: SMS drafts should be energetic, clear, and trustworthy, avoiding emojis unless the inbound user uses them first, with a maximum length of ~320 characters.
- **rule**: Operators must never auto-confirm registrations or payments, never quote specific prices unless confirmed in context, and must match the inbound language (e.g., Spanish).
- **process**: SMS drafts are scored on a 0.0-1.0 rubric: 0.85+ for common questions with clear context; 0.65-0.85 for reasonable drafts with minor assumptions; <0.40 requires flagging for human review.

## Evidence Log

- 2026-10-17T22:38:24.977Z — `clickup_doc_page:8cqnrff-18177/8cqnrff-20517#brand=discipline_rift`
  - `e1` (source_body): decision: draft | skip | flag_human... flag_human: message contains a complaint, refund request, injury, legal threat, or anything emotionally charged. Do NOT draft a reply.
  - `e2` (source_body): No emojis unless the inbound used them first. Short sentences. Mobile-readable. Max ~320 chars per draft unless the question genuinely needs more.
  - `e3` (source_body): Never auto-confirm a registration, payment, or booking... Never quote a specific price unless the contact_context includes a confirmed price. If the inbound is in Spanish, respond in Spanish.
  - `e4` (source_body): Scoring rubric: 0.85+ : Common question... 0.65–0.85 : Reasonable draft but some assumption made... < 0.40 : Don't trust the draft. Set decision to flag_human instead.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-18177/8cqnrff-20517#brand=discipline_rift`
- Source hash: `1f6f5eca6ab5ff43260f3b52326c57becd3004a7211a10855dd04a2cc705df7c`
- Observed at: 2026-10-17T22:38:24.977Z
- Agent run: `090ebf0d-cefc-4f81-97a8-895ccc94ab3f`
- Validation run: `277de515-a7cf-4d0f-839e-a0e3f5c98387`
