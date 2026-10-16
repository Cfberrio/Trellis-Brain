---
brain_note_id: "dest:meetings:22f996fc03946ba820d29b85e61decfe"
canonical_key: "meetings/22f996fc03946ba820d29b85e61decfe"
brand_id: "meetings"
---
# Transcript — 2026-05-11 SyncUp Dev (17277)

## Transcript

- Reunión: [[02-Meetings/2026-05-11 SyncUp Dev (17277)]]

**Luis Torres**: Estoy claro, por eso te llamé. Básicamente, vamos a crear un nuevo stage, pero te escribí implementa esta automatización en un nuevo stage que se llame send call call email, bueno, que es cold preferido. La idea es que a través de, cuando cuando hagas ese nuevo stage, lo aplicas aplicas esa toma sesión, nada más para ese stage, y cuando esté listo, voy a hacer la prueba con ese stage. Entiendes?
**Cristian Berrío**: Para venir a escuela.
**Luis Torres**: Voy a hacer, no, nada más voy hacer la prueba en una sola escuela. Pero pero la idea estaría crear un nuevo stage para no no para no implementar esto en algo que Jacinthe está usando. ¿Entiendes?
**Cristian Berrío**: ¿Y dónde quiere que ponga el nuevo stage?
**Luis Torres**: Puedes ponerlo en pipeline dos, a ver qué tal, creo que ahí podemos jugar con eso.
**Cristian Berrío**: Pero ¿en qué parte exactamente? Tipo,
**Luis Torres**: Oh, puede ser primero, o sea, un contacto con Ok. Vamos a hacer esto. En pipeline dos, vas a crear un stage en la segunda fase, o sea, eso no importa, eso esto nada más este stage nada más va ser para propósitos de prueba. Por eso vamos usar el plan dos. Puedes ponerlo en el plan dos, después de high priority, puedes ponerlo ahí después de esa columna high priority, y vamos a utilizar el contacto y la información de esta de esta persona, de este staff. Necesito que que crees un contacto con esta persona, porque en el correo que yo tengo creado, tengo un correo para el primer nombre y para nombre de la compañía. El nombre de la compañía sería la escuela, o, por ejemplo, business name. Y first name, sería Donna. Okay. Mira eso que te mandé ahí. La documentación tiene tiene custom fields para nombres y eso. Entonces la idea es que ese, la información de este contacto se cree en ese orden, o algo parecido. Te pregunto, los fields que tú creaste para estos son los mismos fields que yo te había mandado, ¿correcto?
**Cristian Berrío**: So, por ejemplo, el full name sería el POC,
**Luis Torres**: Uh-huh. No tenemos field para first name.
**Cristian Berrío**: Sí tenemos, porque eso ya va ¿Cómo se dice eso? O sea, eso ya es nativo de de todos los contactos. Siempre va a tener un nombre, un Gmail y un número de teléfono, o sea, eso no se crea de cero. Siempre está por default.
**Luis Torres**: Okay.
**Cristian Berrío**: La cuestión es que para nombre, y segundo nombre, la idea era poner
**Luis Torres**: Estamos en dos primary contact name. ¿No?
**Cristian Berrío**: No, o sea, la idea era para first name y last name, poner el nombre de la escuela. Porque, lógicamente, a Yassy no le sirve ver a Donald Lyle
**Luis Torres**: Claro.
**Cristian Berrío**: como first name, last name, porque no va saber qué carajo
**Luis Torres**: No le va salir.
**Cristian Berrío**: qué escuela. O sea, yo lo yo lo había puesto o lo había pensado para poner el el the first name at Water Bay, es el first. Que lo tenga claro.
**Luis Torres**: Ejemplo, aquí estoy sacando un ejemplo. Bueno, mentira, vamos a buscar un ejemplo que ya esté en uno. Whisper, no, que ya nosotros tenemos aquí un nombre. Aquí está. Primary contact name es el nombre de la escuela.
**Cristian Berrío**: No sé.
**Luis Torres**: Primary email
**Cristian Berrío**: O sea, que estás compartiendo, pero no. Creo que no.
**Luis Torres**: Aquí en aquí en aquí en clic up. ¿No puedes ver?
**Cristian Berrío**: No, pero no sale. O sea, no sabes lo que estás compartido, estás compartido otra cosa.
**Luis Torres**: Sorry. Estaba compartiendo mi otro monitor. Ok. Aquí, Whisperer and Oak. Nombre de la escuela es primary contact name. Primary email es este. Phone no hay room para el nombre de la persona, ¿cierto? O cuando se mete el nombre de la persona, ¿dónde se mete? Por ejemplo, esta, Dan
**Cristian Berrío**: O sea, en medio del A ver. Mira mejor mi pantalla, ya te comparto. Me dice directamente del pipeline, ¿verdad?
**Luis Torres**: Uh-huh. Habla Nuno, está, ajá.
**Cristian Berrío**: Voy a cerrar todo esto, por esto no importa.
**Luis Torres**: Cosa?
**Cristian Berrío**: Mira, cuando te metes desde el pipeline, ¿verdad?
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Si tú le das a aquí no. Si tú le das al pipeline, te va a salir información supergeneral. Una importante, Pero si tú le das, aquí, te redirige al contacto como tal. Y
**Luis Torres**: Ya.
**Cristian Berrío**: del contacto, toda la información nueva, lo importante, digamos, el el del POC, lo que sea hasta aquí.
**Luis Torres**: Additional info,
**Cristian Berrío**: Exacto. O si quieres ver Bueno, esto no ha puesto nada aún, porque no no no estaba esa información. Por eso tampoco.
**Luis Torres**: para utilizar ese custom field, ahora vete a la automatización, Haz una haz una ventana nueva, no no te vayas a ir, vete a una ventana nueva. Ok, métete en en lo de los automations,
**Cristian Berrío**: Este, ah, ok.
**Luis Torres**: Me deteniendo el lead email,
**Cristian Berrío**: Está bien.
**Luis Torres**: Ahí. Ajá. Ok, dale ahí email, abandono en aseguranza. Ahora, yo tengo ahí custom, no lo guardé. What? Porque no sale el dime guardado. Bro, qué fastidio. Pero bueno, digamos que quiero añadir ahí el el nombre del de la persona, el nombre del del del POC name, Dale ahí los tags, dale al tag, arriba o la izquierda. No, no, no. Ahí mismo a la izquierda. Eso. Ahí sale,
**Cristian Berrío**: Sí. Te vas aquí, Custom Valley. Entonces, vas a custom values, Ah, no, espérate. ¿Cómo que era esto? A contact, perdón. Ya primero a contact. Después te vas a custom fields,
**Luis Torres**: Yeah.
**Cristian Berrío**: y ahí te sale lo que yo creo.
**Luis Torres**: Listo, buenísimo. Ya eso es suficiente.
**Cristian Berrío**: Ok.
**Luis Torres**: El nombre de la escuela, Ah, bueno, ya, yo puedo ver todo eso. Ok, excelente, bro. Crack.
**Cristian Berrío**: El nombre el nombre de la escuela como tal es el
**Luis Torres**: Sí, Whisperer, no creo que sale ahí.
**Cristian Berrío**: realmente tú también puedes poner eso o sea, lo tienes que poner como custom field, obviamente, porque como vas a enviar esto ahora escuela, no puedes poner uno por uno el nombre en la escuela. Igual, o sea, relájate que yo igual de todo eso yo me encargo, o sea, tú solo dime los emails y yo me encargo de poner los custom values y todo eso.
**Luis Torres**: Okay.
**Cristian Berrío**: Eso no te preocupes. Te iba a decir, o sea, básicamente, lo que tiene que hacer Jazyn para todas estas que no tienen POC, es que él sea, si quiere, graba esto para mandárselo, y lo digo en inglés.
**Luis Torres**: Ok. Creo que, clic o puede agarrar tu audio, ¿sí? Cuando esté hablando de ClickUp.
**Cristian Berrío**: Working now.
**Luis Torres**: No sé. K. Just making sure.
**Cristian Berrío**: Creo que no. Creo que lo probé una vez y no me, y no te ha roto audio.
**Luis Torres**: El mío, ¿cierto? Nada más a la de tú y yo cuando estás hablando.
**Cristian Berrío**: Exacto. So, creo que agarra el que... Igual lo puede ver. Se lo puede
**Luis Torres**: Ok. So, when you're trying to create when you're trying to create a, when you're trying to add the point of contact for a specific school, you go to the actual school name, you click on the name of the school. Don't click on the box. So go back. If you click on the box, it take you to the contact. Right? So that that that's the box. We don't wanna do that. We wanna go back and go on the actual school name. Once you do that, you will go down to MenPOC. That's where you're gonna add the name. The email, and their position. Let's say they're front office. Then you add their phone number as well and extension. You click save, and that's it. Cool. Sencillo.
**Cristian Berrío**: Ya que le quede ahí, porque yo sé que eventualmente, cuando iba a empezar esto, me va a preguntar cómo poner las cosas ahí que las ponga bien, porque después cuando vaya a hacer el envío del Igual, lo que yo hice, para que lo tengas claro, es que lo que, el email que se va enviar Espérate, es una bulla. Están haciendo reparaciones aquí.
**Luis Torres**: No, yo no escuché nada, William.
**Cristian Berrío**: Reparaciones. Como un taladro ahí. Este,
**Luis Torres**: Clicó, clicó cancelar absolutamente todos los nueces. Te escucho como que estuviese en un estudio sin ruido.
**Cristian Berrío**: Sí, porque ni ni tenía los audífonos, pues estoy con el con el computador. Pero bueno, Básicamente, para que lo tengas en cuenta, tú aquí, en la automatización... En la automatización, tú, realmente, tú no pones el contacto al que tú quieres enviar información. ¿Sí me entiendes? O sea, aquí no hay un for, email, solo de dónde lo vas a enviar, no hacia dónde lo vas a enviar.
**Luis Torres**: Uh-huh.
**Cristian Berrío**: Yo he leído que GoHyLevel automáticamente toma el email principal. Es decir, tú sabes que estos campos estos campos son los los o sea, estos son los que vienen por defecto, para acá, con
**Luis Torres**: Claro, claro, claro, claro, claro, claro. Sí.
**Cristian Berrío**: Entonces, realmente, ya, sin lo que
**Luis Torres**: Cogedor le manda un correo a ese.
**Cristian Berrío**: Exacto. Yacin no va, o sea, porque es que Bueno, me imagino.
**Luis Torres**: Tenés que editar eso también, tenés que ponerlo ahí también.
**Cristian Berrío**: Exacto. El el POC email, lo tiene que poner es aquí, y aquí. Porque, si deja este
**Luis Torres**: Ok, esa parte no la dejé, pero
**Cristian Berrío**: deja este por defecto, se la enviares a la escuela, no al POC.
**Luis Torres**: Ok, quiere ahora eso no
**Cristian Berrío**: Perfecto. Se me olvida de decirte eso.
**Luis Torres**: Treinta uno. Okay. Perfect. So when we're trying to email when we're trying to use this automation, right, Actually, I just thought about something we're gonna have an automation for. Flag. Okay. That's fine. I'll do it later. But when you're trying to create an automation, when you're trying to send an email, on the automation, you're gonna put their email there. You're gonna put it there, and you're also gonna add it below. So so let's say p o c at Gmail dot com. You're also gonna add it there. So p o c at Gmail dot com. And then you're gonna add their position phone and extension. I think that's the only that's the only new air like, the new field that we have. And that should be it. So remember, you have to put email the email on both. The main contact info and when you scroll all the way down, when it says main POC. Area.
**Cristian Berrío**: Ya, eso es todo.
**Luis Torres**: Amazing.
**Cristian Berrío**: Ya con eso, ya no debería fallar. O sea,
**Luis Torres**: Men.
**Cristian Berrío**: en las manos de Yesin está que el correo se envía al POC. Y que la información se
**Luis Torres**: Listo, buenísimo.
**Cristian Berrío**: Porque si el día de mañana se le olvida cambiar, el POC, de esta la pone acá, se envía la automatización a esta escuela. O sea, al al contacto este de la escuela. ¿No?
**Luis Torres**: Correcto, correcto. Correcto. Bueno, hagamos un test Ábrame ábreme ahí la la broma de mandar aquí un correo de texto. ¿Ok? Te voy a mandar el correo de test, que lo montes. Listo.
**Cristian Berrío**: Hello?
**Luis Torres**: ¿Has podido adelantar algo de hoy,
**Cristian Berrío**: Sí, ya lo estaba cambiando. Falta se le push. Una flecha
**Luis Torres**: Ok. Listo. Cuando termines ahí, montas a, hacemos el test. Parece?
**Cristian Berrío**: Dale, Pero es un contacto nuevo que hay que que hay que crear, ¿o
**Luis Torres**: No, es un contacto, bueno, es nuevo porque sí, porque ya lo tenemos. Estamos usando un test con con un faculty de verdad.
**Cristian Berrío**: Ok.
**Luis Torres**: ¿Me entiendes?
**Cristian Berrío**: Sí, pero el contacto no está creado, o sea, no estaba de la migración que
**Luis Torres**: Se ha creado, antes no, no. Tenés que poner la información de contacto, de este contacto. Lo que quiero lo que quiero asegurarme es que los fields todos funcionen bien, y que el reciba el correo. Esos son los, esos son, esto es lo que yo quiero hacer.
**Cristian Berrío**: nada, nada. Bueno, o sea, móntame solo el nombre de la escuela, el correo y, pues, el número. O sea, el resto da igual. El resto lo puedes dejar en blanco.
**Luis Torres**: Correcto.
**Cristian Berrío**: Móntame eso y yo mando el tres. Ahorita tengo la reunión con Mocha y la
**Luis Torres**: Dale, miro.
**Cristian Berrío**: ¿Me comentas, entonces?
**Luis Torres**: Activo.

_Sincronizado por Brain: 2026-10-16T07:33:44.497Z_
