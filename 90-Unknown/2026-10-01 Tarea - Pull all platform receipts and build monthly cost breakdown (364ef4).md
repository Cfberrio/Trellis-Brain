---
brain_note_id: "dest:unknown:d9a030c0f27d903d9d3b4e8adb3ea4ae"
canonical_key: "unknown/d9a030c0f27d903d9d3b4e8adb3ea4ae"
brand_id: "unknown"
---
# Tarea: Pull all platform receipts and build monthly cost breakdown

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: Habla de varias marcas (`MULTI_BRAND`)
- reason: `The task involves a centralized billing audit for the entire Trellis ecosystem. The data explicitly mentions grouping costs by 'DR' (Discipline Rift) and 'OEV' (Orlando Event Venue), and covers infrastructure used across all brands like GHL, OpenAI, and hosting.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e364ef4` · [Abrir en ClickUp](https://app.clickup.com/t/86e364ef4)

**Contenido original**

Objective
Manually pull receipts and billing data from every platform we use, and consolidate them into a clear monthly cost breakdown so we can see exactly what we're spending and where.
Context
This comes directly from the results of the . Cris concluded that automating a centralized dashboard is too complex right now: each platform exposes billing info differently, and the dev effort to normalize it all wouldn't be worth it. Instead, the right approach is a monthly manual process: pull reports/screenshots from each platform's billing page, consolidate and compare month-over-month, and document the summary in ClickUp.

Cris is the right person for this because (1) this process can't be automated right now, and (2) he's the best person to spot anomalies and know how to fix something if we're spending more than usual.

Platforms to cover: GHL, Composio, OpenAI, Lovable, Apify, Higgsfield, hosting, domains, and any other recurring tools or APIs we're using.
To Keep in Mind
For each platform, extract the receipt, invoice, or billing history for the current month
Consolidate into a single document: platform name, monthly cost, month-over-month change, and any flags for unusual increases
Use ChatGPT to help categorize and compare if needed (as Cris suggested in his analysis)
Group costs by brand (DR, OEV, etc.) and by tool category where possible
Action item A: Downgrade our GHL account. Move us to a lower-tier plan.
Action item B: Dispute the $300 GHL charge. We were not satisfied with the results of upgrading our account and we consider it was not worth it. File the dispute claiming dissatisfaction with the upgrade results.

**Comentarios**

- **2026-09-09 · Cristian Berrío**: September_2026_Software_AI_Usage_Report.md
- **2026-09-09 · Cristian Berrío**: @Luis Torres si le damos downgrade volvemos a pasar a 3 subaccount maximo para que sepas, entonces necesito que me confirmes antes de mandar eso
- **2026-09-14 · Cristian Berrío**: Done, les envie el mensaje, he hice el downgrade
- **2026-09-17 · Luis Torres**: hermano, manda el ticket pidiendole a GHL un refund. create una buena historia para que no no los niegen gastamos mas dinero de lo que deberiamos @Cristian Berrío
- **2026-09-17 · Luis Torres**: t9017418223.p.clickup-attachments.com/t9017418223/d2f50668-45a3-4cf8-ab24-3e2478e08e98/September_2026_Software_AI_Usage_Report.md la proxima necesigamos incluir clickup higgsfield google ai pro plan google tokens apify whatever else we sue go high level everythign anthropic everything @Brain create a subtask on here 86e38f4fa to calculate monthly cost of everything a full brreakdown and recommentations for savinss
- **2026-09-17 · Luis Torres**: orlandoeventvenue.org/ Figure out a way. To make our 3D horse better for Orlando Event Venue, right now it really sucks. We need to put the new pictures in there and make sure that they are placed first because the other pictures are trash. Unless you decide to put the other pic to fix the welcome area pictures and all those pictures as well, do not put them in front. Put them later. Just make sure the structure of the event tour page is strategic. The 3D tour needs to be strategic. @Brain create subtask
- **2026-09-17 · Cristian Berrío**: Screenshot 2026-09-17 at 1.37.36 PM.png

_Sincronizado por Brain: 2026-10-01T03:09:11.428Z_
