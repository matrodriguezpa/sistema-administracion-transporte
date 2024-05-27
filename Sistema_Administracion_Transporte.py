#Sistema de trasporte
import sqlite3
from sqlite3 import Error
from datetime import datetime

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
            horaSalida date NOT NULL,
            cantidadMaxPuestos integer NOT NULL,
            cantidadMaxKilos integer NOT NULL,
            PRIMARY KEY(codigoServicio)
            )
            '''
    print("Crear = ",crear)
    cursorObj.execute(crear)
    con.commit()

def leerServicio():
    codigoServicio=input("Código del servicio: ")
    codigoServicio=codigoServicio.ljust(10)
    nombre=input("Nombre: ")
    origen=input("Ciudad de Origen: ")
    destino=input("Ciudad de destino: ")
    precioVenta=input("Precio de venta: ")
    hS=input("Hora de salida (HH:MM:SS): ")
    print("Hora leida: ",hS)
    print(type(hS))
    fecha="1900:01:01:"+hS
    horaSalida=datetime.strptime(fecha,"%Y:%m:%d:%H:%M:%S")
    print("Hora convertida: ",horaSalida)
    print(type(horaSalida))
    cantidadMaxPuestos=input("Cantidad de puestos: ")
    cantidadMaxKilos=input("Peso que puede llevar: ")
    servicio=(codigoServicio,nombre,origen,destino,precioVenta,horaSalida,cantidadMaxPuestos,cantidadMaxKilos)
    print("La tupla servicio es :",servicio)
    return servicio

def insertarTablaServicios(con,miServicio):
    cursorObj=con.cursor()
    insertar="INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
    print("Insertar = ",insertar)
    cursorObj.execute(insertar,miServicio)
    con.commit()

def insertarTablaServicios2(con):
    codigoServicio=input("Código del servicio: ")
    codigoServicio=codigoServicio.ljust(10)
    cursorObj=con.cursor()
    insertar='INSERT INTO servicios VALUES('+codigoServicio+', "REMESA","CHIA","COTA","100","1900-01-01 12:15:20","10","200")'
    print("Insertar = ",insertar)
    cursorObj.execute(insertar)
    con.commit()

def consultarTablaServicios(con):
    cursorObj=con.cursor()
    consultar='SELECT codigoServicio, nombre, origen, destino, precioVenta FROM servicios'
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        cs=row[0]
        nom=row[1]
        ori=row[2]
        pv=row[4]
        print("La información del servicio es: ",cs,nom,ori,pv)

def consultarTablaServicios1(con):
    cursorObj=con.cursor()
    consultar='''SELECT codigoServicio,
                        nombre,
                        origen,
                        destino,
                        precioVenta,
                        horaSalida,
                        date(horaSalida),
                        time(horaSalida)
                FROM servicios'''
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        cs=row[0]
        nom=row[1]
        ori=row[2]
        pv=row[4]
        fecha=row[5]
        date=row[6]
        time=row[7]
        print("La información del servicio es: ",cs,nom,ori,pv,fecha,"|",date,"|",time)

def consultarTablaServicios2(con):
    cursorObj=con.cursor()
    consultar='''SELECT * FROM servicios'''
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        cs=row[0]
        nom=row[1]
        ori=row[2]
        des=row[3]
        pv=row[4]
        fecha=row[5]
        puestos=row[6]
        kilos=row[7]
        print("La información del servicio es: ",cs,nom,ori,pv,fecha,"|",puestos,"|",kilos)

def consultarTablaServicios3(con):
    cursorObj=con.cursor()
    consultar='''SELECT COUNT(*) FROM servicios'''
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        cuenta=row[0]
        print("La cantidad de registros en la base de datos es: ",cuenta)

def consultarTablaServicios4(con):
    cursorObj=con.cursor()
    consultar='''SELECT sum(precioVenta) FROM servicios'''
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        suma=row[0]
        print("La sumatoria de los precios de venta es: ",suma)

def consultarTablaServicios5(con):
    #origen=input("Ciudad de origen: ")
    cursorObj=con.cursor()
    consultar='''SELECT * FROM servicios WHERE origen="CHIA"'''
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        cs=row[0]
        nom=row[1]
        ori=row[2]
        des=row[3]
        pv=row[4]
        fecha=row[5]
        puestos=row[6]
        kilos=row[7]
        print("La información del servicio es: ",cs,nom,ori,pv,fecha,"|",puestos,"|",kilos)

def consultarTablaServicios6(con):
    origen=input("Ciudad de origen: ")
    cursorObj=con.cursor()
    consultar='SELECT * FROM servicios WHERE origen="'+origen+'"'
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        cs=row[0]
        nom=row[1]
        ori=row[2]
        des=row[3]
        pv=row[4]
        fecha=row[5]
        puestos=row[6]
        kilos=row[7]
        print("La información del servicio es: ",cs,nom,ori,pv,fecha,"|",puestos,"|",kilos)

def consultarTablaServicios7(con):
    cursorObj=con.cursor()
    consultar='SELECT * FROM servicios WHERE origen like "C%"'
    print("Consulta construida = ",consultar)
    cursorObj.execute(consultar)
    filas=cursorObj.fetchall()
    print("El tipo de dato de filas es: ",type(filas))
    for row in filas:
        cs=row[0]
        nom=row[1]
        ori=row[2]
        des=row[3]
        pv=row[4]
        fecha=row[5]
        puestos=row[6]
        kilos=row[7]
        print("La información del servicio es: ",cs,nom,ori,pv,fecha,"|",puestos,"|",kilos)

def actualizarTablaServicios(con):
    cursorObj=con.cursor()
    actualizar='UPDATE servicios SET origen="UNE" WHERE codigoServicio=2'
    print("Actualizar = ",actualizar)
    cursorObj.execute(actualizar)
    con.commit()

def actualizarTablaServicios1(con):
    nombre=input("Nombre del servicio: ")
    cursorObj=con.cursor()
    actualizar='UPDATE servicios SET nombre="'+nombre+'" WHERE codigoServicio=1'
    print("Actualizar = ",actualizar)
    cursorObj.execute(actualizar)
    con.commit()

def main():
    miCon=conexionDB()
    #crearTablaServicios(miCon)
    #servicioCreado=leerServicio()
    #insertarTablaServicios(miCon,servicioCreado)
    #insertarTablaServicios2(miCon)
    #consultarTablaServicios(miCon)
    #consultarTablaServicios1(miCon)
    #consultarTablaServicios2(miCon)
    #consultarTablaServicios3(miCon)
    #consultarTablaServicios4(miCon)
    #consultarTablaServicios5(miCon)
    #consultarTablaServicios6(miCon)
    #consultarTablaServicios7(miCon)
    #actualizarTablaServicios(miCon)
    actualizarTablaServicios1(miCon)
    cerrarConexionDB(miCon)

main()
