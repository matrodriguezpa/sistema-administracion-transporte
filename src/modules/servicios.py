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
            objeto_cursor.execute(crear)
            objeto_conexion.commit()
        except exception as e:
            print(f"Error al crear la tabla 'servicios': {e}")

    def crear_nuevo_servicio(self, objetoConexion, miServicio):
        """Inserta un nuevo servicio en la base de datos.

        Args:
            objetoConexion: Conexión a la base de datos.
            miServicio: Tupla con los datos del servicio (código, nombre, etc.).

        Returns:
            bool: True si la inserción fue exitosa, False en caso contrario.
        """

        objeto_cursor = objetoConexion.cursor()
        insertar = "INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        try:
            objeto_cursor.execute(insertar, miServicio)
            objetoConexion.commit()
            return True
        except exception as e:
            print(f"Error al insertar el servicio: {e}")
            return False

    def actualizar_nombre(self, objeto_conexion, codigo_servicio, nuevo_nombre):
        """Actualiza el nombre de un servicio.

        Args:
            objeto_conexion: Conexión a la base de datos.
            nuevo_nombre: Nuevo nombre del servicio.
            codigo_servicio: Código del servicio a actualizar.

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.
        """

        objeto_cursor = objeto_conexion.cursor()
        actualizar = "UPDATE servicios SET nombre = ? WHERE codigoServicio = ?"
        try:
            objeto_cursor.execute(actualizar, (nuevo_nombre, codigo_servicio))
            objeto_conexion.commit()
            return True
        except exception as e:
            print(f"Error al actualizar el nombre del servicio: {e}")
            return False

    def consultar_informacion(self, objetoConexion, codigoServicio):
        """Consulta la información de un servicio.

        Args:
            objetoConexion: Conexión a la base de datos.
            codigoServicio: Código del servicio a consultar.

        Returns:
            tuple: Tupla con los datos del servicio, o None si no se encuentra.
        """

        objeto_cursor = objetoConexion.cursor()
        consultar = "SELECT * FROM servicios WHERE codigoServicio = ?"

        try:
            objeto_cursor.execute(consultar, (codigoServicio,))
            resultado = objeto_cursor.fetchone()
            return resultado
        except exception as e:
            print(f"Error al consultar la información del servicio: {e}")
            return False
