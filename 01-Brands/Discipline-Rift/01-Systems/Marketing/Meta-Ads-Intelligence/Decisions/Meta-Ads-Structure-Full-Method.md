---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: playbook
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/META_ADS_ESTRUCTURA_DR_METODO_COMPLETO.md"
repo_path: domains/ads/meta/intelligence/META_ADS_ESTRUCTURA_DR_METODO_COMPLETO.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/decision
  - discipline-rift
aliases:
  - "Meta Ads Structure Full Method"
  - "Estructura DR método completo"
---

# Estructuras de campañas Meta para Discipline Rift

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Experiments|DR Meta Ads Experiments]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1A-Objective-and-Optimization-Event|Wave 1A — objetivo y evento de optimización]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget|Wave 1B — volumen y presupuesto]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2A-Campaign-Architecture|Wave 2A — arquitectura de campaña]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-3-Audience-and-Measurement|Wave 3 — audiencia, geo, atribución y medición]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-First-Decision-Synthesis|Síntesis de la primera decisión]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/META_ADS_ESTRUCTURA_DR_METODO_COMPLETO.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---
## Método completo, resultado y por qué funciona

**Fecha:** 2026-08-14
**Task:** Buscar y scrapear mejores estructuras de campañas publicitarias
**Alcance:** qué se hizo, cómo se hizo, qué se decidió, qué queda por probar
**Nivel de conocimiento del resultado:** **HIPÓTESIS DR** — defendible y ejecutable, **todavía no probada con datos de DR**

---

## 0. Lee esto primero (resumen de una página)

**Lo que se pidió:** encontrar las mejores estructuras de campañas publicitarias y cómo scrapear esa información.

**Lo que se entregó:** un sistema que responde *qué estructura debe correr DR, por qué, sobre qué evidencia, y qué la desmentiría* — con la configuración completa lista para ejecutar.

**La configuración recomendada, completa:**

| Capa | Decisión | Por qué |
|---|---|---|
| Campañas | **1** | Ningún driver obliga a más; dividir presupuesto empeora 4 de las 5 causas de "learning limited" que Meta nombra |
| Ad sets | **1** (estado actual, no un techo) | Múltiples ubicaciones caben en un solo ad set — no hace falta fragmentar |
| Presupuesto | **A nivel ad set** (mantener) | Con 1 ad set, la asignación automática de Meta no tiene nada que asignar |
| Objetivo | **CONDICIONAL — sin cerrar** | Sales→Website es la lectura actual; Leads→Website depende de requisitos que DR no ha auditado |
| Audiencia | **Advantage+ audience, Ubicación como control DURO, sin intereses** | Meta documenta qué campos obligan y cuáles solo sugieren |
| Geo | **Unión de radios cerrados alrededor de cada colegio activo, en UN ad set** | El radio mínimo por ciudad es 10 millas; por ubicación personalizada, 0.63 |
| Creativos | **Entran al ad set existente, 2–3 por ronda, en una sola ventana de cambio** | Cada adición reinicia el aprendizaje: una ronda = un reinicio, no tres |
| Evaluación | **Escalera de 5 estados; "no evaluable" es un veredicto válido** | Con el volumen actual, el anuncio individual no es una unidad legible |
| Sin gasto | **Árbol de diagnóstico de 5 ramas antes de culpar al creativo** | Meta documenta que el reparto desigual es normal — le llama "breakdown effect" |
| Atribución | **Estándar · 7 días clic · 1 día visualización** | 7 días es el **máximo que la plataforma ofrece**, no una preferencia copiada |
| Medición | **4 capas; la verdad del negocio vive en la base de datos de DR** | Meta mide publicidad, no es el libro contable |

**Lo más importante que descubrimos:** con el volumen actual de DR, **el anuncio individual no se puede leer**. Cualquier método que prometa identificar "el mejor creativo" con estos datos está vendiendo precisión falsa. El sistema está diseñado para no cometer ese error.

---

## 1. Por qué este documento reemplaza a los anteriores

Los dos MD previos adjuntos a este task eran:

