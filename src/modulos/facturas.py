
class Facturas:
    def __init__(self, objetoConexion):
        self.objetoConexion = objetoConexion

    def imprimir_factura(self, no_factura):
        cursor = None
        try:
            cursor = self.objetoConexion.cursor()  # Usar la conexión del objeto correctamente

            # Obtener ventas
            query_ventas = "SELECT * FROM ventas WHERE no_factura = ?"
            cursor.execute(query_ventas, (no_factura,))
            mi_ventas = cursor.fetchall()
            if not mi_ventas:
                print(f"No se encontraron ventas para la factura {no_factura}")
                return

            # Obtener cliente
            no_identificacion_cliente = mi_ventas[0][1]  # Segunda columna de la venta
            query_cliente = "SELECT * FROM clientes WHERE no_identificacion_cliente = ?"
            cursor.execute(query_cliente, (no_identificacion_cliente,))
            mi_cliente = cursor.fetchone()
            if not mi_cliente:
                print(f"No se encontró el cliente para la factura {no_factura}")
                return

            # Generar el mensaje de la factura
            mensaje = (
                f"COOPERATIVA DE TRANSPORTES LA NACIONAL\n"
                f"Comprobante de venta de la factura No. {no_factura}\n\n"
                f"Cliente: {mi_cliente[1]} {mi_cliente[2]}\n"  # Nombre completo
                f"Dirección: {mi_cliente[3]}\n"               # Dirección
                f"Teléfono: {mi_cliente[4]}\n\n"              # Teléfono
            )

            total_general = 0
            for venta in mi_ventas:
                codigo_servicio = venta[2]  # Tercera columna de la venta
                query_servicio = "SELECT * FROM servicios WHERE codigo_servicio = ?"
                cursor.execute(query_servicio, (codigo_servicio,))
                mi_servicio = cursor.fetchone()
                if mi_servicio:
                    nombre_servicio = mi_servicio[1]
                    precio_unitario = mi_servicio[4]  # Columna de precio de venta
                    cantidad = venta[3]  # Cantidad vendida
                    precio_total = precio_unitario * cantidad
                    total_general += precio_total

                    mensaje += (
                        f"Servicio: {nombre_servicio}\n"
                        f"Hora de salida: {mi_servicio[5]}\n"
                        f"Cantidad: {cantidad}\n"
                        f"Precio unitario: {precio_unitario}\n"
                        f"Subtotal: {precio_total}\n\n"
                    )

            # Agregar la nota de pie con el precio total
            mensaje += (
                "--------------------------------------------------\n"
                f"Total general a pagar: {total_general}\n"
                "--------------------------------------------------\n"
                "Gracias por su compra."
            )

            print(mensaje)

        except Exception as e:
            print(f"Error al imprimir la factura: {e}")
        finally:
            if cursor:
                cursor.close()