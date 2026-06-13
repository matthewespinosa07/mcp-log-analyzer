# 🍎 MCP Apple Orders Monitor

Servidor MCP desarrollado en Python para monitorear y analizar logs de un sistema de gestión de pedidos de productos Apple.

---

## 📖 Descripción del proyecto

**MCP Apple Orders Monitor** es un servidor MCP que analiza un archivo de logs (`app.log`) y expone herramientas para consultar, resumir y diagnosticar el estado operativo de un sistema de pedidos.

El proyecto simula una plataforma donde se gestionan pedidos de productos Apple, como iPhone, MacBook, iPad, Apple Watch y AirPods. El sistema genera registros relacionados con pedidos, pagos, inventario y disponibilidad de servicios.

Este proyecto fue desarrollado como parte de la materia **Ingeniería de Software II**, con el objetivo de comprender el funcionamiento del **Model Context Protocol (MCP)** y su integración con herramientas externas.

---

## 🎯 Problema que resuelve

Los sistemas empresariales generan grandes cantidades de logs que contienen información relevante sobre su funcionamiento.

En un sistema de gestión de pedidos, los logs pueden mostrar:

* Pedidos creados correctamente.
* Errores en pagos.
* Problemas de inventario.
* Advertencias operativas.
* Retrasos en sincronización.
* Fallos críticos del sistema.

Normalmente, un desarrollador o administrador tendría que revisar estos archivos manualmente. Este servidor MCP permite automatizar parte de ese análisis y obtener respuestas estructuradas desde un cliente compatible con MCP.

---

## 🧠 ¿Qué es MCP?

**Model Context Protocol (MCP)** es un estándar abierto que permite que modelos de lenguaje interactúen con herramientas y datos externos de forma organizada.

MCP permite conectar una IA con:

* Archivos.
* APIs.
* Bases de datos.
* Herramientas personalizadas.
* Sistemas externos.

En este proyecto:

* El **Host** puede ser una aplicación compatible con MCP.
* El **Cliente MCP** se comunica con el servidor.
* El **Servidor MCP** está desarrollado en Python.
* Las **Tools** son funciones que analizan el log.
* El **Resource** representa el archivo de log disponible para consulta.

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

El servidor se ejecuta localmente usando transporte `stdio`, lo que permite que MCP Inspector se comunique con el servidor y pruebe sus Tools y Resources.

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
mcp-apple-orders-monitor/
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
│   └── 05-resource-apple-orders.png
│
└── logs/
    └── app.log
```

---

## 💻 Código del servidor

El código principal del servidor MCP se encuentra en el archivo:

```text
server.py
```

Este archivo contiene la implementación del servidor usando `FastMCP`.

En `server.py` se definen las Tools del proyecto:

* `contar_lineas_log`
* `buscar_errores_log`
* `resumir_log`
* `diagnosticar_estado_pedidos`

También se define el Resource:

* `log://apple-orders`

El servidor se ejecuta mediante transporte `stdio`, lo que permite probarlo localmente usando MCP Inspector.

---

## 📄 Archivo de logs

El archivo `logs/app.log` simula eventos reales de un sistema de pedidos de productos Apple.

Ejemplo de contenido:

```text
2026-01-15 09:00:00 INFO Usuario admin inició sesión en el sistema Apple Orders
2026-01-15 09:02:15 INFO Pedido #1001 creado correctamente: iPhone 15 Pro 256GB
2026-01-15 09:04:22 INFO Pedido #1002 creado correctamente: MacBook Air M2 13 pulgadas
2026-01-15 09:06:10 WARNING Stock bajo detectado para AirPods Pro 2
2026-01-15 09:08:45 ERROR Error al procesar pago del pedido #1003: Apple Watch Series 9
2026-01-15 09:10:30 INFO Pedido #1004 enviado correctamente: iPad Pro 11 pulgadas
2026-01-15 09:12:05 ERROR Timeout al consultar pasarela de pagos para pedido #1005
2026-01-15 09:15:50 CRITICAL Servicio de inventario no disponible para validar stock de MacBook Pro
2026-01-15 09:18:20 WARNING Retraso en sincronización con bodega principal
2026-01-15 09:20:00 INFO Usuario admin cerró sesión
```

---

# 🔧 Tools implementadas

## 1️⃣ `contar_lineas_log`

Cuenta la cantidad total de líneas del archivo de log.

### Entrada

```text
app.log
```

### Resultado esperado

```json
{
  "archivo": "app.log",
  "total_lineas": 10
}
```

---

## 2️⃣ `buscar_errores_log`

Busca eventos problemáticos dentro del archivo de log.

Detecta líneas con nivel:

* `ERROR`
* `CRITICAL`

### Entrada

```text
app.log
```

### Resultado esperado

```json
{
  "archivo": "app.log",
  "total_eventos_problematicos": 3,
  "eventos": [
    {
      "linea": 5,
      "contenido": "2026-01-15 09:08:45 ERROR Error al procesar pago del pedido #1003: Apple Watch Series 9"
    },
    {
      "linea": 7,
      "contenido": "2026-01-15 09:12:05 ERROR Timeout al consultar pasarela de pagos para pedido #1005"
    },
    {
      "linea": 8,
      "contenido": "2026-01-15 09:15:50 CRITICAL Servicio de inventario no disponible para validar stock de MacBook Pro"
    }
  ]
}
```

