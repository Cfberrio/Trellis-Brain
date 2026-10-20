---
brain_note_id: "note:ecc5c396-3934-4b53-ad92-4e1ac408053f"
canonical_key: "marketing-attribution-roas-structure"
brand_id: "discipline_rift"
---
# DR Marketing Attribution and ROAS Structure

## Canonical Statement

- **process**: Discipline Rift tracks marketing performance through a structured funnel: Meta Ad (UGC/Raw/Screens/Green/Spider) → /register → Register Started (DR Database) → CompleteRegistration (Pixel/CAPI) → InitiateCheckout (Pixel/CAPI) → Purchase (Pixel/CAPI/DB).
- **fact**: Attribution metrics (CPA, ROAS, Creative, GEO) are calculated by reconciling Meta Ads Manager data with actual payment and revenue data from the DR Database.

## Evidence Log

- 2026-10-20T18:11:33.581Z — `clickup_doc_page:8cqnrff-23377/8cqnrff-34997`
  - `e1` (source_body): META AD
UGC / RAW / SCREENS / GREEN / SPIDER
│
│ UTM + Meta IDs
▼
/register
│
▼
Register Started
[DR DATABASE]
│
▼
CompleteRegistration
[Pixel + CAPI]
│
▼
InitiateCheckout
[Pixel + CAPI]
│
▼
PAYMENT SUCCESS
│
▼
PURCHASE
[Pixel + CAPI + DB]

## Provenance

- Source: `clickup_doc_page` `8cqnrff-23377/8cqnrff-34997`
- Source hash: `a29106855b1e36bbb3c469243699cb59a2acb3f0f24fcfb55204ed2eef3b92ab`
- Observed at: 2026-10-20T18:11:33.581Z
- Agent run: `60f8dfa9-3d48-4ce4-9aa6-0a5ae8bd38f7`
- Validation run: `3cb6c366-f5d9-4263-a63c-feb5e2229f97`
