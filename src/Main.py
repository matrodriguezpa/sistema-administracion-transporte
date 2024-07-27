import sqlite3
from sqlite3 import Error
from ventas_module import Ventas
from servicios_module import Servicios
from clientes_module import Clientes
from menu_module import menu

def connect_data_base():
    try:
        con = sqlite3.connect('base_datos.db')
        return con
    except Error as e:
        print(e)

def close_data_base(con):
    con.close

def main():
    miConexion=connect_data_base()
    miServicio=Servicios()
    miCliente=Clientes()
    miVenta=Ventas()
    miMenu=menu()
    miMenu.menu(miConexion,miServicio,miVenta,miCliente,miMenu)
    
    close_data_base(miConexion)

main()