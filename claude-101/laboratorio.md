# Laboratorio final

Parte III

## Laboratorio final

45 minutos para que cada equipo construya y entregue el MVP de un producto real usando IA con criterio de ingeniería, no como atajo.

### El reto

Equipos de 3 o 4 personas. Ni 2 ni 5.

Construyan el MVP de un producto que resuelva un problema real de estudiantes universitarios. No un problema imaginado: uno que alguien del equipo haya sufrido este semestre.

> Si no pueden nombrar a una persona concreta que tiene el problema, todavía no tienen problema.

Dominios posibles:

- Educación y aprendizaje
- Transporte y movilidad al campus
- Finanzas personales de estudiante
- Organización académica
- Vida universitaria
- Productividad
- Eventos
- Deportes
- Empleo y prácticas

Requisito no negociable: la IA se usa de forma significativa, en al menos una de estas formas.

IA en el producto

El producto usa un modelo en tiempo de ejecución: clasifica, extrae, resume, responde, recomienda. La IA es parte de la funcionalidad.

IA en el proceso

Claude y Claude Code participan en discovery, definición, diseño técnico, código, tests y revisión. La IA es parte de cómo se construyó.

Ambas

Lo esperable en un equipo que aprovechó las tres horas. No suma puntos por sí sola: suma si está evidenciada.

CampusFlow no se puede entregar

CampusFlow es el caso trabajado en clase. Ya vimos su problema, su MVP, su arquitectura, su bug y sus tests. Entregarlo sería entregar lo que ya les dimos resuelto.

Úsenlo como referencia de *formato*: así se ve un problem statement, así se ve una user story con criterios de aceptación, así se ve un diseño técnico. Copiar el dominio, las entidades o el stack tal cual es entregar una plantilla rellenada, y se califica como tal.

### Cronograma minuto a minuto

45 minutos exactos. El reloj corre en la pantalla. Cada fase termine o no termine.

| Min   | Fase                                         | Duración | Qué debe existir al terminar                                                                                           |
|-------|----------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------|
| 00–05 | Formación de equipos y elección del problema | 5        | Equipo armado, roles repartidos, un problema elegido en una frase. Nada de debatir tres ideas.                         |
| 05–12 | Discovery con Claude                         | 7        | Problem statement y user persona. Al menos una iteración: primer output de Claude, crítica del equipo, segundo output. |
| 12–19 | Definición de MVP y user stories             | 7        | MVP con lo que queda fuera explícito. Entre 3 y 5 user stories con criterios de aceptación.                            |
| 19–24 | Diseño técnico                               | 5        | Stack elegido, endpoints o módulos principales, modelo de datos mínimo, dónde entra la IA.                             |
| 24–39 | Construcción con Claude Code                 | 15       | Código que corre. Commits pequeños. Diffs revisados, no aceptados a ciegas.                                            |
| 39–43 | Tests y revisión                             | 4        | Al menos 3 tests, uno de ellos de caso borde. Un bug encontrado y documentado.                                         |
| 43–45 | Entrega y reflexión                          | 2        | README, carpeta `docs/` completa, reflexión escrita, repo empujado.                                                    |
|       | **Total**                                    | **45**   |                                                                                                                        |

Reparto de roles sugerido dentro del equipo, para no bloquearse todos en la misma pantalla:

- **Product**: conduce el discovery y escribe `docs/`. No toca el código.
- **Builder**: maneja Claude Code, hace commits, revisa diffs.
- **Verifier**: escribe y corre tests, busca el caso borde, cuestiona lo generado.
- Si son 4, el cuarto es **Evidence**: guarda prompts, iteraciones y decisiones mientras los demás avanzan.

### Checkpoints

Hay tres cortes de revisión durante el laboratorio. No son acompañamiento: son evaluación formativa. Lo que responda el equipo en cada corte anticipa dónde va a terminar.

| Checkpoint     | Minuto | Qué se pregunta                                                                                                                           | Señal de alarma                                                                       |
|----------------|--------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| CP1 — Problema | ~12    | ¿Quién es la persona que tiene este problema y cómo lo resuelve hoy sin ustedes? ¿Qué queda fuera del MVP?                             | El usuario es "los estudiantes" en general. No hay nada fuera de alcance.             |
| CP2 — Diseño   | ~24    | Muéstrenme el diseño técnico y díganme por qué eligieron eso. ¿Qué propuso Claude que ustedes descartaron?                             | El diseño es exactamente lo que salió del primer prompt y nadie lo cuestionó.         |
| CP3 — Código   | ~39    | Se señala una función del repo y alguien al azar la explica línea por línea. ¿Qué test escribieron y qué caso borde cubre? | Nadie sabe qué hace esa función. Los tests son los que generó Claude y no se leyeron. |

