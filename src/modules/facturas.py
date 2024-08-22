import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


class Facturas:

    def __init__(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()

    def imprimirFactura(self, objetoVenta, objetoCliente, objetoServicio):
        mensaje = f'''
        COOPERATIVA DE TRANSPORTES LA NACIONAL
        Comprobante de venta de la factura no. {miVenta[0]}

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
        Precio total: {miServicio[4] * miVenta[3]}
        '''
        print(mensaje)
        return mensaje

    # envia la factura al correo electrónico
    def enviarCorreoFactura(self, miVenta, miCliente, miServicio):
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
        mensaje = imprimirFactura()

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