| Documento anterior | Qué era | Qué le faltaba |
|---|---|---|
| `DR_ADS_INTELLIGENCE_PLAN.md` | Un **plan de construcción**: carpetas, skills, sprints, actors de Apify, sistema de scoring | Describía **el sistema que íbamos a construir**, no una decisión de negocio. Un plan no dice qué campaña correr |
| `META_ADS_INTELLIGENCE_DR_USAGE.md` | Un **manual de uso**: cómo usar lo construido, a qué archivos ir | Explicaba **cómo navegar la investigación**, no qué hacer con la cuenta |

**El problema de fondo era el mismo en los dos: describían infraestructura, no decisiones.** Un jefe que lee cualquiera de los dos termina sabiendo cómo está organizada la carpeta, pero no sabe qué estructura correr el lunes ni por qué.

**Qué hace este documento distinto:**

1. **Va de decisión en decisión, no de carpeta en carpeta.** Cada sección termina en algo ejecutable.
2. **Separa lo que Meta dice de lo que un experto opina de lo que nosotros suponemos.** Los tres se mezclaban antes; ahora cada afirmación está etiquetada.
3. **Dice explícitamente qué NO sabemos** y qué auditoría lo resuelve.
4. **Incluye cómo se cae la hipótesis.** Cada regla trae qué observación la desmentiría.
5. **No inventa números.** Donde no hay evidencia para un umbral, dice que no la hay en vez de poner una cifra que suene profesional.
6. **Cubre el sistema completo** — objetivo, arquitectura, creativos, audiencia, geo, atribución y medición — no solo la parte de estructura.

---

## 2. Cómo se hizo — paso 0 hasta el final

El trabajo se corrió en **5 olas**, cada una con una compuerta de calidad al final. Ninguna ola podía empezar sin que la anterior entregara sus supuestos por escrito.

### Paso 0 — Definir qué es DR antes de buscar nada

Antes de la primera búsqueda se fijó por escrito qué es DR **sin asumir un formato de campaña**:

> Negocio local de inscripciones deportivas juveniles — geografía limitada (Orlando), quien paga es el padre/madre, quien participa es un niño de 6–12 años, volumen publicitario bajo, resultado final = inscripción de temporada pagada.

**Por qué esto importa más de lo que parece:** la trampa clásica es etiquetar el negocio como "lead gen" o "ecommerce" al principio, porque esa etiqueta **ya decide** el objetivo de campaña antes de investigar. Se prohibió expresamente hacerlo. Cuál objetivo corresponde quedó como pregunta abierta, no como premisa.

### Paso 1 — Convertir el problema en preguntas de decisión

Se construyó un backlog de **20 preguntas numeradas** (A1–A3, B1–B3, C1–C4, D1–D4, E1–E3, G1–G2, más F y S diferidas). Cada una con: qué decisión afecta, qué evidencia existe, qué falta, y **cuándo se puede dar por cerrada**.

**Por qué:** obliga a que cada búsqueda sirva a una decisión concreta. Sin esto, "investigar Meta Ads" produce una biblioteca, no una respuesta.

### Paso 2 — Regla de parada: saturación, no cuota

Se prohibió cualquier regla del tipo "2 fuentes por pregunta". Una pregunta se cierra cuando **evidencia adicional creíble ya no cambiaría la decisión**.

**Consecuencia real:** en la última ola se cerraron 5 preguntas **con cero fuentes nuevas ingeridas**, porque la documentación de Meta ya las resolvía. Eso es un resultado correcto, no un atajo.

### Paso 3 — Jerarquía de evidencia, aplicada sin excepción

```
1. Datos reales de DR                          ← lo más fuerte
2. Documentación oficial de Meta (primera mano)
3. Comportamiento observable de competidores
4. Coincidencia entre expertos independientes
5. Opinión de un solo experto                  ← lo más débil
```

Y una regla que se aplicó en cada afirmación: **el principio y la implementación se evalúan por separado.**

> Ejemplo real: un experto dice "meter creativo nuevo a un ad set activo reinicia su aprendizaje" **(principio — Meta lo confirma)**, "por lo tanto crea un ad set nuevo por cada ronda" **(implementación — asume $1,000/día, DR no puede)**. El principio se adopta. La implementación se rechaza. Antes esto se mezclaba.

### Paso 4 — Plataforma primero, expertos después

