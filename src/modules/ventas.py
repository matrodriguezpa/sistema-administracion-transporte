class Ventas:
    """
    Esta clase representa una venta con atributos como número de factura, número de identificación del cliente,
    código del servicio y cantidad vendida.
    """

    # Atributos de la clase
    no_factura = None
    no_identificacion_cliente = None
    codigo_servicio = None
    cantidad_vendida = None

    def __init__(self, objeto_conexion):
        """
        Constructor de la clase Ventas. Crea la tabla 'ventas' en la base de datos si no existe.

        Args:
            objeto_conexion: Conexión a la base de datos.
        """

        objeto_cursor = objeto_conexion.cursor()
        crear = """CREATE TABLE IF NOT EXISTS ventas(
                    noFactura INTEGER NOT NULL,
                    noIdentificacionCliente INTEGER NOT NULL,
                    codigoServicio INTEGER NOT NULL,
                    cantidadVendida INTEGER NOT NULL
                )"""
        try:
            print("Creando tabla ventas, si no existe.")
            objeto_cursor.execute(crear)
            objeto_conexion.commit()
        except Exception as e:
            print(f"Error al crear la tabla 'ventas': {e}")

    def añadir_servicio_factura(self, objeto_conexion, mi_venta):
        """Registra la venta de un servicio en la base de datos.

        Args:
            objeto_conexion: Conexión a la base de datos.
            mi_venta: Tupla con los datos de la venta (número de identificación del cliente, código del servicio, cantidad vendida).

        Returns:
            bool: True si la inserción fue exitosa, False en caso contrario.
        """
        try:
            objeto_cursor = objeto_conexion.cursor()

            # Genera el número de la factura automáticamente
            consulta_no_factura = "SELECT MAX(noFactura) FROM ventas"
            objeto_cursor.execute(consulta_no_factura)
            resultado = objeto_cursor.fetchone()
            no_factura = 1 if resultado[0] is None else resultado[0] + 1

            insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
            objeto_cursor.execute(insertar, (no_factura, *mi_venta))
            objeto_conexion.commit()

            if objeto_cursor.rowcount > 0:
                print(f"Venta registrada con número de factura {no_factura}.")
                return True
            else:
                print(f"Registro de venta {mi_venta} no pudo ser creado.")
                return False
        except Exception as e:
            print(f"Error al registrar la venta: {e}")
            return False

    def quitar_servicio_factura(self, objeto_conexion, no_factura):
        """Elimina un registro de venta de la base de datos.

        Args:
            objeto_conexion: Conexión a la base de datos.
            no_factura: Número de factura de la venta a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario.
        """
        try:
            objeto_cursor = objeto_conexion.cursor()
            borrar = "DELETE FROM ventas WHERE noFactura = ?"
            objeto_cursor.execute(borrar, (no_factura,))
            objeto_conexion.commit()

            if objeto_cursor.rowcount > 0:
                print(f"Venta con número de factura {no_factura} eliminada.")
                return True
            else:
                print(f"Registro de venta con número de factura {no_factura} no encontrado.")
                return False
        except Exception as e:
            print(f"Error al eliminar la venta: {e}")
            return False
