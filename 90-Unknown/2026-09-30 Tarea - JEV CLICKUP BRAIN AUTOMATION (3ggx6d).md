---
brain_note_id: "dest:unknown:67687d8e8bac2d0f942c9b8a5136ca6a"
canonical_key: "unknown/67687d8e8bac2d0f942c9b8a5136ca6a"
brand_id: "unknown"
---
# Tarea: JEV+CLICKUP BRAIN AUTOMATION

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The source title refers to a technical integration between JEV (likely a specific tool or internal acronym) and ClickUp Brain automation. There is no mention of cheese, event venues, gaming/discipline content, or core Trellis business operations to link it to a specific brand.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3ggx6d` · [Abrir en ClickUp](https://app.clickup.com/t/86e3ggx6d)

**Contenido original**

_Sin texto en el mensaje principal._

**Comentarios**

- **2026-09-29 · Cristian Berrío**: ¿Qué estamos haciendo? Estamos probando una nueva AI llamada Jev para ayudar a Trellis Brain a decidir a qué empresa pertenece una información. Ejemplo: Si entra esto: “Actualizar precios del cheesecake y los cheese boards” Trellis tiene que decidir: Esto pertenece a Cheese to Share. *** ¿Qué queremos lograr? Queremos saber si Jev puede hacer esa clasificación mejor, más rápido o más barato que la AI que usamos hoy. Hoy usamos Gemini. La idea NO es quitar Gemini de una vez. Primero queremos comparar: Gemini dice: Cheese to Share Jev dice: Cheese to Share o por ejemplo: Gemini dice: UNKNOWN Jev dice: Orlando Event Venue Así podemos ver cuál funciona mejor con casos reales. *** ¿Qué ya hicimos? Ya: Creamos acceso a Jev. Probamos la API y funcionó. Le dimos un caso real de Cheese to Share. Jev respondió correctamente cheese_to_share. Creamos el código necesario para que Trellis pueda hablar con Jev. Probamos ese código. Pasaron todos los tests. Resultado actual: 734 tests pasaron 0 tests fallaron Importante: Jev todavía NO está tomando decisiones dentro de Trellis Brain. Por ahora solo construimos y probamos la conexión. *** ¿Qué estamos haciendo ahora? El siguiente paso es poner a Jev a trabajar al lado de Gemini. Algo así: Llega una tarea ↓ Gemini la analiza ↓ Jev también la analiza ↓ Comparamos respuestas Pero: Gemini = sigue mandando Jev = solo observa Ejemplo: Task: "Update volleyball coach schedule" Gemini: discipline_rift Jev: discipline_rift Perfecto. Otro ejemplo: Task: "Venue capacity changed to 275" Gemini: UNKNOWN Jev: orlando_event_venue Guardamos esa diferencia para estudiar quién tenía razón. *** ¿Qué falta? Falta: Conectar Jev en ese modo de prueba. Dejarlo correr con casos reales. Comparar resultados. Medir: quién acierta más, quién manda menos cosas a UNKNOWN, velocidad, costo. Decidir después si Jev realmente vale la pena. *** En una frase Estamos construyendo una prueba donde Gemini sigue manejando Trellis Brain y Jev trabaja en paralelo como segundo clasificador, para comprobar con datos reales si Jev es mejor antes de darle cualquier control.
- **2026-09-29 · Cristian Berrío**: @Luis Torres
- **2026-09-29 · Luis Torres**: ¿Qué queremos lograr? Queremos saber si Jev puede hacer esa clasificación mejor, más rápido o más barato que la AI que usamos hoy. Hoy usamos Gemini. La idea NO es quitar Gemini de una vez. @Cristian Berrío hermano, acutalmente estamos usando tokens de gemini para esto?
- **2026-09-29 · Luis Torres**: avances entendidos hermano
- **2026-09-29 · Luis Torres**: Hermano por que el task esta realizado si todavia no estamos listos?

_Sincronizado por Brain: 2026-09-30T20:41:53.099Z_
