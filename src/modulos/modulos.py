
class Modulos:
    """
    Clase base para los modelos de la base de datos. Define métodos comunes para creación de tablas,
    inserción, actualización y consulta.
    """

    def __init__(self, objeto_conexion, nombre_tabla, esquema_tabla):
        """
        Constructor para inicializar la conexión y crear la tabla si no existe.

        Args:
            objeto_conexion: Conexión a la base de datos.
            nombre_tabla: Nombre de la tabla a crear.
            esquema_tabla: Esquema SQL para la creación de la tabla.
        """
        self.objeto_conexion = objeto_conexion
        self.nombre_tabla = nombre_tabla
        self.esquema_tabla = esquema_tabla
        self.crear_tabla()

    def crear_tabla(self):
        """Crea la tabla en la base de datos si no existe."""
        objeto_cursor = self.objeto_conexion.cursor()
        try:
            print(f"Cargando base de datos {self.nombre_tabla}.")
            objeto_cursor.execute(self.esquema_tabla)
            self.objeto_conexion.commit()
        except Exception as e:
            print(f"Error al crear la tabla '{self.nombre_tabla}': {e}")
        finally:
            objeto_cursor.close()  # Cerramos el cursor para evitar fugas de memoria.

    def insertar(self, datos):
        """Inserta un nuevo registro en la tabla."""
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def actualizar(self, id_registro, nuevos_datos):
        """Actualiza un registro en la tabla."""
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def consultar(self, id_registro):
        """Consulta un registro en la tabla."""
        raise NotImplementedError("Este método debe ser implementado por las subclases")
