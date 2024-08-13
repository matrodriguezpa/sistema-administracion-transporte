import sqlite3
from sqlite3 import Error
from ventas import Ventas
from servicios import Servicios
from clientes import Clientes
from menu import Menu

def conectar_base_datos():
    try:
        conexion = sqlite3.connect("baseDatos.db")
        return conexion
    except Error as e:
        print(e)

def cerrar_base_datos(conexion):
    conexion.close()

def main():
    mi_conexion = conectar_base_datos()
    mi_servicio = Servicios()
    mi_cliente = Clientes()
    miVenta = Ventas()
    mi_menu = Menu()

    mi_menu.menu(mi_conexion, mi_servicio, miVenta, mi_cliente, mi_menu)
    cerrar_base_datos(mi_conexion)

main()
