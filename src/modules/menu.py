import time  # Se utiliza para pausar la ejecución antes de salir del programa.
import sys  # Se utiliza para cerrar el programa cuando el usuario lo indica.
import datetime  # Se utiliza para manejar fechas y horas.


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
                # Captura y validación de los datos del nuevo servicio
                servicios.codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not servicios.codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                servicios.codigo_servicio = int(servicios.codigo_servicio)

                servicios.nombre = input("Ingrese el nombre del servicio: ").strip()
                if not servicios.nombre:
                    raise ValueError("El nombre del servicio no puede estar vacío.")

                servicios.origen = input("Ingrese el origen del servicio: ").strip()
                if not servicios.origen:
                    raise ValueError("El origen del servicio no puede estar vacío.")

                servicios.destino = input("Ingrese el destino del servicio: ").strip()
                if not servicios.destino:
                    raise ValueError("El destino del servicio no puede estar vacío.")

                servicios.precio_venta = input("Ingrese el precio de venta del servicio: ")
                if not servicios.precio_venta.replace('.', '', 1).isdigit() or float(servicios.precio_venta) <= 0:
                    raise ValueError("El precio de venta debe ser un número positivo.")
                servicios.precio_venta = float(servicios.precio_venta)

                hora_minuto_str = input("Ingrese la hora de salida (HH:MM): ")

                try:
                    # Obtener la fecha actual
                    fecha_actual = datetime.now().date()

                    # Combinar la fecha actual con la hora y minutos ingresados, y establecer los segundos en 0
                    servicios.hora_salida = datetime.strptime(f"{fecha_actual} {hora_minuto_str}:00",
                                                              "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    raise ValueError("El formato de la hora es incorrecto. Use 'HH:MM'.")

                servicios.max_puestos = input("Ingrese la cantidad máxima de puestos: ")
                if not servicios.max_puestos.isdigit() or int(servicios.max_puestos) <= 0:
                    raise ValueError("La cantidad máxima de puestos debe ser un número entero positivo.")
                servicios.max_puestos = int(servicios.max_puestos)

                servicios.max_kilos = input("Ingrese la cantidad máxima de kilos: ")
                if not servicios.max_kilos.isdigit() or int(servicios.max_kilos) < 0:
                    raise ValueError("La cantidad máxima de kilos debe ser un número entero positivo o cero.")
                servicios.max_kilos = int(servicios.max_kilos)

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
                creacion_exitosa = servicios.crear_nuevo_servicio(conexion_db, nuevo_servicio)

                salir_del_menu = True
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion_seleccionada == "2":
            try:
                codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                codigo_servicio = int(codigo_servicio)

                nuevo_nombre = input("Ingrese el nuevo nombre del servicio: ").strip()
                if not nuevo_nombre:
                    raise ValueError("El nuevo nombre del servicio no puede estar vacío.")

                actualizacion_exitosa = servicios.actualizar_nombre_servicio(conexion_db, codigo_servicio, nuevo_nombre)

                if actualizacion_exitosa:
                    print("Nombre del servicio actualizado correctamente.")
                else:
                    print("Error al actualizar el servicio, por favor, intente nuevamente.")
                salir_del_menu = True
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion_seleccionada == "3":
            try:
                codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                codigo_servicio = int(codigo_servicio)

                informacion_servicio = servicios.consultar_informacion_servicio(conexion_db, codigo_servicio)

                if informacion_servicio:
                    print("Información del servicio:", informacion_servicio)
                else:
                    print(f"No se encontró información para el código de servicio {codigo_servicio}.")
                salir_del_menu = True

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion_seleccionada == "4":
            print("Saliendo del módulo de Servicios.")
            salir_del_menu = True


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
            clientes.crear_nuevo_cliente(conexion_db)
            salir_del_menu = True

        elif opcion_seleccionada == "2":
            clientes.actualizar_direccion_cliente(conexion_db)
            salir_del_menu = True

        elif opcion_seleccionada == "3":
            clientes.consultar_datos_cliente(conexion_db)
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
            salir_factura = False
            while not salir_factura:
                ventas.añadir_servicio_factura(conexion_db, servicios, clientes, facturas)
                salir_factura = True
            salir_del_menu = True

        elif opcion_seleccionada == "2":
            ventas.quitar_servicio_factura(conexion_db)
            salir_del_menu = True

        elif opcion_seleccionada == "3":
            salir_del_menu = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def gestionar_menu_facturas(conexion_db, facturas):
    """Gestiona el menú de opciones para la administración de facturas.

    Args:
        conexion_db (objeto): Objeto que gestiona la conexión a la base de datos.
        facturas (objeto): Objeto que contiene los métodos para interactuar con las facturas.

    Opciones:
        1. Consultar Factura.
        2. Volver al menú principal.

    Returns:
        None
    """
    salir_del_menu = False
    while not salir_del_menu:
        opcion_seleccionada = input("""
                        MÓDULO FACTURAS
                1. Consultar Factura.
                2. Volver.

                Seleccione una opción:  """)

        if opcion_seleccionada == "1":
            facturas.consultar_factura(conexion_db)
            salir_del_menu = True

        elif opcion_seleccionada == "2":
            salir_del_menu = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def cerrar_programa():
    """Cierra el programa después de una breve pausa.

    Returns:
        None
    """
    print("\nGracias por utilizar el programa.\n")
    time.sleep(1.5)
    sys.exit()


def generar_menu(conexion, servicios, ventas, clientes, facturas):
    """Ejecuta el menú principal, permitiendo al usuario seleccionar entre diferentes módulos o salir del programa.

    Returns:
        None
    """
    while True:
        print("Iniciando programa.")
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
