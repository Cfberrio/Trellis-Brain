---
brain_note_id: "dest:meetings:89106ac19b4fe2958ed3c720c9f361ca"
canonical_key: "meetings/89106ac19b4fe2958ed3c720c9f361ca"
brand_id: "meetings"
---
# SyncUp — 2026-09-03 — DR | Executives 🏐

## Reunión

- Fecha: 2026-09-03
- Horario: 3:21:00 PM - 4:21:38 PM EDT
- Canal: DR | Executives 🏐
- Asistentes: Cristian Berrío, Luis Torres
- ClickUp: https://app.clickup.com/9017418223/v/dc/8cqnrff-24117/8cqnrff-36337
- Transcripción: [[02-Meetings/Transcripts/2026-09-03 SyncUp DR Executives (24117) - Transcript]]

**Notetaker**

_This note is shared with all participants for this meeting._
AI notetaker took notes for this meeting from **3:21:00 PM - 4:21:38 PM EDT**
**Meeting Channel:** DR | Executives 🏐 ([https://app.clickup.com/9017418223/chat/r/8cqnrff-9037](https://app.clickup.com/9017418223/chat/r/8cqnrff-9037))
**Attendees:** Cristian Berrío, Luis Torres
[https://t9017418223.p.clickup-attachments.com/t9017418223/f13ff778-382b-4aad-9f45-a9b0504cfc77/f13ff778-382b-4aad-9f45-a9b0504cfc77.mp3](https://t9017418223.p.clickup-attachments.com/t9017418223/f13ff778-382b-4aad-9f45-a9b0504cfc77/f13ff778-382b-4aad-9f45-a9b0504cfc77.mp3)

**Panorama general**

Reunión operativa para alinear automatizaciones de recordatorios (email/SMS), calendarios y comunicaciones con padres/colegios ante el inicio de temporada. También se revisaron campañas de anuncios, incidencias de telefonía/IVR y problemas con plantillas de confirmación.

**Conclusiones clave**

*   Targeting de anuncios ajustado a edad mínima 30 (rango 30–60/65).
*   Reminders críticos (7 días y 1 día) se priorizaron para eventos de “mañana” y sábado; se decidió reenvío masivo a padres afectados por el cron apagado.
*   Calendario de OEB identificado como "personal"; migración futura a calendario global para permitir multi-asignación.
*   Secuencia de recordatorios confirmada: 30 días (email), 7 días (SMS), 1 día (email+SMS), 1 hora (según configuración); caso específico ajustable de 1 hora a 1 día.
*   Necesidad de desactivar el prompt “presione una tecla para conectar” en la línea Doctor y de implementar SMS de “llamada perdida” en OIB y Doctor.
*   Plantillas de confirmación por email requieren revisión por reportes de mensajes vacíos/no visibles en móvil; se acordó reenviar confirmaciones cuando aplique (ej.: madre de Helen García).
*   Riesgo detectado: doble booking con mismo email puede sobreescribir datos y afectar la mensajería; se investigará.

**Próximos pasos**

- [ ] **Cristian Berrío**: Verificar y asegurar el envío de recordatorios de 7 días y 1 día para eventos de mañana y sábado; ajustar el caso de 1 hora → 1 día cuando corresponda.
- [ ] **Cristian Berrío**: Enviar en bulk correos a padres que no recibieron por el fallo del cron; garantizar que todos tengan reminders.
- [ ] **Cristian Berrío**: Investigar campañas caídas (09/04 y 09/05) y finalizar configuración de ads y audiencias; dejar pendiente solo los creativos.
- [ ] **Cristian Berrío**: Diagnosticar la causa de que el cron de reminders estuviera apagado e implementar corrección.
- [ ] **Cristian Berrío**: Revisar el edge case de doble booking por mismo email y su impacto en la mensajería.
- [ ] **Cristian Berrío**: Revisar/ajustar plantillas de confirmación para visibilidad móvil; reenviar confirmaciones (incluida la de la madre de Helen García).
- [ ] **Cristian Berrío**: Desactivar el feature de “presione una tecla para conectar” en la línea Doctor y configurar SMS de llamada perdida en OIB y Doctor.
- [ ] **Luis Torres**: Contactar a padres/colegios (p. ej., Moore Park) para aclarar inicio real y coordinar recogidas mientras se estabilizan los flujos.
- [ ] **Por asignar**: Planificar migración del calendario de OEB de personal a global para permitir múltiples asignados.

**Temas Clave**

*   **Calendario de OEB configurado como "personal" y limitaciones para escalamiento**
    *   Cristian explicó que el calendario de OEB era "personal", por lo que solo se pudo asignar una persona.
    *   Luis indicó que tenía sentido inicialmente porque él lo iba a manejar, pero a futuro no trabajaría en "venue" y se requeriría un calendario global.
    *   Se consideró convertirlo en un calendario global para permitir que varias personas (p. ej., Sebastián/José Sebastián) se asocien al inventario en específico.
    *   Cristian señaló que para próximas implementaciones la idea sería ponerlo global para soportar múltiples asignados por calendario.

*   **Incidente con Moore Park Elementary: padres llegaron una semana antes** Actualización
    *   Luis recibió una llamada del front desk de "Moth Park Elementary" (corregido por Cristian como "Moore Park") sobre estudiantes que llegaron para volleyball antes del inicio.
    *   Nombres tomados: Ellen (Helen) García y Rami/Remy Salamara/Salimada (mencionado con variantes).
    *   Luis confirmó que la práctica empezaba la próxima semana y se comprometió a contactar a los padres para que los recogieran.
    *   Se enviaron mensajes a los padres: "Please make sure to pick up Helen at the front desk... Practice ... does not start until next week".
    *   Posteriormente, se aclaró por teléfono con un padre que la niña estaba en "champions" y que hubo confusión por fechas; se acordó reenviar la confirmación y programar recordatorios para la próxima semana.

*   **Estado de recordatorios (reminders) y cron apagado** Problema
    *   Cristian reportó que el "cron" que decide si debe enviar correos estaba apagado; no es el que envía el correo sino el que ejecuta periódicamente la verificación.
    *   Indicó que por esa razón los reminders de "un día" estaban apagados, mientras que los "weekly", "absence" y el de "coach que no llenó la sesión" sí estaban prendidos.
    *   Cristian reactivó y verificó que "las otras sí estaban prendidas" y que "por alguna razón, los de reminders estaban apagados".
    *   Luis pidió asegurar que "los correos de los siete días" se mandaran y que se corrigiera el envío en bulk a los padres afectados por la mala configuración del log.

*   **Revisión de campañas de anuncios (ads) y segmentación por edad** Decisión
    *   Cristian copió información de bookings pasados para analizar audiencias y estaba esperando el output para decidir si crear audiencias o qué información útil ajustar.
    *   Se discutió el rango de edades: Cristian preguntó si establecer "dieciocho años en adelante" o "treinta en adelante".
    *   Luis decidió: "definitivamente, treinta"; Cristian fijó "Minimum age, treinta" y tope "treinta hasta sesenta y cinco, cincuenta"; Luis sugirió "hasta sesenta" utilizando ese gap.
    *   Luis mencionó que la cadena de la semana pasada se cayó; también la de mañana estaba caída (fechas revisadas: 09/04 y 09/05). Cristian se comprometió a investigar qué no se había mandado.

*   **Verificación de bookings y discrepancias entre logs y bandeja de entrada** Problema
    *   Luis no veía en su inbox mensajes para el booking de mañana (Jerome) y el del sábado; pidió evidencias de la conversación.
    *   Cristian revisó logs: para un caso del 05 (sábado) y el del 29/08 (Cody Woodman), los workflows aparecían "executed" en verde, incluyendo envío de "guest report" el 29 y "your event access page" el 28.
    *   Se discutió la secuencia de reminders: 30 días (email), 7 días (SMS), 1 día (email y SMS), 1 hora (posible); Luis confirmó que tenían "una hora" y "un día" y pidió ajustar si era necesario.
    *   Luis señaló que cuando el estado era "fully paid" se envió el correo pero no el SMS de 24 horas, posiblemente por aceptación tardía.
    *   Cristian planteó un edge case: un mismo contacto hizo dos bookings consecutivos; Buy Lover no crea dos contactos (un solo contacto por Gmail), lo que podría actualizar datos entre bookings y afectar mensajería; dijo que lo investigaría con "Cloth".

*   **Ajustes puntuales en secuencia de recordatorios para eventos próximos** Decisión
    *   Luis propuso cambiar el reminder de "una hora" a "un día" para un caso específico del sábado.
    *   Cristian dijo que si estaba configurado a un día, se enviaría a las 5 pm porque el booking estaba para las 6.
    *   Se acordó verificar y, de ser necesario, ajustar la configuración para asegurar envíos oportunos para mañana y el sábado.

*   **Telefonía: IVR "press any key" y SMS de llamadas perdidas** Decisión
    *   Luis pidió quitar el feature en el número de Doctor que requiere "press any key to connect" en cada llamada.
    *   Solicitó agregar en OIB y en Doctor un mensaje cuando se pierde la llamada de clientes: "sorry, missed your call, whatever, whatever" (no usar voice agent AI).
    *   Cristian indicó que en VR se había implementado antes por instrucción de Luis y que revisaría el estado actual; mencionó que en RMD decía que no estaba por el agent que nunca pierde llamadas.

*   **Problemas momentáneos de plataforma/autenticación** Problema
    *   Cristian reportó un error de "Check authentication. And network connectivity" y dudó si "Close/Cloth" se había caído; la página de estatus indicaba normalidad, pero experimentó problemas locales.
    *   Luis indicó que debía irse y no pudo profundizar en ese momento.

*   **Plantillas de confirmación por email: visualización en móvil y reenvíos** Problema
    *   Una madre informó que la confirmación que recibió estaba vacía (recibió la factura pero sin información de inicio).
    *   Luis sugirió que el formato de confirmación anterior no era visible para algunos padres; propuso resumirlo para que tenga sentido.
    *   Cristian dijo que podía verse porque se envió desde el website; revisó un envío de "Agosto treinta" en su correo, pero reconoció la queja de la madre sobre contenido vacío en su dispositivo.
    *   Se acordó reenviar la confirmación y asegurar que se envíen recordatorios para la próxima semana.

*   **Coordinación final y pendientes inmediatos** Actualización
    *   Luis pidió a Cristian enviar un mensaje con lo que faltaba para cerrar la estructura de ads; Cristian dijo que solo faltaban "Los creativos" y una "cosita" de configuración (30–40 minutos).
    *   Luis solicitó asegurar que todos los correos de mañana (incluyendo los de "siete días") se mandaran, y enviar correos en bulk a los padres que no recibieron por el fallo del cron/mala configuración del log.
    *   Se enfatizó que todos los padres debían tener reminders y estar "al día" para evitar llamadas de padres la próxima semana.

_Sincronizado por Brain: 2026-10-21T01:48:48.835Z_
