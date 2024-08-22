from datetime import datetime  # usado para el dato de las horas de salida y fechas


from datetime import datetime

class Servicios:

    def __init__(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        crear = '''CREATE TABLE IF NOT EXISTS servicios(
                codigoServicio integer NOT NULL,
                nombre text NOT NULL,
                origen text NOT NULL,
                destino text NOT NULL,
                precioVenta integer NOT NULL,
                horaSalida datetime NOT NULL,
                cantidadMaxPuestos integer NOT NULL,
                cantidadMaxKilos integer NOT NULL,
                PRIMARY KEY(codigoServicio))
                '''
        objetoCursor.execute(crear)
        objetoConexion.commit()

    def crearNuevoServicio(self, objetoConexion):
        # Validar que el código del servicio sea un número entero
        while True:
            try:
                codigoServicio = int(input("Código del servicio: ").strip())
                break
            except ValueError:
                print("Error: El código del servicio debe ser un número entero.")

        nombre = input("Nombre: ").strip().lower()
        origen = input("Ciudad de Origen: ").strip().lower()
        destino = input("Ciudad de destino: ").strip().lower()

        # Validar que el precio de venta sea un número entero
        while True:
            try:
                precioVenta = int(input("Precio de venta: ").strip())
                break
            except ValueError:
                print("Error: El precio de venta debe ser un número entero.")

        # Validar el formato de la hora de salida
        while True:
            hora = input("Hora de salida (HH:MM:SS): ").strip()
            fecha = datetime.now().strftime("%Y-%m-%d ")
            try:
                horaSalida = datetime.strptime(fecha + hora, "%Y-%m-%d %H:%M:%S")
                break
            except ValueError:
                print("Error: La hora de salida debe estar en el formato 'HH:MM:SS'.")

        # Validar que la cantidad máxima de puestos sea un número entero
        while True:
            try:
                puestosMaximo = int(input("Cantidad de puestos: ").strip())
                break
            except ValueError:
                print("Error: La cantidad de puestos debe ser un número entero.")

        # Validar que la cantidad máxima de kilos sea un número entero
        while True:
            try:
                kilosMaximo = int(input("Peso que puede llevar (Kg): ").strip())
                break
            except ValueError:
                print("Error: El peso máximo debe ser un número entero.")

        miServicio = (codigoServicio, nombre, origen, destino, precioVenta, horaSalida, puestosMaximo, kilosMaximo)

        # Inserción en la base de datos
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
