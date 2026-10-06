---
brain_note_id: "dest:unknown:3cbd8568219bec00f115ae6820b86e94"
canonical_key: "unknown/3cbd8568219bec00f115ae6820b86e94"
brand_id: "unknown"
---
# Tarea: 💡 AIM 5: Liderazgo, Iniciativa y Technology Radar

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: Habla de varias marcas (`MULTI_BRAND`)
- reason: `The document outlines a leadership and technology radar initiative intended to be applied across all Trellis brands. It explicitly lists DR (Discipline Rift), OEV (Orlando Event Venue), CTS (Cheese To Share), and Trellis as target applications for the discoveries.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e38pggn` · [Abrir en ClickUp](https://app.clickup.com/t/86e38pggn)

**Contenido original**

Objective
Become an active source of discovery and initiative. Stop depending on "Luis encontró esto, ahora vamos a investigarlo" and start generating "Luis, encontré esto. Creo que puede resolver este problema. Estuve investigándolo y vale la pena probarlo."
Context
Technology & Opportunity Radar: Two brief sessions per week (~20 min each).

Radar A — Tecnología: AI Agents, MCP, dev tools, cloud, APIs, Supabase, Edge Functions, automation, observability, new models, new capabilities of existing tools.

Radar B — Growth/Business: Meta, Google Ads, analytics, attribution, CRM, conversion optimization, lead generation, automation, sales tools, new platform capabilities.

The Radar Filter (every discovery must pass this):

Pregunta Respuesta requerida
¿Qué es? Una oración
¿Qué problema nuestro puede resolver? Debe existir un caso real
¿Dónde podría aplicarse? DR, OEV, CTS, Trellis, otro
¿Qué estamos haciendo actualmente? Comparar vs estado actual
¿Qué ventaja introduce? Tiempo, info, revenue, eficiencia, precisión, automatización
¿Qué costo o riesgo introduce? Ser honesto
¿Podemos probarlo de forma pequeña? Sí/no/cómo
¿Qué recomiendo? Investigar / Probar / Implementar / Ignorar
Thinking pattern for discoveries:
Nueva capacidad → Problema existente → Aplicación → Beneficio → Prueba → Decisión

📎 Full plan: Plan de Implementación
To Keep in Mind
Weekly target: 1 useful discovery (worth knowing about)
Monthly target: 1 deeply investigated opportunity
Monthly stretch: 1 small experiment/pilot (when it makes sense)
Quality > quantity. Don't send links just because they're new
The MCP de Meta example: value wasn't "Meta launched an MCP." It was "now we can calculate ROAS with visibility we didn't have before"

**Comentarios**

- **2026-09-18 · Cristian Berrío**: Radar A, tecnologia, semana 1 (16 y 17 sep). Salio del trabajo real, no de una sesion aparte. Encontre que el espejo de Notion a Obsidian del Coach Hub de DR puede correr solo. Hoy lo hago a mano por MCP y me toma unas 3 horas y media por ciclo (66 paginas la ultima vez). Con un token de integracion interna de Notion, el mismo script baja a minutos y se puede programar. Que resuelve: el vault iba dos semanas atras de Notion y los coaches nuevos leen el vault, no Notion. De paso descubri que la fecha de "ultima edicion" de la base de datos miente, porque un cambio de propiedad toca las 121 filas a la vez. El reloj real esta en el header de cada pagina. Costo: cero. Riesgo: ninguno si el token vive en el .env y nunca en el repo. Prueba pequeña: token mas una corrida en seco sobre 10 paginas, comparando contra la corrida manual del 17. Media hora. Recomiendo implementarlo. Luis, necesito que me crees el token en Notion: Settings, Integrations, Internal, y me lo pases por un canal que no sea ClickUp.
- **2026-09-18 · Cristian Berrío**: Radar B, growth, semana 1 (18 sep). Sobre la app movil de DR que propuse ayer en el task de costos. Que es: empaquetar la web actual de DR como app de iPhone y Android con Capacitor, mismo backend y mismas cuentas, y agregar notificaciones push para los mensajes entre padres y coaches. Que problema resuelve: hoy un padre no se entera cuando el coach le responde, tiene que entrar al sitio. Y los coaches marcan asistencia desde el celular con mala señal. Que hacemos hoy: web responsive y avisos por email o SMS desde GHL. Sin push. Costo: USD 124 el primer año en cuentas de Apple y Google, cero en licencias. El costo real es mi tiempo, son 6 fases, y cada cambio de interfaz nativa pasa por revision de tienda. Riesgo grande que no he verificado: si el proyecto depende de render en servidor, Capacitor no lo empaqueta directo y habria que construir un cliente movil aparte. Prueba pequeña: antes de aprobar nada, medir cuantos mensajes de coach a padre quedan sin leer mas de 24 horas en Fall 2026. Si son pocos, el push no justifica la app y conviene mejorar el aviso por SMS que ya tenemos. Lo mido esta semana. Recomiendo investigar, no implementar todavia. Sin ese numero la app es bonita pero no es negocio.
- **2026-09-18 · Luis Torres**: Excelente, hermano. Me gustan estos descubrimientos. Asegúrate de hacer el checklist, esta aqui mismo @Cristian Berrío No, chequeaste la semana 1 off
- **2026-09-18 · Luis Torres**: Necesitamos herramientas para mejor uso de los tokens. @Cristian Berrío Enciende ese radar y empieza a haber contenido en base a esto
- **2026-09-24 · Cristian Berrío**: Radar A, tecnologia, semana 2. Encontre por mi cuenta un repo que se llama headroom (github.com/headroomlabs-ai/headroom) y lo instale en el computador. Es un proxy local que comprime lo que Claude lee antes de mandarlo al modelo, para gastar menos tokens por sesion. Por que me intereso: en el Decision Brief de la semana pasada vimos que el gasto de Claude y Codex es casi todo lectura, 45K tokens de entrada contra 358 de salida en una tarea normal. Esto ataca justo eso. Hoy nada lo hace, el hook de reparto solo decide quien trabaja. Ahora lo honesto: cuando lo revise hoy a las 4:45 el proxy estaba caido, cero compresiones y cero tokens ahorrados. Creo que solo funciona si abro Claude por el comando de headroom, entonces lo que senti que ahorraba todavia no lo tengo medido. Prueba: hacer la misma tarea dos veces, con y sin headroom, y comparar tokens y que el resultado salga igual. Media hora. Recomiendo probarlo antes de dejarlo fijo. El riesgo es que comprima de mas y Claude pierda un detalle de un archivo.
- **2026-09-24 · Cristian Berrío**: Radar B, growth, semana 2. Buscando novedades de IA por mi cuenta encontre Jev, de TypeSafe AI (typesafe.ai/blog/introducing-system-one-models-and-jev). Es un modelo que no escribe texto, solo devuelve decisiones: clasificar, rutear, puntuar o extraer, con la probabilidad de que tenga razon. Dicen que es entre 40 y 200 veces mas rapido que un LLM para ese tipo de pregunta. Lo conecto con los bots de SMS y Gmail de DR y OEV. Hoy Claude hace todo en un solo llamado: decide si escribe un coach o un padre, que esta pidiendo, si es lead nuevo, y ademas redacta. En agosto eran 19K tokens por mensaje. Y cuando Anthropic falla el mensaje se queda pegado, que fue lo que paso con los 16 clientes de OEV del 4 al 9 de septiembre. La idea seria que Jev clasifique en milisegundos y Claude solo entre cuando hay que redactar. En OEV serviria tambien para puntuar los leads que entran. Lo que no me convence todavia: esta en early access con lista de espera, no lo he probado, el precio no es estable (ellos mismos dicen que no pueden probar que no esta subsidiado) y es una startup que acaba de salir. Prueba: pedir acceso, tomar 50 mensajes reales de los bots que ya sabemos como clasificar y ver si acierta igual. Recomiendo investigarlo. Sin esa prueba no toco produccion.
- **2026-09-30 · Cristian Berrío**: Seguimiento de Jev. La semana pasada lo deje en "investigar", ahora ya lo estoy probando en algo real. Ya tenemos acceso, no estamos en lista de espera. Cree la API key, probe los modelos disponibles y le hice una llamada real con jev-latest. Donde lo meti: en el Brain, para clasificar a que marca pertenece un task de ClickUp (DR, OEV, CTS, Trellis, MULTI o UNKNOWN). No reemplaza el ruteo que ya tenemos. Primero sigue decidiendo el ruteo fijo por lista, folder, space, campo Brand y referencias conocidas. Solo cuando eso no resuelve entra la IA, y ahi Gemini sigue siendo la decision oficial y Jev corre en paralelo solo observando (shadow). Meetings, historial de IA y rutas fijas no pasan por Jev. Prueba manual: le pase un texto sobre actualizar el menu de catering con cheesecake vasco y opciones de tabla de quesos, y lo clasifico como cheese_to_share con confianza 1.0. La integracion shadow pasa 752 tests, 0 fallos. Lo que todavia no tengo son resultados reales. Una sola prueba manual no dice nada, y el shadow aun no esta prendido en produccion. Siguiente paso: activarlo para que junte casos reales y comparar Gemini contra Jev contra la marca correcta. Con esos numeros decido si Jev merece mas autoridad o se queda observando.

_Sincronizado por Brain: 2026-10-01T03:12:41.298Z_
