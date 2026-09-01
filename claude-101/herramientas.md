# Sin suscripción

Escribir una especificación, darle contexto al modelo, revisar un diff, agregar el caso que falta: eso se hace igual en cualquier herramienta. Lo que cambia es cuánto acierta el modelo y qué tan cómodo se trabaja.

Lo más rápido es usar lo que ya tienes por estar matriculado. Si no alcanza, un agente libre con una capa gratuita cubre casi todo. Y si no quieres mandar tu código a ningún servidor, puedes correr un modelo en tu máquina.

### Empieza por lo que ya tienes

| Programa                   | Qué da                                                                                                                                    | Qué pide                                                                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| GitHub Education           | Acceso gratuito a Copilot para estudiantes verificados, más 180 core-hours de Codespaces al mes                                           | Estar inscrito en un programa que otorgue título, cuenta personal de GitHub y prueba de matrícula vigente (carné con fecha, horario o certificado) |
| Copilot Free               | Hasta 2.000 completions al mes, sin verificar estudiante                                                                                  | Solo cuenta de GitHub                                                                                                                              |
| Gemini CLI                 | Capa gratuita con cuenta personal de Google: 60 solicitudes por minuto y 1.000 al día, ventana de contexto de 1M tokens                   | Cuenta de Google                                                                                                                                   |
| Claude Free                | Chat en web, móvil y escritorio, con búsqueda, ejecución de código y conectores MCP remotos. **Claude Code no está en el plan gratuito.** | Cuenta                                                                                                                                             |
| ChatGPT Free               | Chat de texto, acceso limitado a Codex, contexto reducido                                                                                 | Cuenta                                                                                                                                             |
| JetBrains para estudiantes | IDEs completos gratis (IntelliJ IDEA Ultimate, PyCharm, WebStorm), renovable cada año. No sirve para trabajo comercial.                   | Verificación con correo universitario                                                                                                              |

La verificación de GitHub Education tarda unos días y a veces la rebotan. Manda una foto del carné donde se vea la fecha, o el certificado de matrícula. Hazlo antes de que lo necesites.

### Agentes de código libres

Estos trabajan sobre el repositorio, igual que Claude Code. Todos son gratis y de código abierto. Lo que cuesta es el modelo al que los conectes, así que con una capa gratuita o uno local no pagas nada.

| Herramienta | Licencia   | Dónde corre                            | Modelos locales          |
|-------------|------------|----------------------------------------|--------------------------|
| OpenCode    | MIT        | Terminal, escritorio, extensión de IDE | Sí, documentado          |
| Aider       | Apache 2.0 | Terminal                               | Sí                       |
| Cline       | Apache 2.0 | VS Code, JetBrains, Zed, Neovim, CLI   | Sí, documentado          |
| Continue    | Apache 2.0 | VS Code, JetBrains, CLI                | Sí, incluso sin internet |
| Goose       | Apache 2.0 | Terminal y app de escritorio           | Sí, con soporte MCP      |
| Gemini CLI  | Apache 2.0 | Terminal                               | No: usa modelos Gemini   |

Dos avisos, porque hay tutoriales de 2025 que mandan a enlaces muertos. **Roo Code se descontinuó** y su propio repositorio recomienda Cline o el fork ZooCode. Y **Goose cambió de organización** en abril de 2026, así que `block/goose` ya no es la fuente.

El más parecido a lo de la demo es OpenCode. Va en la terminal, trabaja sobre el repositorio, tiene modo de plan y de construcción, subagentes y MCP.

Instalar y arrancar OpenCode

    curl -fsSL https://opencode.ai/install | bash

    cd tu-proyecto
    opencode

Sirve con más de 75 proveedores. Para uno local lo apuntas a un endpoint compatible con la API de OpenAI, y en su documentación están los ejemplos para Ollama y LM Studio.

El archivo de instrucciones del repo sirve igual acá. Cambia el nombre según la herramienta, el contenido es el mismo.