### Los 10 entregables

Diez artefactos. Cortos, específicos, verificables. No se evalúan páginas: se evalúan decisiones.

1.  1 — Problem statement

    Un párrafo. Qué duele, a quién, con qué frecuencia y cómo lo resuelve hoy. Sin la palabra "innovador".

    

    Plantilla

        [Usuario] necesita [capacidad] porque [causa concreta].
        Hoy lo resuelve con [alternativa actual], que falla en [limitación].
        Esto pasa [frecuencia] y le cuesta [tiempo / dinero / nota / estrés].

    

2.  2 — User persona

    Una sola persona, con nombre, semestre y contexto. No un segmento demográfico.

    

    Plantilla

        Nombre, semestre, carrera.
        Contexto: un día típico en una frase.
        Herramientas que ya usa.
        Dolor principal (uno).
        Qué haría que dejara de usar nuestra solución.

    

3.  3 — MVP con alcance explícito

    Tres a cinco funcionalidades dentro. Y una lista igual de larga de lo que queda fuera. El "fuera" es lo que se califica: define si el equipo entendió qué es un MVP.

    

    | Dentro de v0 | Fuera de v0 | Por qué fuera |
    |--------------|-------------|---------------|
    | …            | …           | …             |

    

4.  4 — User stories con criterios de aceptación

    Entre 3 y 5. Cada criterio tiene que poder convertirse en un test. Si no se puede testear, está mal escrito.

    

    Plantilla

        US-01 — Como [persona] quiero [acción] para [beneficio].

        Criterios de aceptación
        - Dado [estado inicial], cuando [acción], entonces [resultado observable].
        - Dado [caso borde], cuando [acción], entonces [comportamiento esperado].
        - Error: dado [entrada inválida], el sistema responde [código / mensaje].

    

5.  5 — Arquitectura

    Un diagrama o una lista de componentes con sus responsabilidades, el stack elegido, el modelo de datos mínimo y dónde entra el modelo de IA (si entra en runtime). Digan qué decisión tomaron y qué alternativa descartaron.

    

    ClienteAPIServicioModelo / IADatos

    

6.  6 — Código funcional

    Corre con un comando documentado. No tiene que estar completo: tiene que estar vivo. Un repo que no arranca no se evalúa como código, se evalúa como intención.

    Commits pequeños y con mensaje. Un único commit gigante llamado "MVP" es una señal, y no buena.

7.  7 — Tests

    Mínimo 3. Al menos uno de caso borde: lista vacía, fecha límite hoy, entrada inválida, zona horaria, permiso ausente. Los tests que solo verifican el happy path no cuentan como verificación.

8.  8 — README

    Qué es, para quién, cómo se instala, cómo se corre, cómo se corren los tests, qué NO hace todavía. Esa última sección es obligatoria.

9.  9 — Evidencia de uso de Claude

    Este es el entregable que más equipos hacen mal. No es "usamos Claude". Es el rastro de cómo pensaron con la herramienta.

    Cuenta como evidencia:

    - **Historial de prompts con sus iteraciones**: prompt v1, qué salió mal, prompt v2, qué mejoró. Mínimo dos cadenas de iteración reales.
    - **Diffs revisados**: al menos un diff generado por Claude Code con el comentario del equipo sobre qué aceptaron, qué modificaron y por qué.
    - **Decisiones tomadas en contra de lo que sugirió Claude**: qué propuso, qué hicieron ustedes, con qué argumento. Mínimo una.
    - **Bugs encontrados en código generado**: qué estaba mal, cómo lo detectaron (test, lectura, ejecución) y cómo lo arreglaron. Mínimo uno.

    No cuenta como evidencia: capturas de pantalla sueltas sin contexto, un pegado del chat completo sin anotar, "le pedimos que hiciera la API y funcionó".

10. 10 — Reflexión

    Media página. Pregunta obligatoria, respondida de forma explícita:

    ¿Qué hizo Claude y qué decisiones tomó el equipo?

    Separen las dos columnas de verdad. Si toda la columna de "el equipo" dice "revisamos", la nota lo va a reflejar.

### Estructura de la entrega

