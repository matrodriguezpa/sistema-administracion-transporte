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

    def crearTablaVentas(self, con):
        cursorObj = con.cursor()
        crear = """CREATE TABLE IF NOT EXISTS Ventas(
                noFactura integer NOT NULL,
                noIdentificacionCliente integer NOT NULL,
                codigoServicio integer NOT NULL,
                cantidadVendida integer NOT NULL,
                PRIMARY KEY(noFactura))"""
        cursorObj.execute(crear)
        con.commit()

    #
    def leerVenta(self, objetoConexion, objetoVentas):
        # Genera el número de la factura automáticamente
        noFactura = 1
        while objetoVentas.consultarTablaVentas(objetoConexion, str(noFactura)) is not None:
            noFactura += 1
        print(f"Número de factura generado{noFactura}")
        noIdentificacionCliente = input("Número de identificación del cliente (Tiene que estar registrado): ").ljust(10)
        codigoServicio = input("Código del servicio a vender: ")
        cantidadVendida = input("Cantidad a vender: ")
        Venta = (str(noFactura), noIdentificacionCliente, codigoServicio, cantidadVendida)
        return Venta

    # 
    def añadirServicioAVender(self, objetoCursor, miVenta):
        objetoCursor = objetoCursor.cursor()
        insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
        objetoCursor.execute(insertar, miVenta)
        objetoCursor.commit()
        return "Venta agregada."

    # Consultar todos los registros
    def consultarTablaVentas1(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT * FROM ventas"
        objetoCursor.execute(consultar)
        resultadosConsulta = objetoCursor.fetchall()
        if not resultadosConsulta:
            print("Tabla vacia.")
        else:
            print("Los registro de la tabla ventas son:")
            for n, (nf,id,cs,can) in enumerate (resultadosConsulta, start = 1):
                print(n,"|",nf,id,cs,can)

    # Consultar un dato de una venta
    def consultarTablaVentas2(self, objetoConexion, dato, noFactura):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT {dato} FROM ventas WHERE noFactura = '{noFactura}'"
        objetoCursor.execute(consultar)
        resultadoConsulta = objetoCursor.fetchone()[0]
        if not resultadoConsulta:
            print("Dato inexistente")
        else:
            return resultadoConsulta

    # Consultar cuantos registros hay en total
    def consultarTablaVentas3(self, con):
        cursorObj = con.cursor()
        consultar = "SELECT COUNT(*) FROM ventas"
        cursorObj.execute(consultar)
        total = cursorObj.fetchone()[0]
        return total

    # Consultar registros por dato
    def consultarTablaVentas4(self, objetoConexion, dato, datoConsulta):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT * FROM ventas WHERE {dato} = '{datoConsulta}'"
        objetoCursor.execute(consultar)
        resultadosConsulta = objetoCursor.fetchall()[0]
        if not resultadosConsulta:
            print("Dato inexistente.")
        else:
            print("Coincidencias:")
            for n, (nf,id,cs,can) in enumerate (resultadosConsulta, start = 1):
                print(n,"|",nf,id,cs,can)
            return resultadosConsulta

    # Borra un registro
    def borrarRegistroTablaVentas(self, objetoConexion, noFactura):
        objetoCursor = objetoConexion.cursor()
        borrar = f"DELETE FROM ventas WHERE noFactura = '{noFactura}'"
        objetoCursor.execute(borrar)
        objetoConexion.commit()
        print("Registro borrado exitosamente.")

    # Borrar toda la tabla de ventas
    def borrarTablaVentas(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        borrar = "DROP TABLE IF EXISTS ventas"
        objetoCursor.execute(borrar)
        objetoConexion.commit()
        print("Tabla ventas borrada exitosamente.")

    # imprimir una factura
    def imprimirFactura(self,miVenta,miCliente,miServicio):
        # Configuración del correo
        correoRemitente = "satlanacional@gmail.com"
        correoSMTP = "smtp.gmail.com"
        puertoSMTP = 587

        # Obtener la contraseña de aplicación de manera segura
        contraseña = getpass.getpass("Introduce tu contraseña de aplicación de Google: ")

        # Obtener el destinatario y el mensaje
        correoDestinatario = miCliente[5]
        asunto = f"Comprobante de venta de la factura no.{miVenta[0]}"

        mensaje = f'''
                COOPERATIVA DE TRANSPORTES LA NACIONAL

        Número de venta:{miVenta[0]}
        Nombre completo del cliente: {miCliente[1],miCliente[2]}  
        Dirección del cliente: {miCliente[3]}
        Teléfono del cliente: {miCliente[4]}
        
        Nombre del producto: {miServicio[1]}
        Hora de salida:  {miServicio[5]}
        Cantidad: {miVenta[3]}
        Precio unitario: {miServicio[4]}
        Precio según la cantidad: {miServicio[4]*miVenta[3]}

        Pie final: 
        Precio total: {miServicio[4]*miVenta[3]}
        '''

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = correoRemitente
        msg['To'] = correoDestinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        try:
            # Conectar al servidor SMTP
            servidor = smtplib.SMTP(correoSMTP, puertoSMTP)
            servidor.starttls()
            servidor.login(correoRemitente, contraseña)

            # Enviar el correo
            servidor.sendmail(correoRemitente, correoDestinatario, msg.as_string())
            print('Correo enviado exitosamente')

        except Exception as e:
            print(f'Ocurrió un error: {e}')

        finally:
            servidor.quit()
