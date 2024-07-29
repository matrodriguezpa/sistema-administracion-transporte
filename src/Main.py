import sqlite3
from sqlite3 import Error
from ventas import Ventas
from servicios import Servicios
from clientes import Clientes
from menu import Menu

def conectarBaseDatos():
    try:
        conexion = sqlite3.connect("baseDatos.db")
        return conexion
    except Error as e:
        print(e)

def cerrarBaseDatos(conexion):
    conexion.close

def main():
    miConexion = conectarBaseDatos()
    miServicio = Servicios()
    miCliente = Clientes()
    miVenta = Ventas()
    miMenu = Menu()

    miMenu.menu(miConexion, miServicio, miVenta, miCliente, miMenu)
    cerrarBaseDatos(miConexion)

main()
