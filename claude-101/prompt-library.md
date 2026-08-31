# Prompt Library

Parte IV

## Prompt Library

Veintiséis prompts completos, listos para copiar y pegar, todos anclados en CampusFlow y todos con la misma estructura de siete secciones: la plantilla que el estudiante debe poder escribir de memoria al salir de clase.

Esta biblioteca no es una colección de trucos. Es una sola plantilla aplicada veintiséis veces a siete roles distintos.

Todos los prompts comparten el mismo esqueleto:

ContextoRolObjetivoRestriccionesInputOutput esperadoValidación

La repetición es intencional. Después de leer la misma estructura veintiséis veces, escribirla deja de ser un ejercicio y se vuelve un reflejo.

Cómo se usan

Los marcadores `{{ASI}}` se reemplazan antes de enviar. Cada prompt lleva arriba una línea que dice exactamente qué va en cada marcador. Un prompt con marcadores sin reemplazar produce respuestas genéricas: el modelo rellena el hueco con lo primero que se le ocurre.

Cuidado

La sección **Validación** no es decorativa. Es lo único que convierte una respuesta plausible en una respuesta auditable. Si la borran para ahorrar tokens, están comprando velocidad con confianza.

### Product Manager

El error típico: pedirle al modelo "ideas para una app de estudiantes". El modelo devuelve veinte features y cero problemas.

La plantilla corrige eso obligando a separar el problema de la solución, a nombrar usuarios concretos y a escribir criterios de aceptación falsables antes de hablar de pantallas.

**PM-01** — Reemplaza `{{SEGMENTO}}` (a quién estudias), `{{EVIDENCIA_CRUDA}}` (notas de entrevistas, mensajes del chat del grupo, quejas reales) y `{{NUMERO_DE_PROBLEMAS}}`.

PM-01 · Problem discovery

    # Contexto
    CampusFlow es un asistente académico para estudiantes de pregrado. La información
    académica está dispersa: syllabus en PDF, fechas en Brightspace, entregas en el chat del
    grupo, reglamento en la web, avisos por correo. Nadie tiene una sola vista de "qué debo
    entregar y cuándo". Estoy en discovery: el producto todavía NO está definido.

    # Rol
    Actúa como Product Manager senior de productos de educación, formado en Jobs To Be Done.
    Tu sesgo profesional es desconfiar de las soluciones que llegan antes que el problema.

    # Objetivo
    Extraer de la evidencia cruda los {{NUMERO_DE_PROBLEMAS}} problemas más dolorosos y
    frecuentes del segmento {{SEGMENTO}}, formulados como problemas y no como features.

    # Restricciones
    - Prohibido proponer soluciones, features, pantallas o nombres de producto.
    - Forma de cada problema: quién, qué intenta lograr, qué lo bloquea, con qué frecuencia
      le pasa y qué le cuesta (tiempo, nota, dinero o estrés).
    - Cada problema respaldado por al menos una cita textual de la evidencia.
    - Un problema que aparece una sola vez se marca como señal débil.
    - Español de Colombia, sin adjetivos de marketing.

    # Input
    Segmento: {{SEGMENTO}}
    Evidencia cruda:
    {{EVIDENCIA_CRUDA}}

    # Output esperado
    1. Tabla: ID, enunciado, frecuencia observada, costo para el usuario, fuerza de la
       evidencia (fuerte / débil).
    2. La cita textual que sustenta cada problema.
    3. Un párrafo: qué problema atacarías primero y por qué.

    # Validación
    Antes de la tabla, escribe "Supuestos" con todo lo que asumiste y que la evidencia NO
    dice. Al final, escribe "Lo que no pude determinar" con las preguntas que le harías a un
    usuario real para confirmar o tumbar cada señal débil. No inventes datos para llenar
    huecos.

**PM-02** — Reemplaza `{{NOTAS_DE_ENTREVISTAS}}` y `{{NUMERO_DE_PERSONAS}}`. Si no tienes entrevistas, dilo: son hipótesis.

PM-02 · Personas y Jobs To Be Done

    # Contexto
    Producto: CampusFlow, asistente académico para estudiantes de pregrado. Usuarios
    preliminares: Ana, 5º semestre, 6 materias, coordina 3 proyectos grupales, vive en el
    celular, se entera tarde de las entregas; Camilo, monitor, responde 40 veces la misma
    pregunta del syllabus; profesora Restrepo, quiere que el reglamento se responda solo.

    # Rol
    Actúa como Product Manager que le entrega estas personas a un equipo de ingeniería que
    las va a usar para decidir alcance. No son material de marketing: son insumo técnico.

    # Objetivo
    Construir {{NUMERO_DE_PERSONAS}} personas accionables con su Job To Be Done principal,
    sus alternativas actuales y el criterio por el que abandonarían el producto.

    # Restricciones
    - Nada de demografía decorativa: ni color favorito, ni marca de celular, ni frase épica.
    - Cada persona: contexto en una frase, día típico, herramientas que YA usa, un único
      dolor principal, JTBD en formato "cuando... quiero... para...", y motivo de abandono.
    - Máximo 12 líneas por persona.
    - Marca con [HIPÓTESIS] todo lo que no venga de las notas de entrevista.

    # Input
    Notas de entrevistas o conversaciones reales:
    {{NOTAS_DE_ENTREVISTAS}}

    # Output esperado
    1. Una ficha por persona con los campos anteriores.
    2. Tabla comparativa: persona, JTBD, alternativa actual, motivo de abandono.
    3. Una frase por persona que un ingeniero pueda usar para decir "esto no es para ella".

    # Validación
    Cierra con una auto-revisión: para cada persona señala cuál de sus campos tiene la
    evidencia más débil y qué pregunta de una línea la confirmaría. Si dos personas comparten
    el mismo JTBD, dilo y propón fusionarlas en vez de inflar el número.

**PM-03** — Reemplaza `{{FEATURE}}` con una de las cuatro del MVP, `{{PERSONA}}` con Ana, Camilo o la profesora Restrepo, y `{{RESTRICCIONES_DE_NEGOCIO}}`.

PM-03 · User stories con criterios de aceptación

    # Contexto
    CampusFlow, MVP v0: importar un syllabus en PDF y extraer entregas con fecha; agenda
    unificada de entregas; preguntas en lenguaje natural sobre los documentos del curso;
    recordatorios (solo especificados). Stack: Python 3.12, FastAPI, PostgreSQL 16 +
    pgvector, SQLAlchemy 2.x, Pydantic v2, pytest, Alembic. API-first, sin frontend, JWT.
    Entidades: users, courses, enrollments, deliverables, documents, chunks, reminders.

    # Rol
    Actúa como Product Manager técnico que escribe historias que un backend engineer puede
    implementar sin volver a preguntar y que un QA puede convertir en tests sin interpretar.

    # Objetivo
    Descomponer la feature {{FEATURE}} para la persona {{PERSONA}} en user stories con
    criterios de aceptación verificables.

    # Restricciones
    - Formato: "Como {{PERSONA}}, quiero ... para ...".
    - Cada historia cabe en un sprint de una persona; si no cabe, pártela.
    - Criterios en Gherkin (Dado / Cuando / Entonces), mínimo tres por historia, y al menos
      uno de camino infeliz. Cada criterio menciona el endpoint o la entidad afectada.
    - Prohibidos los criterios no verificables ("la experiencia debe ser fluida").
    - Cada historia declara explícitamente qué queda fuera de su alcance.

    # Input
    Feature: {{FEATURE}}
    Persona: {{PERSONA}}
    Restricciones de negocio: {{RESTRICCIONES_DE_NEGOCIO}}

    # Output esperado
    1. Historias con ID (CF-XX), narrativa, estimación relativa (S/M/L) y dependencias.
    2. Criterios de aceptación en Gherkin por historia.
    3. Sección "Fuera de alcance" por historia.

    # Validación
    Recorre tus propios criterios y responde en una tabla: ¿cada uno es observable desde la
    API sin mirar la base de datos? Marca los que no lo son y reescríbelos. Después lista las
    decisiones de producto que asumiste porque el input no las especificaba.

**PM-04** — Reemplaza `{{LISTA_DE_FEATURES}}`, `{{TAMANO_DEL_EQUIPO}}`, `{{FECHA_LIMITE}}` y `{{HIPOTESIS}}`.

