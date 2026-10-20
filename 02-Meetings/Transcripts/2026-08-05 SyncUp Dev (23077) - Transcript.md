---
brain_note_id: "dest:meetings:9dc18e79c6b5aa56b17f34981cd2d3f4"
canonical_key: "meetings/9dc18e79c6b5aa56b17f34981cd2d3f4"
brand_id: "meetings"
---
# Transcript — 2026-08-05 SyncUp Dev (23077)

## Transcript

- Reunión: [[02-Meetings/2026-08-05 SyncUp Dev (23077)]]

**User guest**: Que van a estar visitando nuestro website el día de mañana, ya sea su IP, ya sea su el tipo de teléfono que tienen. O sea, ahí para, este es juego profundo, Fíjate, algunas plataformas como Amazon, diferentes para las formas de ecommerce, Cambian, tienen tienen tienen una un una modificación que se llama flex, precio flexible. Que el precio cambia dependiendo del tipo de iPhone que la gente tenga, el tipo de teléfono que la tengan, si tienen un iPhone, si tienen un Nokia, la localización en donde están. Que está en una localización más cara, más más te da tu perfil, y te tengo un buen teléfono, un buen equipo, los precios van a ser más altos, están en una zona más baja y tienen un equipo un teléfono un teléfono de menor, de menor, calidad, el precio baja, Entonces, lo que me refiero es, nada más con la información que podemos acceder con las con lo que las personas entran a nuestro website, podemos recaudar Vamos a hacer, vamos a estar vamos a minar la Necesitamos averiguar cuáles son tipos de mecanismos necesarios, o sea, que cuáles son los tipos de mecanismos en los cuales esta data se utiliza dentro de los ads. Pero el primer paso es buscar una forma de extraer esta data cuando los papás entren. Apenas llenen la forma, apenas entreguen al website, apenas interactúen con el website, que le que le prendamos el tema de las cookies, Yo no sé qué es lo que tengamos que hacer, o sea, realmente, no sé cuáles son las que vamos a tener que implementar, utilizar dentro de website, pero el punto es que necesitamos que dentro del website de haya múltiples capas implementadas para poder minar la información de nuestro ASPs el día de mañana.
**Cristian Berrío**: Aló. Aló, aló, aló.
**User guest**: Del del coach.
**Cristian Berrío**: Hermano, ¿te estás trabando? No te escucho.
**User guest**: Estoy mala señal. ¿Me escuchas?
**Cristian Berrío**: Habla otra vez, sí te escucho.
**User guest**: Dos uno dos. Uno, dos, uno, dos, uno, dos. Christian, uno dos, uno dos. Aló, aló. Uno dos, uno dos, uno dos.
**Cristian Berrío**: Ahora sí te escucho.
**User guest**: ¿Me escuchas?
**Cristian Berrío**: Ahora sí.
**User guest**: ¿Cuál fue la última parte que escuchaste?
**Cristian Berrío**: Excarto a la data. Hasta ahí que
**User guest**: Okay. Vamos a, exacto, vamos a mirar toda la data. Hay, todas las personas que estén interesadas, todas las personas que entren al WhatsApp mañana, quiere decir que recibieron un flyer están interesadas en el programa, se metieron a tratar de registrarse o a buscar información para registrarse, y se, así se registran o no, son ICPs, ICPs. Entonces, todos son ICPs. Qué? Porque vamos a hacer, nosotros vamos a hacer ads, localizados por la geografía, vamos a ads targeted a una locación específica, para las cincuenta y cinco escuelas. Vamos a hacer ads en cincuenta y cinco diferentes lugares. Uno para cada escuela. Dentro de cada escuela, van a rodar esos ads y la idea es que esos ads estén targeted para nuestros ICPs. ¿Cuál es nuestro ICPs? Un un papá de un niño que va a la escuela, un papá de un niño que va a la escuela. Literalmente, ese es el ICP. Este, ya ya con llegar a eso, ya ya ya al llegar a esa persona, estamos estamos logrando, o sea, logramos, lograr que que el app funcionara. Este, por eso es importante buscar los diferentes parámetros, las diferentes variables de data que podemos reconectar y minar el día de mañana con los padres, Y esto, no sé, va a ser a través de los forms, a través del cookies, yo no sé, cómo lo vamos a hacer. Pero hay que implementarlo hoy, que todo esté mañana. Mete esto de Chrome pídele a a ChatGPT, a perplexity, que cree un prompt, averiguar los diferentes mecanismos que existen para esto. Agarra todo lo que dice, mete un prompt y hagamos y investiguemos y hagamos research a ver qué es lo que qué es lo que existe.
**Cristian Berrío**: sea, probablemente Google Ads ya tenga eso implementado nativamente. La cuestión es cómo le pasamos la información.
**User guest**: Como creativamente.
**Cristian Berrío**: Sea, Google Ads, ya nativamente, lo de los target
**User guest**: No, no, nomás hacer el Google Ads, nomás hacer Facebook Ads, nomás hacer Google.
**Cristian Berrío**: Ah, ok, ok.
**User guest**: Pero ¿qué vas haciendo el qué? ¿Start qué?
**Cristian Berrío**: No, oro los target audience. O sea, que
**User guest**: Oh, claro.
**Cristian Berrío**: salga distinto para diferentes
**User guest**: Todos, o sea, claramente, todos Google Ads, Facebook Ads, tienen algún tipo de feature para que te incorpore diferentes orales para llegar a a tu target audience. Ahora, el hecho de que tú crees algunos parámetros dentro de ese target audience no quiere decir que tú vas a llegar a target audience. La idea es que esos parámetros estén específicos y correctos para que los funcionen de manera correcta. O sea, son múltiples cosas que hacen que un ad funcione. El contenido dentro del ad la edición, el mensaje, la la el footage, lo que se está mostrando de forma como como contenido, más todo lo que tiene que ver con, este, todo lo que tiene que ver con la configuración de los ads como tal. Aquí, audiencia, ¿Qué qué qué edad? Etcétera, etcétera, etcétera. Ahora, nosotros estamos haciendo Google Ads como los hace el vecino, El vecino ni siquiera tiene websites propios, ni siquiera tiene ni siquiera tiene, es dueño de su propio código, no tiene tampoco un equipo para para trabajar en development, nosotros sí. Nosotros podemos llegar a una una una a una capa más profunda, nosotros podemos hacer Google Ads, digo, Facebook Ads, Vamos a hacer Facebook Ads
**Cristian Berrío**: Aló. Aló, ¿no, no?
**User guest**: Nosotros vamos a más
**Cristian Berrío**: ¿Está te está trabando, hermano? Trabando.
**User guest**: Aló, aló. Volví, ¿me escuchas?
**Cristian Berrío**: Aló.
**User guest**: Uno dos, uno dos.
**Cristian Berrío**: Quedé hasta la parte de variables.
**User guest**: Sí, básicamente, hay hay dos variables aquí. Una configuración de ads que nosotros hacemos manualmente, o sea, como que estimando bueno, nosotros estimamos que los papás que tienen un niño que van a la escuela están entre la edad de los treinta, los cuarenta y cinco. Etcétera, etcétera. Vamos a configurar todos esos, todas esas variables. Ahora, hay otra capa de profundidad, para la para la configuración de ads, que tiene que ver con algún tipo de mecanismo que que es profundo, que es bastante técnico, para configurar ads, tiene que ver con nuestro, que tiene que ver con la data que nosotros en el website. ¿Hay alguna manera? Porque la gente lo hace, las compañías grandes lo hacen, las compañías pequeñas que son buenas en marketing lo hacen, lo he visto. ¿Algún mecanismo que te permite utilizar la data que viene del website para este, para hacer ads en van a esa audiencia. Ya sea a ese mismo usuario o a usuarios similares a ese usuario que ingresó a tu website. Y llenó la forma, etcétera, etc��tera.
**Cristian Berrío**: Okay. Paso uno, mira lo de la El paso dos ya es orientado a apps,
**User guest**: No, yo ni tengo ni idea. Los pasos los vamos a identificar. Una vez metas todo esto en perplexity, chat, podamos hacer research. O sea, primero que todo necesitamos entender que es posible, o sea, que cómo funciona esto, cuál es el mecanismo, qué podemos qué podemos implementar, data se puede extraer Todas estas todas estas preguntas necesitamos responderlas para poder entender cómo vamos a hacer que esto funcione.
**Cristian Berrío**: Ok, pero
**User guest**: No vamos a planificar pasos sin saber esto, pero primer paso sería eso, o sea, saber cuál es el mecanismo, saber qué datos se pueden extraer, y como estos datos se incorporan dentro de Google Ads, Paso dos, implementación. Si hay algún tipo de cosas que hay que implementar dentro del website de Doctor, para que esta data se pueda extraer, hay que implementar eso. Este, y básicamente, tener un sistema donde podamos guardar toda esa data, y tenerla lista para el momento en que vayamos a lanzar y configurar los ads. Para ese momento, ya necesitas saber cómo tú vas a utilizar esa data dentro de Google Ads, pienso que hacer pruebas de un solo golpe estaría ideal. Es decir, si el mecanismo te dice, que la se puede utilizar para configuración de ads, sea, no es suficiente con leer eso de ChatGPT y ya, darle adelante. No, hay que hay que hacer una prueba, agarra el IP, crea uno crea un set de action en Facebook, y vemos cómo se incorpora, o sea, cómo se implementa. Porque hay unas cosas que son que lo que dice ChatGPT o lo que dice una planificación, no es lo que en realidad es verdad.
**Cristian Berrío**: Correcto. Yo recuperé ahorita lo que acabaste de decir. Entonces, yo ya tengo el prompt de lo primero que hablamos, que es recopilar información. Le agrego acabamos de hablar ahora, o primero el corriente la
**User guest**: Sí, agrégale, agrégale esa prompt.
**Cristian Berrío**: Ok.
**User guest**: Sí, agregar eso a prompt. Porque se nos hace un prompt incompleto, no, no estaría suficientemente grueso. Agarraste la información de ClickUp, ¿no?, la el de ClickUp.
**Cristian Berrío**: Sí. Lo corrompe el plexi. ¿Lo corre en perplexity o...? O el de
**User guest**: Perplexity chat?
**Cristian Berrío**: el mismo prompt.
**User guest**: Correcto. Facúrate cuando le den perplexity. También modo a deep research. Dentro de perplexity.
**Cristian Berrío**: Sure.
**User guest**: La idea es poder extraer un buen jugo el día de mañana, cuando lanzamos los ads, cada cada dólar que se gaste en ads vaya hacia el ICP, porque vamos a poder tener la data. No muchas empresas tienen la capacidad de de tener acceso a exclusivamente, a puros usuarios de, o sea, fíjate que nosotros en discipline rest, siempre los webs tienen algún tipo de variabilidad. Es decir, ponte que tienes un tráfico de mil personas en un website de ropa, pero no sabes si ponte que te voy decir PC en personas que mujeres, porque ropa para mujeres es que hacen ejercicio. Entonces, ponte que tengas mis personas que van a tu website. La mujer, mil personas no. No son mujeres que hacen ejercicio, ¿me entendés? Están en algún tipo de bardialidad. En cambio, el día de mañana, el tráfico que vamos a ver en discipline rest va a ser en base a los nuestros ICPs. Exclusivamente. Y, bueno, casi siempre, ¿no?, pero mañana vamos a ver una cantidad de ICPs elevados.
**Cristian Berrío**: So Oh my god.
**User guest**: Que pasó.
**Cristian Berrío**: They they all been el código? De perplexity.
**User guest**: Cuatro cinco nueve ocho seis cinco. Serious right now. Nada, ¿has visto algo, te ha salido algo?
**Cristian Berrío**: Sí, sí, ya me acaba el prompt. Ya lo voy correr en en todos lados.
**User guest**: Se cae el chat. ¿Mande?
**Cristian Berrío**: El problema chat. O sea, le metí todo lo que hablamos, hacer meeting, the whisper, y déjame acabar el Solo lo voy meter en y todo eso.
**User guest**: Sí, me es muy pronto en chat, y me meto a cancelar, a ver qué qué te sale.
**Cristian Berrío**: Sí, o sea, ¿qué se demora?
**User guest**: Alright. Got it.
**Cristian Berrío**: Tranquilo.
**User guest**: Corretto, corretto, corretto.
**Cristian Berrío**: Demora bastante.
**User guest**: ¿O es el de de perplexity.
**Cristian Berrío**: No, todos tienen, hasta Claude tiene.
**User guest**: Ahí está clic. Research.
**Cristian Berrío**: Sí.
**User guest**: Interesante. Sí, es una función bien útil, la verdad. Muy útil.
**Cristian Berrío**: Ya, ya los tres están corriendo.
**User guest**: Dale, buenísimo, hermano. ¿Te tuve una reunión ahorita a las once? Te das información y necesitas mi decisión en base a lo que vamos a trabajar, avísame, pero creo que la lógica de lo que vamos a hacer de lo que va a suceder el día de mañana, todo lo tenemos los dos estamos claros. Lo que sí tenemos que tener cuidado, hermano, es en que no dañemos el WSDR, lo que sea que hagamos. O sea, es preferible no hacer nada hay que hacer algo y que todo se nos venga abajo y que ni siquiera los ICPs de mañana se puedan registrar.
**Cristian Berrío**: Igual lo que yo te dije, por ejemplo, los videos que te monté, yo eso lo utilizó con, eso se se hicieron con es decir, sabes que playwright es literalmente como si yo estuviera navegando, hundiera un botón, hundiera el otro botón, me registrara
**User guest**: Correcto.
**Cristian Berrío**: sea, como si si lo toman manualmente, pero lo hace en la computadora. Entonces, él maneja el mismo flujo que manejaría una persona del común. Entonces, yo lo probé con una cuenta, que tiene, o sea, una cuenta que ya tiene estudiantes registrados en en temporadas anteriores, y por eso o sea, lo mandé a registrar un nuevo estudiante, como si fuera un padre nuevo, y registrar a estudiantes que ya tenía en esa cuenta.
**User guest**: Claro.
**Cristian Berrío**: Entonces, o sea, el flujo en to end para pares nuevos y pares viejos, lo realizó. Y, pues todo funcionó perfectamente.
**User guest**: Excelente. Bueno, el punto es que también te metas tú desde un punto de vista humano, lo analicen. Como que play, el hecho de que playwright lo haga no significa que es perfecto. ¿Entiendes?, porque a lo mejor, playwright se fue por la lista de padres y revisó que todo esto esté bien, pero la lista de padres, lista de escuelas son cincuenta y cinco escuelas, entonces, no funciona. O no es eficiente para y cosas así, ¿me entendés? Entonces, importante tener esos puntos en en mente.
**Cristian Berrío**: Pues sí, pues sí. Ok. Bueno, entonces, voy a correr todo esto. ¿Los tres? Después lo uno, para ver qué decisiones tomo. Después, cojo cable y los
**User guest**: Acabó.
**Cristian Berrío**: y lo mejor se echan en el PTO. ¿Cómo?
**User guest**: Me acaban de decir que mi reunión va ser cancelada, así que no voy a tener la reunión a las once. Pero igual avísame cuando cuando termines.
**Cristian Berrío**: Ok. Dale, sea, ¿después lo junto a todos, los los tres archivos que me dé. Y, pues, ahí te lo muestro yo. Se saca en conclusiones.
**User guest**: Activo.
**Cristian Berrío**: Listo, hermano. ¿Color y Rosa te voy avisar un tos? Vale.
**User guest**: Dale, dale, bye.

_Sincronizado por Brain: 2026-10-20T02:02:08.695Z_
