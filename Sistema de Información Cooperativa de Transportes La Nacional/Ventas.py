
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

    def añadirServicioAVender(self,con,servicio):
        cursorObj=con.cursor()

        #si la cantidadVendida+puestosVendidos es mayor a los puestos del servicio, no lo acepta 
        while True:
            cantidadVendida=input("Cantidad a vender: ")
            try:
                puestosDisponibles=servicio.consultarTablaServicios0("cantidadMaxPuestos",codigoServicio)
                consulta = 'SELECT cantidadVendida FROM Ventas WHERE codigoServicio="'+codigoServicio+'"'
                cursorObj.execute(consulta)
                puestosVendidos=cursorObj.fetchall()
                #Hace falta sumar todos datos puestosVendidos de cada registro para tener puestosVendidosTotal
                 
                if puestosVendidos == puestosVendidos:
                    print("No hay más puestos disponibles, intente con otro servicio.")
                    break
                if puestosDisponibles>=cantidadVendida+puestosVendidos:
                    puestosVendidos = puestosVendidos+cantidadVendida
                    break
            except:print("Puestos disponibles exedidos, ingrese una cantidad menor.")

        #si el número de identificación o el codigo del serivico no existe, no lo acepta
        while True:
            noIdentificacionCliente=input("noIdentificacionCliente: ")
            codigoServicio=input("Codigo del servicio a vender: ")
            try:
                servicio.consultarTablaServicios0("nombre",codigoServicio)
                break
            except:
                print("Identificación o código invalidos.")

        #imprimir el valor y decir si acepta
        precio=servicio.consultarTablaServicios0("precio",codigoServicio)
        #cantidadVendida*precio
        #¿Acepta? (S/N):
        insertar='INSERT INTO servicios VALUES('+noIdentificacionCliente+','+codigoServicio+','+cantidadVendida+')'
        #Enviar factura al cliente? (S/N):
        #Ingrese correo electrónico
        cursorObj.execute(insertar)
        con.commit()

    #misma funcion pero para transportar cajas???

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