En cada ola se leyó **primero la documentación oficial y actual de Meta**, y solo después se buscó a practicantes — y únicamente para los huecos que la plataforma dejaba abiertos.

**Por qué este orden y no al revés:** porque los expertos describen la plataforma de memoria y la plataforma cambia sin avisar. Pasó en la práctica: un artículo reciente y creíble decía que la herramienta de creative testing de Meta permite "entre 2 y 5 anuncios". La página oficial, leída el mismo día, dice **"2 a 7"**. Se marcó como `OUTDATED`, no como "equivocado" — tenía razón cuando lo escribió.

**Detalle técnico que costó resolver:** el centro de ayuda de Meta devuelve una página vacía a un fetch normal (es una app JS). Hubo que leerla con navegador renderizado. **Explícitamente se prohibió sustituir la página por el resumen de un buscador** — un resumen no es la fuente.

### Paso 5 — Las 5 olas

| Ola | Preguntas | Qué resolvió | Compuerta |
|---|---|---|---|
| **1A** | A1–A3 | Objetivo de campaña y escalera de eventos de optimización | PASS (condicional) |
| **1B** | B1–B3 | Volumen y presupuesto: qué se puede aprender y qué no | PASS |
| **2A** | C1–C4 | Arquitectura: cuántas campañas, dónde el presupuesto, separar testing/scaling | PASS |
| **2B** | D1–D4 | Método creativo: cuántos, dónde, cuándo revisar, cuándo matar | PASS |
| **3** | E1–E3, G1–G2 | Audiencia, geografía, atribución, medición | PASS |

**Cada ola fue auditada externamente y dos de ellas fueron corregidas** — ver §7. Esa es la parte del proceso que más valor generó.

### Paso 6 — Pruebas de estrés antes de cerrar

Cada ola pasó su método por escenarios de fallo antes de darlo por bueno. **76 escenarios en total** (20 + 6 + 20 + 30). No son pruebas en la cuenta real: son pruebas de lógica.

Ejemplos reales que **rompieron reglas y las forzaron a cambiar**:

- *"Han pasado 7 días y casi no hay datos"* → rompió la regla de matar por calendario.
- *"Un anuncio recibe el 90% del gasto"* → rompió la conclusión de que el otro es peor.
- *"El test A/B distingue CTR pero no hay evidencia de negocio"* → rompió la definición de "ganador".

---

## 3. Los hechos de plataforma que mandan sobre todo lo demás

Todo lo retirado de primera mano de la documentación de Meta, con fecha. **Esto no es opinión de nadie.**

### Sobre arquitectura y presupuesto
- El **objetivo de campaña no se puede cambiar** después de publicar: *"You cannot change your published campaign objective. You can always stop your campaign and create a new one."* → equivocarse cuesta la campaña entera.
- El presupuesto Advantage+ (antes CBO) está *"best suited for campaigns with at least 2 ad sets"*. Con un solo ad set, su única función documentada no tiene sobre qué actuar.
- Los criterios que Meta publica para elegir presupuesto por ad set son **todos comparaciones entre ad sets** (valor distinto, tamaños de audiencia distintos, objetivos mixtos). Con un ad set, ninguno es evaluable.
- Meta **no publica ninguna afirmación de rendimiento** a favor de un modo de presupuesto u otro.

### Sobre aprendizaje y ediciones
- Son **siempre significativos**: cualquier cambio de creativo, **agregar un anuncio nuevo al ad set**, cambio de targeting, cambio de evento de optimización, cambio de estrategia de puja.
- "~50 eventos por semana" es la descripción de cuándo *suele* estabilizarse la entrega, con las palabras *"about 50"* y *"as soon as they can deliver stably"*. **No es un umbral.**
- *"Learning limited isn't a penalty."* — textual.
- 4 de las 5 causas de "learning limited" que Meta nombra describen a DR por construcción.

