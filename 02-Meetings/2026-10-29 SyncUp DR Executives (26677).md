---
brain_note_id: "dest:meetings:e8c8f90691419f7ccedde379cd6d591a"
canonical_key: "meetings/e8c8f90691419f7ccedde379cd6d591a"
brand_id: "meetings"
---
# SyncUp — 2026-10-29 — DR | Executives 🏐

## Reunión

- Fecha: 2026-10-29
- Horario: 10:04:23 AM - 10:53:53 AM -05
- Canal: DR | Executives 🏐
- Asistentes: Cristian Berrío, Luis Torres
- ClickUp: https://app.clickup.com/9017418223/v/dc/8cqnrff-26677/8cqnrff-39957
- Transcripción: [[02-Meetings/Transcripts/2026-10-29 SyncUp DR Executives (26677) - Transcript]]

**Notetaker**

_This note is shared with all participants for this meeting._
AI notetaker took notes for this meeting from **10:04:23 AM - 10:53:53 AM -05**
**Meeting Channel:** DR | Executives 🏐 ([https://app.clickup.com/9017418223/chat/r/8cqnrff-9037](https://app.clickup.com/9017418223/chat/r/8cqnrff-9037))
**Attendees:** Cristian Berrío, Luis Torres
[https://t9017418223.p.clickup-attachments.com/t9017418223/a70fdcd9-a846-40ab-be85-034f49d97f4a/a70fdcd9-a846-40ab-be85-034f49d97f4a.mp3](https://t9017418223.p.clickup-attachments.com/t9017418223/a70fdcd9-a846-40ab-be85-034f49d97f4a/a70fdcd9-a846-40ab-be85-034f49d97f4a.mp3)

**Resumen**

Reunión enfocada en la app móvil de Discipline Rift (iOS/Android) para alinear UX del admin en móvil y rediseñar la mensajería/notificaciones tipo WhatsApp. Se definió el plan para migrar comunicaciones de correos/SMS a notificaciones in‑app desde la perspectiva del coach y una campaña de adopción para que padres instalen la app.

**Conclusiones Clave**

*   Notificaciones push estilo WhatsApp: mostrar nombre del entrenador, nombre del equipo/escuela (grupo) y preview del mensaje con límite de caracteres; historial persistente en el mismo hilo de chat (sin inbox separado).
*   Reminders de temporada (30/7/1 días) y correos semanales convertidos a mensajes in‑app redactados desde el POV del coach usando terminología basada en Notion; branding y entrega dentro del hilo de mensajería de equipos.
*   Campaña de adopción tras lanzamiento Android: emails día 1, 3 y 6; SMS día 9 a no‑instalados; email “last chance” día 12; medir % de padres con app instalada y logueada.
*   Política con umbral del 70% de padres en la app: eliminar correos semanales y moverlos a mensajes del coach un día antes de cada práctica; mantener correos de 7 y 1 días y apagar el de 30 días (ajustado durante la reunión).
*   Aprobación Android aún pendiente; en iOS se probarían cambios en dispositivo vía Xcode antes de publicar.
*   Para contenido semanal por deporte: preferencia por plantillas por deporte (aprox. 18) en vez de una solución compleja con dynamic fields y BD de terminología.
*   Incorporar fotos de entrenadores desde Trailish Hub/DocuSign en perfiles y permitir que el coach las cambie.
*   Reducir costos al sustituir miles de correos por notificaciones in‑app.
*   Explorar edición de contenido tipo Notion dentro del admin y posibles updates vía Cloud/MCP; requiere propuesta técnica posterior.
*   Riesgos: demora de aprobación Android; complejidad de dynamic fields; control de costos en automatizaciones (Playwright) con límites y flags.

**Próximos Pasos**

- [ ] **Cristian Berrío**: Definir y maquetar notificaciones push tipo WhatsApp (estructura, límites y registro en chat).
- [ ] **Cristian Berrío**: Convertir correos de 30/7/1 días y semanales a mensajes in‑app desde el POV del coach usando Notion como base de contenido.
- [ ] **Cristian Berrío**: Extraer el árbol completo de comunicaciones (carpeta Whisper/DisciplineReft) y consolidarlo.
- [ ] **Cristian Berrío**: Testear en iPhone con Xcode y publicar cambios cuando sean verificados.
- [ ] **Cristian Berrío**: Revisar recategorización automática en la carpeta Multimarca.
- [ ] **Cristian Berrío**: Implementar fotos de coaches desde Trailish Hub/DocuSign y permitir edición por el coach.
- [ ] **Cristian Berrío**: Proponer solución para edición de contenido tipo Notion en el admin con posibilidad de updates vía Cloud/MCP.
- [ ] **Cristian Berrío**: Preparar propuesta de plantillas semanales por deporte (≈18) y presentar para decidir vs. dynamic fields.
- [ ] **Cristian Berrío**: Crear SOP para reservas con Playwright, con tope de $50 y flag si excede; documentar en MD y ubicarlo en el espacio indicado.
- [ ] **Luis Torres**: Validar la secuencia de adopción (D1, D3, D6 emails; D9 SMS; D12 email) y el criterio de medición del 70%.
- [ ] **Luis Torres**: Enviar el zip con la foto faltante de coach (Dalila) si no está en Trailish Hub.
- [ ] **Luis Torres**: Confirmar el apagado de la segunda ronda de notificaciones por correo y las políticas de 30/7/1 y weekly según el 70%.

**Key Topics**

*   **Problema actual del admin en móvil y objetivos de UX** Problema
    *   Luis describió que desde el teléfono el admin no podía ver la semana, equipos ni resolver consultas rápidas; necesitó ver métricas de mensajes de coaches, buscar jugadores y revisar mensajería entre coaches y padres.
    *   Cristian confirmó el problema y explicó que la app guardaría metadata local (no "cookies") tras la primera apertura para facilitar acceso, incluso con señal limitada.
    *   Se acordó priorizar practicidad: acceso rápido a lo esencial sin múltiples pasos; enfoque en flujos urgentes y puntuales desde el móvil.

*   **Diseño de notificaciones y mensajería estilo WhatsApp** Decisión
    *   Luis pidió que las notificaciones imitaran WhatsApp: mostrar nombre del entrenador, nombre del grupo (escuela/equipo) y un preview del mensaje con límite de caracteres.
    *   Se acordó que las notificaciones fueran simples y cortas; si el texto es corto que se vea completo, si es largo que se corte como en WhatsApp.
    *   Cristian y Luis acordaron no crear un inbox separado; los mensajes y notificaciones quedarían en el mismo hilo de mensajería donde se ven equipos/entrenadores, con registro histórico similar a WhatsApp.

*   **Remitente y POV de los reminders en la app** Decisión
    *   Se decidió simular que los reminders son enviados por el coach, no por "Discipline Rift".
    *   Luis indicó que habría que reescribir los correos/reminders para que sonaran como escritos por el coach, muy precisos y entendibles de un vistazo.
    *   Cristian validó que el chat de "Discipline Rift" o del coach conservaría el historial de toda la mensajería.

*   **Conversión de correos existentes a notificaciones in‑app** Actualización
    *   Luis indicó que se extraería todo el contenido de comunicaciones actuales y se transformaría a notificaciones de app manteniendo la misma secuencia (30, 7 y 1 día) pero con formato de mensaje in‑app.
    *   Se usaría Opus para adaptar el wording de los correos a mensajes de app y Notion como fuente de conocimiento para terminología; Cristian entregaría las notificaciones resultantes.
    *   Se usarían campos dinámicos (dynamic fields) para personalizar mensajes (ej.: temporada, coach, etc.).

*   **Campaña de adopción de la app para padres tras lanzamiento en Android** Decisión
    *   Android seguía sin respuesta de aprobación; no se había aprobado ni negado.
    *   Plan de emails/SMS una vez lanzado Android: tres correos en día 1, día 3 y día 6; a quienes no descarguen la app, SMS en día 9; luego email "last chance" en día 12.
    *   Se mediría si más del 70% de padres tenían la aplicación descargada y logueados; con ese umbral se ajustarían/pausarían correos de temporada y se migrarían comunicaciones a app.

*   **Política de apagado/ajuste de correos según umbral del 70%** Decisión
    *   Versión inicial discutida: al alcanzar ≥70% se apagarían correos de 30, 7 y 1 día dejando solo 1 día; luego Luis ajustó: apagar solo el de 30 días y dejar 7 y 1 por correo.
    *   Se decidió eliminar por completo los weekly emails si se alcanza el 70%, reemplazándolos por mensajes del coach un día antes de cada práctica, adaptando el contenido existente por práctica (ej.: práctica 1, práctica 6).
    *   Objetivo declarado: reducir gastos eliminando miles de correos por temporada (mención aproximada de “como dos mil quinientos correos”).

*   **Fotos de entrenadores en perfiles y capacidad de edición** Decisión
    *   Luis pidió usar las fotos de entrenadores almacenadas en Trailish Hub y DocuSign (mencionó a Dalila) para poblar perfiles.
    *   Se acordó permitir que los coaches pudieran cambiar su foto de perfil desde la app.
    *   Luis se comprometió a enviar un zip del entrenador faltante si no estaba en Trailish Hub.

*   **Recategorización automática en carpeta Multimarca** Actualización
    *   Luis preguntó por la recategorización de lo que estaba en "Multimarca".
    *   Cristian indicó que debía recategorizarse solo; no lo había revisado desde la semana pasada y se comprometió a verificar el estado.

*   **Cambio de host a computadora Windows para reducir fricción** Decisión
    *   Luis propuso cambiar a una computadora Windows recién comprada como host para que Cristian no tuviera tantos inconvenientes.
    *   Cristian indicó que habría que cambiar varias cosas, pero que sí era una solución.

*   **Extracción de árbol de comunicaciones y organización** Decisión
    *   Luis pidió: "Copy what folder. Whisper. Pull all of the information regarding communication sequences. For automated emails for DisciplineReft. Should be one whole tree communications."
    *   Cristian aceptó la solicitud.

*   **Estado de publicación y testing de la app (iOS/Android)** Actualización
    *   Android: Cristian revisó ese día y no vio novedades de aprobación.
    *   iOS: Cristian explicó su flujo de testing con Xcode conectando su celular para verificar cambios antes de montar; estimó que cambios pequeños no deberían demorar más de un día en revisión la primera vez.
    *   Cristian aplicó cambios basados en una auditoría de “Facebook” y otras mejoras UI (impulsar uso de la aplicación, avisos de asistencia/no asistencia).

*   **Edición de contenido tipo Notion dentro del admin y actualización vía Cloud** Idea
    *   Luis pidió poder editar/crear/mover módulos, páginas, títulos y texto en el admin con funciones parecidas a Notion, y ojalá actualizarlo con Cloud como ya hace con Notion y MCP.
    *   Cristian consideró opciones: edición fuera del main dashboard, acceso al repositorio para cambios de contenido, y publicación por su parte; solicitó tiempo para pensar la solución apropiada.
    *   Luis pidió que Cristian se "piense" la solución y luego proponga cómo desarrollarla.

*   **Plantillas por deporte vs. Dynamic Fields para weekly** Decisión
    *   Luis propuso usar dynamic fields asociados a deportes y habilidades (ej.: en fútbol "pase" y en tenis "derecha") para personalizar semanalmente.
    *   Cristian explicó que hacerlo por dynamic fields requeriría una tabla/BD de terminología y mayor complejidad; sugirió manejarlo por plantillas por deporte como antes, estimando 18 plantillas/mensajes inteligentes.
    *   Se acordó que Cristian sacaría mensajes propuestos y, con base en eso, Luis decidiría si aplicar por deporte o explorar dynamic fields.

*   **SOP y automatización con Playwright para reservas con límite de costo** Decisión
    *   Luis solicitó un "exit ticket" confirmando si era posible con Playwright y crear un SOP basado en lo hecho por Yassin.
    *   Se estableció un límite de costo: la reservación no debería pasar de 50 dólares; si lo excede, se debe flaggear y no mandar el pago; documentar instrucciones en MD para futuras reservaciones.
    *   Cristian expresó preocupación por un comentario previo de Yassin sobre un costo de 1,000 dólares; ambos acordaron mitigarlo con las instrucciones y el tope.

*   **Apagado de segunda ronda de notificaciones por correo** Actualización
    *   Luis preguntó si Cristian había apagado la función de correos que enviaba un segundo correo si los padres no respondían; Cristian confirmó que la segunda ronda estaba apagada y que ahora enviaban uno por día, no totalmente apagado.
    *   Se acordó mantener apagada la segunda ronda automática mientras se implementaba la estrategia nueva.

_Sincronizado por Brain: 2026-10-29T19:03:30.405Z_
