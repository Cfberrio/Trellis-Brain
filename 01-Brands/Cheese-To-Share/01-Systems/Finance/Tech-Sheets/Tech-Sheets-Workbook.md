---
type: hub
brand: cts
area: finance/tech-sheets
parent: [[Tech-Sheets-Home]]
source: [[Recipe-Pack-Source-Index]]
source-pack: "Manual de Recetas - Punto de Venta"
source-filename: "2. Fichas Técnicas con Costos Unitarios.xlsx"
status: canon
language: es
sensitivity: financial
---

# Fichas Técnicas — Workbook Index

## Purpose
Costing and pricing workbook for CTS POS recipes + production planta. Source: 8-sheet XLSX. Inputs: recipe ingredients × valor unitario → unit costs → final cost (con MO + merma) → suggested price.

## Source integrity notes
- Workbook has **8 sheets**; some are working/draft sheets (`Revisión - Recetas 4SEP`, `Hoja 9`).
- `COSTO-RECETARIO.` (with trailing period) and `Revisión - Recetas 4SEP` overlap in scope (recipe-level ingredient × cost) — Revisión appears to be a later working copy with extra `DESCRIPCION DE PRODUCTO` column.
- `PRECIOS` is the upstream supplier price database (per-Oz / per-unit cost basis). 971 rows.
- `COSTO PLANTA` + `COSTO FINAL PLANTA` cover internally manufactured base ingredients (cheesecake, caramelized onion, etc.).
- `Hoja 9` is a stub category list (CHS=QUESO, CHARCUTERIA, PRODUCTOS DE LIMPIEZA).
- `DESPERDICIOS` is a daily waste log template (`EV-CAL-FT-10`, version 1, dated 06/04/2025) — operational not costing.
- Multiple sheets contain blank rows and inconsistent column counts. Preserved in per-sheet notes.

## Sheets

| Sheet | Rows | Note |
|---|---|---|
| `COSTO FINAL` | 42 | Per-recipe final cost summary (cost + MO + merma → costo total + tax) |
| `COSTO-RECETARIO.` | 556 | Recipe × ingredient × valor — see [[Tech-Sheets-Costo-Recetario]] |
| `Revisión - Recetas 4SEP` | 550 | Working copy of recetario w/ description column — see [[Tech-Sheets-Revision-Recetas]] |
| `PRECIOS` | 971 | Supplier price database — see [[Tech-Sheets-Precios]] |
| `COSTO PLANTA` | 83 | Planta-produced ingredient costs |
| `COSTO FINAL PLANTA` | 13 | Planta final cost summary |
| `Hoja 9` | 11 | Category stub |
| `DESPERDICIOS` | 338 | Daily waste log template — see [[Tech-Sheets-Desperdicios]] |

---

