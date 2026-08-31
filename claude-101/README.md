# Claude 101 — De Prompting a Product Engineering

Material de la clase para estudiantes de Ingeniería de Sistemas y Computación.

> La IA no es un buscador de respuestas ni una máquina para copiar código. Es una nueva interfaz para trabajar con software, conocimiento y productos.

La clase recorre un solo caso de principio a fin: **CampusFlow**, un asistente académico para estudiantes de pregrado. El mismo producto aparece en los prompts, en el Project, en el repositorio y en las demos.

---

## La presentación

`index.html` — 28 slides con seis preguntas de opción múltiple intercaladas para responder durante la sesión.

Se abre en cualquier navegador, sin instalar nada:

```bash
# clona el repositorio y abre el archivo
open claude-101/index.html      # macOS
xdg-open claude-101/index.html  # Linux
```

Cómo se navega:

| Acción | Tecla |
|---|---|
| Siguiente / anterior | `→` `←` o barra espaciadora |
| Índice de slides | `Esc` o `i` |
| Primera / última | `Inicio` / `Fin` |
| Cambiar tema claro-oscuro | botón **Tema** |

Las preguntas se responden haciendo clic: las opciones incorrectas se marcan y puedes seguir intentando; cuando aciertas aparece la explicación. En pantallas táctiles se avanza deslizando.

---

## Qué hay en cada archivo

| Archivo | Qué contiene |
|---|---|
| `index.html` | La presentación de la clase |
| `laboratorio.md` | Guía de trabajo: seis frentes para avanzar el proyecto de tu equipo, evidencia de uso de IA y criterios de evaluación |
| `prompt-library.md` | 26 prompts completos por rol (PM, SWE, QA, Security, UX, AI Engineer, Code Reviewer) |
| `buenas-practicas.md` | Prompts que no funcionan y su versión profesional, test de alucinación, tres casos de seguridad, cuándo usar qué herramienta |
| `cheat-sheet.md` | Una página para imprimir: estructura de prompt, workflow y las 10 reglas |
| `recursos.md` | Documentación oficial y plan de estudio de dos semanas |
| `campusflow-kit/` | Los siete documentos que se cargan al knowledge de un Claude Project |
| `campusflow-api/` | El repositorio de código sobre el que se trabaja con Claude Code |

---

## Levantar `campusflow-api`

Backend pequeño y real de CampusFlow. Trae **un bug intencional** y **una feature sin implementar**: los dos son parte del ejercicio.

```bash
cd claude-101/campusflow-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python seed.py
pytest -q
uvicorn app.main:app --reload
```

Luego:

```bash
curl localhost:8000/courses/1/agenda
```

Mira el campo `status` de la entrega que vence hoy a las 23:59. Ahí está el bug.

`GET /courses/{course_id}/workload` responde 501: esa es la feature que falta.

El repositorio incluye un `CLAUDE.md` en la raíz. Es lo que hace que Claude Code se comporte bien desde el primer prompt: léelo antes de empezar.

---

## Las diez ideas de la clase

1. Context matters.
2. Prompting is not magic.
3. Projects turn conversations into workspaces.
4. Claude Code works with the codebase, not just the question.
5. Vibe coding is powerful but dangerous without engineering discipline.
6. RAG gives models access to external knowledge.
7. MCP connects models with tools and systems.
8. Agents can act, not only answer.
9. AI-generated code still needs engineering.
10. The engineer is responsible for the result.

> **Don't just use AI. Learn to engineer with AI.**

---

Material verificado con documentación oficial a **agosto de 2026**. Lo que no se pudo confirmar en fuentes primarias está marcado como *no verificado*: las capacidades de estas herramientas cambian cada pocos meses, así que verifica antes de citar.
