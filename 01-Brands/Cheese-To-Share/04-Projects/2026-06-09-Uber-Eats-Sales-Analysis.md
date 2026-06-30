---
brand: Cheese-To-Share
area: projects
note_type: project
status: active
canonical: true
used_for_ai: true
source_type: analysis
owner: Luis
last_updated: 2026-06-09
sensitivity: internal
hub_role: leaf
tags:
  - cts/reporting
  - cts/menu-decision
  - uber-eats
---

# CTS — Análisis de Ventas Uber Eats (Jun 2025 – May 2026)

## Parent
- [[01-Brands/Cheese-To-Share/04-Projects/Projects-Home|CTS Projects — Home]]

## Related
- [[01-Brands/Cheese-To-Share/00-Brand-Core/Offers|CTS Offers]]
- [[01-Brands/Cheese-To-Share/00-Brand-Core/KPIs|CTS KPIs]]

## Objetivo
Base actualizada para **decidir el menú final** de Uber Eats. Ranking por unidades, net sales y tendencia mensual → qué se queda (hero), qué se vigila, qué se corta.

> [!warning] Lectura de los datos (leer antes de decidir)
> - **El año (Jun 2025–May 2026) es la base de ranking.** Los 4 reportes bimestrales son *subconjuntos* del año.
> - **Hay huecos:** faltan **Jun–Jul 2025** y **Abr–May 2026**. Por eso la suma de los bimestres NO cuadra con el total anual. Los bimestres sirven solo para **tendencia**, no para totales.
> - **No hay conteo real de "órdenes".** El Item Leaderboard solo da *unidades vendidas* + *net sales*. Uso **unidades como proxy de demanda**; una orden puede traer varios ítems, así que "órdenes" reales son menos. Si necesitas órdenes exactas hay que sacar el reporte de transacciones, no el de ítems.
> - **Net sales = columna Sales (USD).** %Δ del archivo anual = cambio vs. año anterior.

---

## 1. Resumen ejecutivo

- **~$6,303 net sales / ~405 unidades** en 12 meses. Ticket promedio por ítem ~**$15.60**.
- **Menú concentrado:** el **Top 5 = 59% del revenue y 57% de las unidades.** El menú se puede recortar fuerte sin tocar la facturación.
- **Postres mandan.** Bebidas son ruido (~$37 / año, <1%). Los CheeseBoards venden poco volumen pero a **$48–65** cada uno → palanca de ticket, no de volumen.
- **Cola larga muerta:** ~12 SKUs con 1 unidad o cero en el año. Ahí está el recorte.

---

## 2. Ranking anual — Top items (Jun 2025 – May 2026)

| # | Item | Net Sales | Unidades | Precio/u | %Δ vs año ant. |
|---|------|-----------|----------|----------|----------------|
| 1 | Dubai Chocolate Cake | $1,088 | 68 | $16.00 | +282% |
| 2 | Creme Brulee | $717 | 45 | $15.93 | +113% |
| 3 | Ferrero Rocher Mousse | $669 | 42 | $15.93 | +62% |
| 4 | Triple Oreo Cheesecake | $624 | 39 | $16.00 | +40% |
| 5 | 3 Leches Cake | $608 | 38 | $16.00 | +1800% |
| 6 | Guava Caramel Cake | $416 | 26 | $16.00 | +106% |
| 7 | Traditional Tiramisu | $365 | 23 | $15.87 | +660% |
| 8 | Red Velvet Duo Cake | $224 | 14 | $16.00 | nuevo |
| 9 | Basque Cheesecake | $224 | 14 | $16.00 | +50% |
| 10 | Oreo Funfetti Cheesecake | $224 | 14 | $16.00 | **−30%** |
| — | Cookies (Chocolate Chips) | $130 | 20 | $6.50 | +567% |
| — | Spiced Carrot Dream Cake | $128 | 8 | $16.00 | nuevo |
| — | Fudge Forest Cake | $112 | 7 | $16.00 | nuevo |
| — | Chocolate Cookie Cake | $96 | 6 | $16.00 | +100% |
| — | Cheese Tequeños | $84 | 6 | $14.00 | +100% |
| — | Pineapple Cake | $80 | 5 | $16.00 | nuevo |
| — | Signature Bread Bowl | $90 | 5 | $18.00 | +45% |

### CheeseBoards (rol distinto — ticket alto, bajo volumen)
| Item | Net Sales | Unidades | Precio/u |
|------|-----------|----------|----------|
| Large CheeseBoard (4-5) | $130 | 2 | $65.00 |
| Single CheeseBoard (1-2) | $108.50 | 4 | $27.13 |
| Small CheeseBoard (2-3) | $96.50 | 2 | $48.25 |

### Cola larga / bebidas (revenue marginal)
Carrot Cheesecake $16/1u · Cherry Pistachio Lemon Cheesecake $16/1u · **Pecan Caramel Cake $0/0u (muerto)** · Coke $12.50/5u · Fiji Water $7/2u · Sprite $5/2u · Diet Coke $2.50/1u · Sparkling Ice (Lemonade/Kiwi/Orange-Mango) $3.50/1u c/u · "Cookies" (genérico) $19.50/2u.

