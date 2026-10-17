---
brain_note_id: "dest:meetings:b111f20c6d6626cbe741e8686539d2d8"
canonical_key: "meetings/b111f20c6d6626cbe741e8686539d2d8"
brand_id: "meetings"
---
# Meeting — 2026-05-26

## Reunión

- Fecha: 2026-05-26
- Asistentes: Trellis Fields, CV Capital Investment Group LLC, Trellis Fields
- Video: https://t9017418223.p.clickup-attachments.com/t9017418223/2bd007da-3a26-497a-b9a4-00284658c40c/2bd007da-3a26-497a-b9a4-00284658c40c.mp4?view=open&filename=2nd%20Block%20-%20RenewalOS%20Meeting%20-%2005-26-2026.mp4
- ClickUp: https://app.clickup.com/9017418223/v/dc/8cqnrff-18877/8cqnrff-24497
- Transcripción: [[02-Meetings/Transcripts/2026-05-26 Meeting 2nd Block - RenewalOS Meeting - 05 26 2026 (18877) - Transcript]]

**Notetaker**

**Attendees:** Trellis Fields, CV Capital Investment Group LLC, Trellis Fields
[https://t9017418223.p.clickup-attachments.com/t9017418223/2bd007da-3a26-497a-b9a4-00284658c40c/2bd007da-3a26-497a-b9a4-00284658c40c.mp4?view=open&filename=2nd%20Block%20-%20RenewalOS%20Meeting%20-%2005-26-2026.mp4](https://t9017418223.p.clickup-attachments.com/t9017418223/2bd007da-3a26-497a-b9a4-00284658c40c/2bd007da-3a26-497a-b9a4-00284658c40c.mp4?view=open&filename=2nd%20Block%20-%20RenewalOS%20Meeting%20-%2005-26-2026.mp4)

**Visión General**

La reunión se centró en planificar el desarrollo de un MVP para una plataforma de gestión de pólizas en el sector inmobiliario, haciendo énfasis en la automatización de recordatorios de renovación y la extracción de datos mediante OCR. Se analizaron los flujos de trabajo, la diferenciación entre interfaces web y móvil, y la necesidad de centralizar la documentación y comunicación en herramientas colaborativas.

**Conclusiones Clave**

*   Se acordó enfocar el MVP en la automatización de recordatorios de renovación y en la extracción de datos de pólizas utilizando OCR.
*   Se decidió implementar una estructura en forma de árbol genealógico para gestionar la relación entre pólizas maestras y subpólizas.
*   Se definió diferenciar las funcionalidades de la interfaz web (para administración intensiva) y la móvil (para acceso rápido y práctico por parte de los usuarios).
*   Se estableció la importancia de centralizar la documentación y la comunicación del proyecto a través de plataformas como ClickUp y Obsidian.

**Próximos Pasos**

- [ ] **Cris**: Documentar ejemplos prácticos y flujos de trabajo relacionados con la renovación y carga de pólizas en ClickUp y Obsidian.
- [ ] **Luis**: Configurar y organizar la infraestructura colaborativa en ClickUp para centralizar notas, flujos y la comunicación del proyecto.
- [ ] **Trellis Fields**: Coordinar la definición de roles, accesos y permisos diferenciados para la interfaz web y móvil, abarcando usuarios, brokers y administradores.
- [ ] **Por Asignar**: Establecer un canal central de comunicación (similar a Discord o Telegram) dentro de ClickUp para facilitar la coordinación del equipo.
- [ ] **Cris**: Evaluar y proponer el método óptimo para la carga de pólizas (PDF versus fotografía) y la integración del proceso de OCR en la plataforma.

**Sujets Clés**

*   **Acceso a la plataforma y enlaces compartidos**
    *   Se verificó quién tenía acceso al sistema y se compartieron enlaces para acceso (por ejemplo, link enviado previamente).
    *   Se discutió brevemente la incorporación de nuevas personas a la plataforma, resaltando que en ese momento no había muchos usuarios en espera.

*   **Definición de la solución para el seguimiento y renovación de pólizas** Decisión
    *   Se destacó que el problema central es la gestión de propiedades a escala, donde el seguimiento de pólizas (con diferentes fechas de expiración y coberturas) se vuelve complejo.
    *   Se propuso concentrar el MVP en automatizar los recordatorios de renovación (por ejemplo, notificar 30, 60 o 90 días antes de la expiración).
    *   Se discutió la importancia de incluir un flujo que recoja solicitudes (quotes) a proveedores de seguros basándose en la información extraída de las pólizas.
    *   Se definió el enfoque de la solución sobre el problema de 'tracking' y la gestión de ciclos de pólizas, incluyendo desde pólizas generales hasta pólizas específicas de flood, riesgos y errores/omisiones.

*   **Uso de tecnología OCR y automatización en la extracción de datos** Idea
    *   Se planteó implementar OCR para extraer información crítica de las pólizas, ya sean en formato PDF o mediante fotografías.
    *   La extracción incluiría datos como fecha de expiración, coberturas, deducibles y dirección, lo cual servirá para activar la cadena de eventos para solicitudes de cotización a aseguradoras.
    *   El OCR se evaluará mediante testing para asegurar la calidad de los datos extraídos.

*   **Estructura lógica de la solución y modelado de pólizas** Idea
    *   Se propuso el uso de un 'árbol genealógico' para organizar las pólizas, donde una póliza 'maestra' se desglosa en subpólizas (o 'nietos') según distintas variables y necesidades.
    *   La estructura permitirá manejar múltiples pólizas por propiedad, considerando relaciones jerárquicas para identificar oportunidades de mejorar cobertura y reducir deducibles mediante solicitudes automatizadas.

*   **Diferenciación de interfaces: Web vs Móvil** Decisión
    *   Se analizó que la aplicación deberá contar con versiones web y móvil.
    *   La interfaz web se orientará a la administración intensiva (dashboard de propiedades, manejo de múltiples pólizas, funciones avanzadas), mientras que la versión móvil será para accesos rápidos y funciones básicas, como consultar pólizas o enviar solicitudes rápidas.
    *   Se consideró que ciertos roles y escenarios, como la necesidad de enviar documentación (por ejemplo, PDF de una póliza), se facilitarán en ambas plataformas pero con funcionalidades diferenciadas.

*   **Definición de roles y permisos de usuario** Decisión
    *   Se discutió la estructura de usuarios basada en la entidad 'propiedad' donde múltiples actores (por ejemplo, miembros de un núcleo familiar o colaboradores de una oficina) podrán tener acceso y roles diferenciados.
    *   Se definió que los brokers y proveedores de seguros tendrán accesos limitados principalmente para comunicación y solicitudes de cotización, mientras que los administradores y clientes accederán a funcionalidades más avanzadas.
    *   La estrategia apunta a unificar la comunicación en un solo canal para evitar duplicidad de mensajes.

*   **Uso de herramientas colaborativas para documentación y comunicación** Decisión
    *   Se acordó centralizar la documentación del proyecto y los flujos de trabajo usando herramientas como ClickUp y Obsidian.
    *   Se destacó el uso de voice memos que se transcriban y se almacenen para tener un registro confiable de escenarios, ideas y problemas planteados.
    *   El plan incluye establecer canales de comunicación (similares a Discord o Telegram) dentro de ClickUp para facilitar la interacción continua del equipo.

*   **Próximos pasos y acciones inmediatas** Actualización
    *   Se estableció la necesidad de configurar la infraestructura colaborativa (crear cuentas en ClickUp y centralizar la data en Obsidian).
    *   Se instó a los participantes, en particular a los desarrolladores, a documentar ejemplos y flujos de trabajo reales relacionados con pólizas para afinar la lógica del sistema.
    *   Se acordó mantener una comunicación directa a través de coordinadores (ej. Luis) que permita resolver dudas y ajustar detalles según surjan nuevos requerimientos o bloqueos técnicos.

*   Transcript

    **Trellis Fields:** Debería estar ahí también, no sé qué más está esperando en el middle room le dejaba

    **CV Capital Investment Group LLC:** Actualmente

    **Trellis Fields:** un Cristian por ahí.

    **CV Capital Investment Group LLC:** nadie. Si quiere mándale el link, pero actualmente no tengo nadie esperando.

    **Trellis Fields:** ¿No tienes un Trallis tampoco?

    **CV Capital Investment Group LLC:** Tengo a María, pero no tengo. No tengo más nadie. El ClickUp no tengo ningún tres. Tengo Trellis Fields, pero eso ya parece que se añadió, ¿No?

    **Trellis Fields:** No, yo.

    **CV Capital Investment Group LLC:** ¿Cuál es el email?

    **Trellis Fields:** Ya tiene el link, lo que pasa

    **CV Capital Investment Group LLC:** Ya

    **Trellis Fields:** es que creo

    **CV Capital Investment Group LLC:** lo

    **Trellis Fields:** que

    **CV Capital Investment Group LLC:** tiene.

    **Trellis Fields:** iba el anterior y no sé qué fue lo que hizo,

    **CV Capital Investment Group LLC:** Chévere.

    **Trellis Fields:** pero ya tiene el link y en realidad está nuestro calendario, no sé por qué no lo consigo.

    **CV Capital Investment Group LLC:** En cuanto a la comunicación, déjame ver quién ya vino aquí.

    **Trellis Fields:** Mira, la comunicación debemos trabajarla en base a el plan de trabajo que tú estás proponiendo para Renew os y a lo cual ya estamos en acuerdo con ese plan de trabajo. Puede cambiar en cualquier momento, o sea, el open agreement puede cambiar porque en realidad estamos enmarcando todo esto, todo esto junto, o sea, contarle todo, estemos de acuerdo y todo esto, o sea, no quiere que esto no está set in stone, pero sí me gustaría que trabajemos en el orden que ya está establecido en lo que ya tenemos. Entonces a nivel de comunicación, todo lo que tenga que ver con los recursos que tú vayas a necesitar de parte de Trellis, ya sea branding, estrategia de marketing, posicionamiento, etc. Todo ese flow en el cual podemos desarrollar, porque ya lo como te digo, ya nosotros eso es lo que hacemos para las marcas actualmente. Lo que yo propongo es que Trellis sea contratado por Renew os y que Trellis directamente y en ese caso Moche. En este caso sí, Moche sería la persona. ¿Cris, estás por ahí?

    **CV Capital Investment Group LLC:** No, todavía tengo Amarilla en espera, pero.

    **Trellis Fields:** Cris, Aquí te presento a. ¿Bueno, Cris, Cris, los dos se llaman Cris? ¿Bueno, Christopher y Cristian está por ahí Cris? Brutal. Bueno, Cris es nuestro developer, yo siempre estoy hablando de cosas de development y con Chris es que me doy esas travesías curiosas, creativas y nada, Cristofer es nuestro querido socio.

    **CV Capital Investment Group LLC:** Saludos, Cristian, un placer.

    **Trellis Fields:** Un placer. ¿Ya empezaron hace rato? Acaban de empezar,

    **CV Capital Investment Group LLC:** No, bueno, empezamos hace un ratito, pero estábamos hablando de cosas que, por ejemplo, que están esperando de mí para poder desarrollar el. Para que tú puedas comenzar a desarrollar lo que sería un buen MVP Y nada, yo voy a estar trabajando con ese tipo de cosas. ¿Qué otro tipo de información, Luis, tú crees que Chris necesitaría de mi parte para?

    **Trellis Fields:** Bueno, estamos hablando de que el MVP se va a basar en una solución. Me gustaría que Cris le des la mayor cantidad, o sea, le des un pitch de un minuto de qué se trata de la solución que estamos creando, por qué estamos haciéndolo, o sea, cuál es el problema, cuál es la solución a nivel de industria, qué es lo que la industria ahorita está necesitando y donde nosotros construimos ese puente para que ellos lleguen y luego de eso podemos entrar en como que ya en específicas, en cosas específicas de mentalidad. Pienso que claramente Cris no es, Cristian no es un experto en bienes raíces, entonces es importante que nosotros tenemos más experiencia porque lo hemos trabajado, lo hemos manejado, pero es importante que a nivel de equipo todo esto quede claro. Ten en mente que entre más contexto información tú das ahorita, más esto nos va a permitir desarrollar más rápido a futuro, ya que esto está siendo grabado por nuestras herramientas de ClickUp y vamos a poder agarrar cada palabra que tú digas. Entonces entre más contexto información tú puedas utilizar, ya podemos documentizar esta parte y podemos aclimatizar a cualquiera que trabaje en este concepto hacia esto. Es más, esto puede hasta funcionar para un appetizer para nuestro equipo de Terelu cuando empecemos a trabajar con ellos.

    **CV Capital Investment Group LLC:** Perfecto. Pues mira, Cristian, me llamo Christopher, como te acaba de comentar Luis. Un poquito sobre mí. Vengo de Puerto Rico, comencé en bienes raíces en el 2020 y después de eso comencé a trabajar con un inversionista, un inversionista que tiene muchas propiedades aquí en la Florida. Y básicamente, después de varios años trabajando con él, para él entendimos y él vino a mí con un problema. Y viene siendo que una vez tienes una cierta cantidad de propiedades, puede ser cincuenta, ciento cincuenta, seiscientos, mil, todas las personas parecen tener el mismo problema que viene siendo trackear la cantidad de pólizas que tienen para cada propiedad, ya que hay propiedades que cuentan con más de una póliza. Está la póliza de asegurar la propiedad, está la póliza de liability en caso de que suceda algo de flood, dependiendo si está en una zona inundable y X. Cada propiedad puede tener muchas pólizas.

    **Trellis Fields:** Fíjate que la póliza general de la propiedad y es una póliza que tú utilizarías, por ejemplo, esa póliza tiene un valor de construcción de casa. Quiere decir que si la casa viene un meteorito y le cae a la casa y la destruye por completo, el seguro está en esos casos extremos. Eso es lo que yo entiendo Cris, o sea, yo no soy el industry expert, lo que estoy agarrando información y traduciéndolo un poco, corrígeme si es necesario y estoy llevando la información a la información de lanuage totalmente no está

    **CV Capital Investment Group LLC:** Mira, para ponerlo

    **Trellis Fields:** con esto.

    **CV Capital Investment Group LLC:** más simple, vamos a hablar de un tipo de pólizas que todos conocemos, que son las pólizas médicas. Funciona básicamente de manera igual. Tú pagas una mensualidad, tienes una cobertura y esa cobertura, pues a veces tienes un deducible, a veces no. Eso es algo que se puede. Todo en esta póliza, al igual que la médica, puede ser customizado al momento en el que la póliza se pide. Mira, yo quiero que mi deducible para huracanes, que son bastante común aquí en la Florida, que mi deducible para huracanes no pase de 5 mil dólares. Ahí es donde. Entonces, una vez tú llegas a ese deducible, ahí es donde el seguro está supuesto a reemplazar, por ejemplo, el techo, si es necesario reemplazarlo. Entonces, todas estas pólizas funcionan de manera muy similar a una médica, a una póliza de un carro. Creo que no son comunes en Colombia, pero aquí en Florida, por ejemplo, lo son. Tienes un deducible y si chocas a alguien y el arreglo no sobrepasa el deducible, el seguro no está requerido a cubrirte. Sin embargo, si sobrepasa el deducible, tú pagas el deducible y la diferencia la cubre el seguro. Básicamente así funciona este tipo de póliza que viene siendo la póliza general, como dijo Luis. La póliza de Flood viene siendo la póliza de inundaciones. Si la propiedad se inunda y cumples con los deducibles, pues ahí es donde entra el seguro y te cubre si no cumples con el deducible, que obviamente una propiedad con un deducible más bajo va a costar más dinero, Un seguro con un deducible más alto, pues va a costar menos porque tienes que llegar a ese deducible para que el seguro entonces venga a cubrirte.

    **Trellis Fields:** Y esto para la póliza general. Entonces eso es como un coverage general de una propiedad de una casa, cierto, Que tiene que trabajar basado ese flujo. Ahora, tú hablaste otro flujo aparte que son coberturas de las builder, cierto,

    **CV Capital Investment Group LLC:** Correcto.

    **Trellis Fields:** de riesgo.

    **CV Capital Investment Group LLC:** Ese tipo de pólizas, pólizas de liabilities, pólizas

    **Trellis Fields:** La

    **CV Capital Investment Group LLC:** de errors,

    **Trellis Fields:** significa riesgo en español, Cris. Cris

    **CV Capital Investment Group LLC:** riesgo

    **Trellis Fields:** también habla inglés, pero

    **CV Capital Investment Group LLC:** sea

    **Trellis Fields:** algunas

    **CV Capital Investment Group LLC:** algo

    **Trellis Fields:** palabras.

    **CV Capital Investment Group LLC:** que no entiendas, Cristian, en confianza páranos y pregunta, porque como dice Luis, mientras más tú entiendas, mejor va a ser la solución. Entonces una póliza de riesgo, esas trabajan un poco diferente, por ejemplo, ya ahí requiere un poco más de información y supongamos que tengo un edificio de 30 apartamentos y vino alguien y se cayó por las escaleras, vino alguien, se contactó un abogado de lesiones y nos llegó una demanda y ahí nosotros sometemos esa demanda al seguro. ¿Por qué? Porque nos están nos están demandando porque alguien se cayó en nuestras escaleras. Entonces esas requieren un poco más de información. También está la póliza de errors and omissions, esa es para errores y omisiones. ¿Qué pasa? Supongamos que yo soy un abogado o yo soy un agente de bienes raíces y yo cometí un error en la firma de documentos, una firma de documentos legales. ¿Qué pasa? Yo tengo una póliza que me cubre de omisiones y errores en caso de que algo haya sido omiso en ese tipo de documentos legales, que en muchos estados y en muchas compañías viene siendo un requerimiento, especialmente si trabajas con documentos o con situaciones legales que pueden llegar a tener un valor muy alto. Si estamos trabajando en un contrato, una propiedad que vale 250 millones y de casualidad a mí se me olvidó poner algo sumamente importante. Ahí es donde entra la póliza de errores y omisiones. Entonces vamos a estar trabajando con mucho tipo de pólizas. Todavía no he tomado la decisión, Luis, de si queremos meter todas las pólizas, por ejemplo, póliza de auto, póliza médica, póliza a la aplicación para que las traquee. Es algo que tal vez podemos implementar, Háblenme bien, en una fase 2, en una fase 3. No es nuestra audiencia, sin duda alguna no es nuestra audiencia. Sin embargo, creo que es algo que puede diferenciarnos o que puede mantenernos inclusive creo que es algo que nos puede

    **Trellis Fields:** Nosotros

    **CV Capital Investment Group LLC:** mantener.

    **Trellis Fields:** en los ciclos de un startup siempre hay una fase plató. ¿Entonces claramente en esa fase plató es donde necesitamos creatividad, OK? ¿A qué otro segmento del mercado podemos entrar? Esto es cuando ya hemos explotado cualquier tipo de recurso. Por ejemplo, ahorita la Academia de Deportes Dr. Ya tiene más de 40 equipos en Florida, ya no hay más escuelas. Ahorita el pipeline que tenemos en nuevas escuelas ya está pequeño a comparación otros años. Ya nosotros no tenemos a dónde expandernos. ¿Aquí ya ahorita tenemos que ser creativos, OK? No montamos una franquicia, no vamos a ni en las. Entonces en esa fase es que vamos a ir a una persona fuera nuestra estrategia GTM, bueno, que lo estemos pensando y que ya tengamos esa creatividad desde ahorita, pero definitivamente vamos a enfocarnos en nuestro avatar.

    **CV Capital Investment Group LLC:** Bienes raíces. Perfecto. Entonces ¿Qué pasa? Tiene 150 pólizas, Cristian, y todas tienen una fecha de caducidad diferente. Usualmente viene siendo un año. Las de Flock vienen siendo usualmente seis meses. Entonces la idea sería, tengo mi póliza, si soy alguien nuevo en la plataforma, tengo mi póliza, hago sign up, escojo la membresía que decidí escoger y coloco la póliza y viene. Viene y agarra la información de esta póliza y la crea para que entonces podamos trackearla. Cada póliza tiene información diferente, se expira en una fecha diferente. La idea es que nosotros recibamos recordatorios 60 90. La persona va a escoger cada cuánto quiere escoger, cuando quiere ser recordada, si 90 días antes, 30 y 60 para que entonces le llegue un recordatorio. Esta persona mira, tu póliza está expirando. Aquí hay algunos quotes que Luis vino con la idea de, por ejemplo, pueden haber diferentes basado en el tipo de membresía, sea la básica, la mediana y la más avanzada. Con la ayuda de I podamos ese quote sea por ejemplo, mira, esta es la póliza que tú tienes. Aquí está la misma póliza con un precio más alto. Por ejemplo, si estás pagando la membresía básica, si estás pagando un poco la más avanzada puede ser una póliza, por ejemplo, con la misma cobertura, pero como todos los años se supone que suba, pues aquí tienen la misma cobertura pero por el mismo precio. Y la más avanzada aún puede ser mejor cobertura por un precio más económico,

    **Trellis Fields:** Aquí yo voy a ya traducir un poquito más a nivel de language. Entonces digamos que crisis PhD elevator 30 segundos, problema solución. Cris, apóyame en esa parte.

    **Trellis Fields:** O sea, yo lo que estoy entendiendo,

    **Trellis Fields:** No, no,

    **Trellis Fields:** lo que me causa la duda,

    **Trellis Fields:** dale dale, métele, déjame escucharte a ti y luego dale.

    **Trellis Fields:** o sea, lo único que me causa la duda, o sea, estoy entendiendo toda esa parte de recordatorios y eso, pero realmente, o sea, con nuestra plataforma, con nuestra aplicación ellos van a poder realizar esa renovación o nosotros digamos que lo conectamos con, no sé, una empresa legal que les vende a ellos esa póliza que está hablando.

    **Trellis Fields:** No, creemos que crees un bot de tecnología artificial que cree pólizas, que la genere, que se comunique con bancos y no, mentira, no, no. Ahí es donde está ese flujo. Ya ahorita Cris está hablando como que está pensando los flujos de lógicas, pero vamos a eso ahorita para recapitular un poco. Básicamente estamos creando una plataforma para resolver un problema. El problema es manejo de propiedades en escala. Manejo de propiedades en escala. Esto puede cambiar una vez que Chris ya haga su. Ya no es entregable, pero por ahora estamos trabajando en base a eso. Vamos a construir una solución en el MVP en base a eso. Las personas que manejan propiedades a escala tienen un problema de tracking, tienen un problema de manejo de ciclos de esos seguros. Entonces digamos que están. No tengo una pizarra, a ver si yo escribo aquí, ¿Lo pueden ver

    **CV Capital Investment Group LLC:** ¿No?

    **Trellis Fields:** algo así? ¿Lo pueden leer? ¿Pueden leer eso bien o se lee derecho?

    **CV Capital Investment Group LLC:** Sí, bueno, sí.

    **Trellis Fields:** Entonces tiene un problema de ciclos. Cada póliza tiene un ciclo, el ciclo puede ser un año, etc. Entonces dentro de ese ciclo de póliza hay diferentes cosas, diferentes problemas que suceden. Un problema puede ser cancelaciones, otro problema puede ser endorsements, otro problema puede ser edición short, problemas o cosas que se tienen que hacer o que se pueden hacer o cosas que suceden que se pueden convertir en problemas. Claramente cuando una persona está manejando muchísimas propiedades en escala, todas estas cosas se convierten en un problema grande donde necesita un equipo de personas humanas como Chris, trabajando con el inversionista que trabaja en el tracking, en el updating, pidiendo las cotizaciones de nuevas pólizas, etc. Nosotros, Renew también el nombre puede que protocambie, nos vamos a enfocar para el MVP y la infraestructura de software inicial en una solución. Digamos que el problema es ciclos. Ese es el problema general. De ese problema parten diferentes subproblemas y cada problema tiene una solución. Entonces, lo que está hablando con Cris antes de unirnos contigo, bueno, Christopher, Cristian. Lo que está hablando con Christopher antes de unirme contigo es que el subproblema en el cual nos vamos a enfocar, porque creo que sería súper cool crear una solución stack, stack con un poco de locura adentro, es una solución específica para reminders, reminders de póliza. Es decir, tú Cris, compraste una casa. Cristian, compraste una casa, tu póliza se vence en junio estamos a mayo, ¿Verdad? Se supone, bueno, se vence en julio, estamos a manjo. Entonces crearíamos una función. Tú metes tu póliza, tú entras en Renew OS, sea en una app, sea un browser, puede que funcione dentro de las dos, mete, submite, creas tu perfil y creas una propiedad, porque nos vamos a enfocar en Real Estate. Creas un perfil de una propiedad, bajo ese perfil vas a colocar tu póliza. Al colocar tu póliza, necesitamos que el OCR, la función de primero que todo, que esa póliza pueda ser, tenga este ocre o tener un flujo donde convirtamos que esa póliza se haga el OCR. ¿Te acuerdas que tú hiciste eso con chat? Convertiste todos los libros en OCR con chat. Entonces necesitamos.

    **CV Capital Investment Group LLC:** Pregunta. Y Luis, no sería mejor, por ejemplo, si yo soy nuevo en la plataforma, yo vengo, subo la póliza y me imagino que a eso te refieres, pero el OCR entonces cree la propiedad que está afectando, que esa póliza está afectando. Porque otro punto aquí es que hay pólizas que afectan múltiples propiedades.

    **Trellis Fields:** Epa, epa, epa, Cris. Ya va, ya va, ya va. No estamos hablando de eso, chicos, pero sí, Cris, ya quieres movernos una ensalada, un mango. Sí, eso. Ahí es donde la lógica, Cris, Cristian, va a ser súper importante porque tenemos múltiples variables que afectan a una sola póliza. Estamos hablando de fecha, estamos hablando de cobertura, estamos hablando de máster, de pólizas máster. Es decir que si hay como que esta lógica tiene que ser familia, una lógica familiar. Entonces el abuelo es la póliza máster, el hijo, el hijo, la hija es la póliza, su póliza. Y puede que dentro de esa hija tenga un nieto donde haya una póliza abajo de eso, o tengan varios nietos. Entonces a lo mejor que un nieto es un tipo de póliza, otro nieto es otro tipo de póliza, otro nieto es otro tipo de póliza. Entonces es un árbol genealógico. Pienso que una lógica que podría funcionar es un árbol genealógico dentro de cada póliza. Esto me recuerda a mi experiencia con QuickBooks hace poquito tuve que aprender Badewakris para hacer los taxes y que queden bien, porque Diego hizo un desastre, a pesar de que es otro tema, pero tuve que arreglar una locura dentro de QuickBooks. Y la manera en que, por ejemplo, ellos tienen ciertas lógicas alrededor de reconciliación con tarjetas de crédito es que tienen abuelos, tienen hijos y tienen nietos, ¿Verdad? Si tú puedes reconciliar el dinero que sale y entra de cada tarjeta de crédito y hay una tarjeta de crédito que es dueña de todas esas tarjetas, ¿Cierto? Porque yo tengo

    **CV Capital Investment Group LLC:** Correct.

    **Trellis Fields:** empleados a los cuales yo leo tarjetas, entonces algo parecido. Entonces necesitamos una lógica construida alrededor de árbol genealógico dentro de cada. Entonces un árbol genealógico en cada parte de ese árbol, ¿Verdad? Va a haber una póliza, sea lo que sea, va a haber una póliza dentro de cada parte de ese árbol genealógico. Y esa póliza va a tener, Vamos a hacer diferentes cosas con esa póliza. Esas cosas van a ser soluciones a problemas. Entonces, el problema que acabamos de escoger Christopher y yo, es el problema de renew reminders. Es decir, que si tu póliza se expira en julio, ¿Verdad? Tú ahorita en mayo deberías recibir una notificación y puede ser customizable. Entonces, cuando tú pongas tu póliza abuelo, digamos que tengas una póliza vuelo, ya que Christopher nos lanzó esa bola de béisbol, pones tu póliza vuelo, ¿Verdad? Y si tiene su póliza, la puedes montar también ahí mismo. Entonces, póliza vuelo, la función, necesitamos adentro que si el documento no está OCR, poder extraer la información del documento, porque básicamente un documento CR es un documento con texto extraíble, Christopher. Entonces

    **CV Capital Investment Group LLC:** Okay.

    **Trellis Fields:** necesitamos para poder extraer la información de esa póliza una vez que la extraigamos, definir cuál es la fecha de expiración. Esta es la primera solución. Keep in mind, Van a ver muchas cosas que vamos a hacer con una póliza. Esta es baseline. Vamos a comenzar con esto. Esa póliza va a entrar en una. Va a entrar en el sistema. Vamos a agarrar la fecha de expiración y tú determines la fecha. Si quieres un Remander 30 días antes, vamos a tener una automatización de Reminders 30 días antes. Esa automatización de reminders va a ser un trigger a una cadena de eventos. La primera cadena de eventos es, vamos a pedir, La cadena de eventos comienza con. Vamos a pedir quotes. Esos quotes son cotizaciones que le vamos a pedir a personas dentro de la plataforma, a nuestros aliados de compañías de seguro. Eso lo que necesitamos es, necesitamos un backend. Necesitamos un backend para que ellos puedan entrar los quote makers, ¿Cierto? Que son los que mandan los quotes para que ellos puedan ver el request de ese quote y mandarlo. ¿Qué pasa? Que cuando nuestra herramienta crea ese quote, crea diferentes tipos de request. Crea un request para una póliza baseline, que si tienes una pera, si tienes una pera, si tienes una pera, un bolígrafo te va a dar un bolígrafo, ¿Verdad? Pera con pera. Entonces, si la póliza era una pera, ese quote, ese request va a ser por una pera. Entonces le vamos a decir, mira, compañía de seguro, yo necesito una pera, aquí está esta pera, necesito otra pera, entonces mándame su co. Vamos a tener una manzana, entonces digamos que a mí me gustan las manzanas más que las peras, entonces la manzana va a ser una versión mejor que la pera, Entonces la manzana va a tener un mejor precio que la pera, porque yo en esta etapa de real estate yo necesito pólizas más baratas, digamos. Entonces vamos a pedirle ese request, va a mandar un request para una póliza más económica, la misma cobertura y va a haber otro request para una póliza, otra no, una pera es un kiwi. Entonces va a haber otro request para una póliza más económica y con mejor cobertura. Entonces cuando vamos al cliente que le vamos a mandar la solución que va a ser el factor wow, va a ser que le vamos a dar una manzana, una pera y un kiwi sin que ellos muevan ni un dedo. ¿Como la va a leer la póliza, verdad? Necesitamos varias variables aquí. Cuando lea la póliza necesitamos que lea coberturas, uno, dos, que haga un. ¿Que lea las coberturas y las entienda, dos Que lea la dirección, el address, dónde está localizado? Está localizado al lado de un lago. Esto va a ser, este punto geográfico creo que va a ser uno de los puntos más candelas por cómo nosotros entrenamos a un LL a que entienda que está cerca de un lago. Puede ser normalmente ¿Cómo se dan cuenta de esto? Cris, en el Property Appraiser

    **CV Capital Investment Group LLC:** Bueno,

    **Trellis Fields:** hay un lugar

    **CV Capital Investment Group LLC:** usualmente

    **Trellis Fields:** donde dice

    **CV Capital Investment Group LLC:** sí, en el property appreciate usualmente muestra este, por ejemplo, en qué tipo de flood zone está la propiedad

    **Trellis Fields:** eso

    **CV Capital Investment Group LLC:** si no hay un website especializado para esto

    **Trellis Fields:** aparte.

    **CV Capital Investment Group LLC:** que es el FEMA.

    **Trellis Fields:** OK, Búsqueda de FEMA for Flood. ¿Qué más? ¿Que otra cosa necesitamos como variable de una póliza

    **CV Capital Investment Group LLC:** Bueno,

    **Trellis Fields:** con cobertura?

    **CV Capital Investment Group LLC:** creo que algo que no están mencionando viene siendo la fecha. Obviamente es importante la dirección, la cobertura. ¿Y cuál era la otra que es sumamente

    **Trellis Fields:** No,

    **CV Capital Investment Group LLC:** importante?

    **Trellis Fields:** pero me refiero, Sí, tráelo a la mesa cuando te recuerdes, pero me refiero a que si una propiedad necesita un seguro o una mejor cobertura de flood que se puede inundar, ¿Qué otra cosa necesitaría? Una propiedad seguro de al amor de huracán cuando venga un huracán o algo así, ¿Que otra cosa necesitaría más? Nada, solamente inundación.

    **CV Capital Investment Group LLC:** Lo que pasa es que inundación es una póliza aparte

    **Trellis Fields:** OK,

    **CV Capital Investment Group LLC:** en cuanto a huracán,

    **Trellis Fields:** ¿Como

    **CV Capital Investment Group LLC:** en cuanto a terremoto, ese tipo de pólizas está ya ese tipo de cobertura está en la general,

    **Trellis Fields:** que cobertura en la general? No entiendo eso.

    **CV Capital Investment Group LLC:** o sea, por ejemplo, está la cobertura general, el property insurance, el seguro de propiedad incluye, dependiendo el deducible, incluye este water damage, incluye el daño para huracán, incluye tornado, hay una serie de cosas que incluye robo, todo depende el seguro que hayas escogido. Hay un seguro aparte de ese que viene siendo flood. No todas las propiedades requieren un seguro float, por eso es aparte. Inclusive si lo requiere, son dos pólizas diferentes. Tendrías la póliza de la propiedad y tendrías la póliza flood que no está adjuntada a esta. Es una póliza totalmente separada, con un número de póliza separada,

    **Trellis Fields:** Y si tuviésemos la oportunidad de mejorar una póliza en base a cobertura, ¿Cómo sería? ¿Qué haría que una póliza sea mejor a nivel de cobertura?

    **CV Capital Investment Group LLC:** obviamente un deducible más bajo y un coverage más alto. Por ejemplo, no todas las propiedades, supongamos que el water damage lo que Cubre vienen siendo 5 mil dólares. Realmente si mi propiedad se inunda aquí en Estados Unidos, con 5 mil dólares no me da ni para cambiar los gabinetes. Entonces, con un coverage mayor y un deducible más bajo, eso básicamente, ahí está el beneficio. En la mayoría de las pólizas viene siendo que lo que te dan no es tan alto y quieren que el deducible sea muy alto. Muy alto.

    **Trellis Fields:** ¿Entonces sería una oportunidad de buscar que el mismo AI dentro o el mismo entrenado dentro de esa póliza una vez que la lea. Una vez que lea la póliza, lea cuál es la, o sea que busque una mínimo tenemos que buscar una pera, si tenemos una pera, necesitamos una pera, eso es lo más sencillo, cierto? Cualquier asegurador nos podría decir mira aquí tenés una pera que te voy a dar otra pera. ¿Ahora lo que podríamos lograr que lea y haga es leer esa póliza, ver cuáles son las oportunidades de mejorar la cobertura y bajar el deducible que tenga que pagar el cliente y pedir una manzana Entonces le decimos mira para que me tume esto es una manzana verdad? ¿Si por ejemplo eran mil dólares de deducible que la manzana que lea mismo diga bueno un número, OK, puede ser 500 dólares deducible y que esa misma información se la pase al asegurador, que ya nosotros al asegurador le mandemos, no que ellos nos manden lo que le dé la gana, no vamos a cambiar la industria de aseguradores, van a ver que vamos a darle por donde más les duele porque vamos a pedirle realísticamente, no vamos a pedirle que nos den en las estrellas del cielo, vamos a pedirle algo objetivo en base a la póliza que el mismo día diga bueno mira dame esto si quieres para darme, para entregar esta manzana que es mejor que la pera, necesito esto y que le diga deducible tiene que tener esto y este tiene que ser el otro premium y las aseguradoras que puedan llegar a ese requisito verdad? Que se las manden de una al usuario. ¿Ahora, usuario tiene la oportunidad de pedir o que tenga una membresía sencilla donde si quiere una pera, que tenga una pera y una membresía a lo mejor un poquito, pero eso ya es como modelos que podemos analizar luego con crisis, pero pienso que lograr que entrenar el EDI con información de seguros, cierto? Y que el mismo pueda tomar una decisión en qué sería un mejor, en cuáles son las oportunidades de mejorar la póliza en base al deducible y en base a la cobertura y que le pida eso a nuestros asociados, partners, aseguradores sería un buen y luego antes de que se venza le manda, mira se va a expirar la cobertura y estas son las quotes disponibles para ti. Entonces necesitamos ese flujo completo dentro del app wide level vamos a ponerle un color que sea letras cualquiera claramente supervisor friend, le vamos a meter las animaciones que hemos hecho para que sea bastante engaging la experiencia de usuario, que no sea un website dinosaurio, La idea es que el website se vea fresco, que se vea, que sea interactivo. Entonces esas cositas pequeñitas que hemos estado haciendo para chistoshare, vamos a implementarlas aquí también. Pero ciertamente va a ser what level porque todavía no tenemos branding, entonces no nos vamos a enfocar en el brand, no nos vamos a enfocar en la letra pura lógica de solución para la primera fase. Y Cris, hasta que no tengamos algo un poco más concreto con el área de GTM, yo aconsejo que no continuemos desarrollando hasta que tengamos algo más concreto.

    **CV Capital Investment Group LLC:** Perfecto.

    **Trellis Fields:** Pienso que esta primera fase va a ser buena, la podemos lograr en poco tiempo, pero ciertamente hay que caminar de mano a mano.

    **CV Capital Investment Group LLC:** Me parece bien. Creo que también esto va a ayudar que esta primera fase, empezar así de poquito, va a ayudar que Christian también entienda mejor lo que estamos buscando, la solución que estamos tratando de crear, porque es bastante compleja y mientras más vayas entrando en el tema, te vas a dar cuenta que, bueno, que es un poquito más. No es simplemente renovar una póliza, sino es el tracking de la póliza, el costo de la misma, etcétera, etcétera, y lo mucho que. Y lo mucho que una póliza puede afectar, como bien conversamos al principio, no un individuo que tenga una sola propiedad, eso es fácil de manejar, pero cuando ya estás hablando de múltiples pólizas a escala, se vuelve bastante difícil de. KEEP UP WITH THE deadlines Trabaj.

    **Trellis Fields:** Cien por ciento, 100 por ciento a nivel de comunicación para cerrar ese punto. Ciertamente el producto tiene un potencial masivo, así que Cris, siempre hablamos de detalles, organización y flujos como claros. Entonces es súper importante que pensemos hasta lo que no he pensado, mantener la comunicación súper activa, como lo hacemos para todos los proyectos, la comunicación va a venir directamente de mi parte. Claramente estos espacios van a ser algo que vamos a acostumbrar a hacer, especialmente cuando tengamos avances. Pero básicamente vamos a trabajar el proyecto, vamos a desarrollar juntos y eventualmente a medida que vamos trabajando y teniendo nuevos updates, nuevos flujos, nuevas soluciones, vamos a reunirnos con Chris para entender bien cuál es la solución y el problema de crear una solución alrededor de eso. Claramente ahorita estamos bastante wide level mode porque no tenemos mucho, pero la idea es que pronto ya empecemos a desarrollar en base a lo que eventualmente va a ser la solución completa.

    **Trellis Fields:** ¿OK, bueno, tengo varias preguntitas, la primera es, o sea, esto al final va a ser una aplicación móvil o una aplicación web? Las dos, pero aplicación web tipo, o sea, los usuarios van a ser única y exclusivamente a través de la aplicación móvil o la aplicación web solo va a ser para temas administrativos, o sea, por ejemplo, dashboard, administradores.

    **Trellis Fields:** Yo pienso que la cuenta y todo, o sea que el manejo de la cuenta de pólizas y todo eso, para ser lo más accesible a la persona posible, debería ser web, debería ser móvil. Perdón, ¿Para que? Mira, ¿Cuál es esta póliza? Me meto y ya. En realidad, corrígeme Cris, pero si yo estoy sentado en una oficina con una computadora abierta y necesito manejar pol. Necesito manejar ciento 130 pólizas, lo

    **CV Capital Investment Group LLC:** This

    **Trellis Fields:** más probable

    **CV Capital Investment Group LLC:** is.

    **Trellis Fields:** es que no lo vaya a hacer en mi teléfono. Entonces yo pienso que la interfaz móvil va a ser necesaria de que hagan ciertas cosas dentro de la interfaz móvil. Pero enfocarnos en el uso de la interfaz web, a medida que vamos desarrollando en web, vamos migrando ciertas funciones a móvil. Por ejemplo, una persona debería poder montar una póliza móvil porque si, nosotros tenemos nuestro cliente ideal, pero también puede venir una persona con una póliza a montarla y pagarnos y no le vamos a decir mira no me pagues porque tú eres, tú no tienes un portafolio de millones de dólares, tú no eres para nosotros

    **CV Capital Investment Group LLC:** Yo creo que la parte móvil debe ser mucho más obviamente sencilla y si quieres hacer cualquier cosa un poco más, más difícil pues la.

    **Trellis Fields:** funciones avanzadas en web.

    **CV Capital Investment Group LLC:** Pero por ejemplo que tengas acceso a las pólizas de las propiedades que tengas activa creo que, creo que es una muy básica y buena función especialmente para móvil porque si me llaman y no estoy frente a la computadora, estoy de vacaciones y me piden mira necesito que me envíes copia de la póliza de tal propiedad, o sea, poder acceder ahí en el celular es mucho más sencillo también son soluciones que más a futuro no son soluciones que son parte del MVP, pero por ejemplo lo que es un basic report de las pólizas, por ejemplo, tienes 15 pólizas activas, el costo de las 15 pólizas viene siendo 100 mil dólares que tú puedas ver un dashboard por así decirlo y que en el dashboard en el móvil puedas tener una serie de funciones básicas a la final eso es algo que podemos profundizar luego, pero sí creo que la función móvil va a ser necesaria para lo más sencillo.

    **Trellis Fields:** Claro, y una pregunta, ustedes, o sea, ustedes cuando me hablan de cargar pólizas y eso, o sea, yo lo que entiendo es, por ejemplo, yo adquirí X póliza para mi hogar, pues eso me imagino que no sé, digamos que lo hago a través de, no sé si eso se puede hacer a través de una página web que uno firma, lo que sea, y me llevo un correo de confirmación con, yo que sé, un PDF con toda la información legal de la póliza, o sea, ustedes me hablan de cargar póliza, sería como yo montar ese PDF en la aplicación web, ya que con el PDF ya tenemos montado la póliza, ustedes se refieren a eso, ¿Verdad?

    **CV Capital Investment Group LLC:** Sí, a veces llega así y a veces llega así, entonces uno puede agarrar tal vez la cámara del celular, no creo que la de la computadora, o juntas un PDF o abres la cámara en este caso del celular para poder, para que la aplicación pueda leer todos los detalles de la póliza.

    **Trellis Fields:** Ahora, eso en sí es un flujo totalmente, o sea que le tomen una foto con el teléfono va a ser un flujo totalmente diferente porque hay que asegurarse, o sea, hay muchas variables que a lo mejor la misma herramienta no use bien. Entonces es como que hacer testing va a ser importante antes de como que hacerla funcional. Yo pienso que actualmente deberíamos nada más mandar PDFs, puede llegar de otras maneras y puede ser una foto, puede ser a lo mejor de que una persona está no sé pida que los mismos, ni siquiera que la monten ellos, una función donde le pilla los mismos cotizadores que mira, ponme la póliza ahí en el portal. Entonces todas esas funciones son importantes, pero enfocarnos en una primera que un PDF montado es la más viable, ya por ahí tenemos que asegurarnos que los

    **CV Capital Investment Group LLC:** Si creo,

    **Trellis Fields:** datos los

    **CV Capital Investment Group LLC:** por

    **Trellis Fields:** sirven,

    **CV Capital Investment Group LLC:** ejemplo, si creo de las 10 pólizas que por ejemplo, no sé, si pienso en pólizas que me han llegado, no es hasta que yo las pido por PDF que me las envíen, o sea, sí, sí, sí quiero decir que la mayoría de las pólizas y me imagino que también para la gran mayoría de personas les llega un sobre al correo con la póliza, entonces cuando lleguemos a ese problema y estamos buscando esa solución, si pudiéramos tal vez pensar en la solución para eso, la gran mayoría de personas va a recibir, va a recibir el papel con su, con los detalles,

    **Trellis Fields:** Okay,

    **Trellis Fields:** Pero la póliza no la manda el seguro como tal directamente.

    **CV Capital Investment Group LLC:** no, o sea,

    **Trellis Fields:** A

    **CV Capital Investment Group LLC:** ya

    **Trellis Fields:** menos que la pida.

    **CV Capital Investment Group LLC:** sería

    **Trellis Fields:** A menos que

    **CV Capital Investment Group LLC:** una

    **Trellis Fields:** la pida,

    **CV Capital Investment Group LLC:** adicional, hay que tipo pedírsela al broker y todo eso, pero no, la idea eventualmente es que cuando las personas estén en nuestra aplicación, que el broker, el broker esté desde su lado, él mismo pueda adjuntar la póliza a esa persona, sin embargo una persona si es una persona nueva y que recién está entrando en nuestra aplicación, no va a tener cómo, no va a tener cómo juntar la póliza. Bueno,

    **Trellis Fields:** Entonces

    **CV Capital Investment Group LLC:** alguien.

    **Trellis Fields:** va a tener que ser que para obtener esa póliza el backend que funcione mano a mano con el backend del asegurador y que el asegurador mismo sea el que ponga la póliza. Ni siquiera nos enfoquemos en un tweeter donde el pie de la polimente un request, donde le mandes un request al asegurador que te hizo la póliza que la monte desde la misma aplicación. Y luego tenemos otra función donde le metemos esa función donde él mismo pueda ponerla. Pero si el flujo real es que ellos van a tener que montarla y por eso que hagamos eso como baseline.

    **CV Capital Investment Group LLC:** Sí, porque inclusive si pensamos en pedir siempre al broker, hay brokers que van a estar afiliados con nosotros esperemos que muchos al principio, pero si es un broker que la persona escogió directamente ello y que no está con nosotros en la aplicación, va a ser difícil para ese broker adjuntar.

    **Trellis Fields:** Correcto,

    **CV Capital Investment Group LLC:** ¿Cuáles son las otras preguntas, Cristian?

    **Trellis Fields:** Yo diría que la más importante es, o sea, qué tipo de usuarios van a acceder, porque yo lo estoy planteando de esta manera, aplicación móvil principalmente para usuarios, es decir, ya sea la persona que tiene su póliza y quiere ver todo y le llega la información y los reminders y todo lo que están hablando y un panel, una aplicación ya web que tú entres a Google por un dominio, lo que sea, y ahí manejes ustedes dos como administradores o ahora que está hablando de los brokers también, como que ellos tengan acceso a esa plataforma, o sea, cuáles son realmente los usuarios que van a estar involucrados y quiénes van a estar en aplicación web y quiénes van a estar en, yo que sé, Dashboard.

    **CV Capital Investment Group LLC:** Bueno, por ejemplo, en el área de admin va a estar obviamente Luis, soporte técnico y por así decirlo, los socios van a tener acceso a esa parte backend. En el lado de usuario va a estar el lado de usuario, este lado de cliente, ahí vas a ver tus pólizas, acceder a los documentos y también va a estar el lado de los proveedores de póliza. Entonces

    **Trellis Fields:** Exacto.

    **CV Capital Investment Group LLC:** por.

    **Trellis Fields:** Pero a la pregunta de Cris es ¿Quién vamos a tener? Digamos que hay varias personas, tenemos varios clientes, un cliente son los brokers, los que hacen los seguros, otros son los que piden los seguros, los clientes. Entonces ambos van a tener un acceso diferente a la plataforma ya que ambos tienen diferentes cosas que hacer. ¿La pregunta de Cris es a quién vamos a tener en web y aplicación?

    **CV Capital Investment Group LLC:** Yo no creo que a los proveedores haya que tenerlos en la aplicación, por lo menos no cualquier cosa que sea la parte de la comunicación, que es otra cosa de las que queremos solucionar con este sistema actualmente. Te voy a dar uno de los problemas que yo experimenté durante mientras trabajé en la oficina. Tenemos una oficina y la oficina completa maneja 600 propiedades por así decirlo, ¿Verdad? Entonces ¿Qué pasa? Supongamos que se crea un usuario para la oficina, ¿Cierto? Entonces mediante ese usuario, tanto yo como mi manager en aquel momento podía pedir un quote a uno de los proveedores. ¿Qué pasa? Lo importante, queremos unificar la comunicación, queremos que la comunicación esté en un lugar para que no importa si sea yo, si sea yo, si sea mi manager o bajémoslo a una familia. Supongamos que mi esposa y yo tenemos la aplicación en el celular y queremos hacer un cambio a la póliza. Entonces le escribimos a nuestro proveedor, mira, nos gustaría cambiar tal cosa. Lo que no queremos es yo tener lo que pedir por aquí, pero mi esposa no sabe si yo lo hice, entonces ella viene y lo escribe por otro lado, por mensaje o por email. Sino que aquí podamos tener tal vez la parte de la aplicación, para responder a tu pregunta, del lado de los proveedores puede limitarse solo a la comunicación para que ellos siempre tengan acceso a si reciben un mensaje, si reciben un request y si tienen que hacer algo, pues tal vez pasen a la computadora.

    **Trellis Fields:** En base

    **Trellis Fields:** Ok,

    **Trellis Fields:** a eso pienso que la solución principal, o sea, lo que yo entiendo es que podríamos, Cristian, crear una lógica basada que todo sea en base a la propiedad. La propiedad, como las propiedades tienen su propio árbol genealógico, tienen su propia estructura. Por ejemplo, si en una oficina de un inversionista tienen 300 propiedades y son manejadas por múltiples personas, que esas mismas personas, que tú puedas invitar a personas a manejar esa propiedad, que todo parta, que el usuario no sea la propiedad, que el usuario cree una propiedad, una propiedad, una entidad en sí, que pueda ser manejada por múltiples usuarios al mismo tiempo. Ahí podemos partir con lógica para brokers, lógica para coworkers, porque nuestra solución inversionista, vámonos con eso, Personas que trabajen en la oficina, podemos asignar roles, etcétera, etcétera.

    **Trellis Fields:** Claro,

    **CV Capital Investment Group LLC:** ¿Correcto?

    **Trellis Fields:** sí, o sea, eso que mencionas ya como que aterriza mucho más las cosas y es no tomar, así como tú estás mencionando, digamos que es una familia y alguno del núcleo familiar quiere hacer un cambio en la póliza, entonces no se mide como un usuario y después no sabemos si yo que sé el padre, el esposo, lo que sea está de acuerdo con eso, que no se haga la comunicación a múltiples personas sino que sea a una sola, entonces tomar en vez de usuarios tomarlos como propiedad y en esa propiedad digamos hay yo que sé cuatro personas del núcleo familiar involucradas en esa o con permiso en esa propiedad entonces diría yo que hacerlo en base así como dice Luis, la propiedad como tal es el núcleo y varias personas interactúan varios roles y ahí pues podemos hacer que como te está comunicando que los brokers más que todo son para permisos y para request y para toda la información así como de póliza podemos también incorporarlos para que ellos digamos estén inicialmente en la aplicación web y de ahí pues le ponemos ciertos permisos que obviamente no van a poder ver sino una propiedad en específico o van a tener los request solo van a llegar de una propiedad en específico mientras que nosotros nos va a llegar pues tenemos la información de todas las propiedades, de todas las pólizas, de toda la información de las personas, entonces así como que ya aterriza un poquito más de qué permisos tiene cada quien, qué puede ver cada quien y pues ahí vamos ajustando conforme vayamos avanzando.

    **CV Capital Investment Group LLC:** Children,

    **Trellis Fields:** Amazing, amazing. Disculpen familia que estoy aquí cerrando el venue porque tengo que ya arrancar. Pero bueno, a mí me parece que Cristian, de tu parte, pienso que no es nuestro primer rodeo y definitivamente tenemos el background para entender qué significan este tipo de cosas a nivel de lógica, que al final del día va a ser lo más importante. Y bueno, necesitamos mucho input de parte de Christopher para que la solución sea lo más aterrizada, lo real posible, ya que tenemos experiencia creando cosas que realmente no son funcionales. Entonces ese tipo de detalles. Cristofer, yo pienso que para ti la filosofía de que nunca es poca, o sea, nunca es suficiente información. Entre más información podemos, así nos aburras por 45 minutos hablando de situaciones, escenarios que suceden. Esto es momento para que tú mientras vas en el carro, que te grabes a ti mismo comentando hacia los diferentes casos que has visualizado, pólizas que se cancelan, diferentes cosas que suceden, porque todo eso va a ser información importante para que nosotros la consideremos para la solución como tal, porque al final del día todo eso va a estar adjunto. Lógica.

    **CV Capital Investment Group LLC:** Perfecto, voy a trabajar en eso. Me parece buena idea, especialmente qué tipo de qué manera le funcionaría más que cuando yo me vaya acordando de escenarios por los cuales he pasado, me grabe a mí mismo, sea por texto, sea por voice, sea un video en el que me puedan observar y escuchar, cómo funcionaría para que cuando, mientras yo me siga acordando, me voy grabando y se los mando pues por el medio de comunicación que escojamos.

    **Trellis Fields:** En ClickUp hay una función donde cuando tú grabas un voice memo, automáticamente lo convierte en un transcript. Para nosotros lo importante no es tú, Tú puedes tener una voz así de hombre, pero créeme que no queremos escucharte a ti, queremos tus palabras. Entonces para nosotros lo más importante es poder recibir esa data. Entonces lo que yo recomiendo para nuestro flujo de trabajo, Cris, es que te creemos una cuenta de ClickUp, bueno, le creemos a la empresa a una cuenta de Click Up, podemos ser un mientras tanto, luego le cambiamos el nombre. Creamos primero que todo un ambiente completo de Chrome, de Google, dentro de empresas. Pienso que eso es primordial. Sé que mandaste un folder hoy, pero lo más real, lo más posible, o sea, nosotros necesitamos un lugar donde guardemos nuestra data de forma reliable de otras maneras de guardar data, pero por ahora una cuenta de Chrome es suficiente. Partiendo de esa cuenta de Chrome, le abrimos una cuenta de ClickUp, esa cuenta de Chrome y tú puedes utilizar esa cuota de ClickUp desde tu teléfono, baja la aplicación, te logueas y puedes dejar notas y la puedes. ¿Vamos a crear un chat, sabes? Como Discord, Telegram, todo eso. Eso existe dentro de ClickUp. ClickUp tiene su propio Telegram, por decirlo así. YouTube.

    **CV Capital Investment Group LLC:** Okay,

    **Trellis Fields:** Puedes mandar una bota de voz y esa. Y agarra toda tu. Agarra tu voz y agarra tu data. Lo que agarres esa data, Cris, agarra esa información y la guarda en nuestra mega lente de Obsidian. Claramente vamos a necesitar para el proyecto como tal. Entonces guardamos eso dentro de la mente de Obsidian y posiblemente dentro de ClickUp. No está de más documentar dentro de ClickUp a través de un documento como tal, no a través de un MD. Entonces ya esa información queda guardada tanto dentro de ClickUp como nuestra mente como tal. Así entiende, así tenemos esa información asegurada de una forma donde la podamos utilizar y documentada al mismo tiempo. Entonces tenerte en clico va a ser lo más, o sea, tener a Renew o lo que sea que sea el nombre va a ser lo más importante.

    **CV Capital Investment Group LLC:** Perfecto. Nada, si quieres, cuando termines ahí en el venue, me llamas y cuando estés disponible me cuadramos lo de los accesos y terminamos de cuadrar la parte de lo de la comunicación y lo del branding.

    **Trellis Fields:** Excelente, excelente familia. Pero bueno, comenzamos con esta

    **Trellis Fields:** También

    **Trellis Fields:** solución,

    **Trellis Fields:** si pueden documentar tipo ejemplos, no sé, situaciones reales, sobre todo reales, flujos de trabajo reales, problemas, solución que tú haces, todo eso pues ya como está comunicando Luis lo montamos en ClickUp y yo me encargo personalmente de poner la segunda mente que nosotros tenemos que se llama Obsidian que es como un bol donde está toda la información y empezamos a meter

    **Trellis Fields:** Cris,

    **Trellis Fields:** documentos,

    **Trellis Fields:** Todo lo

    **Trellis Fields:** todo.

    **Trellis Fields:** que, by the way, todo lo que tú has hecho ha sido un flex para todas las. Para muchas reuniones que yo tengo, porque una cosa loquísimamente buena. Entonces ellos ya han visto absolutamente todo.

    **CV Capital Investment Group LLC:** Sí, sí,

    **Trellis Fields:** Sí,

    **CV Capital Investment Group LLC:** sí.

    **Trellis Fields:** claro, claro, 100%.

    **CV Capital Investment Group LLC:** Chévere. Entonces, nada, estamos hablando. Cristian, un placer. Vamos a seguir comunicándonos especialmente, bueno, la comunicación va a ir a través de Luis. Si tienen cualquier duda, cualquier bloque, brincamos en una llamada rápida y aquí a las órdenes. Emocionado de trabajar con ustedes sumamente y de la solución que vamos a crear, que hay una gran necesidad.

    **Trellis Fields:** Igualmente

    **Trellis Fields:** Así es. Allá

    **Trellis Fields:** esto de

    **Trellis Fields:** vamos

    **Trellis Fields:** verdad

    **Trellis Fields:** familia.

    **Trellis Fields:** me emociona bastante.

    **CV Capital Investment Group LLC:** Bien, cuídense.

    **Trellis Fields:** Dale, buenísimas. Gracias por todo, Cris. Estamos hablando. Estamos hablamos, Cristian.

_Sincronizado por Brain: 2026-10-17T00:38:46.345Z_