``` code
<nombre-del-proyecto>/
├── README.md                     # entregable 8
├── docs/
│   ├── 01-problem-statement.md   # entregable 1
│   ├── 02-persona.md             # entregable 2
│   ├── 03-mvp.md                 # entregable 3 (dentro / fuera)
│   ├── 04-user-stories.md        # entregable 4
│   ├── 05-arquitectura.md        # entregable 5 (+ diagrama)
│   └── 10-reflexion.md           # entregable 10
├── ai-evidence/                  # entregable 9
│   ├── prompts.md                # iteraciones: v1 → crítica → v2
│   ├── diffs-revisados.md        # diffs + comentario del equipo
│   ├── decisiones-contra-claude.md
│   └── bugs-encontrados.md
├── src/                          # entregable 6
├── tests/                        # entregable 7
└── requirements.txt | package.json
```

Un repositorio de Git, con historial. Enlace en el formulario de entrega antes del minuto 45.

### La regla anti "Claude, hazme la app"

> Un proyecto generado completamente por IA, que funciona, pero que el equipo no entiende, tiene calificación baja. Que funcione no es la meta: la meta es responder por él.

Seamos precisos, porque esta regla se malinterpreta en las dos direcciones.

No es la falta

- Que Claude haya escrito el 100% del código.
- Que hayan usado Claude Code para toda la construcción.
- Que los tests los haya generado el modelo.
- Que la arquitectura haya salido de una conversación.

Sí es la falta

- Entregar código que nadie del equipo leyó.
- No poder explicar por qué el diseño es así.
- No haber verificado nada: ni corrido, ni testeado, ni cuestionado.
- No tener una sola decisión propia en todo el proyecto.

Delegar es legítimo. Delegar sin revisar es abdicar. El ingeniero responde por el resultado, no por quién tecleó.

### Cómo se detecta en la sustentación

La sustentación no es una presentación. Son cinco minutos de preguntas dirigidas, y funciona así:

1.  Elijo **un integrante al azar**, no al que más habla.
2.  Se abre el repo y se señala **una función específica**. Hay que explicarla: qué recibe, qué devuelve, qué pasa si la entrada está vacía.
3.  Le pido que **justifique una decisión de diseño**: por qué ese modelo de datos, por qué ese endpoint, por qué ese proveedor.
4.  Le pido que **modifique algo en vivo**: un cambio pequeño, con el equipo mirando, en menos de tres minutos.

Tres preguntas de ejemplo, para que sepan a qué se enfrentan:

| Pregunta                                                                                    | Qué estoy midiendo                                                           |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| "Explíqueme esta función línea por línea y dígame qué devuelve si le paso una lista vacía." | Si leyeron el código o solo lo aceptaron.                                    |
| "¿Por qué guardaron esto en esta tabla y no en la otra? ¿Qué se rompe si lo mueven?"        | Si hay un modelo mental del diseño o solo un output.                         |
| "Agregue ahora un campo opcional a este endpoint y haga que el test siga pasando."          | Si pueden operar sobre su propio sistema sin volver a pedirle todo a Claude. |

Tope de nota

Si el equipo no puede explicar lo que entregó, el criterio de comprensión cae a Insuficiente y la nota final del proyecto se topa en 3.0 sobre 5.0, sin importar cuán pulido esté el resto. La comprensión no es un criterio más: es la condición para que los demás cuenten.

### Rúbrica

Siete criterios, 100%. Los descriptores son operativos: describen lo que veo en el repo y en la sustentación, no adjetivos.