---

## 3. Tendencia mensual (unidades por bimestre)

> Solo tendencia. Faltan Jun–Jul 2025 y Abr–May 2026.

| Item | Ago–Sep 25 | Oct–Nov 25 | Dic–Ene 26 | Feb–Mar 26 | Lectura |
|------|:---:|:---:|:---:|:---:|---------|
| Dubai Chocolate Cake | 20 | 8 | 5 | 11 | #1 constante, rebote en Feb–Mar |
| Creme Brulee | 6 | 8 | 7 | 9 | **El más estable — sube parejo** |
| Ferrero Rocher Mousse | 11 | 6 | 5 | 4 | Baja sostenida ⚠️ |
| Triple Oreo Cheesecake | 12 | 4 | 1 | 12 | Volátil, rebote fuerte (+1100%) |
| 3 Leches Cake | 11 | 6 | 1 | 5 | Cae y recupera a medias |
| Guava Caramel Cake | 9 | 4 | 3 | 3 | Baja y se aplana |
| Traditional Tiramisu | 9 | 2 | 1 | 1 | **Cae duro** ⚠️ |
| Basque Cheesecake | 4 | 3 | 4 | 1 | Floja |
| Oreo Funfetti Cheesecake | 6 | 2 | 4 | 2 | Débil + YoY −30% |
| Red Velvet Duo Cake | — | — | — | 9 | **Lanzamiento fuerte** 🚀 |
| Cookies (Chocolate Chips) | 11 | 3 | 2 | 0 | Muriendo como ítem suelto |

---

## 4. Decisiones de menú

> [!success] HERO — se quedan, son la columna (Top 5 = 59% del revenue)
> **Dubai Chocolate Cake · Creme Brulee · Ferrero Rocher Mousse · Triple Oreo Cheesecake · 3 Leches Cake.**
> Foto + posición destacada en Uber Eats. Creme Brulee es el más consistente → buen "ancla" de portada.

> [!info] VIGILAR — se quedan pero bajo observación
> - **Guava Caramel Cake** — buen volumen anual, pero aplanándose.
> - **Traditional Tiramisu** — gran salto YoY pero **tendencia en caída libre** (9→1). Si no rebota en 60 días, baja a rotación.
> - **Ferrero Rocher Mousse** — top-3 anual pero **bajando cada bimestre**. Refrescar foto/posición antes de que caiga más.
> - **Red Velvet Duo Cake** — nuevo, arrancó con 9u. Darle 1 ciclo más para confirmar.
> - **Basque Cheesecake** — flojo; última oportunidad.

> [!quote] CHEESEBOARDS — se quedan por otra razón
> Volumen bajo (2–4 u) pero **$27–65 por unidad** = la palanca de ticket promedio de Uber Eats. No juzgar por unidades. Mantener y empujar como upsell / "para compartir".

> [!failure] CORTAR / CONSOLIDAR — cola larga sin tracción
> - **Pecan Caramel Cake** — 0 unidades en el año. **Quitar ya.**
> - **Oreo Funfetti Cheesecake** — único postre con YoY negativo (−30%) y tendencia débil. Cortar o reemplazar.
> - 1-dígito sin momentum: **Spiced Carrot Dream, Fudge Forest, Chocolate Cookie Cake, Pineapple Cake, Carrot Cheesecake, Cherry Pistachio Lemon Cheesecake.** Dejar máx. 1–2 como rotación estacional; el resto fuera para limpiar el menú.
> - **Bebidas:** dejar solo **Coke + agua** como attach. Quitar **Diet Coke y las 3 Sparkling Ice** (1u/año c/u = SKUs muertos).
> - **Cookies:** unificar "Cookies (Chocolate Chips)" y "Cookies" en **un solo SKU**. Vende como add-on barato ($6.50) pero como ítem suelto está muriendo → reposicionar como complemento, no plato principal.

---

## 5. Próximos pasos

| # | Acción | Dueño | Cuándo |
|---|--------|-------|--------|
| 1 | Quitar Pecan Caramel, Diet Coke, 3x Sparkling Ice del menú UE | Luis | Esta semana |
| 2 | Decidir corte/reemplazo de Oreo Funfetti + cola larga (6 SKUs) | Luis | Esta semana |
| 3 | Unificar los 2 SKUs de Cookies en uno | Luis | Esta semana |
| 4 | Subir/renovar fotos del Top 5 hero + CheeseBoards | Luis | 14 días |
| 5 | Revisar Tiramisu y Ferrero en el próximo bimestre — ¿rebote o baja? | Luis | Próx. reporte |
| 6 | Para medir órdenes reales (no solo ítems), exportar reporte de transacciones de Uber Eats | Luis | Próx. ciclo |

## 6. Fuente
- 5 CSV "sales-leaderboard-items" de Uber Eats: anual `2025-06-01_2026-05-31` + bimestrales (Ago–Sep, Oct–Nov, Dic–Ene, Feb–Mar). Item Leaderboard (no transaccional).
