---
type: reference
brand: cts
area: delivery/utensils
parent: [[Utensils-Home]]
source: [[Recipe-Pack-Source-Index]]
source-pack: "Manual de Recetas - Punto de Venta"
source-filename: "Lista de utensilios.xlsx"
status: canon
language: es
---

# Utensils List

## Purpose
Master utensil and equipment inventory for CTS POS kitchen. Covers cookware, knives, scales, thermometers, containers, dispensers. Includes per-unit and total cost — supports kitchen replenishment and capex planning.

## Source integrity notes
- Workbook = single sheet `Hoja1`, 886 rows total but only **41 utensil rows + 1 header** are populated (rest blank).
- Headers: column 4 + 5 both labeled `TOTAL` (column 5 always blank in source).
- Last row `Espátula Plastico Pelton Gris` has trailing newline in source cell — preserved.
- All currency values appear to be USD (inferred from supplier vocabulary like "Sams", "Pan Food"). Currency unit not explicit in workbook.
- Item names mix Spanish + English vendor SKU descriptors verbatim from supplier catalogs (e.g. "Sartén... TABLE", "Pan Sheet Aluminio").

## Master utensil list

| Utensilio | Cantidad | Precio (USD) | Total (USD) |
|---|---|---|---|
| Cacerola Vapor MESA acero inoxidable calibre 22 DEEP de 4" | 5.0 | 20.0 | 100 |
| Sartén para cocinar al vapor de acero inoxidable calibre 22 de 6 pulgadas TABLE | 5.0 | 42.0 | 210 |
| Sartén para cocinar al vapor de acero inoxidable calibre 22 de 2,5 pulgadas TABLE DEEP | 3.0 | 19.78 | 59.34 |
| Cacerola Vapor MESA Calibre 22 Acero inoxidable 6" DEEP | 5.0 | 29.44 | 147.2 |
| Producto de rollo de etiquetas / preparado por 2 pulgadas X 500 UND | 1.0 | 30.85 | 30.85 |
| Autobús de caja negra de 5 pulgadas y 15 x 20 3 UND | 2.0 | 43.28 | 86.56 |
| Caja de cubierta para autobús gris 15 X 20 | 6.0 | 55.95 | 335.7 |
| Soporte MESA Kit de estante de exhibición | 2.0 | 78.94 | 157.88 |
| Cuchillo Pan Ofset Filo Ondulado 7 Pulgadas | 2.0 | 19.39 | 38.78 |
| Cuchillo CHEF Milenio | 3.0 | 33.69 | 101.07 |
| Tabla Cortante Polietileno Rd 18" X 24" | 4.0 | 38.93 | 155.72 |
| Medidor de tazas Gal Clear | 4.0 | 26.89 | 107.56 |
| Cuchara Medidora Con Tazas 13 Piezas | 2.0 | 135.82 | 271.64 |
| Báscula Digital Porción CONTROL 11 Libras | 3.0 | 158.29 | 474.87 |
| Pinzas para servir de acero inoxidable | 2.0 | 18.56 | 37.12 |
| Guante de horno beige de 17 pulgadas | 2.0 | 39.85 | 79.7 |
| Mango de acero inoxidable sólido azul oscuro para platos | 2.0 | 14.95 | 29.9 |
| Pan Sheet Aluminio 1/2 Tamaño Calibre 18 | 10.0 | 18.99 | 189.9 |
| Pan Sheet Aluminio Cerrado Perla Calibre 16 | 4.0 | 30.72 | 122.88 |
| Set Batería de Cocina Inoxidable 7 Piezas | 1.0 | 192.52 | 192.52 |
| Termómetro digital de bolsillo-40 grados Farenheit a 302 grados Farenheit | 1.0 | 19.99 | 19.99 |
| Termómetro Congelador Refrigerador -40-80 grados Fahrenheit | 1.0 | 11.49 | 11.49 |
| Pan Food Hpan Octavo 4in Amb X6 | 3.0 | 61.51 | 184.53 |
| Cubrir Recipiente para alimentos Transparente UNIVERSAL Ranurado | 18.0 | 15.89 | 286.02 |
| Pan Food Half Oval 4 1/2 Deep x 6 Quart | 1.0 | 168.0 | 168 |
| Rascador Plástico Softspoon Blanco | 3.0 | 3.67 | 11.01 |
| Vaso Medidor Transparente 2 Qt | 3.0 | 15.44 | 46.32 |
| Pan Fry Steelcoat 7 Pulgadas | 1.0 | 32.44 | 32.44 |
| Plato Cassrl Sin Tapa Cerámica Redondo Cáscara De Huevo 9.5 Onzas x12 | 1.0 | 89.36 | 89.36 |
| WHIPPER Mango de nailon para piano | 2.0 | 22.5 | 45 |
| Cuenco Mezclador Acero Inoxidable 4 Qt | 2.0 | 3.22 | 6.44 |
| Brocha para hilvanar repostería de nailon de 2" de ancho | 2.0 | 17.56 | 35.12 |
| Tazón mezclador redondo de acero inoxidable de 256 onzas | 3.0 | 9.65 | 28.95 |
| Horno Microondas Acero Inoxidable | 1.0 | 393.57 | 393.57 |
| Tijeras Tijeras Cocina Inoxidable | 1.0 | 11.81 | 11.81 |
| Salero y Pimentero Acero Inoxidable | 2.0 | 11.22 | 22.44 |
| Dispensador Toalla Rollo 10 Auto BLACK | 1.0 | 72.52 | 72.52 |
| Dispensador Condmnt Botella exprimible de boca ancha transparente 16 oz x 6 | 1.0 | 82.62 | 82.62 |
| Jabonera | 2.0 | 24.95 | 49.9 |
| Rodillo de amasar de madera francés cónico | 2.0 | 9.19 | 18.38 |
| Cucharón Sopa Lourve | 3.0 | 30.52 | 91.56 |
| Espátula Plastico Pelton Gris | 2.0 | 14.94 | 29.88 |

**Total estimado:** ~$4,666.54 USD (suma calculada de columna `Total`)

## Source structural anomalies
- 845 trailing blank rows after the last utensil — preserved as-is in source XLSX.
- Column 5 (second `TOTAL`) is empty across all rows.
- Some rows store `Total` as formula-evaluated number, others as integer — preserved as displayed.

## Related
- [[Utensils-Home]]
- [[Recipes-Home]]
- [[Recipe-Pack-Source-Index]]

