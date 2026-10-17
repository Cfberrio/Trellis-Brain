---
brain_note_id: "dest:meetings:c05539f6f7cef36a09a34658ff91117d"
canonical_key: "meetings/c05539f6f7cef36a09a34658ff91117d"
brand_id: "meetings"
---
# Transcript — 2026-06-25 SyncUp Dev (21717)

## Transcript

- Reunión: [[02-Meetings/2026-06-25 SyncUp Dev (21717)]]

**Cristian Berrío**: Buenos días, buenos días.
**User guest**: Hermano querido, como está todo,
**Cristian Berrío**: Excelente.
**User guest**: ¿Cómo te sentás la coloma de triunfara?
**Cristian Berrío**: Efectivo. Por fin. Después de cuatro años. Después de cuatro años duros, triunfando otra vez.
**User guest**: Así es, ¿verdad? Mira, pero también con el con el mundial están dando durísimo.
**Cristian Berrío**: Canosi, primerito del gruppo.
**User guest**: Sorry.
**Cristian Berrío**: También la estamos, literalmente, la estamos rompiendo en todos lados.
**User guest**: Sí. ¿Te la has visto? ¿Te ha visto el nuevo? ¿Te lo has visto?
**Cristian Berrío**: Claro, todos. Hasta los que no son de Colombia, no los veo.
**User guest**: Brutal. Brutal, brutal. Claramente va por Colombia este mundial, ¿no? O sea, no, tienes otro equipo en en mente.
**Cristian Berrío**: Oh, yeah. Ni que fuera antipatriotas.
**User guest**: La patrona se vende tan fácil, ¿verdad?
**Cristian Berrío**: Así es.
**User guest**: Plutal. Hermano, revisé por encima, los dashboards me parece que tienen como que, realmente, están hecho por nuestro flujo ahora que que trabajamos, la diferencia se se nota, Lo que estoy pensando es, al nivel de funcionalidades y mejoras es lo que tenemos planteado, que te mandé. Que tanto de todo lo que pensamos que íbamos a mejorar hemos hecho, o sea, que falta esa lista. Claramente, yo trato de leer, o sea, leyendo lo que tú has mandado, no he visto esos puntos, o sea, no he visto todos los puntos reflejados.
**Cristian Berrío**: O sea, más que todo, es que los los puntos que reflejaba lo del HTML ese que mandaste, son más que todo orientados a funcionalidades sea, no visibles. Como tal.
**User guest**: Correcto. Correcto.
**Cristian Berrío**: Por ejemplo, por ejemplo, las más críticas era tipo, mejorar lo de lo de la seguridad, mejorar uno que otro como leak que teníamos, de de llaves, ¿Y qué más? Y sí, o sea, eran como funcionales así. Bueno, por ejemplo, aquí tenemos otro también de ¿qué pasa si dos padres pagan al mismo tiempo? Equipo, que solo tiene un cupo.
**User guest**: Correcto.
**Cristian Berrío**: Entonces, o sea, todas esas, por ejemplo, lo de la seguridad, todas esas, eso ya está, eso se hizo desde el principio. Son, más que todo, funcionalidades que son para para eso. Hay otras más chiquitas, que es, por ejemplo... Te busco aquí.
**User guest**: O sea, mi pregunta es, has revisado ese HTML y te has asegurado que todos los puntos estén
**Cristian Berrío**: Claro.
**User guest**: Y también como que ir un poco más allá. Por ejemplo, yo me acuerdo que los botones de registración era difícil editar un equipo, o tenías como que una función de expreta, ¿no? Un equipo a un lado y otra función de expreta era el equipo a otro lado. Y así. ¿Entiendes?
**Cristian Berrío**: O sea, ahorita lo que yo puse, fue que fue clonar una sesión completa. Una season, perdón, Entonces, así ya no lo hago manualmente, uno por uno, sino que ladito toda, y ya después solo es que cambié las fechas.
**User guest**: Marca dijiste? Completa.
**Cristian Berrío**: Que, por ejemplo, ahorita mismo, clonar una una season completa cosa de que solo tenga que enviar los días. Pues eso eso se lo puse. Que decía el HTML, Hay otra
**User guest**: Okay.
**Cristian Berrío**: que dice el HTML, que habíamos quedado que no son tan tan tan de ya para allá. Que, o sea, podría implementarla.
**User guest**: ¿Cómo?
**Cristian Berrío**: Pero son cositas chiquitas, por ejemplo, lo del tercer estado, cuando, o sea, sabes que el estado de de o sea, de la asistencia es como llegó o no llegó.
**User guest**: Mhmm.
**Cristian Berrío**: Pero esta como que llegó tarde, llegó esto, no llegó, sea, presentó excusa, etcétera, etcétera. Como que esas cositas chiquitas las puedo ir poniendo. Pero o sea, lo que puedo hacer, es que le puedo dar un barrido a lo que tenemos, pasándole el HTML y poner un orden de prioridad, cosa de que las que, pues, más importantes que aún faltan,
**User guest**: Pero
**Cristian Berrío**: se pueden implementar y las las puedes
**User guest**: o sea, tú tú estás trackeando tú estás trackeando qué falta versus qué no falta, o sea, ¿tú tienes eso claro?
**Cristian Berrío**: Sí, o sea,
**User guest**: ¿O vas a hacer o vas a hacer que el mismo claro te lo diga?
**Cristian Berrío**: No, no, no, o sea, yo trackeé al principio, sobre todo en la base de en alguna que otra cosita inmediata. Pero, o sea, la intención al principio o lo que se logró todos estos tres días, es duplicarlo.
**User guest**: Mhmm. Correcto.
**Cristian Berrío**: Y, en lo que duplicaba, añadía las cosas que yo sabía que podía añadir enseguida, ejemplo,
**User guest**: Eso eso es es
**Cristian Berrío**: todo el tema de
**User guest**: Ok.
**Cristian Berrío**: Ajá.
**User guest**: Te escucho, te escucho algo.
**Cristian Berrío**: Todo el tema todo el tema de seguridad de de base de datos, de backend, todo eso, todo lo que no se ve.
**User guest**: Ok.
**Cristian Berrío**: Lo lo lo lo las cositas así como, ay, en vez de dos estados, ponle tres, cuatro estados. Las cositas que ya eran como muy específicas que ya no son duplicar, sino que cambian la lógica que ya tenemos, Eso no, o sea, eso no lo he hecho porque, ajá, me tomaba mucho más tiempo y y la idea era, pues, terminar esto y ya después, al terminar esto, pues hacer los cambios que que se pudieran hacer.
**User guest**: Tú la lógica que tenemos de equipo de temporada, O sea, ¿te acuerdas que a veces teníamos, que tuvimos una lógica de temporadas como en noviembre, nueva, para que los estatus no se nos afecten y todo eso. ¿Tú no pensaste eso o lo que hiciste fue copiar y pegar?
**Cristian Berrío**: El background está los cuatro estatus. No, obviamente, eso lo puse. Eso es lo, eso era lo más fundamental. Lo del
**User guest**: Lo mismo, lo damos igual.
**Cristian Berrío**: lo de, ajá, lo lógica de estatus es lo da muy igual, porque es lo que actualmente lo que más funciona. Así como tenemos organizado de los cuatro estatus de open, ongoing, closed, archive, toda esa vaina. La dejé la dejé igual. Exacto.
**User guest**: Okay.
**Cristian Berrío**: Pero sí,
**User guest**: Ok, entonces, que vamos a, esto es lo que vamos a hacer. Revisa, eso eso es lo que pensé, porque como te digo, dentro de los updates que tú me mandas, no veía como que mira, esta tal función fue implementada, estos son los cambios que siendo, lo que lo que me estás confirmando ahorita es que hicimos un copy paste efectivo. Ahora, hoy nos vamos a enfocar en lo siguiente, nos vamos a enfocar en que los puntos que conversamos, que están uno, en el HTML, dos, en la reunión. Acuérdate que el HTML no es palabra de dios, o sea, es simplemente un una auditoría de lo que tenemos lo que tenemos lo que teníamos en el pasado dentro de Doctor, y tiene sugerencias, así que podemos hacer el futuro cuáles son las áreas de mejora, con un breakdown de por área. Dentro de la base de datos, dentro de front end, back end, etcétera. Entonces, vamos a agarrar los puntos que sí nos parecieron válidos y lo vamos a implementar. Claramente, si consigues algún punto que no consigue, que no tiene un beneficio gigante, y que está medio complicado implementarlo, coméntame, yo te voy a validar si sí o no es importante o no, porque a veces ese tipo de sesiones en el lado operacional son un poco más importantes que lo que tú estés pensando a nivel de de cómo función, esas algunas cosas en la operacional en la en la parte operacional son superimportantes que que a lo mejor no lo parecen. De de un visto superficial. Entonces, si piensas que algo que hablamos o si piensas que uno de los puntos, que son válidos, que ya está, que ya establecemos que son válidos, son difíciles de implementar y nos va tomar más tiempo lo necesario, no nos no nos enfrasquemos en esos puntos, sino ataquemos lo más lo más factible, lo más pronto posible. La idea es ir mejorando función por función, función por función, una manera smooth, no quedarme estancados en una en una sola área todo el día.
**Cristian Berrío**: Correcto.
**User guest**: Entonces, comencemos por ahí, con ese HTML y con la reunión, recomiendo también que hagamos una una en es decir, darle el dashboard completo a una sesión de clock, y que la sesión de cloud te haga una auditoría de función ¿cierto? Que mismo darle dar algún tipo de explicación, de cómo se crean los equipos, de cómo se editan, de qué es VR, cómo se crean los equipos, es lo que hacemos. Y crear esas funciones desde ahí. Eso sería ideal. Para que esa sesión de cloud te dé los puntos que se deberían mejorar dentro de ese dashboard. Luego agarras esa ves si algún punto es válido por ejemplo, el botón de el el botón de de editar de equipo, puedes unir, ponte que tengas dos botones de editar equipo en dos lugares diferentes, En vez de tener dos lugares, dos botones, editar equipo en dos lugares diferentes, bonificándote en uno solo. Acuérdate que cuando nosotros estamos trabajando en Merced, era nuestra propia intuición ChatGPT, que nos ayudaban a desarrollar este tipo de funciones, etcétera. Ahorita tenemos la opción de dar de de darle como como input a una sesión de clut absolutamente todo lo que tenga que ver con ese dashboard,
**Cristian Berrío**: Mhmm.
**User guest**: y que ahora mismo nos dé una una auditoría, se lo tenés, no tenemos que sentarnos o yo, detalle por detalle, revisando qué hay que hacer y qué hay que cambiar, y qué es lo que hay que implementar. Entonces, eso es un eso es un puntazo. Ahora, vamos a hacer todo eso, hoy. Hoy hoy es el día de eso, el día de limpieza, limpieza lo que se hizo, implementación de lo que ya tenemos planeado, ya conversamos, y sugiero que abras otra computadora y le metas la sesión y la y le metas la sesión de Twitter, el MCP, lo que sea, para que esa misma otra computadora te esté corriendo autorías mientras tú estás trabajando las funciones reales y no no haces cambios desde esa misma computadora, simplemente haces revisión. Computadora específica para revisión. Entonces, vos sabes, por darte esa computadora, y claramente, la la utilizamos para hacer ese tipo de proceso, y que no se te no y no como que sobrecargar lo que están trabajando actualmente.
**Cristian Berrío**: Correcto. Te iba a decir, ahora que me acuerdo.
**User guest**: Cuéntamelo.
**Cristian Berrío**: Que quedé en cuenta. En el apartado de parents, donde está el skills y tears, Ahorita mismo solo tengo la información, de los skills de voleibol, O sea, lo los de tenis y pickleball nunca los he tenido. Ahora que me acabo de dar cuenta. Me me di cuenta ayer cuando estaba haciendo lo de lo de lo del dashboard de padres. O sea, le sale a lo mismo a los tres a los tres de
**User guest**: Ahí sí está.
**Cristian Berrío**: lo mismo.
**User guest**: Eso está en el drive, en algún lugar, no lo busco. Tier structure. Okay. Busca en Drive un documento que se llama tier structure.
**Cristian Berrío**: And discipline briefed.
**User guest**: No, no, no, en en tres, Fíjate que las niñas ya trabajaron con ese contenido para hacer los los verificados.
**Cristian Berrío**: Okay. Yeah. Perfecto. Ok, ok. Ok, listo. Perfecto. Bueno, sí. Me suena lo de usar el otro combo la auditoría. Sí.
**User guest**: Sí. Sí, sí, sí.
**Cristian Berrío**: Pero no voy a hacer una tutoría y otra voy haciendo cambio. Y ya.
**User guest**: Correcto. Correcto. Correcto.
**Cristian Berrío**: Ok.
**User guest**: Tú tienes, y tú en actualmente tienes tres combos, ¿cierto?
**Cristian Berrío**: Dos.
**User guest**: Sí, la de Julián, Moche, tuya.
**Cristian Berrío**: Ahora sí.
**User guest**: Exacto, pero en total tres.
**Cristian Berrío**: Correcto.
**User guest**: Sí, sugiero que yo, mira, claramente, Travis va a volver a crecer pronto, No, es que no me va querer así por siempre.
**Cristian Berrío**: Mhmm.
**User guest**: Hay mucha, hay un camino por recorrer, No necesariamente estoy o sea, lo ideal, lo ideal, sería que tú utilices esas dos computadoras para tu cosa. Claramente, sí, le das un poco de cabeza, tienes la oportunidad de pensar en qué tipo de proceso los puedes implementar, a pesar de, a veces, este, es como que, bueno, hay algunas complicaciones, porque si estás haciendo updates en dos en dos ambientes al mismo tiempo, claramente hay algún tipo de va a haber algún tipo de de dificultad, ¿no?
**Cristian Berrío**: Claro.
**User guest**: Entonces, mi mi mi take es ese, que tú que tú lo hagas de esa manera. Sea, que que vayas, por un lado, haciendo unos procesos que no afectan los otros, vas a ir por lo en tipo ambiente, que vayas haciendo los otros. Y sí, te gusta más unas dos horas, puedes utilizar esa como home, o sea, lo que tú quieras hacer, no hay problema. Idealmente sería que tú le saques jugos a tu motora, Lo de fanogos, sería que te quedas, por lo menos, con una, de ellas, porque pienso que a medida que vamos trabajando proyectos que se pongan con este nivel de herramientas y de aceleración, podemos estratégicamente organizar un día de trabajo para trabajar múltiples procesos al mismo tiempo, y luego, por ejemplo, yo no me tengo que meter en tu carita, para yo yo te dije que no me metí por completo y fue a propósito. Anoche me costé como la como a las cuatro o cinco de la mañana. Yo vi que tú estás haciendo algo en la madrugada, ¿eras tú?
**Cristian Berrío**: Sí.
**User guest**: Mandando unos códigos de discipline rift.
**Cristian Berrío**: Sí. Estaba probando porque hay veces que bueno, no sé no sé su UTP, pero STP, está pasando y me he dado cuenta. Que a veces falla cuando hago cambios. En algo relativamente relacionado digamos, por ejemplo, cuando yo hice primero terminé el front end, terminé el UTP del front end, que fue cuando te dije que lo pude implementar. Después, cuando estaba implementando el coaches, que también también utiliza OTP, por alguna razón cuando implementé el login de coaches, dañó el sistema OTP, Entonces, me tocó arreglarlo otra vez. Cuando hice otra vez, parents, se dañó el el login de parents, se dañó el sistema OTP. Entonces, como que constantemente como que ajá, hay que hay que estar revisando que no se dañe. Ya no es cosa nuestra, hay que mandar un ticket a lo favor. Para ver. Porque, o sea, estoy investigando y no,
**User guest**: Pero es que actualmente no está
**Cristian Berrío**: No, no, está funcionando.
**User guest**: dañándose.
**Cristian Berrío**: Lo que, la cosa es que cada vez que se hagan cambios,
**User guest**: Oh, la la idea es
**Cristian Berrío**: al al, o sea, remotamente relacionados con el plugin,
**User guest**: Ok.
**Cristian Berrío**: Exacto. Cuando se hacen cambios al login, que que utiliza UTP, hay que estar full pendiente de que no se dañe.
**User guest**: Mhmm.
**Cristian Berrío**: Hay que estar constantemente monitoreando. De que no se dañe. Porque ese
**User guest**: Sí, probablemente es un paso, un, cada que das cambios, que sea un paso de verificación de qué porque claramente se nos cae el OTP y se nos cae la plataforma de registro completo.
**Cristian Berrío**: Correcto.
**User guest**: Es la realidad.
**Cristian Berrío**: Entonces, ayer estaba probando eso, porque cuando mandé los últimos cambios no lo había aprobado. Por eso estaba probando.
**User guest**: Sí. Sí. Sería bueno, creando diferentes, yo te puedo dar una lista de correos externos, donde podemos podemos utilizar. Para darle variabilidad de que no utilicemos el correo todas las veces, para para todas, sino diferentes correos a ver qué sucede con esos correos que que se mandan para hacer o ti ti. Ok. Entonces, tenemos ese ese es el plan de hoy, Necesito que te vayas al correo del discipline rest, rapidito, por
**Cristian Berrío**: Mhmm.
**User guest**: Info, info discipline rest. Y busques
**Cristian Berrío**: Wait. Wait. Reason it.
**User guest**: Inbox. But they'll inbox. Ya te estoy dando el acceso. Está cargando.
**Cristian Berrío**: Veinticuatro.
**User guest**: Hermano, estás, no estás conectado al PNL. ¿Cuál es el código?
**Cristian Berrío**: Veinticuatro.
**User guest**: No, no eras tú.
**Cristian Berrío**: No, sí, veinticuatro.
**User guest**: No, no, no me sé noventa y cuatro, ahora sí. Sí, no está conectado al al VPN.
**Cristian Berrío**: ¿Y tú lo tendría pagado?
**User guest**: Igual no utilizas chat, ¿no?
**Cristian Berrío**: O sea, ahorita lo estaba utilizando en chat. Que hay veces que mi mi Internet se pone lento y se pone aún más lento, si Ajá. ¿Qué pasa con
**User guest**: Exacto. Sí, pero a nivel de VPN, creo que no utilizar VPN tanto como antes, porque chat se estaba viendo inútil.
**Cristian Berrío**: Alright.
**User guest**: Qué locura decir eso, ¿ah? Qué chat, se está moviendo
**Cristian Berrío**: Literalmente. Los los está rompiendo mucho, lo siento.
**User guest**: Sí, voy a cancelar pronto chat. Va a ser un día interesante el día que, de nada. Ya estoy listo, yo ya no utilizo chat, honestamente. Yo chat no... Hanno utilizzato
**Cristian Berrío**: Okay.
**User guest**: So, esto de equipo cloud cien por ciento. Ok, Véndete, buscas sandbox. Las palabras Sandbox.
**Cristian Berrío**: Mhmm.
**User guest**: Sandbox, y va a haber un correo de Will, y Say, que dice discipline risk playbook test account.
**Cristian Berrío**: Ajá.
**User guest**: Vete a correo inicial. Ellos mandaron.
**Cristian Berrío**: Good morning, Luis.
**User guest**: Eso.
**Cristian Berrío**: Uh-huh.
**User guest**: El link me tienes el link, usa el username, usa el password, doguéate, entro al sandbox, a la cuenta de sandbox, y nos vamos a copiar, básicamente, una empresa de software para compañías como Disciplined Rift, nos dieron acceso a un software, el software que ellos crearon para el manejo de deportes para niños. ¿Qué tipo de funciones tienen aquí? Creación de equipos, creación de equipos, o sea, fíjate que hay diferentes tipos de equipos. ¿Te acuerdas la academia de club, de voleibol club?
**Cristian Berrío**: Sí.
**User guest**: Esa academia de voleibol club tiene tiene equipos formados que continúan jugando por un año completo. Esos equipos, o sea, primero que todo, tienes registración de trials. Entonces, trials es el día donde, como se, de prueba. El día de prueba, donde vienen todas las niñas a jugar, a ver quién se queda en el equipo y quién no. Entonces, el entrenador va seleccionando las niñas de la registración que entran, y la selecciona de un equipo. Entonces, esta esta plataforma tiene funciones de software para hacer todo ese proceso. Tiene funciones de software también después, para comunicarse con para comunicación con papás, para cobrarle a papás la membresía del club. Para para postear los los juegos que tiene ese equipo. Entonces, tiene una cantidad de, claramente, la área de club no es una área que actualmente estamos trabajando en discipline rest, y no es una área que vamos a desarrollar a nivel de software, Lo que sí quiero es que que extraigas absolutamente todo, no sé si es posible, no sé qué se te ocurre hacer claramente, tenemos acceso ¿Pudiste hacer login? ¿Metiste en los credenciales?
**Cristian Berrío**: Sí, estoy cacharrando,
**User guest**: Pero funciona la cuenta, ¿no? Es que yo no he metido.
**Cristian Berrío**: funciona.
**User guest**: O sea, yo me he metido, pero con ese creditors, yo revisé todas esas funciones con ellos, básicamente, como un cliente futuro. Ellos no piensan que yo me voy a meter aquí a a sacarles la el jugo de cómo hacen sus cosas. Pero eso es lo que vamos a hacer.
**Cristian Berrío**: Mhmm.
**User guest**: Entonces, nada, el punto es, sacar toda esta información, que está dentro de esta dentro de esta plataforma. Todas las funciones que tienen, No necesitamos la lógica que ellos tienen, sino que necesitamos funciones. Entonces, ¿cómo se ve ejemplo, ellos tienen equipos como los nosotros, ellos tienen equipos que son por un tiempo determinado. Las el los las los equipos que actualmente tenemos, no son equipos de club, son registraciones de equipos de desarrollos, equipos que juegan por un tiempo determinado, que juegan por temporada. ¿Cierto? En DVR nosotros trabajamos por temporada. En club, tú trabajas alrededor de un solo equipo, no es una temporada, sino es un año completo. Entonces, no necesariamente tienes
**Cristian Berrío**: Alright.
**User guest**: necesitas otro tipo de funciones, estas funciones para
**Cristian Berrío**: Club de club es for suplicit.
**User guest**: comunicarte con papás, ¿ah?
**Cristian Berrío**: Ajá, por suscripción.
**User guest**: Esa es
**Cristian Berrío**: Club es por suscripción.
**User guest**: es software.
**Cristian Berrío**: No, lo del club, lo de
**User guest**: O club. Oh, club, exacto. Es por suscripción, exacto. No es un monthly fee, pagan una suscripción, y la misma plataforma ahí te, Playbook te dice para que le puedas mandar reminders a los papás que tienen que pagar algo, que están behind. Están al día, lo de un lado. Todo eso lo manejas desde ahí. Que nos interesa a nosotros Esas funciones nos interesan para futuro, porque no sabemos en el día de mañana vamos a tener el el club de voleibol de nuevo. Claramente, nosotros somos dueños de miles de dólares que hemos que tenemos en equipos, que son, que deberían estar siendo utilizados ahorita, que no están siendo utilizados porque no está funcionando actualmente. Esto es por múltiples razones y motivos, pero ciertamente el club es un es un mal lugar. ¿Qué pasa? Que ellos en la misma plataforma también tienen equipos que van por temporada, entonces tienen esa información montada, lista para que tú creas tus equipos. También tienen setup para competencias, es decir, para setear torneos. Esto sí lo queremos hacer, yo sí quiero las funciones para setear torneos, porque van a haber algunos torneos donde vamos a registrar o sea, vamos a tener algún tipo de torneo, ya sea de voleibol, pico o lo que sea, y necesitamos que los papás se registren en esos torneos, claramente, en el front donde hay que hacer algunos cambios para que podamos tener un apartado donde la gente se pueda registrar para Tomeo, ya sean torneos de tenis, torneos de voleibol, torneos de pico, más probable vamos haciendo turnos de pico, creo que eso va a ser lo más lo más viable. Entonces, revise el apartado de torneos, ese como lo tiene desempleado, y cómo lo podemos implementar dentro de discipline rest. El apartado torneo, el único apartado que me interesa más en cualquier otro. Sería superinteresante tenerlo tenerlo ya desarrollado y listo, Y en un futuro, tendremos un dashboard de de de... ¿Cómo se dice? De... ¿Cómo se dice? En vez de papás, academias, digamos que si nuestra academia de voleibol va a jugar contra otras y nosotros estamos somos los dueños de idea es que esas otras academias puedan entrar a un dashboard donde puedan registrar a sus equipos en esa, en nuestras en nuestros torneos y todo eso, y ya. Esa y en esa misma plataforma podemos setear los webs y toda esa información. Entonces, esa es la esa es la la vía
**Cristian Berrío**: So okay.
**User guest**: Pero el apartado de torneos, realmente, como te digo, los torneos pueden variar, las funciones de torneos pueden variar, muchísimo, dependiendo del deporte. No es lo mismo un torneo de voleibol a un torneo de pico, Las registraciones funcionan diferente, la funcionabilidad es diferente, la construcción del torneo es diferente, Yo pienso, yo pienso que una pasarela de torneos sencilla donde simplemente se pueda se pueda registrar, donde se torna sea visible en el front end, y simplemente las personas paguen Podemos darle esa información en el back end, así está como lo tenemos por temporada. Que mostremos como que un estilo conferencia. A las nueve comienza esto, las diez esto, a las once esto, mostramos esa información en el front end, como que por horas qué es lo que va a suceder, hasta ahora juega tan tan tan edad, hasta ahora hasta ahora jugar a tal edad, y así. Que esa información luego salga en el backend de que papá se registró para un en específico, y que y que entre, eso sería lo lo ideal. Esto no lo vamos a hacer para voleibol como tal, lo vamos a hacer es para como T-cobo es uno de los deportes que más está creciendo en en Florida, este, tenemos oportunidades de crear todo el mercado de pick up, porque tenemos acceso a canchas que que las construy tenemos, son como a diez canchas.
**Cristian Berrío**: Okay. Ok, ok. No, que te iba a decir que o sea, entiendo lo de los torneos y eso, y, bueno, estoy cacharrando aquí, ¿No encontró los de los torneos? La verdad, pero sea, haciendo toda la parte de registración y memberships y todo eso. De los torneos, uno lo ha encontrado.
**User guest**: Mhmm.
**Cristian Berrío**: Pero, o sea, lo lo que tú extraiga la información ya sea para para, pues, para lo nuestro, copiar así, o cositas que puedo duplicar el
**User guest**: O sea... Exacto, exacto.
**Cristian Berrío**: registraciones, y evaluar el tema de
**User guest**: Ejemplo,
**Cristian Berrío**: cuando si Ajá.
**User guest**: No, no, dale, ¿evaluar el tema de qué?
**Cristian Berrío**: Y ahora ahora el tema de de de suscripciones para más adelante. O de torneos.
**User guest**: Excepciones, probablemente no o sea, sería, si si digamos que ellos tienen un buen flujo de submisiones, sería bueno sacar información de una vez, por si acaso. Claramente, esto va depender si scrapear esta información, extraer la data de cómo funciona todo, es difícil, este, ciertamente, vamos a, no vamos a extraer todo. ¿Cierto? Porque claramente extraer algo va a tomar tiempo, y no quiero gastar el día completo extrayendo información, que no sabemos si vamos a utilizar todavía, me parece un gasto de energía y tiempo. Si esta la información no es tan difícil como como lo estoy pensando, y es más sencillo, Este, entonces, ahí sí es más, se se vuelve más sencilla la cosa, porque simplemente en vez de pasar el día completo, activamos cierto nivel de función, que nos va a ayudar a a implementar todos los cambios que que queramos hacer. Poco a poco, ¿cierto? Extrasto a la data, y no no se adelantos. Sí, en el en el caso de que sea difícil extraer, porque claramente nunca nos hemos metido en una es primera vez que nos metemos en software externo, tratando de extraer información, Nunca hemos hecho esto antes. En mi es lo que yo recuerdo, si extraes la información, es más difícil de lo que pensábamos, lo que pienso que podría suceder, es que job proprietor academy, Groveland FL tres cuatro. Un segundo. Call you in five. Ya, que ahorita estoy envía a una escuela con Jacina, y Jacina está perdido. Ok, ya resolví. Entonces, nada, vamos a extraer las funciones que nos parecen cool, Por ejemplo, si tú ves que si te gusta la visibilidad del del del dashboard, del dashboard de de entrada,
**Cristian Berrío**: Mhmm.
**User guest**: Está estaría bueno como que extraer como que qué es lo que está mostrando. Cuáles son las, cómo tienen segmentado la información en el backend, Como que literalmente esto es puro backend, ¿cierto? Realmente, Floren no lo no lo conocemos actualmente. A nivel de backend, puede que tenga la información organizada de una manera o te tenga sentido. Claramente, con un punto de referencia un software, que relativamente sea bueno, Yo no son lo mejor, como que no son tampoco como que, guau, esto está increíble. Pero ciertamente tienen experiencia trabajando con organizaciones como nosotros y han hecho cosas chéveres que podemos adoptar. Entonces, extra la información, extráelo todo si es si es sencillo, Si es difícil, nada más extra lo que te parece que es cool, y utilizamos eso a medida que vamos, que hoy es el día de aprovechar de implementar las funciones que queremos nuevas, mejorar las diferentes áreas que pensamos que se puede mejorar.
**Cristian Berrío**: Okay. Okay. Me suena. Today is
**User guest**: Fíjate que, para conseguir este este dashboard acceso, me costó poco. Pero se logró. Así que ahora que lo tenemos, podemos aprovecharlo.
**Cristian Berrío**: Aquí hay dos links. Está user side link, admin site link.
**User guest**: Correcto.
**Cristian Berrío**: Fuerte situación. Voy a utilizar playwright para ver si es capaz de de meterse. Y sacar la información. Si es así, pues coronamos, porque no me toca nada a mí, sino que el mismo playwright puede hacer eso. Pero Si le doy las credenciales, yo creo que él puede entrar.
**User guest**: Excelente. Hagámoslo. O si no, buscamos la vuelta. Debe haber una manera de hacer esto. Simplemente hay que conseguirla.
**Cristian Berrío**: Creo que sí alcanzo
**User guest**: Hermano. Este, ¿estamos claros por lo que vamos a hacer hoy? Bien.
**Cristian Berrío**: Sí, día de auditoría, auditor.
**User guest**: Sí. El ticket de salida es que que, bueno, ya después de hoy, el ticket que salía para hoy es que después de hoy tengamos todas esas funciones implementadas activas que cuando me vaya a meter de forma meticulosa, a revisar todo, no tenga una lista de cien cosas que que, ajá, que podrían ser diferentes, o sea, tú y yo sabemos, tenemos un año ya trabajando esto, Está funcionalidades de de Doctor, sabemos que funciona, sabemos que no funciona. Lo hemos utilizado de forma operacional, en el día a día a día, así que esa respuesta ya la deberíamos poder aterrizar, así que
**Cristian Berrío**: Correcto.
**User guest**: cuando termine hoy, vamos a ver cómo nos sale toda la vuelta.
**Cristian Berrío**: Si cambio que sean, pues, de prone, que tú me dijiste que ibas a hacer. Herpano, te iba a preguntar,
**User guest**: Adelante.
**Cristian Berrío**: que estoy perdido con las fechas.
**User guest**: Adelante.
**Cristian Berrío**: Tú sabes que yo yo firmé el contrato el viernes, el jueves, no me acuerdo exactamente. Eso se refleja
**User guest**: Ajá.
**Cristian Berrío**: la otra semana.
**User guest**: Correcto. Esta semana se, o sea, el que estamos trabajando pagos retroactivos, entonces, bueno, retroactivos no, simplemente retroactivos a nivel de lo que hace lo que hace en una semana se recompensa el y el mes siguiente. Entonces,
**Cristian Berrío**: Okay.
**User guest**: ni sé eso desde el principio. Entonces, claro, ya esta semana estás en unos salarios, simplemente que lo has reflejado la semana. El de la que gané.
**Cristian Berrío**: Okay. Okay. Sí, sí, es que tenía la duda de si se reflejaba la otra, o la otra otra.
**User guest**: Sí, sí, es un poquito confuso, pasa es que es la mejor manera de poder tener track de qué es lo que sucede de poder trabajar de manera proactiva y no retroactiva, en el sentido de que digamos que si yo mando pagos de la de una semana a semana, algún tipo de cosa va a suceder, algún tipo de cosa va a pasar, entonces, en vez de hacer cambios, simplemente se espera el próximo viernes, vamos tener idea de lo que sucedió, y se hace el pago. Esto aplica más en roles que son no salaried, sino hourly. Que que por ejemplo, coaches que se les paga por hora, Entonces, si ellos un día no fueron a práctica, claramente no se puede hacer práctica. Entonces, el el la semana siguiente van a ver eso reflejado. En tu rol como con salario, es un poquito más nonsense, porque claramente es lo que todo tiende tiende a ser el mismo ritmo. No hay mucha variación. Aparte, o sea, si necesitas un día afuera, no tenés sin problema. El problema es que que ciertamente ahorita tenemos regulaciones y eso para para PTO hay un folder en el home de de tres lists que tengo que explicar en un video y montando ustedes una reunión, explicarles cómo funciona todo eso. Pero el punto es que como estos son que yo trabajo, para las otras empresas, yo los mantuve así para tres días, entonces, Trellis, básicamente, traemos lo que que todas las otras empresas, y por eso no sé si

_Sincronizado por Brain: 2026-10-17T22:29:07.929Z_
