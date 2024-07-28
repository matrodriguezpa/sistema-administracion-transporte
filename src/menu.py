import sys  # para cerrar el programa desde la interfáz y
import time

class Menu:

    # menu principal
    def menuPrincipal(self):
        return input("""
                 ____        _     _______ 
                / ___|      / \   |__   __| 
               | (___      / _ \     | |   
                \___ \    / /_\ \    | |   
                ____) |  / _____ \   | |   
               |_____/  /_/     \_\  |_|   

            SISTEMA DE ADMINISTRACIÓN DE TRANSPORTES 
                        LA NACIONAL

                    MENU PRINCIPAL
            1. Modulo de gestión de Servicios
            2. Modulo de gestión de Clientes
            3. Modulo de ventas
            4. Cerrar programa

            Seleccione una opción: """)

    # menu de la tabla servicios
    def menuServicios(self, objetoConexion, objetoServicios):
        salirMenuServicios = False
        while not salirMenuServicios:


            opcionMenuServicios = input("""
            MÓDULO SERVICIOS
            1. Inserta un servicio
            2. Consultar todos los servicios.
            3. Consultar la fecha y hora de salida de todos los servicios.
            4. Consultar los puestos y peso máximos de todos los servicios.
            5. Consultar un dato de un Servicio.
            6. Consultar cuantos servicios hay en total. 
            7. Consultar suma de los precios de venta de los servicios.
            8. Consultar registro por nombre.
            9. Consultar registro por letra inicial del nombre.
            10. Actualizar el nombre de un registro.
            11. Borra un registro de la tabla servicios.
            12. Borrar toda la tabla de servicios.
            13. Volver.

            Seleccione una opción: """)

            # insertar un nuevo registro en la tabla
            if opcionMenuServicios == "1":
                SercivioCreado = objetoServicios.leerServicio()
                objetoServicios.insertarServicio(objetoConexion, SercivioCreado)

            # consultar todos los registros de la tabla
            elif opcionMenuServicios == "2":
                objetoServicios.consultarTablaServicios1(objetoConexion)

            # consultar todos los registros de la tabla con su fecha y hora de salida
            elif opcionMenuServicios == "3":
                objetoServicios.consultarTablaServicios2(objetoConexion)

            # consultar todos los registros de la tabla con sus puestos y carga máxima
            elif opcionMenuServicios == "4":
                objetoServicios.consultarTablaServicios3(objetoConexion)

            # consultar un dato en específico de un registro
            elif opcionMenuServicios == "5":
                salirOpcionesConsulta = False
                while not salirOpcionesConsulta:
                    consultaSeleccionada = input("""
                        1. Nombre
                        2. Origen.
                        3. Destino.
                        4. Precio
                        5. Hora de salida
                        6. Cantidad máxima de puestos.
                        7. Cantidad máxima de carga.
                        8. Volver.
                        Seleccione un dato a consultar: """)
                    opcionesActualizar = {"1": "nombre","2": "origen","3": "destino","4": "precio","5": "horaSalira","6": "cantidadMaxPuestos","7": "cantidadMaxKilos",}
                    codigoServicio = input("Inserte el codigo del servicio a consultar: ")
                    # Verificar si la opción está en el diccionario
                    if consultaSeleccionada in opcionesActualizar:
                        try:
                            datoConsultado = objetoServicios.consultarTablaServicios4(
                                objetoConexion, opcionesActualizar[consultaSeleccionada], codigoServicio)
                            print("Consulta: El dato",opcionesActualizar[consultaSeleccionada],"del servicio no.",codigoServicio," es ",datoConsultado)
                        except:
                            print("Error en la busqueda: código de servicio inexistente.")
                        salirOpcionesConsulta = True

                    # salir de las opciones de consulta
                    elif consultaSeleccionada == "8":
                        salirOpcionesConsulta = True
                    else:
                        print("Opción inválida, intente otra vez")
                    
            # consultar la cantidad total de registros
            elif opcionMenuServicios == "6":
                total=objetoServicios.consultarTablaServicios5(objetoConexion) 
                print("La cantidad de registros en la tabla Servicios es: ", total)

            # consultar la sumatoria de los precios de venta de los registros
            elif opcionMenuServicios == "7":
                suma = objetoServicios.consultarTablaServicios6(objetoConexion)
                print("La sumatoria de los precios de venta es: ", suma)

            # consultar los registros por el nombre
            elif opcionMenuServicios == "8":
                datoConsulta = input("Nombre a buscar: ").lower()
                objetoServicios.consultarTablaServicios7(objetoConexion, datoConsulta)

            # consultar los registros por las letra iniciales del nombre
            elif opcionMenuServicios == "9":
                datoConsulta = input("Nombre a buscar: ").lower()
                objetoServicios.consultarTablaServicios8(objetoConexion,datoConsulta)

            # actualizar nombre de un registro
            elif opcionMenuServicios == "10":
                codigoServicio = input("Código del servicio a actualizar: ")
                nuevoNombre = input("Nuevo nombre: ")
                try:
                    objetoServicios.actualizarTablaServicios(objetoConexion,nuevoNombre,codigoServicio)
                    print(f"Nombre del servicio {codigoServicio}, actualizado a: {nuevoNombre}.")
                except:
                    print("Error al actualizar el nombre: código de servicio inexistente.")

            # borrar un registro de la tabla servicios
            elif opcionMenuServicios == "11":
                codigoServicio = input("Código del servicio a borrar: ")
                confirmacion = input("¿Estás seguro de que deseas borrar el registro? (s/n): ").lower()
                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    try:
                        objetoServicios.borrarRegistroTablaServicios(objetoConexion, objetoServicios)
                        print("Acción borrar registro ejecutada")
                    except:
                        print("Error al borrar el registro")

            # borrar la tabla servicios
            elif opcionMenuServicios == "12":
                confirmacion = input("¿Estás seguro de que deseas borrar toda la tabla 'servicios'? (s/n): ").lower()

                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    try:
                        objetoServicios.borrarTablaServicios(objetoConexion)
                        print("Tabla 'servicios' borrada exitosamente.")
                    except:
                        print("Error al borrar la tabla 'servicios'.")

            # salir del menú de servicios
            elif opcionMenuServicios == "13":
                salirMenuServicios = True

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    # menu de la tabla clientes
    def menuClientes(self, objetoConexion, objetoClientes):
        salir_menu_clientes = False
        while not salir_menu_clientes:
            opcion_menu_clientes = input("""
                        MÓDULO CLIENTES
                1. Inserta un nuevo cliente.
                2. Consultar todos los clientes.
                3. Consultar un dato de un cliente.
                4. Consultar cuantos servicios hay en total. 
                5. Consultar registro por noIdentificacionCliente.
                6. Consultar registro por letra inicial del nombre.
                7. Actualizar dato de un cliente.
                8. Borra un cliente.
                9. Borrar toda la tabla de clientes.
                10. Volver.

                Seleccione una opción:  """)
            
            # insertar un nuevo cliente
            if opcion_menu_clientes == "1":
                clienteCreado = objetoClientes.leerCliente()
                objetoClientes.insertarTablaClientes(objetoConexion, clienteCreado)

            # consultar todos los registros de la tabla clientes
            elif opcion_menu_clientes == "2":
                objetoClientes.consultarTablaClientes(objetoConexion)

            # consultar un dato de un cliente
            elif opcion_menu_clientes == "3":
                dato = input("Dato a consultar: ")
                noIdentificacionCliente = input("Número de identificación del cliente: ")
                objetoClientes.consultarTablaClientes1(objetoConexion, dato, noIdentificacionCliente)

            elif opcion_menu_clientes == "4":
                objetoClientes.consultarTablaSClientes2(objetoConexion)

            elif opcion_menu_clientes == "5":
                datoConsulta = input("Busqueda: ")
                objetoClientes.consultarTablaClientes3(objetoConexion, datoConsulta)

            elif opcion_menu_clientes == "6":
                datoConsulta = input("Búsqueda: ")
                objetoClientes.consultarTablaClientes4(objetoConexion, datoConsulta)

            elif opcion_menu_clientes == "7":
                objetoClientes.actualizarTablaClientes(objetoConexion)

            elif opcion_menu_clientes == "8":
                noIdentificacionCliente = input("Identificación del cliente a borrar: ")
                confirmacion = input(
                    f"¿Estás seguro de que deseas borrar el cliente {noIdentificacionCliente}? (s/n): "
                ).lower()

                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    objetoClientes.borrarRegistroTablaClientes(
                        objetoConexion, objetoClientes, noIdentificacionCliente
                    )

            elif opcion_menu_clientes == "9":
                confirmacion = input(
                    "¿Estás seguro de que deseas borrar toda la tabla 'Clientes'? (s/n): "
                ).lower()
                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    objetoClientes.borrarTablaClientes(objetoConexion)

            elif opcion_menu_clientes == "10":
                salir_menu_clientes = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    # menu de la tabla ventas
    def menuVentas(self, objetoConexion, objetoServicios, objetoVentas, objetoClientes):

        salir_menu_ventas = False
        while not salir_menu_ventas:

            opciones_ventas = input(
                """
                        MODULO VENTAS
                1. Vender un servicio.
                2. Consultar todas las ventas.
                3. Consultar un dato de una venta.
                4. Consultar cuantos servicios hay en total. 
                5. Consultar registro por número de factura.
                6. Consultar registros por número de identificacion del cliente.
                7. Consultar registros por código del servicio.
                8. Borrar venta.
                9. Borrar tabla ventas.
                10. Imprimir factura.
                11. Volver.

                Seleccione una opción:  
                """
            )

            # comprueba que los datos ingresados esten correctos antes de crear la venta en la base de datos
            if opciones_ventas == "1":

                # Preguntar si es de pasajeros o encomienda
                while True:
                    tipo_carga = input(
                        """
                        1.Pasajero
                        2.Encomienda
                                        
                        Selecione el tipo de servicio: 
                        """
                    )

                    if tipo_carga == "1":
                        tipo_dato_carga = "cantidadMaxPuestos"
                        break

                    elif tipo_carga == "2":
                        tipo_dato_carga = "cantidadMaxKilos"
                        break

                    else:
                        print("Seleccione una opcion valida.")

                validacion_venta = True
                while validacion_venta:

                    # se reciben los datos de la venta
                    ventaConstruida = objetoVentas.leerVenta(objetoConexion, objetoVentas)

                    # comprobar que el numero de identificacion y el codigo sean datos numéricos
                    try:
                        valor_convertido = int(ventaConstruida[2])
                        valor_convertido2 = int(ventaConstruida[3])
                        print("Datos convertido a entero:", valor_convertido,valor_convertido2)
                    except ValueError:
                        print("Uno de los datos ingresados no es numérico, intente otra vez.")
                        validacion_venta = False
                    if validacion_venta:
                        break  # Salir del bucle si se estableció salirValidacionVenta a True

                    # Comprueba los datos (noIdentificacionCliente, codigoServicio)
                    # el numero de factura no se necesita comprobar, porque es generado automaticamente
                    existe_cliente = objetoClientes.consultarTablaClientes1(objetoConexion, "noIdentificacionCliente", ventaConstruida[1])
                    existe_servicio = objetoServicios.consultarTablaServicios3(objetoConexion, "codigoServicio", ventaConstruida[2])

                    if existe_cliente != int(ventaConstruida[1]):
                        print("Cliente no econtrado, compruebe el dato ingresados o si el cliente esta registrado.")
                        validacion_venta = False

                    elif existe_servicio != int(ventaConstruida[2]):
                        print("Servicio no econtrado, compruebe el dato ingresados o si el servicio esta registrado.")
                        validacion_venta = False

                    else:
                        # Comprueba la disponibilidad de Puestos/Kilos
                        codigoServicio = ventaConstruida[2]
                        cantidadVender = int(ventaConstruida[3])  # La cantidad que se quiere vender
                        capacidadMaxima = int(
                            objetoServicios.consultarTablaServicios3(
                                objetoConexion, tipo_dato_carga, codigoServicio
                            )
                        )  # La capacidad máxima de puestos o kilos del servicio
                        cantidadVendidaTotal = int(
                            objetoVentas.consultarCantidadVendidaTotal(
                                objetoConexion, codigoServicio
                            )
                        )  # El espacio que ya se ha vendido del servicio

                        if cantidadVender <= 0:
                            print("La cantidad a vender no puede ser cero o negativa, ingrese una cantidad valida.")
                            validacion_venta = False

                        elif capacidadMaxima == cantidadVendidaTotal:
                            print("No hay más puestos disponibles, intente con otro servicio.")
                            validacion_venta = False

                        elif capacidadMaxima < (cantidadVendidaTotal + cantidadVender):
                            print("Espacio de",tipo_dato_carga,"disponible exedido, ingrese una cantidad menor.")
                            print("Disponible:", capacidadMaxima - cantidadVendidaTotal)
                            validacion_venta = False

                        # Todos los datos son validos y se añade la venta
                        else:
                            print("Venta valida, añadiendo datos ingresados.")
                            objetoVentas.añadirServicioAVender(objetoConexion, ventaConstruida)

                            while True:
                                opcionFactura = input("¿Imprimir factura? (s/n): ").lower()

                                if opcionFactura == "s":

                                    # Se buscan la tupla de datos venta, cliente y servicio para ingresar en la factura.
                                    no_factura = ventaConstruida[0]
                                    noIdentificacionClientes = ventaConstruida[1]
                                    codigoServicio = ventaConstruida[2]

                                    venta = objetoVentas.consultarTablaVentas(objetoConexion, no_factura)[0]
                                    cliente = objetoClientes.consultarTablaClientes3(objetoConexion, noIdentificacionClientes)[0]
                                    servicio = objetoServicios.consultarTablaServicios6(objetoConexion, codigoServicio)[0]

                                    objetoVentas.imprimirFactura(objetoConexion, venta, cliente, servicio)
                                    break

                                else:
                                    print("Impresion de factura cancelada.")
                                    break
                        validacion_venta = False

            # consultar todas las ventas
            elif opciones_ventas == "2":

                objetoVentas.consultarTablaVentas1(objetoConexion)

            # consultar un dato de una factura
            elif opciones_ventas == "3":

                salir_consulta = False
                while not salir_consulta:
                    no_factura = input("Inserte el número de la factura a consultar")

                    opcion_consulta = input(
                        """
                        Seleccione un dato a consultar:
                        1.Número de identificación de cliente.
                        2.Código del servicio.
                        3.Cantidad Vendida.
                        4.Volver.
                        """
                    )

                    # consultar la identificacion del cliente de la venta
                    if opcion_consulta == "1":
                        objetoVentas.consultarTablaVentas2(
                            objetoConexion, "noIdentificacionCliente", no_factura
                        )

                    # consultar el codigo del servicio de la venta
                    elif opcion_consulta == "2":
                        objetoVentas.consultarTablaVentas2(
                            objetoConexion, "codigoServicio", no_factura
                        )

                    # consultar la cantidad de la venta
                    elif opcion_consulta == "3":
                        objetoVentas.consultarTablaVentas2(
                            objetoConexion, "cantidadVender", no_factura
                        )

                    elif opcion_consulta == "4":
                        salir_consulta = True

                    else:
                        print("Opcion invalida, intente otra vez")

            # consultar cuantos registros en total hay en la tabla ventas
            elif opciones_ventas == "4":
                objetoVentas.consultarTablaVentas3(objetoConexion)

            # consultar un registro por número de la Factura
            elif opciones_ventas == "5":
                no_factura = input("inserte el número de factura: ")
                objetoVentas.consultarTablaVentas5(objetoConexion, no_factura)

            # consultar registros por número de identificacion del cliente.
            elif opciones_ventas == "6":
                idConsulta = input("Inserte el número de identificación del cliente: ")
                objetoVentas.consultarTablaVentas6(objetoConexion, "noIdentificacionCliente", idConsulta)

            # consultar registros por código del servicio.
            elif opciones_ventas == "7":
                csConsulta = input("Inserte el codigo del serivicio: ")
                objetoVentas.consultarTablaVentas6(objetoConexion, "codigoServicio", csConsulta)

            # borrar registro de la tabla ventas
            elif opciones_ventas == "8":
                no_factura = input("Inserte el número de factura.")
                confirmacion = input(f"¿Estás seguro de que deseas borrar el registro? (s/n): ").lower()

                if confirmacion != "s":
                    print("Operación cancelada.")
                    return

                objetoVentas.borrarRegistroTablaVentas(objetoConexion, no_factura)

            # borrar tabla ventas
            elif opciones_ventas == "9":
                confirmacion = input(f"¿Estás seguro de que deseas la tabla ventas? (s/n): ").lower()

                if confirmacion != "s":
                    print("Operación cancelada.")
                    return

                objetoVentas.borrarTablaVentas(objetoConexion)

            # imprimir una factura
            elif opciones_ventas == "10":
                facturaVenta = input("Inserte el número de la factura a imprimir:")
                venta = objetoVentas.consultarTablaVentas(objetoConexion, facturaVenta)[0]
                noIdentificacionCliente = str(venta[1])
                codigoServicio = str(venta[2])

                cliente = objetoClientes.consultarTablaClientes3(objetoConexion, noIdentificacionCliente)[0]
                servicio = objetoServicios.consultarTablaServicios6(objetoConexion, codigoServicio)[0]

                objetoVentas.imprimirFactura(objetoConexion, venta, cliente, servicio)

            # salir del menu de ventas
            elif opciones_ventas == "11":
                salir_menu_ventas = True

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    # generar menu
    def menu(self, objetoConexion, objetoServicios, objetoVentas, objetoClientes, objetoMenu):

        # crea las tablas de servicio, clientes y ventas (si ya existen no se crean más).
        objetoServicios.crearTablaServicios(objetoConexion)
        objetoClientes.crearTablaClientes(objetoConexion)
        objetoVentas.crearTablaVentas(objetoConexion)

        # a partir del menu principal, llama a los submenus necesarios selecionados por el usuario.
        while True:
            opcionMenuPrincipal = objetoMenu.menuPrincipal()

            if opcionMenuPrincipal == "1":
                objetoMenu.menuServicios(objetoConexion, objetoServicios)

            elif opcionMenuPrincipal == "2":
                objetoMenu.menuClientes(objetoConexion, objetoClientes)

            elif opcionMenuPrincipal == "3":
                objetoMenu.menuVentas(objetoConexion, objetoServicios, objetoVentas, objetoClientes)

            elif opcionMenuPrincipal == "4":
                print("Cerrando el programa.")
                time.sleep(1)  # se pausa un segundo para que el usuario pueda leer el mensaje antes de que se cierre.
                sys.exit()

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