## Sheet: COSTO FINAL (full content)

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  | PRODUCTO | COSTO | MANO DE OBRA | MERMA | COSTO TOTAL | VALOR TAX | IMPUESTO |
|  |  |  |  |  |  |  |  |
| CHEESEBOARDS | SINGLE BASIC | 8.553583706 | 0.35 | 0.05 | 11.97501719 | 0 | 0 |
|  | MEDIUM BASIC | 9.873025163 | 0.35 | 0.05 | 13.82223523 | 0 | 0 |
|  | SINGLE BELLA | 10.62793875 | 0.35 | 0.05 | 14.87911425 | 0 | 0 |
|  | MEDIUM BELLA | 13.38734751 | 0.35 | 0.05 | 18.74228651 | 0 | 0 |
|  | SINGLE BULLA | 13.48509146 | 0.35 | 0.05 | 18.87912805 | 0 | 0 |
|  | MEDIUM BULLA | 14.01041098 | 0.35 | 0.05 | 19.61457537 | 0 | 0 |
| FLATBREAD | MARGHERITA | 2.626670573 | 0.35 | 0.05 | 3.677338802 | 0 | 0 |
|  | BBQ CHICK | 4.011964522 | 0.35 | 0.05 | 5.61675033 | 0 | 0 |
|  | BUFF CHICK | 5.023156092 | 0.35 | 0.05 | 7.032418529 | 0 | 0 |
|  | PROSCIUTTO | 3.275744382 | 0.35 | 0.05 | 4.586042135 | 0 | 0 |
| SHAREABLES | MEAT BOARD | 6.329703007 | 0.35 | 0.05 | 8.86158421 | 0 | 0 |
|  | GUAC & CHIPS | 3.637220762 | 0.35 | 0.05 | 5.092109067 | 0 | 0 |
|  | CHEESE & BREAD | 3.8841 | 0.35 | 0.05 | 5.43774 | 0 | 0 |
| SANDWICHES | FOCACCIA PISTACHIO | 6.784961058 | 0.35 | 0.05 | 9.498945481 | 0 | 0 |
|  | CAPRESE | 4.546180784 | 0.35 | 0.05 | 6.364653097 | 0 | 0 |
|  | PINEAPPLE PROSCIUTTO | 5.755678452 | 0.35 | 0.05 | 8.057949832 | 0 | 0 |
|  | CHIKEN PESTO | 4.853187142 | 0.35 | 0.05 | 6.794461999 | 0 | 0 |
|  | TRUFFLE BRIE | 5.384753771 | 0.35 | 0.05 | 7.53865528 | 0 | 0 |
|  | HOT HONEY | 7.387673237 | 0.35 | 0.05 | 10.34274253 | 0 | 0 |
|  | BEEF AIOLI | 8.109540741 | 0.35 | 0.05 | 11.35335704 | 0 | 0 |
| TOAST | TUSCANY | 3.816410532 | 0.35 | 0.05 | 5.342974745 | 0 | 0 |
|  | IBIZA | 4.897717404 | 0.35 | 0.05 | 6.856804366 | 0 | 0 |
|  | MANHATTAN | 4.380921931 | 0.35 | 0.05 | 6.133290703 | 0 | 0 |
|  | AVOCADO | 4.292421442 | 0.35 | 0.05 | 6.009390019 | 0 | 0 |
|  | PROVENCE | 5.869231653 | 0.35 | 0.05 | 8.216924314 | 0 | 0 |
|  | POSITANO | 5.608905174 | 0.35 | 0.05 | 7.852467244 | 0 | 0 |
| BREAD BOWLS | DIAVOLA | 3.847876206 | 0.35 | 0.05 | 5.387026689 | 0 | 0 |
|  | MAC’D | 3.41991891 | 0.35 | 0.05 | 4.787886474 | 0 | 0 |
|  | NAPOLI | 3.540481227 | 0.35 | 0.05 | 4.956673717 | 0 | 0 |
|  | CTS | 4.105573503 | 0.35 | 0.05 | 5.747802904 | 0 | 0 |
| DESSERTS | CHOCOLATE FONDUE | 6.227941167 | 0.35 | 0.05 | 8.719117634 | 0 | 0 |
|  | CHEESECAKE BLUEBERRIES | 1.932660479 | 0.35 | 0.05 | 2.705724671 | 0 | 0 |
|  | CHEESECAKE DUBAI CHOCOLATE | 4.151423367 | 0.35 | 0.05 | 5.811992714 | 0 | 0 |
|  | CHEESECAKE PINEAPPLE | 3.152969121 | 0.35 | 0.05 | 4.41415677 | 0 | 0 |
|  | CHEESECAKE GUAVA | 3.102755266 | 0.35 | 0.05 | 4.343857372 | 0 | 0 |
|  | CHEESECAKE | 2.082115456 | 0.35 | 0.05 | 2.914961638 | 0 | 0 |
|  | CHEESECAKE TIRAMISU | 1.372660479 | 0.35 | 0.05 | 1.921724671 | 0 | 0 |
|  | CROSSANT DULCE | 4.828537681 | 0.35 | 0.05 | 6.759952754 | 0 | 0 |
|  |  | 212.1784531 |  |  |  |  |  |

