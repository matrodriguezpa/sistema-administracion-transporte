
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

    def añadirServicioAVender(self,con,noIdentificacionCliente,codigoServicio,cantidadVender):
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

#Arreglar
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
