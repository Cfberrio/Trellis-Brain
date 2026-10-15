---
brain_note_id: "dest:meetings:30613851fe2f964afb3c523e6c217fd6"
canonical_key: "meetings/30613851fe2f964afb3c523e6c217fd6"
brand_id: "meetings"
---
# Meeting — 2026-04-20

## Reunión

- Fecha: 2026-04-20
- Asistentes: Maria Jose Gonzalez Hernandez, Charlize Caro Mazzilli, Julian Felipe Rodriguez Barrera, Charlize Caro Mazzilli, Trellis Fields, Trellis Fields, Charlize Caro Mazzilli, Charlize Caro Mazzilli
- Video: https://t9017418223.p.clickup-attachments.com/t9017418223/7121cf4f-2e7f-4c57-8dd4-54cbec8b4161/7121cf4f-2e7f-4c57-8dd4-54cbec8b4161.mp4?view=open&filename=Herramientas%20para%20edici%C3%B3n%20de%20contenido%20%7C%20Cris%2C%20Julius%2C%20Char%20%26%20Moche%20%20-%2004-20-2026.mp4
- ClickUp: https://app.clickup.com/9017418223/v/dc/8cqnrff-15097/8cqnrff-17097
- Transcripción: [[02-Meetings/Transcripts/2026-04-20 Meeting Herramientas para edición de contenido Cris Julius (15097) - Transcript]]

**Notetaker**

