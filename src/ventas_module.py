
class ClassVentas:
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

    def leerVenta(self):
        noFactura=input("Nombre: ")
        noIdentificacionCliente=input("Número de identificación del cliente: ").ljust(10)
        codigoServicio=input("Apellido: ")
        cantidadVendida=input("Direccion: ")
        Venta=(noFactura,noIdentificacionCliente,codigoServicio,cantidadVendida)
        print("La tupla Venta es :",Venta)
        return Venta

    #arreglar un poco
    def añadirServicioAVender(self,con,objServicios,objVentas,objClientes):
        #Preguntar si es de pasajeros o encomienda
        #Si es pasajeros, no se llena el dato de encomienda y viseversa
        #venta= objVentas.leerVenta()
        while True:
            opcionTipo=input("""
                        1.Pasajero
                        2.Encomienda
                        Selecione el tipo de servicio: """)
            if opcionTipo=="1":
                cantidadMaxDato = "cantidadMaxPuestos"
            elif opcionTipo=="2":
                cantidadMaxDato = "cantidadMaxKilos"
            break
        #si el número de identificación o el codigo del serivico no existe, no lo acepta
        while True:
            existeCliente = objClientes.consultarTablaClientes2(con)
            if existeCliente:
                break
            else:
                print("Intente otra otra vez")

        #si cantidadMaxima (Puestos o Kilos) > cantidadVendidaTotal+cantidadVender, no lo acepta.
        while True:
            cantidadVender=input("Cantidad a vender: ")
            try:
                cantidadMaxima=objServicios.consultarTablaServicios0(cantidadMaxDato,venta[2])
                cantidadVendidaTotal=objVentas.ConsultarCantidadVendidaTotal(con,objServicios)
                
                if cantidadMaxima == cantidadVendidaTotal:
                    print("No hay más puestos disponibles, intente con otro servicio.")
                if (cantidadMaxima>cantidadVendidaTotal+cantidadVender):
                    break
                else:
                    print("Intente otra vez, puestos disponibles: "+cantidadMaxima-cantidadVendidaTotal)
            except:print("Puestos disponibles exedidos, ingrese una cantidad menor.")

        cursorObj=con.cursor()
        noFactura=input("Inserte número de factura: ")
        cursorObj=con.cursor()
        insertar='INSERT INTO Ventas VALUES('+noFactura+','+venta[1]+','+venta[2]+', '+venta[3]+')'
        print("Accion ejecutada = ",insertar)
        cursorObj.execute(insertar)
        con.commit()

    def ConsultarCantidadVendidaTotal(self,con,codigoServicio):
        cursorObj=con.cursor()
        consulta = 'SELECT sum(cantidadVendida) FROM Ventas WHERE codigoServicio="'+codigoServicio+'"'
        cursorObj.execute(consulta)
        cantidadVendidaTotal=cursorObj.fetchall()
        return cantidadVendidaTotal

    def quitarServicioAñadido(self,con):
        cursorObj=con.cursor()
        noFactura=input("Número de la factura servicio a borrar: ")
        borrar='DELETE FROM ventas WHERE codigoServicio='+noFactura
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

    #Completar
    def imprimirFactura(self,con):
        opcionFactura=input("¿Enviar factura al cliente? (S/N):")
        while True:
            if opcionFactura=="s":
                print("")
            elif opcionFactura=="n":
                break
        
        
