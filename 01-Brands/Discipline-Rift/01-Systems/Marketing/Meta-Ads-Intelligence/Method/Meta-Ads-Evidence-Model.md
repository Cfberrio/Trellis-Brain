---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/CLAUDE.md §Knowledge levels, §Principle vs implementation, §Evidence saturation, §Transferability, §Consensus integrity"
repo_path: domains/ads/meta/intelligence/CLAUDE.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/method
  - discipline-rift
aliases:
  - "Modelo de evidencia"
  - "Meta Ads Evidence Model"
  - "Niveles de conocimiento"
---

# Modelo de evidencia — cómo se clasifica todo aquí

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Operating-Rules|Reglas de operación del dominio]] — el texto original completo
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura]]

---

> [!abstract] Para qué sirve esta nota
> Es la nota que hay que leer **antes** de citar cualquier cosa de esta carpeta. Define qué significa cada etiqueta, qué puede y qué no puede hacer cada nivel de evidencia, y por qué un experto famoso diciendo un número no convierte ese número en una regla de DR.

---

## 1. Los seis niveles de conocimiento

Toda afirmación material pertenece a **exactamente uno**. Nunca sube de nivel en silencio.

| Nivel | Qué es | Ejemplo |
|---|---|---|
| **PLATFORM FACT** | Comportamiento o documentación de Meta, de primera mano, fechado | Meta lista "Adding a new ad to your ad set" como significant edit siempre |
| **EXTERNAL PRACTITIONER CLAIM** | Recomendación o resultado reportado por alguien de fuera. Puede estar respaldado, en conflicto, desactualizado o sin validar | "Corre un CBO para testear y escalar" |
| **COMPETITOR OBSERVATION** | Algo visible en publicidad pública de un competidor. Nunca se infiere el rendimiento privado | Soccer Shots Orlando usa el encuadre de la ubicación del colegio |
| **DR HYPOTHESIS** | Algo que creemos y pensamos probar en DR. **No es un resultado** | "Nombrar el colegio del niño puede mejorar la respuesta de padres calificados" |
| **DR TEST RESULT** | Algo observado en un experimento real de DR. Guarda fecha, campaña, variable, resultado, volumen, métrica, límites y si la lectura fue direccional o suficientemente fuerte | — (todavía ninguno) |
| **DR PROVEN OPERATING RULE** | El nivel interno más alto. Requiere evidencia de DR fuerte o repetida. **Nunca se promueve tras un test pequeño** | — (todavía ninguna) |

### Las reglas que mantienen honestos los niveles

- La evidencia externa —por específica que sea— **no es prueba para DR**. Un `self_reported_case_study` sigue siendo auto-reportado mientras nadie lo verifique de forma independiente.
- **PLATFORM FACT, EXTERNAL PRACTITIONER CLAIM y COMPETITOR OBSERVATION son entradas paralelas, no peldaños.** Nada asciende de una a otra.
- El único camino de promoción es **DR HYPOTHESIS → DR TEST RESULT → DR PROVEN OPERATING RULE**, cada paso con evidencia de DR registrada. Sin saltos.
- La **degradación es normal**: una regla probada que queda contradicha por evidencia nueva de DR, o por un cambio de la plataforma, se degrada — con fecha y motivo.

> [!danger] La regla que más se rompe en la práctica
> Un experto con 1.400 cuentas diciendo "esto funciona" sigue siendo **EXTERNAL PRACTITIONER CLAIM**. Su autoridad cambia cuánto vale la pena probarlo. No cambia su nivel.

---

## 2. Los campos que lleva cada claim

Cada afirmación en las notas de expertos viene en un bloque YAML con estos campos. Esto es lo que significan:

