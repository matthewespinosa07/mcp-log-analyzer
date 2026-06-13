# 📊 MCP Log Analyzer

Servidor MCP desarrollado en Python para analizar archivos de logs y exponer herramientas de diagnóstico mediante Model Context Protocol (MCP).

---

## 📖 Descripción del proyecto

**MCP Log Analyzer** es un servidor MCP que analiza un archivo de logs (`app.log`) y expone herramientas para consultar, resumir y diagnosticar el estado operativo de un sistema a partir de sus registros.

El proyecto simula un entorno empresarial donde diferentes eventos del sistema son almacenados en archivos de log. Estos registros pueden contener información sobre operaciones exitosas, advertencias, errores y eventos críticos.

Este proyecto fue desarrollado como parte de la materia **Ingeniería de Software II**, con el objetivo de comprender el funcionamiento del **Model Context Protocol (MCP)** y su integración con herramientas externas.

---

## 🎯 Problema que resuelve

Los sistemas modernos generan grandes cantidades de registros que contienen información importante sobre su funcionamiento.

Entre los eventos que pueden encontrarse en un archivo de logs están:

* Operaciones ejecutadas correctamente.
* Advertencias del sistema.
* Errores de ejecución.
* Problemas de conectividad.
* Fallos de servicios.
* Eventos críticos que requieren atención inmediata.

Analizar estos archivos manualmente puede ser una tarea lenta y propensa a errores. Este servidor MCP automatiza parte del proceso y permite consultar información relevante desde cualquier cliente compatible con MCP.

---

## 🧠 ¿Qué es MCP?

**Model Context Protocol (MCP)** es un estándar abierto que permite que modelos de lenguaje interactúen con herramientas y datos externos de forma estructurada.

MCP facilita la integración con:

* Archivos.
* APIs.
* Bases de datos.
* Herramientas personalizadas.
* Sistemas externos.

En este proyecto:

* El **Host** puede ser una aplicación compatible con MCP.
* El **Cliente MCP** se comunica con el servidor.
* El **Servidor MCP** está desarrollado en Python.
* Las **Tools** realizan operaciones sobre el archivo de logs.
* El **Resource** expone el contenido del archivo para consulta.

---

## 🏗️ Arquitectura

```text
MCP Inspector
     │
     ▼
Cliente MCP
     │
     ▼
Servidor MCP en Python
     │
     ▼
logs/app.log
```

El servidor utiliza transporte `stdio`, permitiendo la comunicación directa con MCP Inspector para probar herramientas y recursos.

---

## 🛠 Tecnologías utilizadas

* Python 3
* MCP SDK para Python
* FastMCP
* MCP Inspector
* GitHub
* Visual Studio Code
* macOS

---

## 📁 Estructura del proyecto

```text
mcp-log-analyzer/
│
├── server.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── evidencias/
│   ├── 01-servidor-conectado.png
│   ├── 02-lista-tools.png
│   ├── 03-resumir-log.png
│   ├── 04-diagnostico-pedidos.png
│   └── 05-resource-app-log.png
│
└── logs/
    └── app.log
```

---

## 💻 Código del servidor

El código principal se encuentra en:

```text
server.py
```

Este archivo contiene la implementación del servidor utilizando `FastMCP`.

Las herramientas implementadas son:

* `contar_lineas_log`
* `buscar_errores_log`
* `resumir_log`
* `diagnosticar_estado_pedidos`

También se define un Resource para exponer el contenido del archivo de logs.

---

## 📄 Archivo de logs

El archivo:

```text
logs/app.log
```

contiene eventos simulados para demostrar las capacidades de análisis del servidor.

Ejemplo:

```text
2026-01-15 09:00:00 INFO Inicio del sistema
2026-01-15 09:02:15 INFO Proceso ejecutado correctamente
2026-01-15 09:04:22 WARNING Consumo elevado de memoria
2026-01-15 09:08:45 ERROR Error de conexión con servicio externo
2026-01-15 09:15:50 CRITICAL Servicio principal no disponible
```

---

# 🔧 Tools implementadas

## 1️⃣ contar_lineas_log

Cuenta la cantidad total de líneas presentes en el archivo de log.

### Resultado esperado

```json
{
  "archivo": "app.log",
  "total_lineas": 10
}
```

---

## 2️⃣ buscar_errores_log