### Sobre creativos y reparto de gasto
- Meta tiene una herramienta nativa de **creative testing** que corre **dentro de la campaña existente**, *"so that high-performing ads can continue to run after the test with delivery system learnings retained. There's no need to merge them into another campaign where the learnings would reset."*
- Esa herramienta **garantiza entrega** a los anuncios de prueba, y sugiere no usar más del **20% del presupuesto**.
- Y dice algo decisivo: **"A confidence level is not included."** La propia herramienta de Meta no entrega significancia estadística.
- El **"breakdown effect"** está documentado por Meta con ese nombre: *"the misinterpretation that our system shifts impressions and spending into underperforming ad sets, placements or ads."*
- Instrucción textual de Meta: **"When running multiple ads in 1 ad set, evaluate your results at the ad set level."**
- Y su propio ejemplo numérico: la ubicación con **mejor** CPA promedio ($1.10) recibió **$50**; la de peor CPA ($1.46) recibió **$450** — y eso es correcto, porque el sistema asigna por costo marginal, no por el promedio que muestra el reporte.
- *"it's normal for some ad sets or ads to deliver less than others."*

### Sobre audiencia
- **Controles (obligan):** Ubicaciones, Edad mínima, Custom audiences a **excluir**, Idiomas.
- **Sugerencias (no obligan):** Edad, Género, Segmentación detallada (intereses), Custom audiences a **incluir**. Textual: *"Suggestions don't always constrain your audience"* — y el propio ejemplo de Meta: si sugieres "Mujeres", el anuncio **puede** entregarse a hombres.
- La única puerta que rompe la ubicación tiene nombre: *"we won't target beyond your locations **unless you select Reach more people likely to respond to your ads**."*

### Sobre geografía
- La segmentación alcanza a quien **"live in, have recently spent time in or go often to"** la zona.
- Advertencia textual: **"Due to signal variations, complete accuracy cannot be guaranteed. You might see some ad impressions, or receive messages or leads from outside your location settings."**
- Radio mínimo: **ciudad = 10 millas**; **ubicación personalizada (dirección/pin) = 0.63 millas**.

### Sobre atribución
- Ventanas actualmente soportadas para conversiones web: **clic 1 o 7 días · visualización 1 día · engage 1 día**. **No existe opción de 28 días de clic.**
- Se configura **a nivel de ad set** y *"inform[s] ad delivery"* — o sea, **afecta la entrega, no solo el reporte**.

### Sobre métricas
- **Link clicks** = clics a destinos *"on or off"* Meta (incluye experiencias dentro de la plataforma).
- **Outbound clicks** = clics que **sacan** a la persona de Meta.
- **Landing page view** = clic **y** carga de página.
- Son **tres métricas distintas**, más una cuarta ("all clicks"). Mezclarlas es el error de medición más común.

---

## 4. Las decisiones, con su razón

### 4.1 Una sola campaña
Meta empuja hacia la consolidación en tres páginas distintas, pero **nunca dice que una campaña baste** — son afirmaciones diferentes y no se mezclan. Lo que sí obliga a una segunda campaña es necesitar **dos objetivos a la vez**, porque el objetivo vive a nivel campaña y no se puede cambiar. DR necesita uno.

Los dos expertos disponibles se contradicen (uno corre 4 campañas, otro 1). **No se resolvió por votación:** uno asume $1,000/día y un inventario de ganadores; el otro asume suficiente volumen de test. **DR no se parece a ninguno de los dos entornos**, así que decidió su propio volumen contra la guía de Meta.

### 4.2 Presupuesto donde ya está
**No es "ABO gana".** Es: con un ad set, la asignación entre ad sets no tiene nada que asignar, el control es idéntico, y **no hay beneficio demostrado que justifique cambiar**. Además el costo de cambiar de modo no está documentado — cambiar sin beneficio y con costo desconocido es mala apuesta.

### 4.3 Creativos al ad set existente, 2–3 por ronda
La herramienta propia de Meta mete creativo nuevo **dentro de la campaña existente** y señala mover creativo a otro lado como lo que **sí** reinicia el aprendizaje. Ese es el mejor argumento disponible y viene de la plataforma.

**Sobre el "2–3": es una hipótesis conservadora de inicio, no un óptimo probado.** La aritmética de DR (≈235–270 impresiones/semana en todo el ad set) demuestra que **ningún** número de anuncios los vuelve comparables entre sí. Por eso 2–3 se elige por diversidad y simplicidad, y se **recalcula** cuando la entrega cambie. No se defiende el número.

