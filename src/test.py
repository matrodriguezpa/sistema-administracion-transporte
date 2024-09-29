import sqlite3
from sqlite3 import Error
from modules.clientes import Clientes
from modules.model import Model


def conectar_base_de_datos():
    """Establece una conexión con la base de datos SQLite."""
    try:
        conexion = sqlite3.connect("base_datos.db")
        return conexion
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")


def cerrar_base_de_datos(conexion):
    """Cierra la conexión con la base de datos SQLite."""
    conexion.close()

def test():
    # Suponiendo que tienes una conexión activa a la base de datos
    conexion = conectar_base_de_datos()

    # Creas una instancia de Clientes
    cliente = Clientes(conexion)

    # Verificas si Clientes hereda de Model
    print(isinstance(cliente, Model))  # Esto debería imprimir True
    print(issubclass(Clientes, Model))  # Esto también debería imprimir True

    cerrar_base_de_datos(conexion)

test()