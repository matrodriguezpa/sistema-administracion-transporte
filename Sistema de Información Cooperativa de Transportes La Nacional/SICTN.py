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

class Clientes:
    def __init__(self):
        noIdentificacionCliente = None
        nombre = None
        apellido = None
        direccion = None
        telefono = None
        correoElectronico = None

    def crearTablaClientes(self,con):
        cursorObj=con.cursor()
        crear='''CREATE TABLE IF NOT EXISTS Clientes(
                noIdentificacionCliente integer NOT NULL,
                nombre text NOT NULL,
                apellido text NOT NULL,
                direccion text NOT NULL,
                telefono integer NOT NULL,
                correoElectronico text NOT NULL,
                PRIMARY KEY(noIdentificacionCliente)
                )
                '''
        cursorObj.execute(crear)
        con.commit()

    def insertarTablaClientes(self,con,miCliente):
        cursorObj=con.cursor()
        insertar="INSERT INTO clientes VALUES(?,?,?,?,?,?,?,?)"
        print("Insertar = ",insertar)
        cursorObj.execute(insertar,miCliente)
        con.commit()

    def insertarTablaCLientes2(self,con):
        noIdentificacionCliente=input("Número de identificación del cliente: ")
        noIdentificacionCliente=noIdentificacionCliente.ljust(10)
        cursorObj=con.cursor()
        insertar='INSERT INTO servicios VALUES('+noIdentificacionCliente+', "REMESA","CHIA","COTA","100","1900-01-01 12:15:20","10","200")'
        print("Insertar = ",insertar)
        cursorObj.execute(insertar)
        con.commit()
    
    def consultarTablaClientes(self,con):
        cursorObj=con.cursor()
        consultar='SELECT noIdentificacionCliente, nombre, apellido, direccion, telefono, correoElectronico FROM clientes'
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            id=row[0]
            nom=row[1]
            ape=row[2]
            dir=row[3]
            tel=row[4]
            cor=row[5]
            print("La información del servicio es: ",id,nom,ape,dir,tel,cor)

    def leerCliente(self):
        noIdentificacionCliente=input("Número de identificación del cliente: ")
        noIdentificacionCliente=noIdentificacionCliente.ljust(10)
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        direccion=input("Direccion: ")
        telefono=input("Teléfono: ")
        correoElectronico=input("Correo Electrónico: ")
        cliente=(noIdentificacionCliente,nombre,apellido,direccion,telefono,correoElectronico)
        print("La tupla servicio es :",cliente)
        return cliente

    def actualizarTablaClienteNombre(self,con):
        noIdentificacionCliente=input("Numero de identificacion del cliente: ")
        nombre=input("Nuevo Nombre: ")
        cursorObj=con.cursor()
        actualizar='UPDATE clientes SET nombre="'+nombre+'" WHERE noIdentificacionCliente='+noIdentificacionCliente
        print("Actualizar Nombre = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    def borrarRegistroTablaClientes(self,con):
        noIdentificacionCliente=input("Numero de identificacion del cliente: ")
        cursorObj=con.cursor()
        borrar='DELETE FROM clientes WHERE noIdentificacionCliente='+noIdentificacionCliente
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

    def borrarTablaClientes(self,con):
        cursorObj=con.cursor()
        borrar='DROP TABLE clientes'
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

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

    #se crea la tabla servicios si no existe
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
        cursorObj.execute(crear)
        con.commit()

    #PARA QUE ES ESTA WEA
    def leerServicio(self):
        codigoServicio=input("Código del servicio: ").ljust(10)
        nombre=input("Nombre: ")
        origen=input("Ciudad de Origen: ")
        destino=input("Ciudad de destino: ")
        precioVenta=input("Precio de venta: ")

        hS=input("Hora de salida (HH:MM:SS): ")
        #FALTA OBETENER FECHA DEL SISTEMA
        fecha="1900:01:01:"+hS
        horaSalida=datetime.strptime(fecha,"%Y:%m:%d:%H:%M:%S")

        cantidadMaxPuestos=input("Cantidad de puestos: ")
        cantidadMaxKilos=input("Peso que puede llevar: ")

        servicio=(codigoServicio,nombre,origen,destino,precioVenta,horaSalida,cantidadMaxPuestos,cantidadMaxKilos)
        print("La tupla servicio es :",servicio)
        return servicio

    #inserta un registro vacio en latabla
    def insertarTablaServicios(self,con,miServicio):
        cursorObj=con.cursor()
        insertar="INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        print("Insertar = ",insertar)
        cursorObj.execute(insertar,miServicio)
        con.commit()
#AREGLAR
    #insertar un registro en la trabla servicios
    def insertarTablaServicios1(self,con):
        codigoServicio=input("Código del servicio: ")
        cursorObj=con.cursor()
        insertar='INSERT INTO servicios VALUES('+codigoServicio+', "REMESA","CHIA","COTA","100","1900-01-01 12:15:20","10","200")'
        print("Accion ejecutada = ",insertar)
        cursorObj.execute(insertar)
        con.commit()
    
    #consultar todos los registros de la tabla servicios
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
            des=row[3]
            pv=row[4]
            print("La información del servicio es: ",cs,nom,ori,des,pv)

    #consultar fecha y hora de salida
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
            des=row[3]
            fecha=row[5]
            date=row[6]
            time=row[7]
            print("La información del servicio es: ",cs,nom,ori,des,fecha,"|",date,"|",time)

    #consultar puestos máximos y peso máximos 
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
            puestos=row[6]
            kilos=row[7]
            print("La información del servicio es: ",cs,nom,ori,"|",puestos,"|",kilos)

    #consultar cuantos registros hay en la base de datos
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

    #consultar suma de los precios de las ventas
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

    #consultar registro por nombre
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
            print("La información del servicio es: ",cs,nom,ori,des,pv,fecha,"|",puestos,"|",kilos)

    #consultar registros por letra
    def consultarTablaServicios7(self,con):
        cursorObj=con.cursor()
        origen=input("Primera letra de Ciudad de origen: ")
        consultar='SELECT * FROM servicios WHERE origen like "'+origen+'%"'
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
            print("La información del servicio es: ",cs,nom,ori,des,pv,fecha,"|",puestos,"|",kilos)

    #actualiza el nombre de un registro de la trabla de servicios
    def actualizarTablaServicios(self,con):
        codigoServicio=input("Codigo del servicio a actualizar el nombre: ")
        nombre=input("Nuevo nombre del servicio: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET nombre="'+nombre+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #borra un registro
    def borrarRegistroTablaServicios(self,con):
        codigoServicio=input("Codigo del servicio a borrar: ")
        cursorObj=con.cursor()
        borrar='DELETE FROM servicios WHERE codigoServicio='+codigoServicio
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

    #borra toda la tabla
    def borrarTablaServicios(self,con):
        cursorObj=con.cursor()
        borrar='DROP TABLE servicios'
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

class Ventas:
    def __init__(self):
        noFactura = None
        noIdentificacionCliente = None
        codigoServicio = None
        cantidadVendida = None

    def crearTablaVentas(self,con):
        cursorObj=con.cursor()
        crear='''CREATE TABLE IF NOT EXISTS Ventas(
                noFactura integer NOT NULL,
                noIdentificacionCliente text NOT NULL,
                codigoServicio integer NOT NULL,
                cantidadVendida integer NOT NULL,
                PRIMARY KEY(noFactura)
                )
                '''
        cursorObj.execute(crear)
        con.commit()

    def añadirServicioAVender(self,con):
        noIdentificacionCliente=input("noIdentificacionCliente: ")
        codigoServicio=input("Codigo del servicio a vender: ")
        cantadadVendida=input("Cantidad a vender: ")
        cursorObj=con.cursor()
        insertar='INSERT INTO servicios VALUES('+noIdentificacionCliente+','+codigoServicio+','+cantadadVendida+')'
        cursorObj.execute(insertar)
        con.commit()


    #def quitarServicioAñadido():


    def imprimirFactura(self):
        print("""
                /----------FACTURA DE VENTA----------/
                            CLIENTE
                            
                            ORIGEN
                            DESTINO
                            
                            ...
                            
                            PRECIO
              """)    

def menu(miConexion,objServicios):
    salirPrincipal=False
    while not salirPrincipal:
        opcPrincipal=input('''
                           
//--------- Sistema de información Cooperativa de transportes la nacional-----------//

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
    miCliente=Clientes()
    
    miServicio.crearTablaServicios(miCon)
    miCliente.crearTablaClientes(miCon)

    miServicio.insertarTablaServicios1(miCon)
    
    menu(miCon,miServicio)
    cerrarConexionDB(miCon)

main()