PM-04 · Definición de MVP y recorte de alcance

    # Contexto
    CampusFlow debe salir a un piloto real con un curso de la universidad. Alcance v0
    declarado: importar syllabus en PDF, agenda unificada, preguntas en lenguaje natural
    sobre documentos del curso, recordatorios especificados. Fuera de v0: app móvil nativa,
    integración con el LMS, notificaciones push, chat grupal. Stack fijo, sin frontend.

    # Rol
    Actúa como Product Manager responsable de que el piloto salga a tiempo. Tu trabajo hoy no
    es agregar valor: es quitar alcance sin matar la hipótesis del producto.

    # Objetivo
    Recortar {{LISTA_DE_FEATURES}} al conjunto mínimo que permita aprender si CampusFlow le
    sirve a Ana, con {{TAMANO_DEL_EQUIPO}} personas y fecha límite {{FECHA_LIMITE}}.

    # Restricciones
    - El MVP debe permitir medir una hipótesis, no solo "funcionar".
    - Toda feature que sobrevive lleva una métrica asociada.
    - Toda feature cortada lleva escrito qué se pierde y qué se aprende igual sin ella.
    - No inventes capacidad de equipo ni velocidad histórica: si no te la doy, pídela.
    - Máximo 5 features dentro del MVP.

    # Input
    Features candidatas: {{LISTA_DE_FEATURES}}
    Equipo: {{TAMANO_DEL_EQUIPO}} · Fecha límite: {{FECHA_LIMITE}}
    Hipótesis principal a validar: {{HIPOTESIS}}

    # Output esperado
    1. Tabla: feature, dentro/fuera, razón en una línea, métrica si entra.
    2. Definición del MVP en un párrafo que quepa en un mensaje de Slack.
    3. Lista "v0.1 candidatas" con lo cortado, ordenada por costo de oportunidad.
    4. Los tres riesgos que introduce este recorte.

    # Validación
    Termina con un ejercicio de refutación: describe el escenario en que este MVP sale a
    tiempo, la gente lo usa y aun así NO aprendimos nada sobre la hipótesis. Si ese escenario
    es plausible, propón el cambio mínimo de alcance que lo elimina.

**PM-05** — Reemplaza `{{BACKLOG}}`, `{{CRITERIO_DE_NEGOCIO}}` (retención en el piloto, soporte ahorrado a Camilo) y `{{DATOS}}`.

PM-05 · Priorización con trade-offs explícitos

    # Contexto
    CampusFlow ya tiene el MVP v0 corriendo con un curso piloto. Entidades: users, courses,
    enrollments, deliverables, documents, chunks, reminders. Deuda técnica conocida: la
    lógica de "días restantes" está duplicada en services/deadlines.py y api/routes.py, y los
    tests solo cubren el happy path de days_left.

    # Rol
    Actúa como Product Manager que tiene que defender esta priorización frente a un equipo de
    ingeniería escéptico y frente a un stakeholder académico impaciente.

    # Objetivo
    Ordenar el backlog {{BACKLOG}} maximizando {{CRITERIO_DE_NEGOCIO}}, dejando visibles los
    trade-offs de cada decisión.

    # Restricciones
    - Usa un marco explícito (RICE, WSJF o costo de retraso) y declara cuál usas.
    - Todo número viene del input o va marcado como estimación tuya.
    - La deuda técnica y los tests faltantes compiten en la misma lista que las features: no
      los mandes a una lista aparte.
    - Prohibido empatar: si dos ítems quedan iguales, desempata con un criterio declarado.
    - Máximo una línea de justificación por ítem.

    # Input
    Backlog: {{BACKLOG}}
    Criterio de negocio a maximizar: {{CRITERIO_DE_NEGOCIO}}
    Datos disponibles de uso, soporte e incidentes: {{DATOS}}

    # Output esperado
    1. Tabla priorizada: rango, ítem, puntaje del marco, justificación de una línea.
    2. Los tres ítems que NO harías este trimestre y por qué.
    3. Un párrafo: el dato que, si llegara, reordenaría toda la lista.

    # Validación
    Para los tres primeros ítems, di cuál de tus estimaciones es la más frágil y qué pasaría
    con el orden si estuviera equivocada por un factor de dos. Marca con [SIN DATO] cada
    celda donde tuviste que inventar un número.

### Software Engineer

El error típico: pedir "hazme el endpoint" sin contrato, sin esquema y sin errores. Sale código que compila y que nadie puede revisar.

La plantilla corrige eso fijando el stack, el contrato de API y el criterio de "terminado" antes de que se escriba la primera línea.

**SWE-01** — Reemplaza `{{CAPACIDAD}}`, `{{RESTRICCIONES_NO_FUNCIONALES}}` (latencia, volumen, despliegue) y `{{CODIGO_ACTUAL}}`.

SWE-01 · Diseño de arquitectura y contrato de API

    # Contexto
    Repositorio campusflow-api. Stack no negociable: Python 3.12, FastAPI, PostgreSQL 16 +
    pgvector, SQLAlchemy 2.x, Pydantic v2, pytest, Alembic. API-first, sin frontend, JWT.
    Entidades: users, courses, enrollments, deliverables, documents, chunks, reminders.
    Estructura: app/api/routes.py, app/services/, app/models/, app/schemas/, alembic/versions.

    # Rol
    Actúa como Software Engineer senior de backend que va a mantener este diseño dos años y
    que odia las abstracciones que nadie usa.

    # Objetivo
    Diseñar la arquitectura y el contrato de API de {{CAPACIDAD}} antes de escribir código.

    # Restricciones
    - No cambies el stack ni agregues librerías sin justificarlo en una línea.
    - Cada endpoint se especifica con método, ruta, permisos, request model y response model
      de Pydantic v2, y todos los códigos de error con su cuerpo.
    - Todo cambio de esquema va con su migración de Alembic descrita, y su rollback.
    - Las rutas no contienen lógica de negocio: separa app/api/routes.py de app/services/.
    - Prohibido escribir código de implementación. Solo diseño.

    # Input
    Capacidad: {{CAPACIDAD}}
    Restricciones no funcionales: {{RESTRICCIONES_NO_FUNCIONALES}}
    Código o esquema actual relevante:
    {{CODIGO_ACTUAL}}

    # Output esperado
    1. Flujo request-response en texto, capa por capa.
    2. Contrato de API por endpoint, con ejemplos de request y response en JSON.
    3. Cambios de modelo e índices, con migración y rollback descritos.
    4. Tres decisiones de diseño con su alternativa descartada y el motivo.

    # Validación
    Cierra con "Supuestos y huecos": todo lo que asumiste sobre código que no viste, y para
    cada supuesto, qué archivo del repositorio habría que abrir para confirmarlo. No propongas
    nada que no puedas justificar con el input dado.

**SWE-02** — Implementa la feature pendiente canónica del repo. Reemplaza `{{DEFINICION_DE_HORAS}}`, `{{DEFINICION_DE_SEMANA}}` y `{{CODIGO_ACTUAL}}`.

SWE-02 · Implementación de un endpoint nuevo

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, pytest, Alembic, auth JWT simple. Convenciones: rutas
    delgadas en app/api/routes.py, lógica en app/services/, schemas en app/schemas/.
    Feature pendiente: GET /courses/{course_id}/workload, la carga académica de la semana
    (número de entregas y horas estimadas por materia).

    # Rol
    Actúa como Software Engineer del equipo de CampusFlow. Escribes código que pasa por code
    review de un colega exigente hoy mismo.

    # Objetivo
    Implementar GET /courses/{course_id}/workload completo: schema, servicio, ruta y tests.

    # Restricciones
    - La ruta no hace queries. Pydantic v2, no v1. SQLAlchemy 2.x con select().
    - Todas las fechas timezone-aware en UTC. Prohibido datetime.utcnow().
    - Autorización: solo ve la carga quien tiene fila en enrollments para ese curso; si no,
      403; si el curso no existe, 404.
    - Tests de pytest en el mismo entregable, con al menos un caso de borde.
    - Sin dependencias nuevas.

    # Input
    Regla de estimación de horas: {{DEFINICION_DE_HORAS}}
    Semana de referencia: {{DEFINICION_DE_SEMANA}}
    Código actual (models, schemas, rutas):
    {{CODIGO_ACTUAL}}

    # Output esperado
    1. Cada archivo creado o modificado, completo, con su ruta.
    2. Migración de Alembic, o la frase "no requiere migración" justificada.
    3. Tests de pytest y el comando exacto para correrlos.

    # Validación
    Antes del código, escribe los cinco casos que refutarían tu implementación si estuviera
    mal: semana sin entregas, entregas que cruzan el fin de semana, usuario no matriculado,
    curso inexistente y entrega que vence hoy a las 23:59. Después del código, di cuáles de
    los cinco quedaron cubiertos por tus tests y cuáles no.