### Correr un modelo en tu máquina

Hay dos formas. Las dos levantan un endpoint compatible con la API de OpenAI, y por ahí se conecta cualquiera de los agentes de arriba.

Ollama · terminal

``` code
curl -fsSL https://ollama.com/install.sh | sh

ollama pull qwen2.5-coder:7b
ollama run qwen2.5-coder:7b
```

Endpoint: `http://localhost:11434/v1`. Pide una API key que ignora: pon literalmente `ollama`.

LM Studio · interfaz gráfica

``` code
lms get
lms server start
```

Descarga la aplicación de `lmstudio.ai` y el CLI `lms` viene incluido. Endpoint: `http://127.0.0.1:1234/v1`.

Antes de bajar 14 GB, calcula si te cabe. Con cuantización de 4 bits cuenta como 0,6 GB de memoria por cada mil millones de parámetros, más lo del contexto. Es cálculo de servilleta, no cifra oficial.

| Tu máquina                          | Qué corre de verdad                     | Para qué sirve                                                                                               |
|-------------------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 8 GB de RAM                         | Modelos de 1,5B a 7B con contexto corto | Explicar código, generar funciones sueltas, autocompletar. Compite con el navegador y el IDE por la memoria. |
| 16 GB de RAM                        | 7B cómodo, 14B justo                    | Lo anterior, más tareas de un solo archivo con algo de contexto                                              |
| 32 GB o Mac con 24–32 GB unificados | Hasta 24B–30B                           | Empieza a ser usable para tareas agénticas cortas                                                            |
| Windows sin GPU dedicada            | Corre en CPU                            | Funciona para completar código; frustrante para agentes                                                      |

Modelos de código que caben en un portátil: `qwen2.5-coder` (0.5B a 14B), `deepseek-coder` (1.3B y 6.7B), `starcoder2`, `codegemma`, `yi-coder`, `opencoder`. Ya en el límite: `devstral:24b` (14 GB de descarga, pensado para agentes) y `qwen3-coder:30b` (19 GB).

### Antes de decidir

- Un 7B local queda muy por debajo de un modelo grande. Para explicar código, escribir funciones y autocompletar va bien. En tareas de varios pasos falla harto y a veces se queda dando vueltas. Si van a trabajar sobre un repo de verdad, una capa gratuita en la nube les va a rendir más.
- Las capas gratuitas suelen usar lo que mandas. Los términos de la API de Gemini dicen que en los servicios no pagos Google usa lo que envías y lo que responde para desarrollar sus productos, y que hay revisores humanos que pueden leerlo. Cada proveedor tiene su política. Así que nada de código de la práctica, datos de otras personas ni trabajos confidenciales por ahí. Si eso te preocupa, lo local no manda nada.
- La cuota se acaba. Un agente hace decenas de llamadas por tarea, así que es normal quedarse sin nada a mitad de una sesión. Ten el plan B ya configurado.
- Correr el modelo localmente deja el procesador al máximo. Ventilador a fondo y la batería se va rapidísimo. Trabaja enchufado.
- Que la herramienta sea gratis no significa que el uso lo sea. OpenCode, Aider, Cline, Continue y Goose son libres, pero necesitan una API key. Sin capa gratuita ni modelo local, eso cuesta.

### Qué montar

| Si...                                                   | Montaje                                                                           |
|---------------------------------------------------------|-----------------------------------------------------------------------------------|
| Quieres empezar en cinco minutos                        | Verifica GitHub Education y usa Copilot en el IDE de siempre                      |
| Quieres un agente sobre el repositorio, como en la demo | OpenCode conectado a una capa gratuita de API                                     |
| Trabajas sin internet o con datos sensibles             | Ollama con un modelo de código, y OpenCode o Continue apuntando al endpoint local |
| Ya vives en VS Code                                     | Cline o Continue, con capa gratuita o con Ollama                                  |

Cualquiera de esos sirve para el proyecto del curso. Móntalo antes de la próxima sesión, no durante.
