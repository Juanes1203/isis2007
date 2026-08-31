# Guía de trabajo

### De dónde parten

Cada equipo llega con un proyecto ya elegido. Eso cambia el ejercicio: no se trata de inventar un producto en 45 minutos, sino de **avanzarlo con criterio de ingeniería** apoyándose en IA.

Lo que hicimos con CampusFlow durante la clase — problema, usuario, MVP, historias, diseño técnico, código, tests — es exactamente lo que van a hacer con su propia idea. La diferencia es que CampusFlow era un ejemplo y esto es su proyecto.

Antes de abrir Claude

Pónganse de acuerdo en una frase: *"nuestro producto le permite a \_\_\_ hacer \_\_\_ para que \_\_\_"*. Si el equipo no la puede decir sin discutir, ese es el primer frente de trabajo, no el código.

### Los seis frentes

Escojan dónde está su proyecto hoy y avancen desde ahí. Muchos equipos van a necesitar el frente 1 aunque crean que ya lo tienen resuelto.

1.  Afilar el problema y el usuario

    **Les sirve si** su usuario es "los estudiantes" en general, o si no saben cómo resuelve hoy ese problema sin ustedes.

    **Qué pedirle a Claude:** que actúe como product researcher, que a partir de su descripción liste usuarios candidatos, hipótesis y riesgos, y que marque explícitamente qué está asumiendo.

    **Cómo saben que quedó:** pueden nombrar una persona concreta, con qué frecuencia le pasa el problema y qué usa hoy en su lugar. Y tienen escrita al menos una hipótesis que podría resultar falsa.

    

    Cuidado

    Claude genera hipótesis, no las valida. Una hipótesis solo se valida hablando con usuarios reales. Si el entregable dice "validamos con Claude", eso no es validación.

    

2.  Recortar el MVP

    **Les sirve si** su lista de funcionalidades tiene más de cinco cosas, o si no hay nada explícitamente fuera de alcance.

    **Qué pedirle a Claude:** que ordene las funcionalidades por valor para el usuario contra esfuerzo, que proponga el corte mínimo que ya resuelve el problema, y que justifique cada exclusión.

    **Cómo saben que quedó:** tienen una tabla de lo que entra y lo que *no* entra en v0. La segunda columna es la que demuestra que hubo decisión.

    

    | Entra en v0                                | Queda fuera                        | Por qué                                      |
    |--------------------------------------------|------------------------------------|----------------------------------------------|
    | La capacidad que resuelve el dolor central | Todo lo que sea "y además…"        | Sin esto el producto no existe               |
    | El flujo mínimo de punta a punta           | Perfiles, ajustes, personalización | No cambian si la hipótesis es cierta o falsa |

    

3.  User stories y criterios de aceptación

    **Les sirve si** van a empezar a programar. Sin criterios de aceptación no pueden evaluar lo que Claude genere.

    **Qué pedirle a Claude:** que convierta cada capacidad del MVP en historias con criterios en formato Dado / Cuando / Entonces, y que agregue los casos borde que ustedes no pensaron.

    **Cómo saben que quedó:** cada historia tiene al menos un criterio que puede fallar. "El sistema funciona correctamente" no es un criterio.

    

    Plantilla de historia

        Como {{TIPO_DE_USUARIO}}
        quiero {{CAPACIDAD}}
        para {{RESULTADO}}

        Criterios de aceptación
        - Dado {{CONTEXTO}}, cuando {{ACCIÓN}}, entonces {{RESULTADO OBSERVABLE}}
        - Caso borde: dado {{SITUACIÓN RARA}}, entonces {{COMPORTAMIENTO ESPERADO}}

    

4.  Diseño técnico

    **Les sirve si** ya saben qué construir pero no cómo, o si cada integrante tiene un stack distinto en la cabeza.

    **Qué pedirle a Claude:** que proponga dos o tres arquitecturas alternativas para su caso con sus contras, no una sola. Ustedes eligen y escriben por qué.

    **Cómo saben que quedó:** tienen el stack cerrado, las entidades principales y los endpoints o pantallas del MVP. Y una decisión que tomaron *en contra* de lo que Claude propuso, con su razón.

    

    Para ingenieros

    Hay decisiones que un modelo no debería cerrar solo: el modelo de datos que define el negocio, los límites de consistencia, qué se guarda de los usuarios y por cuánto tiempo, y cualquier cosa que cueste plata. Esas se discuten en el equipo y se dejan escritas.

    

5.  Construir con Claude Code

    **Les sirve si** ya tienen repositorio y algo que implementar.

    **El orden que funciona:** escribir un `CLAUDE.md` corto antes del primer prompt, trabajar en rama, pedir cambios pequeños, leer el diff, correr los tests, hacer commit. Repetir.

    

    CLAUDE.md mínimo para su repo

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

    

    **Cómo saben que quedó:** el código corre, y cualquier integrante puede explicar qué hace la función que acaba de entrar.

6.  Verificar

    **Les sirve siempre.** Es el frente que más se salta y el que más pesa en la evaluación.

    - **Tests:** pidan explícitamente los casos borde. El happy path lo escribe cualquiera.
    - **Diff:** revisen alcance inesperado, archivos que no debía tocar, dependencias nuevas, secretos, y tests que "pasan" porque bajaron la exigencia.
    - **Seguridad:** consultas parametrizadas, validación de entradas, nada de llaves en el repositorio.

    > Nunca hagan merge de un diff que no entienden.

