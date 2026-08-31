# CampusFlow — Requisitos v0

Alcance: MVP v0 del repo `campusflow-api`. Todo lo que no esté aquí no se implementa.
Prioridad MoSCoW: Must = entra en v0; Should = entra si sobra tiempo; Could = backlog;
Won't = decisión tomada de NO hacerlo en v0.

---

## 1. Requisitos funcionales

### Autenticación y usuarios

- **RF-01 (Must).** El sistema permite registrar un usuario con correo institucional y contraseña.
- **RF-02 (Must).** El sistema emite un JWT con expiración de 24 h en el login.
- **RF-03 (Must).** Todo endpoint que no sea `/auth/*` ni `/health` exige un JWT válido.
- **RF-04 (Should).** El usuario puede cambiar su contraseña autenticado.
- **RF-05 (Won't).** OAuth institucional, SSO, recuperación de contraseña por correo.

### Cursos e inscripciones

- **RF-06 (Must).** El usuario puede crear un curso con código, nombre, semestre y zona horaria.
- **RF-07 (Must).** El usuario puede inscribirse a un curso con rol `student`, `monitor` o `professor`.
- **RF-08 (Must).** El usuario solo ve cursos en los que está inscrito.
- **RF-09 (Could).** Un monitor puede invitar estudiantes a un curso por código.

### Documentos e ingesta

- **RF-10 (Must).** El usuario sube un PDF (syllabus, reglamento, guía) asociado a un curso.
- **RF-11 (Must).** El sistema extrae el texto del PDF, lo divide en chunks y genera embeddings.
- **RF-12 (Must).** El sistema propone entregas con fecha detectadas en el syllabus.
- **RF-13 (Must).** Las entregas propuestas requieren confirmación del usuario antes de guardarse.
- **RF-14 (Should).** El sistema reporta el estado de ingesta: `pending`, `processing`, `ready`, `failed`.
- **RF-15 (Won't).** OCR de documentos escaneados. Un PDF sin capa de texto se rechaza con mensaje claro.

### Entregas y agenda

- **RF-16 (Must).** El usuario puede crear, editar y eliminar entregas de un curso en el que está inscrito.
- **RF-17 (Must).** `GET /me/agenda` devuelve las entregas de todos los cursos del usuario,
  ordenadas por fecha de vencimiento ascendente.
- **RF-18 (Must).** Cada entrega en la agenda incluye `days_left`, calculado en UTC.
- **RF-19 (Must).** Una entrega cuyo vencimiento aún no ha pasado NUNCA se marca como vencida.
- **RF-20 (Should).** `GET /courses/{course_id}/workload` devuelve la carga de la semana:
  número de entregas y horas estimadas por materia.
- **RF-21 (Could).** Filtro de agenda por rango de fechas y por curso.

### Preguntas sobre documentos (RAG)

- **RF-22 (Must).** `POST /courses/{course_id}/ask` responde una pregunta en lenguaje natural
  usando únicamente los documentos de ese curso.
- **RF-23 (Must).** Toda respuesta incluye las citas: `document_id`, página y fragmento del chunk usado.
- **RF-24 (Must).** Si el retrieval no supera el umbral de similitud, el sistema responde
  "no está en los documentos del curso" en vez de improvisar.
- **RF-25 (Won't).** Preguntas que crucen documentos de cursos en los que el usuario no está inscrito.

### Recordatorios

- **RF-26 (Must).** El modelo de datos soporta recordatorios (`reminders`) con canal y offset.
- **RF-27 (Won't).** El envío real de recordatorios (correo, push) en v0. Solo se especifica y se modela.

---

## 2. Requisitos no funcionales

### Rendimiento
- **RNF-01.** p95 de `GET /me/agenda` ≤ 300 ms con 6 cursos y 60 entregas, sin caché.
- **RNF-02.** p95 de `POST /courses/{id}/ask` ≤ 3 s de extremo a extremo, incluyendo embedding
  de la pregunta, retrieval y generación.
- **RNF-03.** Ingesta de un PDF de 15 páginas: ≤ 30 s hasta estado `ready`.
- **RNF-04.** El retrieval sobre 5.000 chunks de un curso devuelve top-8 en ≤ 120 ms.

### Seguridad
- **RNF-05.** Contraseñas con `bcrypt`, cost factor 12. Nunca en logs.
- **RNF-06.** JWT firmado con HS256, secreto desde variable de entorno, expiración 24 h.
- **RNF-07.** Toda consulta a base de datos usa parámetros. Cero SQL construido por concatenación.
- **RNF-08.** Autorización por recurso: cada endpoint verifica que el usuario esté inscrito
  en el curso antes de leer o escribir. No basta con estar autenticado.

### Privacidad de datos académicos
- **RNF-09.** Los documentos de un curso solo son legibles por usuarios inscritos en ese curso.
- **RNF-10.** Los logs no contienen texto de documentos, contenido de preguntas ni correos completos.
- **RNF-11.** Borrar un usuario borra sus enrollments, sus reminders y sus documentos propios
  (`ON DELETE CASCADE`), y deja los cursos intactos.
- **RNF-12.** No se envían datos personales al proveedor de embeddings: se envía texto del documento,
  nunca nombre, correo ni identificador del estudiante.

### Disponibilidad y operación
- **RNF-13.** Objetivo 99% mensual en horario de clase (6 a.m.–11 p.m. `America/Bogota`).
- **RNF-14.** `GET /health` responde en menos de 50 ms y verifica conexión a Postgres.
- **RNF-15.** Toda fecha se persiste en `timestamptz` en UTC. La conversión a zona local
  ocurre solo en la capa de presentación.

---

## 3. User stories del MVP con criterios de aceptación

### US-01 — Ver la agenda unificada

**Como** Ana, estudiante con 6 materias,
**quiero** ver todas mis entregas en una sola lista ordenada por urgencia,
**para** no tener que reconstruirla a mano cada semana.

```gherkin
Funcionalidad: Agenda unificada

  Escenario: Estudiante con entregas en varios cursos
    Dado que soy un usuario autenticado inscrito en 3 cursos
    Y que existen 7 entregas futuras repartidas entre esos cursos
    Cuando hago GET /me/agenda
    Entonces recibo 200
    Y la respuesta contiene 7 entregas
    Y las entregas vienen ordenadas por due_at ascendente
    Y cada entrega incluye course_code, title, due_at y days_left

  Escenario: Estudiante sin entregas
    Dado que soy un usuario autenticado sin cursos inscritos
    Cuando hago GET /me/agenda
    Entonces recibo 200
    Y la respuesta es una lista vacía
```

### US-02 — Una entrega que vence hoy a las 23:59 no está vencida

**Como** Ana,
**quiero** que una entrega que vence hoy a las 11:59 p.m. aparezca como pendiente y de primera,
**para** no asumir que ya la perdí cuando todavía tengo horas.

Este es el escenario que hoy falla. `days_left` mezcla `datetime` naive con instantes en UTC
y aplica `.days` sobre un `timedelta` negativo, así que trunca hacia abajo y devuelve `-1`.

```gherkin
Funcionalidad: Cálculo de días restantes

  Escenario: Entrega que vence hoy a las 23:59 hora de Bogotá
    Dado que la hora actual es 2026-09-15T14:00:00-05:00
    Y que existe una entrega con due_at = 2026-09-16T04:59:00Z
    Cuando hago GET /me/agenda
    Entonces la entrega aparece con days_left igual a 0
    Y la entrega NO está marcada como overdue
    Y la entrega aparece antes que cualquier entrega con due_at posterior

  Escenario: Entrega vencida hace media hora
    Dado que la hora actual es 2026-09-16T05:30:00Z
    Y que existe una entrega con due_at = 2026-09-16T04:59:00Z
    Cuando hago GET /me/agenda
    Entonces la entrega está marcada como overdue
    Y days_left es un número negativo

  Escenario: Lista vacía
    Dado que no tengo entregas
    Cuando calculo la agenda
    Entonces no se lanza ninguna excepción
    Y el resultado es una lista vacía
```

### US-03 — Importar un syllabus y confirmar las entregas

**Como** Ana,
**quiero** subir el PDF del syllabus y revisar las fechas que el sistema detectó,
**para** cargar un semestre completo en minutos sin confiar a ciegas.

```gherkin
Funcionalidad: Ingesta de syllabus

  Escenario: PDF con tabla de fechas
    Dado que estoy inscrita en el curso ISIS1225
    Cuando subo syllabus.pdf a POST /courses/ISIS1225/documents
    Entonces recibo 202 con un document_id y status "processing"
    Y cuando el estado pasa a "ready"
    Entonces GET /documents/{document_id}/proposals devuelve al menos 5 entregas propuestas
    Y ninguna entrega se guardó todavía en deliverables

  Escenario: Confirmación parcial de propuestas
    Dado que tengo 6 propuestas de entregas
    Cuando confirmo 4 de ellas con POST /documents/{document_id}/proposals/confirm
    Entonces se crean exactamente 4 filas en deliverables
    Y las 2 propuestas no confirmadas se descartan

  Escenario: PDF sin capa de texto
    Cuando subo un PDF escaneado
    Entonces recibo 422
    Y el mensaje indica que el documento no tiene texto extraíble
```

### US-04 — Preguntar sobre los documentos del curso

**Como** Camilo, monitor,
**quiero** que el asistente responda preguntas del syllabus citando el documento,
**para** dejar de responder 40 veces lo mismo sin arriesgar una respuesta inventada.

```gherkin
Funcionalidad: Preguntas sobre documentos del curso

  Escenario: Pregunta cubierta por el syllabus
    Dado que el curso ISIS1225 tiene un syllabus indexado
    Cuando hago POST /courses/ISIS1225/ask con "¿cuánto vale el parcial 1?"
    Entonces recibo 200
    Y la respuesta contiene al menos una cita con document_id y página
    Y cada chunk citado existe en la tabla chunks

  Escenario: Pregunta fuera de los documentos
    Cuando hago POST /courses/ISIS1225/ask con "¿quién ganó el mundial de 2022?"
    Entonces la respuesta indica que no está en los documentos del curso
    Y la lista de citas está vacía

  Escenario: Curso ajeno
    Dado que NO estoy inscrito en el curso ISIS2304
    Cuando hago POST /courses/ISIS2304/ask
    Entonces recibo 403
```

### US-05 — Carga académica de la semana

**Como** Ana,
**quiero** ver cuántas entregas y cuántas horas estimadas trae cada materia esta semana,
**para** decidir qué empiezo el lunes.

```gherkin
Funcionalidad: Carga académica semanal

  Escenario: Semana con entregas
    Dado que estoy inscrita en ISIS1225
    Y que hay 3 entregas de ese curso entre lunes y domingo de esta semana
    Cuando hago GET /courses/ISIS1225/workload
    Entonces recibo 200
    Y deliverable_count es 3
    Y estimated_hours es la suma de estimated_hours de esas 3 entregas

  Escenario: Semana sin entregas
    Cuando hago GET /courses/ISIS1225/workload en una semana sin entregas
    Entonces recibo 200
    Y deliverable_count es 0
    Y estimated_hours es 0
```
