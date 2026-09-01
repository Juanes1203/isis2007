# Sin suscripción

### Tres rutas

Escribir una especificación, dar contexto a un modelo, revisar un diff, agregar el caso borde que falta: todo eso se hace igual con cualquier herramienta.

Estas tres rutas se pueden combinar. La tercera funciona sin internet.

1\. Lo que ya tienen por ser estudiantes

Programas educativos y planes gratuitos. Lo más rápido de montar.

2\. Agente open source + API gratuita

Un agente de código libre conectado a un proveedor con capa gratuita. La ruta más práctica para trabajar sobre un repositorio.

3\. Todo local

Modelo abierto corriendo en su máquina. Cero costo, cero envío de datos, y menos capacidad.

### Ruta 1 — Lo que ya tienen

| Programa                   | Qué da                                                                                                                                    | Qué pide                                                                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| GitHub Education           | Acceso gratuito a Copilot para estudiantes verificados, más 180 core-hours de Codespaces al mes                                           | Estar inscrito en un programa que otorgue título, cuenta personal de GitHub y prueba de matrícula vigente (carné con fecha, horario o certificado) |
| Copilot Free               | Hasta 2.000 completions al mes, sin verificar estudiante                                                                                  | Solo cuenta de GitHub                                                                                                                              |
| Gemini CLI                 | Capa gratuita con cuenta personal de Google: 60 solicitudes por minuto y 1.000 al día, ventana de contexto de 1M tokens                   | Cuenta de Google                                                                                                                                   |
| Claude Free                | Chat en web, móvil y escritorio, con búsqueda, ejecución de código y conectores MCP remotos. **Claude Code no está en el plan gratuito.** | Cuenta                                                                                                                                             |
| ChatGPT Free               | Chat de texto, acceso limitado a Codex, contexto reducido                                                                                 | Cuenta                                                                                                                                             |
| JetBrains para estudiantes | IDEs completos gratis (IntelliJ IDEA Ultimate, PyCharm, WebStorm), renovable cada año. No sirve para trabajo comercial.                   | Verificación con correo universitario                                                                                                              |

La verificación de GitHub Education tarda unos días y a veces rebota. Manden una foto legible del carné con la fecha visible, o el certificado de matrícula. Háganlo antes de necesitarlo.

### Ruta 2 — Agentes de código open source

Todos son gratis y de código abierto. Lo que cuesta es el modelo al que los conecten: con una capa gratuita o un modelo local, el costo queda en cero.

| Herramienta | Licencia   | Dónde corre                            | Modelos locales          |
|-------------|------------|----------------------------------------|--------------------------|
| OpenCode    | MIT        | Terminal, escritorio, extensión de IDE | Sí, documentado          |
| Aider       | Apache 2.0 | Terminal                               | Sí                       |
| Cline       | Apache 2.0 | VS Code, JetBrains, Zed, Neovim, CLI   | Sí, documentado          |
| Continue    | Apache 2.0 | VS Code, JetBrains, CLI                | Sí, incluso sin internet |
| Goose       | Apache 2.0 | Terminal y app de escritorio           | Sí, con soporte MCP      |
| Gemini CLI  | Apache 2.0 | Terminal                               | No: usa modelos Gemini   |

Dos avisos, porque muchos tutoriales de 2025 mandan a enlaces muertos: **Roo Code se descontinuó** (su propio repositorio recomienda Cline o el fork ZooCode) y **Goose cambió de organización** en abril de 2026, así que `block/goose` ya no es la fuente.

#### OpenCode, paso a paso

Agente de terminal que trabaja sobre el repositorio, con modos de plan y de construcción, subagentes y soporte de MCP.

Instalar y arrancar

    curl -fsSL https://opencode.ai/install | bash

    cd su-proyecto
    opencode

Soporta más de 75 proveedores de modelos. Para conectarlo a un modelo local basta apuntarlo a un endpoint compatible con la API de OpenAI —Ollama en `http://localhost:11434/v1`, LM Studio en `http://127.0.0.1:1234/v1`— y su documentación trae los ejemplos de configuración.

El archivo de instrucciones del repositorio sirve igual acá. Cambia el nombre según la herramienta; el contenido es el mismo.

### Ruta 3 — Modelos corriendo en su máquina

Dos formas de levantar un modelo local. Ambas exponen un endpoint compatible con la API de OpenAI, que es lo que permite conectarlas a cualquiera de los agentes de arriba.

