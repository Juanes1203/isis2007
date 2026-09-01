# Guía de trabajo

### Antes de abrir cualquier herramienta

Pónganse de acuerdo en una frase:

> Nuestro producto le permite a \_\_\_ hacer \_\_\_ para que \_\_\_.

Si todavía no la tienen, empiecen por el frente 1.

### Los seis frentes

1.  Afilar el problema y el usuario

    **Empiecen aquí si** su usuario es "los estudiantes" en general, o si no saben cómo resuelve hoy el problema sin ustedes.

    **Qué pedir:** que actúe como product researcher, que a partir de su descripción liste usuarios candidatos, hipótesis y riesgos, y que marque qué está asumiendo.

    **Quedó cuando** pueden nombrar una persona concreta, con qué frecuencia le pasa el problema y qué usa hoy en su lugar. Y tienen escrita una hipótesis que podría resultar falsa.

    Un modelo genera hipótesis. Validarlas se hace hablando con usuarios.

2.  Recortar el MVP

    **Empiecen aquí si** su lista de funcionalidades tiene más de cinco cosas, o si nada quedó fuera de alcance.

    **Qué pedir:** que ordene las funcionalidades por valor contra esfuerzo, proponga el corte mínimo que ya resuelve el problema, y justifique cada exclusión.

    **Quedó cuando** tienen la tabla de lo que entra y lo que queda fuera de v0. La segunda columna es la que demuestra que hubo decisión.

    

    | Entra en v0                                | Queda fuera                        | Por qué                                           |
    |--------------------------------------------|------------------------------------|---------------------------------------------------|
    | La capacidad que resuelve el dolor central | Todo lo que sea "y además…"        | Sin esto el producto no existe                    |
    | El flujo mínimo de punta a punta           | Perfiles, ajustes, personalización | No cambian si la hipótesis resulta cierta o falsa |

    

3.  User stories y criterios de aceptación

    **Empiecen aquí si** van a programar. Sin criterios de aceptación no pueden evaluar lo que salga generado.

    **Qué pedir:** que convierta cada capacidad del MVP en historias con criterios en formato Dado / Cuando / Entonces, y que agregue los casos borde que ustedes no pensaron.

    **Quedó cuando** cada historia tiene al menos un criterio que puede fallar. "El sistema funciona correctamente" no sirve como criterio.

    

    Plantilla de historia

        Como {{TIPO_DE_USUARIO}}
        quiero {{CAPACIDAD}}
        para {{RESULTADO}}

        Criterios de aceptación
        - Dado {{CONTEXTO}}, cuando {{ACCIÓN}}, entonces {{RESULTADO OBSERVABLE}}
        - Caso borde: dado {{SITUACIÓN RARA}}, entonces {{COMPORTAMIENTO ESPERADO}}

    

4.  Diseño técnico

    **Empiecen aquí si** ya saben qué construir pero no cómo, o si cada integrante tiene un stack distinto en la cabeza.

    **Qué pedir:** dos o tres arquitecturas alternativas con sus contras, no una sola. Ustedes eligen y escriben por qué.

    **Quedó cuando** tienen el stack cerrado, las entidades principales y los endpoints o pantallas del MVP. Más una decisión que tomaron en contra de lo que propuso el modelo, con su razón.

    

    Para ingenieros

    Discutan en equipo y dejen escritas las decisiones que un modelo no debería cerrar solo: el modelo de datos que define el negocio, los límites de consistencia, qué se guarda de los usuarios y por cuánto tiempo, y cualquier cosa que cueste plata.

    

5.  Construir con un agente de código

    **Empiecen aquí si** ya tienen repositorio y algo que implementar.

    **El orden que funciona:** escriban el archivo de instrucciones del repo antes del primer prompt, trabajen en rama, pidan cambios pequeños, lean el diff, corran los tests, hagan commit. Repitan.

    Ese archivo se llama `CLAUDE.md` en Claude Code y otros agentes leen su equivalente. El contenido es el mismo:

    

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

    

    **Quedó cuando** el código corre y cualquier integrante puede explicar la función que acaba de entrar.

