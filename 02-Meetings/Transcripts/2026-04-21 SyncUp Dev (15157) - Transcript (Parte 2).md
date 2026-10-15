---
brain_note_id: "dest:meetings:955e7a330b43a282c79d3f6bd247f4e0"
canonical_key: "meetings/955e7a330b43a282c79d3f6bd247f4e0"
brand_id: "meetings"
---
# Transcript — 2026-04-21 SyncUp Dev (15157)

## Transcript

- Reunión: [[02-Meetings/2026-04-21 SyncUp Dev (15157)]]
- Parte 2 de 2
- Anterior: [[02-Meetings/Transcripts/2026-04-21 SyncUp Dev (15157) - Transcript]]

**Cristian Berrío**: O sea, que va a implementar como tal las soluciones Cloud Code. Que Obsidian haga algo. Obsidian eso es una biblioteca. Pero como va a estar conectado a Cloud Code, Cloud Code tiene todo el contexto, la balance es cómo es cómo se van a comunicar entre ellos ya. Dame el contexto, CloudCore recibe el contexto, hey, esto no me sirve o hey, necesito que hagamos una modificación a reglas de del call, cambia esto y le manda tipo, el outflow para que lo cambie. O sea, Cloud Code, ¿cómo es eso? O sea, le manda Obsidian a cambiar la política del por qué ya tenemos. ¿O sí puede cambiar?
**Luis Torres**: Clauco, ¿puede qué? ¿Cambiar qué? Está leyendo esto, disculpa.
**Cristian Berrío**: Sí, o sea, estoy viendo, Obsidian no es una biblioteca estática. O sea, sí puede cambiar. Pero no sé si lo cambia el mismo o lo cambia a Cloud Code. Yo creo que lo cambié a Cloud Code.
**Luis Torres**: Exacto. Entonces necesitamos skills de cloud con nos donde podamos editar Obsidian. No sé si es un skill que tú construyes o un skill que ya tienes.
**Cristian Berrío**: Sí, o sea, el mismo el mismo tutorial me estaba indicando. El mismo TikTok me estaba indicando que la idea la lo jugoso de de usar Obsidian con Cloud Code es conectarlos entre sí para que no solo lea, sino que también edite las cosas.
**Luis Torres**: Eso,
**Cristian Berrío**: Eso es lo eso es lo lo el el valor que tiene Cloud con con Obsidian. Que puede ver y editar. El mismo Obsidian.
**Luis Torres**: la verificación completa A ver. Crear la planificación. Crear la planificación completa por marca, el objetivo que queremos conseguir con la información que vamos a tener dentro de Obsidian marca. Bueno, bro, listo. Entonces te dejo esto esto está en tu, esto está en chat, Igual te lo dejaré en clic, Seguiré trabajando en
**Cristian Berrío**: Okay.
**Luis Torres**: Ahora sí, uno dos uno dos. Dale, vamos a darle. Aquí ya, más o menos, planificación general, todas las marcas. Obsidian no va a ser una biblioteca estática donde agarramos finales, la fuente de información, una base de conocimiento tuya, una herramienta para estándar, mejorar y actualizar. Ok. Entonces, este, aquí está. Marco, quedemos entre... Qué debe entender? Estamos ayudando solamente, hay que, ok, arquitectura mínima dentro de Obsidian, Esto no le presta atención, La arquitectura mínima te lo voy a pasar por otra parte. La la arquitectura en Obsidian las montando con el chat de Obsidian como tal. Aquí está el contexto general para qué vamos a utilizar Obsidian, qué tenemos que implementar de Obsidian por marca. Aquí está.
**Cristian Berrío**: Ok. Vamos a Pero organízalos o sea, cambia el nombre, cambia el título a los a los chats.
**Luis Torres**: Esto es plan obsidian. Esto es
**Cristian Berrío**: Instructure.
**Luis Torres**: structure Sí. Y puedes llevarte los dos chats a tu a tu foda de dev, si quieres, anteriormente.
**Cristian Berrío**: Ahí sigue escribiendo.
**Luis Torres**: Si Obsidian, o sea, aquí la parte más fastidiosa, va a ser colocarlos, extraer la data, y colocarlo y y dejar que, porque a me lo organiza, pero la parte facciosa para ti va ser como que agarres la data como tal.
**Cristian Berrío**: Correcto.
**Luis Torres**: Toma toda esta información como contexto actualiza la estructura por marca. También quiero que actualices la estructura de Alex Formosi con esta información. Dame toda la información de y los libros que tenemos en knowledge, para darle instrucciones a un a una herramienta que va a funcionar como un notebook con toda esta información que tenemos en el knowledge, de Alex Formosi, para hacer business development.
**Cristian Berrío**: Le iba decir, pero, por ejemplo, o sea, la comunicación de los correos, los mensajes de PeerSpace, toda esa cosa, como tal, yo voy a extraer, digamos, O sea, voy a quedar en un manual y en ese manual van a voy a poner tres, cuatro ejemplos de mensajes de texto y de correo. Solo el tema de comunicación. ¿Verdad? O sea, el resto sí es poner como que toda la info de de lo de Doctor, lo de los currículums y todo eso.
**Luis Torres**: Yo utilizaré más de tres, cuatro correos para los mensajes de texto. Yo pienso que un buen exit ticket sería unos buenos entre diez y quince correos por marca. De diferentes tipos. Y luego los metes en el
**Cristian Berrío**: Por eso, pero
**Luis Torres**: luego
**Cristian Berrío**: pero eso es para crear solo el manual o solo para para poner los ejemplos?
**Luis Torres**: Ambos.
**Cristian Berrío**: ¿Eso en qué me refiero?
**Luis Torres**: Ambos. Porque manual debe tener ejemplos. ¿Me entiendes?
**Cristian Berrío**: Sí. O sea, lo que yo tenía pensado era coger diez correos ChatGPT, ey, miro la estructura de esto, crea un manual, así como que a palabras muy muy gruesas. Después de que me da el manual,
**Luis Torres**: Utiliza la skill, pero no porque no utiliza el skill que tienes de comunicación.
**Cristian Berrío**: Ajá, por eso, ¿sabes?, es es darte un ejemplo. O sea, lo pongas al skill que que habíamos hablado, me da el manual, y en ese manual, digamos, abajo del todo, le pego cuatro ejemplos de correo. Eso es lo que yo me estoy eso es que estoy yo. Preguntando.
**Luis Torres**: No, porque está equivocado. Yo agarraría quince correos de de de de de la marca. Acuérdate que esos correos no todos son de lo mismo, La idea es que la
**Cristian Berrío**: Mhmm.
**Luis Torres**: la idea, la razón por la cual tú escoges un una cantidad de correos grande, no unos no dos, sino quince, veinte correos, es porque hay diferentes tipos de correos. Por ejemplo, nosotros en en Doctor nosotros definimos que hay correos de staff y correos de para los papás. Y decimos automatizar ambos. Ambos tienen chats, bots, que funcionan de manera diferente. Entonces, yo agarraría quince a veinte correos no le des una estructura, ¿verdad?, no no le digas, mira, esta es la estructura, dile más bien al bot, lee estos correos, compartmentaliza esto. Lee estos correos, compartmentaliza los correos entre los diferentes tipos de correos que existen, ¿verdad? Una vez que entiendas los diferentes tipos de correos que existen, crea ejemplos, utiliza el, utiliza los correos que te di, para utilizarlos como ejemplos reales Eso es una estructura que me dio aquí, uno de estos chats me había dado esa estructura, ejemplos reales, ¿verdad? Ahí pones, y los pones los ejemplos, primero, pones los correos reales, Luego mandas, escribes una información o contexto de cómo escribimos los correos, para ese segmento. Digamos que la, que en ese compartimiento, digamos que compartimiento es entrenadores. Le das los quince correos, compartimientos, hay gavetas, ¿verdad?, diferentes gavetas. Una gaveta es papás. Entonces, dentro de la gaveta, los papás están los correos como ejemplo. Luego está, luego el el agente le pides que te dé comunicación, approach de comunicación. Nos comunicamos a los papás de la siguiente manera, nos comunicamos a una papá de una manera auténtica, donde hablamos, donde nos importa que el estudiante sea prioridad, etcétera, etcétera, etcétera, el agente debería darte esa estructura. Como que el contexto de esa forma de comunicación, dentro de esa gaveta. ¿Cuál es el contexto? Cuáles son los ejemplos buenos y utiliza esa gente de una vez para crear ejemplos mejorados. ¿Me entiendes?
**Cristian Berrío**: Sí.
**Luis Torres**: Ejemplos optimizados. Y eso lo vas a hacer por gaveta, Entonces, si en la si en Doctor está la gaveta de los papás, la gaveta de faculty, está la gaveta de los coaches, necesitas que ese agente te comparte, te te haga un, te haga un, te los divida por categoría, te cree esa estructura. Lo que tienes que darle a la gente, como prompt, es identificar la los diferentes tipos de correos que hay, Una vez que los identifique, categorízalos, categorízalos en diferentes segmentos, una de los tenga fermentizados, quiero que me des el correo original en de esa en esa aplicado original aplicado en esa categoría, ¿verdad?, y que te dé los correos originales. Luego, que te dé el contexto de cómo, cuál es nuestro método de comunicación, y luego que te dé una mejora de cómo podemos optimizar Y luego agarrás todo eso, se lo mandas a a cloud, a a Obsidian. O simplemente le das los correos Sí, sí, le le das esa estructura. Correos actuales y correos optimizados. O simplemente le das los correos optimizados. También. Le puedes decir a le puedes decir a la gente. Optimiza estos correos, crea un contexto, crea un, categorízalos, una vez que los categorice, optimízalos y crea un contexto de cómo nosotros nos comunicamos por correo. Y ya. Una vez que tengas ese archivo, ponlo en Obsidian. En Obsidian yo puedo abrir files, ¿verdad? Yo puedo abrir, yo puedo dar esa información visualmente.
**Cristian Berrío**: Sí.
**Luis Torres**: No es que Ok. Entonces, una vez que eso esté ahí, yo me puedo meter eventualmente a revisar qué es lo que lo que tú pusiste y y me aseguro de que esté correcto. Si el agente, si es un buen agente con buenos skills, no debería haber un problema, porque ya lo que se ha hecho está escrito, lo que hay es que optimizarlo y guardar los récords de eso. Aquí estoy creando tu chat. Está viendo lo que está haciendo, ¿no? Lo de qué es extracción.
**Cristian Berrío**: Aquí quedó.
**Luis Torres**: ¿Dónde está el chat de...? Es Hermoso.
**Cristian Berrío**: Creo que es ese, sí.
**Luis Torres**: ¿Tienes mucho más libros en knowledge que no estoy viendo reflejado en tu output. Necesito que los libros, necesito la información, libro y la información que se puede extraer por por libro. No me importa la información que tú quieras describir o poner sobre el libro, lo que necesita una estructura, de los libros que tenemos en tu knowledge. Ok. Estructura global simplificada. Mira, aquí está. Mira, ¿ves? Aquí está. Esta es la estructura por marca. Ah, sí, sí. Mira, Joaquín, estructura por marca. Brand name, y toda esta locurita. Por marca. Una vez que tú lees esta estructura, este esto sí está bien, ¿Te acuerdas que lo primero que habíamos visto tenía un arroz con mango, mezclando como que tenía como que esto generalizado para todas las marcas? Ahorita ya está aterrizado para para todo. Y la lógica. Bueno, pienso que estamos listos. ¿Qué opinas tú?
**Cristian Berrío**: Yes. Oh, ya, con eso ya
**Luis Torres**: Tenemos todo atrasado.
**Cristian Berrío**: con eso ya Sí, ya con eso hay suficiente contexto. Ya con eso ya me sirve.
**Luis Torres**: Mhmm. Aquí hay un error. Ah, no, mira, Juan, Juan el mío no playbooks. Sí, aquí está, aquí está perfecto. Aquí esta es Ormosi, este libro es Ormosi, Fíjate que lo que está aquí, Cris, todo esto lo es Formosi. Todos estos libros están metidos, en este bot. Entonces, lo que estoy pidiendo aquí, que extraiga la estructura de todos los libros que tiene, para que tú agarres esa estructura, y la metas dentro de Don Juan Mosey. Para que cuando tú, para cuando el bot recibe esos archivos, ya sepa cómo ordenarlo. Aunque yo pienso, que, una vez que con esta información de Formosi, se supone que Obsidian es inteligente, ¿no?
**Cristian Berrío**: Sí.
**Luis Torres**: Con esta información de Formosi, él ya podría categorizar los libros, pero no, yo pienso que esta estructura cambia esta estructura a abajo. Con esta información real que viene de los libros de Ormosa. Ya esto está a mi nombre. Ahora sí. Ahora tenemos estructura por marca, Entonces, conclusión, este es el plan de Obsidian, o sea, que está todo especificado por marca. Este plan me lo llevé para la estructura de Obsidian, Dentro de la estructura de Obsidian, utilizamos el plan para levantar esta estructura por marca, que va ser parte de de nuestro cerebro.
**Cristian Berrío**: Okay.
**Luis Torres**: Y también, y vamos a tener estructura por marca y vamos a tener una estructura generalizada que es con la información de aquí están todos los MDs. Aquí sí estamos sacándole jugo a estos libros. ¿Qué pasa con ChatGPT? Como ChatGPT no tiene end this, no tiene esta información bien segmentada, el output que te da está bueno lo que puede extraer del documento en ese momento. Cinco. ¿Me entendiste esa parte? Bueno, te pregunto, ¿cuál es la ventaja de darle esta estructura algo como Obsidian donde lea todos estos MDs y los pueda hacer mientras los entienda bien, en vez de utilizar un chat, como yo creo, el de Hormosi, donde tengan los mismos libros.
**Cristian Berrío**: Porque si ahí, como está en el mismo ambiente de Obsidia, pues tienes toda la información de Hermosi, y tienes toda la información de las tres marcas. Entonces, por ejemplo, si tú te das al GPT de Ormosi, lo que toca hacer a ti cada vez que vayas a crear algo, es darle todo un contexto de una marca, y hacerlo todo de cero, te va a dar output así como como el que has hecho ahora, O sea, has hablado con con Obsidian, has hablado con con exacto, con el GPT de Obsidian, y la has tenido que hacer uno y otra vez prompt, o has tenido que mandar como cinco prompts. Porque obviamente, tú le das el contexto pero le falta como más detalle o le falta que sea más estructurado a lo que tú quieres como tal.
**Luis Torres**: Mhmm.
**Cristian Berrío**: La ventaja de tener Obsidian, Ormosi, tener las tres marcas, es que no tienes que escribir cuatro párrafos, tienes que escribir cinco prompts para cambiar cosas. Porque ya lo tienes todo en un solo lugar. Entonces, pues, obviamente, el output que te va a dar es muchísimo mejor y es muchísimo más estructurado a lo que tú quieres y a lo que realmente hacemos, no es ChatGPT inventando o adivinando qué es lo que tiene que hacer o qué o cuál es la que quieres tú.
**Luis Torres**: Correcto.
**Cristian Berrío**: Entonces, lógicamente, pues ya teniendo una estructura y unos libros, de Hermosi, el nuestro Obsidia, los cambios que se vayan a realizar o las implementaciones que se vayan a hacer ya van a ser aterrizados a lo que nosotros hacemos.
**Luis Torres**: Correcto. Bueno, entonces, nada, te queda esto es la información de la lógica, implementación de correo, grabé todo lo que te dije, está ahí. No sé cómo está el output, pero lo puedes revisar. Igual, debería ser algo parecido a lo que hablamos. Estructurado Obsidian, Hormosi, y por marca. Y plan, el plan como tal. De cómo vamos, de qué es que vamos a hacer en
**Cristian Berrío**: K.
**Luis Torres**: ¿De qué se supone y cuál es el objetivo de esto que estamos haciendo con Oxygen? listos?
**Cristian Berrío**: Listo, ahora sí. Leito, leito.
**Luis Torres**: Vamos a darle play, vamos a darle play. Fíjate que cuando montemos esto, podemos empezar a hacer contenido para trailers cuando nuestra mente bien, bien bacana, bien bien bonita. Ese va a ser el donde vamos a poder hacer el flex el el mega flex, hablando de lo que hicimos. Y le podemos decir, mira, únete a nuestra broma, y le damos un sync y te podemos dar acceso a un sync a lo que tenemos de Formosi. Para que no tengan que ellos hacer todo. Porque lo lo que me molesta de estas cosas es que sí son chévere, fíjate, llevamos tú y yo una hora cuarenta minutos hablando sobre el plan de trabajo, porque esto que estamos hablando ahorita es nuestro plan de trabajo,
**Cristian Berrío**: What's
**Luis Torres**: ahora tú vas a ir a implementar, te vas a tardar un par de horas implementando, y luego lo vamos a poder utilizar. Nos tomó dos personas y más de cinco horas un día. Una persona normal, cuál es el cuál es cuál es la En realidad, es muy cool, pero cuál es la... Tiene que dedicarlo un tiempaso para poder utilizar este tipo de cosas, entiendes? Entonces, la idea sería yo pienso hacerlo un poquito más fácil para ello, donde no tengan que hacerlo literalmente todos ellos mismos de cero.
**Cristian Berrío**: Literal, que solo sea prácticamente.
**Luis Torres**: Correcto, correcto, correcto. Lo voy hacer a Monche que revise esta conversación que que tuvimos ahorita. Le voy mandar este transcript para para que esté al tanto de lo que estamos haciendo, porque esto debería pasar a contenido de Pero bueno, ya viste que tenemos redes sociales, ya tenemos página de LinkedIn, ya puedes poner tu LinkedIn bonito,
**Cristian Berrío**: Yeah.
**Luis Torres**: vamos a hacer una sesión de fotos allá en Colombia, para que tengas sus fotos profesionales, etcétera. Vamos a darle con todo.
**Cristian Berrío**: Man or man? Bueno,
**Luis Torres**: Ándale, hermano. Me dices cómo te ¿Serías algo?
**Cristian Berrío**: Dale, dale. ¿Qué más? Dale, pues.
**Luis Torres**: Dale,
**Cristian Berrío**: Ahí comentando, entonces. Bye.
**Luis Torres**: Bye.

_Sincronizado por Brain: 2026-10-15T17:21:03.526Z_
