from modulos.modulos import Modulos

class Clientes(Modulos):
    """
    Esta clase representa un cliente con atributos como número de identificación, nombre, apellido,
    dirección, teléfono y correo electrónico.
    """

    # Atributos de la clase
    no_identificacion_cliente = None
    nombre = None
    apellido = None
    direccion = None
    telefono = None
    correo_electronico = None

    def __init__(self, objeto_conexion):
        esquema = '''
        CREATE TABLE IF NOT EXISTS clientes(
            no_identificacion_cliente INTEGER NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            apellido VARCHAR(20) NOT NULL,
            direccion TEXT NOT NULL,
            telefono INTEGER NOT NULL,
            correo_electronico VARCHAR(40) NOT NULL,
            PRIMARY KEY(no_identificacion_cliente)
        )'''
        super().__init__(objeto_conexion, 'clientes', esquema)

    def insertar(self, mi_cliente):
        """Inserta un nuevo cliente en la base de datos."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            insertar = "INSERT INTO clientes VALUES(?,?,?,?,?,?)"
            objeto_cursor.execute(insertar, mi_cliente)
            self.objeto_conexion.commit()
            print("Cliente creado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al crear el registro: {e}")
            return False
        finally:
            objeto_cursor.close()

    def actualizar(self, no_identificacion_cliente, nueva_direccion):
        """Actualiza la dirección de un cliente."""
        try:
            objeto_cursor = self.objeto_conexion.cursor()
            actualizar = "UPDATE clientes SET direccion = ? WHERE no_identificacion_cliente = ?"
            objeto_cursor.execute(actualizar, (nueva_direccion, no_identificacion_cliente))
            self.objeto_conexion.commit()
            return objeto_cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return False
        finally:
            objeto_cursor.close()

    def consultar(self, no_identificacion_cliente):
        """Consulta la información de un cliente."""
        objeto_cursor = self.objeto_conexion.cursor()
        consultar = "SELECT * FROM clientes WHERE no_identificacion_cliente = ?"
        try:
            objeto_cursor.execute(consultar, (no_identificacion_cliente,))
            return objeto_cursor.fetchone()
        except Exception as e:
            print(f"Error al consultar el registro: {e}")
            return None
        finally:
            objeto_cursor.close()

    def consultar_todos(self):
        """Consulta todos los registros de la tabla clientes."""
        objeto_cursor = self.objeto_conexion.cursor()
        consultar = "SELECT * FROM clientes"  # Asumiendo que la tabla es 'servicios'
        try:
            objeto_cursor.execute(consultar)
            return objeto_cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar todos los registros: {e}")
            return None
        finally:
            objeto_cursor.close()