> **Corrección aplicada tras auditoría:** en la primera versión esto se presentó como "derivado de la capacidad", lo cual exageraba lo que la aritmética prueba. Se reetiquetó.

### 4.4 Una ronda = una ventana de cambio
Cada adición de creativo es una edición significativa. Meter 3 anuncios de a uno cuesta **3 reinicios**; meterlos juntos cuesta **1**. Meta también advierte que *"if changes are too frequent then your campaign will be constantly adapting and in flux"*.

**Honestidad requerida:** Meta **no** dice "agrupa los cambios". Eso es inferencia nuestra sobre un hecho de plataforma. Queda marcado como hipótesis DR.

### 4.5 Cuándo revisar: por evidencia, no por calendario
> **Corrección aplicada tras auditoría:** la primera versión exigía "mínimo 7 días", tomando el número de la guía de **tests A/B** de Meta. Es un mecanismo distinto. Meta **no publica** un mínimo de observación para entrega natural. Se eliminó la regla dura.

Ahora: se revisa cuando la ventana estuvo **técnicamente limpia** y hay **entrega suficiente para clasificar**. El tiempo es contexto, nunca evidencia. Una semana con 2 clics no es un creativo probado.

### 4.6 Escalera de evidencia y tipos de "matar"
Cinco estados, de "no está corriendo" a "hay evidencia de negocio". **El estado por defecto hoy es "no evaluable" — y mantener el anuncio es la acción correcta.**

Cuatro tipos de kill, separados a propósito:
- **Técnico** (roto, rechazado, URL mala) — inmediato, no necesita datos.
- **Marca/política** (rompe las reglas de claims de DR) — inmediato, no necesita datos.
- **Rendimiento dominado** — juicio del operador bajo condiciones documentadas.
- **Calidad downstream** — requiere evidencia de inscripciones; hoy no alcanzable.

> **Corrección aplicada tras auditoría:** "misma orden de magnitud de exposición" y "más de una ventana" se estaban usando como umbrales mecánicos. No hay evidencia que fije esas fronteras. Se degradaron a **condiciones que aumentan la confianza**, no a reglas que califican.

### 4.7 Sin gasto: diagnosticar antes de juzgar
Orden fijo: **¿el anuncio puede entregar?** → **¿el ad set puede entregar?** → **¿es simplemente reparto?** → **¿hay exposición suficiente para juzgar?** → **¿hace falta un test controlado?**

Con el volumen de DR, la respuesta por defecto en la rama 3 es **sí, es reparto** — que es exactamente lo que Meta documenta como normal.

> **Corrección aplicada tras auditoría:** el absoluto "nunca fuerces gasto" era demasiado fuerte. Se reemplazó por una distinción: **manipular la entrega a mano sigue rechazado** (Meta lo desaconseja explícitamente), pero **exposición controlada y financiada mediante un test diseñado es legítima** cuando la pregunta importa y DR puede pagar un test interpretable. Hoy falla la condición de presupuesto — pero es una condición que puede cambiar, no un principio eterno.

### 4.8 Audiencia: duro donde importa, suelto donde no
La geografía es la única calificación de DR que la plataforma realmente hace cumplir — y es binaria: un padre fuera del área **no puede** inscribir, por más interés que tenga.

**Los intereses se rechazan** por tres razones: no obligan por defecto, forzarlos encoge una audiencia ya pequeña (y "audiencia pequeña" es la primera causa de learning limited que Meta lista), y no hay evidencia de que ningún interés prediga una inscripción pagada.

Edad: mínimo adulto como control (quien paga es adulto). **Sin tope superior** — abuelos y tutores también compran. Género: sin restricción. Idioma: **no restringir por defecto** — Orlando tiene mucha población hispanohablante y restringir excluiría padres calificados; si el creativo es solo en inglés, esa es una decisión de cobertura, no un default de targeting.

### 4.9 Geo: radios por colegio, en un solo ad set
**El punto que lo desbloquea todo: varias ubicaciones dentro de un mismo ad set no son varios ad sets.** DR obtiene geometría por colegio sin pagar fragmentación. Por eso **no** se reabre la arquitectura.

