---
brain_note_id: "dest:meetings:fe5e1907ce76e43404e90dba1c1110eb"
canonical_key: "meetings/fe5e1907ce76e43404e90dba1c1110eb"
brand_id: "meetings"
---
# Transcript — 2026-06-30 SyncUp Dev (21857)

## Transcript

- Reunión: [[02-Meetings/2026-06-30 SyncUp Dev (21857)]]

**Luis Torres**: Hermano, ¿me escuchas?
**Cristian Berrío**: Ahora sí escucho.
**Luis Torres**: ¿Cómo está todo, Mero?
**Cristian Berrío**: Excelente, excelente.
**Luis Torres**: ¿Cómo te fue en tu en tu cabañita?
**Cristian Berrío**: Ahí es como ahí como con un poquito arriba, pero pero todo bien.
**Luis Torres**: Ahora, ¿ya estás enfermo?
**Cristian Berrío**: No, tengo, me quiere como quedar ahí, pero aún no tengo.
**Luis Torres**: Tomate una pastilla, una broma para que para que pareje el la cadena de eventos
**Cristian Berrío**: Let's see.
**Luis Torres**: Ayayay. Hermano, vamos a darle play. Sobre qué está pasando, el problema.
**Cristian Berrío**: A ver, nosotros tenemos una cuenta de Trellis, todo está y queremos conectar la cuenta de info de Gmail.
**Luis Torres**: Correcto, tenemos una cuenta de cloud a través de trade list y queremos conectar info, sí.
**Cristian Berrío**: Correcto. En un principio, yo lo que hice fue que me metí a la cuenta de Google de Trellis, y creé, pues, los permisos y toda la cuestión y toda la cosa, sea, como como cuando creamos el las cosas en en Facebook developer.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Bueno, es igual y o sea, es distinto, pero es igual. Mismo proceso, te creo una aplicación, la aplicación se conecta a Claude. Entonces, en ese en ese pues, en esa conexión, digamos que me deja realizar la conexión, o sea, todo funciona perfecto, me me deja conectarlo. Al momento de yo mandar un prompt para que haga cualquier cosa relacionada a Gmail, extrae el correo, lo que sea, lo que sea, lo que sea. Me dice que no tengo los permisos. Entonces, yo me puse a investigar en foros, etcétera, etcétera. Y, bueno, me dijeron como que, bueno, en vez de crear la cuenta, Porque yo, como la creé en Trelix, lo que hice fue como que puse un usuario, que es el de info, para que hiciera como que todos los tests. Entonces, me dijeron, bueno, para que no tengas que hacer eso, crea la cuenta, directamente de info, cosa de que no tengas que darle permiso a info, porque él ya es el dueño de la cuenta, o sea, tienes que hacer nada de eso, ya después lo conectas a Claude. Eso es lo que estaba recién haciendo ahora.
**Luis Torres**: Pero es que eso no funcionado, porque el club va a reconocer que Info no puede conectarse.
**Cristian Berrío**: O sea, no sé exactamente si es un book o qué es lo que pasa. O sea, debería ser un book, porque no tiene sentido que la única manera que yo use Gmail es a través de la cuenta que ya tengo comprada, por el mismo Gmail de de Claude. O sea, no tiene sentido.
**Luis Torres**: No tiene sentido.
**Cristian Berrío**: O sea, yo como, o sea, si yo tengo, por ejemplo, una cuenta, dije, de Claude, como lo que queremos hacer de info, que no tiene nada que ver con Claude, no no está en cloud, o sea, no debería, dejar, perdón, conectarse, no tiene sentido que que, única y exclusivamente, la cuenta con la que tienes Claude la única cuenta que puedes acceder a Gmail. No tiene sentido. Lo que te quiero decir.
**Luis Torres**: Sí, tiene sentido porque Claude va a querer desde una perspectiva de negocio, va a querer que quiera que tengas cuentas de Claude con cada una de tus empresas.
**Cristian Berrío**: Bajo ese punto, de pronto, pero el punto es que no no me
**Luis Torres**: Y por eso es que, por ejemplo, tú te metes en MCP, tú no vas a poder conectar un MCP de otra cuenta de Google que no sea la cuenta de Google que está asociada con con Trellis. Porque, de hecho, para para autenticar tu cuenta de de Google, la para tu para autenticar tu cuenta de clusters, tenemos un login con con Google, o sea, lo Google creo que no tenemos credenciales de cloud, ¿cierto?
**Cristian Berrío**: No.
**Luis Torres**: Exacto. ¿Y podemos crear credenciales de cloud? Y no tener no tener asociado a cuenta de Google,
**Cristian Berrío**: Porque igual estaría asociado al mismo correo. O sea, habría que, pues, eliminar la cuenta y volverla hacer ya, pero es que, de todas maneras, voy a decir exactamente... No, mentira. Bueno, no es de nuestra, no es de no es de entrar y y me dejó con la etapa.
**Luis Torres**: Acuérdate que ahora está, acuérdate que Cloud trabaja bajo un modelo de negocios donde No les importa a las personas que estén logged in, en la cuenta, a pesar de que todos estén trabajando desde la misma cuenta. Por ejemplo, cien porciones pueden estar conectadas a CloudTrailist, y no va a hacer ninguna diferencia porque todos están usando la misma cuenta de Trellis. Nada está saliéndose.
**Cristian Berrío**: Ya igual puedo mandar ticket, porque igual no perdemos nada mandar el ticket. Porque ya, agoté mis recursos creativos, Incluso, ChatGPT me dijo, ¿sabes qué?, mando un ticket. ChatGPT ya no se le ocurre más nada literalmente. Me dijo que mande ticket.
**Luis Torres**: ¿Y por qué no haces la otra la otra forma, donde le des permisos de de Trellis a info?
**Cristian Berrío**: Ya lo hice. O sea,
**Luis Torres**: ¿No te dejó?
**Cristian Berrío**: ajá, o sea, lo que hice fue, esa fue la primera que hice, desde el mismo Trellis, creé toda la aplicación, toda la conexión, y puse a info como usuario, administrador. Salé literalmente todos los permisos de la aplicación, se lo di a info, Ah, eso fue la que hice al principio. Después fue que la hice al revés. En vez de crear un lo creé en y después de lo conecté a Claude.
**Luis Torres**: Y no te dejo.
**Cristian Berrío**: No, Incluso, lo puse en en, o sea, la aplicación la puse en testing, publiqué la aplicación para ver si de pronto era que publicando me dejaba. Sea, pero es literalmente todo lo que me decía ChatGPT. Hasta el punto en el que ya me dijo, manda un ticket, porque ya nada que hacer. Borré cookies, eliminé conexiones, O sea, todo lo que te puedas imaginar,
**Luis Torres**: Sí, mando el ticket, pero en base a la segunda opción, no la mandes en base a la primera. Digo, en base a la Manda ticket en base a la primera opción, no en base a la segunda. Como que mira, era una cuenta con nuestra cuenta de necesitamos otro administrador para esta cuenta que creé para de MCP, y no me está ir lo que sea que sea el error, me están los terror. Algo así.
**Cristian Berrío**: Sí, porque, o sea, ves que lo raro es que te deja autenticarte. O sea, como tal, conexión sale que ya se estableció. Porque te autentican, o sea, te sale la pestaña de Google, pones el usuario de info, la contraseña, enter, o sea, te sale todo perfecto, no sea ningún error, el problema es cuando ya intentas hacer algo útil, escribir cualquier cosa en Gmail o extraer cualquier información de Gmail, ahí te sale que como si no tuvieras permiso. Como si no fueras un usuario autenticado.
**Luis Torres**: Ah, bueno, mándale eso. Pero en base a la primera opción, no le no le hagas el segundo, porque, o sea, Cloud no va a querer que te lo digo que desde el punto de nivel de negocio, Cloud quiere que nosotros tengamos una cuenta de Cloud con info. Fíjate, si tú tratas de hacer lo mismo para los correos de trailers, probablemente lo podrías hacer. Sería bueno hacer una prueba.
**Cristian Berrío**: So O sea, que que que extraiga la del del Trellis. De los correos, así me
**Luis Torres**: Exacto, que extraigas algo de los correos o trates de de hacer que funcione, a ver si funciona. Pero obviamente va a funcionar. Eso te diría a ti, que el problema no está en la función, el problema está en quién está usando la función.
**Cristian Berrío**: Sí. No, y el problema es que Gmail no tiene un MCP nativo. O sea, no tiene algo así ya creado. Por ejemplo, de Supervis, literalmente, con un comando, lo y le di login a Supervis. Así ha sido con la mayoría. O sea, la mayoría de click up, todo eso, ha sido literalmente con un comando. Gmail, por por el contrario, o Drive o Google como tal, lo tienes que hacer a mano. O tienes que ir una aplicación y después de esa aplicación conectarla, o sea, todo es muy manual.
**Luis Torres**: El todo, el el setup del es manual, básicamente.
**Cristian Berrío**: Exacto. Me imagino que es por lo de Gemini. Imagino que es por Caja. Conflicto de intereses con Gemini support.
**Luis Torres**: Supuesto.
**Cristian Berrío**: Pero no, no deja no deja hacer la conexión directa con con Claude. Sí, frenó la mitad de la planificación de hoy.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Igual, de pronto, lo que podría hacer en lo que mando el ticket y eso, para extracción de correos, podría probar utilizando Playrate, que el Playrate, tú sabes que es como que accede a tu computador, y hace todo lo que tú puedes hacer.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Siempre y cuando, pues, obviamente, uno lee las credenciales.
**Luis Torres**: Mhmm.
**Cristian Berrío**: Podría intentar maybe, dándole las credenciales de info, para ver si si puede acceder y no, o sea, no si Gmail no lo no lo saca porque es un bot, podría intentar
**Luis Torres**: Mhmm.
**Cristian Berrío**: como que toda la explicación, que él lo extraiga manualmente, toda esa y la ponga en un en un archivo.
**Luis Torres**: Eso es, no.
**Cristian Berrío**: Como una solución así,
**Luis Torres**: Me suena. ¿Por qué no pones el playwright en una en una de las otras laptops nuevas?
**Cristian Berrío**: Él lo tiene. Yo se lo había puesto a ella. Ay, tipo, yo se lo había puesto.
**Luis Torres**: Yeah.
**Cristian Berrío**: No puedo dejar corriendo ahí.
**Luis Torres**: Sí.
**Cristian Berrío**: O sea, ya no
**Luis Torres**: Sí. Sí. ¿Tiene las credenciales de enviar puestas ya también? O tienes que ponerlas?
**Cristian Berrío**: Okay.
**Luis Torres**: En la en las computadoras de Doctor,
**Cristian Berrío**: No, o sea, igual las puedo poner, eso no me da. Porque igual el el el autenticadito de ahí es el el número de D.R. Entonces, yo lo tengo aquí.
**Luis Torres**: Sí. Extraigamos los correos con ¿Qué más vamos a hacer? Mi entrada, mientras ha cerrado el MCP. Pero eso sí, o sea, Sí, creo que la única manera extra de corroborar eso, y si acaso, Ahorita estamos utilizando n ocho n para la documentación de correo, ¿cierto?
**Cristian Berrío**: Sí. O sea, manda con pocos correos y y el chatbot. Y el chatbot de, perdón, el Gmail agent que responde correo. Y los research que hace también. O sea, en HD nos da bastantes cositas ahorita bien.
**Luis Torres**: Mhmm. Buenísimo. Sí, bueno, manda el ticket a ver qué qué te dicen. La chat que te haga un buen caso con el email, a ver si si
**Cristian Berrío**: Igual, él ya tiene todo el contexto de qué es lo que está pasando el chat.
**Luis Torres**: Exacto. O sea, hazlo estratégicamente, de manera de que no sé, te puedan dar en la en la luz verde.
**Cristian Berrío**: Okay.
**Luis Torres**: Porque yo, genuinamente, pienso que es a propósito.
**Cristian Berrío**: Probablemente.
**Luis Torres**: Esa, esa es mi esa es mi teoría.
**Cristian Berrío**: Una pregunta. Lo de lo de trellis game que tú montaste, ¿tú al final solucionaste o
**Luis Torres**: Sí, ya, ya, soluciono, ya está listo.
**Cristian Berrío**: Te iba a preguntar, como vi el post, yo dije, sé si la habrá solucionado o qué.
**Luis Torres**: Sí,
**Cristian Berrío**: ¿Lo diste por por Instagram,
**Luis Torres**: Sí, lo hice por creé una función en ManyChat. Que es como básicamente, una un tool de automations, nativo en Instagram y Facebook, que me responde la gente a eso.
**Cristian Berrío**: programa ahora, entonces.
**Luis Torres**: ¿Qué cosa?
**Cristian Berrío**: Ya no me ya no me necesita.
**Luis Torres**: No, no fue fue fue eso, náhuara. Más bien eso fue un dolor de cabeza demasiado estúpido, demasiado sencillo, y fue fue tedioso hacerlo porque lo hice mal. Entonces tuve que volver a hacerlo. Hacerlo bien, etcétera.
**Cristian Berrío**: Okay. Bueno, voy a estar yendo, entonces... Ah, pregunta. ¿Revisaste al final
**Luis Torres**: Adelante.
**Cristian Berrío**: lo de discipline brief para hacer la migración de domain, correo, todo eso.
**Luis Torres**: Sí, de hecho, tengo una, un documento de revisiones que que estoy terminando. Lo revisé todo, pero te estoy mandando feedback. Entonces, bueno, está listo, así que hay que esperar a que lo termine.
**Cristian Berrío**: La idea es que
**Luis Torres**: Probablemente hoy
**Cristian Berrío**: Mhmm.
**Luis Torres**: Estoy esperando a terminar otras cosas y montarme en esas revisiones.
**Cristian Berrío**: Ya. Pues la idea es mirar todo eso enseguida. Antes de que Berzel cobre el siguiente mes de de facturación de
**Luis Torres**: ¿Cuándo cobran a siete más?
**Cristian Berrío**: Buena pregunta. Ya dejé de reviso.
**Luis Torres**: ¿Bertha no está cobrando? No, Versa no nos cobra.
**Cristian Berrío**: No cobra.
**Luis Torres**: No.
**Cristian Berrío**: ¿Es seguro?
**Luis Torres**: Por el hosting,
**Cristian Berrío**: Sí, no.
**Luis Torres**: Creo que no nos joda. Lo que se va a fallar, el con nuestra base de datos. De hecho, Lobo nos mandó un correo sobre nuestra base de datos, el Lobo, que no entendí.
**Cristian Berrío**: No, no envié un correo. Lo hago. Ah, no, versus no los cobra tierra, so. ¿En dónde nos envió? Más bien, ¿cuándo lo viste?
**Luis Torres**: Ya va. Add funds to continue using low services. Star, Vea vea los los correos de star. Me mandaron ayer el correo.
**Cristian Berrío**: Deja y reviso
**Luis Torres**: Activo.
**Cristian Berrío**: No, tenemos.
**Luis Torres**: Mi pregunta es, es ese correo que necesitamos fondos?, ¿qué significa ese correo?
**Cristian Berrío**: A ver. Sabes que lo bajo él tiene. Tanto el el hosting del domain base de datos, también modelo en el que tú puedes escribirle prompts y que haga cosas. ¿Verdad? Tiene muchas que eso te lo embute en todo, en una suscripción dizque de veinte dólares. ¿Verdad?
**Luis Torres**: Ajá.
**Cristian Berrío**: Pues eso es completamente viable. Cuando tú tienes, no sé, hay que decir tres websites, dos websites, Nosotros ahorita mismo tenemos seis websites funcionando. Cada uno con su base de datos. Obviamente, por Randy Thailand event venue.
**Luis Torres**: Pero para eso no le hacemos un upgrade a la supresión.
**Cristian Berrío**: Sí, sí, sí. Pero lo que te quiero decir es, nosotros le dimos un update al plan que ya tenemos o sea, de veinte dólares, lo que le dimos upgrade fue a los créditos. No al plan como tal. Porque la base de datos funciona es con créditos, entre más cosas haga, no sé, entre más información nos llegue, más usemos la base de datos, Por ejemplo, con lo que sea, Ahora, con discipline rift, sobre todo, con discipline rift metimos una hoja de O sea, un año de base de datos, en un día, pues, obviamente, ahí fue donde se agotaron los créditos. Entonces,
**Luis Torres**: ¿La suscripción incluye créditos?
**Cristian Berrío**: la suscripción incluye créditos, claro. Entonces, ahorita nosotros tenemos cien
**Luis Torres**: Y se nos están acabando ya de nuevo.
**Cristian Berrío**: No, no, no, no, no, escúchame. Nosotros, el la el mes pasado teníamos cien. Recuerda que el mes pasado hicimos cheese to share, e Renewable OS. Los tres, prácticamente, trabajamos fue todo el mes pasado. Entonces, usamos demasiado logo. Y demasiado las bases de datos. Lógicamente, nada más con una suscripción pasada, no, solo tenemos cien créditos. Ahora lo que fuimos ahora lo que hicimos fue que aumentamos eso el dólar, ahora tenemos doscientos créditos. Salió eso ayer porque aún no se habían recargado los créditos del mes. Y como ya como te digo, el mes pasado lo usamos demasiado, para todo, pues, realmente, se nos estaba acabando. Ya este mes ya está en doscientos otra vez, y ya prácticamente terminamos pues, la mayoría de cosas que que o sea, ya terminamos lo lo más pesado, ya no vamos a trabajar en cuatro websites distintos, sino que dos, tres websites, ¿sí?
**Luis Torres**: Correcto, porque ahorita estamos a Lobo Pro. ¿Cierto?
**Cristian Berrío**: Exacto. O sea, seguimos en lo hago el pro, pero con más créditos. O sea, seguimos con la misma suscripción, porque la otra es como de de business or enterprise, que, literalmente, o sea, no nos agrega nada nuevo, nos da los y nos da los mismos créditos. O sea, nos da como que unos features ahí, pero los mismos sin créditos, el otro no no nos sirven sin créditos.
**Luis Torres**: Ah, ya entendí.
**Cristian Berrío**: Nos sirven son doscientos créditos.
**Luis Torres**: ¿Esos créditos se consumen también por la base de datos?
**Cristian Berrío**: Claro. Con la base de datos se consume. Entonces, claro, yo miré toda una base de datos completa Obviamente, o sea, los cien que teníamos literalmente pasaron a diez, y fue cuando te dije, hey, no tenemos créditos.
**Luis Torres**: Ahí subimos a doscientos créditos al mes.
**Cristian Berrío**: Claro. La migración se comió todos los créditos? Literalmente.
**Luis Torres**: Entendido. Entendido. Entendido. Entendido.
**Cristian Berrío**: Sí. Por ejemplo, mira, aquí está. Discipline rift, consumió ciento cuarenta y siete créditos. El mes pasado.
**Luis Torres**: Base de datos, que que consume toda esta base de datos,
**Cristian Berrío**: Ya digo. Pero vamos ir a como ahorrando y vendenio. Que a y Benvenio no le metemos mano. Solo consume la base de datos.
**Luis Torres**: ¿Cómo ves eso? ¿Cómo es esa información?
**Cristian Berrío**: En settings. Te vas a
**Luis Torres**: Ok, listo, aquí en settings.
**Cristian Berrío**: With the settings, te vas a plans and credit usage,
**Luis Torres**: Yeah.
**Cristian Berrío**: A la derecha, usage, le deja igual, mira, por proyecto. Por ejemplo, run the un venue,
**Luis Torres**: Cincuenta créditos.
**Cristian Berrío**: Sí. Pero cincuenta créditos en todo el mes. Entonces, mira que ahí, si tú te das cuenta, hay una que se llama build, otra que se llama run. Tú tienes que fijarte, más que todo, en el run. Diariamente,
**Luis Torres**: ¿Dónde está eso?
**Cristian Berrío**: cuando te vas a
**Luis Torres**: Ah, ya.
**Cristian Berrío**: a usage details, la grafía que está a la derecha. Sí, claro.
**Luis Torres**: Build. Ah, okay. Okay. Run.
**Cristian Berrío**: Exacto. Built créditos. Built son los créditos que yo uso, por ejemplo, cuando voy a hacer el repo, yo una función, que no se puede hacer se tiene que hacer sí o sí por por o sea, lo lo hacen específicamente para que tú mandes prompts, obviamente, que consumas crédito. Si no, no hay otra manera de hacerlo. Entonces, si te das cuenta, Nada más corriendo, Orlando y Benvenio, son dos dos créditos al día. Sí, mira.
**Luis Torres**: For Ronald Bill,
**Cristian Berrío**: For run, Built, obviamente, pues puede, fácilmente puede ser cincuenta, si tú le das un prompt muy
**Luis Torres**: Ah, não, foram, sim, foram. Un crédito al día, dice veintiuno punto dos créditos. Por orden de
**Cristian Berrío**: Exacto. O sea, nada más por correrlo son dos al día. Prácticamente.
**Luis Torres**: ¿Cómo que dos al día, hermano? Dos al día fue en cuarenta. Sesenta créditos.
**Cristian Berrío**: Виделло, database. ¿En qué en qué en qué en qué viste esto?
**Luis Torres**: Estoy en run, me parece que son veintiuno punto un créditos para Orlando Benvenio.
**Cristian Berrío**: Me perdí. ¿Dónde está? Aquí. Mira, Por run como tal, son alrededor de dos.
**Luis Torres**: Dos. ¿Por qué dos? A. Por lo que ves ahí.
**Cristian Berrío**: Exacto, o sea, nada más corriéndolo sin yo tirar
**Luis Torres**: Ah,
**Cristian Berrío**: Ajá.
**Luis Torres**: es que comienza el corte en junio diecisiete.
**Cristian Berrío**: Entonces,
**Luis Torres**: Junio diecisiete,
**Cristian Berrío**: Buena pregunta, no tengo ni idea.
**Luis Torres**: That's so odd.
**Cristian Berrío**: Literalmente. Entendí por qué. Oh, ya sé por qué. Mire, O sea, antes no te decían, cuánto consumías. Junio diecisiete te están diciendo cuánto consume correr el modelo.
**Luis Torres**: Es una nueva función, claro.
**Cristian Berrío**: Sí.
**Luis Torres**: Interesante.
**Cristian Berrío**: Un registro más, personalizado. No, sí, o sea, perfecto, porque, o sea, realmente, por cada aplicación se van a correr dos o sea, o sea, por día van a ser dos, ahorita mismo tenemos como cinco. O sea, son alrededor de diez. Aproximadamente. Pero, obviamente, varía. Entre más lo uses, pues más consumes.
**Luis Torres**: Por supuesto. O
**Cristian Berrío**: Pero yo creo que sí nos da.
**Luis Torres**: uses tipo, hasta el backend,
**Cristian Berrío**: Literalmente, todo. O sea, base de datos, network que es que esté deployed, Storage es, digamos que si nosotros guardamos fotos, videos, lo que sea. Y funciones son los triggers que yo te digo, que, por ejemplo, una función que esté mirando,
**Luis Torres**: Con razón, luego está haciendo tanto dinero.
**Cristian Berrío**: Exacto. O sea, es que lo tienes todo y y, en verdad, súper, bajo costo, porque en vez de tener cuatro cosas que te cuestan veinte dólares tienes una cosa que te cuesta cincuenta.
**Luis Torres**: Es lo que queremos hacer, ¿cierto?
**Cristian Berrío**: Claro. Claro.
**Luis Torres**: Ay, pero no nos escapamos, salimos de una cosa para que el precio de otra suba. No no no, ni financiero, no, estás muy feliz por esto.
**Cristian Berrío**: No, pero yo creo que yo creo que Bueno, no sé.
**Luis Torres**: Ok, hermano, entonces, vamos a hacer, mándale el ticket a a Tropic a los a los a nuestros queridos amigos de esperaremos no podemos guardar hacia adelante sin sin eso realmente, sea, necesitamos una manera de poder integrar a Cloud dentro de las otras marcas para Puerra. Mensajes de Pregunta,
**Cristian Berrío**: Pregunta.
**Luis Torres**: una manera de que Gojalavo reciba todos los mensajes del inbox. De correo electrónico, que el inbox de correo electrónico se maneje por Go ahead level. No, es que eso es una locura.
**Cristian Berrío**: O sea, que todo llegue allá.
**Luis Torres**: Básicamente, Porque es que no con jalón, no te veo problema conectándolo a cloud, ¿cierto?
**Cristian Berrío**: Ah, no, sí. Sí es fácil, sí. Sí me dejó. Tú dices que estoy allí acá. Muy buenas
**Luis Torres**: O sea, ¿cómo podemos cómo podemos controlar para que la comunicación con personas se maneje desde gojalao?
**Cristian Berrío**: sea, como tal, es que nosotros tenemos el el email como tal, ya lo tenemos conectado. Al Google Level. La cuestión es, no sé hasta qué punto uno puede o sea, obviamente, pues, la información que nosotros mandamos aquí, es decir, emails, que son automatización, pues, obviamente, los llegan a nosotros. Pero emails que ya son
**Luis Torres**: Externos.
**Cristian Berrío**: distantes a nosotros, o sea, ya son de marketing, de lo que sea cualquier otra cosa.
**Luis Torres**: No, y no es de papás que nos mandó un correo, ejemplo.
**Cristian Berrío**: Por eso, o sea, pero esos son, o sea, sigue siendo información que no sale de nuestro go ahead luego. Sino que sale de un papá que nos escribió al correo.
**Luis Torres**: Exacto.
**Cristian Berrío**: O sea, no sé hasta qué punto. Se podría
**Luis Torres**: Go, al lado, ¿puede ser un el help para eso?
**Cristian Berrío**: Exacto.
**Luis Torres**: Porque en tal caso de que Gohalla use el hub de mensajes, de cualquier tipo de de inbox, ya sea mensaje de texto y correos electrónicos, nosotros podríamos agarrar esa esa esa función para meter a Cloud dentro de Gojat Level y dentro de Gojat Level comunicarnos con papás, y todas las personas. Para respuestas ¿cierto? Para que todos los inquiries de comunicaciones vengan desde go ahead level. Así, no tienes que conectar el MCP de Gmail a Claude, si no conectas Claude a go ahead level, de go ahead level respondes a papás.
**Cristian Berrío**: Correcto. No sé si sería el sueño americano, últimamente.
**Luis Torres**: Si puedes conseguir una manera, de que, ojalá, pueda leer nuestra bandeja de entrada, y recibirla, sería ideal. Especialmente porque tenemos la nueva de go hello. Yeah.
**Cristian Berrío**: Quisiera que sí se puede. ¿Qué tan qué tan común es que un padre te escribo al correo? En sentido de o sea, en el sentido de que no, que llenen nuestro nuestro contact form,
**Luis Torres**: No tan común. Mayoría mandan correos directamente a nosotros, porque dice, fíjate, mandamos un email marketing, responden, o mandamos un reminder, responden. O sea, también es parte de mi pregunta. ¿Desde dónde estamos mandando la mayoría de nuestros correos electrónicos o papás actualmente? ¿Desde Gohan Level o desde área ocho n?
**Cristian Berrío**: N ocho n. Realmente,
**Luis Torres**: Lo vamos a migrar a cosas de nuevo? Esas automatizaciones.
**Cristian Berrío**: Sí se podría, en verdad, son bastante estúpidas las automatizaciones esas. Ahí ya podríamos sí, o sea, no, o sea, sí, si si lo hacemos así, ya podríamos manejar si por x o y motivos no nos deja meter todo el inbox de nuestro Gmail aquí, pues ya manejaríamos una suma considerable de de correos. Porque, como tú dices, la mayoría de veces te responden es a los correos que tú mandas. Por automatización.
**Luis Torres**: Correcto.
**Cristian Berrío**: O por marketing.
**Luis Torres**: Correcto.
**Cristian Berrío**: Más que un correo, o bueno, y si acaso un contact form, pero que te manden un correo así individual, que pongan el el tu correo y manden así, un texto. Es poquito.
**Luis Torres**: Los correos de que mandan Google AdLévo los manda desde info errores discipline rift, que nosotros podemos editar de quién los está mandando.
**Cristian Berrío**: Sí, sí, porque sí, las automatizaciones, uno puede poner el el nombre, y el correo. From
**Luis Torres**: Digamos que si vas a mandarle vas a contacts y le vas a mandar un grupo de personas un correo, también puedes editar eso. Los contactos, digamos que vas a segmentar los contactos de un papá en una temporada después, podemos controlar quién está mandando esos correos al papá.
**Cristian Berrío**: Sí. Tú puedes controlar ¿Qué es lo que vas a mandar? From no, perdón, from name. A ver, espera aquí.
**Luis Torres**: Porque sale group training
**Cristian Berrío**: Porque es la cuenta. La super account como tal, pero tú puedes poner el el de
**Luis Torres**: info. ¿A dónde dime, perdón? ¿Gmail? ¿Aló? Aló.
**Cristian Berrío**: Sí, mira, tú le puedes poner. Nosotros le pusimos Luis, o info. Buena pregunta.
**Luis Torres**: Le pusimos info.
**Cristian Berrío**: ¿Le pusimos info?
**Luis Torres**: Ajá. Creo que el STTP es la configuración que está, hay que cambiar la configuración de los correos, de de dónde vienen los correos.
**Cristian Berrío**: Eso te iba a decir. Eso te iba a decir, porque ahorita mismo tal de Luis. ¿Dónde está? Bueno, ¿que tengo aquí? Es el de Luis, sí, mira.
**Luis Torres**: Okay.
**Cristian Berrío**: Pero creo que... Ah, mira, podemos medir otro. Ok. Podemos añadir todos. Y me imagino que cuando añadamos otro, tú vayas a mandar un correo así,
**Luis Torres**: No, no, no, hay que aprobarlo, aquí no podemos asumir. Haz esa prueba.
**Cristian Berrío**: No, por eso, por eso, por eso. Pero me imagino que cuando ya añadamos otro, te va a salir la opción de que mandes a través de Luis o a través de Info.
**Luis Torres**: Excelente.
**Cristian Berrío**: ¿Tendría?
**Luis Torres**: Ok, entonces, mira lo que vamos a hacer. Vamos a tener a grupos de escuela por día, ¿cierto? Vamos a tener a grupos de escuela por días, vamos a tener grupos de escuela por lunes, martes, miércoles, jueves, viernes, Vamos a tener una lista de esas escuelas por día, vamos a tener un grupo de escuelas que van a entrar en la categoría de ese día en específico, así, si necesitamos mandar un correo de cancelación o lo que sea, simplemente seleccionamos el grupo y le y nos comunicamos con el grupo a través de correos electrónicos. Correos electrónicos de ahora en adelante van a ser a través de GoHad level, Necesitamos trabajar GoHad level para todas las comunicaciones internas y externas, ya Necesitamos asegurarnos de que los domains de Luis arroba discipline rift y e info estén seleccionados. ¿Ok? Estén seleccionados tipo la que tenga la configuración lista. Info y Luis tiene que estar los dos configurados adentro. Info, tiene que ser el correo que esté default, para todas las comunicaciones. Info, Luis va a ser específicamente para correos de marketing. Para que ellos se comuniquen con correos de marketing. Así podemos segmentar y separar comunicaciones que vengan de marketing y comunicaciones que vengan de de de discipline risk, como tal.
**Cristian Berrío**: Correcto.
**Luis Torres**: ¿Quieres SFT provider? ¿Qué es el eficaz?
**Cristian Berrío**: O sea, es lo que utiliza Google. O sea, ¿sí cómo manda la prueba?
**Luis Torres**: Y eso no es accesible, esos mensajes no son accesibles desde el mismo Gmail, ¿cierto?
**Cristian Berrío**: Estos mensajes. Sea, los que llegan aquí en
**Luis Torres**: Sí, exacto, los que nosotros vamos mandando en go ahead level. Qué bien.
**Cristian Berrío**: Ah, no, no, no.
**Luis Torres**: Son específicamente para verlos desde desde
**Cristian Berrío**: Yo te cojo el nuevo. Sí.
**Luis Torres**: DHL. Ok, entonces necesitamos hacer esas configuraciones. De Luis info desde go ahead level. Que info sea default y que Luis esté específicamente para acercar correos de marketing.
**Cristian Berrío**: Okay.
**Luis Torres**: Necesitamos que eso esté listo para poder comunicarnos con papás, faculty, todas las cosas poder conectar, Vamos a utilizar playwright, para extraer toda la data de la información. Esa data de información llévatela a Clico, esa data de información la vamos a luego utilizar en cloud, para que Claude tenga MD, tenga skills, entrenadas en la respuesta de esos correos, ¿verdad?, para que el hemoclova pueda reconocer si es un papá o si es un faculty, a quienes estamos hablando. O un coach. Este, también necesito y y también... Ajá. Papá, coach, playwright. Entonces, vamos a vamos a darle así, playwright, extracción de información.
**Cristian Berrío**: Mhmm.
**Luis Torres**: Extensión de información, skills de clon, Clon reconoce con quién hablamos, papás, coaches, faculty, ¿verdad?, necesitamos alrededor de veinte correos para de papás, diez correos o más de faculty, y diez correos o más de coaches. No pueden ser, cuando estés extrayendo esa data, no pueden ser correos genéricos, tienen que ser correos tiene que ser correos que sean replies, ¿cierto? No correos que estemos mandando a la faculty como tal. Porque yo no voy a utilizar clon Bueno, no voy utilizar cloud, el cloud que tú estás entrenando, el club de tu de entrenamiento es un club de replies, específico para replies. Porque el club de generation de correos va a ser otro clut. No va ser de que tú estás no va ser de que tú estás creando. O sea, como que los skills son diferentes. Hay skills para generación de correos, hay skills para de correos. Y ambas skills funcionan diferente, entonces necesito que cuando extraigas, extraigas solamente replies. De padres, coaches y escuelas, faculty. Una vez extraída esa información, se crean los MDs, y los metemos en en el modelo que estás utilizando para los replies dentro, de go ahead level. Digamos que tenemos un club específico. Cuando tú creas un cloud para responder o hacer algún tipo de función, tú le metes MD, ¿le puedes meter MD en específico? Lo puedes configurar,
**Cristian Berrío**: Sí, sí.
**Luis Torres**: El los skills de clon, y puedes tener múltiples, ¿cierto?
**Cristian Berrío**: Correcto.
**Luis Torres**: Entonces, cuando tú estés extrayendo la información, extrae información de replies y extrae información de emails sent. ¿Cierto? Emails sent a papás coaches y faculty. Queremos email sent, como que email sent, como que el primer correo que se manda. Porque queremos esa información porque tenemos también un modelo de de MD que nos ayude o sea, quiero quiero toda esa data extraída para luego yo crear un correo que me ayude a crear correos para faculty, papás, y coaches. ¿Me entiendes?
**Cristian Berrío**: No. Sí no entendí.
**Luis Torres**: Digamos que le mandamos un correo a faculty, vamos a irnos a a día con un ejemplo. Deja de compartir rapidito, por Cuando yo estoy creando un correo nuevo, lo voy a pasar a un a un a papás, a a coaches, faculty, lo que sea, By the way, recomiendo, creo que tú lo haces, que tengas, tú tienes diferentes Windows de en las diferentes marcas de que tú trabajas, ¿no?
**Cristian Berrío**: Correcto.
**Luis Torres**: Sí, porque si no, mucho arroz con mango. Bueno, esto es como que le dicen, desktops. Diferentes desktops. Ok. El correo inicial es un correo totalmente diferente a los replies que yo les mando a los a los a los a los a faculty. Digamos que los los los la generación de correos, primero, es ¿esto es un correo más sencillo? Probámonos a este correo. Five of our eight students are on vacation this week. Okay. Sorry. Okay. Aquí le estoy diciendo, hola, Mistrella, fíjate que el correo es bien denso. Ahora, el reply no es nada denso, El reply es bueno, aquí ya está, el reply reply son un poquito más
**Cristian Berrío**: Es algo más sencillo.
**Luis Torres**: straightforward. Exacto. La reply so, straightforward. La extracción de correos que tú vas a hacer va a ser específicamente de replies, no de correos iniciales. Los correos iniciales los correos podemos decirle Sí, como que inbound, o outbound, tenemos outbound emails, que es el primer correo, el primer, outbound significa el primer correo que mandamos a una persona, faculty coach. Necesitamos extraer outbound, pero eso es para, eso eso es menos importante. Eso es menos importante, porque en realidad lo más importante para nosotros es lo que recibimos como reply, lo que recibimos como inbound. Reply es para inbound. Entonces, básicamente replies, ¿cierto? Eso es lo que vamos a tener. El modelo, cuando estemos usando playwright, vamos a extraer correos de replies, para generar los MDs, entrenar al modelo para hacer replies. Esto lo vamos a hacer en Doctor, lo vamos a hacer en OVB, lo vamos a hacer en Como te expliqué en la planificación, para llegar hablamos con tres personas diferentes. En OEB, con una sola persona, el cliente. Entonces, claramente, diferentes por eso es que necesito extracción de diferentes tipos de conversaciones en porque diferentes. Conversaciones que estamos teniendo. Cuando cuando estés utilizando play rates, especialmente si lo tienes en otra computadora y no te toma mucho esfuerzo hacerlo, si puedes extraer correos que nosotros mandemos a outbound, que son estos correos que están saliendo de nuestra bandeja que están saliendo de nuestro correo, outbound. Si puedes extraerme correos de faculty outbound, correos de parents outbound, correos de coaches outbound, sería excelente. Así yo puedo agarrar esos correos y desarrollar en ties para entrenar a modelos de cloud, así lo tengo que yo volver a utilizar playwright y meterme a extraer esto, ya que tú ya estás extrayendo. ¿Me entiendes?
**Cristian Berrío**: Correcto.
**Luis Torres**: Y y yo voy a entrar en ese y yo voy a crear esas skills, porque digamos que eso es algo más como que Tinder muy específico, que yo tengo que hacer. En cambio, los replies, sigue siendo específico, pero como igual como es un draft, igual requiere que nosotros le metamos mano, no tiene que ser tan acertado. En cambio, el modelo de los SEOs que yo para el el outbound tiene que ser muy bueno, porque la idea es que entienda la información que yo quiera compartir y ya la pueda crear el mismo. Entonces, básicamente, estamos creando un engine de correos electrónicos, y lo vamos a hacer a través de Go ahead Load, porque creo que el MCP no no va a lograr que te conectes desde desde aquí. Desde info. Eso quiere decir también la mayoría de nuestras comunicaciones de ahora en adelante van a ser utilizadas, van a ser manejadas desde go ahead level. Ya nosotros estamos pagando Go ahead level, estamos pagando Claude, y sabemos que cloud se conecta a través de MCPs a nuestras cuentas de Gohat level, entonces simplemente utilizamos nuestra cuenta de Gohat level, no nos compliquemos no nos compliquemos utilizando cloud directamente, en nuestras otras cuentas. Entonces, Es que yo tengo eso, sorry.
**Cristian Berrío**: Correcto.
**Luis Torres**: Bueno, más y menos lo mismo. La idea es o sea, yo pienso que, en vez de estar construyendo en diferentes áreas, pienso que es mejor construir en áreas donde ya tenemos algo establecido. Es decir, extracción de métricas, Si MCP, si Goja Level ya tiene un MCP que extrae data a nuestro Goja Level, necesitamos construir nosotros nuestro propio MCP, cuando simplemente podemos meter utilizar el MCP que ya está creado, que conecta todas nuestras redes sociales, a a a go ahead level, y go ahead level, lo podemos conectar a Flore. Entonces, simplemente utilizamos el el el MCP. De Claude y GoHub level para extraer la información que nosotros necesitamos.
**Cristian Berrío**: Exacto. Es verdad.
**Luis Torres**: ¿No tiene más sentido eso? Como que across the board,
**Cristian Berrío**: Sì sì sì. Sí, porque el de el Google evo y el cloud ya está conectado. Eso ya está listo.
**Luis Torres**: Correcto. Tú puedes seleccionar el shop account que estás trabajando desde Google's level, sea, todo eso es customizable, ¿cierto?
**Cristian Berrío**: Una pregunta. No me acuerdo muy bien, deje la prueba enseguida.
**Luis Torres**: Porque si no si no hay si no hay especificidad, dentro de Claude, para trabajar en un SOAP account en específico y tener herramientas e información para un SOAP account en específico, esto no va a funcionar. Porque cada cada cada empresa dentro de go ahead level, cada subaccount, tiene, es totalmente diferente a la otra.
**Cristian Berrío**: O sea, yo sé que, por separado, se puede hacer. Pero no me acuerdo si juntas se pueden hacer. Pero ya te digo.
**Luis Torres**: ¿Cómo así? Tipo, ah, porque claro, tú tienes cuentas de subaccounts separadas. ¿Cierto?
**Cristian Berrío**: Eso, O sea, cada sopa es es un mundo interno. Entonces. Hacer la conexión, lógicamente, yo tengo que ir la integración en cada subcuenta. Pero lo que no me acuerdo, lo que no estoy seguro, Lo que no me acuerdo, lo que nací seguro, es si ahorita mismo atrás de Google se puede acceder a una sola cuenta, o se puede acceder a varias cuentas. Eso es lo que no estoy seguro, pero estoy verificando ahorita mismo.
**Luis Torres**: Regardless, podrías entrar a través de caso of account.
**Cristian Berrío**: Si si tienes las si tienes las la las cuatro subcuentas, y de las cuatro subcuentas hiciste la misma integración, con los mismos scopes, pues tú solo indicas quiero entrar al lado Orlando y Benio, pues él utiliza la contraseña, Orlando y Benio. La de cheese to share, él utiliza la contraseña de cheese to share. Independientemente O sea,
**Luis Torres**: Para poder crear esos replays que tú hiciste, la automatización de replays y todo eso.
**Cristian Berrío**: independientemente si es a través de una o a través de todas, pues se puede acceder
**Luis Torres**: Y tú le puedes indicar a Claude qué tipo de skills usan para hacer esa respuesta, ¿cierto?
**Cristian Berrío**: Sí. O sea, le dices como que, mira, utiliza Google Heavy, accede a Goji Level, a este account, utiliza el nombre de las que que le quieras poner, para crear este correo. Ya.
**Luis Torres**: Y una vez establecido, se queda así.
**Cristian Berrío**: Exacto. Y, pues, cómo lo configuras, pues, te envía el correo o se genera como draft, así como los los SMS de Google, ahorita.
**Luis Torres**: Ok, fíjate, luego que investigues si puedes desde desde una sola cuenta, digamos, la cuenta de Trellis, acceder a todos estos sub accounts y crear skills para cada uno de esos sub accounts utilizando cloud. Si no es el caso, vamos a tener que hacerlo separado, Lo que sí tienes que tener es mucho cuidado, si es posible, tienes que asegurarte de que los replies, o sea, que los skills de cloud estén funcionando con el subaccount correcto. Es decir, no podemos utilizar MDs combinados de OEB, CTS y Doctor juntos, responder correos de Doctor, por ejemplo, porque va causar mucho ruido, no va a ser una buena respuesta.
**Cristian Berrío**: Claro. No, igual eso sí se puede apartar, eso es lo de menos. O sea, tú puedes segmentar las instrucciones que te quieres para uno o las instrucciones que quieres para otro. Como cuando
**Luis Torres**: Entendido.
**Cristian Berrío**: Sí, o sea, se puede segmentar eso, nada menos.
**Luis Torres**: El tema sí es posible.
**Cristian Berrío**: No, cien por ciento. O sea, superposible. O sea, por es que realmente los MD funcionan, Incluso, hay veces que no tienes que poner como que slash el nombre en las skills, sino que solo mencionas como quiero que utilices la skill de marketing, etcétera. No, le tienes que poner el el el slash. Y ya, a través de keyword, si sabe que la skill se llama marketing, emails. Pues, si tú le pones marketing emails o algo de marketing emails marketing, o sea, lo pones al revés, cualquier keyword él ya lo asocia. Con la skill que tiene que usar.
**Luis Torres**: Hermano, mira esa locura. Fonos con AI, Fonos etcétera.
**Cristian Berrío**: ¿Qué es eso?
**Luis Torres**: Activate AI early on air points. Free AI. Free between June first and August twentieth twenty
**Cristian Berrío**: O sea, eso es AI.
**Luis Torres**: Mira,
**Cristian Berrío**: Bueno, yo yo probé yo probé porque ellos tienen ellos tienen workflow, que hay automatizaciones. Por medio de un prompt. Pero no, no la da. Cuando yo lo probé, no la da. Cuando hice lo de dSpace, yo probé utilizando, tipo, creando el prompt no por no, sino ponerle un prompt así superdetallado. Pero no, o sea, me generaba unas locuras. No estaba tan desarrollada, estaba en beta. Bueno, es en beta aún, de workflow.
**Luis Torres**: El AI, este AI, este mismo.
**Cristian Berrío**: O sea, el AI de workflow específicamente, porque el AI o sea, que tienen metido ahí es para varias cosas, mira.
**Luis Torres**: Conversations.
**Cristian Berrío**: Para fondos, para workflows. Exacto. Tiene varias cosas, pero, por lo menos, de workflow, no no la dio. Aún está muy muy beta.
**Luis Torres**: Y workflows, ese mismo, ese que dice ahí, workflows AI, phonoc AI, ¿Tú lo probaste?
**Cristian Berrío**: Sí, exacto.
**Luis Torres**: ¿Cómo lo probaste si no tenemos ese ese a esa a esa función? No la hemos comprado.
**Cristian Berrío**: Está está está está inmerso, porque aún está en beta. O no sé si ya lo terminaron. Pero para cuando dice dispace, como estaba en beta, aún me dejaba usar lo de Workflow Gai. O sea, si tú ahorita te metes a cualquier cuenta, te pones en automations, te sale que lo puedes generar con ella ahí, el workflow. Pero no.
**Luis Torres**: Porque
**Cristian Berrío**: A mí personalmente no me
**Luis Torres**: porque, de verdad, no es no es el de Jugo. Qué locura esta gente.
**Cristian Berrío**: Buena pregunta. Review your subaccount under fee.
**Luis Torres**: Bueno, regardless, no necesitamos nada de esta basura porque va a tener más al club. Así que váyanse y métanse eso, ahí, perdón, no lo es quepa. Claude es mejor.
**Cristian Berrío**: Así es. Igual, meterle, pagar AI para cogerlo, no tiene sentido.
**Luis Torres**: No. No.
**Cristian Berrío**: Está
**Luis Torres**: Para eso tenemos claro.
**Cristian Berrío**: Exacto.
**Luis Torres**: Así es, hermano. Este, pero bueno, vamos a darle play. Avísame qué es, más o menos, qué vas cuadrando.
**Cristian Berrío**: Sí. Vamos a poner multitasking. Mientras hago playwright,
**Luis Torres**: Sí.
**Cristian Berrío**: mando el ticket
**Luis Torres**: Acuérdate, playback extracción, te expliqué cómo funciona la extracción. Luego, vamos a tener todo básicamente, vamos a convertir creo que el el la vuelta para todo el manejo de comunicaciones va a tener que ser a través de GoHealth Level. Esa va ser la mejor opción que vamos a tener, porque si no lo trabajamos dentro de go ahead, le vamos a tener una unos flows muy segmentados, muy En cambio, desde Google Health luego ya tenemos número de teléfono, tenemos correo, tenemos todo tipo de comunicaciones integradas, literalmente la metemos le metemos claro y estamos listo. El tema es que también necesito dentro de level necesito crear necesito saber cómo crear contacto de, bueno, tú creas un contacto y creas un y creo que ya eso es suficiente, ¿no? Por ejemplo, yo me meto aquí en la cuenta de Doctor, Discipline Rift, contactos, Yo aquí puedo Digamos, pregunta, podemos crear
**Cristian Berrío**: If I
**Luis Torres**: podemos crear un tablas de Excel que sean importadas con un botón hacia acá. Porque mira, fíjate que, por ejemplo, para los coaches, estoy compartiendo pantalla, ¿cierto? Para los coaches yo tengo esta función, que Bueno, ¿tú has visto esto? El roster de los coches.
**Cristian Berrío**: Correcto.
**Luis Torres**: Necesitamos, si vamos a comunicarnos por, Goja Level, necesito mandar comunicaciones por Goja Level. Entonces, necesito importar el roster de coaches a Goja Level. Y tener un level donde diga current coaches, otro que diga past coaches, Sí, digamos, algo así. Coaches, y meterá todos esos coches debajo de ese level. De la misma manera, también tengo otro tipo de sí, coaches y escuelas. También tenemos el school database. Que es este, donde tenemos la contacto de todas las escuelas. Si quiere mandar una comunicación a una escuela, lo haría desde aquí,
**Cristian Berrío**: Correcto.
**Luis Torres**: O sea, lo haría desde Google Cloud también. No importa, primero, nuestros contactos de las escuelas.
**Cristian Berrío**: O sea, sí se puede importar fácilmente. La cuestión es que no es importar la loca por importar. En Excel. O sea, habría que usar, por ejemplo, cuando yo importé los contactos, de de lo que teníamos en en nuestra base de datos, y nuestra base de datos y lo que teníamos regado, como lo que usábamos antes. Wix. Lo que tenemos en Wix, lo que tenemos es nuestra base de datos. Obviamente, pues, las columnas son totalmente distintas. El nombre de las columnas y toda la información como tal. O sea, antes de importar cualquier cualquier información, ya sea, pues, los school database o lo que sea, o el contacto de los coaches, primero hay que cuadrar cuáles son las columnas que se van a a migrar, o sea, qué información es importante, qué información es importante. Y ponerle un label,
**Luis Torres**: Yeah.
**Cristian Berrío**: crear una nueva columna que tenga un label que sea, no sé, coaches, lo que sea, etcétera.
**Luis Torres**: Ojalá o
**Cristian Berrío**: Exacto. O cojo ahí, le hago los... No, no, no, yo digo un un tag ese tipo coaches o
**Luis Torres**: Oh,
**Cristian Berrío**: o schools,
**Luis Torres**: por supuesto. Por supuesto, por supuesto, por supuesto.
**Cristian Berrío**: o schools Orlando School, exacto. Entonces, como que ya con eso, ya sí se puede importar fácilmente. Pero si tú descargas eso y lo importas, pues probablemente salga malo, y, si no salga malo, pues el va a ser confuso,
**Luis Torres**: No, no, no, no, la idea de esto aquí para que, este, todo esto esté todo esto esté organizado, todo esto esté bonito. Porque
**Cristian Berrío**: No, sí, pero importar esa información o sea, es bastante fácil, no no tiene esencia.
**Luis Torres**: Excelente.
**Cristian Berrío**: Se puede se puede importar el Excel.
**Luis Torres**: Excelente. Entonces, me queda pendiente arreglar toda esta data para dejártela bonita y te indicándote qué es lo que necesitamos extraer.
**Cristian Berrío**: Exacto.
**Luis Torres**: Para tanto para los coches y tanto para las escuelas claramente los papás ya tenemos nuestro flujo con nuestros tags de temporada. Pregunta, ¿esos tags están funcionando dentro de Google Health ahorita, ya que los tenemos desde Lowable?
**Cristian Berrío**: Sí.
**Luis Torres**: En una base de datos nueva.
**Cristian Berrío**: Sí, no, hace, o sea, sí, que todo, sí. Funcionando. Ahorita mismo, como te dije, que no hemos apagado, la cuenta Discipline Brief, ahorita mismo todas las registraciones que están llegando todo eso, independientemente, está yendo bajo y luego. Porque aún aún no está pagada la las funciones y la base de datos. Toda esa información nueva está llegando. De todas maneras, por curarnos en salud cuando ya nos migremos, voy a a importar los contactos. O sea, importar los contactos nuevos la información nueva que vos es nuevo. O sea, con los tax nuevos de de esta temporada, con los padres que ya se están teniendo y escribiendo esta semana. Pero, Lucy, aún está donde, aún está llegando. Aún está llegando toda toda esa
**Luis Torres**: O sea, lo importante es que los tags de los papás funcionen con nueva website, también con el web, también con los que estamos trabajando ahorita.
**Cristian Berrío**: No, con el nuevo web sí sí sirve. Todo eso, o sea,
**Luis Torres**: Excelente.
**Cristian Berrío**: todo eso ya se está mandando.
**Luis Torres**: Excelente. Entonces vamos a mover todas nuestras comunicaciones hacia hacia level. Esto que también cambien las formas, las formas que los papás llenen. Que se llenen de hacia abajo al level. Que no nos lleguen a traer Gmail, Creo que nos pasa eso con con OEV, si no me equivoco.
**Cristian Berrío**: Okay. Ok, para reflexionar. Pero ahí ya la forma estaría maluquita. O sea, si va a estar embedded, así, tipo, de go ahead level, ya estaría maluquita. Que sepas. Ya no sería tan
**Luis Torres**: Sigue sigue sigue sigue estando así, sigue estando Maluca, no no la he mejorado.
**Cristian Berrío**: O sea, es que no es personalizable, ya es como un form de Google. No puedes cambiar lo visual, solo los campos. Y el texto.
**Luis Torres**: Sí, bueno, adelante. Lo que sea, o sea, lo que sea, con tal de que o sea, un ejemplo de una forma que, en qué website tenemos estas formas de cogerle
**Cristian Berrío**: En calendario de hoy, vi. Es la única. Se verían así.
**Luis Torres**: Dale.
**Cristian Berrío**: So, entonces. Es soba, me parece.
**Luis Torres**: O sea, lo que vamos a tener que hacer es que se vea más digamos que, ajá, que lo tengamos que sí aquí. Que se vea un poquito más pequeño, que que esto, que que el form se vea menos, que tenga menos protagonismo en el de website. Y ya.
**Cristian Berrío**: Mhmm. Sí. O sea, ajustar el tamaño, sí, sí podría.
**Luis Torres**: Y aquí, por ejemplo, ajá, que sea como que ah, ok, que que no es tan no es tanta diferencia.
**Cristian Berrío**: No, ese es nuestro.
**Luis Torres**: Fíjate que a nivel de términos visuales,
**Cristian Berrío**: Ese ese ese es el nuestro.
**Luis Torres**: OIB.
**Cristian Berrío**: Correcto, ajá.
**Luis Torres**: OIB contact. Y esto lo hicimos nosotros.
**Cristian Berrío**: Ajá, correcto.
**Luis Torres**: Nuevo ad level, entonces, como que no se ve tan diferente, simplemente que es al esquinas no son redondas, etcétera, pero no están no es tan drástico. Con tal, eso podemos colocar el form en el website, no tenemos problema.
**Cristian Berrío**: Okay. Me parece, entonces.
**Luis Torres**: Así que nada, conectamos esos MCPs, saquen más información con Playwright, vamos a darle play.
**Cristian Berrío**: Sí. Me parece, me parece.
**Luis Torres**: Y bueno, no está de más mandar el ticket hacia hacia Antropic para verificar que nuestra teoría. Sería bueno. Así sabemos cuáles son sus extensiones.
**Cristian Berrío**: No volver a perder el tiempo con con Google. Y Claude.
**Luis Torres**: Sí, exacto, para saber qué, cómo ellos se sienten al respecto. Si de verdad son uno, egoístas, locos, competidores, maniáticos, ajá.
**Cristian Berrío**: Dale, pues. Voy a mandar ticket, entonces.
**Luis Torres**: Dale, está bien, tío, Juan Manuel, Blé.
**Cristian Berrío**: Hermano. Comentando, entonces.
**Luis Torres**: Dale, pues.
**Cristian Berrío**: Dale. Bye.

_Sincronizado por Brain: 2026-10-17T22:33:47.113Z_
