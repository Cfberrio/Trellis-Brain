---
brain_note_id: "note:a7fed4c2-8bfc-4aac-9ca0-bb30761d2249"
canonical_key: "ai-agent-operating-standard"
brand_id: "trellis_core"
---
# AI-Agent-Operating-Standard

## Canonical Statement

- **rule**: The 8-rule agent standard for AI-driven system interactions: (1) dangerous actions (send, delete, pay, change permissions) are not tools; (2) if a dangerous action is required, it must be confirmed by a human in code; (3) step and spend limits must be tuned with data; (4) reserve the message before acting to prevent duplicate runs; (5) only load data required for the specific case; (6) host tools only on calls that need them; (7) keep keys out of agent reach; (8) maintain a trace of every step with secrets removed and test scenarios before model changes.

## Evidence Log

- 2026-11-18T04:21:55.142Z — `clickup_doc_page:8cqnrff-27397/8cqnrff-40757`
  - `e1` (source_body): The 8-rule agent standard (ESTANDAR-AGENTES.md), in short, the model asks and our code executes: (1) dangerous actions (send, delete, pay, change permissions) are not tools; (2) if one is needed, it runs only when a person's yes comes back in code; (3) a step and spend limit tuned with data; (4) reserve the message before acting, so two runs never do the same thing twice; (5) only the data each case needs; (6) hosted tools only on the calls that need them; (7) keys out of the agent's reach; (8) a trace of every step, with secrets removed, and test scenarios before every prompt or model change.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-27397/8cqnrff-40757`
- Source hash: `4f5587bb4b0756f5ed5bc5850326361f57afdcdddc27117f567099aee1f328e1`
- Observed at: 2026-11-18T04:21:55.142Z
- Agent run: `a40cacf2-4593-479d-87e8-49e2eb11ba33`
- Validation run: `b54d5e56-c3b6-49b9-b6f8-f46ac744098b`
