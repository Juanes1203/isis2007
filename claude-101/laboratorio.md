# Guía de trabajo

### Antes de abrir cualquier herramienta

Pónganse de acuerdo en una sola frase:

> Nuestro producto le permite a \_\_\_ hacer \_\_\_ para que \_\_\_.

Si no les sale, ese es el trabajo de hoy.

### Por dónde seguir

#### Afinar el problema y el usuario

¿Su usuario sigue siendo "los estudiantes"? Toca afinarlo. Lo mismo si no saben qué hace esa persona hoy para resolver el problema sin ustedes.

Pídanle al modelo que haga de investigador: que proponga usuarios posibles, que diga qué está asumiendo y qué podría salir mal.

Ya está cuando pueden decir el nombre de una persona, cada cuánto le pasa esto y qué hace hoy en su lugar. Ojo con una cosa: el modelo propone hipótesis, no las comprueba. Eso toca hablando con gente.

#### Recortar el MVP

Si la lista pasa de cinco funcionalidades, o si no dejaron nada por fuera, falta recortar.

Pídanle que ordene por valor contra esfuerzo y que proponga el corte más chiquito que ya resuelve el problema. Que justifique cada cosa que saca.

Lo que dejaron por fuera es lo que muestra que decidieron:

| Entra en v0                                | Queda fuera                        | Por qué                                           |
|--------------------------------------------|------------------------------------|---------------------------------------------------|
| La capacidad que resuelve el dolor central | Todo lo que sea "y además…"        | Sin esto el producto no existe                    |
| El flujo mínimo de punta a punta           | Perfiles, ajustes, personalización | No cambian si la hipótesis resulta cierta o falsa |

#### User stories y criterios de aceptación

Esto va antes de programar. Sin criterios no tienen contra qué comparar lo que salga generado.

Pidan que cada capacidad del MVP quede como historia con criterios en Dado / Cuando / Entonces, y que agregue los casos raros que ustedes no pensaron.

Cada historia necesita al menos un criterio que pueda fallar. "El sistema funciona correctamente" no sirve.

Plantilla de historia

    Como {{TIPO_DE_USUARIO}}
    quiero {{CAPACIDAD}}
    para {{RESULTADO}}

    Criterios de aceptación
    - Dado {{CONTEXTO}}, cuando {{ACCIÓN}}, entonces {{RESULTADO OBSERVABLE}}
    - Caso borde: dado {{SITUACIÓN RARA}}, entonces {{COMPORTAMIENTO ESPERADO}}

#### Diseño técnico

Ya saben qué construir pero no cómo. O cada uno tiene un stack distinto en la cabeza.

Pidan dos o tres arquitecturas con sus contras, no una. Con una sola no hay contra qué compararla. Ustedes escogen y escriben por qué.

Ya está cuando tienen el stack cerrado, las entidades y los endpoints o pantallas del MVP. Guarden también una decisión donde le llevaron la contraria al modelo, con la razón.

Para ingenieros

Hay decisiones que no las cierra un modelo solo. El modelo de datos que define el negocio, los límites de consistencia, qué guardan de los usuarios y por cuánto tiempo, y cualquier cosa que cueste plata. Esas se hablan en equipo y quedan escritas.

#### Construir con un agente de código

Ya tienen repositorio y algo que implementar. El orden que sirve es este: escriban el archivo de instrucciones del repo antes de pedir nada, trabajen en rama, pidan cambios chiquitos, lean el diff, corran los tests, hagan commit. Y otra vez.

Ese archivo se llama `CLAUDE.md` en Claude Code. Otros agentes leen el suyo con otro nombre y el contenido es igual:

Archivo de instrucciones mínimo

    # {{NOMBRE DEL PROYECTO}}

    Qué es: {{UNA FRASE}}
    Stack: {{LENGUAJE, FRAMEWORK, BASE DE DATOS}}

    Comandos
    - Tests: {{COMANDO}}
    - Correr en local: {{COMANDO}}

    Estándares
    - {{CONVENCIÓN DE NOMBRES, ESTILO, ESTRUCTURA DE CARPETAS}}
    - Nada de SQL construido por concatenación de strings.
    - Ningún secreto en el código: van en variables de entorno.

    Qué no tocar
    - {{ARCHIVOS O CARPETAS QUE NO SE MODIFICAN}}

    Antes de dar algo por terminado
    - Los tests pasan y hay al menos un caso borde cubierto.
    - El diff se revisó línea por línea.

Ya está cuando el código corre y cualquiera del equipo puede explicar la función que acaba de entrar.

#### Verificar

Es lo que todo el mundo se salta y lo que más pesa en la nota.

Con los tests, pidan los casos raros de una vez. El happy path lo saca cualquiera.

