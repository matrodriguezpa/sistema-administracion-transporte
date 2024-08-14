from datetime import datetime  # usado para el dato de las horas de salida y fechas


class Servicios:

    # El constructor crea la tabla servicios si no existe
    def __init__(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
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
        objetoCursor.execute(crear)
        objetoConexion.commit()

    def crearNuevoServicio(self, objetoConexion):
        codigoServicio = input("Código del servicio: ").ljust(10)
        nombre = input("Nombre: ").lower()
        origen = input("Ciudad de Origen: ").lower()
        destino = input("Ciudad de destino: ").lower()
        precioVenta = input("Precio de venta: ")

        ###COMPROBACIÓN DE LOS DATOS
        # comrobar los datos sean enteros
        # comprueba si la hora ingresada esta en el formato correcto y lo junta con la fecha para crear la hora de salida
        while True:
            hora = input("Hora de salida (HH:MM:SS): ")
            fecha = datetime.now().strftime("%Y:%m:%d:")
            # comprueba el formato de la hora inserada
            try:
                fechaCompleta = fecha + hora
                horaSalida = datetime.strptime(fechaCompleta, "%Y:%m:%d:%H:%M:%S")  # resultado final de la fecha
                break
            except ValueError:
                print("Error: La hora de salida debe estar en el formato 'HH:MM:SS'.")

        puestosMaximo = input("Cantidad de puestos: ")
        kilosMaximo = input("Peso que puede llevar (Kg): ")
        miServicio = (codigoServicio, nombre, origen, destino, precioVenta, horaSalida, puestosMaximo, kilosMaximo)

        # inserta el servicio
        objetoCursor = objetoConexion.cursor()
        insertar = "INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        objetoCursor.execute(insertar, miServicio)
        objetoConexion.commit()
        print("Nuevo servicio insertado.")

    def actualizarNombreServicio(self, objetoConexion, nuevoNombre, codigoServicio):
        objetoCursor = objetoConexion.cursor()
        actualizar = f"UPDATE servicios SET nombre = '{nuevoNombre}' WHERE codigoServicio = '{codigoServicio}'"
        if objetoCursor.rowcount == 0:
            print("El registro que intenta actualizar no existe.")
        else:
            objetoCursor.execute(actualizar)
            objetoConexion.commit()

    def consultarInformacionServicio(self, objetoConexion, codigoServicio):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT * FROM servicios WHERE codigoServicio = '{codigoServicio}'"
        objetoCursor.execute(consultar)
        datoConsultado = objetoCursor.fetchone()[0]
        return datoConsultado
