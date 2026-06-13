from pathlib import Path
from mcp.server.fastmcp import FastMCP


# Creamos el servidor MCP.
# Este nombre identifica nuestro servidor dentro de un cliente MCP.
mcp = FastMCP("mcp-apple-orders-monitor")


# BASE_DIR representa la carpeta donde está este archivo server.py.
BASE_DIR = Path(__file__).parent

# LOGS_DIR representa la carpeta logs dentro del proyecto.
LOGS_DIR = BASE_DIR / "logs"


def obtener_ruta_segura(nombre_archivo: str) -> Path:
    """
    Construye una ruta segura hacia un archivo .log dentro de la carpeta logs.

    Esta función evita que el servidor lea archivos fuera de la carpeta permitida.
    """

    ruta = LOGS_DIR / nombre_archivo

    if not ruta.exists():
        raise FileNotFoundError(
            f"El archivo {nombre_archivo} no existe en la carpeta logs."
        )

    if ruta.suffix != ".log":
        raise ValueError("Solo se permiten archivos con extensión .log.")

    return ruta


def contar_niveles_log(ruta: Path) -> dict:
    """
    Cuenta cuántos eventos INFO, WARNING, ERROR y CRITICAL existen en el archivo log.

    Esta función no está expuesta directamente como Tool MCP.
    Es una función interna usada por varias Tools.
    """

    resumen = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if "CRITICAL" in linea:
                resumen["CRITICAL"] += 1
            elif "ERROR" in linea:
                resumen["ERROR"] += 1
            elif "WARNING" in linea:
                resumen["WARNING"] += 1
            elif "INFO" in linea:
                resumen["INFO"] += 1

    return resumen


@mcp.tool()
def contar_lineas_log(nombre_archivo: str) -> dict:
    """
    Cuenta cuántas líneas tiene un archivo .log del sistema de pedidos.

    Args:
        nombre_archivo: Nombre del archivo log. Ejemplo: app.log
    """

    ruta = obtener_ruta_segura(nombre_archivo)

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    return {
        "archivo": nombre_archivo,
        "total_lineas": len(lineas)
    }


@mcp.tool()
def buscar_errores_log(nombre_archivo: str) -> dict:
    """
    Busca eventos ERROR y CRITICAL en el log del sistema de pedidos.

    Args:
        nombre_archivo: Nombre del archivo log. Ejemplo: app.log
    """

    ruta = obtener_ruta_segura(nombre_archivo)

    eventos_problematicos = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            if "ERROR" in linea or "CRITICAL" in linea:
                eventos_problematicos.append({
                    "linea": numero_linea,
                    "contenido": linea.strip()
                })

    return {
        "archivo": nombre_archivo,
        "total_eventos_problematicos": len(eventos_problematicos),
        "eventos": eventos_problematicos
    }


@mcp.tool()
def resumir_log(nombre_archivo: str) -> dict:
    """
    Genera un resumen del log contando eventos INFO, WARNING, ERROR y CRITICAL.

    Args:
        nombre_archivo: Nombre del archivo log. Ejemplo: app.log
    """

    ruta = obtener_ruta_segura(nombre_archivo)
    resumen = contar_niveles_log(ruta)

    return {
        "archivo": nombre_archivo,
        "resumen": resumen
    }


@mcp.tool()
def diagnosticar_estado_pedidos(nombre_archivo: str) -> dict:
    """
    Diagnostica el estado general del sistema de gestión de pedidos Apple.

    La herramienta analiza los niveles del log y devuelve:
    - estado general del sistema;
    - resumen de eventos;
    - recomendación operativa.
    
    Args:
        nombre_archivo: Nombre del archivo log. Ejemplo: app.log
    """

    ruta = obtener_ruta_segura(nombre_archivo)
    resumen = contar_niveles_log(ruta)

    total_warning = resumen["WARNING"]
    total_error = resumen["ERROR"]
    total_critical = resumen["CRITICAL"]

    if total_critical > 0:
        estado = "CRITICO"
        recomendacion = (
            "Revisar inmediatamente el servicio de inventario, "
            "ya que existe al menos un evento crítico que puede afectar "
            "la validación de stock y la continuidad de los pedidos."
        )
    elif total_error >= 2:
        estado = "CON_ERRORES"
        recomendacion = (
            "Revisar la pasarela de pagos y los servicios externos, "
            "porque se detectaron múltiples errores en el procesamiento de pedidos."
        )
    elif total_warning > 0:
        estado = "EN_OBSERVACION"
        recomendacion = (
            "Monitorear el sistema, ya que existen advertencias relacionadas "
            "con stock o sincronización operativa."
        )
    else:
        estado = "ESTABLE"
        recomendacion = (
            "El sistema no presenta errores ni advertencias relevantes en el log analizado."
        )

    return {
        "archivo": nombre_archivo,
        "estado_general": estado,
        "resumen": resumen,
        "recomendacion": recomendacion
    }


@mcp.resource("log://apple-orders")
def leer_log_pedidos_apple() -> str:
    """
    Expone el archivo logs/app.log como un Resource MCP.

    Este Resource representa el log operativo del sistema de gestión de pedidos Apple.
    """

    ruta = obtener_ruta_segura("app.log")

    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


if __name__ == "__main__":
    # Ejecuta el servidor usando transporte stdio.
    # stdio permite que un cliente MCP local, como MCP Inspector,
    # se comunique con este servidor mediante entrada/salida estándar.
    mcp.run(transport="stdio")