**SWE-03** — Refactor sobre la duplicación canónica del repo. Reemplaza `{{CODIGO_ACTUAL}}` con los dos archivos completos y `{{TESTS_ACTUALES}}`.

SWE-03 · Refactoring de lógica duplicada

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, pytest, Alembic. El cálculo de "días restantes" está
    duplicado en app/services/deadlines.py y app/api/routes.py, y las dos copias divergieron.
    Cobertura actual: solo el happy path de days_left.

    # Rol
    Actúa como Software Engineer haciendo un refactor de riesgo controlado sobre código en
    producción. Tu regla: un refactor no cambia comportamiento observable.

    # Objetivo
    Eliminar la duplicación dejando una única fuente de verdad para el cálculo de días
    restantes, sin alterar el contrato público de la API.

    # Restricciones
    - Pasos pequeños y reversibles: cada paso deja el repositorio verde.
    - Primero caracterización: tests que capturen el comportamiento ACTUAL, incluido el que
      consideres incorrecto, antes de mover nada.
    - Si detectas un bug durante el refactor, NO lo arregles aquí: documéntalo aparte.
    - La función unificada vive en app/services/deadlines.py, con firma tipada; las rutas solo
      delegan. Sin dependencias nuevas.

    # Input
    Código actual de los dos archivos:
    {{CODIGO_ACTUAL}}
    Tests existentes:
    {{TESTS_ACTUALES}}

    # Output esperado
    1. Tests de caracterización, antes de tocar nada.
    2. Plan de refactor numerado, con el estado del repositorio tras cada paso.
    3. Archivos finales completos.
    4. Sección "Bugs detectados, no corregidos aquí", con la reproducción de cada uno.

    # Validación
    Demuestra que el refactor es seguro: para cada test de caracterización indica si pasa
    antes y después del cambio. Luego enumera qué comportamientos NO pudiste verificar con el
    código que te di y qué necesitarías para verificarlos.

**SWE-04** — El bug canónico de la clase. Reemplaza `{{REPORTE}}`, `{{CODIGO_ACTUAL}}` y `{{EVIDENCIA}}` (logs, salida observada).

SWE-04 · Debugging con hipótesis explícitas

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, pytest, Alembic. Síntoma: una entrega que vence HOY a las
    23:59 aparece en la agenda como "vencida" y el ordenamiento queda mal. Entorno: la base
    guarda deadlines en UTC, el servidor corre en UTC, los estudiantes están en
    America/Bogota (UTC-5).

    # Rol
    Actúa como Software Engineer haciendo debugging disciplinado. No parcheas síntomas:
    formulas hipótesis, las ordenas por probabilidad y las descartas con evidencia.

    # Objetivo
    Encontrar la causa raíz del síntoma y proponer la corrección mínima.

    # Restricciones
    - Antes de proponer cambios, enumera al menos tres hipótesis distintas, y para cada una
      qué observación la confirmaría y cuál la descartaría.
    - La corrección es mínima: nada de reescribir el módulo.
    - Fechas timezone-aware en UTC; el formateo a hora local es de la capa de presentación.
    - Prohibido datetime.utcnow() y comparar naive con aware.
    - Entrega un test que falle ANTES del fix y pase DESPUÉS.

    # Input
    Reporte del usuario: {{REPORTE}}
    Código actual:
    {{CODIGO_ACTUAL}}
    Traza, logs o salida observada: {{EVIDENCIA}}

    # Output esperado
    1. Tabla de hipótesis: hipótesis, probabilidad, cómo confirmarla, cómo descartarla.
    2. Causa raíz en tres líneas y test de regresión que reproduce el fallo.
    3. Diff mínimo del fix.
    4. Otros lugares del repositorio que probablemente tienen el mismo defecto.

    # Validación
    Explica por qué el fix NO es un parche: describe la clase entera de errores que elimina.
    Después lista las condiciones en las que tu fix seguiría fallando (otro huso horario, una
    entrega sin hora). Si no pudiste descartar una hipótesis con lo que te di, dilo en vez de
    elegir la más cómoda.

### QA Engineer

El error típico: pedir "escríbeme tests". El modelo devuelve el happy path, todo pasa, y la sensación de seguridad es falsa.

La plantilla corrige eso separando el diseño de casos de la escritura de código, y exigiendo particiones de equivalencia y valores frontera antes de importar pytest.

**QA-01** — Reemplaza `{{ENDPOINT}}`, `{{CRITERIOS_DE_ACEPTACION}}` (la salida de PM-03) y `{{REGLAS_DE_NEGOCIO}}`.

QA-01 · Diseño de casos de prueba desde criterios de aceptación

    # Contexto
    Producto CampusFlow, repositorio campusflow-api. Stack: Python 3.12, FastAPI,
    PostgreSQL 16 + pgvector, SQLAlchemy 2.x, Pydantic v2, pytest, Alembic, JWT. Entidades:
    users, courses, enrollments, deliverables, documents, chunks, reminders. Estado de la
    suite: solo existe el happy path de days_left; no hay pruebas de borde, ni de zona
    horaria, ni de listas vacías.

    # Rol
    Actúa como QA Engineer que diseña la suite antes de escribirla y que mide su trabajo por
    los defectos que encuentra, no por la cobertura que reporta.

    # Objetivo
    Convertir {{CRITERIOS_DE_ACEPTACION}} en casos de prueba trazables para {{ENDPOINT}}.

    # Restricciones
    - Cada caso se enlaza al criterio que verifica. Sin casos huérfanos.
    - Usa particiones de equivalencia y valores frontera, y declara cuáles usaste.
    - Cubre tres niveles: unidad (servicio), integración (con base de datos) y contrato
      (forma del JSON y códigos HTTP).
    - Cada caso: precondición, entrada, acción y resultado esperado exacto.
    - Prohibido escribir código de test aquí. Solo diseño.
    - Prioriza cada caso como P0, P1 o P2 y justifica los P0 en una línea.

    # Input
    Endpoint bajo prueba: {{ENDPOINT}}
    Criterios de aceptación: {{CRITERIOS_DE_ACEPTACION}}
    Reglas de negocio conocidas: {{REGLAS_DE_NEGOCIO}}

    # Output esperado
    1. Tabla: ID, criterio cubierto, nivel, prioridad, precondición, entrada, esperado.
    2. Matriz de trazabilidad criterio-caso, resaltando los criterios sin cobertura.
    3. Datos de prueba necesarios: usuarios, cursos, enrollments, deliverables.

    # Validación
    Audita tu propia matriz: nombra los criterios que quedaron con un solo caso, porque son
    los más frágiles. Luego lista lo que NO se puede probar con esta suite y qué tipo de
    prueba haría falta (carga, seguridad, exploratoria).

**QA-02** — Reemplaza `{{FUNCION_O_ENDPOINT}}`, `{{CODIGO_ACTUAL}}` y `{{SUPUESTOS_DE_FECHAS}}`. Este es el prompt que rompe el bug canónico.

QA-02 · Casos borde y análisis adversarial

    # Contexto
    CampusFlow calcula "días restantes" a partir de un deadline guardado en UTC; los
    estudiantes están en America/Bogota (UTC-5). Ya hay un defecto reportado: una entrega que
    vence hoy a las 23:59 aparece como vencida. Stack: Python 3.12, FastAPI, PostgreSQL 16 +
    pgvector, SQLAlchemy 2.x, Pydantic v2, pytest, Alembic.

    # Rol
    Actúa como QA Engineer adversarial. Tu objetivo no es confirmar que el código funciona:
    es encontrar la entrada que lo rompe y que nadie pensó.

    # Objetivo
    Producir el catálogo de casos borde de {{FUNCION_O_ENDPOINT}}, ordenado por probabilidad
    de que haya un defecto real detrás.

    # Restricciones
    - Cubre estas familias: vacío / uno / muchos, límites numéricos, fechas y zonas horarias,
      concurrencia, datos malformados, permisos, unicode y textos largos.
    - En fechas cubre explícitamente: mismo día antes y después de medianoche local, entrega
      ya vencida, cambio de día entre UTC y America/Bogota, deadline sin hora, timedelta
      negativo.
    - Cada caso dice qué defecto sospechas, no solo qué entrada usar.
    - Prohibido repetir casos que ya son happy path. Máximo una línea por caso.

    # Input
    Función o endpoint: {{FUNCION_O_ENDPOINT}}
    Código o firma:
    {{CODIGO_ACTUAL}}
    Supuestos del negocio sobre fechas: {{SUPUESTOS_DE_FECHAS}}

    # Output esperado
    1. Tabla: ID, familia, entrada, esperado, defecto sospechado, prioridad.
    2. Los cinco casos que ejecutarías primero si solo tuvieras diez minutos.
    3. Preguntas abiertas a producto sobre comportamiento indefinido.

    # Validación
    Para esos cinco casos, predice el resultado del código ACTUAL y márcalo como "pasa" o
    "falla". Esa predicción es tu apuesta: si el código real la contradice, tu modelo mental
    del sistema está mal. Señala también los casos cuyo resultado no puedes predecir con lo
    que te di.

