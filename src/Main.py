import sqlite3
from sqlite3 import Error
import Ventas
import Servicios
import Clientes
import menu

def connect_data_base():
    try:
        con=sqlite3.connect('miBaseDatos.db')
        return con
    except Error:
        print(Error)

def close_data_base(con):
    con.close()

def main():
    miConexion=connect_data_base()
    miServicio=Servicios.ClassServicios()
    miCliente=Clientes.ClassClientes()
    miVenta=Ventas.ClassVentas()
    miMenu=menu.ClassMenu()
    miMenu.menu(miConexion,miServicio,miVenta,miCliente,miMenu)
    
    close_data_base(miConexion)
main()