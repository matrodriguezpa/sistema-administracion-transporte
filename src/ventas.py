import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


class Ventas:

    def __init__(self, con):
        cursorObj = con.cursor()
        crear = """CREATE TABLE IF NOT EXISTS Ventas(
                noFactura integer NOT NULL,
                noIdentificacionCliente integer NOT NULL,
                codigoServicio integer NOT NULL,
                cantidadVendida integer NOT NULL,
                PRIMARY KEY(noFactura))"""
        cursorObj.execute(crear)
        con.commit()

    def añadirServicioFactura(self, objetoConexion, objetoVentas):
        # Genera el número de la factura automáticamente
        noFactura = 1
        while objetoVentas.consultarTablaVentas2(objetoConexion, "noFactura", str(noFactura)) is not None:
            noFactura += 1
        print(f"Número de factura generado{noFactura}")
        noIdentificacionCliente = input("Número de identificación del cliente (Tiene que estar registrado): ").ljust(10)
        codigoServicio = input("Código del servicio a vender: ")
        cantidadVendida = input("Cantidad a vender: ")
        miVenta = (str(noFactura), noIdentificacionCliente, codigoServicio, cantidadVendida)
        objetoCursor = objetoConexion.cursor()
        insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
        objetoCursor.execute(insertar, )
        objetoConexion.commit()
        print("Nuevo cliente agregado.")

    def borrarServicioFactura(self, objetoConexion, noFactura):
        objetoCursor = objetoConexion.cursor()
        borrar = f"DELETE FROM ventas WHERE noFactura = '{noFactura}'"
        objetoCursor.execute(borrar)
        objetoConexion.commit()
        print("Registro borrado exitosamente.")

    def imprimirFactura(self, miVenta, miCliente, miServicio):
        # Configuración del correo
        correoRemitente = 'satlanacional@gmail.com'
        correoSMTP = 'smtp.gmail.com'
        puertoSMTP = 587
        tiempoEsperaSMTP = 10  # Establecer un tiempo de espera en segundos

        # Obtener la contraseña de aplicación de manera segura
        contraseña = getpass.getpass("Introduce tu contraseña de aplicación de Google: ")

        # Obtener el destinatario y el mensaje
        correoDestinatario = miCliente[5]
        asunto = f"Comprobante de venta de la factura no. {miVenta[0]}"

        # Mensaje del correo
        precioTotal = miServicio[4] * miVenta[3]
        mensaje = f'''
        COOPERATIVA DE TRANSPORTES LA NACIONAL
        Número de venta: {miVenta[0]}
        Nombre completo del cliente: {miCliente[1]} {miCliente[2]}
        Dirección del cliente: {miCliente[3]}
        Teléfono del cliente: {miCliente[4]}
        
        Nombre del producto: {miServicio[1]}
        Hora de salida: {miServicio[5]}
        Cantidad: {miVenta[3]}
        Precio unitario: {miServicio[4]}
        Precio según la cantidad: {precioTotal}

        Pie final: 
        Precio total: {precioTotal}
        '''

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = correoRemitente
        msg['To'] = correoDestinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        try:
            # Conectar al servidor SMTP con tiempo de espera
            servidor = smtplib.SMTP(correoSMTP, puertoSMTP, timeout=tiempoEsperaSMTP)
            servidor.starttls()
            servidor.login(correoRemitente, contraseña)

            # Enviar el correo
            servidor.sendmail(correoRemitente, correoDestinatario, msg.as_string())
            print('Correo enviado exitosamente.')

        except smtplib.SMTPException as e:
            print(f'Ocurrió un error con el servidor SMTP: {e}')
        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            if 'servidor' in locals():
                servidor.quit()

    # envia la factura al correo electrónico
    def enviarCorreo(self, miVenta, miCliente, miServicio):
        # Configuración del correo
        correoRemitente = 'satlanacional@gmail.com'
        correoSMTP = 'smtp.gmail.com'
        puertoSMTP = 587
        tiempoEsperaSMTP = 10  # Establecer un tiempo de espera en segundos

        # Obtener la contraseña de aplicación de manera segura
        contraseña = getpass.getpass("Introduce tu contraseña de aplicación de Google: ")

        # Obtener el destinatario y el mensaje
        correoDestinatario = miCliente[5]
        asunto = f"Comprobante de venta de la factura no. {miVenta[0]}"

        # Mensaje del correo
        precioTotal = miServicio[4] * miVenta[3]
        mensaje = f'''
        COOPERATIVA DE TRANSPORTES LA NACIONAL
        Número de venta: {miVenta[0]}
        Nombre completo del cliente: {miCliente[1]} {miCliente[2]}
        Dirección del cliente: {miCliente[3]}
        Teléfono del cliente: {miCliente[4]}

        Nombre del producto: {miServicio[1]}
        Hora de salida: {miServicio[5]}
        Cantidad: {miVenta[3]}
        Precio unitario: {miServicio[4]}
        Precio según la cantidad: {precioTotal}

        Pie final: 
        Precio total: {precioTotal}
        '''

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = correoRemitente
        msg['To'] = correoDestinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        try:
            # Conectar al servidor SMTP con tiempo de espera
            servidor = smtplib.SMTP(correoSMTP, puertoSMTP, timeout=tiempoEsperaSMTP)
            servidor.starttls()
            servidor.login(correoRemitente, contraseña)

            # Enviar el correo
            servidor.sendmail(correoRemitente, correoDestinatario, msg.as_string())
            print('Correo enviado exitosamente.')

        except smtplib.SMTPException as e:
            print(f'Ocurrió un error con el servidor SMTP: {e}')
        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            if 'servidor' in locals():
                servidor.quit()
