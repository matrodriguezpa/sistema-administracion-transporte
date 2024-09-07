import time  # Para pausar la ejecución antes de salir del programa.
import sys  # Para cerrar el programa cuando el usuario lo indica.
from datetime import datetime  # Para manejar fechas y horas.
import re  # Para comprobación de los datos


def mostrar_menu_principal():
    """Muestra el menú principal del sistema de administración de transportes y captura la opción seleccionada por el usuario.

    Returns:
        str: Opción seleccionada por el usuario.
    """
    return input("""
           _____      ___   _______ 
          / ____|    / _ \ |__   __|       
          \____ \   / /_\ \   | |   
           ____) | / _____ \  | |   
          |_____/ /_/     \_\ |_|  

    SISTEMA DE ADMINISTRACIÓN DE TRANSPORTES 
                   LA NACIONAL

                MENU PRINCIPAL
        1. Módulo de gestión de Servicios
        2. Módulo de gestión de Clientes
        3. Módulo de Ventas
        4. Módulo de Facturas
        5. Cerrar programa

        Seleccione una opción: """)


def gestionar_menu_servicios(conexion_db, servicios):
    """
    Gestiona el menú de opciones para la administración de servicios.
    Opciones:
        1. Crear un nuevo servicio.
        2. Actualizar el nombre de un servicio.
        3. Consultar la información de un servicio.
        4. Volver al menú principal.

    Args:
        conexion_db (objeto): Objeto que gestiona la conexión a la base de datos.
        servicios (objeto): Objeto que contiene los métodos para interactuar con los servicios.

    Returns:
        None
    """
    salir_del_menu = False
    while not salir_del_menu:
        opcion_seleccionada = input("""
               MÓDULO SERVICIOS
        1. Crear un nuevo servicio.
        2. Actualizar el nombre de un servicio.
        3. Consultar Información de un servicio.
        4. Volver.

        Seleccione una opción: """)

        if opcion_seleccionada == "1":
            try:
                seleccion_transporte = False
                while not seleccion_transporte:
                    carga_max = 0
                    tipo_venta = input("Ingrese el tipo de producto: pasajeros (1) o encomienda (2): ")
                    if tipo_venta == "1" or tipo_venta =="2":
                        seleccion_transporte = True
                    else:
                        print("Dato ingresado no válido")

                # Captura y validación de los datos del nuevo servicio

                # Validación del código del servicio
                servicios.codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not servicios.codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                servicios.codigo_servicio = int(servicios.codigo_servicio)

                # Validación del nombre del servicio
                servicios.nombre = input("Ingrese el nombre del servicio: ").strip()
                if not servicios.nombre:
                    raise ValueError("El nombre del servicio no puede estar vacío.")
                if len(servicios.nombre) < 3 or len(servicios.nombre) > 20:
                    raise ValueError("El nombre del servicio debe tener entre 3 y 20 caracteres.")

                # Validación del origen del servicio
                servicios.origen = input("Ingrese el origen del servicio: ").strip()
                if not servicios.origen:
                    raise ValueError("El origen del servicio no puede estar vacío.")
                if len(servicios.origen) < 3 or len(servicios.origen) > 20:
                    raise ValueError("El origen del servicio debe tener entre 3 y 20 caracteres.")

                # Validación del destino del servicio
                servicios.destino = input("Ingrese el destino del servicio: ").strip()
                if not servicios.destino:
                    raise ValueError("El destino del servicio no puede estar vacío.")
                if len(servicios.destino) < 3 or len(servicios.destino) > 20:
                    raise ValueError("El destino del servicio debe tener entre 3 y 20 caracteres.")

                # Validación del precio de venta
                servicios.precio_venta = input("Ingrese el precio de venta del servicio: ")
                if not servicios.precio_venta.replace('.', '', 1).isdigit() or float(servicios.precio_venta) <= 0:
                    raise ValueError("El precio de venta debe ser un número positivo.")
                servicios.precio_venta = float(servicios.precio_venta)

                # Validación de hora de salida
                hora_minuto_str = input("Ingrese la hora de salida (HH:MM): ")
                fecha_actual_str = datetime.now().strftime("%Y-%m-%d")
                try:
                    hora_valida = datetime.strptime(hora_minuto_str, "%H:%M")
                except ValueError:
                    raise ValueError("El formato de la hora es incorrecto. Use 'HH:MM'.")
                servicios.hora_salida = datetime.strptime(f"{fecha_actual_str} {hora_minuto_str}:00",
                                                          "%Y-%m-%d %H:%M:%S")
                print(f"Hora de salida establecida a: {servicios.hora_salida}")

                if tipo_venta == "1":
                    # Validación de la cantidad máxima de puestos
                    servicios.max_puestos = input("Ingrese la cantidad máxima de puestos: ")
                    if not servicios.max_puestos.isdigit() or int(servicios.max_puestos) < 0:
                        raise ValueError("La cantidad máxima de puestos debe ser un número entero positivo.")
                    if len(servicios.destino) < 1 or len(servicios.destino) > 20:
                        raise ValueError("Los puestos maximos del servicio debe tener entre 1 y 20 caracteres.")
                    servicios.max_puestos = int(servicios.max_puestos)
                    servicios.max_kilos = 0
                elif tipo_venta == "2":
                    servicios.max_puestos = 0
                    # Validación de la cantidad máxima de kilos
                    servicios.max_kilos = input("Ingrese la cantidad máxima de kilos: ")
                    if not servicios.max_kilos.isdigit() or int(servicios.max_kilos) < 0:
                        raise ValueError("La cantidad máxima de kilos debe ser un número entero positivo o cero.")
                    if len(servicios.destino) < 1 or len(servicios.destino) > 20:
                        raise ValueError("Los kilos maximos del servicio debe tener entre 1 y 20 caracteres.")
                    servicios.max_kilos = int(servicios.max_kilos)
                else:
                    raise ValueError("Tipo de producto (pasajero // encomienda) indeterinado.")

                # Crear y validar el nuevo servicio
                print("Los datos ingresados son válidos, creando servicio.")
                nuevo_servicio = (servicios.codigo_servicio,
                                  servicios.nombre,
                                  servicios.origen,
                                  servicios.destino,
                                  servicios.precio_venta,
                                  servicios.hora_salida,
                                  servicios.max_puestos,
                                  servicios.max_kilos)

                # Llamada al método para crear un nuevo servicio
                servicios.crear_nuevo_servicio(conexion_db, nuevo_servicio)

                salir_del_menu = True
            except ValueError as error:
                print(f"Error: {error}")
                salir_del_menu = True

        elif opcion_seleccionada == "2":
            try:
                # Validación del código del servicio
                codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")

                # Validación del nuevo nombre del servicio
                nuevo_nombre = input("Ingrese el nuevo nombre del servicio: ").strip()
                if not nuevo_nombre:
                    raise ValueError("El nuevo nombre del servicio no puede estar vacío.")
                if len(nuevo_nombre) < 3 or len(nuevo_nombre) > 50:
                    raise ValueError("El nuevo nombre del servicio debe tener entre 3 y 50 caracteres.")

                # Insersion del dato
                actualizacion_exitosa = servicios.actualizar_nombre_servicio(conexion_db, codigo_servicio, nuevo_nombre)
                if actualizacion_exitosa:
                    print("Nombre del servicio actualizado correctamente.")
                else:
                    print("Error al actualizar el servicio, por favor, intente nuevamente.")
                salir_del_menu = True
            except ValueError as error:
                print(f"Error: {error}")
                salir_del_menu = True

        elif opcion_seleccionada == "3":
            try:
                codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                codigo_servicio = int(codigo_servicio)

                informacion_servicio = servicios.consultar_informacion_servicio(conexion_db, codigo_servicio)

                if informacion_servicio:
                    print("Información del servicio:\n")
                    print(
                        f"Código del servicio: {informacion_servicio[0]}| Nombre:{informacion_servicio[1]}, Origen:{informacion_servicio[2]}, Destino: {informacion_servicio[3]},Precio de venta:{informacion_servicio[4]}, Hora de salida:{informacion_servicio[5]}, Puestos máximos: {informacion_servicio[6]},Kilos máximos: {informacion_servicio[7]},")
                else:
                    print(f"No se encontró información para el código de servicio {codigo_servicio}.")
                salir_del_menu = True

            except ValueError as error:
                print(f"Error: {error}")
                salir_del_menu = True

        elif opcion_seleccionada == "4":
            print("Saliendo del módulo de Servicios.")
            salir_del_menu = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def gestionar_menu_clientes(conexion_db, clientes):
    """
    Gestiona el menú de opciones para la administración de clientes.
    Opciones:
            1. Crear un nuevo cliente.
            2. Actualizar la dirección de un cliente.
            3. Consultar los datos de un cliente.
            4. Volver al menú principal.

    Args:
        conexion_db (objeto): Objeto que gestiona la conexión a la base de datos.
        clientes (objeto): Objeto que contiene los métodos para interactuar con los clientes.

    Returns:
        None
    """
    salir_del_menu = False
    while not salir_del_menu:
        opcion_seleccionada = input("""
                        MÓDULO CLIENTES
                1. Crear un nuevo cliente.
                2. Actualizar dirección del cliente.
                3. Consultar datos de un cliente.
                4. Volver.

                Seleccione una opción:  """)

        if opcion_seleccionada == "1":
            try:
                # Captura y validación de los datos del nuevo cliente

                clientes.no_identificacion_cliente = input("Ingrese el número de identificación: ")
                if not clientes.no_identificacion_cliente.isdigit():
                    raise ValueError("El número de identificación debe ser un número.")
                clientes.no_identificacion_cliente = int(clientes.no_identificacion_cliente)

                clientes.nombre = input("Ingrese el nombre: ")
                if not clientes.nombre.isalpha():
                    raise ValueError("El nombre solo deben contener letras.")
                if len(clientes.nombre) < 3 or len(clientes.nombre) > 20:
                    raise ValueError("El nombre del cliente debe tener entre 3 y 50 caracteres.")

                clientes.apellido = input("Ingrese el apellido: ")
                if not clientes.apellido.isalpha():
                    raise ValueError("El apellido solo deben contener letras.")
                if len(clientes.apellido) < 3 or len(clientes.nombre) > 20:
                    raise ValueError("El apellido del cliente debe tener entre 3 y 20 caracteres.")

                print("Ingreso de la dirección de cliente")
                tipo_via = input("Ingrese el tipo de vía (calle/carrera/diagonal/transversal): ").strip().lower()
                if tipo_via not in ["calle", "carrera", "diagonal", "transversal"]:
                    raise ValueError("El tipo de vía debe ser 'calle' o 'carrera'.")

                numero_via = input("Ingrese el número de la vía: ").strip()
                if not re.match(r"^\d+[a-zA-Z]*$", numero_via):
                    raise ValueError(
                        "El número de la vía debe ser un número, opcionalmente seguido de una letra o varias.")

                numero_puerta = input("Ingrese el número de puerta: ").strip()
                if not re.match(r"^\d+[a-zA-Z]*$", numero_puerta):
                    raise ValueError(
                        "El número de la puerta debe ser un número, opcionalmente seguido de una letra o varias.")

                numero_adicional = input("Ingrese el número adicional (después del guión '-'): ").strip()
                if not numero_adicional.isdigit():
                    raise ValueError("El número adicional debe ser un número.")

                clientes.direccion = f"{tipo_via} {numero_via}#{numero_puerta}-{numero_adicional}"

                patron_direccion = r"^(calle|carrera|diagonal|transversal) \d+[a-zA-Z]*#\d+[a-zA-Z]*-\d+$"
                if not re.match(patron_direccion, clientes.direccion, re.IGNORECASE):
                    raise ValueError("La dirección no tiene el formato adecuado. Ej: calle 45bis#52a-27.")
                print(f"Dirección insertada: {clientes.direccion}")

                clientes.telefono = input("Ingrese el Teléfono: ")
                if not clientes.telefono.isdigit():
                    raise ValueError("El teléfono debe ser un número.")
                if len(clientes.telefono) < 3 or len(clientes.telefono) > 20:
                    raise ValueError("El telefono debe tener entre 3 y 20 caracteres.")

                clientes.correo_electronico = input("Ingrese el correo electrónico: ")
                patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
                if not re.match(patron_correo, clientes.correo_electronico):
                    raise ValueError("El correo electrónico no tiene el formato adecuado. Ej: nombre@correo.algo.")
                if len(clientes.correo_electronico) < 5 or len(clientes.correo_electronico) > 20:
                    raise ValueError("El coreeo electrónico debe tener entre 5 y 20 caracteres.")

                mi_cliente = (clientes.no_identificacion_cliente,
                              clientes.nombre,
                              clientes.apellido,
                              clientes.direccion,
                              clientes.telefono,
                              clientes.correo_electronico)

                clientes.crear_nuevo_cliente(conexion_db, mi_cliente)
                salir_del_menu = True

            except ValueError as e:
                print(f"Error: {str(e)}")
                salir_del_menu = True

        elif opcion_seleccionada == "2":

            try:
                numero_identificacion = input("Ingrese el número de identificación del cliente (número entero): ")

                if not numero_identificacion.isdigit():
                    raise ValueError("El número de identificación debe ser un número entero.")
                numero_identificacion = int(numero_identificacion)

                # Ingresar la nueva dirección por partes
                nueva_direccion = input("Ingrese la nueva dirección del cliente:")
                patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
                if not re.match(patron_correo, clientes.correo_electronico):
                    raise ValueError("El correo electrónico no tiene el formato adecuado. Ej: nombre@correo.algo.")
                if len(clientes.correo_electronico) < 5 or len(clientes.correo_electronico) > 20:
                    raise ValueError("El coreeo electrónico debe tener entre 5 y 20 caracteres.")

                actualizacion_exitosa = clientes.actualizar_direccion_cliente(conexion_db, numero_identificacion,
                                                                              nueva_direccion)

                if actualizacion_exitosa:
                    print("Dirección del cliente actualizada correctamente.")
                else:
                    print("Error al actualizar la dirección, por favor, intente nuevamente.")
                salir_del_menu = True

            except ValueError as error:
                print(f"Error: {error}")
                salir_del_menu = True

        elif opcion_seleccionada == "3":
            try:
                numero_identificacion = input("Ingrese el número de identificación del cliente (número entero): ")
                if not numero_identificacion.isdigit():
                    raise ValueError("El número de identificación debe ser un número entero.")

                datos_cliente = clientes.consultar_datos_cliente(conexion_db, numero_identificacion)
                if datos_cliente:
                    print("Información del cliente:", datos_cliente)
                else:
                    print(f"No se encontró información para el cliente con identificación {numero_identificacion}.")
                salir_del_menu = True

            except ValueError as error:
                print(f"Error: {error}")
                salir_del_menu = True

        elif opcion_seleccionada == "4":
            salir_del_menu = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def gestionar_menu_ventas(conexion_db, servicios, clientes, ventas, facturas):
    """
    Gestiona el menú de opciones para la administración de ventas.
    Opciones:
        1. Vender un servicio.
        2. Quitar servicio vendido.
        3. Volver al menú principal.

    Args:
        conexion_db (objeto): Objeto que gestiona la conexión a la base de datos.
        servicios (objeto): Objeto que contiene los métodos para interactuar con los servicios.
        clientes (objeto): Objeto que contiene los métodos para interactuar con los clientes.
        ventas (objeto): Objeto que contiene los métodos para interactuar con las ventas.
        facturas (objeto): Objeto que contiene los métodos para interactuar con las facturas.

    Returns:
        None
    """
    salir_del_menu = False
    while not salir_del_menu:
        opcion_seleccionada = input("""
                        MÓDULO VENTAS
                1. Vender un servicio.
                2. Quitar servicio vendido.
                3. Volver.

                Seleccione una opción:  """)
        if opcion_seleccionada == "1":
            try:
                # Generar número de factura si no existe
                if ventas.no_factura is None:
                    ventas.no_factura = ventas.generar_numero_factura(conexion_db)

                continuar_ventas = True
                while continuar_ventas:
                    ventas.no_identificacion_cliente = input("Ingrese el número de identificación del cliente: ")
                    mi_cliente = clientes.consultar_informacion_cliente(conexion_db, ventas.no_identificacion_cliente)
                    if mi_cliente is None or mi_cliente is False:
                        raise ValueError("Cliente no encontrado")

                    ventas.codigo_servicio = input("Ingrese el código del servicio que va a vender: ")
                    mi_servicio = servicios.consultar_informacion_servicio(conexion_db, ventas.codigo_servicio)
                    if mi_servicio is None or mi_servicio is False:
                        raise ValueError("Servicio no encontrado")

                    ventas.cantidad_vendida = input("Ingrese la cantidad a vender: ")
                    cantidad_vendida = int(ventas.cantidad_vendida)
                    if cantidad_vendida < 0:
                        raise ValueError("La cantidad no puede ser negativa")

                    #comprobar si la carga es de puestos o de encomienda
                    if mi_servicio[6] == 0:
                        carga_max = 7
                    else:
                        carga_max = 6

                    # Verificar disponibilidad
                    if not ventas.verificar_disponibilidad(conexion_db, mi_servicio, cantidad_vendida, carga_max):
                        raise ValueError("Cantidad a vender excede el espacio disponible")

                    # Insertar la venta
                    mi_venta = (
                        ventas.no_factura, ventas.no_identificacion_cliente, ventas.codigo_servicio, cantidad_vendida)
                    ventas.añadir_servicio_factura(conexion_db, mi_venta)

                    realizar_compra = input("¿El cliente desea realizar otra venta? (s/n): ")
                    if realizar_compra.lower() != 's':
                        continuar_ventas = False

                imprimir_factura = input("¿Deseas imprimir la factura de venta? (s/n): ")
                if imprimir_factura.lower() == 's':
                    facturas.imprimir_factura(conexion_db, ventas.no_factura)
            except ValueError as e:
                print(f"Error: {str(e)}")
            finally:
                ventas.no_factura = None  # Resetear el número de factura

        elif opcion_seleccionada == "2":
            no_factura = input("Ingrese el número de factura del servicio de la factura a quitar: ")
            codigo_servicio = input("Ingrese el codigo del servicio de la factura a quitar: ")
            no_identificacion_cliente = input("Ingrese el número de identificación del cliente de la factura a quitar: ")
            cantidad_vendida = input("Ingrese la cantidad que sea habia vendido de la venta de la factura  a quitar: ")
            ventas.quitar_servicio_factura(conexion_db, no_factura,codigo_servicio,no_identificacion_cliente, cantidad_vendida)

        elif opcion_seleccionada == "3":
            salir_del_menu = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def gestionar_menu_facturas(conexion_db, facturas):
    """
    Gestiona el menú de opciones para la administración de facturas.
    Opciones:
        1. Imprimir Factura.
        2. Volver al menú principal.

    Args:
        conexion_db (objeto): Objeto que gestiona la conexión a la base de datos.
        facturas (objeto): Objeto que contiene los métodos para interactuar con las facturas.

    Returns:
        None
    """
    salir_del_menu = False
    while not salir_del_menu:
        opcion_seleccionada = input("""
                        MÓDULO FACTURAS
                1. Imprimir Factura.
                2. Cancelar.

                Seleccione una opción:  """)

        if opcion_seleccionada == "1":
            no_factura = input("Ingrese el número de la factura: ")
            facturas.imprimir_factura(conexion_db, no_factura)
            salir_del_menu = True

        elif opcion_seleccionada == "2":
            salir_del_menu = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def cerrar_programa():
    """
    Cierra el programa después de una breve pausa.

    Returns:
        None
    """
    print("\nGracias por utilizar el programa.\n")
    time.sleep(1.5)
    sys.exit()


def generar_menu(conexion, servicios, ventas, clientes, facturas):
    """
    Ejecuta el menú principal, permitiendo al usuario seleccionar entre diferentes módulos o salir del programa.

    Returns:
        None
    """
    while True:
        print("Iniciando pantalla principal...")
        opcion_principal = mostrar_menu_principal()
        if opcion_principal == "1":
            gestionar_menu_servicios(conexion, servicios)
        elif opcion_principal == "2":
            gestionar_menu_clientes(conexion, clientes)
        elif opcion_principal == "3":
            gestionar_menu_ventas(conexion, servicios, clientes, ventas, facturas)
        elif opcion_principal == "4":
            gestionar_menu_facturas(conexion, facturas)
        elif opcion_principal == "5":
            cerrar_programa()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
