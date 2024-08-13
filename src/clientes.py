

class Clientes:

    # crear la tabla servicios si no existe
    def __init__(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        crear = '''CREATE TABLE IF NOT EXISTS Clientes(
                noIdentificacionCliente integer NOT NULL,
                nombre text NOT NULL,
                apellido text NOT NULL,
                direccion text NOT NULL,
                telefono integer NOT NULL,
                correoElectronico text NOT NULL,
                PRIMARY KEY(noIdentificacionCliente))
                '''
        objetoCursor.execute(crear)
        objetoConexion.commit()

    # escribir un cliente para insertar luego
    def crearNuevoCliete(self, objetoConexion):
        noIdentificacionCliente = input("Número de identificación del cliente: ").ljust(10)
        nombre = input("Nombre: ").lower()
        apellido = input("Apellido: ").lower()
        direccion = input("Direccion: ").lower()
        telefono = input("Teléfono: ")
        correoElectronico = input("Correo Electrónico: ").lower()
        miCliente = (noIdentificacionCliente, nombre, apellido, direccion, telefono, correoElectronico)
        # comrobación de datos
        objetoCursor = objetoConexion.cursor()
        insertar = "INSERT INTO clientes VALUES(?,?,?,?,?,?)"
        objetoCursor.execute(insertar, miCliente)
        objetoConexion.commit()
        print("Nuevo cliente agregado.")

    # actualizar el nombre de un cliente
    def actualizarDirecciónCliente(self, objetoConexion, nuevoNombre, noIdentificacionCliente):
        objetoCursor = objetoConexion.cursor()
        actualizar = f"UPDATE clientes SET nombre = '{nuevoNombre}' WHERE noIdentificacionCliente = '{noIdentificacionCliente}'"
        if objetoCursor.rowcount == 0:
            print("El registro que intenta actualizar no existe.")
        else:
            objetoCursor.execute(actualizar)
            objetoConexion.commit()

    # consultar registro por dato
    def consultarTablaClientes4(self, objetoConexion, noIdentificacionCliente):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT * FROM clientes WHERE noIdentificacionCliente = '{noIdentificacionCliente}'"
        objetoCursor.execute(consultar)
        resultadosBusqueda = objetoCursor.fetchall()
        if not resultadosBusqueda:
            print("Datos inexistentes")
        else:
            print("Coincidencias encontradas:")
            for n, (id, nom, ape, dir, tel, cor) in enumerate(resultadosBusqueda, start=1):
                print(f"{n}. | {id}, {nom} {ape}, {dir}, {tel}, {cor}")
            return resultadosBusqueda[0]