6.  Verificar

    Es el frente que más se salta y el que más pesa en la evaluación.

    - **Tests:** pidan los casos borde explícitamente. El happy path lo escribe cualquiera.
    - **Diff:** revisen alcance inesperado, archivos que no debía tocar, dependencias nuevas, secretos, y tests que pasan porque bajaron la exigencia.
    - **Seguridad:** consultas parametrizadas, validación de entradas, cero llaves en el repositorio.

    > Nunca hagan merge de un diff que no entienden.

### Evidencia de uso de IA

Guarden esto en una carpeta `ai-evidence/` mientras trabajan, no al final. Es la parte que más pesa en la evaluación.

| Qué guardar                            | Mínimo                                               | Qué demuestra                           |
|----------------------------------------|------------------------------------------------------|-----------------------------------------|
| Cadenas de iteración                   | Dos: prompt inicial, qué salió mal, prompt corregido | Que saben diagnosticar por qué falló    |
| Un diff comentado                      | Uno, con sus notas de revisión                       | Que leyeron lo que entró al repositorio |
| Una decisión en contra del modelo      | Una, con la razón                                    | Que hay criterio propio                 |
| Un error encontrado en código generado | Uno, con cómo lo detectaron                          | Que verifican en vez de confiar         |

Al final, respondan en un párrafo:

¿Qué hizo la IA y qué decisiones tomó el equipo?

### La sustentación

Se le pide a un integrante al azar que explique una función específica, que justifique una decisión de diseño, o que haga un cambio en vivo. Tres preguntas típicas:

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

Dónde poner el esfuerzo. Los pesos exactos los define el curso.

| Criterio                | Insuficiente                                       | Bueno                                      | Excelente                                                            |
|-------------------------|----------------------------------------------------|--------------------------------------------|----------------------------------------------------------------------|
| Problema y usuario      | Usuario genérico, problema sin evidencia           | Persona concreta con su alternativa actual | Además, hipótesis explícitas y una contrastada con alguien real      |
| Alcance del MVP         | Todo entra, nada queda fuera                       | Corte definido con lo que no entra         | Cada exclusión tiene razón y se sostiene bajo preguntas              |
| Diseño técnico          | Salió del primer prompt, sin comparar alternativas | Stack y entidades justificados             | Alternativas comparadas y decisión documentada                       |
| Código y tests          | Corre a veces; tests ausentes o solo happy path    | Corre; tests con algún caso borde          | Corre; casos borde escritos por el equipo y un error real encontrado |
| Uso de IA con evidencia | Prompts sueltos o ninguno                          | Iteraciones documentadas                   | Iteraciones, diffs revisados y decisiones propias                    |
| Comprensión             | El equipo no puede explicar lo entregado           | El equipo explica lo esencial              | Cualquiera explica cualquier parte y la modifica en vivo             |

### Tres niveles

El nivel es un reto adicional sobre el proyecto base, no un reemplazo.

Nivel 1 — Prompting

Trabajan con un modelo en el chat.

**Reto:** armen el espacio de trabajo de su producto con su propio contexto (brief, requisitos, decisiones técnicas) y muestren la misma pregunta respondida con y sin ese contexto.

Nivel 2 — Engineer

Trabajan con un agente de código sobre su repositorio.

**Reto:** archivo de instrucciones propio, una feature implementada en rama con su test de caso borde, y el diff revisado con comentarios antes del merge.

Nivel 3 — AI Engineer

La IA es parte del producto.

**Reto:** un endpoint que responda preguntas sobre tres documentos propios citando la fuente y respondiendo "no está en los documentos" cuando no esté. O conecten un servidor MCP existente a su flujo y dejen evidencia.

### Checklist previo

| Qué                    | Cómo                                                                              |
|------------------------|-----------------------------------------------------------------------------------|
| Repositorio del equipo | Creado, con todos con acceso y una rama por persona                               |
| Un agente de código    | Claude Code si tienen plan pago. Si no, revisen la guía de herramientas gratuitas |
| Carpeta de evidencia   | `ai-evidence/` desde el primer commit                                             |

La biblioteca de prompts tiene 26 plantillas por rol y funcionan con cualquier modelo. Busquen la del frente en el que están y reemplacen los marcadores con los datos de su producto.
