# ISIS2007 · Diseño de Productos e Innovación en TI

Portal del curso (sitio estático) y utilidades de apoyo. Semestre **2026-II**,
Universidad de los Andes.

## 🌐 El sitio

| Página | Archivo |
| --- | --- |
| Inicio | `index.html` |
| Cronograma 2026-II | `schedule.html` |
| Actividades y entregas | `actividades.html` |
| Recursos y materiales | `recursos-materiales.html` |
| Equipo docente | `team.html` |
| Ruleta de estudiantes | `ruleta-estudiantes.html` |
| Registro de asistencia | `asistencia-simple.html` |

### Sistema de diseño

Toda la interfaz comparte un único tema inspirado en la identidad visual de
Uniandes (negro, amarillo institucional, tipografía Inter, mucho espacio en blanco):

```
assets/theme.css   → tokens de color/tipografía y componentes (cards, tablas, botones…)
assets/site.js     → cabecera y pie de página compartidos + menú responsive
```

Para agregar una página al menú, edita el arreglo `NAV` en `assets/site.js`.
Cada página incluye:

```html
<link rel="stylesheet" href="assets/theme.css">
...
<script src="assets/site.js"></script>
```

El cronograma resalta automáticamente la próxima sesión según la fecha del día
y está optimizado para imprimir en PDF (Cmd/Ctrl + P).

## 🧰 Exportación a PDF

Este repositorio también incluye un script que combina las páginas del curso en
un solo PDF con las imágenes integradas.

## 📋 Características

- ✅ **Exportación completa**: Combina index, schedule y team en un solo PDF
- ✅ **Imágenes integradas**: Las fotos del equipo se incluyen automáticamente
- ✅ **Estilos optimizados**: Diseño perfecto para impresión
- ✅ **Saltos de página**: Organización automática del contenido
- ✅ **Colores preservados**: Gradientes y estilos visuales mantenidos
- ✅ **Tablas formateadas**: Cronograma perfectamente estructurado

## 🛠️ Instalación

```bash
npm install
```

## 🚀 Uso

### Exportar todo el contenido a PDF

```bash
npm run export-all
```

O directamente:

```bash
node export-all-to-pdf.js
```

### Exportar solo una página específica

```bash
npm run convert
```

## 📄 Archivos generados

- `ISIS2007-Documento-Completo-Perfecto.pdf` - PDF completo con todas las páginas

## 📁 Estructura del proyecto

```
├── assets/
│   ├── theme.css           # Sistema de diseño compartido
│   └── site.js             # Cabecera, menú y pie de página
├── index.html              # Página principal
├── schedule.html           # Cronograma 2026-II
├── actividades.html        # Actividades y entregas
├── recursos-materiales.html# Material de clase
├── team.html               # Equipo docente
├── ruleta-estudiantes.html # Ruleta + preguntas con IA
├── asistencia-simple.html  # Registro de asistencia
├── Archivos_de_Curso/      # PDFs del curso
├── export-all-to-pdf.js    # Script de exportación a PDF
├── FotoArturo.jpeg         # Foto del profesor
├── FotoJuanes.jpeg         # Foto del monitor
└── package.json            # Configuración del proyecto
```

## 🎨 Características del PDF generado

### Página 1: Información del Curso
- Descripción del curso ISIS2007
- Objetivos de aprendizaje
- Información académica (créditos, horario, sección)
- Enfoque en Lean Startup y Generative AI

### Página 2: Equipo Docente
- Fotos de todos los miembros del equipo
- Información de contacto
- Enlaces a LinkedIn
- Roles y responsabilidades

### Página 3: Cronograma Completo
- Información del semestre
- Sistema de evaluación detallado
- Cronograma semanal completo
- Fechas y actividades específicas

## 🔧 Configuración técnica

- **Formato**: A4
- **Márgenes**: 20mm en todos los lados
- **Fondo**: Incluido para preservar colores
- **Imágenes**: Integradas en base64
- **Fuentes**: Segoe UI (sistema)

## 🐛 Solución de problemas

### Error: "Cannot find module 'puppeteer'"
```bash
npm install
```

### Error: "Cannot find image files"
Asegúrate de que los archivos de imagen estén en el directorio raíz:
- `FotoArturo.jpeg`
- `FotoJuanes.jpeg`
- `FotoCatalina.jpeg`

### PDF no se genera
Verifica que tienes permisos de escritura en el directorio actual.

## 📞 Soporte

Para problemas técnicos, contacta al equipo de ISIS2007.

---

**Universidad de los Andes**  
Departamento de Ingeniería de Sistemas y Computación  
Semestre 2026-II
