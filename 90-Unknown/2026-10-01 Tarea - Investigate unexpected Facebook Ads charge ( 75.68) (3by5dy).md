---
brain_note_id: "dest:unknown:3b3e124c33adc07fd9f292459b945971"
canonical_key: "unknown/3b3e124c33adc07fd9f292459b945971"
brand_id: "unknown"
---
# Tarea: Investigate unexpected Facebook Ads charge ($75.68)

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The document is a detailed financial audit and reconciliation task for Facebook Ads charges on a Chase Business card. While it mentions specific transaction dates and amounts, it contains no mention of Trellis brands, specific products, or venue names. It is a generic administrative/accounting task for a business entity that could be any of the brands or the parent company.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3by5dy` · [Abrir en ClickUp](https://app.clickup.com/t/86e3by5dy)

**Contenido original**

Objective
Conduct a full audit of our Facebook/Meta Ads account to determine why we're being charged when no ad sets are supposed to be live, and reconcile all historical charges to confirm Meta has billed us accurately.
Context
A charge of $75.68 from Facebook Advertising posted on Sep 18, 2026 (transaction date Sep 17, 2026) to the Chase Business card ending in 7111. We have no active ad sets launched, so this charge should not exist. We need to understand exactly where this money went and whether Meta has been overbilling us.

Screenshot of the transaction:

Spending Audit & Reconciliation
Phase 1: Identify the Source of the $75.68 Charge
Log into Meta Ads Manager and pull the full activity log for the week of Sep 14 - Sep 21, 2026
Check for any ad sets, campaigns, or ads that were active, scheduled, or in "learning" status during that period
Look at the Billing section in Meta Business Suite and match the $75.68 to a specific campaign/ad set
Check if there are any "automatic" rules or scheduled campaigns that could have auto-launched ads
Verify the payment activity tab: does Meta show the $75.68 charge on their end too, or is this a phantom bank charge?
Phase 2: Full Account Access & Security Audit
Pull a list of every user, partner, and app with access to our Meta Business account and ad account
Confirm no unauthorized users have been added or have ad-creation permissions
Check the ad account Activity History for any actions taken by users we don't recognize
Review connected apps/integrations that might have API access to create or enable ads
Check if there's a second ad account linked to the same payment method (card ending 7111)
Phase 3: Historical Spending Reconciliation (Chase Transactions → Meta Billing)
Use the attached Chase7111_Activity_20260921.csv as the source of truth for bank-side charges. You will NOT be getting separate bank statements. This downloaded transaction sheet is your reconciliation baseline.

All Facebook charges already extracted from the CSV (card 7111 only, 45 transactions, $1,802.16 total):

Full Facebook charge list from Chase data
Txn Date | Post Date | Description | Amount
09/17/2026 | 09/18/2026 | FACEBK *4H84K6S2Q4 | $75.68 ← THE CHARGE IN QUESTION
09/03/2026 | 09/04/2026 | FACEBK *MCE6A6E2Q4 | $100.00
09/03/2026 | 09/03/2026 | FACEBK *XGD226A2Q4 | $100.00
09/02/2026 | 09/03/2026 | FACEBK *52VPG423Q4 | $100.00
09/02/2026 | 09/02/2026 | FACEBK *VEL8G4S2Q4 | $100.00
09/01/2026 | 09/02/2026 | FACEBK *C4T4B423Q4 | $100.00
09/01/2026 | 09/02/2026 | FACEBK *8K6YE522Q4 | $100.00
09/01/2026 | 09/01/2026 | FACEBK *TBRN9423Q4 | $96.00
08/31/2026 | 09/01/2026 | FACEBK *EAUPD4N2Q4 | $96.00
08/28/2026 | 08/30/2026 | FACEBK *492SW362Q4 | $83.00
08/28/2026 | 08/28/2026 | FACEBK *SPU9U422Q4 | $83.00
08/27/2026 | 08/28/2026 | FACEBK *BKN7Z3W2Q4 | $71.00
08/26/2026 | 08/27/2026 | FACEBK *PM63P3S2Q4 | $66.00
08/26/2026 | 08/27/2026 | FACEBK *UR7YM422Q4 | $60.00
08/26/2026 | 08/26/2026 | FACEBK *3DY4H323Q4 | $59.00
08/25/2026 | 08/26/2026 | FACEBK *FM9DK362Q4 | $59.00
08/21/2026 | 08/23/2026 | FACEBK *VB2B3362Q4 | $35.00
08/21/2026 | 08/23/2026 | FACEBK *3U2Q23S2Q4 | $33.00
08/21/2026 | 08/23/2026 | FACEBK *G7NY93W2Q4 | $33.00
08/21/2026 | 08/23/2026 | FACEBK *WESL2362Q4 | $28.00
08/21/2026 | 08/21/2026 | FACEBK *A4TKL4E2Q4 | $27.00
08/20/2026 | 08/21/2026 | FACEBK *H5L8Z262Q4 | $31.00
08/20/2026 | 08/21/2026 | FACEBK *QMUCJ4E2Q4 | $18.68
08/20/2026 | 08/21/2026 | FACEBK *EZPCV223Q4 | $14.00
08/20/2026 | 08/21/2026 | FACEBK *WVNZY322Q4 | $11.00
08/20/2026 | 08/21/2026 | FACEBK *LEHYV223Q4 | $11.00
08/20/2026 | 08/21/2026 | FACEBK *DLE483W2Q4 | $11.00
08/20/2026 | 08/21/2026 | FACEBK *4NUPV223Q4 | $10.00
08/20/2026 | 08/21/2026 | FACEBK *X3VGY262Q4 | $10.00
08/20/2026 | 08/21/2026 | FACEBK *VLRW73W2Q4 | $10.00
08/20/2026 | 08/21/2026 | FACEBK *W4ST73W2Q4 | $10.00
08/20/2026 | 08/21/2026 | FACEBK *DB64Y2S2Q4 | $10.00
08/20/2026 | 08/21/2026 | FACEBK *TM3523N2Q4 | $9.00
08/19/2026 | 08/20/2026 | FACEBK *N3KTU2S2Q4 | $14.00
08/19/2026 | 08/20/2026 | FACEBK *AECUW2N2Q4 | $14.00
08/19/2026 | 08/20/2026 | FACEBK *B9CMD4E2Q4 | $14.00
08/19/2026 | 08/20/2026 | FACEBK *3KKQW2N2Q4 | $13.00
08/19/2026 | 08/20/2026 | FACEBK *XUQW34J2Q4 | $12.85
08/19/2026 | 08/20/2026 | FACEBK *EY5HW2N2Q4 | $12.00
08/19/2026 | 08/20/2026 | FACEBK *BKGLF4E2Q4 | $12.00
08/19/2026 | 08/20/2026 | FACEBK *SGY434J2Q4 | $12.00
08/19/2026 | 08/20/2026 | FACEBK *D9PN34J2Q4 | $10.00
08/19/2026 | 08/20/2026 | FACEBK *JXUWT322Q4 | $9.95
08/19/2026 | 08/20/2026 | FACEBK *T5VQT2S2Q4 | $9.00
08/19/2026 | 08/20/2026 | FACEBK *DAJXE4E2Q4 | $9.00

Steps:
Open Meta Ads Manager → Billing section and export all billing receipts/invoices for Aug 19 – Sep 21, 2026 (the date range covered by the Chase data)
For every FACEBK charge in the table above, find the matching Meta invoice/receipt. Match by date and amount
Build a reconciliation spreadsheet with columns: Chase Txn Date | Chase Amount | FACEBK Ref Code | Meta Invoice Date | Meta Invoice Amount | Match (Y/N) | Notes
Flag any charges that appear on Chase but NOT in Meta's billing (phantom charges)
Flag any charges that appear in Meta's billing but NOT on Chase (missing from bank)
Flag any amount mismatches between the two sides
Total up: Chase says $1,802.16 across 45 Facebook charges. Does Meta's billing say the same?
Phase 4: Campaign Performance vs. Spend Verification
For any past campaigns that did run, compare the reported spend in Ads Manager to the actual amounts billed
Check if Meta charged for impressions/clicks that seem inflated or outside our targeting parameters
Look at the breakdown of spend by day for any campaigns, and see if there are spend spikes that don't align with our budget caps
Verify that daily/lifetime budget limits were respected on every campaign
Phase 5: Resolution & Documentation
If the $75.68 (or any other charge) is unauthorized or inaccurate:
File a dispute directly through Meta's Billing Support
Screenshot everything before filing
Flag the charge on our Chase Business card as potentially fraudulent
If Meta has been overbilling us on past campaigns, document the total overcharge amount
Compile a final report with: total amount charged, total amount verified as legitimate, total discrepancy, and recommended next steps
If everything checks out, document that too so we have a clean paper trail
To Keep in Mind
Meta is notorious for opaque billing. Don't take their dashboard numbers at face value: always verify against the bank
Check for "pending" charges vs. "posted" charges. Sometimes Meta authorizes amounts and then adjusts them
Look for small recurring charges that might fly under the radar (subscription fees, verification fees, etc.)
If you find the ad account is clean, check whether another Meta product (like a boosted post from the Facebook page itself) could have triggered the charge
Export/screenshot everything as you go. If we need to dispute, we want receipts
Time-sensitive: if this is unauthorized, we want to flag it with Chase within 60 days of the transaction

**Comentarios**

- **2026-09-21 · Luis Torres**: @Brain Take the reconciliation to actual charges to the transactions. Actually, let me print this report. I'll print the report based on transactions on the card. He won't be getting statements. He will just be getting a downloaded sheet of all transactions made. Chase7111_Activity_20260921.csv
- **2026-09-22 · Luis Torres**: Hermano, no veo nada aquí. Simplemente veo que lo que pasa es que está realizado @Cristian Berrío
- **2026-09-22 · Cristian Berrío**: O sea en pocas palabras no se realizó ningún cobro raro, lo de los 70 y pico de dólares, era el remaining balance de cuando se corrieron los ads.
- **2026-09-22 · Cristian Berrío**: https://t9017418223.p.clickup-attachments.com/t9017418223/62d754ee-bc48-4411-96f1-f0cbff3b6f00/62d754ee-bc48-4411-96f1-f0cbff3b6f00.webm?filename=Explicaci%C3%B3n+cobros+Meta+ads.webm&open=true
- **2026-09-22 · Cristian Berrío**: mala mia no se habia subido el video
- **2026-09-22 · Luis Torres**: Recibido hermano, gracias por el video
- **2026-09-22 · Luis Torres**: Hermano, una pregunta: ¿hiciste la reconciliación entre lo que nos ha cobrado Meta Ads y el Excel que te mandé con lo que nos ha cobrado en la tarjeta? Hay una parte en este task donde hablamos de hacer una auditoría y reconciliación a los gastos y lo que nos terminaron cobrando

_Sincronizado por Brain: 2026-10-01T03:15:59.648Z_
