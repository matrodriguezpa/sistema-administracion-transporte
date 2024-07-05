
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
                noIdentificacionCliente text NOT NULL,
                codigoServicio integer NOT NULL,
                cantidadVendida integer NOT NULL,
                PRIMARY KEY(noFactura)
                )
                '''
        cursorObj.execute(crear)
        con.commit()

    def leerVenta(self):
        noFactura=input("Nombre: ")
        noIdentificacionCliente=input("Número de identificación del cliente: ").ljust(10)
        codigoServicio=input("Apellido: ")
        cantidadVendida=input("Direccion: ")
        Venta=(noFactura,noIdentificacionCliente,codigoServicio,cantidadVendida)
        return Venta

    def añadirServicioAVender(self,con,venta):
        cursorObj=con.cursor()
        insertar="INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        cursorObj.execute(insertar,venta)
        con.commit()

    def consultarTablaVentas():
        return

    def consultarCantidadVendidaTotal(self,con,codigoServicio):
        cursorObj=con.cursor()
        consulta = 'SELECT sum(cantidadVendida) FROM Ventas WHERE codigoServicio="'+codigoServicio+'"'
        cursorObj.execute(consulta)
        cantidadVendidaTotal=cursorObj.fetchall()
        return cantidadVendidaTotal

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

    #imprimir una factura
    def imprimirFactura(self,con,cliente,venta):
        # Configuración del correo
        correo_origen = 'satlanacional@gmail.com'
        correo_smtp = 'smtp.gmail.com'
        puerto_smtp = 587

        # Obtener la contraseña de aplicación de manera segura
        contraseña = getpass.getpass('Introduce tu contraseña de aplicación de Google: ')

        # Obtener el destinatario y el mensaje
        correo_destino = input('Introduce el correo del destinatario: ')
        asunto = "Factura de venta no."+venta[0]
        mensaje = f'''
        TRANSPORTES LA NACIONAL

        Cliente
            Identificacion: 
            Nombre:
            Apellido:
            Direccion: 
            Telefono:
            Correo Electronico: 
        
        Viaje Transporte:
            Codigo Servicio:
            Nombre:
            Origen:
            Destino:
            Precio Venta:
            Hora Salida:  
            Cantidad: 
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