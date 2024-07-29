from datetime import datetime # usado para el dato de las horas de salida y fechas


class Servicios:

    def __init__(self):
        codigoServicio = None
        nombre = None
        origen = None
        destino = None
        precioVenta = None
        horaSalida = None
        cantidadMaxPuestos = None
        cantidadMaxKilos = None

    # crear la tabla servicios si no existe
    def crearTablaServicios(self, objetoConexion):
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

    # escribir un servicio para insertar luego
    def leerServicio(self):
        codigoServicio = input("Código del servicio: ").ljust(10)
        nombre = input("Nombre: ").lower()
        origen = input("Ciudad de Origen: ").lower()
        destino = input("Ciudad de destino: ").lower()
        precioVenta = input("Precio de venta: ")

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
        servicio = (codigoServicio,nombre,origen,destino,precioVenta,horaSalida,puestosMaximo,kilosMaximo)
        return servicio

    # inserta un registro
    def insertarServicio(self, objetoConexion, miServicio):
        objetoCursor = objetoConexion.cursor()
        insertar = "INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        objetoCursor.execute(insertar, miServicio)
        objetoConexion.commit()
        print("Nuevo servicio insertado.")

    # consultar todos los registros
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

    # consultar la fecha y hora de salida de todos los registros
    def consultarTablaServicios2(self, objetoConexion):
        objetoCursor=objetoConexion.cursor()
        consultar = "SELECT codigoServicio, nombre, origen, date(horaSalida), time(horaSalida) FROM servicios"
        objetoCursor.execute(consultar)
        resultadosConsulta = objetoCursor.fetchall()
        if not resultadosConsulta:
            print("Tabla vacia.")
        else:
            print("Los registros de la tabla servicio son: \n")
            for n, (cs, nom, ori, fecha,hora ) in enumerate(resultadosConsulta, start=1):
                print(f"{n}. | {cs}, {nom}, {ori} | {fecha} {hora}")

    # consultar los puestos máximos y peso máximos de todos los registros
    def consultarTablaServicios3(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT codigoServicio, nombre, origen, destino, cantidadMaxPuestos, cantidadMaxKilos FROM servicios"
        objetoCursor.execute(consultar)
        resultadosConsulta = objetoCursor.fetchall()
        if not resultadosConsulta:
            print("Tabla vacia.")
        else:
            print("Los registros de la tabla servicio son: \n")
            for n, (cs, nom, ori, des, puestos, kilos) in enumerate(resultadosConsulta, start=1):
                print(f"{n}. | {cs}, {nom}, {ori}, {des} | {puestos} puestos | {kilos} kilos")

    # consultar un dato de un servicio
    def consultarTablaServicios4(self, objetoConexion, dato, codigoServicio):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT {dato} FROM servicios WHERE codigoServicio = '{codigoServicio}'"
        objetoCursor.execute(consultar)
        datoConsultado = objetoCursor.fetchone()[0]
        return datoConsultado

    # consultar cuantos registros hay en total
    def consultarTablaServicios5(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT COUNT(*) FROM servicios"
        objetoCursor.execute(consultar)
        totalRegistros = objetoCursor.fetchone()[0]
        return totalRegistros

    # consultar suma de los precios de venta
    def consultarTablaServicios6(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT SUM(precioVenta) FROM servicios"
        objetoCursor.execute(consultar)
        sumaPrecios = objetoCursor.fetchone()[0]
        return sumaPrecios

    # consultar registros por dato
    def consultarTablaServicios7(self,objetoConexion,dato,nombre):
        objetoCursor=objetoConexion.cursor()
        consultar = f"SELECT * FROM servicios WHERE {dato} = '{nombre}'"
        objetoCursor.execute(consultar)
        resultadosBusqueda = objetoCursor.fetchall()
        if not resultadosBusqueda:
            print("Busqueda fallida, no se encontraron coincidencias.")
        else:
            print("Coincidencias de busqueda: \n")
            for n, (cs, nom, ori, des, pv, fecha, puestos, kilos) in enumerate(resultadosBusqueda, start=1):
                print(f"{n}. | {cs}, {nom}, {ori}, {des}, {pv}, {fecha}| {puestos} puestos | {kilos} kilos")

    # consultar registros por letra inicial del nombre
    def consultarTablaServicios8(self, objetoConexion, letraInicial):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT * FROM servicios WHERE nombre LIKE '{letraInicial}%'"
        objetoCursor.execute(consultar)
        resultados = objetoCursor.fetchall()
        if not resultados:
            print("Dato inexistente")
        else:
            print("Coincidencias de búsqueda: \n")
            for n, (cs, nom, ori, des, pv, fecha, puestos, kilos) in enumerate(resultados, start=1):
                print(f"{n}. | {cs}, {nom}, {ori}, {des}, {pv}, {fecha}| {puestos} puestos | {kilos} kilos")

    # actualiza nombre de un registro de la trabla de servicios
    def actualizarTablaServicios(self, objetoConexion, nuevoNombre, codigoServicio):
        objetoCursor = objetoConexion.cursor()
        actualizar = f"UPDATE servicios SET nombre = '{nuevoNombre}' WHERE codigoServicio = '{codigoServicio}'"
        if objetoCursor.rowcount == 0:
            print("El registro que intenta actualizar no existe.")
        else:
            objetoCursor.execute(actualizar)
            objetoConexion.commit()

    # borra un registro
    def borrarRegistroTablaServicios(self, objetoConexion, codigoServicio):
        objetoCursor = objetoConexion.cursor()
        borrar = f"DELETE FROM servicios WHERE codigoServicio = '{codigoServicio}'"
        objetoCursor.execute(borrar)
        #si el cursor esta vacio
        if objetoCursor.rowcount == 0:
            print("El registro que intenta eliminar no existe.")
            objetoConexion.rollback()
        else:
            objetoConexion.commit()
            print("Acción borrar registro ejecutada")

    # borrar toda la tabla de servicios
    def borrarTablaServicios(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        borrar = "DROP TABLE IF EXISTS servicios"
        objetoCursor.execute(borrar)
        objetoConexion.commit()
