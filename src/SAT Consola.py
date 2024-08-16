import sqlite3
from sqlite3 import Error
from modulos.ventas import Ventas
from modulos.servicios import Servicios
from modulos.clientes import Clientes
from modulos.menu import Menu


def conectarBaseDatos():
    try:
        conexion = sqlite3.connect("baseDatos.db")
        return conexion
    except Error as e:
        print(e)


def cerrarBaseDatos(conexion):
    conexion.close()


def main():
    miConexion = conectarBaseDatos()
    miServicio = Servicios(miConexion)
    miCliente = Clientes(miConexion)
    miVenta = Ventas(miConexion)
    miMenu = Menu(miConexion)

    miMenu.menu(miConexion, miServicio, miVenta, miCliente, miMenu)
    cerrarBaseDatos(miConexion)


main()
