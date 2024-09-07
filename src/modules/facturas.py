class Facturas:
    def __init__(self, objetoConexion):
        self.objetoConexion = objetoConexion

    def imprimir_factura(self, conexion, no_factura):
        cursor = None
        try:
            cursor = conexion.cursor()

            # Obtener ventas
            query_ventas = "SELECT * FROM ventas WHERE no_factura = ?"
            cursor.execute(query_ventas, (no_factura,))
            mi_ventas = cursor.fetchall()
            if not mi_ventas:
                print(f"No se encontraron ventas para la factura {no_factura}")
                return

            # Obtener cliente
            no_identificacion_cliente = mi_ventas[0][1]
            query_cliente = "SELECT * FROM clientes WHERE no_identificacion_cliente = ?"
            cursor.execute(query_cliente, (no_identificacion_cliente,))
            mi_cliente = cursor.fetchone()
            if not mi_cliente:
                print(f"No se encontró el cliente para la factura {no_factura}")
                return

            # Generar el mensaje de la factura
            mensaje = f"COOPERATIVA DE TRANSPORTES LA NACIONAL\nComprobante de venta de la factura no. {no_factura}\n"
            mensaje += f"""
    Nombre completo del cliente: {mi_cliente[1]} {mi_cliente[2]}
    Dirección del cliente: {mi_cliente[3]}
    Teléfono del cliente: {mi_cliente[4]}
    """

            total_general = 0
            for venta in mi_ventas:
                codigo_servicio = venta[2]
                query_servicio = "SELECT * FROM servicios WHERE codigo_servicio = ?"
                cursor.execute(query_servicio, (codigo_servicio,))
                mi_servicio = cursor.fetchone()
                if mi_servicio:
                    precio_unitario = mi_servicio[4]
                    cantidad = venta[3]
                    precio_total = precio_unitario * cantidad
                    total_general += precio_total

                    mensaje += f"""
    Nombre del producto: {mi_servicio[1]}
    Hora de salida: {mi_servicio[5]}
    Cantidad: {cantidad}
    Precio unitario: {precio_unitario}
    Precio según la cantidad: {precio_total}
    """

            mensaje += f"\nPie final:\nPrecio total: {total_general}\n"
            print(mensaje)

        except Exception as e:
            print(f"Error al imprimir la factura: {e}")
        finally:
            if cursor:
                cursor.close()