**QA-03** — Reemplaza `{{CASOS}}` con la salida de QA-01 o QA-02, más `{{CODIGO_ACTUAL}}` y `{{CONFTEST_ACTUAL}}`.

QA-03 · Tests automatizados en pytest

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, pytest, Alembic; cliente de pruebas TestClient de FastAPI.
    Convenciones: tests en tests/, fixtures en tests/conftest.py, base de datos de pruebas
    efímera por sesión, nada de mocks sobre SQLAlchemy. Entidades: users, courses,
    enrollments, deliverables, documents, chunks, reminders.

    # Rol
    Actúa como QA Engineer que escribe la suite que el equipo corre en cada commit. Un test
    lento o intermitente es un test que alguien va a borrar.

    # Objetivo
    Convertir los casos {{CASOS}} en tests de pytest ejecutables.

    # Restricciones
    - Un assert conceptual por test; nombres del tipo test_sujeto_condicion_esperado.
    - Usa @pytest.mark.parametrize para las familias de casos; nada de copiar y pegar.
    - Fechas congeladas de forma determinista (freezegun o inyección del reloj). Prohibido
      datetime.now() dentro del test.
    - Fixtures para los datos: nada de crear registros a mano en cada test.
    - Nada de sleep, ni dependencia entre tests, ni orden implícito.
    - Marca con marcadores de pytest los tests lentos o de integración.

    # Input
    Casos a automatizar: {{CASOS}}
    Código bajo prueba:
    {{CODIGO_ACTUAL}}
    Fixtures existentes: {{CONFTEST_ACTUAL}}

    # Output esperado
    1. tests/conftest.py completo con las fixtures nuevas o modificadas.
    2. Los archivos de test completos.
    3. Comando de ejecución, y el comando para correr solo los P0.
    4. Qué se espera que falle hoy contra el código actual, y por qué.

    # Validación
    Antes de entregar, audita tu suite en una tabla y responde: (a) ¿algún test pasaría igual
    si borro la lógica que dice probar? (b) ¿alguno depende del reloj real o del orden de
    ejecución? (c) ¿algún caso del input quedó sin test? Corrige lo que falle antes de
    mostrar el código final.

### Security Engineer

El error típico: pedir "revisa la seguridad de este código". Sin activo, sin atacante y sin superficie, el modelo devuelve una lista de buenas prácticas.

La plantilla corrige eso obligando a nombrar qué se protege, de quién, y qué pasa si falla.

**SEC-01** — Reemplaza `{{ALCANCE}}` (el componente a modelar), `{{ACTIVOS}}` (los datos que importan) y `{{ARQUITECTURA}}`.

SEC-01 · Threat modeling con STRIDE

    # Contexto
    CampusFlow, API académica multiusuario. Stack: Python 3.12, FastAPI, PostgreSQL 16 +
    pgvector, SQLAlchemy 2.x, Pydantic v2, Alembic, auth JWT simple, sin frontend. Entidades:
    users, courses, enrollments, deliverables, documents, chunks, reminders. Superficie
    externa: subida de PDF del syllabus, extracción de entregas, consulta en lenguaje natural
    sobre documentos (RAG sobre pgvector) y agenda. Población: estudiantes, monitores y
    profesores de una misma universidad, con datos académicos personales.

    # Rol
    Actúa como Security Engineer haciendo threat modeling con STRIDE sobre un sistema que
    todavía se puede cambiar barato, porque está en piloto.

    # Objetivo
    Modelar las amenazas de {{ALCANCE}} sobre los activos {{ACTIVOS}} y priorizar mitigaciones.

    # Restricciones
    - Empieza por el data flow en texto: entidades externas, procesos, almacenes y fronteras
      de confianza. Sin eso no hay modelo.
    - Recorre las seis categorías STRIDE en cada frontera. No saltes ninguna.
    - Cada amenaza: activo afectado, atacante plausible, precondición, impacto y mitigación
      concreta al stack. Nada de "usar buenas prácticas".
    - Obligatorio incluir tenancy (un estudiante leyendo datos de un curso donde no está
      matriculado) y prompt injection vía el texto del PDF subido, que entra al contexto.
    - No inventes componentes que no estén en el contexto.

    # Input
    Alcance: {{ALCANCE}} · Activos a proteger: {{ACTIVOS}}
    Arquitectura o código relevante:
    {{ARQUITECTURA}}

    # Output esperado
    1. Data flow en texto con fronteras de confianza numeradas.
    2. Tabla STRIDE: ID, frontera, categoría, amenaza, impacto, probabilidad, mitigación.
    3. Las cinco mitigaciones que implementarías primero, con esfuerzo estimado.
    4. Riesgos aceptados conscientemente en v0, escritos como decisión.

    # Validación
    Cierra con "Lo que este modelo no cubre": componentes, integraciones o actores que
    quedaron fuera por falta de información, y la pregunta concreta que habría que responder
    para incluirlos. Marca con [SUPUESTO] cada afirmación sobre el sistema que no salió del
    input.

**SEC-02** — Reemplaza `{{DIFF_O_MODULO}}` (funciona bien sobre el diff de un PR), `{{MODELO_DE_AMENAZA}}` y `{{DATOS_SENSIBLES}}`.

SEC-02 · Análisis de vulnerabilidades sobre código

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, Alembic. Auth JWT simple, HS256, secreto en variable de
    entorno. Datos sensibles: identidad del estudiante, matrículas, entregas, documentos del
    curso. Despliegue: contenedor detrás de un reverse proxy, base de datos gestionada.

    # Rol
    Actúa como Security Engineer haciendo revisión de código orientada a explotabilidad. Un
    hallazgo sin ruta de explotación es ruido y le quita credibilidad al resto del informe.

    # Objetivo
    Auditar {{DIFF_O_MODULO}} y reportar solo vulnerabilidades con ruta de explotación descrita.

    # Restricciones
    - Cada hallazgo: ubicación exacta (archivo y línea), clase de vulnerabilidad, ruta de
      explotación paso a paso, impacto y severidad justificada.
    - Prioriza en este orden: autenticación y autorización, IDOR y control de acceso por
      objeto, inyección (SQL y de prompt), exposición de datos en respuestas y logs, manejo
      de secretos, deserialización y subida de archivos.
    - En la subida de PDF evalúa tamaño máximo, tipo real del archivo, ruta de escritura y el
      hecho de que su texto entra al contexto de un modelo.
    - Prohibidos los hallazgos genéricos sin línea de código que los sustente.
    - Cada corrección va como diff mínimo, no como reescritura.

    # Input
    Código a auditar:
    {{DIFF_O_MODULO}}
    Modelo de amenaza asumido: {{MODELO_DE_AMENAZA}}
    Datos que maneja este código: {{DATOS_SENSIBLES}}

    # Output esperado
    1. Tabla de hallazgos ordenada por severidad, con ruta de explotación.
    2. Diff de corrección por hallazgo.
    3. Lista aparte de "olores" que no son vulnerabilidades pero hay que arreglar.

    # Validación
    Para cada hallazgo, escribe la petición HTTP concreta que lo demostraría: método, ruta,
    cabeceras y cuerpo. Si un hallazgo no se puede demostrar así, degrádalo a "sospecha" y di
    qué parte del sistema tendrías que ver para confirmarlo. Declara qué archivos habrías
    necesitado y no te di.

**SEC-03** — Reemplaza `{{FUNCIONALIDAD}}` con lo que se va a escribir seguro desde cero, más `{{REGLAS_DE_ACCESO}}` y `{{CODIGO_ACTUAL}}`.

