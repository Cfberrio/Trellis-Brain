---
type: source
brand: cts
parent: [[Recipes-Home]]
status: source
---

# Recipe Pack Source Index

Raw imported source material from CTS recipe ZIP pack. Evidence layer — preserves original fidelity. Canonical clean notes live under `01-Systems/Delivery/Recipes/`.

## Status
Empty. ZIP not yet extracted.


## Imported batches
- **Phase 1A — Desserts** (2026-04-27)
  - Source ZIP: `1. MANUAL DE RECETAS - PUNTO DE VENTA-20260427T163324Z-3-001.zip`
  - File processed: `7. DESSERTS/DESSERTS CHOCOLATE FONDUE.docx`
  - Canon note: [[Chocolate-Fondue]]

## Pending
- Cheeseboards, Flatbread, Shareables, Sandwich, Toasts, Bread Bowls
- Storage protocols (EN+ES)
- Utensilios XLSX
- Fichas Técnicas Costos XLSX
- Carta XLSX
- Recomendaciones / Algo de Historia
- **Phase 1B — Cheeseboards** (2026-04-27)
  - File processed: `1. CHEESEBOARDS/1. TABLAS.docx`
  - Canon note: [[Tablas-Cheeseboards]]
  - Note: source contained 4 variants (Base/Basic/Bella/Bulla) consolidated into one note per Phase 1B scope rule.
- **Phase 1C — Flatbread** (2026-04-27)
  - Files processed:
    - `2. FLATBREAD/1. FLATBREAD MARGHERITA.docx`
    - `2. FLATBREAD/2. FLATBREAD BBQ CHICK_.docx`
    - `2. FLATBREAD/3. FLATBREAD BUFF CHICK_.docx`
    - `2. FLATBREAD/4. FLATBREAD PROSCIUTTO.docx`
  - Canon notes: [[Flatbread-Margherita]], [[Flatbread-BBQ-Chicken]], [[Flatbread-Buffalo-Chicken]], [[Flatbread-Prosciutto]]
- **Phase 1D — Shareables** (2026-04-27)
  - Files processed:
    - `3. SHAREABLES/2. SHAREABLES CHEESE & BREAD.docx`
    - `3. SHAREABLES/3. SHAREABLES GUAC & CHIPS.docx`
  - Canon notes: [[Shareables-Cheese-And-Bread]], [[Shareables-Guac-And-Chips]]
  - Note: source ZIP did not contain a `1. SHAREABLES *.docx` file (numbering jumps from 2 → 3).
