---
brain_note_id: "dest:meetings:8bd99673d36033bfacd570c45acd3d36"
canonical_key: "meetings/8bd99673d36033bfacd570c45acd3d36"
brand_id: "meetings"
---
# SyncUp — 2026-09-04 — DR | Executives 🏐

## Reunión

- Fecha: 2026-09-04
- Horario: 11:24:46 AM - 11:46:04 AM EDT
- Canal: DR | Executives 🏐
- Asistentes: Cristian Berrío, Luis Torres
- Video: https://t9017418223.p.clickup-attachments.com/t9017418223/446da800-cf42-4dd0-9d33-93c1e0cba9bb/446da800-cf42-4dd0-9d33-93c1e0cba9bb.mp4
- ClickUp: https://app.clickup.com/9017418223/v/dc/8cqnrff-24177/8cqnrff-36437
- Transcripción: [[02-Meetings/Transcripts/2026-09-04 SyncUp DR Executives (24177) - Transcript]]

**Notetaker**

_This note is shared with all participants for this meeting._
AI notetaker took notes for this meeting from **11:24:46 AM - 11:46:04 AM EDT**
**Meeting Channel:** DR | Executives 🏐 ([https://app.clickup.com/9017418223/chat/r/8cqnrff-9037](https://app.clickup.com/9017418223/chat/r/8cqnrff-9037))
**Attendees:** Cristian Berrío, Luis Torres
[https://t9017418223.p.clickup-attachments.com/t9017418223/446da800-cf42-4dd0-9d33-93c1e0cba9bb/446da800-cf42-4dd0-9d33-93c1e0cba9bb.mp4](https://t9017418223.p.clickup-attachments.com/t9017418223/446da800-cf42-4dd0-9d33-93c1e0cba9bb/446da800-cf42-4dd0-9d33-93c1e0cba9bb.mp4)

**Resumen general**

Reunión de sincronización operativa y técnica entre Luis y Cristian para revisar incidencias en notificaciones, accesos OEB y flujos de correos (faculty/roster). Se trataron ajustes de configuración, usabilidad del código de acceso y el diseño de una nueva función para enviar rosters por equipo desde el dashboard.

**Hallazgos clave**

*   Terminología unificada: se usó "notificación" para abarcar email y SMS.
*   Notificaciones previas al evento: estándar en 24 horas antes; reservas antiguas (de julio) permanecieron con la secuencia vieja de 1 hora, explicando la ausencia de notificación del día anterior.
*   Acceso OEB: el portal debía cerrarse completamente 6 horas después de finalizar la reservación (sin acceso indefinido).
*   Guest report: el envío se disparaba 1 hora antes de que terminara la reserva; debía confirmarse su recepción y visualización en Detalles del booking.
*   Validación del código de acceso: se acordó ignorar caracteres especiales (#, guiones) y validar por texto/números para aceptar variaciones de entrada.
*   Creación/validación de códigos desde el dashboard: se flexibilizó la estructura del reservation number (permitir letras/números) y se solicitó un código con guion y "R"; el nombre (name) aceptaba cualquier valor.
*   Función de rosters: se definió crear una función en el dashboard para enviar correos por equipo usando el template existente y dynamic fields (coaches, dirección, nombres) conectados al faculty; no se activaría un envío 100% automático.
*   Observación técnica de llamadas: posible mala configuración hacía visibles llamadas de una coach (Grace) en una cuenta distinta; se tomaría nota para revisión posterior.
*   Integración Google Workspace: comportamiento inconsistente hacía que algunos correos enviados desde el website aparecieran en el inbox de Google (y viceversa), aunque mejoraba la entregabilidad de marketing.

**Próximos pasos**

- [ ] **Cristian Berrío**: Implementar el cierre total del portal OEB 6 horas después de finalizar cada reserva.
- [ ] **Cristian Berrío**: Normalizar la validación del código de acceso para ignorar caracteres especiales y aceptar variaciones con/ sin # y guion.
- [ ] **Cristian Berrío**: Verificar en producción si se han completado guest reports reales y confirmar su visualización en Detalles del booking.
- [ ] **Cristian Berrío**: Confirmar el trigger del guest report 1 hora antes del fin y validar el flujo desde móvil y computadora.
- [ ] **Cristian Berrío**: Flexibilizar la validación del reservation number y crear el código solicitado con guion y "R".
- [ ] **Cristian Berrío**: Diseñar e implementar la función en el dashboard para enviar rosters por equipo usando el template y dynamic fields del faculty.
- [ ] **Luis Torres**: Revisar el posible solapamiento con tareas de Jassín sobre los correos del miércoles y aclarar responsabilidades.
- [ ] **Por asignar**: Diagnosticar la incidencia de visibilidad de llamadas (Grace/Doctor/Orlando) y revisar la configuración de cuentas/agencias.
- [ ] **Cristian Berrío**: Mantener a Luis actualizado por el canal acordado conforme avance en cada pendiente.

**Key Topics**

*   **Incidencia de llamadas registradas en cuentas incorrectas (Grace/Doctor/Orlando)** Problema
    *   Luis informó que Grace, una coach de Doctor, llamó al número de Doctor pero la llamada apareció registrada en la cuenta de Orlando Benvenio Gojalevo.
    *   Luis sospechó una mala configuración, posiblemente por tener su teléfono conectado a la cuenta main, lo que haría visibles sus llamadas a todas las agencias.
    *   Se acordó tomar nota y revisar la configuración para aclarar por qué todos podrían ver llamadas que le caen a Luis.

*   **Terminología y alineación sobre "notificación" (email y SMS)**
    *   Luis pidió usar el término "notificación" para evitar confusiones, ya que no solo se enviaban correos sino también mensajes de texto.
    *   Cristian confirmó que cuando se enviaba uno (correo), también se enviaba el otro (mensaje), ya que uno estaba debajo del otro en la secuencia.

*   **Fallo de notificación de 24h y explicación por cambio de secuencia (julio vs agosto)** Actualización
    *   Luis indicó que una notificación debió enviarse 24 horas antes y no se envió.
    *   Cristian explicó que en agosto se hicieron cambios para enviar con 24 horas de antelación, pero la reserva era de julio y seguía la secuencia vieja (1 hora antes).
    *   Se confirmó que, por pertenecer a la secuencia anterior, no se envió la notificación de 24 horas en ese caso.

*   **Política de acceso a la página OEB post‑reserva** Decisión
    *   Luis definió que la página de acceso no debía permanecer abierta indefinidamente después de finalizar la reservación.
    *   Se decidió cerrar todo el acceso 6 horas después de que termine la reservación (no solo quitar el código ni la sección de "how to enter").
    *   Se discutió brevemente mantener 12 horas o 24 horas, pero se fijó en 6 horas.

*   **Guest report: ubicación, funcionamiento y verificación de uso real** Actualización
    *   Cristian indicó que el guest report se veía en detalles del booking.
    *   Cristian afirmó que el flujo funcionaba en pruebas con reservas de prueba, cargando fotos desde computadora o teléfono y visualizándolas como administrador.
    *   Luis pidió revisar si algún usuario real había completado el guest report y confirmar su funcionamiento actual.
    *   Luis indicó que el guest report se enviaba 1 hora antes de terminar la reserva y acordaron dejarlo así.

*   **Mejora de usabilidad en el campo de código de acceso (variaciones con hashtag y guion)** Decisión
    *   Luis señaló que algunos usuarios copiaban el código con el hashtag o con el hyphen y la validación fallaba.
    *   Acordaron permitir variaciones ignorando caracteres especiales y validar por texto y números (caracteres normales), aceptando entradas con o sin hashtag/hyphen.
    *   Cristian propuso identificar solo el texto y los números, sin considerar caracteres especiales, para evitar confusiones.

*   **Creación de accesos desde el dashboard y formato de reservation number** Actualización
    *   Discutieron la creación de accesos desde el dashboard y dónde aparecen.
    *   El sistema exigía que los reservation numbers empezaran con OEB y guion (ej. OEB-2025).
    *   Cristian indicó que podía cambiarlo para permitir "cualquier cosa" (números o letras) y que en "name" se podía poner cualquier valor.
    *   Luis solicitó crear un código con dash y la letra "R"; Cristian comentó que ya lo había cambiado para permitir cualquier estructura.

*   **Automatización del envío de correos de faculty/roster desde el admin dashboard** Decisión
    *   Acordaron crear una función (no envío totalmente automático) para enviar rosters desde el dashboard con un botón, utilizando el template existente y dynamic fields.
    *   Se decidió enviar por equipo (no por día). El equipo debía estar conectado al faculty y tomar los correos e información de coaches, dirección, nombre, etc.
    *   Luis señaló que los correos de faculty se actualizaban cada año en la database y que ya estaban actualizados para este año, faltando un cambio.
    *   Cristian propuso que, con tal de que la información estuviera actualizada, se pudiera especificar el/los correos destino del faculty al enviar.

*   **Observaciones sobre integración con Google Workspace y visibilidad cruzada de correos** Actualización
    *   Cristian comentó que, al conectar el Workspace al website para enviar correos de marketing, algunos correos enviados por la automatización aparecían en el inbox de Google y viceversa, de forma intermitente.
    *   Indicó que esto parecía ser reciente y con bugs, observándolo en Discipline Rift y OIB.
    *   Luis destacó que esta conexión ayudaba a que correos de marketing no fueran marcados como spam.

*   **Seguimiento y coordinación operativa posterior a la reunión**
    *   Luis pidió a Cristian mantenerlo actualizado a medida que fuera abordando los pendientes tratados.
    *   Se mencionó que Luis revisaría el punto sobre si Jassín asumió el envío de todos los correos del miércoles tras el primero que mandó Cristian.
    *   Luis indicó no pasar todo por el chat de DRI sectors para el seguimiento.

_Sincronizado por Brain: 2026-10-21T01:49:36.268Z_
