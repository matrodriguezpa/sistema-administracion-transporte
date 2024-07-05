
from datetime import datetime # Usado para el dato de las horas de salida y fechas

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

    # Crear la tabla servicios si no existe
    def crearTablaServicios(self,con):
        cursorObj=con.cursor()
        crear='''CREATE TABLE IF NOT EXISTS Servicios(
                codigoServicio integer NOT NULL,
                nombre text NOT NULL,
                origen text NOT NULL,
                destino text NOT NULL,
                precioVenta integer NOT NULL,
                horaSalida date NOT NULL,
                cantidadMaxPuestos integer NOT NULL,
                cantidadMaxKilos integer NOT NULL,
                PRIMARY KEY(codigoServicio)
                )
                '''
        cursorObj.execute(crear)
        con.commit()

    # Escribir un servicio para insertar luego
    def leerServicio(self):
        codigoServicio=input("Código del servicio: ").ljust(10)
        nombre=input("Nombre: ")
        origen=input("Ciudad de Origen: ")
        destino=input("Ciudad de destino: ")
        precioVenta=input("Precio de venta: ")

        # Comprueba si la hora ingresada esta en el formato correcto 
        while True:
            hora = input("Hora de salida (HH:MM:SS): ")
            fecha = datetime.now().strftime("%Y:%m:%d:")
            try:
                fechaCompleta = fecha + hora
                horaSalida = datetime.strptime(fechaCompleta, "%Y:%m:%d:%H:%M:%S")
                break
            except ValueError:
                print("Error: La hora de salida debe estar en el formato HH:MM:SS.")

        cantidadMaxPuestos=input("Cantidad de puestos: ")
        cantidadMaxKilos=input("Peso que puede llevar: ")

        servicio=(codigoServicio,nombre,origen,destino,precioVenta,horaSalida,cantidadMaxPuestos,cantidadMaxKilos)
        return servicio

    # Inserta un registro
    def insertarServicio(self,con,miServicio):
        cursorObj=con.cursor()
        insertar="INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        cursorObj.execute(insertar,miServicio)
        con.commit()
    
    # Consultar todos los registros
    def consultarTablaServicios(self, con):
        cursorObj = con.cursor()
        consultar = 'SELECT * FROM servicios'
        cursorObj.execute(consultar)
        filas = cursorObj.fetchall()

        print("Los registro de la tabla servicio son:")
        n=1
        for row in filas:
            cs = row[0]
            nom = row[1]
            ori = row[2]
            des = row[3]
            pre = row[4]
            fec = row[5]
            pue = row[6]
            kil = row [7]
            print(n,"|",cs,nom,ori,des,"| $",pre,"|",fec,"|",pue,"|",kil)
            n=n+1

    # Consultar la fecha y hora de salida de todos los registros
    def consultarTablaServicios1(self,con):
        cursorObj=con.cursor()
        consultar = "SELECT codigoServicio, nombre, origen, destino, date(horaSalida), time(horaSalida) FROM servicios"
        cursorObj.execute(consultar)
        filas = cursorObj.fetchall()
        
        for row in filas:
            cs = row[0]
            nom = row[1]
            ori = row[2]
            des = row[3]
            fecha = row[4] 
            hora = row[5]  
            print(cs,nom,ori,des,"|",fecha,"|",hora)

    # Consultar los puestos máximos y peso máximos de todos los registros 
    def consultarTablaServicios2(self,con):
        cursorObj=con.cursor()
        consultar="SELECT * FROM servicios"
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()

        for row in filas:
            cs=row[0]
            nom=row[1]
            ori=row[2]
            des=row[3]
            puestos=row[6]
            kilos=row[7]
            print(cs,nom,ori,des,"|",puestos,"|",kilos)

    # Consultar un dato especifico de un registro
    def consultarTablaServicios3(self,con,tipoDato,codigoServicio):
        
        cursorObj=con.cursor()
        consultar = "SELECT "+tipoDato+" FROM servicios WHERE codigoServicio ="+codigoServicio
        cursorObj.execute(consultar)
        datoConsultado = cursorObj.fetchone()[0]

        print ("El dato",tipoDato,"del registro",codigoServicio,"es", datoConsultado)
        return datoConsultado
    
    # Consultar cuantos registros en total hay en la base de datos
    def consultarTablaServicios4(self,con):
        cursorObj=con.cursor()
        consultar = "SELECT COUNT(*) FROM servicios"
        cursorObj.execute(consultar)
        total = cursorObj.fetchone()[0]
        print("La cantidad de registros en la base de datos es: ", total)
        return total

    # Consultar suma de los precios de venta
    def consultarTablaServicios5(self,con):
        cursorObj=con.cursor()
        consultar = "SELECT SUM(precioVenta) FROM servicios"
        cursorObj.execute(consultar)
        suma = cursorObj.fetchone()[0]
        print("La sumatoria de los precios de venta es: ", suma)
        return suma

    # Consultar registro por nombre
    def consultarTablaServicios6(self,con):
        tipoDato=input("Dato a buscar: ")
        datoConsulta=input("Datos que coincidan: ")

        cursorObj=con.cursor()
        consultar = 'SELECT * FROM Servicios WHERE '+tipoDato+'="'+datoConsulta+'"'
        cursorObj.execute(consultar)
        filas = cursorObj.fetchall()

        if not filas:
            print("Dato inexistente")
        else:
            print("Coincidencias:")
            for row in filas:
                cs = row[0]
                nom = row[1]
                ori = row[2]
                des = row[3]
                pv = row[4]
                fecha = row[5]
                puestos = row[6]
                kilos = row[7]
                print("La información del servicio es:", cs, nom, ori, des, pv, fecha, "|", puestos, "|", kilos)

    # Consultar registros por letra inicial
    def consultarTablaServicios7(self,con):
        tipoDato = input("Dato a buscar: ")
        datoConsulta = input("Datos que coincidan: ")

        cursorObj = con.cursor()
        consultar = f"SELECT * FROM Servicios WHERE {tipoDato} LIKE '{datoConsulta}%'"
        cursorObj.execute(consultar)
        filas = cursorObj.fetchall()

        if not filas:
            print("Dato inexistente")
        else:
            print("Coincidencias:")
            for row in filas:
                cs = row[0]
                nom = row[1]
                ori = row[2]
                des = row[3]
                pv = row[4]
                fecha = row[5]
                puestos = row[6]
                kilos = row[7]
                print("La información del servicio es:", cs, nom, ori, des, pv, fecha, "|", puestos, "|", kilos)
    
    # Actualiza un dato de un registro de la trabla de servicios
    def actualizarTablaServicios(self, con):

        codigoServicio = input("Código del servicio a actualizar: ")
        dato = input("Nombre del dato: ")
        valorActualizado = input("Dato actualizado: ")

        actualizar = 'UPDATE Servicios SET '+dato+' = "'+valorActualizado+'" WHERE codigoServicio = "'+codigoServicio+'"'

        try:
            cursorObj= con.cursor()
            cursorObj.execute(actualizar)
            con.commit()

        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            con.rollback()

    # Borra un registro
    def borrarRegistroTablaServicios(self, con, objServicio):
        
        codigoServicio = input("Código del servicio a borrar: ")
        confirmacion = input(f"¿Estás seguro de que deseas borrar el registro {codigoServicio}? (s/n): ").lower()
        
        if confirmacion != 's':
            print("Operación cancelada.")
            return

        try:
            cursorObj= con.cursor()
            existeServicio = str(objServicio.consultarTablaServicios3(con,"codigoServicio",codigoServicio))
            if existeServicio == codigoServicio:
                borrar = 'DELETE FROM servicios WHERE codigoServicio = "'+codigoServicio+'"'
                cursorObj.execute(borrar)
                con.commit()
                print("Acción borrar registro ejecutada")
            else:
                print("El registro que intenta eliminar no existe.")
        except Exception as e:
            print(f"Error al borrar el registro, {e}")
            con.rollback()

    # Borrar toda la tabla de servicios
    def borrarTablaServicios(self, con):
        confirmacion = input("¿Estás seguro de que deseas borrar toda la tabla 'servicios'? (s/n): ").lower()
        
        if confirmacion != 's':
            print("Operación cancelada.")
            return
        
        try:
            cursorObj=con.cursor()
            borrar = 'DROP TABLE IF EXISTS servicios'
            cursorObj.execute(borrar)
            con.commit()
            print("Tabla 'servicios' borrada exitosamente.")
        except Exception as e:
            print(f"Error al borrar la tabla 'servicios': {e}")