Se rechaza Orlando ciudad completa: el piso de radio por ciudad es 10 millas y Orlando es un metro turístico de primer nivel — se compran clics baratos de gente que no puede inscribir. Se rechaza un ad set por colegio: fragmenta el presupuesto y, según la ola anterior, las unidades individuales **ni siquiera son legibles** con este volumen.

**Distinción obligatoria:** cercanía geográfica **no prueba** que el hijo asista a ese colegio. La geo es un filtro de "atendible"; la elegibilidad del colegio la carga el mensaje y la página de destino, y se verifica —si acaso— dentro del sistema de DR.

### 4.10 Atribución: 7 días de clic porque es el techo
La recomendación coincide con la convención de un experto, **pero no viene de ahí** — ese experto la enuncia sin ninguna justificación. Viene de que **7 días es la ventana de clic más larga que Meta ofrece**, y la decisión de un padre es de varios días. DR toma el máximo disponible.

**Prohibido explícitamente:** cambiar de ventana hasta que el CPA se vea bien. La ventana de entrega se elige una vez, por adelantado, con razón declarada. La comparación existe para ver **sensibilidad**, no para escoger el número más favorable.

**Declaración obligatoria:** conversiones atribuidas por Meta **≠** todas las inscripciones de DR **≠** inscripciones *causadas* por Meta.

### 4.11 Medición: 4 capas, y el libro contable es de DR
1. **Entrega** — ¿Meta puede entregar la estructura? (gasto, impresiones, alcance, frecuencia, CPM, estado de entrega)
2. **Mensaje** — ¿genera movimiento hacia el sitio? (outbound CTR sobre impresiones; **tasa de LPV sobre outbound clicks**)
3. **Respuesta calificada** — ¿son clientes plausibles? (**vive en los sistemas de DR, no en Meta**)
4. **Negocio** — inscripciones pagadas, en **la base de datos de DR**

> **Corrección aplicada durante pruebas:** un borrador dividía LPV entre *link clicks*. Está mal: link clicks incluye clics a experiencias dentro de la plataforma, así que el denominador infla. Se corrigió a **LPV ÷ outbound clicks**.

---

## 5. El árbol de diagnóstico — para qué sirve realmente todo esto

Cuando un anuncio no funciona, el equipo tiene que poder decir **por qué**. Ese es el producto final:

```
1. ¿ENTREGÓ?              no → problema de ESTRUCTURA. No culpes al mensaje.
2. ¿ENTREGÓ DENTRO DEL ÁREA ATENDIBLE?  no → problema de AUDIENCIA/configuración.
3. ¿HUBO CLICS SALIENTES Y LPV?         no → el MENSAJE es plausible (nunca probado con muestras mínimas).
4. ¿LLEGARON A LA PÁGINA CORRECTA E INICIARON INSCRIPCIÓN?
                          no → calificación del mensaje, de la audiencia, o desajuste de landing.
5. ¿SE CONVIRTIERON EN INSCRIPCIÓN PAGADA?
                          no → oferta, precio, landing, timing, UX de registro. NO culpes al targeting automáticamente.
6. ¿META LO ESTÁ ACREDITANDO?
                          → separa FALLO DE NEGOCIO de FALLO DE MEDICIÓN.
```

**Los dos casos que este árbol evita, y que antes se habrían diagnosticado mal:**
- Inscripciones en la base de DR que Meta no reporta → **es un hueco de medición, no una campaña fallida.**
- Evento en Meta sin inscripción real → **es un problema de instrumentación, no un éxito publicitario.**

---

## 6. Lo que NO se puede concluir (y por qué esto vale dinero)

| Nunca concluir | Por qué |
|---|---|
| "Ese anuncio gastó más, es el mejor" | Es el breakdown effect. Meta lo documenta con un ejemplo donde el de **mejor** CPA recibió **menos** presupuesto — correctamente |
| "Este creativo ganó" (con datos actuales) | Meta instruye evaluar **a nivel ad set** con varios anuncios; su propia herramienta no entrega nivel de confianza |
| "El targeting geo garantiza residentes" | Meta: *"complete accuracy cannot be guaranteed"* |
| "Meta reportó 3 conversiones, entonces hubo 3 inscripciones" | Atribución ≠ libro contable ≠ causalidad |
| "28 días muestra más conversiones, es más preciso" | Ni siquiera existe esa ventana de clic |
| "Cero inscripciones históricas" | Lo correcto es: **no medido** en los extractos disponibles. No es lo mismo |
| "No hay Pixel/CAPI" | Lo correcto es: **no se encontró código** en los repos inspeccionados. La cuenta real no se auditó |
| "Advantage+ baja el costo 9.7%, úsalo" | Cifra agregada de Meta sin población, geografía, escala ni diseño experimental |

