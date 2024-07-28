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

    def añadirServicioAVender(self, objetoCursor, miVenta):
        objetoCursor = objetoCursor.cursor()
        insertar = "INSERT INTO ventas VALUES(?,?,?,?)"
        objetoCursor.execute(insertar, miVenta)
        objetoCursor.commit()
        return "Venta agregada."

    # Consultar registro por factura
    def consultarTablaVentas1(self, objetoConexion, noFactura):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT * FROM ventas WHERE noFactura={noFactura}"
        objetoCursor.execute(consultar)
        resultadoConsulta = objetoCursor.fetchall()[0]
        if not resultadoConsulta:
            print("Venta no encontrada.")
        else:
            return resultadoConsulta

    # Consultar todos los registros
    def consultarTablaVentas2(self, objetoConexion):
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

    # consultar registro por noFactura
    def consultarTablaVentas3(self, con, noFactura):
        cursorObj=con.cursor()
        consultar = f"SELECT * FROM ventas WHERE noFactura='{noFactura}'"
        cursorObj.execute(consultar)
        resultadosConsulta = cursorObj.fetchall()
        if not resultadosConsulta:
            print("Datos inexistentes")
        else:
            print("Coincidencias:")
            for n, (nf,id,cs,can) in enumerate (resultadosConsulta, start = 1):
                print(n,"|",nf,id,cs,can)
            return resultadosConsulta

    # Consultar un dato especifico de una venta
    def consultarTablaVentas4(self, objetoConexion, dato, noFactura):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT {dato} FROM ventas WHERE noFactura = '{noFactura}'"
        objetoCursor.execute(consultar)
        resultadoConsulta = objetoCursor.fetchone()[0]
        if not resultadoConsulta:
            print("Dato inexistente")
        else:
            return resultadoConsulta

    # Consultar cuantos registros hay en total
    def consultarTablaVentas5(self, con):
        cursorObj = con.cursor()
        consultar = "SELECT COUNT(*) FROM ventas"
        cursorObj.execute(consultar)
        total = cursorObj.fetchone()[0]
        return total

    # Consultar registros por dato
    def consultarTablaVentas6(self, objetoConexion, dato, resultadosConsulta):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT * FROM ventas WHERE {dato} = '{resultadosConsulta}'"
        objetoCursor.execute(consultar)
        resultadosConsulta = objetoCursor.fetchall()
        if not resultadosConsulta:
            print("Dato inexistente")
        else:
            print("Coincidencias:")
            for n, (nf,id,cs,can) in enumerate (resultadosConsulta, start = 1):
                print(n,"|",nf,id,cs,can)
            return resultadosConsulta

    # Consultar el total de ventas
    def consultarCantidadVendidaTotal(self, objetoConexion, codigoServicio):
        objetoCursor=objetoConexion.cursor()
        consulta = "SELECT sum(cantidadVendida) FROM ventas WHERE codigoServicio = '{codigoServicio}'"
        objetoCursor.execute(consulta)
        resultadosConsulta = objetoCursor.fetchone()
        cantidadVendidaTotal = resultadosConsulta[0] #if resultado[0] is not None else 0 #esto es importante, no se porque
        return cantidadVendidaTotal

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
