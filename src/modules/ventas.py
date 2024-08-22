class Ventas:

    def __init__(self, con):
        cursorObj = con.cursor()
        crear = """CREATE TABLE IF NOT EXISTS Ventas(
                noFactura integer NOT NULL,
                noIdentificacionCliente integer NOT NULL,
                codigoServicio integer NOT NULL,
                cantidadVendida integer NOT NULL,
                PRIMARY KEY(noFactura))"""
        cursorObj.execute(crear)
        con.commit()

    def venderServicio(self, objetoConexion):
        # Genera el número de la factura automáticamente
        noFactura = 1
        # Consultar la tabla para con eso crear el número de venta
        # while objetoVentas.consultarTablaVentas(objetoConexion, "noFactura", str(noFactura)) is not None:
        #   noFactura += 1
        print(f"Número de factura generado{noFactura}")
        noIdentificacionCliente = input("Número de identificación del cliente (Tiene que estar registrado): ").ljust(10)
        codigoServicio = input("Código del servicio a vender: ")
        cantidadVendida = input("Cantidad a vender: ")
        miVenta = (str(noFactura), noIdentificacionCliente, codigoServicio, cantidadVendida)
        objetoCursor = objetoConexion.cursor()
        insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
        objetoCursor.execute(insertar, )
        objetoConexion.commit()
        print("Nuevo cliente agregado.")

    def quitarServicioVendido(self, objetoConexion, noFactura):
        objetoCursor = objetoConexion.cursor()
        borrar = f"DELETE FROM ventas WHERE noFactura = '{noFactura}'"
        objetoCursor.execute(borrar)
        objetoConexion.commit()
        print("Registro borrado exitosamente.")
