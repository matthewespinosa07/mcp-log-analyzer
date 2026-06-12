from pathlib import Path
from mcp.server.fastmcp import FastMCP


# Creamos el servidor MCP.
# Este nombre aparecerá cuando el cliente MCP se conecte.
mcp = FastMCP("mcp-log-analyzer")


# BASE_DIR representa la carpeta donde está este archivo server.py.
BASE_DIR = Path(__file__).parent

# LOGS_DIR representa la carpeta logs dentro del proyecto.
LOGS_DIR = BASE_DIR / "logs"


def obtener_ruta_segura(nombre_archivo: str) -> Path:
    """
    Construye una ruta segura hacia un archivo .log dentro de la carpeta logs.

    Esta función evita que el usuario analice archivos fuera de la carpeta permitida.
    """

    ruta = LOGS_DIR / nombre_archivo

    if not ruta.exists():
        raise FileNotFoundError(
            f"El archivo {nombre_archivo} no existe en la carpeta logs."
        )

    if ruta.suffix != ".log":
        raise ValueError("Solo se permiten archivos con extensión .log.")

    return ruta


@mcp.tool()
def contar_lineas_log(nombre_archivo: str) -> dict:
    """
    Cuenta cuántas líneas tiene un archivo .log.

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
    Busca las líneas que contienen la palabra ERROR.

    Args:
        nombre_archivo: Nombre del archivo log. Ejemplo: app.log
    """

    ruta = obtener_ruta_segura(nombre_archivo)

    errores = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            if "ERROR" in linea:
                errores.append({
                    "linea": numero_linea,
                    "contenido": linea.strip()
                })

    return {
        "archivo": nombre_archivo,
        "total_errores": len(errores),
        "errores": errores
    }


@mcp.tool()
def resumir_log(nombre_archivo: str) -> dict:
    """
    Cuenta cuántos mensajes INFO, WARNING y ERROR hay en el archivo.

    Args:
        nombre_archivo: Nombre del archivo log. Ejemplo: app.log
    """

    ruta = obtener_ruta_segura(nombre_archivo)

    resumen = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if "INFO" in linea:
                resumen["INFO"] += 1
            elif "WARNING" in linea:
                resumen["WARNING"] += 1
            elif "ERROR" in linea:
                resumen["ERROR"] += 1

    return {
        "archivo": nombre_archivo,
        "resumen": resumen
    }


@mcp.resource("log://app")
def leer_log_principal() -> str:
    """
    Expone el archivo logs/app.log como un Resource MCP.

    Un Resource es información que el modelo o cliente puede consultar.
    """

    ruta = obtener_ruta_segura("app.log")

    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


if __name__ == "__main__":
    # Ejecuta el servidor usando stdio.
    # stdio significa entrada/salida estándar.
    # Es una forma común de conectar servidores MCP locales con clientes MCP.
    mcp.run()