Con el diff, miren si tocó archivos que no tenía que tocar, si metió dependencias nuevas, si dejó alguna llave por ahí, y si los tests pasan porque les bajaron la exigencia.

Y revisen lo de siempre en seguridad: consultas parametrizadas, validación de lo que entra, cero llaves en el repositorio.

> Nunca hagan merge de un diff que no entienden.

### Evidencia de uso de IA

Vayan guardando esto en una carpeta `ai-evidence/` mientras trabajan. Dejarlo para el final nunca funciona, y es de lo que más pesa en la nota.

| Qué guardar                            | Mínimo                                               | Qué demuestra                           |
|----------------------------------------|------------------------------------------------------|-----------------------------------------|
| Cadenas de iteración                   | Dos: prompt inicial, qué salió mal, prompt corregido | Que saben diagnosticar por qué falló    |
| Un diff comentado                      | Uno, con sus notas de revisión                       | Que leyeron lo que entró al repositorio |
| Una decisión en contra del modelo      | Una, con la razón                                    | Que hay criterio propio                 |
| Un error encontrado en código generado | Uno, con cómo lo detectaron                          | Que verifican en vez de confiar         |

Y al final contesten en un párrafo:

¿Qué hizo la IA y qué decisiones tomó el equipo?

### La sustentación

Se escoge a alguien del equipo al azar y se le pide que explique una función, que defienda una decisión de diseño o que haga un cambio ahí mismo. Las preguntas suelen ser de este estilo:

1.  Expliquen esta función: qué recibe, qué devuelve, qué pasa si le llega vacío.
2.  ¿Por qué eligieron este diseño? ¿Qué propuso el modelo que descartaron?
3.  Agreguen aquí un caso borde y háganlo pasar.

No penaliza

- Que la IA haya escrito el 100% del código.
- Que la arquitectura la haya propuesto el modelo y ustedes la hayan adoptado.
- Usar IA en todas las etapas.

Sí penaliza

- Entregar código que el equipo no puede explicar.
- No haber verificado nada de lo generado.
- Cero decisiones propias en todo el proyecto.
- Tests que solo cubren el happy path.

### Criterios de evaluación

Para que sepan dónde poner el esfuerzo. Los pesos exactos los pone el curso.

| Criterio                | Insuficiente                                       | Bueno                                      | Excelente                                                            |
|-------------------------|----------------------------------------------------|--------------------------------------------|----------------------------------------------------------------------|
| Problema y usuario      | Usuario genérico, problema sin evidencia           | Persona concreta con su alternativa actual | Además, hipótesis explícitas y una contrastada con alguien real      |
| Alcance del MVP         | Todo entra, nada queda fuera                       | Corte definido con lo que no entra         | Cada exclusión tiene razón y se sostiene bajo preguntas              |
| Diseño técnico          | Salió del primer prompt, sin comparar alternativas | Stack y entidades justificados             | Alternativas comparadas y decisión documentada                       |
| Código y tests          | Corre a veces; tests ausentes o solo happy path    | Corre; tests con algún caso borde          | Corre; casos borde escritos por el equipo y un error real encontrado |
| Uso de IA con evidencia | Prompts sueltos o ninguno                          | Iteraciones documentadas                   | Iteraciones, diffs revisados y decisiones propias                    |
| Comprensión             | El equipo no puede explicar lo entregado           | El equipo explica lo esencial              | Cualquiera explica cualquier parte y la modifica en vivo             |

### Si quieren ir más allá

Tres retos extra, según qué tan lejos quieran llevarlo. Van encima del proyecto, no en vez de.

Prompting

Trabajan con un modelo en el chat.

**Reto:** armen el espacio de trabajo de su producto con su propio contexto (brief, requisitos, decisiones técnicas) y muestren la misma pregunta respondida con y sin ese contexto.

Con un agente de código

Trabajan con un agente de código sobre su repositorio.

**Reto:** archivo de instrucciones propio, una feature implementada en rama con su test de caso borde, y el diff revisado con comentarios antes del merge.

Con IA dentro del producto

La IA es parte del producto.

**Reto:** un endpoint que responda preguntas sobre tres documentos propios citando la fuente y respondiendo "no está en los documentos" cuando no esté. O conecten un servidor MCP existente a su flujo y dejen evidencia.

### Checklist previo

| Qué                    | Cómo                                                                              |
|------------------------|-----------------------------------------------------------------------------------|
| Repositorio del equipo | Creado, con todos con acceso y una rama por persona                               |
| Un agente de código    | Claude Code si tienen plan pago. Si no, revisen la guía de herramientas gratuitas |
| Carpeta de evidencia   | `ai-evidence/` desde el primer commit                                             |

En la biblioteca hay 26 prompts por rol y sirven con cualquier modelo. Busquen el que corresponde a lo que están haciendo y cambien los marcadores por los datos de su producto.
