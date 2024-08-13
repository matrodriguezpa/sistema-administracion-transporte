from datetime import datetime # usado para el dato de las horas de salida y fechas


class Servicios:

    #se crea la tabla servicios si no existe
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

#COMBINAR LEER E INSERTAR?
    # escribir un servicio para insertar luego
    def crearServicioNuevo(self,objetoConexion):
        codigoServicio = input("Código del servicio: ").ljust(10)
        nombre = input("Nombre: ").lower()
        origen = input("Ciudad de Origen: ").lower()
        destino = input("Ciudad de destino: ").lower()
        precioVenta = input("Precio de venta: ")

        ###COMPROBACIÓN DE LOS DATOS
        #comrobar los datos sean enteros
        # comprueba si la hora ingresada esta en el formato correcto y lo junta con la fecha para crear la hora de salida
        while True:
            hora = input("Hora de salida (HH:MM:SS): ")
            fecha = datetime.now().strftime("%Y:%m:%d:")
            # comprueba el formato de la hora inserada
            try:
                fechaCompleta = fecha + hora
                horaSalida = datetime.strptime(fechaCompleta, "%Y:%m:%d:%H:%M:%S") # resultado final de la fecha
                break
            except ValueError:
                print("Error: La hora de salida debe estar en el formato 'HH:MM:SS'.")

        puestosMaximo = input("Cantidad de puestos: ")
        kilosMaximo = input("Peso que puede llevar (Kg): ")
        miServicio = (codigoServicio,nombre,origen,destino,precioVenta,horaSalida,puestosMaximo,kilosMaximo)

        #inserta el servicio
        objetoCursor = objetoConexion.cursor()
        insertar = "INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        objetoCursor.execute(insertar, miServicio)
        objetoConexion.commit()
        print("Nuevo servicio insertado.")

    # actualiza NOMBRE de servicio
    def actualizarNombreServicio(self, objetoConexion, nuevoNombre, codigoServicio):
        objetoCursor = objetoConexion.cursor()
        actualizar = f"UPDATE servicios SET nombre = '{nuevoNombre}' WHERE codigoServicio = '{codigoServicio}'"
        if objetoCursor.rowcount == 0:
            print("El registro que intenta actualizar no existe.")
        else:
            objetoCursor.execute(actualizar)
            objetoConexion.commit()

    # consultar un servicio con el nombre
    def consultarServicio(self, objetoConexion, dato, codigoServicio):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT {dato} FROM servicios WHERE codigoServicio = '{codigoServicio}'"
        objetoCursor.execute(consultar)
        datoConsultado = objetoCursor.fetchone()[0]
        return datoConsultado

###??????????????????????
    # consultar servicio
    def consultarTablaServicios1(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT * FROM servicios"
        objetoCursor.execute(consultar)
        resultadosConsulta = objetoCursor.fetchall()
        if not resultadosConsulta:
            print("Tabla vacia.")
        else:
            print("Los registros de la tabla servicio son: \n")
            for n, (cs, nom, ori, des, pv, fecha, puestos, kilos) in enumerate(resultadosConsulta, start=1):
                print(f"{n}. | {cs}, {nom}, {ori}, {des}, {pv}, {fecha}| {puestos} puestos | {kilos} kilos")

    # consultar suma de los precios de venta
    def consultarTablaServicios6(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT SUM(precioVenta) FROM servicios"
        objetoCursor.execute(consultar)
        sumaPrecios = objetoCursor.fetchone()[0]
        return sumaPrecios

    # consultar cuantos registros hay en total #AGREGAR A BUSQUEDA PRINCIPAL
    def consultarTablaServicios5(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT COUNT(*) FROM servicios"
        objetoCursor.execute(consultar)
        totalRegistros = objetoCursor.fetchone()[0]
        return totalRegistros
