#Sistema de trasporte
import sqlite3
from sqlite3 import Error
def conexionDB():
    try:
        con=sqlite3.connect('miBaseDatos.db')
        return con
    except Error:
        print(Error)

def cerrarConexionDB(con):
    con.close()

def crearTablaServicios(con):
    cursorObj=con.cursor()
    crear='''CREATE TABLE IF NOT EXISTS Servicios(
            codigoServicio integer NOT NULL,
            nombre text NOT NULL,
            origen text NOT NULL,
            destino text NOT NULL,
            precioVenta integer NOT NULL,
            horaSlida date NOT NULL,
            cantidadMaxPuestos integer NOT NULL,
            cantidadMaxKilos integer NOT NULL,
            PRIMARY KEY(codigoServicio)            
            )
            '''
    print("Crear = ",crear)
    cursorObj.execute(crear)
    con.commit()
    
def main():
    miCon=conexionDB()
    crearTablaServicios(miCon)
    cerrarConexionDB(miCon)

main()