| Criterio                               | Peso     | Insuficiente (0–2.4)                                                                                                                                                                                 | Aceptable (2.5–3.4)                                                                                     | Bueno (3.5–4.2)                                                                                                      | Excelente (4.3–5.0)                                                                                                                                |
|----------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Problema y usuario                     | 15%      | Problema genérico. El usuario es "los estudiantes". No hay alternativa actual descrita.                                                                                                              | Problema identificable pero amplio. Persona plana, sin dolor concreto.                                  | Problema concreto con persona nombrada, dolor claro y alternativa actual.                                            | Problema afilado, persona creíble con contexto real, alternativa actual descrita y por qué falla. Se nota que hablaron con alguien o lo vivieron.  |
| Definición de MVP y alcance            | 10%      | No hay MVP: hay una lista de deseos. Nada fuera de alcance.                                                                                                                                          | MVP declarado pero sobredimensionado para 45 minutos. "Fuera" superficial.                              | MVP acotado, con lista explícita de lo que queda fuera y coherencia con el problema.                                 | MVP mínimo de verdad, con exclusiones argumentadas. Cada funcionalidad se rastrea a un dolor de la persona.                                        |
| Diseño técnico                         | 15%      | No hay diseño, o es el primer output de Claude sin revisar. Sin modelo de datos.                                                                                                                     | Componentes y stack listados, sin justificación ni alternativas.                                        | Arquitectura coherente, modelo de datos mínimo, decisiones justificadas.                                             | Diseño defendible: trade-offs explícitos, alternativa descartada con argumento, límites del sistema declarados y ubicación clara de la IA.         |
| Código funcional                       | 15%      | No arranca, o no existe. Un solo commit.                                                                                                                                                             | Arranca con ayuda. Cubre una parte del MVP. Historial pobre.                                            | Corre con el comando documentado y cubre el núcleo del MVP. Commits razonables.                                      | Corre limpio, cubre el MVP declarado, estructura clara, historial de commits pequeños y legibles.                                                  |
| Tests y verificación                   | 15%      | Sin tests, o tests que no corren. Nada verificado.                                                                                                                                                   | Tests de happy path únicamente. No se probó ningún caso borde.                                          | Tres o más tests, al menos uno de caso borde, todos pasan.                                                           | Tests derivados de los criterios de aceptación, casos borde deliberados, y al menos un bug real encontrado y corregido con su test de regresión.   |
| Uso de IA con evidencia de iteración   | 20%      | Sin evidencia, o capturas sueltas. Un prompt, un output, entregado.                                                                                                                                  | Prompts guardados pero sin iteración ni crítica. No hay diffs comentados.                               | Dos cadenas de iteración documentadas, diffs revisados con comentario, al menos un bug detectado en código generado. | Todo lo anterior más decisiones tomadas contra la sugerencia de Claude, argumentadas. Se ve un equipo dirigiendo la herramienta, no obedeciéndola. |
| Comprensión demostrada en sustentación | 10%      | **"Funciona pero el equipo no lo entiende" cae aquí.** El integrante al azar no explica la función, no justifica el diseño o no logra el cambio en vivo. **Topa la nota final del proyecto en 3.0.** | Explica a grandes rasgos. Duda en el porqué. El cambio en vivo requiere volver a pedirle todo a Claude. | Cualquier integrante explica su parte y justifica las decisiones principales. El cambio en vivo sale.                | Todo el equipo responde con precisión, reconoce los límites de lo que construyeron y modifica el sistema en vivo sin fricción.                     |
| **Total**                              | **100%** |                                                                                                                                                                                                      |                                                                                                         |                                                                                                                      |                                                                                                                                                    |

Regla de tope, otra vez

Un proyecto puede sacar Excelente en código, tests y evidencia, y aun así cerrar en 3.0 si la comprensión queda en Insuficiente. Es intencional. Entregar lo que no se entiende es el único error que esta clase no perdona.

### Tres niveles de challenge

El proyecto base es el mismo para todos. El nivel es el reto adicional que cada equipo elige según lo que ya sabe hacer. Elijan al minuto 0 y no cambien: subir de nivel a mitad de camino es cómo se pierde el laboratorio.

| Nivel               | Herramientas                        | Debe demostrar                                                                                                                   | Reto adicional                                                                                                                                                                                                                            | Evidencia                                                                                                               | Bono |
|---------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|------|
| **1 — Beginner**    | Prompting + Claude (chat o Project) | Que sabe convertir una conversación en especificación. Contexto, requisitos y restricciones explícitos; iteración deliberada.    | Llevar un mismo requisito de nivel 1 a nivel 3: tres versiones del prompt, cada una con la crítica que motivó la siguiente, y una tabla comparando los tres outputs contra los criterios de aceptación.                                   | `ai-evidence/prompts.md` con las tres versiones, las críticas y la tabla comparativa.                                   | +5%  |
| **2 — Engineer**    | Claude Code + Git + testing         | Que trabaja sobre el repositorio, no sobre la conversación. Commits, ramas, diffs revisados, tests que fallan antes de arreglar. | Ciclo completo de bug: escribir un test que falle sobre un caso borde real, dejar que Claude Code proponga el arreglo, rechazar o modificar al menos una parte del diff, y cerrar con el test en verde en una rama con PR o merge commit. | Historial de Git con el commit rojo y el commit verde, el diff con los comentarios de rechazo, y `bugs-encontrados.md`. | +8%  |
| **3 — AI Engineer** | RAG + MCP + agente                  | Que entiende retrieval, tool use y el ciclo de un agente. Y que sabe cuándo no hace falta.                                       | Elegir **una** de las dos opciones de abajo. Una sola, bien hecha.                                                                                                                                                                        | Ver detalle en las opciones.                                                                                            | +12% |