---

## 3️⃣ `resumir_log`

Genera un resumen de eventos por nivel.

### Entrada

```text
app.log
```

### Resultado esperado

| Nivel    | Cantidad |
| -------- | -------- |
| INFO     | 5        |
| WARNING  | 2        |
| ERROR    | 2        |
| CRITICAL | 1        |

También puede verse en formato JSON:

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

## 4️⃣ `diagnosticar_estado_pedidos`

Analiza el resumen del log y determina el estado general del sistema de pedidos.

Estados posibles:

* ✅ `ESTABLE`
* 🟡 `EN_OBSERVACION`
* 🟠 `CON_ERRORES`
* 🔴 `CRITICO`

### Entrada

```text
app.log
```

### Resultado esperado

```json
{
  "archivo": "app.log",
  "estado_general": "CRITICO",
  "resumen": {
    "INFO": 5,
    "WARNING": 2,
    "ERROR": 2,
    "CRITICAL": 1
  },
  "recomendacion": "Revisar inmediatamente el servicio de inventario, ya que existe al menos un evento crítico que puede afectar la validación de stock y la continuidad de los pedidos."
}
```

---

# 📚 Resource implementado

## `log://apple-orders`

Expone el contenido completo del archivo:

```text
logs/app.log
```

Este Resource permite que un cliente MCP consulte el log operativo del sistema de pedidos Apple.

---

# ⚙️ Instalación

## 1️⃣ Clonar o descargar el proyecto

Si se clona desde GitHub:

```bash
git clone <url-del-repositorio>
cd mcp-apple-orders-monitor
```

Si el repositorio tiene otro nombre, entrar a la carpeta correspondiente. Por ejemplo:

```bash
cd mcp-log-analyzer
```

---

## 2️⃣ Crear entorno virtual

En macOS:

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

Si no existe el archivo `requirements.txt`, se puede instalar directamente la dependencia principal:

```bash
pip install "mcp[cli]"
```

Luego se puede generar el archivo `requirements.txt` con:

```bash
pip freeze > requirements.txt
```

---

# ▶️ Ejecución

Para iniciar el servidor MCP en modo desarrollo:

```bash
mcp dev server.py
```

Este comando abre **MCP Inspector**, una herramienta que permite probar las Tools y Resources del servidor MCP.

---

# 🧪 Pruebas realizadas

Las pruebas se realizaron usando **MCP Inspector**.

## ✅ Prueba 1: conexión del servidor

Se verificó que MCP Inspector se conecta correctamente al servidor:

```text
mcp-apple-orders-monitor
```

---

## ✅ Prueba 2: listado de Tools

Se verificó que el servidor expone correctamente las siguientes Tools:

```text
contar_lineas_log
buscar_errores_log
resumir_log
diagnosticar_estado_pedidos
```

---

## ✅ Prueba 3: ejecución de `resumir_log`

Entrada usada:

```text
app.log
```

Resultado esperado:

```json
{
  "INFO": 5,
  "WARNING": 2,
  "ERROR": 2,
  "CRITICAL": 1
}
```

---

## ✅ Prueba 4: ejecución de `diagnosticar_estado_pedidos`

Entrada usada:

```text
app.log
```

Resultado esperado:

```text
Estado general: CRITICO
```

Esto indica que el sistema requiere atención inmediata debido a un evento crítico relacionado con el servicio de inventario.

---

## ✅ Prueba 5: consulta del Resource

Se verificó que el Resource:

```text
log://apple-orders
```

permite consultar el contenido del archivo:

```text
logs/app.log
```

---

# 🎓 Relación con Ingeniería de Software

Este proyecto aplica conceptos de Ingeniería de Software como:

* Integración entre sistemas.
* Monitoreo de aplicaciones.
* Análisis de logs.
* Arquitectura cliente-servidor.
* Protocolos de comunicación.
* Reutilización de componentes.
* Separación de responsabilidades.
* Uso de estándares abiertos.

MCP facilita que una aplicación de inteligencia artificial pueda interactuar con herramientas externas sin crear una integración personalizada diferente para cada sistema.

---

# 📦 Entregables cubiertos

Este repositorio cubre los entregables correspondientes a la **Opción A: Implementación Práctica de un Servidor MCP Básico**:

* Código fuente del servidor MCP.
* Archivo de logs de ejemplo.
* Tools personalizadas.
* Resource personalizado.
* Instrucciones de instalación.
* Instrucciones de ejecución.
* Pruebas realizadas con MCP Inspector.
* Repositorio documentado en GitHub.

---

# ✅ Conclusiones

El proyecto demuestra cómo MCP permite conectar herramientas personalizadas con modelos de lenguaje mediante un protocolo estándar.

A través de este servidor es posible analizar logs, detectar errores, identificar eventos críticos y generar diagnósticos operativos de forma automatizada.

La solución es sencilla, pero representa un caso realista de uso empresarial: apoyar el monitoreo y diagnóstico inicial de un sistema de pedidos mediante herramientas conectadas a clientes compatibles con MCP.

---

# 👨‍💻 Autores

**Estudiantes:** Matthew Espinosa y Checho Andrade

**Materia:** Ingeniería de Software II

**Universidad:** Escuela Tecnológica Instituto Técnico Central (ETITC)