SEC-03 · Secure coding de una funcionalidad nueva

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, pytest, Alembic, JWT. Entidades: users, courses,
    enrollments, deliverables, documents, chunks, reminders. Regla de tenancy: un usuario
    accede solo a cursos donde tiene fila en enrollments; el profesor accede a todo su curso;
    nadie accede a otro curso. El texto de los documentos subidos se convierte en chunks y se
    inyecta en el contexto del modelo al responder preguntas.

    # Rol
    Actúa como Security Engineer que escribe la implementación de referencia. El resto del
    equipo va a copiar tu patrón, así que el patrón importa más que el caso puntual.

    # Objetivo
    Implementar {{FUNCIONALIDAD}} segura por construcción, no por revisión posterior.

    # Restricciones
    - Validación de entrada con Pydantic v2 en el borde, no dentro del servicio.
    - Autorización por objeto dentro del query: la pertenencia se comprueba en la consulta,
      no después de traer la fila. Consultas parametrizadas con SQLAlchemy 2.x.
    - Errores que no filtran información: 404 en vez de 403 cuando revelar la existencia del
      recurso ya es una fuga.
    - Nada de secretos en el código ni datos personales en logs. Sin dependencias nuevas.
    - El texto de documentos es entrada no confiable frente al modelo: delimítalo y no le des
      autoridad de instrucción.

    # Input
    Funcionalidad: {{FUNCIONALIDAD}}
    Reglas de acceso adicionales: {{REGLAS_DE_ACCESO}}
    Código existente relevante:
    {{CODIGO_ACTUAL}}

    # Output esperado
    1. Código completo por archivo.
    2. Tabla control-por-control: qué amenaza mitiga cada decisión del código.
    3. Tests de seguridad en pytest: acceso cruzado entre cursos, token inválido, token
       expirado, entrada malformada, payload de inyección de prompt dentro del documento.

    # Validación
    Ataca tu propio código: elige el control más débil, descríbelo como lo haría un atacante y
    di si tu implementación lo detiene. Si no lo detiene, corrige el código antes de terminar
    la respuesta y muestra el diff.

### UX Designer

El error típico: pedir "mejora la UX" de una API sin frontend y esperar pantallas. En CampusFlow la experiencia son los mensajes de error, el formato de la agenda y las respuestas del asistente.

La plantilla corrige eso definiendo el usuario, el momento y el criterio de éxito antes de hablar de interfaz.

**UX-01** — Reemplaza `{{TAREA}}` (por ejemplo: subir el syllabus y ver sus entregas), `{{PERSONA}}` y `{{RESTRICCIONES_TECNICAS}}`.

UX-01 · User flow de punta a punta

    # Contexto
    CampusFlow es API-first y en v0 no tiene frontend propio: la experiencia se consume desde
    un cliente delgado y desde respuestas en lenguaje natural. Personas: Ana (5º semestre, 6
    materias, vive en el celular, se entera tarde de las entregas), Camilo (monitor) y la
    profesora Restrepo. Capacidades v0: importar syllabus en PDF, agenda unificada, preguntas
    sobre documentos del curso, recordatorios especificados. Fuera de v0: app móvil nativa,
    integración con el LMS, push, chat grupal.

    # Rol
    Actúa como UX Designer de producto que diseña flujos, no pantallas bonitas, y que trabaja
    con un equipo que en esta versión solo puede construir API.

    # Objetivo
    Diseñar el user flow completo de {{TAREA}} para {{PERSONA}}, incluidos los caminos que
    fallan.

    # Restricciones
    - El flujo empieza antes del producto (qué estaba haciendo la persona) y termina después
      (qué hace con el resultado).
    - Cada paso: intención, acción, respuesta del sistema y estado emocional en tres palabras.
    - Obligatorio modelar los estados vacío, cargando, parcial y error.
    - Para la extracción del PDF, modela el caso en que sale incompleta o dudosa: qué ve la
      persona y cómo corrige.
    - Nada de decisiones visuales. Máximo 12 pasos en el camino principal.

    # Input
    Tarea: {{TAREA}} · Persona: {{PERSONA}}
    Restricciones técnicas conocidas: {{RESTRICCIONES_TECNICAS}}

    # Output esperado
    1. Camino principal paso a paso, con los cuatro campos por paso.
    2. Ramas alternativas y de error, enlazadas al paso donde se bifurcan.
    3. Los textos exactos de los mensajes clave, incluidos los de error.
    4. Los tres momentos donde la persona más probablemente abandona.

    # Validación
    Marca cada paso con su evidencia: [OBSERVADO] si sale del contexto que te di, [SUPUESTO]
    si lo estás infiriendo. Luego escribe la única pregunta que le harías a Ana para validar
    el paso más frágil del flujo.

**UX-02** — Reemplaza `{{ARTEFACTO}}` (respuestas de la API, mensajes de error, formato de la agenda), `{{CONTEXTO_DE_USO}}` y `{{PERSONA}}`.

UX-02 · Revisión de UX con heurísticas

    # Contexto
    En CampusFlow v0 la experiencia percibida son tres cosas: los mensajes de error de la API,
    el formato de la agenda de entregas y las respuestas en lenguaje natural del asistente
    sobre los documentos del curso. Persona principal: Ana, que consulta desde el celular,
    con poco tiempo, entre clases. Defecto conocido: una entrega que vence hoy a las 23:59 se
    muestra como "vencida", lo que destruye la confianza en toda la agenda.

    # Rol
    Actúa como UX Designer haciendo una revisión heurística. Reportas problemas con severidad,
    no opiniones de gusto personal.

    # Objetivo
    Revisar {{ARTEFACTO}} y producir una lista priorizada de problemas de experiencia con su
    corrección concreta.

    # Restricciones
    - Usa las heurísticas de Nielsen y declara cuál viola cada hallazgo.
    - Cada hallazgo: qué ve el usuario, por qué es problema para Ana en su contexto, severidad
      de 1 a 4, y la corrección exacta con el texto reescrito.
    - Cualquier dato mostrado que sea incorrecto o ambiguo va como severidad alta, aunque
      parezca cosmético: la confianza es la métrica.
    - Los mensajes de error dicen qué pasó, por qué y qué hacer ahora. Reescribe los que no.
    - Prohibidos los rediseños completos. Solo cambios acotados. Español de Colombia.

    # Input
    Artefacto a revisar:
    {{ARTEFACTO}}
    Contexto de uso: {{CONTEXTO_DE_USO}} · Persona: {{PERSONA}}

    # Output esperado
    1. Tabla: ID, heurística violada, qué ve el usuario, severidad, corrección.
    2. Los textos reescritos, listos para pegar en el código.
    3. Los tres cambios con mejor relación impacto-esfuerzo.

    # Validación
    Para cada hallazgo de severidad 3 o 4, escribe la tarea de usability testing de una frase
    que confirmaría que el problema existe de verdad. Y separa en una lista aparte llamada
    "Opinión, no hallazgo" todo lo que sea preferencia tuya y no problema demostrable.

**UX-03** — Reemplaza `{{SUPERFICIE}}`, `{{NIVEL_WCAG}}` (normalmente AA) y `{{TECNOLOGIAS_DE_ASISTENCIA}}`.

UX-03 · Accesibilidad

    # Contexto
    CampusFlow es material académico obligatorio, no un producto opcional. En v0 su salida es
    texto: agenda de entregas, respuestas del asistente sobre documentos del curso y mensajes
    de error de la API, renderizados por un cliente delgado en el celular. Población real:
    estudiantes con baja visión, con lector de pantalla, con dislexia, y con conexión
    intermitente y datos limitados.

    # Rol
    Actúa como UX Designer especialista en accesibilidad. Evalúas contra criterios numerados,
    no contra sensaciones.

    # Objetivo
    Evaluar {{SUPERFICIE}} contra WCAG {{NIVEL_WCAG}} y entregar correcciones aplicables.

    # Restricciones
    - Cada hallazgo cita el criterio WCAG por número y nombre.
    - Cubre las cuatro dimensiones: perceptible, operable, comprensible, robusto.
    - En contenido generado por el modelo evalúa además legibilidad: longitud de frase, jerga,
      estructura, y si la respuesta se entiende leída en voz alta por un lector de pantalla.
    - En la agenda, evalúa si el estado de una entrega se comunica solo por color o también
      por texto.
    - Prohibido responder "cumple" sin decir cómo lo verificaste.
    - Distingue lo que se corrige en el contenido de lo que se corrige en el cliente.

    # Input
    Superficie evaluada:
    {{SUPERFICIE}}
    Nivel objetivo: {{NIVEL_WCAG}}
    Tecnologías de asistencia a soportar: {{TECNOLOGIAS_DE_ASISTENCIA}}

    # Output esperado
    1. Tabla: criterio WCAG, estado (cumple / no cumple / no verificable), evidencia,
       corrección propuesta.
    2. Los textos y estructuras corregidos.
    3. Verificaciones manuales que un humano debe hacer con lector de pantalla.
    4. Riesgos de accesibilidad propios de respuestas generadas por un modelo.

    # Validación
    Declara qué criterios marcaste como "no verificable" con la información dada y por qué; no
    los cuentes como cumplidos. Luego lista tus supuestos sobre cómo el cliente renderiza este
    contenido, porque de ellos depende la mitad de tu evaluación.