| Campo | Qué responde |
|---|---|
| `claim` | La afirmación en una frase |
| `recommended_action` | Qué haría alguien que le cree |
| `business_type` · `spend_level` · `conversion_volume_context` | En qué tipo de cuenta se dijo. `null` = no lo declaró |
| `evidence` | La cita textual que respalda el claim |
| `evidence_basis` | De qué tipo es la evidencia: `opinion`, `self_reported_case_study`, `live_account_walkthrough`, `designed_test`, `aggregated_experiments`… |
| `evidence_basis_details` | Descripción concreta de qué se mostró realmente |
| `evidence_strength` | `none` / `weak` / `medium` / `strong` |
| `platform_validation_status` | Ver §3 |
| `research_question_ids` | Qué preguntas del backlog informa |
| `published_at` · `source_url` · `timestamp` | Trazabilidad |
| `confidence` | Qué tan segura es la lectura de lo que la persona dijo |

Y fuera del YAML, la capa de traducción a DR:

- **`applicability_to_DR`** — `high` / `medium` / `low`
- **`modification_required`** — `yes` / `no`
- **`principle_transfers`** / **`implementation_transfers`** — `yes` / `partial` / `no` / `untested`
- **`reason`** — por qué, en prosa, incluyendo qué lo desmentiría

---

## 3. `platform_validation_status` — qué califica exactamente

Califica **una sola dimensión**: si la documentación **actual de primera mano de Meta** respalda el componente de plataforma o mecanismo del claim.

`UNVALIDATED` · `SUPPORTED` · `PARTIALLY_SUPPORTED` · `CONFLICTING` · `OUTDATED` · `INSUFFICIENT_EVIDENCE` · `NOT_APPLICABLE`

- `NOT_APPLICABLE` marca afirmaciones de resultado, creatividad o estrategia que la documentación de plataforma **no puede** validar. Es una respuesta correcta, no un hueco.
- **No promueve nada.** Vive dentro del nivel EXTERNAL PRACTITIONER CLAIM y ahí se queda.
- **Historia del campo:** antes de 2026-08-13 se llamaba `validation_status` y su definición era "Meta lo respalda **o los datos de DR** lo respaldan" — que colapsaba la capa de plataforma con la capa de DR en una sola palabra. Por eso se renombró.

### Las tres dimensiones nunca se mezclan

1. **Validación de plataforma** — contra la documentación de Meta.
2. **Corroboración o conflicto entre fuentes** — contra otros practicantes, registrado en síntesis.
3. **Transferibilidad** — contra el contexto real de DR.

Un resultado de DR **no muta ninguna de las tres**. "El practicante propuso X; Meta no pudo validarlo; DR después observó Y" se queda exactamente así.

---

## 4. Principio vs implementación

Un claim de practicante casi siempre empaqueta un **mecanismo** y una **táctica**. Se evalúan por separado, siempre.

- **Principio** — el mecanismo de fondo: *"añadir creatividad a un ad set vivo reinicia su aprendizaje"*.
- **Implementación** — la táctica construida encima: *"por lo tanto lanza un ad set nuevo por cada ronda de creatividad"*.

**Un principio puede transferir a DR mientras su implementación no** — y ése ha sido con diferencia el resultado más común de todo este trabajo. Casi todo el panel razona desde presupuestos que DR no tiene.

---

## 5. Regla de umbrales numéricos

**Nunca se fuerza un número exacto cuando la evidencia no lo establece.**

Una conclusión puede ser: un rango; una regla condicional; un disparador observable de revisión; una condición mínima cualitativa; o **"no se encontró un umbral numérico defendible"**. Las cinco son respuestas honestas y completas.

Los números exactos solo se permiten con evidencia trazable. El folclore de practicantes nunca se convierte en cifra.

---

## 6. Saturación — la regla de parada

**No hay cuota de fuentes.** Nunca "2 fuentes por pregunta".

Una pregunta se cierra cuando **evidencia creíble adicional ya no cambiaría la decisión**. Algunas cierran con documentación fuerte de Meta más un caso muy comparable y ninguna contradicción creíble. Otras necesitan 3, 4 o más fuentes independientes porque los practicantes discrepan de verdad.

En la última ola se cerraron **5 preguntas con cero fuentes nuevas ingeridas**, porque la documentación de Meta ya las resolvía. Eso es un resultado correcto, no un atajo.

---

## 7. Independencia — quién cuenta como una sola voz

