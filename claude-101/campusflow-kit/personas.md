# CampusFlow — Personas

Tres personas reales, no arquetipos de catálogo. Cada una viene de entrevistas de agosto 2026.
Si una user story no se puede atribuir a una de las tres, sobra.

---

## Ana Ramírez — estudiante, 5º semestre

**Contexto.** 20 años, Ingeniería de Sistemas. 6 materias este semestre: Estructuras de Datos,
Bases de Datos, Probabilidad, Sistemas Operativos, Ética Profesional y un electiva de diseño.
Coordina 3 proyectos grupales (13 personas en total entre los tres). Trabaja 8 horas semanales
como asistente de laboratorio. Vive en el celular: el computador lo abre para programar y para
entregar, nada más.

**Un día típico.** 6:40 a.m. revisa WhatsApp en el bus: 4 grupos con 60 mensajes sin leer, dos de
ellos con un cambio de fecha enterrado entre memes. En clase anota fechas en Notas del iPhone.
Al mediodía abre Brightspace para confirmar una entrega y la fecha que ve no coincide con la del
syllabus. A las 10 p.m. arma una lista en papel de lo que debe entregar esta semana. La lista dura
tres días antes de quedar desactualizada.

**Dolores.**
- Se entera tarde de las entregas, sobre todo de las que cambian de fecha.
- No sabe qué semana va a ser pesada hasta que ya está encima.
- Reconstruye la misma lista de entregas tres veces por semana, a mano.
- Cuando pregunta en el grupo, recibe tres respuestas distintas y ninguna con fuente.

**Qué intenta hoy.** Notas del iPhone + recordatorios manuales + un Google Calendar que dejó
de actualizar en la semana 4 + preguntar en el grupo + revisar Brightspace "por si acaso".

**Qué la haría abandonar el producto.** Que la agenda le muestre una fecha equivocada una sola vez.
Si entrega tarde confiando en CampusFlow, no vuelve. También la pierde cualquier flujo que le
exija abrir el computador o llenar un formulario por cada entrega.

> "Yo no necesito que me organice la vida. Necesito abrir una pantalla y saber qué se vence esta
> semana, sin tener que confirmar en tres lados si la fecha es de verdad."

---

## Camilo Duarte — monitor de curso, 8º semestre

**Contexto.** 23 años. Monitor de Estructuras de Datos, 180 estudiantes matriculados. Le pagan por
10 horas semanales: atender el foro, calificar tres talleres y correr la sesión de dudas del jueves.
Está haciendo su proyecto de grado en paralelo y quiere que la monitoría le cueste menos.

**Un día típico.** Abre el foro del curso y encuentra 14 preguntas nuevas. 9 son la misma pregunta
reformulada: si el taller se entrega en `.zip` o en repositorio, cuánto pesa el parcial, qué pasa si
entrega un día tarde. Copia y pega respuestas viejas. El jueves en la sesión de dudas vuelven a
preguntar lo mismo en voz alta. Escribe un mensaje fijado que nadie lee.

**Dolores.**
- Responde 40 veces por semestre la misma pregunta sobre el syllabus.
- Las respuestas que da quedan enterradas en el foro y no las encuentra ni él.
- Cuando la profesora cambia una política, sus respuestas viejas quedan mal y él no se entera.

**Qué intenta hoy.** Un documento de "preguntas frecuentes" en Drive que actualiza dos veces por
semestre, mensajes fijados en el foro, y responder con capturas de pantalla del PDF del syllabus.

**Qué lo haría abandonar el producto.** Que el asistente responda mal sobre una política de
calificación. Una respuesta inventada sobre el porcentaje del parcial le cuesta a él, no al modelo.
También lo pierde si mantener el contenido le toma más tiempo del que le ahorra.

> "Si el bot se inventa que el taller vale 20% cuando vale 15%, el que da la cara en la sesión del
> jueves soy yo. Prefiero que diga 'no sé' a que suene seguro."

---

## Profesora Luisa Restrepo — titular del curso

**Contexto.** 44 años. Dicta dos secciones de Estructuras de Datos (180 y 90 estudiantes) y una
electiva de posgrado. Investiga, dirige tesis y coordina el área. Su tiempo con el curso es
finito y ya está asignado.

**Un día típico.** Entre clase y clase revisa correo: 6 mensajes de estudiantes preguntando cosas
que están en el syllabus, 2 pidiendo prórroga, 1 con una duda real. Corrige la fecha de un taller
en Brightspace pero no en el PDF del syllabus, y sabe que eso va a generar 20 preguntas.

**Dolores.**
- Contesta por correo lo que ya está escrito en el syllabus y en el reglamento.
- Cada cambio de fecha genera una ola de confusión que dura una semana.
- No tiene forma de saber qué se está entendiendo mal hasta que llega el reclamo.

**Qué intenta hoy.** Un syllabus muy detallado (14 páginas), anuncios en Brightspace, y repetir las
políticas en voz alta la primera clase y antes de cada parcial.

**Qué la haría abandonar el producto.** Que el material de su curso salga del curso, o que el
asistente le atribuya a ella una política que no escribió. También que subir un documento le tome
más de dos minutos.

> "Yo escribí el syllabus una vez. No debería tener que explicarlo 180 veces, ni que alguien
> me ponga en la boca reglas que no puse."

---

## Lo que estas tres personas implican para el producto

- Ana exige **exactitud de fechas** por encima de features. De ahí M-01 y M-05.
- Camilo exige **citas verificables**. De ahí la regla: sin cita, no hay respuesta.
- Restrepo exige **control del material y esfuerzo mínimo de carga**. De ahí la ingesta en un paso.
