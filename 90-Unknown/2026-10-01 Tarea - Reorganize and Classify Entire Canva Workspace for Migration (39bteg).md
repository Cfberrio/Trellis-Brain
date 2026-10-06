---
brain_note_id: "dest:unknown:6feb587a212c8c3b95d54cb59ca97223"
canonical_key: "unknown/6feb587a212c8c3b95d54cb59ca97223"
brand_id: "unknown"
---
# Tarea: Reorganize and Classify Entire Canva Workspace for Migration

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: Habla de varias marcas (`MULTI_BRAND`)
- reason: `The document is a comprehensive migration and reorganization plan for a Canva workspace that explicitly covers all Trellis brands (Cheese To Share, Discipline Rift, Orlando Event Venue, and Trellis Fields/Core). It provides specific folder structures and naming conventions for each brand individually.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e39bteg` · [Abrir en ClickUp](https://app.clickup.com/t/86e39bteg)

**Contenido original**

Objective
Organize the complete Canva workspace so every design and asset has an identifiable brand, purpose, and future migration destination. This is split into two passes: Pass 1 (Organization) happens entirely inside Canva, Pass 2 (Migration Classification) determines how each file gets exported.

Context
The current Canva workspace has several competing systems: folders like PRINTS, VENUE, TRELLIS, DR, CTS, DIRECCIÓN, Luis, plus loose recent designs and uploads. Top-level folders organized by format (flyers, social, print) create confusion because a Discipline Rift flyer ends up in a company-wide PRINTS folder alongside CTS and OEV work.

The fix: reorganize around ownership first: brand → purpose → project/campaign.
New Master Structure
00 — INBOX / TO SORT

01 — TRELLIS FIELDS
    01 Brand System
    02 Templates
    03 Marketing & Social
    04 Sales & Presentations
    05 Internal
    06 Recruiting
    90 Archive

02 — DISCIPLINE RIFT
    01 Brand System
    02 Templates
    03 Registrations & Campaigns
    04 Schools
    05 Sports
    06 Parent Communications
    07 Coach / Operations
    08 Print
    09 Social Media
    90 Archive

03 — CHEESE TO SHARE
    01 Brand System
    02 Templates
    03 Catering
    04 Menus
    05 Events
    06 Marketing & Social
    07 Print
    90 Archive

04 — ORLANDO EVENT VENUE
    01 Brand System
    02 Templates
    03 Venue Marketing
    04 Ads
    05 Packages & Pricing
    06 Events
    07 Print
    90 Archive

05 — RELIABLE / TRUSTED VENUES
    01 Brand System
    02 Templates
    03 Marketing
    04 Sales
    90 Archive

06 — IMPULSA
    01 Brand System
    02 Templates
    03 Marketing
    90 Archive

07 — LUIS TORRES
    01 Personal Brand
    02 Presentations
    03 Social
    04 Projects
    90 Archive

08 — CLIENT / COMMUNITY MANAGEMENT
    [Client Name]
        01 Brand
        02 Social
        03 Ads
        04 Campaigns
        90 Archive

98 — SHARED ASSETS
    Logos
    Photos
    Video
    Icons
    Backgrounds
    Fonts & Typography References
    Reusable Trellis Assets

99 — LEGACY ARCHIVE
Naming Convention
Rename important designs to be searchable using this format:

[BRAND] — [PROJECT] — [ASSET] — [VARIANT]

Examples:
DR — Fall 2026 — Volleyball Registration Flyer — Print
DR — Fall 2026 — Tennis Registration Flyer — Print
DR — Windermere — Volleyball Registration — IG Feed
CTS — Baby Shower — Catering Menu
OEV — Venue Rental — Birthday Ad — Meta 01
TF — Recruiting — Video Editor Job Post
LT — Never Alone — Presentation

Dates go in the filename only when actually relevant.

To Keep in Mind
Pass 1: Organization (inside Canva)
For every item in the workspace:

1. Identify the brand:
Trellis Fields
Discipline Rift
Cheese To Share
Orlando Event Venue
Reliable / Trusted Venues
Impulsa
Luis Torres
Client / Community Management
Shared Asset
Unknown → Inbox

2. Determine what the file actually is:
Brand asset, reusable template, campaign, social post, advertisement, flyer/print, presentation, internal document, event asset, photograph/video/upload, old/unused material

3. Move it into the new folder structure.
Do NOT organize primarily by format (flyer / Instagram / print / image / video) at the highest level
First ask: Whose file is this? Then: What is it used for?

4. Rename important designs using the naming convention above.

5. 00 — INBOX / TO SORT rule: Anything you cannot confidently identify goes here. Do not guess. Luis or Moche will review that folder later.

6. DO NOT DELETE DUPLICATES. Move and classify only. If you see five nearly identical files, group them together in the correct brand/project folder. Deletion happens after migration and backup, not during cleanup.
Pass 2: Migration Classification
Once everything is organized, go folder by folder and classify each design:

Classification Meaning Export Format
A — ACTIVE / EDITABLE Currently in use SVG/PPTX + visual backup
B — TEMPLATE Reusable Figma + SVG/source
C — ARCHIVE Historical PDF/PNG
D — ORIGINAL ASSET Source image/video Original file
E — DELETE LATER / DUPLICATE Redundant Preserve until migration verifiedMigration Tracker
Maintain a tracker sheet with these columns:

Brand Canva Folder Design Category Active? Reusable? Export Format Migrated Reviewed
DR Fall 2026 Volleyball Flyer Print Yes Yes SVG + PNG ☐ ☐
CTS Catering Baby Shower Menu Sales Yes Yes SVG + PDF ☐ ☐
OEV Ads Wedding Ad 03 Meta Ad No No PNG ☐ ☐
This becomes the audit trail proving Canva can safely be canceled.
First Session Priorities
Create the new top-level folder structure
Create 00 — INBOX / TO SORT
Reconcile existing DR, CTS, TRELLIS, VENUE, Luis, etc. folders with the new brand structure
Start moving loose designs from Recents/Projects into the appropriate brand
Break up generic folders like PRINTS and move each item into the brand it belongs to
Separate uploads/original assets from finished designs
Keep anything ambiguous in Inbox
Do not delete anything
Track progress in the migration sheet

Finish the full organizational pass before doing the mass migration. Otherwise you permanently inherit the current Canva disorder into Figma/Drive.

Source comment with full details: comment:90170252132743

**Comentarios**

- **2026-09-15 · Cristian Berrío**: Pase 1 (organización) hecho — 313 ítems inventariados, 64 carpetas creadas, 196 moves sin fallos. Status → ejecutando. Qué pasa: raíz de Canva limpia; estructura brand→purpose del spec creada completa; todo diseño/asset movido a su marca o a 00 — INBOX / TO SORT (90 ítems: 43 imágenes sin nombre, 40 diseños sin título, 7 PDFs personales). Tracker con clasificación A–E, export format y nombre propuesto: Canva Migration Tracker (Sheet). Decidí: mover carpetas legacy enteras (CERTIFICADOS, PLANTILLAS CONTENIDO, COMMUNITY M., DIRECCIÓN…) en vez de ítem por ítem — preserva agrupación interna, 1/20 del costo. Sub-niveles se refinan en Pase 2 (marcados en el tracker). Riesgo: (1) 6 docs personales (W2, paystub, Remitly, HelloSign) viven en el Canva de empresa — recomiendo sacarlos, no migrarlos. (2) Las carpetas nuevas se crearon bajo mi usuario vía MCP; falta verificar que Luis ve 01–99 o compartirlas con el Team. Pendiente manual (el MCP no borra ni renombra carpetas): eliminar 6 cascarones vacíos en raíz (DR, CTS, TRELLIS, VENUE, Luis, PRINTS) + quitar de raíz 2 diseños con doble membresía. Siguiente paso: Luis revisa INBOX en el Sheet (columna Brand) · Cristian ejecuta renombrado masivo (137 diseños con nombre propuesto) tras aprobación · Pase 2: clasificación de export por carpeta. Tiempo: 40 min (15-sep 14:37–15:15).
- **2026-09-16 · Luis Torres**: Categorización correcta. Todos los pagos que están en uploads se quedan en Canva, no se vuelven a extraer. Procede a la extracción, luz verde @Cristian Berrío
- **2026-09-16 · Luis Torres**: image.png @Brain Have @Cristian Berrío understand to not dump files in our Google Drive folder. They need to be organized somewhere appropriately.
- **2026-09-18 · Cristian Berrío**: Hecho: 155 diseños exportados de Canva y ubicados en Drive. 242 archivos en total. Qué hice: Creé la estructura CANVA dentro de cada raíz de marca en Drive (TF, DR, CTS, RV, LT, OEV, IMPULSA), con las mismas subcarpetas del tracker (01 Brand System, 02 Templates, 03 Marketing, etc.). Exporté por API todo lo clasificado A, B y C en el sheet. A y B en PDF más PPTX editable, C solo PDF, print en calidad pro, video en mp4. Cada archivo subió directo a su subcarpeta de marca. Nada quedó suelto en la raíz de Drive. Verifiqué cada subida contra la respuesta de Drive: id, carpeta padre y tamaño. 242 de 242 ok, cero fallos. Uploads, personales e INBOX se quedaron en Canva, como acordamos. Columna Migrated del sheet actualizada para los 155. Limitaciones que encontré: Dos diseños tipo doc (RV Venue Scaling Roadmap y un doc de TF) no permiten PPTX por API. Solo PDF. Si se necesitan editables, se convierten en Canva primero. La API no exporta SVG. Los logos vectoriales siguen solo en Canva. El PPTX del TF Stories Pack pesa 788 MB. Recomiendo una versión liviana antes de compartirlo. Encontrado en el camino: hay 6 docs personales en el workspace de Canva. No los toqué. Riesgo: la verificación fue por API, no visual. Fuentes raras pueden verse distintas en el PPTX. Siguiente paso: Luis revisa 3 carpetas al azar (TF 01 Brand, CTS 02 Templates, DR 05 Sports) y confirma. Esta semana. Tiempo: 2h35 neto (11:09 a 15:00 con pausa).

_Sincronizado por Brain: 2026-10-01T03:14:43.530Z_
