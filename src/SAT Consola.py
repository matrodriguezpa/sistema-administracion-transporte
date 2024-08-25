import sqlite3
from sqlite3 import Error
from modules.ventas import Ventas
from modules.servicios import Servicios
from modules.clientes import Clientes
from modules.facturas import Facturas
import modules.menu


def conectarBaseDatos():
    try:
        conexion = sqlite3.connect("baseDatos.db")
        return conexion
    except Error as e:
        print(e)


def cerrarBaseDatos(conexion):
    conexion.close()


def main():
    conexionBaseDeDatos = conectarBaseDatos()
    moduloServicios = Servicios(conexionBaseDeDatos)
    moduloClientes = Clientes(conexionBaseDeDatos)
    moduloVentas = Ventas(conexionBaseDeDatos)
    moduloFacturas = Facturas(conexionBaseDeDatos)
    menuAplicacion = modules.menu

    # El menù toma la conexiòn a la dase de datos y los modulos del programa
    menuAplicacion.generar_menu(conexionBaseDeDatos, moduloServicios, moduloVentas, moduloClientes, moduloFacturas)
    cerrarBaseDatos(conexionBaseDeDatos)


main()
