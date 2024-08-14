import sys  # para cerrar el programa desde la interfáz y
import time

class Menu:

    # menu principal
    @staticmethod
    def menuPrincipal():
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
        salirMenuClientes = False
        while not salirMenuClientes:
            opcionMenuClientes = input("""
                        MÓDULO CLIENTES
                1. Inserta un nuevo cliente.
                2. Consultar todos los clientes.
                3. Consultar un dato de un cliente.
                4. Consultar cuantos clientes hay en total. 
                5. Consultar registro por nombre.
                6. Consultar registro por letra inicial del nombre.
                7. Actualizar nombre de un cliente.
                8. Borra un cliente.
                9. Borrar toda la tabla de clientes.
                10. Volver.

                Seleccione una opción:  """)
            
            # insertar un nuevo cliente
            if opcionMenuClientes == "1":
                clienteCreado = objetoClientes.leerCliente()
                objetoClientes.insertarTablaClientes(objetoConexion, clienteCreado)

            # consultar todos los registros de la tabla clientes
            elif opcionMenuClientes == "2":
                objetoClientes.consultarTablaClientes1(objetoConexion)

            # consultar un dato de un cliente
            elif opcionMenuClientes == "3":
                salirOpcionesConsulta = False
                while not salirOpcionesConsulta:
                    consultaSeleccionada = input("""
                        1. Nombre
                        2. Apellido.
                        3. Dirección.
                        4. Telefono.
                        5. Correo Electrónico.
                        6. Volver.
                        Seleccione un dato a consultar: """)
                    opcionesActualizar = {"1": "nombre","2": "apellido","3": "direccion","4": "telefono","5": "correoElectronico"}
                    noIdentificacionCliente = input("Inserte la identificación del cliente a consultar: ")

                    # Verificar si la opción está en el diccionario
                    if consultaSeleccionada in opcionesActualizar:
                        try:
                            datoConsultado = objetoClientes.consultarTablaClientes2(
                                objetoConexion, opcionesActualizar[consultaSeleccionada], noIdentificacionCliente)
                            print("Consulta: El dato",opcionesActualizar[consultaSeleccionada],"del cliente ",noIdentificacionCliente," es ",datoConsultado)
                        except:
                            print("Error en la busqueda: Cliente no encontrado.")
                        salirOpcionesConsulta = True

                    # salir de las opciones de consulta
                    elif consultaSeleccionada == "6":
                        salirOpcionesConsulta = True
                    else:
                        print("Opción inválida, intente otra vez")

            # consultar cuantos clientes hay en total
            elif opcionMenuClientes == "4":
                total = objetoClientes.consultarTablaSClientes3(objetoConexion)
                print(f"El total de registros en la tabla es: {total}")

            # buscar clientes por nombre
            elif opcionMenuClientes == "5":
                nombreConsulta = input("Nombre a buscar: ").lower()
                objetoClientes.consultarTablaClientes4(objetoConexion,"nombre",nombreConsulta)

            # buscar clientes por letra inicial de nombre
            elif opcionMenuClientes == "6":
                letraInicial = input("Búsqueda: ").lower()
                objetoClientes.consultarTablaClientes5(objetoConexion, letraInicial)

            # actualizar dato de la tabla clientes
            elif opcionMenuClientes == "7":
                noIdentificacionCliente= input("Número de identificación del cliente: ")
                nuevoNombre = input("Nuevo nombre del cliente: ").lower()
                try:
                    objetoClientes.actualizarTablaClientes(objetoConexion, nuevoNombre, noIdentificacionCliente)
                except:
                    print("Error al actualizar el dato.")
            # borrar registro de la tabla clientes
            elif opcionMenuClientes == "8":
                noIdentificacionCliente = input("Identificación del cliente a borrar: ")
                confirmacion = input(f"¿Estás seguro de que deseas borrar el cliente {noIdentificacionCliente}? (s/n): ").lower()

                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    try:
                        objetoClientes.borrarRegistroTablaClientes(
                            objetoConexion, objetoClientes, noIdentificacionCliente)
                    except:
                        print("Error al borrar el registro.")

            # borrar la tabla clientes
            elif opcionMenuClientes == "9":
                confirmacion = input("¿Estás seguro de que deseas borrar toda la tabla 'Clientes'? (s/n): ").lower()
                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    try:
                        objetoClientes.borrarTablaClientes(objetoConexion)
                    except:
                        print("Error al borrar la tabla.")

            # salir del menu de clientes
            elif opcionMenuClientes == "10":
                salirMenuClientes = True

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    # menu de la tabla ventas
    def menuVentas(self, objetoConexion, objetoServicios, objetoVentas, objetoClientes):

        salirMenuVentas = False
        while not salirMenuVentas:

            opcionesVentas = input("""
                        MODULO VENTAS
                1. Vender un servicio.
                2. Consultar todas las ventas.
                3. Consultar un dato de una venta.
                4. Consultar cuantos servicios hay en total. 
                5. Consultar registros por número de identificacion del cliente.
                6. Consultar registros por código del servicio.
                7. Borrar venta.
                8. Borrar tabla ventas.
                9. Imprimir factura.
                10. Volver.

                Seleccione una opción:  """)

            # comprueba que los datos ingresados esten correctos antes de crear la venta en la base de datos
            if opcionesVentas == "1":

                # Preguntar si es de pasajeros o encomienda
                while True:
                    tipoCarga = input("""
                        1.Pasajero
                        2.Encomienda
                                        
                        Selecione el tipo de servicio: """)

                    if tipoCarga == "1":
                        datoCarga = "cantidadMaxPuestos"
                        break

                    elif tipoCarga == "2":
                        datoCarga = "cantidadMaxKilos"
                        break

                    else:
                        print("Seleccione una opcion valida.")

                while True:

                    # se reciben los datos de la venta
                    ventaConstruida = objetoVentas.leerVenta(objetoConexion, objetoVentas)

                    # Comprobación 1: comprobar que el numero de identificacion y el codigo sean datos numéricos.
                    try:
                        int(ventaConstruida[1])
                        int(ventaConstruida[2])
                        int(ventaConstruida[3])
                    except ValueError:
                        print("Uno de los datos ingresados no es numérico, intente otra vez.")
                        break  # Salir de la validación

                    # Comprobación 2: Comprueba que los datos (noIdentificacionCliente, codigoServicio) existan en la tabla cliente y servicios
                    try:
                        existeCliente = objetoClientes.consultarTablaClientes2(objetoConexion, "noIdentificacionCliente", ventaConstruida[1])
                        existeServicio = objetoServicios.consultarTablaServicios4(objetoConexion, "codigoServicio", ventaConstruida[2])

                        if existeCliente != int(ventaConstruida[1]):
                            print("Cliente no encontrado, compruebe el dato ingresado o si el cliente está registrado.")
                            break

                        elif existeServicio != int(ventaConstruida[2]):
                            print("Servicio no encontrado, compruebe el dato ingresado o si el servicio está registrado.")
                            break
                    except:
                        print("Uno de los datos ingresados no existe en la tabla servicios/clientes.")
                        break  # Salir de la validación

                    # Comprobación 3: Comprueba que no se exceda la disponibilidad de Puestos/Kilos
                    try:
                        codigoServicio = ventaConstruida[2]
                        cantidadNecesitadaVender = int(ventaConstruida[3])  # la cantidad que se quiere vender
                        capacidadMaxima = int(objetoServicios.consultarTablaServicios4(objetoConexion, datoCarga, codigoServicio)) # la capacidad máxima de puestos o kilos del servicio
                        cantidadYaVendida = int(objetoVentas.consultarTablaVentas5(objetoConexion)) # el espacio que ya se ha vendido del servicio (cantidadVendidatotal)
                        
                        # se realiza la comprobación
                        if cantidadNecesitadaVender <= 0:
                            print("La cantidad a vender no puede ser cero o negativa, ingrese una cantidad válida.")
                            break
                        elif capacidadMaxima == cantidadYaVendida:
                            print("No hay más puestos disponibles, intente con otro servicio.")
                            break
                        elif capacidadMaxima < (cantidadYaVendida + cantidadNecesitadaVender):
                            print("Espacio de", datoCarga, "disponible excedido, ingrese una cantidad menor.")
                            print("Disponible:", capacidadMaxima - cantidadYaVendida)
                            break
                    except Exception as e:
                        print(f"Error al comprobar la disponibilidad de Puestos/Kilos: {e}")
                        break  # Salir de la validación
                    
                    # todos los datos son válidos y se añade la venta.
                    print("Venta válida, añadiendo datos ingresados.")
                    objetoVentas.añadirServicioAVender(objetoConexion, ventaConstruida)
                    
                    # pregunta al cliente si quiere recibir factura (que se envia al correo electrónico).
                    while True:
                        opcionFactura = input("¿Imprimir factura? (s/n): ").lower()
                        if opcionFactura == "s":

                            # Se buscan la tupla de datos venta, cliente y servicio para ingresar en la factura.
                            print("Obteniendo datos de venta...")
                            miVenta = objetoVentas.consultarTablaVentas4(objetoConexion,"noFactura",ventaConstruida[0])
                            miCliente = objetoClientes.consultarTablaClientes4(objetoConexion,"noIdentificacionCliente",ventaConstruida[1])
                            miServicio = objetoServicios.consultarTablaServicios7(objetoConexion,"codigoServicio",ventaConstruida[2])
                            print(f"{miVenta}\n {miCliente}\n {miServicio}")
                            objetoVentas.imprimirFactura(objetoConexion, miVenta, miCliente, miServicio)
                            break
                        else:
                            print("Impresion de factura cancelada.")
                            break
                    break

            # consultar todas las ventas
            elif opcionesVentas == "2":
                objetoVentas.consultarTablaVentas1(objetoConexion)

            # consultar un dato de una venta
            elif opcionesVentas == "3":

                salirConsulta = False
                while not salirConsulta:

                    opcionSelecionada = input("""
                        1.Número de identificación de cliente.
                        2.Código del servicio.
                        3.Cantidad Vendida.
                        4.Volver.

                        Seleccione un dato a consultar: """)
                    opcionesActualizar = {"1": "noIdentificacionCliente","2": "codigoServicio","3": "cantidadVendida"}
                    codigoServicio = input("Inserte el número de la factura a consultar: ")  
                    
                    # Verificar si la opción está en el diccionario
                    if opcionSelecionada in opcionesActualizar:
                        try:
                            datoConsultado = objetoServicios.consultarTablaVentas2(
                                objetoConexion, opcionesActualizar[opcionSelecionada], codigoServicio)
                            print("Consulta: El dato",opcionesActualizar[opcionSelecionada],"la venta no.",codigoServicio," es ",datoConsultado)
                        except:
                            print("Error en la busqueda: no. de factura inexistente.")
                        salirConsulta = True
                    elif opcionSelecionada == "4":
                        salirConsulta = True
                    else:
                        print("Opcion invalida, intente otra vez")

            # consultar cuantos registros en total hay en la tabla ventas
            elif opcionesVentas == "4":
                cantidadYaVendida = objetoVentas.consultarTablaVentas3(objetoConexion)
                print(f"El total de registros es {cantidadYaVendida}")

            # consultar registros por número de identificacion del cliente.
            elif opcionesVentas == "5":
                idConsulta = input("Inserte el número de identificación del cliente: ")
                objetoVentas.consultarTablaVentas4(objetoConexion, "noIdentificacionCliente", idConsulta)

            # consultar registros por código del servicio.
            elif opcionesVentas == "6":
                csConsulta = input("Inserte el codigo del serivicio: ")
                objetoVentas.consultarTablaVentas4(objetoConexion, "codigoServicio", csConsulta)

            # borrar registro de la tabla ventas
            elif opcionesVentas == "7":
                codigoServicio = input("Inserte el número de factura.")
                confirmacion = input(f"¿Estás seguro de que deseas borrar el registro? (s/n): ").lower()
                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    try:
                        objetoVentas.borrarRegistroTablaVentas(objetoConexion, codigoServicio)
                    except:
                        print("Error al borrar el registro.")

            # borrar tabla ventas
            elif opcionesVentas == "8":
                confirmacion = input(f"¿Estás seguro de que deseas la tabla ventas? (s/n): ").lower()
                if confirmacion != "s":
                    print("Operación cancelada.")
                else:
                    try:
                        objetoVentas.borrarTablaVentas(objetoConexion)
                    except:
                        print("Error al borrar la tabla ventas.")

            # imprimir una factura
            elif opcionesVentas == "9":
                facturaVenta = input("Inserte el número de la factura a imprimir:")
                try:
                    print("Obteniendo datos de venta...")
                    miVenta = objetoVentas.consultarTablaVentas4(objetoConexion,"noFactura",facturaVenta)

                    noIdentificacionCliente = str(miVenta[1])
                    codigoServicio = str(miVenta[2])
                    
                    print("Obteniendo datos de factura...")
                    miCliente = objetoClientes.consultarTablaClientes4(objetoConexion,"noIdentificacionCliente",noIdentificacionCliente)
                    miServicio = objetoServicios.consultarTablaServicios7(objetoConexion,"codigoServicio",codigoServicio)

                    objetoVentas.imprimirFactura(miVenta, miCliente, miServicio)
                except:
                    print("Error al imprimir la factura.")

            # salir del menu de ventas
            elif opcionesVentas == "10":
                salirMenuVentas = True

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