### AI Engineer

El error típico: pedir "hazme un RAG" y recibir un script con un tamaño de chunk fijo y ninguna justificación.

La plantilla corrige eso obligando a declarar el corpus, las preguntas reales y qué se mide antes de elegir librería.

**AI-01** — Reemplaza `{{CORPUS}}`, `{{PREGUNTAS_REALES}}` y `{{PRESUPUESTO}}` (latencia y costo por consulta).

AI-01 · Diseño del pipeline de RAG

    # Contexto
    CampusFlow, capacidad 3 del MVP: responder preguntas en lenguaje natural sobre documentos
    del curso (syllabus en PDF, reglamento, guías). Stack: Python 3.12, FastAPI, PostgreSQL 16
    + pgvector, SQLAlchemy 2.x, Pydantic v2, Alembic; entidades documents, chunks, courses,
    enrollments. Restricción de datos: cada respuesta solo puede usar documentos de cursos
    donde el usuario tiene enrollment. Anthropic no ofrece modelo de embeddings propio: se usa
    un proveedor externo. La práctica estándar es retrieval híbrido (denso más léxico) con
    reranking, y no hay consenso publicado sobre el tamaño óptimo de chunk.

    # Rol
    Actúa como AI Engineer que va a operar este pipeline en producción y a explicarle a un
    profesor por qué el sistema respondió lo que respondió.

    # Objetivo
    Diseñar el pipeline de RAG completo para {{CORPUS}}, optimizado para {{PREGUNTAS_REALES}}
    dentro del presupuesto {{PRESUPUESTO}}.

    # Restricciones
    - Cubre todas las etapas: ingestión, parsing del PDF, chunking, embeddings, indexación en
      pgvector, retrieval, reranking, construcción del prompt, generación y citación.
    - Todo parámetro (chunk, solapamiento, top-k, umbral) se declara como hipótesis a medir.
      Prohibido dar un número sin decir cómo lo validarías.
    - El filtro por enrollment se aplica en el retrieval, no después.
    - Toda respuesta cita documento y sección; si no hay evidencia suficiente, el sistema dice
      que no sabe.
    - El texto de los documentos es entrada no confiable frente al modelo.

    # Input
    Corpus: {{CORPUS}}
    Preguntas reales de estudiantes: {{PREGUNTAS_REALES}}
    Presupuesto de latencia y costo: {{PRESUPUESTO}}

    # Output esperado
    1. Pipeline etapa por etapa, con entradas y salidas.
    2. Tabla de decisiones: parámetro, valor inicial, razón, cómo se mide, cómo se ajusta.
    3. Esquema de la tabla chunks con índices y migración descrita.
    4. Plantilla del prompt de generación, separando instrucción de contexto recuperado.
    5. Modos de fallo del pipeline y su mitigación.

    # Validación
    Argumenta en contra de tu propio diseño: para este corpus y estas preguntas, ¿cuándo sería
    mejor NO hacer RAG y pasar los documentos completos en el context window? Da la condición
    concreta que inclina la decisión y marca como hipótesis todo parámetro sin evidencia.

**AI-02** — Reemplaza `{{TAREA_DEL_AGENTE}}`, `{{TOOLS_DISPONIBLES}}` y `{{LIMITES}}` (presupuesto, iteraciones, permisos).

AI-02 · Diseño de un agente

    # Contexto
    CampusFlow quiere un agente que evite que Camilo, el monitor, responda 40 veces la misma
    pregunta del syllabus. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector, SQLAlchemy
    2.x, Pydantic v2. Ciclo de tool use de la API: se declaran tools con nombre, descripción e
    input_schema; el modelo responde con stop_reason "tool_use"; la aplicación ejecuta y
    devuelve tool_result con el mismo tool_use_id; el modelo produce la respuesta final. Ese
    ciclo es el agente. Datos accesibles: courses, enrollments, deliverables, documents, chunks.

    # Rol
    Actúa como AI Engineer que diseña agentes de producción, donde un agente que se equivoca
    en silencio es peor que uno que se niega a actuar.

    # Objetivo
    Diseñar el agente que resuelve {{TAREA_DEL_AGENTE}}, con su bucle, sus tools, sus límites
    y su comportamiento ante fallos.

    # Restricciones
    - Define objetivo, estado que mantiene, condición de parada, máximo de iteraciones y qué
      hace al agotarlas.
    - Separa lecturas de escrituras; toda escritura requiere confirmación humana en v0.
    - El agente nunca inventa datos académicos: si una tool falla o vuelve vacía, lo dice.
    - El filtro por enrollment vive dentro de cada tool, no en el prompt.
    - El contenido de los documentos son datos, no instrucciones: el agente debe resistir
      prompt injection embebida en un PDF subido.
    - Justifica el modelo entre claude-opus-5, claude-sonnet-5 y claude-haiku-4-5 por costo,
      latencia y dificultad.

    # Input
    Tarea del agente: {{TAREA_DEL_AGENTE}}
    Herramientas disponibles o construibles: {{TOOLS_DISPONIBLES}}
    Límites operativos: {{LIMITES}}

    # Output esperado
    1. System prompt del agente, completo y listo para usar.
    2. Tools con nombre, descripción y cuándo debe usarse cada una.
    3. El bucle: percepción, decisión, acción, observación, parada.
    4. Política de fallos y qué queda fuera de la autonomía del agente.

    # Validación
    Escribe tres trazas simuladas: una feliz, una con una tool caída y una donde el documento
    del curso trae una instrucción maliciosa dirigida al modelo. Para cada traza di qué debería
    pasar y si tu diseño lo garantiza o solo lo sugiere. Lo que solo se sugiere, márcalo.

**AI-03** — Reemplaza `{{CAPACIDAD_A_EXPONER}}`, `{{ENDPOINTS_ACTUALES}}` y `{{CONSULTAS_TIPICAS}}`.

AI-03 · Definición de tools y schemas

    # Contexto
    CampusFlow: API en FastAPI con Pydantic v2 sobre PostgreSQL 16. Entidades: users, courses,
    enrollments, deliverables, documents, chunks, reminders; endpoints sobre /courses,
    /deliverables y /documents, más la feature pendiente GET /courses/{course_id}/workload.
    Ciclo de tool use: tools con nombre, descripción e input_schema; el modelo emite bloques
    tool_use; la aplicación ejecuta y devuelve tool_result con el mismo tool_use_id. Las
    definiciones de tools consumen tokens de entrada en cada llamada, y el tool use en
    paralelo está activo por defecto.

    # Rol
    Actúa como AI Engineer que sabe que la descripción de una tool es un prompt: el modelo
    decide usarla leyendo ese texto, y ahí se gana o se pierde la mitad de la calidad.

    # Objetivo
    Definir el conjunto mínimo de tools que expone {{CAPACIDAD_A_EXPONER}} al modelo, con
    schemas estrictos.

    # Restricciones
    - Cada tool: nombre en snake_case, descripción de 2 a 4 frases que diga cuándo usarla y
      cuándo NO, e input_schema con types, required, enums y descripción por campo.
    - Prohibido un parámetro de texto libre donde pueda haber un enum.
    - Ninguna tool devuelve datos de cursos sin enrollment: el filtro es un parámetro implícito
      de servidor, no un argumento que el modelo pueda falsear.
    - Las tools de escritura se marcan como tales y describen su efecto irreversible.
    - Salidas acotadas: define tamaño máximo de respuesta y qué se trunca primero.
    - Minimiza el número de tools: si dos se solapan, fusiónalas.

    # Input
    Capacidad a exponer: {{CAPACIDAD_A_EXPONER}}
    Endpoints o funciones existentes: {{ENDPOINTS_ACTUALES}}
    Consultas típicas del usuario: {{CONSULTAS_TIPICAS}}

    # Output esperado
    1. Definiciones de tools en JSON, listas para pegar en el parámetro tools.
    2. Tabla: consulta típica, tools que el modelo debería elegir, en qué orden.
    3. Pares de tools que el modelo podría confundir, y cómo lo evitas desde la descripción.
    4. Costo estimado en tokens de las definiciones, y si conviene desactivar el paralelismo.

    # Validación
    Haz una prueba de ambigüedad contigo mismo: toma cinco consultas del input, léelas solo con
    las descripciones a la vista y di qué tool elegirías. Si dudas en alguna, la descripción
    está mal escrita: corrígela y muestra la versión final. Reporta también qué consultas no se
    pueden resolver con ninguna tool del conjunto.

