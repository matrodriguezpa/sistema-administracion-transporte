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

    def vender_servicio(self, objetoConexion, mi_venta):
        noFactura = 1  # Genera el número de la factura automáticamente
        print(f"Número de factura generado{noFactura}")

        # insertar los datos
        objetoCursor = objetoConexion.cursor()
        insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
        objetoCursor.execute(insertar, noFactura, mi_venta)
        objetoConexion.commit()
        print("Nuevo cliente agregado.")

    def quitarServicioVendido(self, objetoConexion, noFactura):
        try:
            objetoCursor = objetoConexion.cursor()
            borrar = f"DELETE FROM ventas WHERE noFactura = '{noFactura}'"
            objetoCursor.execute(borrar)
            objetoConexion.commit()
            return True
        except exception as e:
            print(f"Error al borrar el servicio vendido: {e}")
            return False