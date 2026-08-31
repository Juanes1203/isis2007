# Claude for Software Engineers — cheat sheet

Parte X

## Claude for Software Engineers

Una página. Para imprimir y pegar al lado del monitor.

1\. Prompting — las seis partes

- **Context** — quién eres, qué producto es, qué stack, qué existe ya.
- **Goal** — una sola tarea, en una frase, con el resultado esperado.
- **Constraints** — versiones, librerías permitidas, estilo, lo que NO debe tocar.
- **Input** — los datos reales: schema, ejemplo de payload, archivo, error completo.
- **Output** — formato exacto: diff, archivo completo, tabla, JSON con estas llaves.
- **Validation** — cómo se comprueba que sirve: tests que deben pasar, casos borde.

Si el prompt no dice cómo se valida, el modelo decide por ti qué significa "correcto".

2\. Workflow — el ciclo

Specify Generate Inspect Test Validate Iterate

- **Specify** — escribe el alcance, los criterios de aceptación y los casos borde antes de pedir código.
- **Generate** — deja que el agente produzca el cambio completo, no fragmentos sueltos.
- **Inspect** — lee el diff línea por línea; mira dependencias nuevas y archivos tocados de más.
- **Test** — corre la suite y agrega tú los casos borde que faltan; que alguno falle primero.
- **Validate** — comprueba contra el criterio de aceptación, no contra "compiló y no explotó".
- **Iterate** — cambia el contexto, no el tono: más datos, menos alcance, otro ángulo.

3\. Herramientas — úsala cuando

| Herramienta   | Úsala cuando                                                                                                              |
|---------------|---------------------------------------------------------------------------------------------------------------------------|
| Claude (chat) | Necesitas pensar, explorar o decidir: discovery, diseño, explicar un error, comparar opciones.                            |
| Projects      | Varias conversaciones comparten el mismo contexto: knowledge del producto + project instructions estables.                |
| Claude Code   | El trabajo ocurre en el repositorio: leer el codebase, editar archivos, correr tests, git y PRs.                          |
| RAG           | El corpus es grande, cambia seguido o tiene permisos por usuario, y no cabe en una sola pasada.                           |
| MCP           | Quieres que el modelo hable con un sistema externo (tools, resources, prompts) por un estándar y no por un script pegado. |
| Agents        | La tarea es multi-paso, con tool use en ciclo y verificación intermedia, no una sola respuesta.                           |

4\. Golden Rules

1.  **Give context.** — el modelo no adivina tu repo.
2.  **Be specific.** — ambiguo entra, basura sale.
3.  **Iterate.** — el primer output es borrador.
4.  **Verify.** — comprueba antes de confiar.
5.  **Test.** — casos borde, no solo happy path.
6.  **Don't trust blindly.** — suena seguro, puede mentir.
7.  **Understand what AI generates.** — si no lo explicas, no lo entregues.
8.  **Protect secrets and data.** — nada de keys ni datos reales.
9.  **Use AI to accelerate thinking, not replace it.** — piensa tú, acelera con IA.
10. **You are responsible for the final product.** — la firma del PR es tuya.

5\. Comandos

``` code
# instalar el CLI
curl -fsSL https://claude.ai/install.sh | bash      # macOS / Linux / WSL
irm https://claude.ai/install.ps1 | iex             # PowerShell
brew install --cask claude-code
winget install Anthropic.ClaudeCode

# abrir una sesión en el repo
cd campusflow-api && claude

# modo no interactivo (pipe, CI, scripts)
claude -p "explica qué hace services/deadlines.py"
git diff main --name-only | claude -p "revisa estos archivos por problemas de seguridad"

# MCP
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp list
/mcp                    # dentro de la sesión: estado de los servidores

# contexto persistente del repo
CLAUDE.md               # en la raíz; se lee al inicio de cada sesión

# traer al terminal una sesión iniciada en web o móvil
claude --teleport

# programar trabajo recurrente en la nube
/schedule
```

Alcances de MCP: local (`~/.claude.json`), project (`.mcp.json`, versionado y compartido con el equipo), user.

6\. Señales de alarma

1.  Vas a hacer merge y no leíste el diff.
2.  Tu prompt cabe en un tweet.
3.  Los tests los escribió la misma pasada que el código y ninguno falla.
4.  Agregaste una dependencia que no sabes qué hace ni quién la mantiene.
5.  Hay una API key en el repo.
6.  No sabes explicar una función que vas a entregar.
7.  "Funciona" es tu único criterio de aceptación.
8.  Llevas cinco intentos repitiendo el mismo prompt sin cambiar el contexto.

> Don't just prompt. Engineer.