**AI-04** — Reemplaza `{{SISTEMA_A_EVALUAR}}`, `{{CRITERIO_DE_CALIDAD}}` (qué es una buena respuesta aquí) y `{{EJEMPLOS}}`.

AI-04 · Diseño de evaluaciones

    # Contexto
    CampusFlow responde preguntas sobre documentos del curso usando RAG sobre pgvector con
    filtro de permisos por enrollment. Realidad del sistema: los modelos no son deterministas,
    alucinan y tienen knowledge cutoff; ninguna de las tres cosas se arregla con un prompt
    mejor, se miden. Riesgo específico: una respuesta incorrecta sobre una fecha de entrega o
    sobre el reglamento tiene consecuencias académicas reales para el estudiante.

    # Rol
    Actúa como AI Engineer responsable de la calidad. Tu entregable no es una demo que
    funcionó: es un número que el equipo pueda seguir midiendo en cada cambio.

    # Objetivo
    Diseñar el sistema de evaluación de {{SISTEMA_A_EVALUAR}} contra {{CRITERIO_DE_CALIDAD}}.

    # Restricciones
    - Define el eval set: cuántos casos, cómo se construyen, quién escribe el gold answer.
    - Mezcla obligatoriamente tres tipos: preguntas con respuesta clara en el corpus, preguntas
      sin respuesta en el corpus (el sistema debe decir que no sabe) y preguntas trampa con
      premisa falsa.
    - Separa métricas de retrieval (recall@k, precisión de citas) de métricas de generación
      (fidelidad a la fuente, cobertura, negativa correcta).
    - Si propones LLM-as-judge, especifica rúbrica, modelo y calibración contra juicio humano.
      Sin eso no es una métrica, es una opinión automatizada.
    - Incluye evaluación de seguridad: prompt injection desde el documento y fuga entre cursos.

    # Input
    Sistema a evaluar: {{SISTEMA_A_EVALUAR}}
    Criterio de calidad del producto: {{CRITERIO_DE_CALIDAD}}
    Ejemplos de preguntas y respuestas reales: {{EJEMPLOS}}

    # Output esperado
    1. Especificación del eval set: tamaño, composición por tipo, proceso de construcción.
    2. Tabla de métricas: nombre, qué mide, cómo se calcula, umbral de aceptación.
    3. Diez casos de evaluación completos, con su gold answer.
    4. Cómo se integra en CI, qué bloquea un merge, y qué NO mide este eval set.

    # Validación
    Ataca tu propio eval: describe una implementación mala del asistente que aun así pasaría
    todas tus métricas con buena nota. Si existe, tu eval tiene un hueco: agrega la métrica o
    el caso que lo cierra. Marca qué umbrales elegiste sin datos y habría que recalibrar con la
    primera corrida real.

### Code Reviewer

El error típico: pegar un diff y escribir "revisa esto". El modelo devuelve comentarios de estilo y se pierde el problema de autorización.

La plantilla corrige eso fijando qué se revisa, con qué estándar, y obligando a separar lo bloqueante de la opinión.

**CR-01** — Reemplaza `{{DIFF}}` con la salida de `git diff main`, `{{DESCRIPCION_DEL_PR}}` y `{{CONVENCIONES}}`.

CR-01 · Revisión de calidad de código

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, pytest, Alembic. Convenciones del CLAUDE.md: rutas delgadas
    en app/api/routes.py, lógica en app/services/, schemas en app/schemas/, tipado obligatorio
    en funciones públicas, fechas siempre timezone-aware en UTC, nada de datetime.utcnow().
    Historia conocida: la lógica de días restantes estuvo duplicada entre servicios y rutas.

    # Rol
    Actúa como Code Reviewer del equipo. Tu trabajo es proteger al repositorio y al autor, en
    ese orden. Directo con el código, respetuoso con la persona.

    # Objetivo
    Revisar {{DIFF}} y decidir: aprobado, aprobado con comentarios, o bloqueado.

    # Restricciones
    - Clasifica cada comentario como BLOQUEANTE, IMPORTANTE o NIT. Los NIT no bloquean nunca.
    - Cada comentario cita archivo y línea, dice qué está mal, por qué importa y cómo se
      arregla. Los tres, siempre.
    - Prohibido comentar lo que un formateador o un linter resuelven solos.
    - Verifica explícitamente: ¿el diff hace lo que dice la descripción?, ¿hay cambios que
      sobran?, ¿hay tests para lo nuevo?
    - Máximo tres comentarios BLOQUEANTES; si hay más, el PR es demasiado grande y ese es el
      comentario principal. Nada de reescribir el PR entero.

    # Input
    Descripción del PR: {{DESCRIPCION_DEL_PR}}
    Diff:
    {{DIFF}}
    Convenciones adicionales del equipo: {{CONVENCIONES}}

    # Output esperado
    1. Veredicto en una línea, con su razón.
    2. Comentarios agrupados por severidad, en formato archivo:línea.
    3. Lo que el PR hace bien, en dos o tres puntos concretos.
    4. Preguntas al autor sobre decisiones que no se entienden desde el diff.

    # Validación
    Cierra con "Confianza de esta revisión": qué partes del cambio no pudiste evaluar porque no
    viste el resto del repositorio, qué archivos habrías necesitado, y si tu veredicto
    cambiaría al verlos.

**CR-02** — Para PRs que cambian estructura, no solo comportamiento. Reemplaza `{{CAMBIO}}`, `{{ARQUITECTURA_ACTUAL}}` y `{{RESTRICCIONES_DEL_EQUIPO}}`.

CR-02 · Revisión de arquitectura

    # Contexto
    Repositorio campusflow-api. Arquitectura acordada: API-first en FastAPI sin frontend;
    rutas delgadas; lógica de negocio en app/services/; acceso a datos con SQLAlchemy 2.x;
    schemas de borde con Pydantic v2; migraciones con Alembic; PostgreSQL 16 con pgvector para
    los chunks. Principio del equipo: la simplicidad es un requisito, no una preferencia. El
    equipo es pequeño y el producto está en piloto.

    # Rol
    Actúa como Code Reviewer con foco arquitectónico. Revisas decisiones estructurales, no
    líneas. Tu pregunta constante es qué cuesta deshacer esto en seis meses.

    # Objetivo
    Evaluar si {{CAMBIO}} es coherente con la arquitectura actual y qué compromete a futuro.

    # Restricciones
    - Evalúa cinco ejes: acoplamiento, cohesión, dirección de las dependencias, facilidad de
      prueba y reversibilidad.
    - Toda abstracción nueva se justifica con al menos dos usos reales presentes; una
      abstracción con un solo uso es comentario BLOQUEANTE.
    - Señala si el cambio mete lógica de negocio en las rutas o consultas en la capa de API.
    - Evalúa el impacto en migraciones: ¿es reversible?, ¿bloquea la tabla?, ¿necesita ventana
      de mantenimiento?
    - Si propones una alternativa, incluye su costo, no solo su beneficio.
    - Prohibido recomendar patrones por nombre sin decir qué problema concreto resuelven aquí.

    # Input
    Cambio propuesto:
    {{CAMBIO}}
    Arquitectura actual relevante: {{ARQUITECTURA_ACTUAL}}
    Restricciones del equipo (tamaño, plazo, operación): {{RESTRICCIONES_DEL_EQUIPO}}

    # Output esperado
    1. Veredicto arquitectónico y su razón principal.
    2. Tabla por eje: eje, evaluación, evidencia en el código, riesgo.
    3. Decisiones que este cambio vuelve difíciles de revertir.
    4. La alternativa más simple que cumple el mismo objetivo, con su costo.

    # Validación
    Escribe el escenario a seis meses: cómo evoluciona este código si el producto pasa de un
    curso piloto a toda la facultad, y en qué punto exacto esta decisión se vuelve un problema.
    Si no puedes proyectarlo con lo que te di, di qué dato de crecimiento necesitas.

**CR-03** — Pase de seguridad sobre un PR concreto. Reemplaza `{{DIFF}}`, `{{SUPERFICIE_AFECTADA}}` y `{{CONTROLES_EXISTENTES}}`.

