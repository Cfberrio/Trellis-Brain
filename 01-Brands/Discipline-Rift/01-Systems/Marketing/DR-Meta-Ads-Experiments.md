---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: playbook
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/experiments.md (commit 3aa367c)"
owner: Cristian
last_updated: 2026-08-13
sensitivity: internal
hub_role: leaf
---

# DR Meta Ads Experiments

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Marketing-Home|DR Marketing Home]]
- [[../Systems-Home|DR Systems Home]]

## Relacionado
- [[DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[Ad-Scripting-Playbook|DR Ad Scripting Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]] — la escalera de evaluación que usan estos experimentos
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!danger] Estado: ninguno ejecutado
> No se ha cambiado ninguna campaña, ad set, anuncio, presupuesto, targeting, placement, Pixel ni CAPI.

---

## Antes de la lista de experimentos

La última ventana medida de DR fue **$82.11 en 30 días — 1.015 impresiones, 256 reach, 10 clics de enlace**, y la campaña está **PAUSADA** con datos de hace tres meses.

> [!warning] Ningún experimento aquí puede alcanzar significancia estadística
> Diez clics al mes no separan un efecto creativo del ruido. Decir lo contrario sería inventar un rigor que esta cuenta no soporta.

Por eso están planteados como **lecturas direccionales con ventanas largas y criterios cualitativos** — la forma honesta de testear a esta escala.

### Tres compuertas aplican a todos

1. **Compuerta A — extract fresco.** Playbook decisión 1.
2. **Compuerta B — geo y `location_types` verificados.** Playbook decisión 2. Testear mensaje mientras la entrega puede incluir turistas desperdicia el test.
3. **Compuerta C — optimization event confirmado.** Playbook decisión 7. Si los landing page views no se registran, no hay métrica de éxito.

**Correr en secuencia, nunca en paralelo.** Dos cambios a la vez a este volumen da un resultado ininterpretable — exactamente el fallo que tuvo el diagnóstico anterior de DR cuando targeting y creativo cambiaron juntos.

Cada experimento es una **edición significativa** (*"Any change to ad creative"*, *"Any change to targeting"*), así que cada uno reinicia el learning phase del ad set. Ese es el costo de correr uno, y por eso son tres y no diez.

> [!note] Sobre `UNKNOWN`
> En los documentos internos, `UNKNOWN` significa que **esa información no estaba visible en el extracto** — no que algo esté roto. No tocar Pixel/CAPI por un `UNKNOWN`.

---

## E1 — Restringir la ubicación a residentes

**Prioridad: 1**

- **Pregunta:** ¿DR está pagando por alcanzar gente que está en Orlando pero no vive allí?
- **Hipótesis:** con `location_types` en el default `['home','recent']`, parte de la entrega llega a visitantes que no pueden inscribir a un hijo. Restringir a residentes concentra el mismo presupuesto en quien sí puede comprar.
- **Evidencia:** *(nivel 1)* sin clave `geo_locations` en cuatro snapshots. *(nivel 2)* Meta: *"If no `location_types` array is provided, it will default to `['home', 'recent']`"*, donde `recent` se determina por datos de dispositivo móvil. Sin input de expertos.
- **Qué cambia:** un solo ajuste — tipo de ubicación a "People living in this location".
- **Qué se mantiene controlado:** creativo, presupuesto, optimization event, placements, bid strategy, número de ad sets.
- **Métrica de éxito:** CPM y costo por landing page view vs. baseline. Secundaria y más fuerte: distribución geográfica de los leads reales (del formulario, no de Meta).
- **Ventana mínima:** 30 días de entrega activa tras relanzar, o 50 clics — lo que ocurra después.
- **Condición de parada:** revertir si el reach colapsa al punto de detener la entrega (Meta nombra *small audience size* como causa de learning limited). También parar si la auditoría muestra que ya estaba correcto — entonces no hay experimento, solo un registro corregido.
- **Riesgo:** bajo-moderado. Es el único donde el arreglo podría crear un problema nuevo.
- **applicability_to_DR:** alta — la residencia es la calificación de la oferta.

---

## E2 — Nombrar la ubicación de entrega en el creativo

**Prioridad: 2**

