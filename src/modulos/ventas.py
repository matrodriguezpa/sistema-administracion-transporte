from modulos.modulos import Modulos

class Ventas(Modulos):
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
        esquema = '''
        CREATE TABLE IF NOT EXISTS ventas(
            no_factura INTEGER NOT NULL,
            no_identificacion_cliente INTEGER NOT NULL,
            codigo_servicio INTEGER NOT NULL,
            cantidad_vendida INTEGER NOT NULL
        )'''
        super().__init__(objeto_conexion, 'ventas', esquema)

    def insertar(self, mi_venta):
        """Inserta un nuevo registro de venta en la base de datos."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
            objeto_cursor.execute(insertar, mi_venta)
            self.objeto_conexion.commit()

            if objeto_cursor.rowcount > 0:
                print(f"Venta registrada con éxito: {mi_venta}")
                return True
            else:
                print(f"No se pudo registrar la venta: {mi_venta}")
                return False
        except Exception as e:
            print(f"Error al insertar la venta: {e}")
            return False
        finally:
            objeto_cursor.close()

    def borrar(self, no_factura, codigo_servicio, no_identificacion_cliente, cantidad_vendida):
        """Elimina un registro de venta de la base de datos."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            borrar = """
            DELETE FROM ventas 
            WHERE no_factura = ? 
            AND codigo_servicio = ? 
            AND no_identificacion_cliente = ?
            AND cantidad_vendida = ?
            """
            objeto_cursor.execute(borrar, (no_factura, codigo_servicio, no_identificacion_cliente, cantidad_vendida))
            self.objeto_conexion.commit()
            
            if objeto_cursor.rowcount > 0:
                print(f"Venta eliminada con éxito: Factura {no_factura}, Servicio {codigo_servicio}")
                return True
            else:
                print("No se encontró la venta con los parámetros proporcionados.")
                return False
        except Exception as e:
            print(f"Error al eliminar la venta: {e}")
            return False
        finally:
            objeto_cursor.close()

    def generar_numero_factura(self):
        """Genera un nuevo número de factura."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            consulta_no_factura = "SELECT MAX(no_factura) FROM ventas"
            objeto_cursor.execute(consulta_no_factura)
            resultado = objeto_cursor.fetchone()
            return 1 if resultado[0] is None else resultado[0] + 1
        except Exception as e:
            print(f"Error al generar el número de factura: {e}")
            return None
        finally:
            objeto_cursor.close()

    def verificar_disponibilidad(self, mi_servicio, cantidad_vendida, carga_max):
        """Verifica si hay disponibilidad de servicio en función de la cantidad vendida."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            consultar = "SELECT SUM(cantidad_vendida) FROM ventas WHERE codigo_servicio = ?"
            objeto_cursor.execute(consultar, (mi_servicio[0],))  # Asumiendo que el código del servicio es el índice 0
            cantidad_ocupada = objeto_cursor.fetchone()[0] or 0

            print(f"Cantidad ocupada: {cantidad_ocupada}")  # Debug info

            # Asegurarse de que mi_servicio tiene el índice correcto
            if len(mi_servicio) > carga_max:
                cantidad_espacio = mi_servicio[carga_max]  # Acceso correcto basado en la carga
                print(f"Capacidad del servicio (carga máxima): {cantidad_espacio}")
            else:
                raise ValueError("Error: El servicio no contiene suficientes datos.")

            # Verificación de disponibilidad
            return cantidad_vendida <= (cantidad_espacio - cantidad_ocupada)
        except Exception as e:
            print(f"Error al verificar disponibilidad: {e}")
            return False
        finally:
            objeto_cursor.close()

    def consultar_todos(self):
        """Consulta todos los registros de la tabla ventas."""
        objeto_cursor = self.objeto_conexion.cursor()
        consultar = "SELECT * FROM ventas"  # Asumiendo que la tabla es 'servicios'
        try:
            objeto_cursor.execute(consultar)
            return objeto_cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar todos los registros: {e}")
            return None
        finally:
            objeto_cursor.close()
