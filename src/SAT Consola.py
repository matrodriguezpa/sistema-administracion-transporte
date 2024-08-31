import sqlite3
from sqlite3 import Error
from modules.ventas import Ventas
from modules.servicios import Servicios
from modules.clientes import Clientes
from modules.facturas import Facturas
import modules.menu


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


def main():
    """Función principal que gestiona la conexión a la base de datos y los módulos del programa."""
    conexion_base_datos = conectar_base_de_datos()

    modulo_servicios = Servicios(conexion_base_datos)
    modulo_clientes = Clientes(conexion_base_datos)
    modulo_ventas = Ventas(conexion_base_datos)
    modulo_facturas = Facturas(conexion_base_datos)

    menu_aplicacion = modules.menu

    # El menú toma la conexión a la base de datos y los módulos del programa
    menu_aplicacion.generar_menu(conexion_base_datos, modulo_servicios, modulo_ventas, modulo_clientes, modulo_facturas)

    cerrar_base_de_datos(conexion_base_datos)


main()
