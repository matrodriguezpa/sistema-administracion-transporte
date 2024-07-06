
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Ventas:

    def __init__(self):
        noFactura = None
        noIdentificacionCliente = None
        codigoServicio = None
        cantidadVendida = None

    def crearTablaVentas(self,con):
        cursorObj=con.cursor()
        crear='''CREATE TABLE IF NOT EXISTS Ventas(
                noFactura integer NOT NULL,
                noIdentificacionCliente integer NOT NULL,
                codigoServicio integer NOT NULL,
                cantidadVendida integer NOT NULL,
                PRIMARY KEY(noFactura)
                )
                '''
        cursorObj.execute(crear)
        con.commit()

    def leerVenta(self):
        noFactura=input("noFactura: ")
        noIdentificacionCliente=input("Número de identificación del cliente (Tiene que estar registrado): ").ljust(10)
        codigoServicio=input("Código del servicio a vender: ")
        cantidadVendida=input("Cantidad a vender: ")
        Venta=(noFactura,noIdentificacionCliente,codigoServicio,cantidadVendida)
        return Venta

    def añadirServicioAVender(self,con,venta):
        cursorObj=con.cursor()
        insertar="INSERT INTO Ventas VALUES(?,?,?,?)"
        cursorObj.execute(insertar,venta)
        con.commit()
        print("Cliente agregado.")

    # Consultar registro por factura
    def consultarTablaVentas(self,con,noFactura):
        try:
            cursorObj=con.cursor()
            consultar = 'SELECT * FROM Ventas WHERE noFactura="'+noFactura+'"'
            cursorObj.execute(consultar)
            filas = cursorObj.fetchall()

            if not filas:
                print("Venta no encontrada")
            else:
                print(filas)
                return filas
        except Exception as e:
                    print(f"Error al buscar la venta! {e}")

    # Consultar todos los registros
    def consultarTablaVentas1(self, con):
        cursorObj = con.cursor()
        consultar = 'SELECT * FROM ventas'
        cursorObj.execute(consultar)
        filas = cursorObj.fetchall()

        if not filas:
            print("Tabla vacia.")
        else:
            print("Los registro de la tabla ventas son:")
            n=1
            for row in filas:
                nF = row[0]
                id = row[1]
                cs = row[2]
                can = row[3]
                print(n,"|",nF,id,cs,can)
                n=n+1


    # Consultar registro por noFactura
    def consultarTablaVentas5(self,con,noFactura):
        
        try:
            cursorObj=con.cursor()
            consultar = 'SELECT * FROM Ventas WHERE noFactura="'+noFactura+'"'
            cursorObj.execute(consultar)
            servicio = cursorObj.fetchall()

            if not servicio:
                print("Datos inexistentes")
            else:
                print("Coincidencias:")
                for row in servicio:
                    cs = row[0]
                    nom = row[1]
                    ori = row[2]
                    des = row[3]
                    print("La información de la venta  es:", cs, nom, ori, des)
            return servicio
        except Exception as e:
                    print(f"Error al buscar la venta, {e}")

    # Consultar un dato especifico de servicio
    def consultarTablaVentas2(self,con,tipoDato,noFactura):
        try:
            cursorObj = con.cursor()
            consultar = 'SELECT '+tipoDato+' FROM Ventas WHERE noFactura = "'+noFactura+'"'
            cursorObj.execute(consultar)
            datoConsultado = cursorObj.fetchone()
            
            if datoConsultado:
                print("El dato",tipoDato,"del registro",noFactura,"es",datoConsultado[0])
                return datoConsultado[0]
            else:
                print("Dato inexistente")
                return None
        except Exception as e:
                    print(f"Error al buscar el servicio! {e}")

        # Consultar cuantos registros hay en total
    def consultarTablaVentas3(self,con):
        cursorObj=con.cursor()
        consultar = "SELECT COUNT(*) FROM Ventas"
        cursorObj.execute(consultar)
        total = cursorObj.fetchone()[0]
        print("La cantidad de registros en la tabla Ventas es: ", total)
        return total
    
    # Consultar registros por letra inicial
    def consultarTablaVentas6(self,con):

        try:
            tipoDato = input("Dato a buscar: ")
            datoConsulta = input("Datos que coincidan: ")

            cursorObj = con.cursor()
            consultar = f"SELECT * FROM Ventas WHERE {tipoDato} LIKE '{datoConsulta}%'"
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
                    print("La información de la venta es:", cs, nom, ori, des)
        except Exception as e:
                    print(f"Error al buscar la venta! {e}")

    def consultarCantidadVendidaTotal(self,con,codigoServicio):
        try:
            cursorObj=con.cursor()
            consulta = 'SELECT sum(cantidadVendida) FROM Ventas WHERE codigoServicio="'+codigoServicio+'"'
            cursorObj.execute(consulta)
            resultado = cursorObj.fetchone()
            cantidadVendidaTotal = resultado[0] if resultado[0] is not None else 0 #esto es importante, no se porque
            return cantidadVendidaTotal
        except Exception as e:
                    print(f"Error al buscar la suma de ventas! {e}")
                    

    # Borra un registro
    def borrarRegistroTablaVentas(self, con):
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

    # Borrar toda la tabla de ventas
    def borrarTablaVentas(self, con):
        try:
            cursorObj=con.cursor()
            borrar = 'DROP TABLE IF EXISTS Ventas'
            cursorObj.execute(borrar)
            con.commit()
            print("Tabla 'ventas' borrada exitosamente.")
        except Exception as e:
            print(f"Error al borrar la tabla 'servicios': {e}")

    #imprimir una factura
    def imprimirFactura(self,con,venta,cliente,servicio):
        # Configuración del correo
        correo_origen = 'satlanacional@gmail.com'
        correo_smtp = 'smtp.gmail.com'
        puerto_smtp = 587

        # Obtener la contraseña de aplicación de manera segura
        contraseña = getpass.getpass('Introduce tu contraseña de aplicación de Google: ')

        # Obtener el destinatario y el mensaje
        correo_destino = input('Introduce el correo del destinatario: ')
        asunto = f"Factura de venta no.{venta[0]}"
        mensaje = f'''
        TRANSPORTES LA NACIONAL

        
        Cliente
            Identificacion: {cliente[0]}
            Nombre: {cliente[1]}
            Apellido: {cliente[2]}
            Direccion: {cliente[3]}
            Telefono: {cliente[4]}
            Correo Electronico: {cliente[5]}
        
        Transporte:
            Codigo Servicio: {servicio[0]}
            Nombre: {servicio[1]}
            Origen: {servicio[2]}
            Destino: {servicio[3]}
            Precio Venta: {servicio[4]}
            fecha: {servicio[5]}
                '''

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = correo_origen
        msg['To'] = correo_destino
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        try:
            # Conectar al servidor SMTP
            server = smtplib.SMTP(correo_smtp, puerto_smtp)
            server.starttls()
            server.login(correo_origen, contraseña)
            
            # Enviar el correo
            server.sendmail(correo_origen, correo_destino, msg.as_string())
            print('Correo enviado exitosamente')
            
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            
        finally:
            server.quit()