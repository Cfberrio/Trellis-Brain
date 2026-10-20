---
brain_note_id: "dest:meetings:825f8327fdbe90a0dafa0728147ac5e9"
canonical_key: "meetings/825f8327fdbe90a0dafa0728147ac5e9"
brand_id: "meetings"
---
# Transcript — 2026-08-14 SyncUp Dev (23437)

## Transcript

- Reunión: [[02-Meetings/2026-08-14 SyncUp Dev (23437)]]

**Cristian Berrío**: Aló.
**Luis Torres**: Buenos días. ¿Cómo está todo?
**Cristian Berrío**: Excelente, excelente.
**Luis Torres**: ¿Puedes descansar ladito?
**Cristian Berrío**: Sí, ahí, dormí.
**Luis Torres**: Fire. Ok, vamos a darle play. Este, ok, ok, ok, ok. Te comenté hace ratico, en el en el soft test sobre sobre escalopearla la estructura de ads, He estado leyendo todo, claramente es mucha información que revisar, No lo no lo revisé con tanto detalle como lo revisé ayer, pero ciertamente puedo ver que que hay una diferencia clara la manera en que los MDs están escritos. O sea, como te dije, no estamos tomando la palabra de de estos expertos como que hace fuese la palabra final, simplemente es un casos de usuario, casos de de escenarios que que sucede en esta área, Tenemos buena estructura dentro de, este, el framework de de de ads como tal, especialmente en la área de de geolocalización. Referencias de meta, también están buenos esos MDs. ResearchTrail, no, veo que hay un patrón aquí de research trail no no lo revisé muy, muy bien. Más o explícame de qué se trata el research trail,
**Cristian Berrío**: ¿En qué parte?
**Luis Torres**: Básicamente, los research questions o las preguntas que estábamos tratando de hacer. Y la respuesta a esas preguntas, me imagino.
**Cristian Berrío**: Exacto. O sea, básicamente, cuando se hacía eso es lo que te estaba diciendo, que Claude o sea, tiene mucho más control en la data que extrae. Entonces, digamos que había una serie de preguntas una serie de interrogantes que queríamos pues, responder.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Entonces, cada vez que se hacía un run, los research run que se hicieron,
**Luis Torres**: Mhmm.
**Cristian Berrío**: que fueron bastanticos, pretendían responder esas preguntas, es decir, si, digamos, que encontraba una página un podcast, un lo que sea, que tuviera información relacionada a apps, antes de extraer esa información, puede buscar esa información. Primero tendría que responder una pregunta, tenía que ver algo con las preguntas esas que están ahí. Así llevamos mucho más control de lo que es con lo que es extraiga y no extrayamos extraer y después tocaba o sea, depurar. Entonces, ahí ya como que llevamos una investigación más Exacto.
**Luis Torres**: Mucho más alineado. Sí, estoy de acuerdo, estoy de acuerdo, me gusta, me gusta, me gusta esa esa orden. Lo que vi que extrajo fue por fue muchos artículos, qué? Artículos especialmente expertos. No nos metimos en tantos días a YouTube, trata sobre la limitación que tiene de leer de leer información disponible online, y lo buscar dentro de redes, entre plataformas de redes sociales, como YouTube, Instagram, etcétera, o o cuál, porque es la razón de por la cual usamos más artículos que nada,
**Cristian Berrío**: O sea, normalmente, ese tipo de persona siempre tiene su su su página web, su su, suscríbete a a sí, o sea, a la lo que sea, como que ellos tienen como que esa información
**Luis Torres**: Bueno, el SQO tienen información, pero normalmente tienes que tener algún tipo de acceso a esa información, ¿no? Por ejemplo, si tenemos un lead magnet que te mandamos la información, si pones tu correo. Entonces, ¿cómo Cloud pone el correo? O sea, ¿cómo Cloud accede a eso?
**Cristian Berrío**: No, por eso, o sea, digamos que la información que ellos manejan normalmente, en los videos información la publica. De alguna manera u otra, la ya sea por newsletter o o lo que sea. Entonces, ¿qué es lo que pasa? Al momento de extraer eso, es complicado Bueno, es un poco bastante, bastante complicado. Meternos cien por ciento a ¿Cómo se dice eso? A vídeos de YouTube y eso. Porque, o sea, eso ya una demora increíble, o sea, extraer información de YouTube o de videos, o sea, ya se demora absurdamente. Entonces, yo vi que Claude identificó una página, se llama Foxwell digital, que ahí, básicamente, la mayoría de expertos por no decir todos,
**Luis Torres**: ¿Cómo se llama?
**Cristian Berrío**: Alton, Foxwell, Digital. Punto com. Es como un blog.
**Luis Torres**: Okay.
**Cristian Berrío**: Que, por ejemplo, ahí, esa es la ese es el blog de la página de de de del experto que encontré, que se llama Andrew Foxwell.
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Por ejemplo, hay otra persona, si yo otra página, que se llama search, engine line, y ahí también otros artículos. O sea, extraemos más artículos que videos porque los videos se nos quedan cortos.
**Luis Torres**: Era más era lo más sencillo que, era lo más rápido y efectivo que podíamos en el momento.
**Cristian Berrío**: Exacto. Entonces, cada experto, etcétera. O sea, yo hice varios runs. Y los dividí de la a a la e. Y para cada rom, intentaba llevar un flujo de que extraje la información, y extraje la información de documentación real. Entonces, como que así dividí las cosas, Por ejemplo, de la a, de a uno a tres, es más que todo research de nuestro website, qué es lo que hacemos. O sea, cuál es nuestro perfil de de o sea, perfil de de personas que queremos tarjetear? Para los ads.
**Luis Torres**: Mhmm.
**Cristian Berrío**: El b era de budget, de volumen, eso era más que todo, información de documentación. Y de expertos también de cómo manejan ese tema de budget.
**Luis Torres**: Mhmm. Mhmm.
**Cristian Berrío**: El C uno al C el c uno al c cuatro, Allí. El segundo, el c cuatro, más que todo, información de expertos. O sea, ¿de qué evidencia real existe? Que se esté usando ahorita mismo? Y así, o sea, como que dividí todo eso, todos los se dividieron en como que extraer información global y específica, de qué se está haciendo en apps. Tanto expertos como documentación actual, de de Meta.
**Luis Torres**: Te pregunto, ¿piensas que es necesario redes sociales de YouTube o te sientes cómodo con los artículos que tenemos? ¿Sientes que es necesario hacerlo?
**Cristian Berrío**: O sea,
**Luis Torres**: Porque si Cloro es el que lo hace y lo podemos hacer de una manera controlada, cuando me refiero, cuando habla de una manera controlada, en en ciencia, cuando tú trabajas, hay un ambiente controlado, quiere decir que tú estás guiando cada paso de proceso, tú tienes control sobre el ambiente en el cual estás desarrollando, trabajando. El caso tuyo, tú creaste una research un research questions que crea un ambiente controlado para la investigación que hiciste. ¿Cierto? Que Cloud va a hacer esto, Ahora, si Claude puede hacer esto y también podemos videos de YouTube, pero normalmente se va tardar más, Le pregunto, ¿es posible hacerlo dentro de un ambiente controlado donde durante el día de hoy, vaya extrayendo esa información?
**Cristian Berrío**: O sea, ¿y sí podemos utilizar API, por ahí? Porque IC Cloud no no, o sea, no
**Luis Torres**: Ahí, ese club me llega, Sergio.
**Cristian Berrío**: No, no. O sea, lo que podríamos hacer, porque igual, o sea, sería demasiado, y estoy seguro que, si lo puedo correr, igual se demoraría absurdamente bastante. Es
**Luis Torres**: ¿Puedes dejarlo en una computadora
**Cristian Berrío**: capturar.
**Luis Torres**: si quieres, también.
**Cristian Berrío**: Sí, pero es igual, toca estar pendiente darle o sea, o sea, estar pendiente de de, por ejemplo, cuando termine un run, porque no puedo todo en seis días, sino que lo tengo que hacer así como en batches. Así como hice este este run ahorita.
**Luis Torres**: Okay.
**Cristian Berrío**: Me tocó hacerlo de la a a la e en batches, porque hacerlo entonces, ya te da no te da lo que es.
**Luis Torres**: Okay.
**Cristian Berrío**: Y lo que puedo hacer, entonces, es coger los videos de las personas que tenemos aquí, y coger dos, dos, tres videos buenos. Más de ahí,
**Luis Torres**: Resietas.
**Cristian Berrío**: ya siento que Exacto.
**Luis Torres**: Recientes.
**Cristian Berrío**: Suficiente más de ahí.
**Luis Torres**: ¿Piensas que esto es algo que te va a consumir como que toda tu intención si lo trabajas? O puedes dejarlo un lado a lo mejor, través de remote access y como que verle irleando en el teléfono mientras? Nos enfocamos en otra cosa.
**Cristian Berrío**: Sí, o sea, ¿sí lo puedo ir dejando así, o sea, lo puedo ir dejando corriendo,
**Luis Torres**: Porque, por ejemplo, en mi caso, cuando me toca hacer algo que me que me toca dar la autorización, sea, claramente primero dejo lo de allow access indefinidamente. Pero si necesita mi atención, lo dejo en el remote access con el teléfono, que vaya corriendo, y voy revisando mientras trabaja la computadora, eso es normalmente lo que yo hago.
**Cristian Berrío**: No, sí, igual, o sea, igual, yo lo puedo dejar corriendo. Es que lo que estoy haciendo ahorita, o, por ejemplo, lo hice ayer, es que, por ejemplo, utiliza ChatGPT para todo el tema del y eso se lo pasaba a Claude. Digamos que Claude me pasaba me me pasaba un output del resumen de qué fue lo que hizo, así detallado. Entonces, ese output lo cogía, se lo pasaba a ChatGPT, con los MD que había generado. Entonces, como que era un proceso de back and forth de de de ChatGPT, ChatGPT revisaba todo, Sí, esto era lo que tenemos que cumplir. Trajo la información correctamente. Ahora continuemos con el paso del b b uno al b b ocho. Y como que así, o sea, y atrás con el chRPT, y y
**Luis Torres**: Correct.
**Cristian Berrío**: Como son videos, y cada ron se va a demorar bastantito, No creo que tenga que estar así, como que de un lado otro. O yo yo lo puedo dar corriendo realmente.
**Luis Torres**: Okay.
**Cristian Berrío**: Cuando termine, pues. Me doy cuenta y copio el
**Luis Torres**: Okay.
**Cristian Berrío**: el output que dejó, la información, y se lo aprovecho repetir.
**Luis Torres**: Listo. Fíjate que yo me siento cómodo con la información que tenemos ahorita. A diferencia de ayer, siento que tenemos suficiente información para movernos hacia adelante, Sin embargo, me gustaría me gustaría tener más fuentes que solo artículos, Realmente, los artículos están bien estructurados, nos están dando la información necesaria, y lograr nuestra información para comenzar. Definitivamente, sería bueno extraer videos si podemos hacerlo, así que si puedes dejar eso a lado, mientras vamos desarrollando lo que tú estás a punto, lo voy a mostrarte ahorita. Sería excelente. Este, compartir rapidito. Ahora, vámonos a, entonces, bueno, ya quedamos así con eso. ¿Piensas que es posible?
**Cristian Berrío**: Sí, sí. ¿Podemos hacer otra cosa, mientras?
**Luis Torres**: Listo. Ahora, vamos a prepararnos espacios dentro de Meta Ads con toda la configuración y los creativos que vamos a a postear. Los creativos como tal, le está haciendo unos le está haciendo unos cambios este, ya tengo los scripts, ya tengo todo listo, Vamos a crear la estructura de los ads como tal. ¿En base a qué? La estructura ads que tenemos claramente Estás viendo mi pantalla, ¿no?
**Cristian Berrío**: Sí.
**Luis Torres**: Estoy compartiendo, ok. Este, fíjate, que nosotros no podemos lanzar nosotros tenemos equipos para que más o menos entiendas la la gravedad del asunto. Yo estoy aquí, yo estoy aquí en este punto en este punto azul. Nosotros tenemos equipos que están aquí, en estos son los equipos de Scopters, si tú te recuerdas de esos equipos. Tenemos muchísimos equipos aquí, tenemos bastantes aquí, muchísimos aquí arriba, bastantes aquí, de este lado a la izquierda, algunos aquí en esta área abajo, algunos aquí en esta área arriba, abajo a la izquierda, y tenemos uno por aquí, tenemos dos aquí en esta área de Klarna. Entonces, el punto es, el punto que te voy a ahorita voy a dar es necesitamos poder montar una estructura que nos permita atacar los ads en cada en cada locación específica. ¿Cómo se llama las locaciones? Bueno, pues, están aquí. Aquí están. Bueno, tú también sabes esta promoción. Aquí están. En la database, de de info, en info hay una database que se llama o veinte sea dos veintisiete. Pero están todas las escuelas que vamos a, en las cuales vamos a hacer ads. Aquí te muestro la escuela, el deporte, el deporte, escuela del deporte, que es los deportes que estamos corriendo. A escuelas donde que yo te voy marcar aquí, escuelas que te voy a marcar aquí en structure, que donde no le vamos a hacer ads. Si tienen el strike, significa que no vamos a hacer ads en esa escuela. Qué no vamos a hacer en alguna escuela? Porque, por ejemplo, hay escuelas donde las registraciones se llenan solas, yo lo hablamos. Yo ya sé cuáles van a ser esas escuelas, no todo, no no me tienes que dar esa No te estoy pidiendo esa información. Una razón y ya la tengo. Ya sé cuál escuela se me va a llenar. Sé cuál escuela son son buenas para este tipo de de flujo. Así que el punto ahora es, que el punto ahora es, que vamos a lanzar los ads dentro de la locación dentro de una locación de este, Okay. Los ads los vamos a los vamos a correr a una a cuatro millas Sí, cuatro millas, para decir que es apropiado. A cuatro millas dentro de cada escuela. Entonces, vamos a darte un ejemplo. El ejemplo va ser a water ray. Water ray. Hum. Fíjate que me lanzó. A la, esta es una escuela que queda abajo a la izquierda. Eso nos podemos lanzar de desde un punto de vista general, no sé, Busco la orden allá en ¿Perdón? ¿Andrés no se va el carro? No está él, pero ¿Mandiote cargando? Necesitaré con los carros. Ahora miro.
**Cristian Berrío**: Thank you. Thanks.
**Luis Torres**: Ok, entonces, a Water Bay... No. Tenés que buscar, vamos a buscar elementary. ¿Nos podemos ir a la al a la a la locación como tal. Esta es una buena manera de verificar que la locación de la escuela es la correcta. Sí, esta es la escuela. Entonces, este ad como tal, lo vamos a correr a cuatro millas de esta área. Es decir, vamos a agarrar toda esta esta warver de mente, vamos a agarrar estas cuatro millas, estas, bueno, de aquí a cuatro millas, cuatro millas son como es como un círculo de este tamaño, más o menos. Más Cuatro millas, a la dirección de la escuela. Vamos a tener cada ¿Ah?
**Cristian Berrío**: Que tú, básicamente, estás diciendo que cada escuela, como tal, va a tener unos sea, un tipo de at distinto, sea, van a haber at distinto entre escuelas. Cuatro
**Luis Torres**: Los ads van a ser dependiendo... Ok. La variación es locación, la la número uno, primera primera capa, es variación de de locación. La variación va a ser en que cada en que cada locación, vamos a correr apps en diferentes locaciones. Sencillo.
**Cristian Berrío**: Mhmm.
**Luis Torres**: Partiendo de la locación de la escuela. Que claramente aquí te estoy mostrando que es esta. Segunda capa, dependiendo de los deportes que tenemos en la escuela, vamos a correr, cuatro ads creativos. ¿Por qué vamos a correr cuatro ads? No sabemos cuál ad va a tener un mejor engagement. Claramente, no podemos lanzar un ad y cruzar los dedos a que funcione. Para esto podemos hacer la función que de obvio de de... ¿Cómo se dice? Cuando la misma plataforma te permite como que le da, le lanza diferente dinero a los ads, dependiendo del performance, ¿cierto?
**Cristian Berrío**: Uh-huh.
**Luis Torres**: O lo podemos hacer manualmente. Como que le damos un budget a todos los creators, y dependiendo del performance de cada creator, y como que el resultado, los click trucks de cada creative, le añadimos después más dinero a un, le quitamos budget a un creative y se lo damos al otro. Y así.
**Cristian Berrío**: Okay.
**Luis Torres**: Este, vamos a tener tres videos y un y una un como con Flare, una foto estática. Una foto estática hacia un movimiento, y tres videos. Esos van a ser los ads. No, mentira, vamos a tener exacto, tres videos y dos, dos, dos fotos estáticas. Dos, dos creators estáticos. Esto lo vamos a lanzar para absolutamente todas las escuelas que no tengan el Structure. Aquí yo te voy a poner, en un ratico te voy a poner la las que vas a tener en structure. Tenemos aquí actualmente, tenemos cuarenta y ocho, van a terminar siendo como treinta diferentes locaciones, Entonces, lo que necesitamos hacer dentro de Google Ads, dentro de Google Ads, perdón, no, perdón, dentro de Facebook Ads, es la estructura utilizando la información que se levantó el día de ayer, anoche, a nivel de cuál es la mejor estructura para nuestra para nuestro problema, para nuestro producto, para nuestro servicio, utilizando esto que está aquí. Claramente, también, utilizando imagino que dentro de los artículos vas a poder imagino que ellos montan cosas visuales, Claramente, LMD y Claude va a tener una una habilidad limitada de mostrarte de cómo se ve la estructura que se monta atrás de cada app. Entonces, por eso es que tú vas a tener que entrar a, bueno, si algo no hace sentido o si está metido dentro, mira, ah, si confundido, a nivel de estructura, de cuál es, cómo vamos montar los creatives, cuál va a ser el audience targeting, cuál cuál estrategias vamos a utilizar para los ads, en base a toda esta información que se levantó sería bueno que te vayas a no a un MD como tal, o que le pidas, o que le des los MDs a Claude y te pueda guiar, en cómo tomar esas decisiones, o agarrar los en Dish y metérselos a GPT, para que GPT te pueda guiar, no tengo ni idea de cómo vas a poder llevar lo que son MDs la creación de estructura real dentro de dentro de de ad management.
**Cristian Berrío**: Uh-huh. Sí.
**Luis Torres**: Aquí está la el database, te voy a dejar ahorita, voy a ahorita revisar cada una de las escuelas. Voy a darle a structure a las que no vamos a lanzar ads, y te mando un mensaje confirmando que estamos listos.
**Cristian Berrío**: Okay. Bueno, sea, bueno, yo voy coger esta toda esta información, y voy a ir cacharreando como funciona Metax Ya cuando tú me pases, las escuelas que no van, y, pues, los creativos, ahí ya vamos montando eso.
**Luis Torres**: Sí. Si quieres, por ahora, este, como que establece las deja los creativos de último, que montamos los creativos de último,
**Cristian Berrío**: Ven acá, una pregunta. Al final, nosotros solucionamos el tema de de meta ads. De Doctor. Que creo que era la el que estaba molestando, algo así.
**Luis Torres**: el de Cisco share. C2Share, que tuvimos que crear la la cuenta de Catering. Qué nos nos bloquearon la cuenta en dos mil veintiuno? ¿No hablamos así?
**Cristian Berrío**: Ah, sí, sí, ya. Sí. Sí, me
**Luis Torres**: Y eso está
**Cristian Berrío**: El de de dar está bien. Acordé.
**Luis Torres**: Sí. Esa fue una muerte COVID, muerte veinte veinte, porque no hay no hay resucitación a este punto. Crear la cuenta de para lanzar los ads por allá. No,
**Cristian Berrío**: Así es. Bueno, entonces, voy a ajustar eso que que dijiste. Al final, que quede claro. Que quede claro y que quede en en clic o lo de los lo de escoger las escuelas y hacerle cuatro millas, eso nos va a servir para segmentar. Que es lo que vamos a mostrar. Localizas.
**Luis Torres**: Cierto, porque fíjate que no, cómo funcionan las escuelas allá, A lo mejor eso es algo que te tengo que explicar. Tipo, cuando tú vas a primaria, ¿cómo tus papás escogen en la escuela que tú vas a ir?
**Cristian Berrío**: O cercanía.
**Luis Torres**: ¿Allí en Colombia?
**Cristian Berrío**: O sea, bueno, por cercanía, no. Aquí es por o sea, privado. Y
**Luis Torres**: Sí, por escuela privada o pública.
**Cristian Berrío**: tipo, religión.
**Luis Torres**: Sí. Allá, los que fue determinante son el la calidad de la escuela, claramente las privadas tienen más calidad, y la algunas de las algunas son escuelas católicas, etcétera. Bueno, en el caso de esta lista de escuelas que nosotros tenemos, si es realmente escuelas católicas, escuelas cristianas, la mayoría, aquí del sistema de escuela público funciona. En el sentido de que son escuelas de buena calidad, etcétera. En algunos casos, bueno, en el caso de las que nosotros tenemos, sí funciona porque tenemos escuelas que donde los papás tienen donde hay buena donde hay una buena segmentación hay buena segmentación monetaria, o sea, una geolocalización, de personas con buen con buen income. Entonces, en el caso nuestras escuelas, como estas escuelas son fundadas por el estado, sí, Depende de la locación, si son buenas escuelas o y y funcionan. Entonces, el punto es, si tú por ejemplo, todas las personas que viven en estar en esta en todas estas casas que están aquí, este, son y tienen niños que son de edad elementary, van a estar a esta escuela. La escuela tiene, dependiendo la escuela, si está una zona rural o no, las escuelas tienen entre dos millas a quince millas de este, de radio. De radiolocalización. ¿Qué pasa? Que en zonas rurales son como más como quince millas, en zonas no tan rurales son en zonas densas, como ciudades grandes, etcétera, son como dos millas, en zonas un poco en el medio, donde no tienen tanta densidad, son cuatro millas. Entonces, por ejemplo, en el caso de está aquí viven miles de familias en esta organización, Esta es una organización gigante, Este, digamos que cubre alrededor de, tiene unas tres, cuatro millas de de cobertura. Entonces, nosotros vamos a lanzar el ad para que se segmente esta a esta a esta población. De esta escuela. Ya que, las reglas de las escuelas públicas está prohibido que alguien que viva aquí, fíjate que aquí hay otra escuela, se llama Sagres,
**Cristian Berrío**: Compartiendo, porque no.
**Luis Torres**: ¿Qué estoy compartiendo?
**Cristian Berrío**: O sea, creo que es la otra pantalla.
**Luis Torres**: Ok, ahora sí. Ok. Estamos dando la organización de aquí. Creo que no entendiste mucho. Pero bueno, esta escuela le pertenece a toda esta organización. Digamos, aquí hay miles de familias, aquí hay como RDOT, cuatro o cinco millas. De esta escuela, a las extremidades de de todas estas casas de aquí. Ahora, alguien que vive aquí, y esta es su residencia, su casa, no, las reglas van en contra de alguien que vive aquí, vaya a esta escuela. Puede que esta escuela sea mejor que esta, pero como tú vives en esta locación, te toca ir a esta escuela. Ahora,
**Cristian Berrío**: Ya entré.
**Luis Torres**: Exacto. Entonces, esa lógica nos permite a nosotros decir, bueno, si nosotros tenemos la escuela, o sea, la lógica es, sabemos el área de la escuela, sabemos dónde queda, check. Google Ads nos permite utilizar geolocalización, Sí, check. Entonces, vamos a crear diferentes Mismo asset, mismo asset, a lo mejor, duplicado, a lo mejor creamos copias de los mismos assets, para diferentes localizaciones. No sé cómo podemos segmentar eso. Pero sí necesitamos saber, o sea, tenemos que tener cuidado en la estructura de apliquemos, porque necesitamos saber si los ads de esta escuela estamos están funcionando. Porque si creamos ads para esta escuela, creamos ads para esta escuela, debajo de un mismo asset ¿verdad?, y no nos permite ver si los si si la población de esta escuela está cliqueando o la población de esta escuela está cliqueando, está inscribiéndose, registrando, o tiene un aquí tenemos muchos clics, y no tenemos registraciones. Y aquí tenemos muchas registraciones pero no tenemos tantos clics. Eso no, claramente, queremos queremos más registraciones y menos clics. Porque esa es la idea de del ad, ¿no?, eso es lo que nos vean y que nos que sepan que son más bonitos. La idea es que nos vean, puedan ver que, efectivamente, este, guau, increíble lo cerca que queda esto.
**Cristian Berrío**: Yes. O sea, en pocas palabras, lo de lo de hacer lo del radio, eso. Es más que todo para controlar las registraciones que estamos teniendo. Más que para lanzar un creativo específico para esa zona.
**Luis Torres**: Correcto. Todos los creativos van a ser la única variabilidad que van a tener los creativos van a ser el deporte. Para devolver, vamos a lanzar un set de creativos y para flag football vamos a lanzar un set de creativos. Vamos a tener más a ser para voleibol y para flag fútbol.
**Cristian Berrío**: Ok, ya entendí, entendí. Ok. Bueno, ya me queda todo claro.
**Luis Torres**: Excelente. Excelente. Vamos a darle play, vamos a ver cómo nos va. Este, monta, empieza a montar la estructura dentro de dentro de dentro de los ads, Si quieres hacer un poquito de de preparación, viendo que puedes dentro de Cloud, a ver si te puede ayudar a a a evitar el trabajo manual, siéntete libre de hacer lo que quieres hacer. Con tal de que quede con tal de que quede bien, Yo estaré trabajando en terminar los creativos para que, al final de ser al día de hoy, dejemos esos creativos en en todas las locaciones.
**Cristian Berrío**: Listo. Entonces, bueno, Ok, bueno, voy a extraer toda la información que tengo ahorita. Con la conversación que tuvimos. Creo en nuevo chat, y ahí voy viendo. Qué qué qué se puede ir haciendo.
**Luis Torres**: Activo.
**Cristian Berrío**: Listo, hermano.
**Luis Torres**: Activo, activo,
**Cristian Berrío**: ¿Qué más?
**Luis Torres**: Pero, bueno, acuérdate de utilizar toda la información extraímo, o sea,
**Cristian Berrío**: Sí, sí, sí.
**Luis Torres**: toda la información que traemos acerca de estructura de ads es para ti, para que tú entiendas cómo vamos a lograr, o sea, es para ti para poder entender la implementación. ¿Cierto? Claramente es para todos nosotros, porque el beneficio y la oportunidad de ads está en la estructura que nosotros logremos implementar.
**Cristian Berrío**: Sea, ¿voy a extraer todo lo la carpeta de knowledge que tiene expertos y tiene official meta, Los research run no no es necesario realmente. Y todos los todos los outputs. Y ya.
**Luis Torres**: Listo.
**Cristian Berrío**: Esa es la información relevante.
**Luis Torres**: Ajá. Y, la mejor, mientras corres eso, vas extrayendo los videos de YouTube de los de los creators en una sesión de cloud.
**Cristian Berrío**: Sí, o sea, a ver, pero, o sea, vamos a traer los videos de YouTube enseguida, pues no sé qué quieres que haga ahora mismo. Para extraer los videos de YouTube tengo que hacer una planificación con chat también, porque API five no es como que, ay, extrae esto, O sea, API, literalmente tienes que pasarle un archivo a ajá, un archivo de Python para que lo corra.
**Luis Torres**: No, por supuesto. Pregunta, ¿hay un hay un donde tú puedes controlar API fases de clon?
**Cristian Berrío**: Sí, sí, yo, ahorita mismo está en el CPS.
**Luis Torres**: Este instalado está listo. Tenemos cinco dólares, me dijiste, que nos quedan, ¿no?
**Cristian Berrío**: Ahorita, bueno, con lo que hicimos ayer, nos quedan como tres dólares, más o menos.
**Luis Torres**: Listo.
**Cristian Berrío**: Ahí gastamos como dos dólares.
**Luis Torres**: Excelente. Este, ok, dentro de APIFI vi unos unos runs que se hicieron por redes sociales, algo así, de de algunos contenidos de no me acuerdo. Que era lo que dice que se hicieron que si la semana no sé, hiciera un test o algo así,
**Cristian Berrío**: Mhmm.
**Luis Torres**: pero no deberíamos estar haciendo runs ahorita por API de entre esos sean de Creo que ¿Te acuerdas de eso? ¿Te acuerdas te recuerdas de por qué se hicieron esos rods?
**Cristian Berrío**: El último que se hizo Ayer fue. Facebook ads. No hay, no, bueno, El nueve. Que La verdad es que no me acuerdo. Pero lo voy a frenar. El último fue, ah, no me tiré su phone, n ocho n. Pero esto fue hace rato.
**Luis Torres**: ¿Qué pasó?
**Cristian Berrío**: No, no, no, no, no, esto fue hace rato. Lo que estaba viendo. Los los voy a frenar.
**Luis Torres**: Sí, sí, no deberíamos, o sea, en ocho de enero ya está cerrado, no debería estar corriendo ¿cierto?
**Cristian Berrío**: No. Bueno, aquí sale que el último fue en en junio.
**Luis Torres**: Agosto, ¿no? Junio.
**Cristian Berrío**: No, aquí sale O sea, el el allí research que tengo, fue en junio el último.
**Luis Torres**: Okay.
**Cristian Berrío**: Pero sí, vuelvo a mirar. Si hay algo corriendo y no estoy dando cuenta.
**Luis Torres**: And then background, exacto.
**Cristian Berrío**: Sí.
**Luis Torres**: Ok, listo. Verifica eso, activa la extracción de los videos de YouTube, si es que te está tardando mucho en crear la planificación para API extra, la extracción de los videos de YouTube, Avísame y nos vemos hacia adelante con con lo demás, porque definitivamente no es no es super mega sería helpful, pero no es algo que es super mega importante todavía.
**Cristian Berrío**: Okay.
**Luis Torres**: Y, si puede ser, sería, yo escogería que, en vez de escoger los mismos que estamos haciendo ahorita, expertos similares a ellos. Que expertos que se sepan la vuelta bien dentro de Facebook Ads, que sean esos seguros que venden cursos de setecientos dólares, prometiéndote que que vas a conseguir las respuestas a todos tus problemas.
**Cristian Berrío**: Yeah.
**Luis Torres**: Es una mentira. Pero sí, si podemos tener otros expertos que no sean ellos, sería mejor, aún ya que así incluimos más variabilidad en la respuesta y entre más personas que nos den información, más llegamos a estar a tener información que es real. No basura.
**Cristian Berrío**: Okay. O sea, bueno, voy estar voy a intentar extraer de dos a tres videos por por nueva persona. Los que ya están.
**Luis Torres**: Correcto.
**Cristian Berrío**: Ver qué tanto se demora. Yo creo que dos dos a tres está bien.
**Luis Torres**: Correcto. Correcto, correcto. Así es, hermano. Vamos a darle, ya sea cuatro millas, cuatro millas de la escuela.
**Cristian Berrío**: Listo. Italy.
**Luis Torres**: Un radio de radio de cuatro millas.
**Cristian Berrío**: Listo.
**Luis Torres**: Dale, hermano. Pensé algo así, estamos pendiente. Cuídate mucho. Mención.
**Cristian Berrío**: Contando.

_Sincronizado por Brain: 2026-10-20T18:14:02.418Z_
