
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

    def añadirServicioAVender(self,con,objServicios,objVentas,objClientes):
        #Preguntar si es de pasajeros o encomienda
        #Si es pasajeros, no se llena el dato de encomienda y viseversa
        while True:
            opcionTipo=input("""
                        1.Pasajero
                        2.Encomienda
                        Selecione el tipo de servicio: """)
            if opcionTipo=="1":
                cantidadMaxDato = "cantidadMaxPuestos"
                break
            elif opcionTipo=="2":
                cantidadMaxDato = "cantidadMaxKilos"
                break
        #si el número de identificación o el codigo del serivico no existe, no lo acepta
        #Arreglar, no funciona laconsulta
        #buscar otra forma de comprobar que el dato existe
        while True:
            try:
                noIdentificacionCliente ="1"
                codigoServicio = "1"
                if (objClientes.consultarTablaClientes1(con)==noIdentificacionCliente):
                    break
            except:
                print("Datos invalidos, intente otra vez")

        #si cantidadMaxima (Puestos o Kilos) > cantidadVendidaTotal+cantidadVender, no lo acepta.
        while True:
            cantidadVender=input("Cantidad a vender: ")
            try:
                cantidadMaxima=objServicios.consultarTablaServicios0(cantidadMaxDato,codigoServicio)
                cantidadVendidaTotal=objVentas.ConsultarCantidadVendidaTotal(con,objServicios)
                
                if cantidadMaxima == cantidadVendidaTotal:
                    print("No hay más puestos disponibles, intente con otro servicio.")
                if (cantidadMaxima<cantidadVendidaTotal+cantidadVender):
                    break
            except:print("Puestos disponibles exedidos, ingrese una cantidad menor.")

        cursorObj=con.cursor()
        noFactura=input("Inserte número de factura: ")
        cursorObj=con.cursor()
        insertar='INSERT INTO Ventas VALUES('+noFactura+','+noIdentificacionCliente+','+codigoServicio+', '+cantidadVender+')'
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
    def imprimirFactura(self,con,objServicio,codigoServicio,cantidadVender):
        cursorObj=con.cursor()
        consultar=objServicio.consultarTablaServicios0("precio",codigoServicio)
        precio=cursorObj.execute(consultar)
        precioTotal=cantidadVender*precio
        print("/----------FACTURA DE VENTA----------/")
        print('PRECIO:',precioTotal)
        
        opcionFactura=input("¿Enviar factura al cliente? (S/N):")
        if opcionFactura=="S":
            consultar=objServicio.consultarTablaClientes("correoElectronico",codigoServicio)
            correoElectronico=cursorObj.execute(consultar)
            #codigo para enviar factura
