---
brain_note_id: "note:f79f0888-4e21-4152-bcff-6c7d083a168e"
canonical_key: "proxy-metric-framework"
brand_id: "discipline_rift"
---
# Proxy Metric Selection and Validation Framework

## Canonical Statement

- **rule**: When selecting a proxy metric for ad optimization, evaluate candidates against four dimensions: correlation strength, timeliness, actionability, and stability over time.
- **rule**: To prevent optimizing for low-value activity, validate a proxy metric by calculating the ratio of proxy events to actual registrations and ensuring this ratio remains stable over time.

## Evidence Log

- 2026-10-20T02:07:08.278Z — `clickup_doc_page:8cqnrff-23377/8cqnrff-35037`
  - `e1` (source_body): A proxy optimization metric should be selected on four dimensions — correlation strength, timeliness, actionability, and stability over time.
  - `e2` (source_body): Do not select a proxy metric so far up the funnel that it permits the algorithm to prioritize low-value activity; validate a candidate proxy by calculating the ratio of proxy events to desired events and checking that the ratio holds over time.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-23377/8cqnrff-35037`
- Source hash: `b534bb3088c6a2d79d2d111f99ccd7cd2f47beb330ce7cde88da2b4a40229f54`
- Observed at: 2026-10-20T02:07:08.278Z
- Agent run: `47e7599f-4620-4aa9-9ca7-16435a726d8f`
- Validation run: `18d7ad7e-61f1-46e8-95cb-7f6105faeacb`