---

## Sheet: COSTO PLANTA (full content)

| PRODUCTO | DESCRIPCION DE  PRODUCTO | PRODUCTO | U. MEDIDA | CANTIDAD | VALOR | VALOR POR PRODUCTO |  |
|---|---|---|---|---|---|---|---|
| BASQUE CHEESECAKE | Queso crema | SOFT CREAM CHEESE JAMES FARM | Oz | 17.85 | 0.1527160494 | 2.725981481 |  |
| BASQUE CHEESECAKE | Azucar | SUGAR | Oz | 7.14 | 0.06421497797 | 0.4584949427 |  |
| BASQUE CHEESECAKE | Crema de leche heavy  whipping cream | CREMA DE LECHE HEAVY  WHIPPING CREAM | Oz | 8.92 | 0.1451822917 | 1.295026042 |  |
| BASQUE CHEESECAKE | Huevos | HUEVOS | Und | 4.0 | 0.4663333333 | 1.865333333 |  |
| BASQUE CHEESECAKE | Harina de arroz | FLOUR RICE BLANCO | Oz | 0.5 | 0.03685638767 | 0.01842819383 |  |
| BASQUE CHEESECAKE | Queso de cabra | CHS GOAT CHEESE | Oz | 7.85 | 0.4514285714 | 3.543714286 | 8 PORCIONES |
| BASQUE CHEESECAKE | Vainilla | VAINILLA | Oz | 0.3 | 0.1276851852 | 0.03830555556 | 9.945283834 |
| BASQUE CHEESECAKE TIRAMISU |  | LADY FINGER COOKIES | Un | 24.0 | 0.07142857143 | 1.714285714 |  |
| BASQUE CHEESECAKE TIRAMISU |  | SUGAR | Oz | 0.5 | 0.06421497797 | 0.03210748899 |  |
| BASQUE CHEESECAKE TIRAMISU |  | CAFE INSTANTANEO | Oz | 0.5 | 0 | 0 |  |
| BASQUE CHEESECAKE TIRAMISU |  | CALUA - LICOR DE CAFE | Oz | 2.0 | 0 | 0 |  |
| BASQUE CHEESECAKE TIRAMISU |  | SOFT CREAM CHEESE JAMES FARM | Oz | 17.85 | 0.1527160494 | 2.725981481 |  |
| BASQUE CHEESECAKE TIRAMISU |  | SUGAR | Oz | 7.14 | 0.06421497797 | 0.4584949427 |  |
| BASQUE CHEESECAKE TIRAMISU |  | CREMA DE LECHE HEAVY  WHIPPING CREAM | Oz | 8.92 | 0.1451822917 | 1.295026042 |  |
| BASQUE CHEESECAKE TIRAMISU |  | HUEVOS | Und | 4.0 | 0.4663333333 | 1.865333333 |  |
| BASQUE CHEESECAKE TIRAMISU |  | FLOUR RICE BLANCO | Oz | 0.5 | 0.03685638767 | 0.01842819383 |  |
| BASQUE CHEESECAKE TIRAMISU |  | CHS GOAT CHEESE | Oz | 7.85 | 0.4514285714 | 3.543714286 |  |
| BASQUE CHEESECAKE TIRAMISU |  | VAINILLA | Oz | 0.3 | 0.1276851852 | 0.03830555556 |  |
| CEBOLLA CARAMELIZADA | cebollas blancas | WHITE ONION | Und | 12.0 | 0.49275 | 5.913 |  |
| CEBOLLA CARAMELIZADA | vinagre | VINAGRE | Oz | 2.0 | 0.04845588235 | 0.09691176471 |  |
| CEBOLLA CARAMELIZADA | agua | AGUA | Oz | 2.0 | 0 | 0 |  |
| CEBOLLA CARAMELIZADA | azucar | SUGAR | Oz | 400 | 0.06421497797 | 25.68599119 |  |
| CEBOLLA CARAMELIZADA | aceite de oliva | OIL OLIVE SUPREMO | Oz | 100 | 0.1885185185 | 18.85185185 |  |
| CEBOLLA CARAMELIZADA | de aceto balsamico | BALSAMIC ARTIGIANO BELGIOSO | Oz | 50 | 0.371875 | 18.59375 | 69.14150481 |
| DIF DE BUFALO |  | PARMESANO | Oz | 16.0 | 0.8725 | 13.96 |  |
| DIF DE BUFALO |  | SOUR CREAM | Oz | 24.0 | 0.11 | 2.64 |  |
| DIF DE BUFALO | POLLO DESPECHADO | SYS GR CHIKEN | Oz | 48.0 | 0.4129012346 | 19.81925926 |  |
| DIF DE BUFALO | DIP DE BUFALO | SAUCE WINGBUF | GALON | 48.0 | 0.11828125 | 5.6775 |  |
| DIF DE BUFALO |  | PEPPER | Oz | 3.0 | 1.74875 | 5.24625 |  |
| DIF DE BUFALO |  | CHS CHEDDAR WHITE | Oz | 64.0 | 0.1851851852 | 11.85185185 |  |
| DIF DE BUFALO |  | MAYONESA | Oz | 36.0 | 0.1283823529 | 4.621764706 |  |
| DIF DE BUFALO |  | AJINOMOTO | Oz | 2.0 | 0.390625 | 0.78125 | 64.59787582 |
| DIP DE ESPINACA | Sour cream | SOUR CREAM | Oz | 48.0 | 0.11 | 5.28 |  |
| DIP DE ESPINACA | Cream cheese spre |  CREAM CHEESE SOFT | Oz | 48.0 | 0.2820205479 | 13.5369863 | 18.8169863 |
| DIP DE ESPINACA | Parmesano Cheese | PARMESANO | Oz | 24.0 | 0.8725 | 20.94 |  |
| DIP DE ESPINACA | White Cheddar | CH WHITE SHARP CHEDDAR CHEESE - JAMES FARM | Oz | 64.0 | 0.183 | 11.712 |  |
| DIP DE ESPINACA | Pimienta | PEPPER | Oz | 0.2 | 1.74875 | 0.34975 |  |
| DIP DE ESPINACA | Mayonesa | MAYONESA | Oz | 36.0 | 0.1283823529 | 4.621764706 |  |
| DIP DE ESPINACA | Ajinomoto | AJINOMOTO | Oz | 2.0 | 0.390625 | 0.78125 | 38.40476471 |
| GLASSE DE LIMON | jugo de limon amarillo | LIMÓN CHOICE FRESCO | Oz | 4.0 | 0.2261811594 | 0.9047246377 |  |
| GLASSE DE LIMON | aceite de oliva | OIL OLIVE SUPREMO | Oz | 12.0 | 0.1885185185 | 2.262222222 |  |
| PIÑA Y GUAYABA |  | SYS TOPPING PINEAPPLE | Oz | 1.8 | 0.2501714678 | 0.450308642 |  |
| PIÑA Y GUAYABA |  | DIP DE GUAYABA | Oz | 1.8 | 0.2222748815 | 0.4000947867 |  |
| POLLO DESMECHADO | pechuga de pollo | CHICKEN BREAST | Oz | 649.0 | 0.1966784141 | 127.6442907 |  |
| POLLO DESMECHADO | cebolla cabezona | WHITE ONION | Und | 2.0 | 0.49275 | 0.9855 |  |
| POLLO DESMECHADO | aceite de oliva | OIL OLIVE SUPREMO | Oz | 1.0 | 0.1885185185 | 0.1885185185 |  |
| POLLO DESMECHADO | sazonador | SAZONADOR | Oz | 0.3 | 0.83856 | 0.251568 | 133.0872276 |
| POLLO DESMECHADO | ajises dulces | PACKER LABEL MINI SWEET PEPPERS, FRESH, 4 LB PACKAGE, 1/CASE | Oz | 32.0 | 0.4175330396 | 13.36105727 |  |
| SALSA NAPOLITANA | cilantro | CILANTRO FRESCO | Oz | 4.0 | 0.434375 | 1.7375 |  |
| SALSA NAPOLITANA | carne molida de res | MOLIDO DE RES | Oz | 64 | 0.3418882979 | 21.88085106 |  |
| SALSA NAPOLITANA | carne molida de cerdo | MOLIDO DE CERDO | Oz | 16.0 | 0.2219647577 | 3.551436123 |  |
| SALSA NAPOLITANA | cebolla grande | WHITE ONION | Und | 1.0 | 0.49275 | 0.49275 |  |
| SALSA NAPOLITANA | salsa marinara | SALSA MARINARA | Oz | 48.0 | 0.1251587302 | 6.007619048 |  |
| SALSA NAPOLITANA | sal | SAL | Oz | 7.0 | 0.03230769231 | 0.2261538462 |  |
| SALSA NAPOLITANA | pimienta | PEPPER | Oz | 3.5 | 1.74875 | 6.120625 |  |
| SALSA NAPOLITANA | mostaza | MOSTAZA | Oz | 100 | 0.08522058824 | 8.522058824 | Oz TOTAL |
| SALSA NAPOLITANA | salsa de tomate | SALSA TOMATO PIZZAIOLO | Oz | 100.0 | 0.1822222222 | 18.22222222 | 66.76121613 |
| AIOLI DE CILANTRO - SALSA VERDE | cilantro | CILANTRO FRESCO | Oz | 64 | 0.434375 | 27.8 |  |
| AIOLI DE CILANTRO - SALSA VERDE | perejil | PEREJIL | Oz | 16.0 | 0.436875 | 6.99 |  |
| AIOLI DE CILANTRO - SALSA VERDE | cabezas de ajo | AJOS | Oz | 5.0 | 0.4430864198 | 2.215432099 | 63.74971314 |
| AIOLI DE CILANTRO - SALSA VERDE | limon | LIMES BAGS 5 LB | Oz | 3.0 | 0.09225 | 0.27675 |  |
| AIOLI DE CILANTRO - SALSA VERDE | cebollin | CEBOLLIN | Oz | 5.0 | 0.853125 | 4.265625 |  |
| AIOLI DE CILANTRO - SALSA VERDE | aceite de oliva | OIL OLIVE SUPREMO | Oz | 2.0 | 0.1885185185 | 0.377037037 |  |
| AIOLI DE CILANTRO - SALSA VERDE | sal | SAL | Oz | 7.0 | 0.03230769231 | 0.2261538462 | 5.145565883 |
| AIOLI DE CILANTRO - SALSA VERDE | pimenton verde | PIMENTON VERDE FRESCO | Oz | 8.0 | 0.1765822785 | 1.412658228 |  |
| AIOLI DE CILANTRO - SALSA VERDE | mayonesa | MAYONESA | Oz | 17.1 | 0.1283823529 | 2.195338235 | 3.607996463 |
| QUESO CREMA DE CEBOLLA |  | CHEESE BRIE SPREAD CREAM PHILADELPHIA | Oz | 48.0 | 0.2910958904 | 13.97260274 |  |
| QUESO CREMA DE CEBOLLA |  | CEBOLLA ROJA | Oz | 5.0 | 0.07422222222 | 0.3711111111 |  |
| QUESO CREMA DE CEBOLLA |  | ALCAPARRAS | Oz | 25.0 | 0.2915625 | 7.2890625 |  |
| QUESO CREMA DE CEBOLLA |  | PEPPER | Oz | 0.01 | 1.74875 | 0.0174875 |  |
| DIP CTS |  | PUERROS | Paq | 5.0 | 4.37 | 21.85 |  |
| DIP CTS |  | VINO CHARDONNEY | ml | 750.0 | 0.006666666667 | 5 |  |
| DIP CTS |  | SAL | Oz | 0.17 | 0.03230769231 | 0.005492307692 |  |
| DIP CTS |  | PEPPER | Oz | 0.085 | 1.74875 | 0.14864375 | LB |
| DIP CTS |  | CHEESE BRIE SPREAD CREAM | Oz | 160 | 0.2875 | 46 | Oz |
| DIP CTS |  | MAYO REAL | Oz | 32.0 | 0.125859375 | 4.0275 | Oz TOTAL |
| DIP CTS |  | PARMESANO | Oz | 36.0 | 0.8725 | 31.41 | 108.4416361 |
|  |  |  | #N/A |  | 0 | 0 |  |
|  |  |  | #N/A |  | 0 | 0 |  |
|  |  |  | #N/A |  | 0 | 0 |  |
|  |  |  | #N/A |  | 0 | 0 |  |
|  |  |  | #N/A |  | 0 | 0 |  |

