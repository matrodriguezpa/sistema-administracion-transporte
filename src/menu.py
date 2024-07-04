
class ClassMenu:
    def mostrar_menu_principal(self):
        return input('''
             ____        _      _____  
            / ___|      / \    |_   _| 
           | (___      / _ \     | |   
            \___ \    / /_\ \    | |   
            ____) |  / _____ \   | |   
           |_____/  /_/     \_\  |_|   

        SISTEMA DE ADMINISTRACIÓN DE TRANSPORTES 
                    LA NACIONAL

        MENU PRINCIPAL
        1. Modulo de Ventas
        2. Modulo de gestión de Clientes
        3. Modulo de gestión de Servicios

        Seleccione una opción: ''')

    def menu_ventas(self,miConexion, objServicios, objVentas,objClientes):
        salirVentas = False
        while not salirVentas:
            opcionVentas = input('''
            MODULO VENTAS
            1. Vender un servicio.
            2. Imprimir factura.
            3. Volver.

            Seleccione una opción:  ''')

            if opcionVentas == '1':
                objVentas.añadirServicioAVender(miConexion, objServicios, objVentas,objClientes)
                while True:
                    opcionFactura = input("¿Imprimir factura? (S/N): ")
                    if opcionFactura.upper() == "S":
                        objVentas.imprimirFactura()
                    break
            elif opcionVentas == '2':
                objVentas.imprimirFactura()
            elif opcionVentas == '3':
                salirVentas = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def menu_gestion_clientes(self):
        salirClientes = False
        while not salirClientes:
            opcionClientes = input('''
            MODULO CLIENTES
            1. Insertar un servicio leído por el teclado.
            2. Volver.

            Seleccione una opción:  ''')

            if opcionClientes == '1':
                # Aquí iría la lógica para insertar un servicio leído por el teclado
                pass
            elif opcionClientes == '2':
                salirClientes = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def menu_gestion_servicios(self,miConexion, objServicios):
        salirServicios = False
        while not salirServicios:
            opcionServicios = input('''
            MODULO SERVICIOS
            1. Insertar un servicio leído por el teclado.
            2. Consultar todos los registros de la tabla servicios.
            3. Consultar fecha y hora de salida.
            4. Consultar puestos máximos y peso máximos.
            5. Consultar cuántos registros hay en la base de datos.
            6. Consultar suma de los precios de las ventas.
            7. Consultar registro por nombre.
            8. Consultar registros por letra.
            9. Actualizar el nombre de un registro.
            10. Actualizar el origen de un registro.
            11. Actualizar el destino de un registro.
            12. Actualizar el precio de venta de un registro.
            13. Actualizar la hora de salida de un registro.
            14. Actualizar la cantidad máxima de puestos de un registro.
            15. Actualizar la cantidad máxima de kilos de un registro.
            16. Borrar un registro.
            17. Borrar la tabla servicios.
            18. Volver.

            Seleccione una opción: ''')

            if opcionServicios == '1':
                servicioCreado = objServicios.leerServicio()
                objServicios.insertarTablaServicios(miConexion, servicioCreado)
            elif opcionServicios == '2':
                objServicios.consultarTablaServicios0(miConexion)
            elif opcionServicios == '13':
                salirServicios = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def menu(self,miConexion,objServicios,objVentas,objClientes,objMenu):
        objServicios.crearTablaServicios(miConexion)
        objClientes.crearTablaClientes(miConexion)
        objVentas.crearTablaVentas(miConexion)

        salirPrincipal = False
        while not salirPrincipal:
            opcPrincipal = objMenu.mostrar_menu_principal()
            if opcPrincipal == '1':
                objMenu.menu_ventas(miConexion, objServicios, objVentas,objClientes)
            elif opcPrincipal == '2':
                objMenu.menu_gestion_clientes()
            elif opcPrincipal == '3':
                objMenu.menu_gestion_servicios(miConexion, objServicios)
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")