### Evidencia de uso de IA

Esto no es burocracia: es la parte que más pesa, porque es donde se ve si el equipo pensó o solo pegó.

Guarden en una carpeta `ai-evidence/` mientras trabajan, no al final:

| Qué guardar                            | Mínimo                                                     | Qué demuestra                                            |
|----------------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| Cadenas de iteración                   | Dos casos: prompt inicial, qué salió mal, prompt corregido | Que saben diagnosticar por qué falló, no solo reintentar |
| Un diff comentado                      | Uno, con sus notas de revisión                             | Que leyeron lo que entró al repositorio                  |
| Una decisión en contra de Claude       | Una, con la razón                                          | Que hay criterio propio                                  |
| Un error encontrado en código generado | Uno, con cómo lo detectaron                                | Que verifican en vez de confiar                          |

¿Qué hizo Claude y qué decisiones tomó el equipo?

Esa pregunta se responde en un párrafo al final. Si la respuesta es "Claude hizo todo", falta trabajo.

### La regla

Esto NO es falta

- Que Claude haya escrito el 100% del código.
- Que la arquitectura la haya propuesto Claude y ustedes la hayan adoptado.
- Usar IA en todas las etapas del proyecto.

Esto sí

- Entregar código que nadie en el equipo puede explicar.
- No haber verificado nada de lo que se generó.
- No tener una sola decisión propia en todo el proyecto.
- Tests que solo cubren el happy path porque nadie los leyó.

En la sustentación se le pide a un integrante al azar que explique una función específica, que justifique una decisión de diseño, o que haga un cambio pequeño en vivo. Tres preguntas típicas:

1.  Señalen esta función y explíquenla: qué recibe, qué devuelve, qué pasa si le llega vacío.
2.  ¿Por qué eligieron este diseño y no el otro? ¿Qué propuso Claude que descartaron?
3.  Agreguen aquí un caso borde y háganlo pasar.

> Usar IA para todo el código no es la falta. La falta es no entender lo que entregaron.

### Criterios de evaluación

Referencia de en qué se fija la evaluación del proyecto. Los pesos exactos los define el curso; lo que importa aquí es dónde poner el esfuerzo.

| Criterio                | Insuficiente                                      | Bueno                                      | Excelente                                                                |
|-------------------------|---------------------------------------------------|--------------------------------------------|--------------------------------------------------------------------------|
| Problema y usuario      | Usuario genérico, problema sin evidencia          | Persona concreta con su alternativa actual | Además, hipótesis explícitas y al menos una contrastada con alguien real |
| Alcance del MVP         | Todo entra, nada queda fuera                      | Corte definido con lo que no entra         | Cada exclusión tiene razón y se sostiene bajo preguntas                  |
| Diseño técnico          | Es lo que salió del primer prompt, sin cuestionar | Stack y entidades justificados             | Se compararon alternativas y se documentó la decisión                    |
| Código y tests          | Corre a veces; tests ausentes o solo happy path   | Corre; tests con algún caso borde          | Corre; casos borde escritos por el equipo y un error real encontrado     |
| Uso de IA con evidencia | Prompts sueltos o ninguno                         | Iteraciones documentadas                   | Iteraciones, diffs revisados y decisiones propias contra lo sugerido     |
| Comprensión             | Nadie explica el código entregado                 | El equipo explica lo esencial              | Cualquiera explica cualquier parte y la modifica en vivo                 |

Tope

Un proyecto que funciona pero que el equipo no entiende cae en Insuficiente en comprensión, y eso topa la nota sin importar qué tan pulido esté el resto. Funcionar no es el criterio.

### Tres niveles, según dónde esté el equipo

Nivel 1 — Prompting

Trabajan con Claude en el chat o en un Project.

**Reto:** armen el Project de su producto con su propio knowledge (brief, requisitos, decisiones técnicas) y muestren la misma pregunta respondida fuera y dentro del Project.

Nivel 2 — Engineer

Trabajan con Claude Code sobre su repositorio.

**Reto:** un `CLAUDE.md` propio, una feature implementada en rama con su test de caso borde, y el diff revisado con comentarios antes del merge.

Nivel 3 — AI Engineer

La IA es parte del producto, no solo de cómo lo construyen.

**Reto:** un endpoint que responda preguntas sobre tres documentos propios citando la fuente y respondiendo "no está en los documentos" cuando no esté; o conectar un servidor MCP existente a su flujo de trabajo dejando evidencia.

El nivel es el reto adicional, no el proyecto base. Un nivel 3 brillante sobre un producto sin problema definido no compensa el frente 1.

### Antes de empezar

| Qué                           | Cómo                                                                               |
|-------------------------------|------------------------------------------------------------------------------------|
| Repositorio del equipo        | Creado, con todos con acceso, y una rama por persona                               |
| Claude Code                   | `curl -fsSL https://claude.ai/install.sh | bash`, luego `cd su-proyecto && claude` |
| Carpeta de evidencia          | `ai-evidence/` en el repositorio, desde el primer commit                           |
| Si alguien no tiene plan pago | Trabajen en el chat web y documenten los prompts. La evidencia vale igual.         |

La biblioteca de prompts tiene 26 plantillas listas por rol. Empiecen por la del rol que corresponde al frente en el que están, y reemplacen los marcadores con los datos de su producto.