**Attendees:** Maria Jose Gonzalez Hernandez, Charlize Caro Mazzilli, Julian Felipe Rodriguez Barrera, Charlize Caro Mazzilli, Trellis Fields, Trellis Fields, Charlize Caro Mazzilli, Charlize Caro Mazzilli
[https://t9017418223.p.clickup-attachments.com/t9017418223/7121cf4f-2e7f-4c57-8dd4-54cbec8b4161/7121cf4f-2e7f-4c57-8dd4-54cbec8b4161.mp4?view=open&filename=Herramientas%20para%20edici%C3%B3n%20de%20contenido%20%7C%20Cris%2C%20Julius%2C%20Char%20%26%20Moche%20%20-%2004-20-2026.mp4](https://t9017418223.p.clickup-attachments.com/t9017418223/7121cf4f-2e7f-4c57-8dd4-54cbec8b4161/7121cf4f-2e7f-4c57-8dd4-54cbec8b4161.mp4?view=open&filename=Herramientas%20para%20edici%C3%B3n%20de%20contenido%20%7C%20Cris%2C%20Julius%2C%20Char%20%26%20Moche%20%20-%2004-20-2026.mp4)

**Visión general**

La reunión se centró en la demostración práctica y la puesta en marcha de herramientas técnicas (Node.js, NPX, Remotion, Cloud Code, entre otras) para optimizar la edición de video y automatizar flujos de trabajo. Trellis Fields lideró la sesión, guiando al equipo a través de la instalación, configuración y resolución de problemas técnicos en tiempo real.

**Conclusiones clave**

*   Se decidió continuar con la demostración pese a los múltiples problemas técnicos, aplicando soluciones prácticas como reiniciar la terminal y desactivar el VPN.
*   Se acordó verificar la correcta instalación y configuración de Node.js, Chocolate, NPX, Remotion y Cloud Code para asegurar un entorno de trabajo estable.
*   Se optó por crear y utilizar una carpeta de plantillas (templates) para facilitar la reutilización de elementos en futuros proyectos y reducir así el tiempo de edición.
*   Se estableció la necesidad de registrar y compartir los logs de error y feedback para afinar la estrategia de troubleshooting y capacitación.

**Próximos pasos**

- [ ] **Por asignar**: Completar la instalación de Node.js y Chocolate siguiendo el tutorial presentado.
- [ ] **Por asignar**: Ejecutar los comandos NPX para crear proyectos de video y copiar el output en el chat para su verificación.
- [ ] **Por asignar**: Desactivar el VPN y reiniciar la terminal cuando se presenten conflictos que afecten la ejecución de comandos.
- [ ] **Por asignar**: Verificar el correcto funcionamiento de Remotion y Cloud Code en los sistemas utilizados (Windows y Mac).
- [ ] **Por asignar**: Crear y organizar una carpeta de plantillas que contenga los elementos y configuraciones para la edición de videos.
- [ ] **Por asignar**: Registrar y enviar los logs de error y feedback obtenido durante la sesión al equipo encargado.
- [ ] **Por asignar**: Revisar y actualizar los prompts para la creación de videos, incorporando mejoras basadas en la experiencia de esta capacitación.

**Temas Claves**

*   **Instalación y Configuración Inicial** Actualización
    *   Se inició la reunión con la descarga e instalación de Node.js utilizando el instalador (Standalone binary o Installer MSI) y la ejecución de comandos 'Next' para proceder por defecto.
    *   Se mencionó la instalación de Chocolate (posiblemente Chocolatey) de forma automática, y se verificó que los participantes pudieran seguir los pasos sin necesidad de reinstalar en equipos Mac, salvo cuando se presentaran nuevas funcionalidades.
    *   Maria José, Julian y Charlize confirmaron la ejecución exitosa de algunos pasos básicos (descarga, instalación y configuración inicial).

*   **Ejecución de Comandos NPX y Uso de la Terminal** Problema
    *   Se ejecutaron comandos NPX para crear proyectos de video, como 'npx create video', y se realizaron pruebas en la terminal para verificar que se copiara el output correcto.
    *   Se presentaron errores relacionados con la ejecución de scripts en PowerShell, incluidos mensajes sobre políticas de ejecución ('set execution policy scope current user') y archivos deshabilitados, lo cual derivó en instrucciones para cerrar y reabrir terminales.
    *   La sesión incluyó reiteradas instrucciones para copiar y pegar comandos en el chat, y se coordinó el troubleshooting en tiempo real para solucionar conflictos (por ejemplo, problemas por tener activado el VPN).

*   **Demostración del Uso de Remotion y Cloud Code** Actualización
    *   El facilitador mostró cómo utilizar Remotion para la edición automatizada de videos, explicando el proceso desde abrir la terminal hasta que aparezca el mensaje 'Server ready'.
    *   Se demostró la activación de una skill en Cloud Code (por ejemplo, 'Remotion Best Practice') para gestionar plantillas y elementos multimedia en el proyecto.
    *   Los participantes observaron el flujo en el que una interfaz basada en web permite trabajar en modo similar a programas de edición (como Photoshop) y verificar en vivo la ejecución de comandos.

*   **Organización de Plantillas y Flujo de Trabajo para Automatización** Idea
    *   Se discutió la importancia de crear y organizar carpetas de templates para que, en futuros proyectos, puedan reutilizarse elementos multimedia, scripts y el output de videos ya editados.
    *   El facilitador propuso el uso de prompts detallados (con el apoyo de herramientas como ChatGPT) para generar nuevas variantes de videos y superar bloqueos creativos, aprovechando los elementos guardados en los templates.
    *   Se hizo hincapié en la necesidad de mantener una estructura de archivos organizada para agilizar la edición y permitir la estandarización del flujo de trabajo creativo.

*   **Consideraciones Técnicas y Recomendaciones de Optimización** Decisión
    *   Se abordaron recomendaciones técnicas como desactivar el VPN para evitar conflictos durante la descarga y ejecución de comandos, así como sugerencias sobre el uso de adaptadores USB-C para conectar periféricos en portátiles.
    *   Se discutieron las implicancias de políticas de seguridad en PowerShell y se propusieron soluciones (como cerrar procesos a través del Task Manager) para resolver bloqueos en la ejecución de los comandos.
    *   El grupo intercambió comentarios sobre la lentitud de algunos equipos y se sugirió reiniciar aplicaciones o el propio computador cuando fuera necesario.

*   **Recomendaciones Finales, Próximos Pasos y Feedback** Decisión
    *   El facilitador recalcó que, a pesar de los múltiples problemas técnicos, se debía avanzar con la configuración y que cada participante debía copiar los outputs de los comandos para confirmar la correcta instalación.
    *   Se recomendaron pasos a seguir: completar las instalaciones, ejecutar los comandos correctamente, organizar los templates y documentar los errores y soluciones para compartirlos con Luis y el resto del equipo.
    *   Se enfatizó la importancia del feedback y la comunicación interna para ajustar los flujos de trabajo y garantizar que todos los miembros estén alineados para futuras sesiones de edición automatizada.

*   Transcript

    **Maria Jose Gonzalez Hernandez:** Hola,

    **Trellis Fields:** ¿Cómo estamos muchachos? ¿Cómo estamos?

    **Maria Jose Gonzalez Hernandez:** bien, bien ¿Y tú cómo? ¿Estás?

    **Trellis Fields:** Ahí vamos. Ah bueno, Luis me pidió que le hiciera una reunión con ustedes para mostrar las herramientas esa que encontré que es para editar, crear videos, para ser en verdad lo que sea, pero pues yo supongo que ustedes no hacen como que vídeos así tipo, no sé, inteligencia artificial, imágenes falsas, entonces supongo que les serviría a ustedes para editar, realmente yo desconozco bastante cómo es que editan ustedes o cómo es que hacen las cosas ustedes, entonces no sé si esto realmente les sirva o qué, o de pronto les ayuda, si un poquito en algo mínimo, pero igual Luis me dijo que les mostrara, entonces yo les muestro. Tantas personas aquí,

    **Maria Jose Gonzalez Hernandez:** ¿Son las notas?

    **Trellis Fields:** OK, OK, bueno, voy a mostrarles qué es lo que encontré y cómo funciona para que ustedes lo usen y lo cacharree y no se, miren para ver, o sea, hice un ejemplo, se llama Luquito, pero es porque no les explicar a la gente cómo hacer las cosas, entonces supongo que ustedes sabrán los términos y cómo hacerlo más bonito, entonces yo no sé, voy a compartir. Bueno, bueno muchachos, paso uno. Bueno, primero que todo, ya están todos ready en el computador, todo está perfecto,

    **Maria Jose Gonzalez Hernandez:** Sí,

    **Charlize Caro Mazzilli:** Yes.

    **Trellis Fields:** Primero que todo, descargar Node JS Creo que este tutorial va a demorar menos diría yo,

    **Maria Jose Gonzalez Hernandez:** dale, listo. Una pregunta, ¿Esto lo vamos a tener que hacer de nuevo con las Macs? Por ejemplo, lo que hicimos la vez pasada también.

    **Trellis Fields:** O sea, la idea es que yo, según el seteo que me dijo que hiciera Luis, me dijo que les dejara todo eso listo, entonces diría que no tienen que hacer de nuevo, pero ya cualquier otro feature nuevo que Luis quiera poner o que encontremos cada uno, pues ya eso sí hay que hacer un mini tutorial, pero igual ustedes en verdad descargar skills y agentes no tiene mucha ciencia, o sea, si ustedes ven un vídeo en TikTok o YouTube, lo que sea, normalmente ellos les explican y es literalmente 5 minutos que se demora en instalando algo, entonces no se preocupen, Bueno, me dice cuando lo descarguen,

    **Maria Jose Gonzalez Hernandez:** Lo instalamos,

    **Julian Felipe Rodriguez Barrera:** Le damos en Standalone binary o en Installer MSI de la izquierda. Una vez que le doy a instalar o le clic al setup, le doy a Next en todo. Next en todo

    **Trellis Fields:** Yes, next, next,

    **Julian Felipe Rodriguez Barrera:** automático. Install the necessary tools para instalar Chocolate.

    **Trellis Fields:** Pantalla,

    **Maria Jose Gonzalez Hernandez:** Yo le di todo Next e instalar

    **Julian Felipe Rodriguez Barrera:** Chocolate.

    **Trellis Fields:** dale, Sí,

    **Maria Jose Gonzalez Hernandez:** anda, yo no hice eso.

    **Trellis Fields:** pero bueno, creo que no importa, pero igual yo siempre lo veo como que todo automático, nada de CTO individual, pero creo que no importaría mucho.

    **Maria Jose Gonzalez Hernandez:** Dale,

    **Trellis Fields:** Vamos

    **Maria Jose Gonzalez Hernandez:** Bueno,

    **Trellis Fields:** a ver qué pasa.

    **Maria Jose Gonzalez Hernandez:** Está

    **Charlize Caro Mazzilli:** No vi

    **Maria Jose Gonzalez Hernandez:** bien.

    **Charlize Caro Mazzilli:** que le dio.

    **Trellis Fields:** Salió una pestañita como un checkbox, no hay ni que chocolate

    **Charlize Caro Mazzilli:** Ça se

    **Trellis Fields:** a

    **Charlize Caro Mazzilli:** active.

    **Trellis Fields:** Charles.

    **Julian Felipe Rodriguez Barrera:** Para tener todos los juguetes

    **Trellis Fields:** Ajá, exacto,

    **Julian Felipe Rodriguez Barrera:** necesito

    **Trellis Fields:** pero creo

    **Julian Felipe Rodriguez Barrera:** café.

    **Trellis Fields:** que eso no afecta el precio del padre, o sea, yo no hice eso que están haciendo ustedes, que eso lo hice hace meses, entonces no me acuerdo qué puse yo, entonces supongo que todo es automático, no creo

    **Maria Jose Gonzalez Hernandez:** Aha.

    **Trellis Fields:** que afecte el proceso

    **Maria Jose Gonzalez Hernandez:** ¿Qué sigue?

    **Trellis Fields:** siguiente. ¿Ya se les instaló? ¿OK, sí o no? ¿Bueno, vamos a esperar un par minuticos,

    **Julian Felipe Rodriguez Barrera:** ¿Que han hecho, compadres? A mí me sigue instalando. Dice installing node js y status me quedan cero. Se

    **Trellis Fields:** o sea, se instaló o no se instaló?

    **Julian Felipe Rodriguez Barrera:** me está enterando. Ah, es que me salió una ventana emergente y no le di así. Ahora sí. Updating. Muy bien,

    **Maria Jose Gonzalez Hernandez:** ¿El chocolate Y que?

    **Julian Felipe Rodriguez Barrera:** chocolate.

    **Trellis Fields:** No te tocaba, no te tocaba,

    **Charlize Caro Mazzilli:** Me salió como una pantalla que dice Install Additional Tools y se presiona la tecla para continuar.

    **Trellis Fields:** dale todo, todo lo que sea adicional más siempre va a ayudar. No sé ni qué dije, pero me entendía,

    **Julian Felipe Rodriguez Barrera:** Presione una tecla. Ahora me abrió el CMD. Creo que alguien deberá compartir. Voy a compartir pantalla como para tener un seguimiento de lo que

    **Trellis Fields:** Si, muestra para ver qué está haciendo último,

    **Julian Felipe Rodriguez Barrera:** está ocurriendo en este instante del tiempo.

    **Charlize Caro Mazzilli:** Me abrió el windows power chain.

    **Trellis Fields:** OK, supongo que ya se los instaló, Dale, dale,

    **Julian Felipe Rodriguez Barrera:** ¿Salió el símbolo del sistema?

    **Trellis Fields:** dale, dale, dame cualquier tecla, dale espacio ya, OK, abre curso, Creo que eso no importa,

    **Julian Felipe Rodriguez Barrera:** ¿Que me estás instalando, compadre?

    **Trellis Fields:** es chocolate, Chocolate instaling chocolate

    **Julian Felipe Rodriguez Barrera:** Esa es la clave. Mineki.

    **Trellis Fields:** Sigue abriendo cursor, todo

    **Charlize Caro Mazzilli:** Espero que me llegue chocolate.

    **Trellis Fields:** chocolate. Ah muchachos, by the way, tienen que cambiar la cuenta de cursor que antes estaba con Discipline Rift, Luis me dijo que eso no le gusta, así que lo pongamos todo modo trail mientras que se descarga eso, entran a cursor, todos se van a la parte de arriba a la derecha donde salís que Upgrade to pro, el último de la derecha que es como el de ajuste, el de siempre, de toda la vida, le hunden ahí,

    **Julian Felipe Rodriguez Barrera:** ¿Por qué será que no me cargue el Cloud Code? ¿Qué hemos hecho, compadres?

    **Trellis Fields:** abre el ser lo que lo viste, lo que viste arriba al lado de upgrade bro, arriba a la derecha, a la derecha, no a la derecha. Settings, settings.

    **Julian Felipe Rodriguez Barrera:** Ya leí. Le estoy spameando clic como loco.

    **Trellis Fields:** ¿Está pensando

    **Julian Felipe Rodriguez Barrera:** Si, está

    **Trellis Fields:** o

    **Julian Felipe Rodriguez Barrera:** echándole

    **Trellis Fields:** se

    **Julian Felipe Rodriguez Barrera:** mente.

    **Trellis Fields:** raya? Cierra y abre cursor Ey, por qué cerraste eso,

    **Julian Felipe Rodriguez Barrera:** Ya está. Me dice que se reabre.

    **Trellis Fields:** o sea cierra y abre cursor,

    **Julian Felipe Rodriguez Barrera:** Entonces ¿Qué pasó con el chocolate?

    **Trellis Fields:** No sé.

    **Julian Felipe Rodriguez Barrera:** Es chocolate. Chocolate, Chocolate. No pasa nada.

    **Trellis Fields:** Cule necio

    **Julian Felipe Rodriguez Barrera:** Ahora vas a ver Amargo.

    **Trellis Fields:** que cierra todo, Faltaba era

    **Julian Felipe Rodriguez Barrera:** Cierra

    **Trellis Fields:** que

    **Julian Felipe Rodriguez Barrera:** todo. Cierra

    **Trellis Fields:** apagaras

    **Julian Felipe Rodriguez Barrera:** el.

    **Trellis Fields:** el computador porque no ab.

    **Julian Felipe Rodriguez Barrera:** No me queda esta vaina. Ñañero, No sé qué es lo que está pasando.

    **Trellis Fields:** Mata, mata,

    **Julian Felipe Rodriguez Barrera:** ¿Vamos a cerrar todo de verdad?

    **Trellis Fields:** mata el proceso, Entra, entra, ya sé entra Task Manager en la barrita de buscar,

    **Julian Felipe Rodriguez Barrera:** Sí, sí,

    **Trellis Fields:** bueno, entra task manager y mata el proceso

    **Julian Felipe Rodriguez Barrera:** vamos a cerrar el.

    **Trellis Fields:** supone instalar el chocolate,

    **Maria Jose Gonzalez Hernandez:** ¿Julián, estamos grabando la reunión?

    **Trellis Fields:** claro que no la están grabando, no están grabando.

    **Maria Jose Gonzalez Hernandez:** Sí, sí, está en las notas de ClickUp.

    **Julian Felipe Rodriguez Barrera:** ¿Y por qué no?

    **Trellis Fields:** Tú juras que Luis ve, tú

    **Maria Jose Gonzalez Hernandez:** No,

    **Trellis Fields:** juras,

    **Maria Jose Gonzalez Hernandez:** pero yo no, pero yo sí.

    **Trellis Fields:** La verdad que tú eres la segunda admin

    **Julian Felipe Rodriguez Barrera:** My

    **Trellis Fields:** qué

    **Julian Felipe Rodriguez Barrera:** people

    **Trellis Fields:** decirte. ¿Cierra Cloud Code, cierra la pestaña Cloud Code, a ver,

    **Julian Felipe Rodriguez Barrera:** juega. Santo remedio. Este no sabe mucho.

    **Trellis Fields:** ahí está, dale a cómo es que se sale ahí? ¿Dale a cursor account, dale open, a la derecha será, no? Vete a cursar, baja, no sé, por ahí debe estar para el logout, ahí está lugar, ahora sube sign in y inicia sesión con Google de Travis,

    **Julian Felipe Rodriguez Barrera:** ¿No importa?

    **Trellis Fields:** dale cancel,

    **Maria Jose Gonzalez Hernandez:** Todos tenemos que hacer eso.

    **Trellis Fields:** Sí, sí, para que lo pongan en modo trading entonces

    **Maria Jose Gonzalez Hernandez:** ¿Puedes

    **Trellis Fields:** settings,

    **Maria Jose Gonzalez Hernandez:** hacerlo otra vez?

    **Trellis Fields:** sí habrán settings, en settings váyanse a logout. ¿Abre curso otra vez? Julián,

    **Maria Jose Gonzalez Hernandez:** Dijo que ya venía, creo. ¿Puedo compartir pantalla? Pantalla completa.

    **Trellis Fields:** ¿Ya leíste los gauss? Ah no mentira, baja, baja ahí logout, ahora sube, dale, sign in y le das contrin contra,

    **Charlize Caro Mazzilli:** No, porque no carga. Estoy dando,

    **Trellis Fields:** no te carga, cierra

    **Charlize Caro Mazzilli:** o sea le doy

    **Trellis Fields:** la,

    **Charlize Caro Mazzilli:** a.

    **Trellis Fields:** comparte pantalla, comparte pantalla

    **Julian Felipe Rodriguez Barrera:** ¿Que señor? Bueno, no me deja.

    **Trellis Fields:** otra vez, mira, ya ahí te sale sign in No, no, bueno sí o bueno no, Cierra la pestaña esa, no importa Dale, sign in. Ahora sí te sale y le das con Google de Terel, Abre cursor, chatlist,

    **Julian Felipe Rodriguez Barrera:** ¿Ahora que me pide? Código de verificación

    **Trellis Fields:** métete ahí a settings, cierra la pestaña de Cloud Code.

    **Julian Felipe Rodriguez Barrera:** en tu tablet. Llegó un código de verificación. 52 Un

    **Charlize Caro Mazzilli:** La pestaña,

    **Julian Felipe Rodriguez Barrera:** número

    **Charlize Caro Mazzilli:** es algo.

    **Trellis Fields:** Tú ves la. Exacto, cierra eso. Ahora sí,

    **Maria Jose Gonzalez Hernandez:** ¿Qué pasó?

    **Julian Felipe Rodriguez Barrera:** en la tablet te llegó un número de verificación para yo poder entrar con la cuenta de teles aquí.

    **Maria Jose Gonzalez Hernandez:** Ya,

    **Trellis Fields:** ahora sí

    **Julian Felipe Rodriguez Barrera:** Bueno,

    **Trellis Fields:** baja

    **Julian Felipe Rodriguez Barrera:** dice galaxy s.

    **Trellis Fields:** Logout.

    **Julian Felipe Rodriguez Barrera:** No sé si se para el celular. Sí. OK, ya me está verificando. Súper, excelente. Parece que ya se pudo.

    **Trellis Fields:** Bueno muchachos, muchachos, muchachos. ¿Se le instaló todos? No, manito arriba para decir que sí.

    **Maria Jose Gonzalez Hernandez:** ¿Que sigue? ¿Azulet? Sí, ya, a mí se me descargó

    **Trellis Fields:** Sí, dale, sí. Login. Ah no, mentira, que espérate, no, espérate, ahorita sale eso. Dale, cancel. Los tres punticos.

    **Julian Felipe Rodriguez Barrera:** Dijo Luis la pregunta que.

    **Maria Jose Gonzalez Hernandez:** porque no tienes puesto el VPN.

    **Julian Felipe Rodriguez Barrera:** Yo Estamos. Del oficio.

    **Trellis Fields:** ¿Cómo está?

    **Julian Felipe Rodriguez Barrera:** Veo muy ocupados.

    **Trellis Fields:** ¿Cómo van los js muchachos?

    **Julian Felipe Rodriguez Barrera:** Intentar otra vez. Login group trailer set free Return to cursor. Excelente, ya puedo. Todo está setup.

    **Trellis Fields:** Correcto, es correcto,

    **Julian Felipe Rodriguez Barrera:** Esperemos a que entonces.

    **Trellis Fields:** dale Login con Trellis. Charlie está como muy pasivo agresiva con ese cursor.

    **Julian Felipe Rodriguez Barrera:** Diablazo, papá Dios. Everybody's falling in love and I'm falling behind. Mientras tanto, ¿Por qué no?

    **Trellis Fields:** Muchachos, una pregunta,

    **Maria Jose Gonzalez Hernandez:** Oigan qué embarrada el primer post de Trellis

    **Julian Felipe Rodriguez Barrera:** ¿Por

    **Charlize Caro Mazzilli:** ¿Por

    **Julian Felipe Rodriguez Barrera:** qué?

    **Charlize Caro Mazzilli:** qué

    **Maria Jose Gonzalez Hernandez:** sali que nuestra misión y era Visión sale duplicado

    **Charlize Caro Mazzilli:** no? Pero si se puede cambiar, cámbienlo y yo lo corrijo sin quitarlo.

    **Maria Jose Gonzalez Hernandez:** Dale, anda que embarra.

    **Trellis Fields:** ¿Luis se dio cuenta?

    **Maria Jose Gonzalez Hernandez:** No se dio cuenta, Se dio cuenta mi hermana,

    **Trellis Fields:** Qué rico, qué rico, qué rico.

    **Julian Felipe Rodriguez Barrera:** ¿Qué?

    **Maria Jose Gonzalez Hernandez:** Mi

    **Julian Felipe Rodriguez Barrera:** Bueno,

    **Maria Jose Gonzalez Hernandez:** hermana me lo mandó y me dijo visión

    **Julian Felipe Rodriguez Barrera:** gigi. Gigi.

    **Maria Jose Gonzalez Hernandez:** mierda. ¿Cuál es nuestra misión, nuestra visión?

    **Julian Felipe Rodriguez Barrera:** Voy a hacer.

    **Trellis Fields:** ¿Este? ¿Bueno, ahora se van a abrir una terminal como les enseñé que se abrió la terminal muchachos, Si prestaron atención,

    **Charlize Caro Mazzilli:** Cómo se que ya. Porque aquí pareciera que no.

    **Trellis Fields:** no? Parece que no da la trabajo.

    **Maria Jose Gonzalez Hernandez:** Yo te presté atención, Mira, voy a compartirte la pantalla completa

    **Trellis Fields:** Abre otra vez curso,

    **Maria Jose Gonzalez Hernandez:** Ya pueden verme

    **Julian Felipe Rodriguez Barrera:** Yes.

    **Maria Jose Gonzalez Hernandez:** Terminal nueva terminal, mira.

    **Trellis Fields:** Nivel, Nivel,

    **Julian Felipe Rodriguez Barrera:** Claramente que el que le sabe, le sabe y el que no le sabe

    **Maria Jose Gonzalez Hernandez:** Claro

    **Trellis Fields:** exacto.

    **Maria Jose Gonzalez Hernandez:** y

    **Trellis Fields:** Bueno, prueba de fuego para ver si de verdad se les instaló. Node js,

    **Julian Felipe Rodriguez Barrera:** la

    **Trellis Fields:** Copien

    **Julian Felipe Rodriguez Barrera:** que puede,

    **Trellis Fields:** lo que les pegué.

    **Julian Felipe Rodriguez Barrera:** la que no. Critico

    **Trellis Fields:** Copien lo que les pegué de NPX

    **Julian Felipe Rodriguez Barrera:** en el chat. OK, ahí sí, ¿Verdad? NPX

    **Trellis Fields:** lo pegan en la terminal. Exacto.

    **Julian Felipe Rodriguez Barrera:** que no se puede porque.

    **Maria Jose Gonzalez Hernandez:** se puede cargar el archivo porque está deshabilitada en este sistema para mayor información

    **Trellis Fields:** OK, vamos a probar otra opción. Vete a la barrita esa búsqueda donde están las extensiones, donde sale lo de Cloud Code, vete arriba y busca node js en search extension node js, js.

    **Julian Felipe Rodriguez Barrera:** Parte de arriba extensions

    **Maria Jose Gonzalez Hernandez:** ¿Cuál, cuál es?

    **Julian Felipe Rodriguez Barrera:** No,

    **Trellis Fields:** Ya te digo,

    **Julian Felipe Rodriguez Barrera:** Pero quería tanto chocolate. No lo defraudaré, papá. Le voy a enseñar a hacer chocolate casero. Le voy a enseñar a conectar cursor con node JS de forma casera. Me cree solo si lo veo,

    **Trellis Fields:** No sé qué hacer muchachos, pero son los vainas que me dan rabia. Charlie, a ti te dejó, a ningún lo dejó.

    **Maria Jose Gonzalez Hernandez:** No me.

    **Julian Felipe Rodriguez Barrera:** Pero quería conectar. No JS concurso. No se preocupe, le voy a enseñar a conectar.

    **Maria Jose Gonzalez Hernandez:** Charlie,

    **Julian Felipe Rodriguez Barrera:** No,

    **Maria Jose Gonzalez Hernandez:** ya actualicé la imagen, es la número 4, te voy a pasar el link, lo

    **Julian Felipe Rodriguez Barrera:** solo si lo veo.

    **Maria Jose Gonzalez Hernandez:** pasaré aquí por el chat.

    **Julian Felipe Rodriguez Barrera:** Me

    **Trellis Fields:** Reflexionemos juntos muchachos.

    **Maria Jose Gonzalez Hernandez:** Bueno, al final no es

    **Julian Felipe Rodriguez Barrera:** creo

    **Maria Jose Gonzalez Hernandez:** ninguno de.

    **Trellis Fields:** Peguen la terminal de ustedes en el PowerShell, a ver si, o sea, habrán PowerShell en la barra buscada en tu computador.

    **Julian Felipe Rodriguez Barrera:** de chocolate que cerré.

    **Trellis Fields:** Sí, eso mismo. Windows s. A ver, ejecuta eso,

    **Julian Felipe Rodriguez Barrera:** Pegado el drive. Ya dice que no se puede, que el archivo está deshabilitada la ejecución de scripts en el sistema.

    **Trellis Fields:** pasan eso, Copy t. Vamos a ver qué podemos hacer muchachos. ¿Qué debería hacer?

    **Julian Felipe Rodriguez Barrera:** Opción a, opción b.

    **Trellis Fields:** ¿Decirle a Luis? No se puede Muchachos, ejecuten eso en PowerShell para ver qué les dice, a ver cómo los trata,

    **Maria Jose Gonzalez Hernandez:** Cosa,

    **Julian Felipe Rodriguez Barrera:** Esperemos que me dé el princess treatment. Oígame, parece que todo bien, no me dio errores esto, No, Vamos a intentar atrás con el npx.

    **Trellis Fields:** Pero intentenlo en curso.

    **Julian Felipe Rodriguez Barrera:** OK. Need to install the front packages.

    **Trellis Fields:** Lo mismo te

    **Julian Felipe Rodriguez Barrera:** Ahora

    **Trellis Fields:** salió

    **Julian Felipe Rodriguez Barrera:** sí tengo permiso, pero que me falta un paquete por instalar.

    **Trellis Fields:** el chocolate, Imagina

    **Julian Felipe Rodriguez Barrera:** Dice que me falta el create video 4 0 4 5

    **Trellis Fields:** qué

    **Julian Felipe Rodriguez Barrera:** 0

    **Trellis Fields:** rico, dale y que mucho le está saliendo.

    **Julian Felipe Rodriguez Barrera:** acá en la firme. Vamos a ver, vamos a hacer la intentación. Yo

    **Trellis Fields:** Pero lo están haciendo en dónde lo están haciendo en curso.

    **Maria Jose Gonzalez Hernandez:** Yo

    **Julian Felipe Rodriguez Barrera:** lo

    **Maria Jose Gonzalez Hernandez:** estoy

    **Julian Felipe Rodriguez Barrera:** hice

    **Maria Jose Gonzalez Hernandez:** haciendo

    **Julian Felipe Rodriguez Barrera:** en

    **Maria Jose Gonzalez Hernandez:** el curso

    **Trellis Fields:** Hazlo

    **Julian Felipe Rodriguez Barrera:** y

    **Trellis Fields:** en curso,

    **Julian Felipe Rodriguez Barrera:** en amo

    **Trellis Fields:** hazlo todo en curso.

    **Julian Felipe Rodriguez Barrera:** y en amo me sale que necesito el package create video.

    **Trellis Fields:** A ver,

    **Julian Felipe Rodriguez Barrera:** OK, to proceed.

    **Maria Jose Gonzalez Hernandez:** Sí, dale Yes.

    **Julian Felipe Rodriguez Barrera:** Okay,

    **Trellis Fields:** Dale blank, dale enter a Blanc

    **Julian Felipe Rodriguez Barrera:** ahora sí me sale todo.

    **Trellis Fields:** Direct, dale enter. Yeah, Yes, yes, yes.

    **Julian Felipe Rodriguez Barrera:** Me salió error. Add agent skills get additional. Buen hecho.

    **Trellis Fields:** Pienso y reflexiono y medito. Pienso, reflexiono,

    **Maria Jose Gonzalez Hernandez:** Y

    **Trellis Fields:** medito

    **Maria Jose Gonzalez Hernandez:** renuncias,

    **Trellis Fields:** y renuncio. Exacto.

    **Julian Felipe Rodriguez Barrera:** En efecto, mejor anuncio,

    **Maria Jose Gonzalez Hernandez:** Eso se va para Redevel

    **Julian Felipe Rodriguez Barrera:** Pero está grabando todo. Todo en plan video.

    **Trellis Fields:** No, no

    **Maria Jose Gonzalez Hernandez:** No,

    **Trellis Fields:** hay vídeo. Si no hay vídeo no cuenta.

    **Maria Jose Gonzalez Hernandez:** o sea, sí es que Click graba el vídeo

    **Julian Felipe Rodriguez Barrera:** Ah, excelente. No, Bien,

    **Maria Jose Gonzalez Hernandez:** Agraba cada vez que una persona habla se escucha la voz y editamos eso,

    **Julian Felipe Rodriguez Barrera:** Identifique al menos como tres clips aquí cuando dices hey muchachos, se está grabando la reunión. Opción A renunciar y colma. Y la de meditar que dijo Cristian Y sale contenido de redes. Mi gente, mi maestro siempre dijo que hay que saber balancear erotismo y la profesionalidad.

    **Trellis Fields:** Con clau. Vamos a hacer lo siguiente muchachos, vamos a hacer lo siguiente. Ok, ok, ok, ok chicos. Bueno, vamos a hacer esto muchachos, Váyanse otra vez a cursor. Van a abrir

    **Julian Felipe Rodriguez Barrera:** Listo.

    **Trellis Fields:** un chat de Cloud como les enseñé la vez pasada

    **Maria Jose Gonzalez Hernandez:** O sea escribimos Cloud.

    **Trellis Fields:** o lo hacen desde la aplicación de Como ustedes quieran. ¿Como quiera, quiero cómo le enseñé que se hacía eso, no?

    **Julian Felipe Rodriguez Barrera:** ¿Qué crees que hicieron?

    **Trellis Fields:** Y después abre, abre, abre Cloud todos necesito que abran Cloud como les enseñé y el resto cómo estaba el resto

    **Julian Felipe Rodriguez Barrera:** No, disculpa, es que Luis me escribió una cosa que necesita urgente. Creo que tenemos que ser.

    **Trellis Fields:** abre Cloud Code como les enseñé. Hay otra manera más sencilla como les había enseñado muchachos, por favor. Mira la pantalla Moche enseñ

    **Julian Felipe Rodriguez Barrera:** Okay.

    **Trellis Fields:** Tira la clara.

    **Maria Jose Gonzalez Hernandez:** Voy a cerrar esto, síganme muchachos. Tú te vas a la parte de extensiones y buscas Cloud que tienes instalado pues te va a salir ahí, le das clic ahí ¿Qué pasa cuando tiene punticos acá? Y le das abrir ya y te va a salir y cierra la terminal Si la tienes abajo

    **Trellis Fields:** Ahí está,

    **Julian Felipe Rodriguez Barrera:** Verdaderamente,

    **Trellis Fields:** eso es todo.

    **Julian Felipe Rodriguez Barrera:** el que le sabe, le

    **Trellis Fields:** Eso,

    **Julian Felipe Rodriguez Barrera:** sabe

    **Trellis Fields:** eso es

    **Julian Felipe Rodriguez Barrera:** Desde

    **Trellis Fields:** todo. Ahí

    **Julian Felipe Rodriguez Barrera:** tiempo

    **Trellis Fields:** está.

    **Julian Felipe Rodriguez Barrera:** es mejorar la inteligencia humana ha sido símbolo de prestigio.

    **Trellis Fields:** Sí, tienen que prestar más atención muchachos, por favor, por favor. Dale pull al repo y le copian el mensajito que les puse abajo, el link le dicen dale pool al repo y se lo pegan ahí

    **Maria Jose Gonzalez Hernandez:** aquí

    **Trellis Fields:** cas

    **Maria Jose Gonzalez Hernandez:** dale pull así

    **Trellis Fields:** al repo

    **Maria Jose Gonzalez Hernandez:** al repo

    **Trellis Fields:** y ya

    **Maria Jose Gonzalez Hernandez:** le copio

    **Trellis Fields:** copias el link. Exacto,

    **Maria Jose Gonzalez Hernandez:** así, confírmame. Si,

    **Trellis Fields:** Exacto,

    **Maria Jose Gonzalez Hernandez:** así

    **Trellis Fields:** correcto. ¿Eso?

    **Maria Jose Gonzalez Hernandez:** y

    **Julian Felipe Rodriguez Barrera:** ¿What did you do?

    **Trellis Fields:** ¿Escribe dale pura al repo y pegas el link que puse en el chat

    **Maria Jose Gonzalez Hernandez:** le das yes.

    **Trellis Fields:** absolutamente a todo, OK?

    **Julian Felipe Rodriguez Barrera:** Y es esto de set execution policy scope. ¿Qué es eso? Lo

    **Trellis Fields:** No sé qué

    **Julian Felipe Rodriguez Barrera:** tengo

    **Trellis Fields:** estás

    **Julian Felipe Rodriguez Barrera:** que escribir

    **Trellis Fields:** viendo.

    **Julian Felipe Rodriguez Barrera:** el chat de la llamada set execution policy scope current user.

    **Trellis Fields:** No,

    **Julian Felipe Rodriguez Barrera:** ¿Que es eso?

    **Trellis Fields:** eso

    **Julian Felipe Rodriguez Barrera:** Que

    **Trellis Fields:** fue un paso antes. Copia el link que sale abajo de GitHub, co Escribes en el chat en Cloud Code, dale pull al repo y le pegas el link y le das enter,

    **Julian Felipe Rodriguez Barrera:** depura el repo. ¿Cómo

    **Trellis Fields:** si,

    **Julian Felipe Rodriguez Barrera:** lo

    **Trellis Fields:** Dale

    **Julian Felipe Rodriguez Barrera:** voy a depurar?

    **Trellis Fields:** pool, dale pura al repo y dale pura al repo. Dices así al chat,

    **Julian Felipe Rodriguez Barrera:** Dale pool al repo. Así.

    **Trellis Fields:** pura el report, dale pura, si, eso es todo y le pegas el link. Compadre, ¿Qué pasó ahí?

    **Julian Felipe Rodriguez Barrera:** Para que lo cierro.

    **Trellis Fields:** No, no, no, dale. Link, pe.

    **Julian Felipe Rodriguez Barrera:** Otra vez

    **Trellis Fields:** No

    **Julian Felipe Rodriguez Barrera:** Locura.

    **Trellis Fields:** mis tokens.

    **Maria Jose Gonzalez Hernandez:** Tu

    **Julian Felipe Rodriguez Barrera:** Oh, mis tokens lo ya yes a todo y que yes, absolutamente todo.

    **Trellis Fields:** Exacto Charlie, tú cómo,

    **Charlize Caro Mazzilli:** Mal. ¿Por qué no cargo?

    **Trellis Fields:** pero trata lo bonito, dile, no sé el video por favor.

    **Julian Felipe Rodriguez Barrera:** Funciona. Mi terminal consentido ya funciona.

    **Maria Jose Gonzalez Hernandez:** MacBook Pro no te haría eso Charlie

    **Trellis Fields:** Cierra, cierra todo chat, deja solo curso. El Chrome, el chrome, cierra las 14 pestañas que tiene de Chrome.

    **Charlize Caro Mazzilli:** ¿Este Moche? Creo que va a tocar volver a publicar eso porque.

    **Maria Jose Gonzalez Hernandez:** lo deja. ¿No, dale, no pasa nada Aunque déjame intentarlo a mí de mi teléfono para o

    **Trellis Fields:** Lo importante

    **Maria Jose Gonzalez Hernandez:** tengo que iniciar?

    **Trellis Fields:** es que Luis no se dé cuenta la grabación

    **Maria Jose Gonzalez Hernandez:** ¿Cuál es la contraseña de Trelis? Me la va a pasar por WhatsApp, No me la vaya a decir por acá.

    **Trellis Fields:** no creo,

    **Maria Jose Gonzalez Hernandez:** ¿Hacerme la por anda verdad que estoy compartiendo? Me la pasas aquí por WhatsApp.

    **Charlize Caro Mazzilli:** Give me a minute. Una contraseña súper difícil. Okay,

    **Trellis Fields:** No, Beta se ve bonita, se ve chévere muchacho, mire, acabo de hacer una prueba de edición

    **Maria Jose Gonzalez Hernandez:** No es esa.

    **Trellis Fields:** de lo que, lo que me pasaste tu Moche y se ve bastante bien, siento que esta herramienta la full de pronto no le quedaría 100% perfecto pero les quita o bueno, en verdad no sé cuánto se demoran ustedes editando un vídeo,

    **Julian Felipe Rodriguez Barrera:** Dos horas y media, tres horas,

    **Trellis Fields:** pero no, no, no, editando solo, o sea, ya tienes todos los clips, ya los tienes juntos, no sé, y editarlo como tal

    **Julian Felipe Rodriguez Barrera:** Una hora más o menos. Sí, no, como media, si uno tiene todos los clips. Bueno, no importa.

    **Trellis Fields:** realmente el problema de ustedes siempre va a ser encontrar los clips

    **Julian Felipe Rodriguez Barrera:** Si, eso es como lo que más. Lo que es más tedioso por el tema de que no, pues tengo que carpeta buscar separar como el momento del b roll que. Que concuerde con lo que está diciendo el voiceover.

    **Trellis Fields:** igual yo les doy la herramienta pero

    **Julian Felipe Rodriguez Barrera:** Claro,

    **Trellis Fields:** igual eso

    **Julian Felipe Rodriguez Barrera:** claro,

    **Trellis Fields:** ya siempre va a ser como. Eso siempre va a ser como muy manual.

    **Julian Felipe Rodriguez Barrera:** en efecto.

    **Trellis Fields:** Efecto caballero.

    **Julian Felipe Rodriguez Barrera:** Bueno, Cher, muchas gracias.

    **Trellis Fields:** Me dice cuando terminen de hacer lo que

    **Julian Felipe Rodriguez Barrera:** Lo

    **Trellis Fields:** cambiar,

    **Julian Felipe Rodriguez Barrera:** de

    **Trellis Fields:** de poner, de quitar, no sé, no está cambiando o que estamos esperando,

    **Charlize Caro Mazzilli:** Yo no le podía hacer, está lento.

    **Maria Jose Gonzalez Hernandez:** Aquí

    **Trellis Fields:** Todos están ahí.

    **Maria Jose Gonzalez Hernandez:** No, no todos Charlie no lo ha podido hacer

    **Julian Felipe Rodriguez Barrera:** pool completo. ¿Settings

    **Trellis Fields:** Bueno, hasta

    **Julian Felipe Rodriguez Barrera:** what?

    **Trellis Fields:** que Charlie no haga, nadie se va a avanzar de aquí, nadie se va a esta reunión, OK,

    **Julian Felipe Rodriguez Barrera:** Bueno, ¿Y entonces? Bueno, ya me dijiste que tenía que darle pool a tal cosa Y luego lo de arriba, lo de SEC Execution Policy Scope.

    **Trellis Fields:** eso no importa.

    **Maria Jose Gonzalez Hernandez:** Charlie,

    **Julian Felipe Rodriguez Barrera:** OK,

    **Maria Jose Gonzalez Hernandez:** No nos complicamos, tenemos esa vaina, así nadie va a saber qué servicio.

    **Julian Felipe Rodriguez Barrera:** Los

    **Maria Jose Gonzalez Hernandez:** Los

    **Julian Felipe Rodriguez Barrera:** noto.

    **Maria Jose Gonzalez Hernandez:** únicos que sabemos eso somos nosotros,

    **Trellis Fields:** Y

    **Maria Jose Gonzalez Hernandez:** nadie se va a dar

    **Trellis Fields:** Luis

    **Maria Jose Gonzalez Hernandez:** cuenta.

    **Trellis Fields:** sabe eso,

    **Maria Jose Gonzalez Hernandez:** No, Qué risa Cris, que ris.

    **Trellis Fields:** Pero nos hicieron suficientemente sorprendida cuando Luis dijo que les iba a dar las max

    **Charlize Caro Mazzilli:** ¿Cómo

    **Trellis Fields:** que no se hicieron suficientemente

    **Maria Jose Gonzalez Hernandez:** No

    **Trellis Fields:** sorprendidos cuando Luis dijo que les iba a dar las max. Tienen que decir wow,

    **Maria Jose Gonzalez Hernandez:** se

    **Trellis Fields:** tienen

    **Maria Jose Gonzalez Hernandez:** sintió.

    **Trellis Fields:** que llorar,

    **Charlize Caro Mazzilli:** y qué

    **Trellis Fields:** tienen

    **Charlize Caro Mazzilli:** más? Que.

    **Trellis Fields:** que llorar, tenían que mandar un audio llorando.

    **Maria Jose Gonzalez Hernandez:** Sí ya había

    **Trellis Fields:** Dijo

    **Maria Jose Gonzalez Hernandez:** dicho.

    **Trellis Fields:** que iba a dar una

    **Julian Felipe Rodriguez Barrera:** Read instructor. Okay.

    **Trellis Fields:** Charlie no sé reinicia el compu, no seas lo que lo que consideres.

    **Maria Jose Gonzalez Hernandez:** Una pregunta, esos computadores, o sea, a mí no me gustan mucho como los touchpad de los portátiles. ¿Eso se puede conectar algún mouse? Y si se puede conectar algún mouse a cualquier tipo de. No sé, compatibilidad con cualquiera.

    **Trellis Fields:** Yo creo que como eso son 2020 20 21 creo. Mentira, en verdad no estoy seguro. De

    **Maria Jose Gonzalez Hernandez:** El mío es 2019,

    **Trellis Fields:** pronto el tuyo sí Moch. Exacto, eso te iba a decir. ¿De pronto el tuyo tenga tipo USB de pronto, pero de Charlie y Julián sé que son tipo C de todas maneras adicional a eso se le puede, o sea le pueden comprar un adaptador de eso, un adaptador no, cómo que se llama

    **Julian Felipe Rodriguez Barrera:** Circumstance

    **Trellis Fields:** eso?

    **Julian Felipe Rodriguez Barrera:** yours.

    **Trellis Fields:** ¿No sé cómo llamarlo, pero como un exten, o sea extender los puertos con un adaptador, no sé cómo se le dice eso exactamente, pero eso cuesta como 20 mil pesos mercado libre que literalmente lo conectas siendo tipo C y tiene USB, tiene HDMI, tiene más puertos tipo cómo se le llama eso? Pero me entendieron, cuesta como 20 mil pesos mercado libre,

    **Maria Jose Gonzalez Hernandez:** Le puedo

    **Trellis Fields:** no te

    **Maria Jose Gonzalez Hernandez:** conectar.

    **Trellis Fields:** compras un

    **Maria Jose Gonzalez Hernandez:** Tenía pensado en. Porque yo tengo acá un mouse Logitech, entonces de pronto le sirva. No sé

    **Trellis Fields:** es tipo USB

    **Maria Jose Gonzalez Hernandez:** si es USB.

    **Trellis Fields:** de pronto es que de pronto el tuyo sí, no estoy seguro, estoy seguro que

    **Maria Jose Gonzalez Hernandez:** OK,

    **Trellis Fields:** Julián si son tipo C 100% creo.

    **Maria Jose Gonzalez Hernandez:** son más de mouse, pero bueno.

    **Trellis Fields:** Hay que ver, hay que ver

    **Maria Jose Gonzalez Hernandez:** Es que pel.

    **Trellis Fields:** Charlie cómo vamos tu disculpa mami.

    **Maria Jose Gonzalez Hernandez:** Voy a dejar de compartir para que Charlie comparta y se vea lo que ella

    **Trellis Fields:** Si

    **Maria Jose Gonzalez Hernandez:** escuchando.

    **Trellis Fields:** comparte Charlie se va más lento,

    **Maria Jose Gonzalez Hernandez:** No, pero es que no se sabe lo que ella tiene, de pronto está esperando a que carga algo que no es. Julián, ¿Puedes dejar de compartir

    **Trellis Fields:** eso es verdad,

    **Maria Jose Gonzalez Hernandez:** para que Charlie nos muestre?

    **Trellis Fields:** Está chambeando mientras está en la reunión. El

    **Maria Jose Gonzalez Hernandez:** Claro,

    **Trellis Fields:** verdadero espíritu Trelis,

    **Maria Jose Gonzalez Hernandez:** yo también estoy chambeando.

    **Julian Felipe Rodriguez Barrera:** La camisa por la camiseta. La camiseta por la empresa. La camisa por la camiseta.

    **Maria Jose Gonzalez Hernandez:** Pero que te va lento el computador Charlie,

    **Charlize Caro Mazzilli:** No sé, es que no me abre el coso ese.

    **Trellis Fields:** Comparte, comparte por favor, pero comparte.

    **Charlize Caro Mazzilli:** Pero no te puedo capaz porque está reiniciando.

    **Trellis Fields:** Ah OK, No sabía qué

    **Maria Jose Gonzalez Hernandez:** Nos

    **Trellis Fields:** equipo.

    **Maria Jose Gonzalez Hernandez:** vemos. Nos vemos el domingo. Vamos a Tepinburger de la primera que fuimos,

    **Charlize Caro Mazzilli:** Porque el domingo.

    **Julian Felipe Rodriguez Barrera:** Porque el domingo vamos a recogerlo. Digo, porque el domingo cumplo yo.

    **Maria Jose Gonzalez Hernandez:** dependiendo si es el sábado, sábado. Si es el domingo, domingo porque creo que Luis va a querer que trabajemos el lunes a menos de que salgamos. A menos de que vayamos el lunes y no sé, nos encontremos el lunes y trabajemos por allá el lunes.

    **Julian Felipe Rodriguez Barrera:** Al final se hacen en el.

    **Trellis Fields:** Bueno moche, pero mete presión social para que Luis nos mande la comida por favor. Oye Luis tengo, me dice oye Luis tengo cule pil

    **Maria Jose Gonzalez Hernandez:** Pero tendría que ser un sábado.

    **Trellis Fields:** ni un domingo. No importa, no importa, él lo manda, él lo manda. La

    **Julian Felipe Rodriguez Barrera:** You are my sunshine definitive.

    **Trellis Fields:** vaina es que como empezó el Burger Master, yo no creo que diera una vaina. Burger Master es la jugada porque ya te despachan, ya te van despachando rápido, entonces no creo que esa sea la jugada. Ir a Topping,

    **Julian Felipe Rodriguez Barrera:** Sticker for laptop. Al final el tema del slogan por estética.

    **Trellis Fields:** El dólar está 3.600 y cuando Luis nos pagó estaba en 3.500,

    **Julian Felipe Rodriguez Barrera:** Pero cuando yo no trabajaba. Dólar a 5.000 ¿A cuánto? A 5.000. Dólar a 5. 000 cuando

    **Maria Jose Gonzalez Hernandez:** Cuando estaba en

    **Julian Felipe Rodriguez Barrera:** está en olímpica dólar a

    **Maria Jose Gonzalez Hernandez:** 3.000,

    **Julian Felipe Rodriguez Barrera:** 4.800

    **Maria Jose Gonzalez Hernandez:** 800.000. Estaba como en 4.000 antes.

    **Trellis Fields:** 4.500 el

    **Julian Felipe Rodriguez Barrera:** pero

    **Trellis Fields:** año

    **Julian Felipe Rodriguez Barrera:** empiezan

    **Trellis Fields:** pasado,

    **Julian Felipe Rodriguez Barrera:** a trabajar

    **Trellis Fields:** bueno,

    **Julian Felipe Rodriguez Barrera:** y dólar

    **Trellis Fields:** el año

    **Julian Felipe Rodriguez Barrera:** a

    **Trellis Fields:** antepasado.

    **Julian Felipe Rodriguez Barrera:** 2.000. Increíble. Deflación histórica. Dólar a 1.000 pesos.

    **Maria Jose Gonzalez Hernandez:** Quedan nueve minutos restantes de la reunión.

    **Trellis Fields:** ¿Y cómo vamos? Bueno y no se chambea, entonces le decimos alguien.

    **Maria Jose Gonzalez Hernandez:** Pues bueno, yo puedo esperar aquí, yo voy a cerrar el micrófono mientras sigo trabajando igual si van a. Estamos a espera de Char de Charlie,

    **Trellis Fields:** No se pueda poner vídeos, no me gusta.

    **Julian Felipe Rodriguez Barrera:** Un filósofo dijo una vez, GPT no es tan bueno.

    **Trellis Fields:** Iba a decir una grosería pero estamos

    **Maria Jose Gonzalez Hernandez:** estamos

    **Trellis Fields:** la

    **Maria Jose Gonzalez Hernandez:** modo

    **Trellis Fields:** fiscalía

    **Maria Jose Gonzalez Hernandez:** familia.

    **Trellis Fields:** aquí metida,

    **Julian Felipe Rodriguez Barrera:** Tienes que decir repámpano

    **Trellis Fields:** la fiscalía.

    **Julian Felipe Rodriguez Barrera:** a la fiscalía.

    **Trellis Fields:** Llama a la fiscalía.

    **Julian Felipe Rodriguez Barrera:** Estoy diciendo algo preguntando por chape de ella. Uy,

    **Charlize Caro Mazzilli:** Y si te apura,

    **Julian Felipe Rodriguez Barrera:** tengo que decirle ahora que no vaya con lo por temas estéticos. Entonces le pasaré stick al final.

    **Charlize Caro Mazzilli:** Ustedes saben que ahora se puede poner en Meet Spotify,

    **Trellis Fields:** De verdad vamos.

    **Charlize Caro Mazzilli:** o sea, podríamos estar escuchando música. Dale,

    **Trellis Fields:** ¿Por cierto Charlie, terminé lo de las métricas y pero solo de meta Instagram de los dos no alcancé a hacerlo de TikTok porque o sea no sé cómo hacerlo bueno es que no sepa cómo hacerlo, es que no me ha dado el output que yo quiero y Luis como que cogió rabia y me dijo ya no hagas nada de TikTok pero ya por lo menos torre el trabajo de meta Instagram entonces para que sepas

    **Charlize Caro Mazzilli:** OK, mándamelo para ver,

    **Trellis Fields:** pero que ejecuté porque lo ejecuté hace como una semana entonces no sé qué tanta información haya recopilado o no sé si quieres que lo ejecute a final de mes o un día antes que se acabe el mes tú lo mires para ver si te sirve o si hay que

    **Charlize Caro Mazzilli:** O

    **Trellis Fields:** ajustar

    **Charlize Caro Mazzilli:** sea

    **Trellis Fields:** algo

    **Charlize Caro Mazzilli:** mensual, pero mándamelo para ver cómo es que te da el output.

    **Trellis Fields:** lo da Maluquito, debe estar por alguno de alguna parte en los

    **Charlize Caro Mazzilli:** Eso

    **Trellis Fields:** archivos

    **Charlize Caro Mazzilli:** lo hiciste con Clau,

    **Julian Felipe Rodriguez Barrera:** Wow, wow, wow, wow, wow.

    **Trellis Fields:** tú también lo puedes buscar porque yo

    **Charlize Caro Mazzilli:** pero

    **Trellis Fields:** monté

    **Charlize Caro Mazzilli:** te da

    **Trellis Fields:** como

    **Charlize Caro Mazzilli:** la

    **Trellis Fields:** tanto

    **Charlize Caro Mazzilli:** información o.

    **Trellis Fields:** Sí,

    **Julian Felipe Rodriguez Barrera:** It's

    **Trellis Fields:** sí

    **Julian Felipe Rodriguez Barrera:** the

    **Trellis Fields:** me da

    **Julian Felipe Rodriguez Barrera:** first.

    **Trellis Fields:** la información pero obviamente no me lo da como no bonita obviamente pero ya te digo exactamente

    **Charlize Caro Mazzilli:** ¿Pero a qué te refieres con bonito?

    **Trellis Fields:** las tablas la verdad así como maluquitas ya te más

    **Charlize Caro Mazzilli:** Porque lo que mandó Moche nos dijo y lo viste, como que toma esa información y la convierte en diapositivas. Entonces por el lado estético no importa, importa información.

    **Trellis Fields:** Pues sí, pues sí mira lo te voy a compartir, te lo mando, te comparto pantalla

    **Charlize Caro Mazzilli:** Como quieras.

    **Trellis Fields:** te lo va a mandar quiero leer? ¿Por Clickoff se puede mandar eso creo que Clickoff no deja mandar cosas raras no?

    **Maria Jose Gonzalez Hernandez:** Bueno, ¿En qué quedaron? ¿Se pudo avanzar algo?

    **Trellis Fields:** Cómo

    **Maria Jose Gonzalez Hernandez:** ¿En qué quedaron ¿Se pudo avanzar algo?

    **Trellis Fields:** no sé Charlie como antes pero no coge rabia.

    **Maria Jose Gonzalez Hernandez:** Super chill.

    **Trellis Fields:** Me tiró estos dos output tú me dirás si te sirven o si no te sirven o sé que ajustar algo

    **Maria Jose Gonzalez Hernandez:** No estás transmitiendo.

    **Trellis Fields:** no se lo comparte Charlie,

    **Maria Jose Gonzalez Hernandez:** OK,

    **Trellis Fields:** o sea es lo de las métricas que ella utiliza todos los meses para hacer cositas y con eso puedes usar lo del Cloud s Design que Luis se siente orgulloso de ustedes le montas los CSV y él te puede crear el, o sea, o sea lo monta todos los CSV que tú me dijiste que tú coges como que toda la información de las métricas de todas las redes sociales de las marcas le pones un prompt así como de contexto y tú después de eso haces como unas diapositivas no, o estoy loco o no me acuerdo, no me acuerdo eso lo hablamos hace como un mes Bueno entonces para hacer las diapositivas para no hacer dos procesos distintos que tú primero sacas un PDF y después de eso me imagino que son las diapositivas, en vez de hacer eso, digo yo que puedes pegar todos los CSV o toda la información como tal de las métricas, le metes el prompt y lo haces en Cloud Design. ¿Que estaba diciendo U para que te cree las diapositivas así como un reporte, pero hoy día? Wow, qué bonito, o no sé si solo a usted le sirve a ustedes, pero no sé, el punto es que para que utilicen lo que paga Luis,

    **Charlize Caro Mazzilli:** Okay,

    **Trellis Fields:** pero igual vamos a ver. ¿Ya, OK, abre curso, pero no llores, tranquila, tranquila, tranquilidad, OK? Tranquilidad.

    **Maria Jose Gonzalez Hernandez:** ya Charles ha pasado por todas las emociones.

    **Trellis Fields:** Dios sabe cómo hacer sus cosas tranquilas, Por favor. ¿Lo tienes conectado el computador?

    **Charlize Caro Mazzilli:** Como así

    **Trellis Fields:** ¿Tienes conectado el enchufe?

    **Charlize Caro Mazzilli:** es de mesa.

    **Julian Felipe Rodriguez Barrera:** Hey pordas.

    **Trellis Fields:** Bien, Por favor. Ya, pero no le des varias veces que lo sobresaturas, lo sobreestimulas. Espera que se calme

    **Julian Felipe Rodriguez Barrera:** Lo sobreestimula

    **Trellis Fields:** como el niñito.

    **Julian Felipe Rodriguez Barrera:** un niñito heladito con TDAH. Con TDAH con exceso de dopamina.

    **Trellis Fields:** La real, bro, la real.

    **Julian Felipe Rodriguez Barrera:** Por supuesto que lo conozco, yo soy él. Oigan, estuve haciendo un prompt para pedirle a Chagpt que nos dé prompts. Para pedirle a Higgsfield que nos haga imágenes. Que nos haga imágenes en los carruseles. Imágenes de fondo, backgrounds para los carruseles. Solamente tenemos que pasar la información que mucho nos pone como en el ClickUp. Es decir, slide 1 tiene que tener este texto, slide 2 este texto, slide 3 este lo puse en promes reutilizables. De pronto decir

    **Trellis Fields:** Dios mío.

    **Julian Felipe Rodriguez Barrera:** Arial C.

    **Maria Jose Gonzalez Hernandez:** OK, gracias. Deberías colocar eso en ClickUp

    **Julian Felipe Rodriguez Barrera:** Si, eso iba a decir. ¿En qué parte lo anuncio?

    **Maria Jose Gonzalez Hernandez:** en la parte de creadores.

    **Trellis Fields:** Charlie, abre Task Manager, a ver cómo está tu situación. Ahí está mi historia de tareas. A ver, Tranquilízate, tranquilízate, tranquilízate. Está pensando. Ya, ya, ya. Vamos a ver qué está pasando. Mira, cursor no se ha abierto, Dale doble clic a cursor otra vez. Bueno, ya, cierra, cierre el administrador de tarea. No quiero saber más. Nada de perder la calma, tranquilicémonos. O. OK, OK.

    **Charlize Caro Mazzilli:** Yeah.

    **Trellis Fields:** No me acuerdo ni por qué parte iba ahora el cloud. Ah, ya, sí, sí me acordé. ¿Cómo está muchacho?

    **Julian Felipe Rodriguez Barrera:** ¿Yo? Usted Las veo muy bien. Yo. Usted Los veo ocupados. Todo apunte aquí ya está realizado.

    **Trellis Fields:** Muchachos, una pregunta. ¿Ustedes como cuánto, cuánto tiempo trabajan exactamente?

    **Julian Felipe Rodriguez Barrera:** ¿No quiere saberlo?

    **Charlize Caro Mazzilli:** Cinco lunes a sábado

    **Julian Felipe Rodriguez Barrera:** Yo trabajo el día.

    **Trellis Fields:** No lo que deberían trabajar, sino que trabajan realmente

    **Julian Felipe Rodriguez Barrera:** Bueno, yo empiezo. Yo empiezo

    **Charlize Caro Mazzilli:** Ya.

    **Julian Felipe Rodriguez Barrera:** a las 9 de la mañana y literal acabo hasta que ya acabo como a las 6 intento. Pues no se irá. Así hubiese sido como hasta las 8. Se puede decir que trabajo. 10. 11.

    **Trellis Fields:** 20 horas.

    **Julian Felipe Rodriguez Barrera:** 12\. 1. 2. 3. 7.

    **Trellis Fields:** Y copia eso todo, todo. That's a lot.

    **Charlize Caro Mazzilli:** Este lo pego así sin más.

    **Trellis Fields:** Pero copia todo y pégalo. Exacto, todo, todo, hasta el mensaje dale pura al repo, no lo copiaste, Te preocupes, los bros lo cometemos cualquiera. Ya, Bueno muchachos, ya podemos pasar al paso 2. ¿Cómo se sienten?

    **Maria Jose Gonzalez Hernandez:** Bien, bien.

    **Trellis Fields:** No, ya no quiero demorar mucho responder Ya no me dieron la monda. Ay, qué bueno. Discúlpame. Family friendly. Qué vergüenza, qué vergüenza mentir. No me acuerdo que iba a ser. ¿Y ahora

    **Maria Jose Gonzalez Hernandez:** El paso

    **Trellis Fields:** que se hacía?

    **Maria Jose Gonzalez Hernandez:** 2.

    **Trellis Fields:** Ah, ya, bueno, ahora la terminal más una pequeña pul. La terminal. ¿Cómo se abre la terminal? Eso, eso, pero deje y carga, deje y carga. Tranquila, tú tienes afán, yo no tengo afán.

    **Charlize Caro Mazzilli:** ¿Josie and what?

    **Maria Jose Gonzalez Hernandez:** Tenemos otras cosas que terminar.

    **Trellis Fields:** Esos

    **Julian Felipe Rodriguez Barrera:** Terminal.

    **Trellis Fields:** son detalles. Ahora no trae terminar.

    **Maria Jose Gonzalez Hernandez:** Otra

    **Trellis Fields:** Yes, escribe cloud. No, no, así no, no, no escribe Cloud, o sea, tiene que haber una terminal.

    **Maria Jose Gonzalez Hernandez:** Tenemos.

    **Trellis Fields:** Está compartiendo.

    **Charlize Caro Mazzilli:** Yo no ve

    **Trellis Fields:** Ah, OK. Pensé que era bueno, pero Espérate, tú vas a terminar, ¿Verdad? A la derecha

    **Charlize Caro Mazzilli:** cómo así.

    **Trellis Fields:** arriba y ahora es una terminal. Pero eso no es una terminal,

    **Charlize Caro Mazzilli:** Ya la abrí,

    **Trellis Fields:** no has abierto nada. Si, te estoy viendo

    **Charlize Caro Mazzilli:** mira.

    **Trellis Fields:** y no, ¿Quién estaba viendo entonces

    **Maria Jose Gonzalez Hernandez:** A mí seguramente

    **Trellis Fields:** de pronto no? Bueno, no sé, el que esté ahí, el que estoy viendo no ha abierto la terminal. Qué vergüenza. Disculpa,

    **Maria Jose Gonzalez Hernandez:** aquí

    **Trellis Fields:** escribe Claudia.

    **Maria Jose Gonzalez Hernandez:** Cloud Enter.

    **Trellis Fields:** ¿Sí, Julián, tú también estás dándole eso?

    **Julian Felipe Rodriguez Barrera:** Yes.

    **Trellis Fields:** Escriban slash remotion.

    **Maria Jose Gonzalez Hernandez:** I see,

    **Julian Felipe Rodriguez Barrera:** ¿Remotion o Remote?

    **Trellis Fields:** Bueno, cierren otra vez cursor y vuelven

    **Charlize Caro Mazzilli:** ¿Remote

    **Trellis Fields:** a abrir

    **Charlize Caro Mazzilli:** o no remote?

    **Trellis Fields:** remotion, pero no les sale, entonces cierren cursor y vuelvan a abrir. Muchachos, por favor, si son tan amables.

    **Julian Felipe Rodriguez Barrera:** Muy obrigado.

    **Trellis Fields:** ¿No se les ha actualizado, entonces no sé por qué te salió eso?

    **Charlize Caro Mazzilli:** A mí me sale que Update available.

    **Trellis Fields:** A ver, eso es de curso, eso no importa.

    **Charlize Caro Mazzilli:** No se puede ver.

    **Trellis Fields:** A ver. No, ¿Qué estás haciendo? Disculpa, dejen mirar para cuál pantalla estoy viendo.

    **Charlize Caro Mazzilli:** Yo tengo la pantallita verde al lado izquierdo.

    **Trellis Fields:** OK, entonces eres tú. ¿Ya cerraste curso, lo volviste a abrir?

    **Charlize Caro Mazzilli:** ¿No?

    **Trellis Fields:** Bueno, ahí está. Importante detalle. Slash remotion, a ver si te sale ahora no te sale,

    **Julian Felipe Rodriguez Barrera:** No me sale algo que diga remotion, solo remote.

    **Trellis Fields:** entonces vuelvan y apliquen esta. Se van a terminar o se abren una nueva terminal y ponen otra vez npx create video. Charlie, cierra la pestaña de clon. Eso es lo que se queda cargando infinitamente. Da la blank.

    **Julian Felipe Rodriguez Barrera:** Okay. Choose a template.

    **Charlize Caro Mazzilli:** Cloud.

    **Trellis Fields:** Espérate allí alrededor. A new project will be great. ¿Por qué no le sale remotion? No, dale escape. No es fuc, No les.

    **Charlize Caro Mazzilli:** A mí mira si me sale.

    **Trellis Fields:** No, no te sale porque mochi tampoco le sale. Pero ya les doy el comando para recargar entonces. Dios mío, padre,

    **Maria Jose Gonzalez Hernandez:** Pero cálmate.

    **Trellis Fields:** No me dio nada. Ya no me dieron. Vamos a ver cómo

_Resumen recortado por tamaño. Completo en ClickUp: https://app.clickup.com/9017418223/v/dc/8cqnrff-15097/8cqnrff-17097._

_Sincronizado por Brain: 2026-10-15T17:20:46.138Z_
