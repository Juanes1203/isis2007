# CampusFlow — Product Brief

Versión: 0.4 · Revisado: 2026-08-24 · Dueño: equipo del curso
Estado: v0 en construcción · Repo: `campusflow-api`

## 1. El problema

La información académica de un estudiante de pregrado vive en cinco lugares que no se
hablan entre sí:

- el syllabus en PDF que el profesor sube la primera semana,
- las fechas que alguien copia (a veces mal) a Brightspace o Canvas,
- las entregas que se acuerdan en el chat del grupo,
- el reglamento académico, publicado en la web de la universidad,
- los avisos por correo que llegan a las 11 de la noche.

El estudiante no tiene **una sola vista** de "qué debo entregar y cuándo".
El costo no es la falta de información: es el costo de reunirla otra vez, cada vez.

## 2. Evidencia

- **E-01.** 12 entrevistas con estudiantes de 4º a 7º semestre (agosto 2026).
  9 de 12 entregaron tarde al menos una vez por no ver un cambio de fecha.
- **E-02.** Camilo, monitor de Estructuras de Datos, registró 40+ preguntas repetidas
  en un semestre sobre políticas del syllabus: porcentajes, política de retardo, formato.
- **E-03.** Revisión de 6 syllabus reales del semestre pasado: los 6 traen las fechas en
  tablas con formatos distintos y 4 de 6 cambiaron al menos una fecha durante el semestre.

## 3. Supuestos — SON SUPUESTOS DE CLASE, NO DATOS VALIDADOS

Están marcados a propósito. Ninguno está probado. Si uno cae, el producto cambia.

- **S-01.** El estudiante sube el PDF del syllabus una vez por materia sin quejarse.
- **S-02.** Un syllabus con tabla de fechas permite extraer al menos el 80% de las entregas.
- **S-03.** El estudiante confía en una agenda automática **si puede ver de dónde salió cada fecha**.
- **S-04.** El profesor no bloquea el uso del material dentro del curso.
- **S-05.** El valor está en la agenda unificada. El chat sobre documentos es el gancho de entrada.

Si S-02 cae, CampusFlow se convierte en un formulario manual y pierde la mayor parte
de su razón de existir. Es el supuesto que hay que atacar primero.

## 4. Usuarios objetivo

- **Ana**, 5º semestre, 6 materias, coordina 3 proyectos grupales. Usuario primario.
- **Camilo**, monitor de curso. Usuario secundario: gana tiempo, no pierde control.
- **Profesora Restrepo**, titular. No es usuaria diaria; es quien autoriza y quien
  quiere que el reglamento y el syllabus "se respondan solos".

Detalle en `personas.md`.

## 5. Propuesta de valor en una frase

Una sola agenda de entregas construida a partir de los documentos reales del curso,
que además responde en lenguaje natural con la cita exacta del documento de donde salió.

## 6. Alcance v0

1. **Importar syllabus en PDF** y extraer entregas con fecha, con revisión del estudiante.
2. **Agenda unificada** de entregas por estudiante, ordenada por urgencia real.
3. **Preguntas en lenguaje natural** sobre los documentos del curso, con citas (RAG).
4. **Recordatorios**: especificados y modelados en base de datos, **sin implementar** en v0.

## 7. Explícitamente FUERA de alcance v0

- App móvil nativa (iOS/Android).
- Integración con el LMS (Brightspace/Canvas) por API o scraping.
- Notificaciones push.
- Chat grupal, comentarios, colaboración entre estudiantes.
- Calificaciones, notas parciales, proyección de nota final.
- Multi-universidad, multi-idioma, multi-tenant.

Si una conversación propone algo de esta lista, la respuesta correcta es "fuera de v0",
no "buena idea, agrégalo".

## 8. Métricas de éxito (umbrales, no deseos)

- **M-01 Extracción.** Sobre un set de 10 syllabus etiquetados a mano:
  recall ≥ 0.80 y precisión ≥ 0.90 en entregas con fecha.
- **M-02 Rendimiento.** p95 de `GET /me/agenda` ≤ 300 ms con 6 materias y 60 entregas.
- **M-03 Confianza.** ≥ 90% de las respuestas de `/ask` incluyen al menos una cita
  a un chunk existente; 0 citas inventadas en la muestra de revisión semanal.
- **M-04 Uso.** ≥ 60% de los estudiantes activos abren la agenda 3 o más veces por semana
  entre la semana 5 y la 12 del semestre.
- **M-05 Resultado.** Entregas tardías autoreportadas por estudiante por semestre:
  de 1.8 (línea base de E-01) a menos de 1.0.

## 9. Riesgos

- **R-01.** Syllabus escaneados o con tablas raras rompen la extracción. Mitigación: revisión
  humana obligatoria antes de guardar las entregas.
- **R-02.** Alucinación en `/ask`. Mitigación: respuesta sin cita se rechaza y se responde
  "no está en los documentos del curso".
- **R-03.** Zonas horarias. Una entrega que vence hoy a las 23:59 se muestra como vencida.
  Ya ocurrió: es el bug abierto de `days_left`. Mitigación: todo en UTC, ver ADR-04.
- **R-04.** Datos académicos personales. Un bug de autorización expone la agenda de otro.
- **R-05.** Derechos sobre el material del profesor. No se comparte fuera del curso.
- **R-06.** Si el LMS abre una API decente, el caso de uso principal se reduce.

## 10. Preguntas abiertas (sin resolver)

- **Q-01.** ¿El documento subido pertenece al estudiante o al curso? Si es del curso,
  200 estudiantes no deberían subir 200 copias del mismo PDF.
- **Q-02.** Cuando el profesor cambia una fecha, ¿re-ingesta completa o edición manual
  del deliverable? ¿Qué gana si hay conflicto?
- **Q-03.** ¿Se muestra el vencimiento en la zona horaria del curso o en la del usuario?
  Hoy asumimos `America/Bogota` para todos, y es una decisión que va a doler.
- **Q-04.** Recordatorios: ¿correo, in-app o ambos? La tabla existe; el canal no está decidido.
- **Q-05.** ¿Qué hacemos con las entregas sin hora, solo con fecha? Hoy asumimos 23:59.
