---
brain_note_id: "note:43dcecfd-50ed-4753-9a22-9624bd5fbbf6"
canonical_key: "ghl-wallet-optimization-standard"
brand_id: "trellis_core"
---
# GoHighLevel Wallet Optimization Standard

## Canonical Statement

- **process**: To optimize GHL wallet costs, move email workflows from premium 'Inbound Webhook' triggers to 'Contact Tag' triggers. This avoids the $0.01 premium execution fee per email, reducing costs to the standard $0.000675 rate.
- **fact**: SMS templates should be kept to 160 characters or fewer, using plain ASCII characters (no emojis or special dashes), to ensure they bill as a single segment rather than multiple segments.
- **process**: Set GHL wallet auto-recharge to $50 to reduce the frequency of transactions while maintaining the same total spend.

## Evidence Log

- 2026-11-19T04:14:20.924Z — `clickup:86e409jk6#brand=trellis_core`
  - `e1` (source_body): Move the DR app emails off the Inbound Webhook trigger. ... GHL Conversations API: same LC Email, $0.000675 per email, no premium step.
  - `e2` (source_child): DR now writes the email data to the contact through the GHL API (free) and adds a tag; the tag starts the workflow.
  - `e3` (source_child): the app's automatic emails ... now start in GHL in a free way. Before, every one of those emails cost an extra $0.01 "premium" fee ... Now each email costs only the normal $0.0007.
  - `e4` (source_child): 160 characters max, including greeting... 27 contained a non-GSM character (21× "—", 8× "–", 4× "•", plus two emoji), which makes every segment 70 characters instead of 160.
  - `e5` (source_child): all 4 SMS were 2 segments (212–265 chars) = 8 segments per lead. Rewritten to 1 segment each, plain ASCII
  - `e6` (source_child): A4 done: auto-recharge raised from $10 to $50 (Agency Settings > Billing > Wallet & Recharge).

## Provenance

- Source: `clickup` `86e409jk6#brand=trellis_core`
- Source hash: `f775b7fb93e559a6c9c3f8baef6e4e8211048919b85dcdd6bd2c9b8e89763542`
- Observed at: 2026-11-19T04:14:20.924Z
- Agent run: `ac49b627-6ade-447d-88b0-1a951cb90941`
- Validation run: `5d15a7ea-50ee-463e-be9a-d214ddefaa89`