- **Pregunta:** ¿poner "en la escuela de tu hijo" en el anuncio mejora el engagement y el encaje post-clic?
- **Hipótesis:** el diferenciador más fuerte de DR es la conveniencia on-campus. Decirlo en el hook atrae a los padres para quienes eso decide, y repele a quienes no.
- **Evidencia:** *(nivel 3)* Soccer Shots Orlando, *"Soccer at Your Child's School! ⚽️🏫"* — **el único anuncio de 99 con la ubicación en el título**, del análogo local más cercano. **1 familia, muestra de 4 — bajo la barra de consenso**, y su rendimiento es desconocido. *(nivel 1)* la conveniencia on-campus es uno de los tres deliverables de DR.
- **Qué cambia:** solo el creativo — una variante cuyo hook nombra la entrega on-campus.
- **Qué se mantiene controlado:** targeting, geo, presupuesto, optimization event, placements, URL de destino.
- **Métrica de éxito:** CTR y tasa de landing page view vs. el creativo actual. Solo direccional.
- **Ventana mínima:** 14 días por tramo, **en secuencia** — primero baseline, luego variante. Un split en paralelo a este presupuesto mata a ambos.
- **Condición de parada:** parar si la variante no acumula impresiones suficientes en 14 días; eso es un veredicto de presupuesto, no de creativo.
- **Riesgo:** bajo. Cambio de contenido, reversible. El costo es el reinicio de learning.
- **applicability_to_DR:** alta · **modification_required:** no
- **Bloqueado por:** playbook decisión 8 — el creativo actual de DR no está capturado, así que no hay baseline registrado.

---

## E3 — Declarar el rango de edad en el copy

**Prioridad: 3**

- **Pregunta:** ¿nombrar "kids 6–12" reduce los clics mal calificados?
- **Hipótesis:** con presupuesto local pequeño, cada clic de un padre con hijo fuera de 6–12 es gasto irrecuperable. Un calificador explícito cambia volumen por calidad.
- **Evidencia:** *(nivel 3)* **3 de 5 marcas independientes** declaran el rango (i9 *"kids 5–14"*, SSS *"ages 1 to 10"*, KidStrong *"ages 1–11"*). Las tres son nacionales con rangos más amplios — la táctica transfiere, los números no. *(nivel 1)* 6–12 es un no-negociable de DR.

> [!caution] Contra-evidencia registrada
> Nick Theriot argumenta lo contrario: estrechar a quién llama el hook reduce el pool y **suprime** la entrega. A la entrega ya delgada de DR ese riesgo es real. **Este experimento testea deliberadamente algo que un experto desaconsejaría** — por eso es experimento y no adopción.

- **Qué cambia:** solo el copy — añadir el calificador de edad.
- **Qué se mantiene controlado:** todo lo demás, incluida la decisión de hook de E2, que debe resolverse antes.
- **Métrica de éxito:** tasa de landing page view y, si hay datos de leads, proporción de leads con hijo en 6–12. **Una caída de clics con subida de proporción calificada es un éxito, no un fracaso** — definirlo antes de lanzar.
- **Ventana mínima:** 21 días. Más larga que E2 porque el efecto esperado es sobre la composición del clic, no el conteo.
- **Condición de parada:** parar si impresiones o entrega caen fuerte — eso corroboraría el argumento de supresión de Nick, lo cual es en sí un hallazgo útil.
- **Riesgo:** moderado. Es el único con evidencia experta creíble apuntando al otro lado.
- **applicability_to_DR:** alta · **modification_required:** no

---

## Explícitamente NO propuestos

| No propuesto | Por qué |
|---|---|
| Restricción de placements | Meta no publica rendimiento por placement, DR tiene 10 clics, y un experto argumenta en contra |
| Test de estructura multi-campaña | DR ya está máximamente consolidada |
| Test de "packs" de creativos | Requiere financiar ad sets en paralelo |
| Test de minimum spend | El remedio puede ser una edición significativa; $5/día es ~185% del gasto diario de DR |
| Cambio de optimization event (LPV → lead) | Plausible, pero cambia la métrica de éxito de todo lo demás a media marcha. Revisar tras la compuerta C |
| Test de ventana de atribución | Meta no enumera ventanas por objetivo; a 10 clics/mes no es la restricción que ata |
| Cualquier cosa con confianza / carácter como promesa | Las reglas de claims de DR lo prohíben salvo que se mida |

---

## Resumen honesto

Tres experimentos, todos con compuertas, todos secuenciales, ninguno con poder estadístico.

> [!important] La restricción que ata no es el diseño del experimento — es el volumen
> A $2.70/día con la campaña pausada, las jugadas de mayor valor en el [[DR-Meta-Ads-Playbook|playbook]] son **auditorías** (geo, tracking, extracción), no tests.
>
> Correrlos al volumen actual produce impresiones direccionales, no evidencia. Queda dicho aquí para que nadie cite después un resultado de 10 clics como un hallazgo.
