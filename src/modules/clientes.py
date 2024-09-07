class Clientes:
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
        """
        Constructor de la clase Clientes. Crea la tabla 'clientes' en la base de datos si no existe.

        Args:
            objeto_conexion: Conexión a la base de datos.
        """

        objeto_cursor = objeto_conexion.cursor()
        crear = '''CREATE TABLE IF NOT EXISTS clientes(
                no_identificacion_cliente integer NOT NULL,
                nombre varchar(20) NOT NULL,
                apellido varchar(20) NOT NULL,
                direccion text NOT NULL,
                telefono integer NOT NULL,
                correo_electronico varchar(40) NOT NULL,
                PRIMARY KEY(no_identificacion_cliente))
                '''
        try:
            print("Cargando base de datos clientes.")
            objeto_cursor.execute(crear)
            objeto_conexion.commit()
        except Exception as e:
            print(f"Error al crear la tabla 'clientes': {e}")

    def crear_nuevo_cliente(self, objeto_conexion, mi_cliente):
        """Inserta un nuevo cliente en la base de datos.

        Args:
            objeto_conexion: Conexión a la base de datos.
            mi_cliente: Tupla con los datos del cliente (número de identificación, nombre, etc.).

        Returns:
            bool: True si la inserción fue exitosa, False en caso contrario.
        """
        try:
            objeto_cursor = objeto_conexion.cursor()
            insertar = "INSERT INTO clientes VALUES(?,?,?,?,?,?)"
            objeto_cursor.execute(insertar, mi_cliente)
            objeto_conexion.commit()
            if objeto_cursor.rowcount > 0:
                print("Cliente creado exitosamente.")
                return True
            else:
                print(f"Registro {mi_cliente} no pudo ser creado.")
                return False
        except Exception as e:
            print(f"Error al crear el registro: {e}")
            return False

    def actualizar_direccion_cliente(self, objeto_conexion, no_identificacion_cliente, nueva_direccion):
        """Actualiza la dirección de un cliente.

        Args:
            objeto_conexion: Conexión a la base de datos.
            no_identificacion_cliente: Número de identificación del cliente a actualizar.
            nueva_direccion: Nueva dirección del cliente.

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.
        """
        try:
            objeto_cursor = objeto_conexion.cursor()
            actualizar = "UPDATE clientes SET direccion = ? WHERE no_identificacion_cliente = ?"
            objeto_cursor.execute(actualizar, (nueva_direccion, no_identificacion_cliente))
            objeto_conexion.commit()

            # Verificar si alguna fila fue actualizada
            if objeto_cursor.rowcount > 0:
                return True
            else:
                print(f"Registro {no_identificacion_cliente} de la tabla clientes no encontrado.")
                return False
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return False

    def consultar_informacion_cliente(self, objeto_conexion, no_identificacion_cliente):
        """Consulta la información de un cliente.

        Args:
            objeto_conexion: Conexión a la base de datos.
            no_identificacion_cliente: Número de identificación del cliente a consultar.

        Returns:
            tuple: Tupla con los datos del cliente, o None si no se encuentra.
        """
        objeto_cursor = objeto_conexion.cursor()
        consultar = "SELECT * FROM clientes WHERE no_identificacion_cliente = ?"

        try:
            objeto_cursor.execute(consultar, (no_identificacion_cliente,))
            resultado = objeto_cursor.fetchone()
            if resultado:
                return resultado
            else:
                print(f"Registro {no_identificacion_cliente} de la tabla clientes no encontrado.")
                return None
        except Exception as e:
            print(f"Error al consultar el registro: {e}")
            return None
