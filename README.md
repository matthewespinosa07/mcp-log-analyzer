# 🍎 MCP Apple Orders Monitor

Servidor MCP desarrollado en Python para monitorear y analizar logs de un sistema de pedidos de productos Apple.

---

## 📖 Descripción del proyecto

**MCP Apple Orders Monitor** es un servidor MCP que analiza un archivo de logs (`app.log`) y expone herramientas para consultar, resumir y diagnosticar el estado operativo del sistema.

Este proyecto fue desarrollado como parte de la materia **Ingeniería de Software II**, con el objetivo de comprender el funcionamiento del **Model Context Protocol (MCP)** y su integración con herramientas externas.

---

## 🎯 Problema que resuelve

Los sistemas empresariales generan grandes cantidades de logs que contienen información relevante sobre:

* Pedidos creados correctamente.
* Errores en pagos.
* Problemas de inventario.
* Advertencias operativas.
* Fallos críticos del sistema.

Este servidor MCP permite automatizar el análisis de esos registros y obtener respuestas estructuradas mediante herramientas accesibles desde cualquier cliente compatible con MCP.

---

## 🧠 ¿Qué es MCP?

**Model Context Protocol (MCP)** es un estándar abierto que permite que modelos de lenguaje interactúen con:

* Archivos
* APIs
* Bases de datos
* Herramientas personalizadas
* Sistemas externos

### Arquitectura

```text
MCP Inspector
     │
     ▼
 Cliente MCP
     │
     ▼
Servidor MCP
     │
     ▼
logs/app.log
```

---

## 🛠 Tecnologías utilizadas

* Python 3
* MCP SDK para Python
* FastMCP
* MCP Inspector
* GitHub
* Visual Studio Code

---

## 📁 Estructura del proyecto

```text
mcp-apple-orders-monitor/
│
├── server.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── logs/
    └── app.log
```

---

## 📄 Archivo de logs

Ejemplo de contenido:

```text
2026-01-15 09:00:00 INFO Usuario admin inició sesión
2026-01-15 09:06:10 WARNING Stock bajo detectado
2026-01-15 09:08:45 ERROR Error al procesar pago
2026-01-15 09:15:50 CRITICAL Servicio de inventario no disponible
```

---

# 🔧 Tools implementadas

## 1️⃣ contar_lineas_log

Cuenta la cantidad total de líneas del archivo de log.

### Resultado esperado

```json
{
  "archivo": "app.log",
  "total_lineas": 10
}
```

---

## 2️⃣ buscar_errores_log

Busca eventos con nivel:

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

Genera un resumen de eventos:

| Nivel    | Cantidad |
| -------- | -------- |
| INFO     | 5        |
| WARNING  | 2        |
| ERROR    | 2        |
| CRITICAL | 1        |

---

## 4️⃣ diagnosticar_estado_pedidos

Determina el estado general del sistema.

Estados posibles:

* ✅ ESTABLE
* 🟡 EN_OBSERVACION
* 🟠 CON_ERRORES
* 🔴 CRITICO

### Ejemplo

```json
{
  "estado_general": "CRITICO"
}
```

---

# 📚 Resource implementado

## log://apple-orders

Expone el contenido completo del archivo:

```text
logs/app.log
```

para que pueda ser consultado desde un cliente MCP.

---

# ⚙️ Instalación

## Clonar el proyecto

```bash
git clone <url-del-repositorio>
cd mcp-apple-orders-monitor
```

## Crear entorno virtual

```bash
python3 -m venv .venv
```

## Activar entorno

```bash
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución

```bash
mcp dev server.py
```

Esto abrirá MCP Inspector para probar las herramientas y recursos del servidor.

---

# 🧪 Pruebas realizadas

### Listado de Tools

```text
contar_lineas_log
buscar_errores_log
resumir_log
diagnosticar_estado_pedidos
```

### Resultado de resumir_log

```json
{
  "INFO": 5,
  "WARNING": 2,
  "ERROR": 2,
  "CRITICAL": 1
}
```

### Resultado de diagnosticar_estado_pedidos

```text
Estado general: CRITICO
```

---

# 🎓 Relación con Ingeniería de Software

Este proyecto aplica conceptos de:

* Integración entre sistemas
* Monitoreo de aplicaciones
* Análisis de logs
* Arquitectura cliente-servidor
* Protocolos de comunicación
* Reutilización de componentes

---

# ✅ Conclusiones

El proyecto demuestra cómo MCP permite conectar herramientas personalizadas con modelos de lenguaje mediante un protocolo estándar.

A través de este servidor es posible analizar logs, detectar errores, identificar eventos críticos y generar diagnósticos operativos de forma automatizada.

---

# 👨‍💻 Autores

**Estudiantes:** Matthew Espinosa y Checho Andrade

**Materia:** Ingeniería de Software II

**Universidad:** Escuela Tecnológica Instituto Técnico Central
