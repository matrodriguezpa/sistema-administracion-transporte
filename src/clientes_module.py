
class Clientes:
    def __init__(self):
        noIdentificacionCliente = None
        nombre = None
        apellido = None
        direccion = None
        telefono = None
        correoElectronico = None

    # Crear la tabla servicios si no existe
    def crearTablaClientes(self,con):
        cursorObj=con.cursor()
        crear='''CREATE TABLE IF NOT EXISTS Clientes(
                noIdentificacionCliente integer NOT NULL,
                nombre text NOT NULL,
                apellido text NOT NULL,
                direccion text NOT NULL,
                telefono integer NOT NULL,
                correoElectronico text NOT NULL,
                PRIMARY KEY(noIdentificacionCliente)
                )
                '''
        cursorObj.execute(crear)
        con.commit()
    
    # Escribir un cliente para insertar luego
    def leerCliente(self):
        noIdentificacionCliente=input("Número de identificación del cliente: ")
        noIdentificacionCliente=noIdentificacionCliente.ljust(10)
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        direccion=input("Direccion: ")
        telefono=input("Teléfono: ")
        correoElectronico=input("Correo Electrónico: ")
        cliente=(noIdentificacionCliente,nombre,apellido,direccion,telefono,correoElectronico)
        print("La tupla Cliente es :",cliente)
        return cliente

    # Inserta un registro
    def insertarTablaClientes(self,con,miCliente):
        cursorObj=con.cursor()
        insertar="INSERT INTO clientes VALUES(?,?,?,?,?,?,?,?)"
        cursorObj.execute(insertar,miCliente)
        con.commit()
    
    # Consultar todos los registros
    def consultarTablaClientes(self,con):
        cursorObj=con.cursor()
        consultar = 'SELECT * FROM Clientes'
        cursorObj.execute(consultar)
        filas = cursorObj.fetchall()
        for fila in filas:
            print("La información del cliente es:", fila)
    
    # Consultar un dato especifico de un registro
    def consultarTablaServicios2(self,con):
        dato = input("Dato a consultar: ")
        codigoServicio = input("Código del dato: ")

        cursorObj=con.cursor()
        consultar = f'SELECT {dato} FROM servicios WHERE codigoServicio = {codigoServicio}'
        cursorObj.execute(consultar)
        resultado = cursorObj.fetchone()
        return resultado[0]

    # Actualizar dato de un registro
    def actualizarTablaClienteNombre(self,con):
        noIdentificacionCliente=input("Numero de identificacion del cliente: ")
        nombre=input("Nuevo Nombre: ")
        cursorObj=con.cursor()
        actualizar='UPDATE clientes SET nombre="'+nombre+'" WHERE noIdentificacionCliente='+noIdentificacionCliente
        cursorObj.execute(actualizar)
        con.commit()

    # Borra un registro
    def borrarRegistroTablaServicios(self, con):
        codigoServicio = input("Código del servicio a borrar: ")
        try:
            cursorObj= con.cursor()
            borrar = 'DELETE FROM servicios WHERE codigoServicio = %s'
            cursorObj.execute(borrar, (codigoServicio,))
            con.commit()
            print("Registro borrado exitosamente.")
        except Exception as e:
            print(f"Error al borrar el registro: {e}")
            con.rollback()

    # Borrar toda la tabla de servicios
    def borrarTablaServicios(self, con):
        try:
            with con.cursor() as cursorObj:
                borrar = 'DROP TABLE IF EXISTS servicios'
                print("Sentencia = ", borrar)
                cursorObj.execute(borrar)
                con.commit()
                print("Tabla 'servicios' borrada exitosamente.")
        except Exception as e:
            print(f"Error al borrar la tabla 'servicios': {e}")