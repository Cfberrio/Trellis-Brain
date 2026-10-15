---
brain_note_id: "note:5d60b1a3-5be6-457e-abd6-676a0a50b183"
canonical_key: "ai-investing-research-system-standard"
brand_id: "trellis_core"
---
# AI Investing Research System - Implementation Standard

## Canonical Statement

- **decision**: The system resolves two distinct decisions: 1. Vehicle Selection (comparing products following the exact same index using Cost, Performance, Risk, Access, Scale, and Evidence Quality) and 2. Exposure Selection (organizing other indices into Exposure Families within a Market Map).
- **rule**: When SEC XBRL filings contain internal contradictions (e.g., returns attributed to the wrong share class), the system must mark the data as a conflict and exclude it from comparisons to prevent contamination.
- **process**: To ensure accurate comparisons across different issuers, the system uses official CUSIP identifiers to validate holdings and identity rather than relying on inconsistent naming conventions.
- **fact**: The system successfully completed a census of over 1,700 market indices with 96% precision, identifying candidates without manual lists.

## Evidence Log

- 2026-10-07T15:11:26.956Z — `clickup:86e3kmpef`
  - `e1` (source_body): a personal, Claude-assisted research system with two separate tracks. Track 1 Funds (ETFs first... Track 2 US-listed stocks has two analysts that never share a score... First deliverable is the ETF pilot: 8–12 plain, unlevered ETFs in 3 peer bins
  - `e2` (source_body): What it is NOT: a trading bot. No broker connections... Research output is never authorization to trade. Permission ladder: research only → read-only → monitoring → paper → human-approved live. Only step 1 is authorized today.
  - `e3` (source_child): Hermano, propuesta aprobada. Mueve hacia adelante la implementación.

## Provenance

- Source: `clickup` `86e3kmpef`
- Source hash: `1f7475d4806dad62d55ce0149ccad40de8b79b2b547e987b1e12d8daea5b9b04`
- Observed at: 2026-10-07T15:11:26.956Z
- Agent run: `e9008f32-77ef-4ae7-9b76-3d11f5f1dfe2`
- Validation run: `a253e4ba-940f-43b2-8e46-18fed3c8ad11`