Nivel 3 — Opción A: endpoint de preguntas sobre 3 documentos

Un endpoint `POST /ask` que responda preguntas sobre tres documentos del proyecto (syllabus, reglamento, notas de clase, lo que aplique a su dominio).

3 documentosChunking simpleEmbeddingsBúsqueda top-kClaudeRespuesta + fuente

Retrieval simple es suficiente: chunks de tamaño fijo, embeddings de un proveedor externo (Anthropic no ofrece modelo de embeddings propio), similitud coseno en memoria o en pgvector. Nada de reranking, nada de híbrido.

Requisito de calidad: la respuesta debe citar de qué documento y de qué fragmento salió. Y deben tener una pregunta de prueba cuya respuesta *no* está en los documentos, para mostrar qué hace el sistema cuando no sabe.

**Evidencia**: el endpoint corriendo, un test con la pregunta respondible y otro con la no respondible, y media página sobre por qué RAG y no meter los tres documentos completos en el context window.

Nivel 3 — Opción B: servidor MCP conectado y usado

Conectar un servidor MCP existente a Claude Code y usarlo dentro del flujo del proyecto. No construyan un servidor desde cero: en 45 minutos no da.

``` code
claude mcp add --transport http <nombre> <url-del-servidor>
claude mcp list
# dentro de la sesión:
/mcp
```

Registro en `.mcp.json` versionado en el repo, para que todo el equipo tenga la misma configuración.

**Evidencia**: el `.mcp.json`, la transcripción de una tarea real resuelta con al menos una tool del servidor, qué tools expone y para qué sirvieron, y un párrafo sobre el riesgo de prompt injection de ese servidor concreto y qué credenciales le dieron.

El bono se gana, no se declara

El bono solo aplica si el proyecto base está completo. Un nivel 3 brillante sobre un MVP sin tests y sin README no suma nada: suma sobre algo que ya está bien. Y si el reto adicional no tiene evidencia verificable en el repo, no existe.

### Qué necesita cada equipo antes de empezar

Revisen esto ahora, no al minuto 3. Un equipo instalando dependencias durante el laboratorio ya perdió una fase completa.

| Requisito                                             | Cómo verificar                                     | Quién lo necesita     |
|-------------------------------------------------------|----------------------------------------------------|-----------------------|
| Cuenta de Claude activa                               | Sesión abierta en claude.ai                        | Todos                 |
| Claude Code instalado y autenticado                   | `claude --version` y luego `cd proyecto && claude` | Al menos el Builder   |
| Repositorio de Git creado y con acceso para el equipo | Los 3 o 4 pueden hacer `push`                      | Todos                 |
| Python 3.12 o Node LTS instalado                      | `python --version` / `node --version`              | Builder y Verifier    |
| Framework de tests listo                              | `pytest --version` o `npm test` corriendo en vacío | Verifier              |
| API key del proveedor de embeddings                   | Una llamada de prueba responde                     | Solo nivel 3 opción A |
| Carpeta `docs/` y `ai-evidence/` creadas              | Existen en el primer commit                        | Product y Evidence    |

Instalación del CLI, si les falta:

``` code
# macOS / Linux / WSL
curl -fsSL https://claude.ai/install.sh | bash

# PowerShell
irm https://claude.ai/install.ps1 | iex

# alternativas
brew install --cask claude-code
winget install Anthropic.ClaudeCode
```

Plan B si no tienen plan pago

No todos van a tener Claude Code disponible. No es excusa para no entregar, y no penaliza la nota.

- Trabajen en el chat web: discovery, MVP, user stories, diseño técnico y generación de código funcionan ahí igual de bien.
- Copien el código al repo a mano y hagan los commits ustedes. Commits pequeños de todos modos.
- La evidencia se vuelve más importante, no menos: peguen los prompts completos y sus iteraciones en `ai-evidence/prompts.md`, y anoten qué cambiaron ustedes al pegar el código.
- En vez de diffs de Claude Code, documenten un "diff manual": qué generó el chat, qué quedó en el repo, qué modificaron y por qué.
- Para el nivel 2, el ciclo de bug se demuestra igual con Git: commit del test que falla, commit del arreglo.

Asegúrense de que al menos una persona del equipo tenga Claude Code si van a intentar nivel 2 o 3. Repártanse el equipo en función de eso.

> En 45 minutos nadie construye un producto terminado. Lo que sí se construye es la evidencia de que saben dirigir el trabajo, revisarlo y responder por él.