---

## 7. Qué se corrigió durante el proceso (y por qué eso es la prueba de que sirve)

**Este sistema se equivocó en público y se corrigió — seis veces.** Esa capacidad es el activo, no la ausencia de errores.

| Error | Cómo se detectó | Corrección |
|---|---|---|
| "No existe palanca de calidad para embudos web" | Segunda página oficial de Meta decía lo contrario | Se reabrió una rama completa de objetivo |
| Evento calificado basado en edad/colegio del niño | Términos de Business Tools de Meta | **Bloqueado** — prohíbe datos de menores de 13 en el payload, **en el nombre del evento y en los criterios** |
| C3 decidía también el nivel de ad set | Auditoría externa | Se devolvió D1 a estado abierto — Wave 2A se estaba comiendo una pregunta que no le tocaba |
| Piso de 7 días para entrega natural | Auditoría externa | Eliminado: el número venía de la guía de tests A/B, otro mecanismo |
| "2–3 creativos" presentado como derivado | Auditoría externa | Reetiquetado como hipótesis provisional |
| "Nunca fuerces gasto" como absoluto | Auditoría externa | Reemplazado por distinción entre manipulación manual y test controlado financiado |

**Además:** dos MDs anteriores fueron rechazados y el trabajo se rehizo. Eso también está en el registro.

---

## 8. Sobre el scraping — qué se hizo y qué no

El task pedía "scrapear". Lo que se hizo:

- **99 anuncios** de 6 anunciantes (5 marcas independientes) extraídos y normalizados de la Ad Library, con evidencia cruda guardada.
- **16 páginas oficiales de Meta** leídas de primera mano con navegador renderizado, con fecha y URL cada una.
- **13 fuentes de practicantes** indexadas, **49 claims** extraídos con su cita textual.

Lo que **no** se hizo, deliberadamente:

- **No se infiere estructura de campaña de la Ad Library.** La biblioteca no publica gasto, CPA, ROAS, conversiones, presupuestos, targeting ni estructura. Deducir "esta marca usa CBO" mirando anuncios es inventar.
- **No se compraron transcripciones caras** de contenido que no cambiaba una decisión.
- **Costo total en retrieval pagado a lo largo de las 5 olas: $0.00.**

**Lo que sí sirvió del scraping de competidores:** evidencia de **mensaje**, no de estructura. 3 de 5 marcas nombran la banda de edad; 3 de 5 nombran fecha de temporada y ventana de inscripción; una nombra el colegio en el título. Eso alimenta el mensaje, no la arquitectura.

**Y una conclusión incómoda pero honesta:** la mayor parte del contenido público sobre "estructuras de campañas" es granja de SEO con números sin origen — "2–4 campañas", "8–15 creativos por ad set", "refresca cada 2–4 semanas". Se rechazó en las cuatro olas donde apareció. **Que muchos repitan la misma cifra no la convierte en evidencia.**

---

## 9. Lo que falta — y todo es auditoría de DR, no más investigación

Ninguno bloquea la ejecución. **Ninguno se resuelve leyendo más.**

| # | Auditoría | Dónde |
|---|---|---|
| 1 | ¿Existe selección "solo residentes" en la ruta de campaña de DR? | Ads Manager |
| 2 | Estado real de Pixel/CAPI — **sigue siendo DESCONOCIDO** | Events Manager |
| 3 | ¿El custom audience `DR HISTORIC` está actuando como sugerencia? | Ads Manager |
| 4 | ¿Engage-through se puede desactivar por separado? | Ads Manager |
| 5 | ¿Puede el flujo de registro capturar y guardar un identificador de campaña? | Sitio + base de datos |
| 6 | Agregar link clicks, outbound clicks, LPV y columnas de acciones al extracto | Pipeline Phase 1 |