Ollama · terminal

``` code
curl -fsSL https://ollama.com/install.sh | sh

ollama pull qwen2.5-coder:7b
ollama run qwen2.5-coder:7b
```

Endpoint: `http://localhost:11434/v1`. Pide una API key que ignora: pongan literalmente `ollama`.

LM Studio · interfaz gráfica

``` code
lms get
lms server start
```

Se descarga la aplicación de `lmstudio.ai` y el CLI `lms` viene incluido. Endpoint: `http://127.0.0.1:1234/v1`.

#### Qué modelo corre en su portátil

Regla práctica con cuantización de 4 bits: cuenten unos 0,6 GB de memoria por cada mil millones de parámetros, más lo que ocupe el contexto. No es una cifra oficial, es una aproximación para calcular antes de descargar 14 GB.

| Su máquina                          | Qué corre de verdad                     | Para qué sirve                                                                                               |
|-------------------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 8 GB de RAM                         | Modelos de 1,5B a 7B con contexto corto | Explicar código, generar funciones sueltas, autocompletar. Compite con el navegador y el IDE por la memoria. |
| 16 GB de RAM                        | 7B cómodo, 14B justo                    | Lo anterior, más tareas de un solo archivo con algo de contexto                                              |
| 32 GB o Mac con 24–32 GB unificados | Hasta 24B–30B                           | Empieza a ser usable para tareas agénticas cortas                                                            |
| Windows sin GPU dedicada            | Corre en CPU                            | Funciona para completar código; frustrante para agentes                                                      |

Modelos de código que se pueden descargar hoy en el rango de un portátil: `qwen2.5-coder` (0.5B a 14B), `deepseek-coder` (1.3B y 6.7B), `starcoder2`, `codegemma`, `yi-coder`, `opencoder`. Ya en el límite superior: `devstral:24b` (14 GB de descarga, pensado explícitamente para agentes) y `qwen3-coder:30b` (19 GB).

### Lo que hay que saber antes de elegir

- **Un 7B local rinde muy por debajo de un modelo frontera.** Sirve bien para explicar código, escribir funciones y autocompletar. En tareas agénticas de varios pasos (llamar herramientas, editar varios archivos, no perder el hilo) falla bastante y a veces entra en bucles. Para trabajar sobre un repositorio real, una capa gratuita en la nube rinde mejor.
- **Privacidad.** Las capas gratuitas suelen usar lo que envías para mejorar el producto. Los términos de la API de Gemini, por ejemplo, dicen explícitamente que en los servicios no pagos Google usa el contenido enviado y las respuestas generadas para desarrollar sus productos, y que revisores humanos pueden leerlo. Cada proveedor tiene su política y hay que leerla. Regla simple: nada de código propietario de una práctica, datos personales de terceros ni trabajos confidenciales en una capa gratuita. Si eso les preocupa, la ruta local no envía nada.
- **Los límites de tasa se agotan.** Un agente hace decenas de llamadas por tarea. Es normal quedarse sin cuota a mitad de una sesión larga: tengan un plan B configurado antes de necesitarlo.
- **Batería y calor.** La inferencia local mantiene el procesador al máximo. En portátil eso es ventilador a fondo y batería que se va rápido: trabajen enchufados.
- **La herramienta es gratis; el uso no siempre.** OpenCode, Aider, Cline, Continue y Goose son libres, pero necesitan una API key. Sin capa gratuita ni modelo local, generan costo.

### Qué montar

| Si...                                                   | Montaje                                                                          |
|---------------------------------------------------------|----------------------------------------------------------------------------------|
| Quieren empezar en cinco minutos                        | Verifiquen GitHub Education y usen Copilot en su IDE de siempre                  |
| Quieren un agente sobre el repositorio, como en la demo | OpenCode conectado a una capa gratuita de API                                    |
| Trabajan sin internet o con datos sensibles             | Ollama con un modelo de código + OpenCode o Continue apuntando al endpoint local |
| Ya viven en VS Code                                     | Cline o Continue, con capa gratuita o con Ollama                                 |

Cualquiera de esos montajes alcanza para el proyecto del curso. Móntenlo antes de la próxima sesión.

Datos verificados en la documentación oficial de cada herramienta a septiembre de 2026. Esto cambia cada pocos meses: si un comando o un límite no cuadra, revisen la documentación del proyecto.
