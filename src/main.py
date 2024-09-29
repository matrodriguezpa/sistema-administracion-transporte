import sqlite3
from sqlite3 import Error

from modulos.modulos import Modulos
from modulos.ventas import Ventas
from modulos.servicios import Servicios
from modulos.clientes import Clientes
from modulos.facturas import Facturas

import modulos.menu


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
    conexion = conectar_base_de_datos()

    servicios = Servicios(conexion)
    clientes = Clientes(conexion)
    ventas = Ventas(conexion)
    facturas = Facturas(conexion)

    menu_aplicacion = modulos.menu

    # El menú toma la conexión a la base de datos y los módulos del programa
    menu_aplicacion.generar_menu(servicios, ventas, clientes, facturas)

    cerrar_base_de_datos(conexion)


main()
