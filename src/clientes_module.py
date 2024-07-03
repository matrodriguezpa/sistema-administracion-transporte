
class ClassClientes:
    def __init__(self):
        noIdentificacionCliente = None
        nombre = None
        apellido = None
        direccion = None
        telefono = None
        correoElectronico = None

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

    def insertarTablaClientes(self,con,miCliente):
        cursorObj=con.cursor()
        insertar="INSERT INTO clientes VALUES(?,?,?,?,?,?,?,?)"
        print("Insertar = ",insertar)
        cursorObj.execute(insertar,miCliente)
        con.commit()

    def insertarTablaCLientes2(self,con):
        noIdentificacionCliente=input("Número de identificación del cliente: ")
        noIdentificacionCliente=noIdentificacionCliente.ljust(10)
        cursorObj=con.cursor()
        insertar='INSERT INTO servicios VALUES('+noIdentificacionCliente+', "REMESA","CHIA","COTA","100","1900-01-01 12:15:20","10","200")'
        print("Insertar = ",insertar)
        cursorObj.execute(insertar)
        con.commit()
    
    def consultarTablaClientes(self,con):
        cursorObj=con.cursor()
        consultar='SELECT noIdentificacionCliente, nombre, apellido, direccion, telefono, correoElectronico FROM clientes'
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            id=row[0]
            nom=row[1]
            ape=row[2]
            dir=row[3]
            tel=row[4]
            cor=row[5]
            print("La información del servicio es: ",id,nom,ape,dir,tel,cor)
    
    def consultarTablaClientes1(self,con):
        cursorObj=con.cursor()
        dato = input("Número de indentificación del cliente: ")
        codigoServicio = input("Codigo del servicio a vender: ")
        consultar = 'SELECT noIdentificacionCliente FROM Clientes WHERE noIdentificacionCliente="'+dato+'"'
        cursorObj.execute(consultar)
        #el problema esta en que no entiendo el fetch
        resultado=cursorObj.fetchall()
        print(consultar)
        print(resultado)
        return resultado
        
    def consultarTablaClientes2(self, con):
        cursorObj = con.cursor()
        no_identificacion_cliente = input("Número de identificación de cliente: ")
        
        # Comprobar existencia en la tabla Clientes
        cursorObj.execute("SELECT noIdentificacionCliente FROM clientes WHERE noIdentificacionCliente = 1")
        registro = cursorObj.fetchone()
        print(registro)

        if registro and registro[0] == no_identificacion_cliente:
            print("Aceptado")
            return True
        else:
            print("No aceptado")

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

    def actualizarTablaClienteNombre(self,con):
        noIdentificacionCliente=input("Numero de identificacion del cliente: ")
        nombre=input("Nuevo Nombre: ")
        cursorObj=con.cursor()
        actualizar='UPDATE clientes SET nombre="'+nombre+'" WHERE noIdentificacionCliente='+noIdentificacionCliente
        print("Actualizar Nombre = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    def borrarRegistroTablaClientes(self,con):
        noIdentificacionCliente=input("Numero de identificacion del cliente: ")
        cursorObj=con.cursor()
        borrar='DELETE FROM clientes WHERE noIdentificacionCliente='+noIdentificacionCliente
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

    def borrarTablaClientes(self,con):
        cursorObj=con.cursor()
        borrar='DROP TABLE clientes'
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()