---

## Sheet: COSTO FINAL PLANTA (full content)

|  | PRODUCTO | COSTO | MANO DE OBRA | MERMA | COSTO TOTAL |  |  |
|---|---|---|---|---|---|---|---|
|  | BASQUE CHEESECAKE | 1.243160479 | 0.2 | 0.05 | 1.553950599 |  |  |
|  | CEBOLLA CARAMELIZADA | 69.14150481 | 0.35 | 0.05 | 96.79810673 |  |  |
|  | DIP DE ESPINACA | 57.22175101 | 0.35 | 0.05 | 80.11045141 |  |  |
|  | GLASSE DE LIMON | 3.16694686 | 0.35 | 0.05 | 4.433725604 |  |  |
|  | MERMELADA DE BLUE BERRY | 0 | 0.35 | 0.05 | 0 |  |  |
|  | POLLO DESECHADO | 0 | 0.35 | 0.05 | 0 |  |  |
|  | SALSA NAPOLITANA | 66.76121613 | 0.35 | 0.05 | 93.46570258 |  |  |
|  | SALSA VERDE | 0 | 0.35 | 0.05 | 0 |  |  |
|  | DIF DE BUFALO | 64.59787582 | 0.35 | 0.05 | 90.43702614 |  |  |
|  | DUBAI CHOCOLATE | 0 | 0.35 | 0.05 | 0 |  |  |
|  | FRUTOS DE BOSQUE BLUEBERRIES | 0 | 0.35 | 0.05 | 0 |  |  |
|  | PIÑA Y GUAYABA | 0.8504034287 | 0.35 | 0.05 | 1.1905648 |  |  |

---

## Sheet: Hoja 9 (full content)

| CHS | QUESO |  |  |
|---|---|---|---|
| CHARCUTERIA |  |  |  |
| PRODUCTOS DE LIMPIENZA |  |  |  |
| FRUTAS - LEGUMBRES |  |  |  |
| PANADERIA |  |  |  |
| EMPAQUES |  |  |  |
| ABARROTES |  |  |  |
| BEBIDAS |  |  |  |
| PRODUCTOS PERSONAL |  |  |  |
| PROTEINA |  |  |  |
| False |  |  |  |

---

## Heavy sheets (linked)
Per-sheet notes preserve full data without bloating this hub:
- [[Tech-Sheets-Costo-Recetario]]
- [[Tech-Sheets-Revision-Recetas]]
- [[Tech-Sheets-Precios]]
- [[Tech-Sheets-Desperdicios]]

## Related
- [[Tech-Sheets-Home]]
- [[Pricing-Logic]]
- [[Recipes-Home]]
- [[Recipe-Pack-Source-Index]]