**La #5 es la de mayor valor de todo el proyecto.** Sin ese enlace, el diagnóstico se detiene en el paso 4 y DR queda ciega después del clic.

---

## 10. Lo que DR debe probar ahora

| Hipótesis | Si es cierta | Si es falsa |
|---|---|---|
| Los controles duros de geo mantienen la entrega atendible | La geo reportada se queda en zona y los inscritos vienen de ahí | Hay entrega fuera de zona con la expansión apagada |
| El mensaje específico califica sin matar la entrega | Sube la respuesta calificada aunque baje el CTR | La entrega colapsa sin ganancia de calidad |
| Los radios por campus entregan lo suficiente | La entrega se sostiene comparada con la línea base | Se muere → ampliar radios **deliberadamente**, aceptando el costo |
| 7 días de clic captura el ciclo del padre | Las conversiones son mayormente por clic | Dominan las de visualización, o se agrupan en el día 6–7 |
| El anuncio individual no es legible hoy | Las métricas por anuncio oscilan sin orden estable | Aparece un orden estable en ≥2 ventanas |
| Agrupar cambios supera gotearlos | La entrega se estabiliza más rápido tras un cambio agrupado | No hay ventaja frente a cambios dispersos |

---

## 11. Cómo se opera esto, semana a semana

**Antes de una ronda:** campaña y ad set activos · estado de entrega limpio en todos los anuncios · la ronda anterior ya clasificada · nada más va a cambiar esta semana · oferta y landing correctas.

**Durante:** solo cambia el creativo. Se mantienen fijos presupuesto, audiencia/geo, ubicaciones, evento de optimización, estrategia de puja, landing y oferta. Todo se publica en **una** sesión.

**Después:** no editar. No agregar otro anuncio. No prender y apagar anuncios "para ayudarlos". Sí correr el diagnóstico de sin-gasto.

**Revisión:** clasificar cada anuncio en su estado. Aplicar los kills en orden. Etiquetar cada lectura **DIRECCIONAL** o **SUFICIENTEMENTE FUERTE**. **Registrar la ronda** — fecha, qué entró, qué se mantuvo fijo, entrega por anuncio, estados, decisiones y razones.

> **Ese registro es lo que construye la Mitad 2.** Sin él, cada ronda empieza de cero y DR nunca acumula su propia evidencia — que es el objetivo entero del proyecto.

---

## 12. Estado honesto del entregable

**Lo que esto es:** la mejor hipótesis inicial defendible, construida sobre mecánicas actuales de Meta verificadas de primera mano, la evidencia de operadores reales que sobrevivió al filtro, y las restricciones reales de DR.

**Lo que esto NO es:** no está probado con datos de DR. **Nada aquí es una regla operativa probada.** Ningún resultado de DR ha validado todavía una sola de estas decisiones.

**Dónde estamos:** la investigación externa fundacional está **cerrada**. Se cerró porque la última ola resolvió cinco preguntas con cero fuentes nuevas — señal de que seguir leyendo ya no mueve la decisión.

**Qué sigue:** las 6 auditorías, el enlace clic→inscripción, y correr. **La siguiente fuente de evidencia de alto valor ya no es otro experto — es Discipline Rift.**

---

### Archivos de respaldo

```
output/wave-1a-event-framework.md              objetivo y escalera de eventos
output/wave-1b-volume-budget-framework.md      volumen, presupuesto, qué se puede aprender
output/wave-2a-campaign-architecture-framework.md   arquitectura + disparadores de revisión
output/wave-2b-creative-operating-method.md    método creativo completo
output/wave-3-audience-measurement-framework.md     audiencia, geo, atribución, medición
knowledge/official-meta/                       16 documentos oficiales, fechados
knowledge/experts/                             claims con cita textual y fuerza de evidencia
knowledge/research-runs/                       registro de cada corrida, incluidos los rechazos
knowledge/research-questions.md                las 20 preguntas y su estado
```

**Regla que sostiene todo el sistema:** si una afirmación no se puede rastrear hasta una fuente verificable, no entra. Si no se sabe, dice `DESCONOCIDO` — nunca una suposición razonable.
