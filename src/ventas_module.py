
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