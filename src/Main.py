import sqlite3
from sqlite3 import Error
import ventas_module as ventas
import servicios_module as servicios
import clientes_module as clientes
import menu_module as menu

def conectar_db():
    try:
        con = sqlite3.connect('base_datos.db')
        return con
    except Error as e:
        print(e)

def cerrar_conexion_db(con):
    con.close()

def main():
    conexion = conectar_db()
    servicio = servicios.ClassServicios()
    cliente = clientes.ClassClientes()
    venta = ventas.ClassVentas()
    menu = menu.ClassMenu()
    menu.menu(conexion, servicio, venta, cliente, menu)
    
    cerrar_conexion_db(conexion)

main()