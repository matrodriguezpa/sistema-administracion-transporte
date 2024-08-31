class Servicios:
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
        """
        Constructor de la clase Servicio. Crea la tabla 'servicios' en la base de datos si no existe.

        Args:
            objeto_conexion: Conexión a la base de datos.
        """

        objeto_cursor = objeto_conexion.cursor()
        crear = '''CREATE TABLE IF NOT EXISTS servicios(
                codigoServicio integer NOT NULL,
                nombre text NOT NULL,
                origen text NOT NULL,
                destino text NOT NULL,
                precioVenta integer NOT NULL,
                horaSalida date NOT NULL,
                cantidadMaxPuestos integer NOT NULL,
                cantidadMaxKilos integer NOT NULL,
                PRIMARY KEY(codigoServicio))
                '''
        try:
            print("Creando tabla servicios, si no existe.")
            objeto_cursor.execute(crear)
            objeto_conexion.commit()
        except exception as e:
            print(f"Error al crear la tabla 'servicios': {e}")

    def crear_nuevo_servicio(self, objeto_conexion, mi_servicio):
        """Inserta un nuevo servicio en la base de datos.

        Args:
            objeto_conexion: Conexión a la base de datos.
            mi_servicio: Tupla con los datos del servicio (código, nombre, etc.).

        Returns:
            bool: True si la inserción fue exitosa, False en caso contrario.
        """
        try:
            objeto_cursor = objeto_conexion.cursor()
            insertar = "INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
            objeto_cursor.execute(insertar, mi_servicio)
            objeto_conexion.commit()
            if objeto_cursor.rowcount > 0:
                print("Servicio creado exitosamente.")
                return True
            else:
                print(f"Registro {mi_servicio} no pudo ser creado.")
                return False
        except Exception as e:
            print(f"Error al crear el registro: {e}")
            return False

    def actualizar_nombre_servicio(self, objeto_conexion, codigo_servicio, nuevo_nombre):
        """Actualiza el nombre de un servicio.

        Args:
            objeto_conexion: Conexión a la base de datos.
            nuevo_nombre: Nuevo nombre del servicio.
            codigo_servicio: Código del servicio a actualizar.

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.
        """
        try:
            objeto_cursor = objeto_conexion.cursor()
            actualizar = "UPDATE servicios SET nombre = ? WHERE codigoServicio = ?"
            objeto_cursor.execute(actualizar, (nuevo_nombre, codigo_servicio))
            objeto_conexion.commit()

            # Verificar si alguna fila fue actualizada
            if objeto_cursor.rowcount > 0:
                print("Servicio actualizado exitosamente.")
                return True
            else:
                print(f"Registro {codigo_servicio} de la tabla servicios no encontrado.")
                return False
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return False


def consultar_informacion_servicio(self, objeto_conexion, codigo_servicio):
    """Consulta la información de un servicio.

    Args:
        objeto_conexion: Conexión a la base de datos.
        codigo_servicio: Código del servicio a consultar.

    Returns:
        tuple: Tupla con los datos del servicio, o None si no se encuentra.
    """

    objeto_cursor = objeto_conexion.cursor()
    consultar = "SELECT * FROM Servicios WHERE codigoServicio = ?"

    try:
        objeto_cursor.execute(consultar, (codigo_servicio,))
        resultado = objeto_cursor.fetchone()
        if resultado is not None:
            print("Servicio consultado exitosamente:")
            return resultado
        else:
            print(f"Registro {codigo_servicio} de la tabla servicios no encontrado.")
            return False
    except Exception as e:
        print(f"Error al buscar el registro: {e}")
        return False