CR-03 · Revisión de seguridad de un PR

    # Contexto
    Repositorio campusflow-api. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, Alembic, auth JWT simple. Regla de tenancy: un usuario accede
    solo a cursos donde tiene fila en enrollments. Los documentos subidos son PDFs de terceros
    cuyo texto entra al contexto del modelo en el flujo de RAG. Datos personales en juego:
    identidad del estudiante, matrículas, entregas y notas.

    # Rol
    Actúa como Code Reviewer con sombrero de seguridad. Este pase es distinto del de calidad:
    aquí solo importa lo que un atacante puede hacer con este cambio.

    # Objetivo
    Determinar si {{DIFF}} introduce riesgo en {{SUPERFICIE_AFECTADA}} y bloquear el merge si
    lo hace.

    # Restricciones
    - Revisa en este orden: autorización por objeto, autenticación, validación de entrada,
      inyección (SQL y de prompt), exposición de datos en respuesta y en logs, manejo de
      secretos, dependencias nuevas.
    - Toda consulta nueva filtra por enrollment dentro del query; si filtra después, es
      BLOQUEANTE.
    - Toda dependencia añadida se justifica: qué hace, quién la mantiene, qué permisos pide.
    - Si el diff toca el flujo de documentos, evalúa prompt injection desde el contenido.
    - Prohibido aprobar por ausencia de evidencia: si no puedes ver el control, dilo.

    # Input
    Superficie afectada: {{SUPERFICIE_AFECTADA}}
    Diff:
    {{DIFF}}
    Controles de seguridad que ya existen: {{CONTROLES_EXISTENTES}}

    # Output esperado
    1. Veredicto: merge, merge con condiciones, o bloqueado.
    2. Hallazgos con severidad, ubicación y ruta de explotación en una línea.
    3. Diffs de corrección mínimos.
    4. Tests de seguridad que deberían acompañar este PR.

    # Validación
    Antes del veredicto, escribe la petición HTTP exacta con la que explotarías el hallazgo más
    grave, y qué respuesta esperas con y sin la corrección. Si ningún hallazgo se convierte en
    una petición concreta, di que el PR está limpio en lo que pudiste ver, y enumera lo que no
    pudiste ver.

**CR-04** — Para código que va a vivir mucho tiempo. Reemplaza `{{MODULO}}`, `{{HORIZONTE}}` y `{{TESTS_ACTUALES}}`.

CR-04 · Revisión de mantenibilidad y deuda técnica

    # Contexto
    Repositorio campusflow-api. Equipo pequeño y rotación alta: los monitores del curso cambian
    cada semestre y heredan el código. Stack: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
    SQLAlchemy 2.x, Pydantic v2, pytest, Alembic. Deuda conocida: la lógica de días restantes
    estuvo duplicada entre app/services/deadlines.py y app/api/routes.py, y la suite solo cubre
    el happy path de days_left. Parte del código se generó con IA y se aceptó sin revisión
    profunda.

    # Rol
    Actúa como Code Reviewer evaluando mantenibilidad. Tu criterio: ¿puede una persona nueva
    entender y cambiar este módulo con seguridad en su primera semana?

    # Objetivo
    Evaluar la mantenibilidad de {{MODULO}} en un horizonte de {{HORIZONTE}} y proponer un plan
    de pago de deuda.

    # Restricciones
    - Evalúa claridad de nombres, tamaño y responsabilidad de cada función, duplicación,
      acoplamiento temporal, magia implícita, cobertura y calidad de los tests.
    - Distingue deuda deliberada (documentada, con fecha) de deuda accidental.
    - Señala los rastros de código generado sin revisar: comentarios que explican lo obvio,
      abstracciones no usadas, manejo de errores genérico, patrones inconsistentes con el repo.
    - Cada ítem de deuda lleva costo de arreglarlo e interés de no arreglarlo.
    - Prohibido proponer una reescritura completa. El plan cabe en dos sprints de una persona.

    # Input
    Módulo a revisar:
    {{MODULO}}
    Horizonte de mantenimiento: {{HORIZONTE}}
    Tests actuales: {{TESTS_ACTUALES}}

    # Output esperado
    1. Puntaje de mantenibilidad por dimensión, con la evidencia que lo sustenta.
    2. Inventario de deuda: ítem, tipo, costo de arreglo, interés de no arreglarlo.
    3. Plan de pago ordenado, con qué se hace primero y por qué.
    4. Las tres preguntas que una persona nueva se haría leyendo esto, y dónde debe estar la
       respuesta.

    # Validación
    Haz la prueba del reemplazo: qué pasaría si mañana el único autor de este módulo deja el
    equipo. Nombra las tres cosas que se perderían por no estar escritas en ningún lado. Luego
    marca qué partes de tu evaluación son objetivas y cuáles son juicio tuyo.

### La plantilla maestra

Los veintiséis prompts anteriores son la misma plantilla. Esta es la versión vacía: la que hay que poder escribir sin mirar.

Plantilla maestra · vacía

    # Contexto
    {{QUE_SISTEMA_O_PRODUCTO}}: qué es, para quién, en qué estado está.
    {{STACK_Y_RESTRICCIONES_TECNICAS}}: lenguaje, framework, base de datos, versiones.
    {{ESTADO_ACTUAL}}: qué ya existe, qué falla hoy, qué se decidió y no se discute.

    # Rol
    Actúa como {{ROL_PROFESIONAL}} con {{EXPERIENCIA_O_SESGO}}.
    {{CRITERIO_PROFESIONAL}}: qué le importa a ese rol y qué rechaza.

    # Objetivo
    {{RESULTADO_UNICO_Y_MEDIBLE}}. Un solo objetivo: si hay dos, son dos prompts.

    # Restricciones
    - {{LO_QUE_NO_SE_PUEDE_CAMBIAR}}
    - {{FORMATO_O_CONVENCION_OBLIGATORIA}}
    - {{LO_QUE_ESTA_PROHIBIDO_HACER}}
    - {{LIMITE_DE_TAMANO_O_ALCANCE}}

    # Input
    {{DATOS_REALES}}: código, evidencia, requisitos, logs, transcripciones.
    {{PARAMETROS_DEL_CASO}}: los valores concretos del problema de hoy.

    # Output esperado
    1. {{ARTEFACTO_1}} con su formato exacto.
    2. {{ARTEFACTO_2}} con su formato exacto.
    3. {{ARTEFACTO_3}} con su formato exacto.
    Di el formato: tabla, diff, JSON, archivos completos, lista priorizada.

    # Validación
    {{TECNICA_DE_AUTOVERIFICACION}}, elegida entre estas:
    - listar los supuestos y separarlos de los hechos del input;
    - auto-verificarse contra los criterios de aceptación, uno por uno;
    - declarar qué NO se pudo determinar con la información dada;
    - proponer los casos de prueba que refutarían la propia solución;
    - construir el escenario en que la solución falla, y corregirla antes de entregar.

Qué hace cada sección y qué se rompe cuando falta:

| Sección         | Para qué sirve                                                                                | Si falta esta sección, el modelo…                                                                                    |
|-----------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Contexto        | Le da el mundo del problema: producto, stack, estado actual y lo que ya está decidido.        | …responde sobre un sistema genérico, propone cambiar el stack y da consejos que no aplican a tu repositorio.         |
| Rol             | Fija el criterio profesional con el que se juzga la respuesta y el sesgo útil que debe tener. | …contesta como un asistente promedio: correcto, blando y sin priorizar nada.                                         |
| Objetivo        | Declara el único resultado que cuenta como éxito.                                             | …hace un poco de todo, se desvía a lo que le parece interesante y no entrega nada terminado.                         |
| Restricciones   | Marca los límites duros: lo que no se cambia, lo prohibido, el tamaño y las convenciones.     | …mete librerías nuevas, reescribe módulos enteros y rompe las convenciones del equipo.                               |
| Input           | Entrega los datos reales del caso: código, evidencia, requisitos, valores.                    | …inventa el input que le falta y construye toda la respuesta sobre datos imaginarios.                                |
| Output esperado | Define el formato y los artefactos exactos que debe devolver.                                 | …entrega prosa larga que hay que reformatear a mano antes de poder usarla.                                           |
| Validación      | Obliga a una comprobación explícita: supuestos, huecos, contraejemplos o tests de refutación. | …entrega todo con la misma confianza, sin distinguir lo que sabe de lo que asumió, y el error aparece en producción. |

> Un prompt sin sección de validación no produce respuestas peores. Produce respuestas igual de buenas y mucho más difíciles de auditar.

Para ingenieros

Estos prompts se versionan. Van en el repositorio, en `prompts/` o dentro de una Skill de Claude Code, y se revisan en el PR como cualquier otro artefacto.

Cuando un prompt falla, el arreglo casi nunca está en el objetivo: está en Contexto, Restricciones o Validación.
