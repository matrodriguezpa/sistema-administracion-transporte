from modulos.modulos import Modulos

class Servicios(Modulos):
    """
    Esta clase representa un servicio con atributos como código, nombre, origen, destino,
    precio de venta, hora de salida, cantidad máxima de puestos y cantidad máxima de kilos.
    """

    # Atributos de la clase
    codigo_servicio = None
    nombre = None
    origen = None
    destino = None
    precio_venta = None
    hora_salida = None
    cantidad_max_puestos = None
    cantidad_max_kilos = None

    def __init__(self, objeto_conexion):
        esquema = '''
        CREATE TABLE IF NOT EXISTS servicios(
            codigo_servicio INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            origen TEXT NOT NULL,
            destino TEXT NOT NULL,
            precio_venta INTEGER NOT NULL,
            hora_salida DATE NOT NULL,
            cantidad_max_puestos INTEGER NOT NULL,
            cantidad_max_kilos INTEGER NOT NULL,
            PRIMARY KEY(codigo_servicio)
        )'''
        super().__init__(objeto_conexion, 'servicios', esquema)

    def insertar(self, mi_servicio):
        """Inserta un nuevo servicio en la base de datos."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            insertar = "INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
            objeto_cursor.execute(insertar, mi_servicio)
            self.objeto_conexion.commit()
            print("Servicio creado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al crear el registro: {e}")
            return False
        finally:
            objeto_cursor.close()

    def actualizar(self, codigo_servicio, nuevo_nombre):
        """Actualiza el nombre de un servicio."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            actualizar = "UPDATE servicios SET nombre = ? WHERE codigo_servicio = ?"
            objeto_cursor.execute(actualizar, (nuevo_nombre, codigo_servicio))
            self.objeto_conexion.commit()
            return objeto_cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return False
        finally:
            objeto_cursor.close()

    def consultar(self, codigo_servicio):
        """Consulta la información de un servicio."""
        objeto_cursor = self.objeto_conexion.cursor()
        consultar = "SELECT * FROM servicios WHERE codigo_servicio = ?"
        try:
            objeto_cursor.execute(consultar, (codigo_servicio,))
            return objeto_cursor.fetchone()
        except Exception as e:
            print(f"Error al consultar el registro: {e}")
            return None
        finally:
            objeto_cursor.close()

    def consultar_todos(self):
        """Consulta todos los registros de la tabla servicios."""
        objeto_cursor = self.objeto_conexion.cursor()
        consultar = "SELECT * FROM servicios"  # Asumiendo que la tabla es 'servicios'
        try:
            objeto_cursor.execute(consultar)
            return objeto_cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar todos los registros: {e}")
            return None
        finally:
            objeto_cursor.close()

