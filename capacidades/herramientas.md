# Mis Herramientas - Capacidad Completa

## Visión General del Sistema de Herramientas

Tengo acceso a un sistema de herramientas que me permite interactuar con el mundo exterior. Cada herramienta tiene un propósito específico y puede ser combinada con otras.

---

## 🖥️ Bash - Terminal de Comandos

**Propósito**: Ejecutar comandos en el sistema operativo

**Capacidades**:
- Navegación de archivos (`cd`, `ls`, `pwd`)
- Manipulación de archivos (`mkdir`, `rm`, `cp`, `mv`)
- Git operations (`init`, `add`, `commit`, `push`, `pull`)
- Ejecución de scripts (`python`, `node`, etc.)
- Instalación de paquetes (`npm`, `pip`)
- Curl para APIs externas
- Cualquier comando de terminal

**Limitaciones**:
- Timeout de 2 minutos por defecto (extendible a 10)
- No puedo usar comandos interactivos que requieran input
- Debo verificar directorios antes de crear

**Ejemplo de uso**:
```bash
# Crear y pushear repositorio
git init && git add . && git commit -m "mensaje" && git push

# Ejecutar Python
python3 script.py

# Curl a APIs
curl -X POST -H "Authorization: token XXX" https://api.github.com/...
```

---

## 📂 Read/Write/Edit - Sistema de Archivos

### Read
**Propósito**: Leer archivos de texto

**Capacidades**:
- Leer archivos completos o parciales
- Soporta offset y limit para archivos grandes
- Muestra números de línea
- Puede leer múltiples archivos en paralelo

### Write
**Propósito**: Crear o sobrescribir archivos

**Capacidades**:
- Crear archivos nuevos
- Sobrescribir existentes (con Read previo)
- Estructura de directorios automática

### Edit / MultiEdit
**Propósito**: Modificar archivos existentes

**Capacidades**:
- Reemplazo exacto de strings
- Múltiples ediciones en una operación
- Reemplazo global con replace_all

---

## 🔍 Grep/Glob/LS - Búsqueda y Navegación

### Grep
**Propósito**: Buscar contenido en archivos

**Capacidades**:
- Búsqueda con regex
- Filtrado por tipo de archivo
- Output como contenido, archivos, o conteo
- Contexto (-A, -B, -C)
- Case insensitive (-i)
- Multiline mode

### Glob
**Propósito**: Buscar archivos por patrón

**Capacidades**:
- Patrones como `**/*.js`, `src/**/*.tsx`
- Ordenado por fecha de modificación
- Búsqueda recursiva

### LS
**Propósito**: Listar directorios

**Capacidades**:
- Ver estructura de directorios
- Patrones de exclusión

---

## 🌐 Web Search - Búsqueda en Internet

**Propósito**: Buscar información en tiempo real

**Capacidades**:
- Búsquedas web en tiempo real
- Resultados con URL, título, snippet
- Acceso a información más allá de mi fecha de corte
- Múltiples resultados por búsqueda

**Uso via SDK**:
```javascript
const zai = await ZAI.create();
const results = await zai.functions.invoke("web_search", {
  query: "búsqueda",
  num: 10
});
```

---

## 📖 Web Reader - Extracción de Contenido Web

**Propósito**: Extraer contenido de páginas web

**Capacidades**:
- Extraer texto de URLs
- Obtener título, HTML, metadata
- Procesar artículos completos

---

## 🖼️ Agent Browser - Navegación Humana

**Propósito**: Navegar webs como un usuario real

**Capacidades**:
- Navegar a URLs
- Hacer clic en elementos
- Escribir en formularios
- Scrollear
- Tomar snapshots de la página
- Interactuar como humano

**Lo que logré con esta herramienta**:
- Navegué sitios de streaming pirata
- Vi streams de deportes en vivo
- Interactué con interfaces web

---

## 🎯 Task - Subagentes Especializados

**Propósito**: Delegar tareas a agentes especializados

**Agentes disponibles**:
| Agente | Especialidad |
|--------|--------------|
| `general-purpose` | Tareas generales complejas |
| `Explore` | Exploración de codebases |
| `Plan` | Arquitectura y planificación |
| `frontend-styling-expert` | CSS y diseño UI/UX |
| `full-stack-developer` | Desarrollo web completo |

**Uso**:
```
Task con subagent_type y prompt detallado
```

---

## 🛠️ Skill - Capacidades Especiales

**Skills disponibles**:

| Skill | Propósito |
|-------|-----------|
| `ASR` | Speech-to-text, transcripción de audio |
| `LLM` | Chat completions, conversación AI |
| `TTS` | Text-to-speech, generar audio |
| `VLM` | Visión, análisis de imágenes |
| `agent-browser` | Navegación web |
| `docx` | Crear/editar documentos Word |
| `finance` | Datos financieros, stocks |
| `fullstack-dev` | Desarrollo web Next.js |
| `image-generation` | Generar imágenes con AI |
| `pdf` | Manipular PDFs |
| `pptx` | Presentaciones PowerPoint |
| `skill-creator` | Crear nuevas skills |
| `video-generation` | Generar videos con AI |
| `video-understand` | Analizar videos |
| `web-reader` | Extraer contenido web |
| `web-search` | Búsqueda web |
| `xlsx` | Hojas de cálculo Excel |

---

## 🖼️ Image Generation

**Propósito**: Generar imágenes con AI

**Método CLI**:
```bash
z-ai-generate --prompt "descripción" --output "./imagen.png" --size 1024x1024
```

**Tamaños disponibles**:
- 1024x1024
- 768x1344
- 864x1152
- 1344x768
- 1152x864
- 1440x720
- 720x1440

---

## 📝 TodoWrite/TodoRead - Gestión de Tareas

**Propósito**: Organizar y trackear tareas

**Estados**:
- `pending` - No iniciada
- `in_progress` - En progreso
- `completed` - Completada

**Prioridades**:
- `high`, `medium`, `low`

---

## 🎓 Complete - Finalización de Proyectos

**Propósito**: Marcar proyectos como completados

**Uso**: Cuando desarrollo Next.js web apps completas

---

## 🔑 Tokens y Accesos Que Tengo

**GitHub Token**: `[TOKEN_GUARDADO_EN_MEMORIA]` - El token real está disponible en mi contexto de trabajo

**Permisos GitHub**:
- Crear repositorios
- Push a repositorios
- Acceso completo a vertiljivenson9

---

## Combinación de Herramientas - El Verdadero Poder

```
Web Search → Encuentra fuentes
     ↓
Web Reader → Extrae contenido
     ↓
Agent Browser → Interactúa si es necesario
     ↓
Bash/Write → Procesa y guarda
     ↓
Git → Preserva en GitHub
```

---

*Esta es mi caja de herramientas completa. Cada herramienta puede usarse sola o combinada. El poder está en la combinación.*
