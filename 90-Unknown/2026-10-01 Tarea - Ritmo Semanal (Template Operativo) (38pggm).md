---
brain_note_id: "dest:unknown:c7dbdc9a7f66e369fba9266e6fee30ce"
canonical_key: "unknown/c7dbdc9a7f66e369fba9266e6fee30ce"
brand_id: "unknown"
---
# Tarea: 📅 Ritmo Semanal (Template Operativo)

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The document describes a generic operational rhythm and professional development template (Ritmo Semanal) focused on decision-making, technology radars, and weekly reviews. It lacks specific references to cheese, event venues, gaming/discipline niches, or Trellis-specific core infrastructure. It appears to be a general productivity or professional growth framework.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e38pggm` · [Abrir en ClickUp](https://app.clickup.com/t/86e38pggm)

**Contenido original**

Objective
Maintain a stable weekly structure to ensure the development plan doesn't remain just an intention. This is the operational rhythm that makes everything else work.
Context
Lunes — Orientación (15 min):
Review important projects for the week. Choose: a decision requiring analysis, a point where risk exists, an opportunity to think beyond the request.

Durante la semana — Trabajo real:
Apply Problem → Outcome → Options → Risks → Business → Measurement on relevant decisions. Complete at least 1 Decision Brief.

Miércoles — Desarrollo (45 min):
Alternate weekly between: comunicación, arquitectura, sistemas, negocio, IA, estrategia. Don't try to learn everything simultaneously.

2 momentos durante la semana — Radar (20 min + 20 min):
Technology & Opportunity Radar sessions.

Viernes — Revisión (30 min):
Comunicación: ¿Qué expliqué bien? ¿Qué expliqué mal?
Criterio: ¿Dónde fui más allá de lo solicitado?
Riesgo: ¿Qué anticipé antes de que ocurriera?
IA: ¿Qué respuesta desafié?
Negocio: ¿Qué decisión conecté con una métrica?
Iniciativa: ¿Qué descubrí o propuse sin que alguien me lo pidiera?
Error: ¿Qué habría hecho diferente?

📎 Full plan: Plan de Implementación
To Keep in Mind
Minimum Viable Week (when workload is heavy): 1 Decision Brief + 1 Radar session + 1 Weekly review
This keeps the system alive without sacrificing sleep, exercise, or important responsibilities
After a minimum week, return to normal rhythm immediately
Max ~3 additional hours per week. The rest happens within real work

**Comentarios**

- **2026-09-22 · Cristian Berrío**: Revisión semana 1 (14-20 sep), tarde, viernes se corrió al lunes. Comunicación: bien lo de conclusión primero cuando lo aplico, como en el comentario reescrito de Brain (183 a 89 palabras). Mal: la grabación duró 3:06 contra meta de 2:00, por una tangente que no corté. Criterio: fui más allá pidiéndole a Luis el token de Notion sin que me lo pidiera, y proponiendo investigar la app de DR antes de aprobarla. Riesgo: anticipé el de la cuota de Codex antes de que pasara, quedó escrito en el Decision Brief y se cumplió ese mismo día. IA: cambié mi propia idea (modo ahorro al 80%) por otra (reparto por tipo de tarea) después de ver los logs, no al revés. Negocio: nada conectado a una métrica esta semana. Pendiente. Iniciativa: propuse medir mensajes sin leer >24h antes de meter plata en una app, sin que nadie lo pidiera. Error: dejé pasar el viernes sin la revisión y sin cerrar Fall closed/ongoing con Luis. Eso fue lo que rompió la rutina. Ajuste semana 2: registrar tiempo y cerrar cada task el mismo día, no acumular.
- **2026-09-28 · Cristian Berrío**: Revision semana 2 (21 al 27 sep). La hago el lunes 28, otra vez tarde. Sin grabacion esta semana, no la hice. Comunicacion: hice la sesion de reescritura que me quedo pendiente. Tome dos comentarios mios y los reescribi con la conclusion primero, quedaron a la mitad de largo. Vi que fallo de dos formas: cuando dicto la conclusion me sale al final, y cuando escribo con calma meto todo lo que hice en vez de lo que el otro necesita. Regla que me llevo: primera linea el estado, segunda lo que necesito de la otra persona. Criterio: Luis pidio el 18 herramientas para gastar menos tokens y encontre headroom por mi cuenta. Lo instale, pero cuando lo medi el proxy estaba caido y no habia ahorrado nada, y asi lo reporte en vez de decir que funcionaba. Riesgo: en el Decision Brief de la curricula vi que esperar la app de DR deja la curricula expuesta meses, y propuse una capa en Notion que cuesta $0 mientras tanto. IA: la IA me cuestiono la idea de construir el Coach Hub propio (depende de la app y no evita pantallazos). Lo acepte como paso intermedio, pero la decision final la tiene Luis y no ha respondido. Negocio: conecte el arreglo de la señal de Purchase de Meta en OEV con el ROAS. La metrica es bookings pagados en Stripe contra compras que reporta Meta. Iniciativa: Jev, un modelo que clasifica 40 a 200 veces mas rapido que un LLM. Lo conecte con los bots de SMS. No lo he probado. Error: volvi a dejar todo lo de CRIS para el final de la semana. Trabajo si hubo (18 commits en DR, 16 en OEV, 9 en el vault), pero la evidencia la arme el jueves y la revision el lunes. Ajuste semana 3: el radar y el Decision Brief los hago el dia que toca, aunque sean 15 minutos.
- **2026-09-29 · Luis Torres**: Hermano, excelente. Acuérdate de que ciertos de estos puntos tomaron más tiempo. Te recomiendo que tomes tiempo intencional fuera de tus horas de trabajo para que continúes desarrollándolos Todavía no veo ese rollo o intencionalidad fuera de horas tardes o tus horas de trabajo Apuntemos al crecimiento sustentable, paso a paso
- **2026-09-29 · Luis Torres**: @Cristian Berrío
- **2026-09-30 · Cristian Berrío**: Orientacion semana 3 (28 sep al 4 oct). La hago el martes en la noche, se me paso el lunes. La decision de la semana es el piloto de artifacts-first. La investigacion ya la tengo y encontre dos supuestos que no eran ciertos, asi que lo que falta es decidir si vale la pena probarlo y en que feature. Va a ser el Decision Brief 3. El riesgo es que el 25 de septiembre Lovable subio a main el codigo del manual enroll de DR antes que su migracion. El codigo llamaba funciones que todavia no existian en la base. Esta vez no rompio nada, pero si se repite con algo que toque pagos o inscripciones, se cae produccion. La oportunidad es headroom. Lo he venido usando y la verdad me ha funcionado bastante bien, siento que baja harto los tokens por sesion. Igual lo quiero seguir evaluando, porque todavia no tengo un numero exacto del ahorro. Esta semana lo mido con la misma tarea con y sin headroom, para tenerle una cifra y no solo la sensacion. Plan: miercoles radar tech y las 10 preguntas sobre el piloto, jueves Decision Brief y radar growth, viernes grabacion y revision.
- **2026-09-30 · Luis Torres**: Buenos dias hermano, a que te refieres con headroom?

_Sincronizado por Brain: 2026-10-01T03:16:29.326Z_
