
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

        noIdentificacionCliente=input("Número de identificación del cliente: ").ljust(10)
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        direccion=input("Direccion: ")
        telefono=input("Teléfono: ")
        correoElectronico=input("Correo Electrónico: ")

        cliente=(noIdentificacionCliente,nombre,apellido,direccion,telefono,correoElectronico)
        return cliente

    # Inserta un registro
    def insertarTablaClientes(self,con,miCliente):

        cursorObj=con.cursor()
        insertar="INSERT INTO clientes VALUES(?,?,?,?,?,?)"
        cursorObj.execute(insertar,miCliente)
        con.commit()
        print("Cliente agregado.")
    
    # Consultar todos los clientes
    def consultarTablaClientes(self, con):
        cursorObj = con.cursor()
        consultar = 'SELECT * FROM Clientes'
        cursorObj.execute(consultar)
        filas = cursorObj.fetchall()

        if not filas:
            print("Tabla vacia.")
        else:
            print("Los registro de la tabla clientes son:")
            n=1
            for row in filas:
                id = row[0]
                nom = row[1]
                ape = row[2]
                dir = row[3]
                tel = row[4]
                cor = row[5]
                print(n,"|",id,"|",nom,ape,"|",dir,"|",tel,"|",cor)
                n=n+1
    
    # Consultar un dato de un cliente
    def consultarTablaClientes1(self,con,tipoDato,noIdentificacionCliente):
        try:
            cursorObj = con.cursor()
            consultar = 'SELECT '+tipoDato+' FROM Clientes WHERE noIdentificacionCliente = "'+noIdentificacionCliente+'"'
            cursorObj.execute(consultar)
            datoConsultado = cursorObj.fetchone()
            
            if datoConsultado:
                print("El dato",tipoDato,"del registro",noIdentificacionCliente,"es",datoConsultado[0])
                return datoConsultado[0]
            else:
                print("Dato inexistente")
                return None
        except Exception as e:
                    print(f"Error al buscar el servicio! {e}")
        
    # Consultar cuantos registros hay en total 
    def consultarTablaSClientes2(self,con):
        cursorObj=con.cursor()
        consultar = "SELECT COUNT(*) FROM Clientes"
        cursorObj.execute(consultar)
        total = cursorObj.fetchone()[0]
        print("La cantidad de registros en la tabla Clientes es: ", total)
        return total
    
    # Consultar registro por nombre
    def consultarTablaClientes3(self,con,datoConsulta):
        try:
            cursorObj=con.cursor()
            consultar = 'SELECT * FROM Clientes WHERE nombre="'+datoConsulta+'"'
            cursorObj.execute(consultar)
            filas = cursorObj.fetchall()

            if not filas:
                print("Datos inexistentes")
            else:
                print("Coincidencias:")
                n=1
                for row in filas:
                    id = row[0]
                    nom = row[1]
                    ape = row[2]
                    dir = row[3]
                    tel = row[4]
                    cor = row[5]
                    print(n,"|",id,"|",nom,ape,"|",dir,"|",tel,"|",cor)
                    n=n+1
        except Exception as e:
                    print(f"Error al buscar el servicio! {e}")
    
    # Consultar registros por letra inicial del nombre
    def consultarTablaClientes4(self,con,datoConsulta):
        try:
            cursorObj = con.cursor()
            consultar = f"SELECT * FROM Clientes WHERE nombre LIKE '{datoConsulta}%'"
            cursorObj.execute(consultar)
            filas = cursorObj.fetchall()

            if not filas:
                print("Dato inexistente")
            else:
                print("Coincidencias:")
                n=1
                for row in filas:
                    id = row[0]
                    nom = row[1]
                    ape = row[2]
                    dir = row[3]
                    tel = row[4]
                    cor = row[5]
                    print(n,"|",id,"|",nom,ape,"|",dir,"|",tel,"|",cor)
                    n=n+1
        except Exception as e:
                    print(f"Error al buscar el servicio! {e}")

    # Actualizar dato de un cliente
    def actualizarTablaServicios(self, con):

        noIdentificacionCliente = input("Código del servicio a actualizar: ")
        dato = input("Nombre del dato: ")
        valorActualizado = input("Dato actualizado: ")

        actualizar = 'UPDATE Clientes SET '+dato+' = "'+valorActualizado+'" WHERE noIdentificacionCliente = "'+noIdentificacionCliente+'"'
        try:
            cursorObj= con.cursor()
            cursorObj.execute(actualizar)
            con.commit()
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            con.rollback()

    # Borra un registro
    def borrarRegistroTablaClientes(self, con, objClientes,noIdentificacionCliente):
        try:
            cursorObj= con.cursor()
            existeCliente = str(objClientes.consultarTablaClientes1(con,"noIdentificacionCliente",noIdentificacionCliente))
            if existeCliente == noIdentificacionCliente:
                borrar = 'DELETE FROM Clientes WHERE noIdentificacionCliente = "'+noIdentificacionCliente+'"'
                cursorObj.execute(borrar)
                con.commit()
                print("Acción borrar registro ejecutada")
            else:
                print("El registro que intenta eliminar no existe.")
        except Exception as e:
            print(f"Error al borrar el registro! {e}")
            con.rollback()

    # Borrar toda la tabla de clientes
    def borrarTablaClientes(self, con):
        try:
            cursorObj = con.cursor()
            borrar = 'DROP TABLE IF EXISTS Clientes'
            cursorObj.execute(borrar)
            con.commit()
            print("Tabla 'Clientes' borrada exitosamente.")
        except Exception as e:
            print(f"Error al borrar la tabla 'Clientes': {e}")