Busca eventos problemáticos dentro del archivo de log.

Detecta líneas con nivel:

* ERROR
* CRITICAL

### Resultado esperado

```json
{
  "archivo": "app.log",
  "total_eventos_problematicos": 3
}
```

---

## 3️⃣ resumir_log

Genera un resumen de eventos por nivel.

### Resultado esperado

```json
{
  "archivo": "app.log",
  "resumen": {
    "INFO": 5,
    "WARNING": 2,
    "ERROR": 2,
    "CRITICAL": 1
  }
}
```

---

## 4️⃣ diagnosticar_estado_pedidos

Analiza el contenido del log y determina el estado general del sistema.

Estados posibles:

* ✅ ESTABLE
* 🟡 EN_OBSERVACION
* 🟠 CON_ERRORES
* 🔴 CRITICO

### Resultado esperado

```json
{
  "estado_general": "CRITICO"
}
```

---

# 📚 Resource implementado

## log://app-log

Expone el contenido completo del archivo:

```text
logs/app.log
```

Este recurso permite que un cliente MCP consulte directamente el archivo de registros.

---

# ⚙️ Instalación

## 1️⃣ Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd mcp-log-analyzer
```

---

## 2️⃣ Crear entorno virtual

```bash
python3 -m venv .venv
```

---

## 3️⃣ Activar entorno virtual

```bash
source .venv/bin/activate
```

---

## 4️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

O instalar MCP directamente:

```bash
pip install "mcp[cli]"
```

---

# ▶️ Ejecución

Para iniciar el servidor:

```bash
mcp dev server.py
```

Esto abrirá MCP Inspector para probar las herramientas y recursos disponibles.

---

# 🧪 Pruebas realizadas

Las pruebas fueron realizadas utilizando MCP Inspector.

## ✅ Prueba 1: conexión del servidor

Se verificó que MCP Inspector se conecta correctamente al servidor:

```text
mcp-log-analyzer
```

**Evidencia:** `01-servidor-conectado.png`

---

## ✅ Prueba 2: listado de Tools

Se verificó que el servidor expone correctamente:

```text
contar_lineas_log
buscar_errores_log
resumir_log
diagnosticar_estado_pedidos
```

**Evidencia:** `02-lista-tools.png`

---

## ✅ Prueba 3: ejecución de resumir_log

Se comprobó la generación correcta del resumen de eventos.

**Evidencia:** `03-resumir-log.png`

---

## ✅ Prueba 4: ejecución de diagnosticar_estado_pedidos

Se verificó el diagnóstico automático del estado del sistema.

**Evidencia:** `04-diagnostico-pedidos.png`

---

## ✅ Prueba 5: consulta del Resource

Se verificó la lectura correcta del Resource asociado al archivo de logs.

**Evidencia:** `05-resource-app-log.png`

---

# 🎓 Relación con Ingeniería de Software

Este proyecto aplica conceptos fundamentales de Ingeniería de Software:

* Arquitectura cliente-servidor.
* Integración entre sistemas.
* Monitoreo de aplicaciones.
* Procesamiento de información.
* Análisis de logs.
* Reutilización de componentes.
* Protocolos de comunicación.
* Uso de estándares abiertos.

---

# 📦 Entregables cubiertos

Este repositorio cubre los entregables correspondientes a la **Opción A: Implementación Práctica de un Servidor MCP Básico**:

* Código fuente del servidor MCP.
* Archivo de logs de ejemplo.
* Tools personalizadas.
* Resource personalizado.
* Instrucciones de instalación.
* Instrucciones de ejecución.
* Evidencias de pruebas realizadas.
* Repositorio documentado en GitHub.

---

# ✅ Conclusiones

El proyecto demuestra cómo MCP permite conectar herramientas personalizadas con modelos de lenguaje mediante un protocolo estándar.

A través de este servidor es posible analizar archivos de logs, detectar errores, identificar eventos críticos y generar diagnósticos operativos de forma automatizada.

La solución representa un caso práctico de integración entre inteligencia artificial y sistemas externos para facilitar tareas de monitoreo y análisis de registros.

---

# 👨‍💻 Autores

**Estudiantes:** Matthew Espinosa y Checho Andrade

**Materia:** Ingeniería de Software II

**Universidad:** Escuela Tecnológica Instituto Técnico Central (ETITC)
