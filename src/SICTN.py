import sqlite3
from sqlite3 import Error
import Ventas
import Servicios
import Clientes
import menu

def conexionDB():
    try:
        con=sqlite3.connect('miBaseDatos.db')
        return con
    except Error:
        print(Error)

def cerrarConexionDB(con):
    con.close()

def main():
    miCon=conexionDB()
    miServicio=Servicios.Servicios()
    miCliente=Clientes.Clientes()
    miVenta=Ventas.Ventas()
    
    miServicio.crearTablaServicios(miCon)
    miCliente.crearTablaClientes(miCon)
    miVenta.crearTablaVentas(miCon)
    
    menu.menu(miCon,miServicio,miVenta)
    cerrarConexionDB(miCon)
main()

