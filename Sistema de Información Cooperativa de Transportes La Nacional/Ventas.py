
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
        cantidadVendida=input("Cantidad a vender: ")
        cursorObj=con.cursor()
        insertar='INSERT INTO servicios VALUES('+noIdentificacionCliente+','+codigoServicio+','+cantidadVendida+')'
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
