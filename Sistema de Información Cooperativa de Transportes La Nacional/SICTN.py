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

class Servicios:

    def __init__(self):
        codigoServicio = None
        nombre = None
        origen = None
        destino = None
        precioVenta = None
        horaSalida = None
        cantidadMaxPuestos = None
        cantidadMaxKilos = None
        
    def crearTablaServicios(self,con):
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

    def leerServicio(self):
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

    def insertarTablaServicios(self,con,miServicio):
        cursorObj=con.cursor()
        insertar="INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        print("Insertar = ",insertar)
        cursorObj.execute(insertar,miServicio)
        con.commit()

    def insertarTablaServicios2(self,con):
        codigoServicio=input("Código del servicio: ")
        codigoServicio=codigoServicio.ljust(10)
        cursorObj=con.cursor()
        insertar='INSERT INTO servicios VALUES('+codigoServicio+', "REMESA","CHIA","COTA","100","1900-01-01 12:15:20","10","200")'
        print("Insertar = ",insertar)
        cursorObj.execute(insertar)
        con.commit()

    def consultarTablaServicios(self,con):
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

    def consultarTablaServicios1(self,con):
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

    def consultarTablaServicios2(self,con):
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

    def consultarTablaServicios3(self,con):
        cursorObj=con.cursor()
        consultar='''SELECT COUNT(*) FROM servicios'''
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            cuenta=row[0]
            print("La cantidad de registros en la base de datos es: ",cuenta)

    def consultarTablaServicios4(self,con):
        cursorObj=con.cursor()
        consultar='''SELECT sum(precioVenta) FROM servicios'''
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            suma=row[0]
            print("La sumatoria de los precios de venta es: ",suma)

    def consultarTablaServicios5(self,con):
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

    def consultarTablaServicios6(self,con):
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

    def consultarTablaServicios7(self,con):
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

    def actualizarTablaServicios(self,con):
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET origen="UNE" WHERE codigoServicio=2'
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    def actualizarTablaServicios1(self,con):
        nombre=input("Nombre del servicio: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET nombre="'+nombre+'" WHERE codigoServicio=1'
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    def borrarRegistroTablaServicios(self,con):
        codigoServicio=input("Codigo del servicio: ")
        cursorObj=con.cursor()
        borrar='DELETE FROM servicios WHERE codigoServicio='+codigoServicio
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

    def borrarTablaServicios(self,con):
        cursorObj=con.cursor()
        borrar='DROP TABLE servicios'
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

def menu(miConexion,objServicios):
    salirPrincipal=False
    while not salirPrincipal:
        opcPrincipal=input('''
//-------- Sistema de información Cooperativa de transportes la nacional-----------//

                    //---MENU PRINCIPAL---//

                    
                1.Menú de gestión de Servicios
                2.Menú de gestión de Clientes
                3.Menú de Ventas
                4.Imprimir factura
                5.Salir

                Seleccione una opción: ''')
        if(opcPrincipal=='1'):
            salirServicios=False
            while not salirServicios:
                opcServicios=input('''

                    //---SERVICIOS---//

                1.Insertar un servicio leido por teclado
                2.Insertar un sevicio
                3.consultar un servicio

                ...
                
                13.Salir

                Seleccione una opción: ''')
                
                if(opcServicios=='1'):
                    servicioCreado=objServicios.leerServicio()
                    objServicios.insertarTablaServicios(miConexion,servicioCreado)
                if(opcServicios=='2'):
                    objServicios.insertarTablaServicios2(miConexion)
                if(opcServicios=='3'):
                    objServicios.consultarTablaServicios(miConexion)
                if(opcServicios=='13'):
                    salirServicios=True
        elif(opcPrincipal=='2'):
            salirPrincipal=True
        elif(opcPrincipal=='3'):
            salirPrincipal=True
        elif(opcPrincipal=='4'):
            salirPrincipal=True
        elif(opcPrincipal=='5'):
            salirPrincipal=True

def main():
    miCon=conexionDB()
    miServicio=Servicios()
    miServicio.crearTablaServicios(miCon)
    menu(miCon,miServicio)
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
    #actualizarTablaServicios1(miCon)
    #borrarRegistroTablaServicios(miCon)
    #borrarTablaServicios(miCon)
    cerrarConexionDB(miCon)

main()
