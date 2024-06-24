import sqlite3
from sqlite3 import Error
import Ventas
import Servicios
import Clientes
import Menu

def conexionDB():
    try:
        con=sqlite3.connect('miBaseDatos.db')
        return con
    except Error:
        print(Error)

def cerrarConexionDB(con):
    con.close()

def main():
    miConexion=conexionDB()
    miServicio=Servicios.ClassServicios()
    miCliente=Clientes.ClassClientes()
    miVenta=Ventas.ClassVentas()
    miMenu=Menu.ClassMenu()
    miMenu.menu(miConexion,miServicio,miVenta,miCliente,miMenu)
    
    cerrarConexionDB(miConexion)
main()