- **Phase 1E — Bread Bowls** (2026-04-27)
  - Files processed:
    - `6. BREAD BOWLS/1. BREAD BOWL MAC'D.docx`
    - `6. BREAD BOWLS/2. BREAD BOWL NAPOLI.docx`
    - `6. BREAD BOWLS/3. BREAD BOWL DIAVOLA.docx`
    - `6. BREAD BOWLS/4. BREAD BOWL CTS.docx`
  - Canon notes: [[Bread-Bowl-MacD]], [[Bread-Bowl-Napoli]], [[Bread-Bowl-Diavola]], [[Bread-Bowl-CTS]]
  - Cross-cutting integrity flag: all 4 reference "queso Gouda (merma)" in step 3 but Gouda absent from all ingredient tables.
  - File 4 (CTS) uses expanded template w/ empty fields (Código Interno, Utensilios y Equipos list, Método de Preparación block, Especificación column).
  - File 1 (Mac'D) original filename contains right single-quote (`MAC'D`); raw ZIP listing shows mojibake (`MAC���D`) due to non-UTF-8 zip encoding.
  - File 2 (Napoli) ingredient `Salami Genova Sliced` listed but never used in steps; ingredient table omits Sal but step 5 instructs salt addition.
  - File 3 (Diavola) ingredient `Withe Sharp Cheddar Monterrey` — typo `Withe` preserved verbatim.
- **Phase 1F — Sandwich + Toasts** (2026-04-27)
  - Sandwich files (7):
    - `4. SANDWICH/1. SANDWICH FOCACCIA PISTACHIO.docx`
    - `4. SANDWICH/2. SANDWICH CAPRESE.docx`
    - `4. SANDWICH/3. SANDWICH PINEAPPLE PROSCIUTTO.docx`
    - `4. SANDWICH/4. SANDWICH CHIKEN PESTO_.docx`
    - `4. SANDWICH/5. SANDWICH TRUFFLE BRIE.docx`
    - `4. SANDWICH/6. SANDWICH HOT HONEY.docx`
    - `4. SANDWICH/7. SANDWICH BEEF AIOLI.docx`
  - Sandwich canon: [[Sandwich-Focaccia-Pistachio]], [[Sandwich-Caprese]], [[Sandwich-Pineapple-Prosciutto]], [[Sandwich-Chicken-Pesto]], [[Sandwich-Truffle-Brie]], [[Sandwich-Hot-Honey]], [[Sandwich-Beef-Aioli]]
  - Toasts files (6):
    - `5. TOASTS/1. TUSCANY.docx`
    - `5. TOASTS/2. IBIZA.docx`
    - `5. TOASTS/3. FRENCHIE.docx`
    - `5. TOASTS/4. AVOCADO.docx`
    - `5. TOASTS/5. POSITANO.docx`
    - `5. TOASTS/PROVENCE.docx` *(no number prefix in source)*
  - Toasts canon: [[Toast-Tuscany]], [[Toast-Ibiza]], [[Toast-Frenchie]], [[Toast-Avocado]], [[Toast-Positano]], [[Toast-Provence]]
  - Cross-cutting source issues:
    - All Toasts source spell `Multigraim` (not Multigrain) — preserved.
    - `Rugula` (table) vs `rúcula` (steps) drift across both categories.
    - Multiple recipes reference tomate cherry / rúcula in steps without listing them in ingredient tables (Tuscany, Pineapple Prosciutto, Chicken Pesto, Truffle Brie, Avocado).
    - Source filename `4. SANDWICH CHIKEN PESTO_.docx` — typo `CHIKEN` + trailing underscore preserved.
    - Source filename `PROVENCE.docx` lacks numbering prefix.
    - Caprese: `Tomate Fresco` listed twice; `Oil Olive Supremo` unit `GR` instead of `Oz`.
    - Ibiza: `Glasé de Limón` listed twice with different quantities.
    - Beef Aioli: name says "Aioli" but ingredient is `Salsa Verde`; "aceite de tomate" referenced in step but absent from table.
- **Phase 1G — Recipe-support materials** (2026-04-27)
  - **Storage protocols** (DOCX, EN+ES):
    - `5. EV-CAL-MAN-02 Protocol for Storage and Preservation of Supplies - English.docx`
    - `5. EV-CAL-MAN-02 Protocolo de Almacenamiento y Conservación de Insumos - Spanish.docx`
    - Canon: [[Storage-Protocol]] (bilingual single note)
  - **Utensils**:
    - `Lista de utensilios.xlsx` (1 sheet, 41 utensils)
    - Canon: [[Utensils-List]]
  - **Tech sheets / fichas técnicas**:
    - `2. Fichas Técnicas con Costos Unitarios.xlsx` (8 sheets)
    - Canon: [[Tech-Sheets-Workbook]] + per-heavy-sheet notes ([[Tech-Sheets-Costo-Recetario]], [[Tech-Sheets-Revision-Recetas]], [[Tech-Sheets-Precios]], [[Tech-Sheets-Desperdicios]])
  - **Menu (Carta workbook)**:
    - `Carta Cheese to Share.xlsx` (8 sheets, multi-version EN+ES + DOWNTOWN)
    - Canon: [[Menu-Operations]]
  - **Still pending** (recipe pack supplemental, out of Phase 1G scope):
    - `1. Recetario Estandarizado 3.Manual de Preparación/ALGO DE HISTORIA.docx`
    - `RECOMENDACIONES.docx`
    - `RECOMENDACIONES GENERALES.docx`

## Recipe pack import status
- Phases 1A–1F: 7 recipe categories complete (Desserts, Cheeseboards, Flatbread, Shareables, Bread Bowls, Sandwich, Toasts).
- Phase 1G: storage, utensils, tech sheets, menu — complete.
- Pending: 3 prep guides (history + general recommendations).
- **Phase 1H — Recipe support references** (2026-04-27)
  - Files processed:
    - `1. Recetario Estandarizado 3.Manual de Preparación/RECOMENDACIONES.docx`
    - `1. Recetario Estandarizado 3.Manual de Preparación/RECOMENDACIONES GENERALES.docx`
    - `1. Recetario Estandarizado 3.Manual de Preparación/ALGO DE HISTORIA.docx`
  - Canon notes:
    - [[Recipe-Recommendations]]
    - [[General-Recommendations]]
    - [[Recipe-History-And-Context]]
  - Placement: `01-Systems/Delivery/Recipes/Reference/` (justified subfolder for 3 support docs)

## Recipe pack — final status

✅ **Recipe pack import complete.** All source files in `1. MANUAL DE RECETAS - PUNTO DE VENTA-...zip` accounted for:
- 7 recipe categories canon (Desserts, Cheeseboards, Flatbread, Shareables, Bread Bowls, Sandwich, Toasts)
- Storage protocols (EN+ES) canon
- Utensils list canon
- Tech sheets workbook canon (8 sheets, full data)
- Menu carta canon (8 sheets, full data)
- Recipe support references canon (3 documents)
