class Ventas:
    """
    Esta clase representa una venta con atributos como número de factura, número de identificación del cliente,
    código del servicio y cantidad vendida.
    """
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
                    no_factura INTEGER NOT NULL,
                    no_identificacion_cliente INTEGER NOT NULL,
                    codigo_servicio INTEGER NOT NULL,
                    cantidad_vendida INTEGER NOT NULL
                )"""
        try:
            print("Cargando base de datos ventas.")
            objeto_cursor.execute(crear)
            objeto_conexion.commit()
        except Exception as e:
            print(f"Error al crear la tabla 'ventas': {e}")

    def generar_numero_factura(self, objeto_conexion):
        """Genera un nuevo número de factura."""
        objeto_cursor = objeto_conexion.cursor()
        consulta_no_factura = "SELECT MAX(no_factura) FROM ventas"
        objeto_cursor.execute(consulta_no_factura)
        resultado = objeto_cursor.fetchone()
        return 1 if resultado[0] is None else resultado[0] + 1

    def verificar_disponibilidad(self, objeto_conexion, mi_servicio, cantidad_vendida, carga_max):
        """Verifica si hay disponibilidad para la venta."""
        objeto_cursor = objeto_conexion.cursor()
        consultar = f"SELECT SUM(cantidad_vendida) FROM ventas WHERE codigo_servicio = {self.codigo_servicio}"
        objeto_cursor.execute(consultar)
        cantidad_ocupada = objeto_cursor.fetchone()[0] or 0
        cantidad_espacio = mi_servicio[carga_max]
        return cantidad_vendida <= (cantidad_espacio - cantidad_ocupada)

    def añadir_servicio_factura(self, objeto_conexion, mi_venta):
        """Registra la venta de un servicio en la base de datos."""
        try:
            objeto_cursor = objeto_conexion.cursor()
            insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
            objeto_cursor.execute(insertar, mi_venta)
            objeto_conexion.commit()

            if objeto_cursor.rowcount > 0:
                print(f"Venta registrada con número de factura {self.no_factura}.")
                return True
            else:
                print(f"Registro de venta {mi_venta} no pudo ser creado.")
                return False
        except Exception as e:
            print(f"Error al registrar la venta: {e}")
            return False

    def quitar_servicio_factura(self, objeto_conexion, no_factura, codigo_servicio, no_identificacion_cliente, cantidad_vendida):
        """Elimina un registro de venta específico de la base de datos."""
        try:
            objeto_cursor = objeto_conexion.cursor()
            borrar = """
            DELETE FROM ventas 
            WHERE no_factura = ? 
            AND codigo_servicio = ? 
            AND no_identificacion_cliente = ?
            AND cantidad_vendida = ?
            """
            objeto_cursor.execute(borrar, (no_factura, codigo_servicio, no_identificacion_cliente,cantidad_vendida))
            objeto_conexion.commit()
            if objeto_cursor.rowcount > 0:
                print(
                    f"Venta con número de factura {no_factura}, código de servicio {codigo_servicio} y número de identificación del cliente {no_identificacion_cliente} eliminada.")
                return True
            else:
                print(f"Registro de venta no encontrado con los parámetros proporcionados.")
                return False
        except Exception as e:
            print(f"Error al eliminar la venta: {e}")
            return False