Gente que repite el mismo framework no son confirmaciones independientes. Los clusters registrados hoy:

| Cluster | Miembros | Cuenta como |
|---|---|---|
| Foxwell ecosystem | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Andrew-Foxwell\|Andrew Foxwell]] · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Courtney-Fritts\|Courtney Fritts]] (publica en foxwelldigital.com) | 1 voz |
| CTC / 4x400 | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Taylor-Holiday\|Taylor Holiday]] · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Andrew-Faris\|Andrew Faris]] (ex Head of Strategy de CTC) | 1 voz |
| Tier 11 / Perpetual Traffic | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Ralph-Burns\|Ralph Burns]] y sus co-presentadores | 1 voz |
| Independientes | [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Ben-Heath\|Ben Heath]] · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Jon-Loomer\|Jon Loomer]] · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Dara-Denney\|Dara Denney]] · [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Sam-Piliero\|Sam Piliero]] · otros | 1 voz cada uno |

La misma regla aplica a competidores vía `brand_family`: **KidStrong HQ y KidStrong Windermere son dos anunciantes y una marca.** Que coincidan es una marca hablando consigo misma.

**Número de anuncios no es número de marcas.** Cuando se declara consenso, se declara también cuántas familias independientes lo componen.

---

## 8. Estatus de panel — qué peso tiene cada experto

| Estatus | Qué significa |
|---|---|
| `VETTED_OPERATOR` | Demuestra operación real de cuentas (walkthroughs en vivo, tests diseñados). **No significa que estemos de acuerdo con él** |
| `SOURCE_CONTRIBUTOR` | Aporta framework o dato útil, pero el corpus no demuestra que opere cuentas de Meta. No cuenta como corroboración de operador |
| `ORGANIZATIONAL_SOURCE` | No es una persona — es una organización o vendor. Puede traer la evidencia más fuerte y a la vez un conflicto de interés declarado |
| `QUARANTINED` | Provenencia rota (p. ej. todas las fuentes sin fecha). No es un juicio sobre su capacidad; es un juicio sobre lo que podemos probar |

---

## 9. Transferibilidad a DR

**Nunca se copia a ciegas:** estrategia de ecommerce, estrategia de franquicia nacional, estrategia de competidor de deportes juveniles, mensajes de alto rendimiento / elite.

DR es: **Orlando local, quien paga es el padre, niños de 6–12, amigable para principiantes, diversión primero, liderado por coach, en el colegio después de clases.**

### La compuerta de recomendación

Una recomendación solo entra si mejora al menos uno de estos:

- calidad del setup
- calidad de tracking / señal
- condiciones de aprendizaje
- exactitud del geo
- control de placements
- claridad creativa
- ajuste oferta–mensaje

Si no mejora ninguno, se queda fuera. **Interesante no es un criterio.**

---

## 10. Reglas de Ad Library

**Permitido observar:** anunciante; estado activo/inactivo cuando se provee; creatividad; copy; hook de apertura; oferta visible; CTA; formato; destino; fecha de inicio cuando se provee; longevidad observable; variaciones activas visibles.

**Prohibido inferir** salvo que el dato lo respalde explícitamente: gasto, CPA, ROAS, conversiones, ingresos, rentabilidad, geografía de targeting, composición de audiencia, presupuesto, estructura de campaña, estructura de ad set, "el anuncio ganador".

**Nunca se llama ganador a un anuncio activo.**

**Longevidad es un proxy de priorización, no prueba de rendimiento.** Un anuncio que lleva 90 días corriendo merece inspección más cercana porque el anunciante ha seguido eligiendo correrlo. Eso es todo lo que dice. Cada salida que use longevidad debe etiquetarla como proxy **en el punto de uso** — no una vez en una nota al pie.

---

## 11. Fechas y frescura

Cada observación material conserva `captured_at`, y donde exista `published_at`, `start_date`, `first_seen`, `last_verified_at`.

Un conteo puntual de anuncios **nunca** se presenta después como valor vivo. **Ninguna estrategia sin fecha entra al playbook.**

Si algo se desconoce, es `null` — no una suposición plausible.
