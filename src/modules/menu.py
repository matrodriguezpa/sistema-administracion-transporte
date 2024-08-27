import time  # Se importa para pausar la ejecución antes de salir del programa.
import sys  # Se importa para cerrar el programa cuando el usuario lo indica.

import datetime


# menu principal
def menu_principal():
    return input("""           
           _____      ___   _______ 
          / ____|    / _ \ |__   __|       
          \____ \   / /_\ \   | |   
           ____) | / _____ \  | |   
          |_____/ /_/     \_\ |_|  

    SISTEMA DE ADMINISTRACIÓN DE TRANSPORTES 
                   LA NACIONAL

                MENU PRINCIPAL
        1. Modulo de gestión de Servicios
        2. Modulo de gestión de Clientes
        3. Modulo de ventas
        4. Modulo de facturas
        5. Cerrar programa

        Seleccione una opción: """)


# Menú de la tabla servicios

def menu_servicios(objeto_conexion, objeto_servicios):
    """Function: Gestión del menú de opciones para la administración de servicios.

    Args:
        objetoConexion (objeto): Objeto que gestiona la conexión a la base de datos.
        objetoServicios (objeto): Objeto que contiene los métodos para interactuar con los servicios.

    Opciones:
        1. Crear un nuevo servicio.
        2. Actualizar el nombre de un servicio.
        3. Consultar la información de un servicio.
        4. Volver al menú principal.

    Returns:
        None
    """

    salir_servicios = False
    while not salir_servicios:
        # Mostrar el menú de opciones
        opcion_servicios = input("""
               MÓDULO SERVICIOS
        1. Crear un nuevo servicio
        2. Actualizar el nombre de un servicio.
        3. Consultar Información de un servicio
        4. Volver

        Seleccione una opción: """)

        # Opción 1: Crear un nuevo servicio
        if opcion_servicios == "1":
            try:
                # Asignación y validación de datos
                objeto_servicios.codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not objeto_servicios.codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                objeto_servicios.codigo_servicio = int(objeto_servicios.codigo_servicio)

                objeto_servicios.nombre = input("Ingrese el nombre del servicio: ").strip()
                if not objeto_servicios.nombre:
                    raise ValueError("El nombre del servicio no puede estar vacío.")

                objeto_servicios.origen = input("Ingrese el origen del servicio: ").strip()
                if not objeto_servicios.origen:
                    raise ValueError("El origen del servicio no puede estar vacío.")

                objeto_servicios.destino = input("Ingrese el destino del servicio: ").strip()
                if not objeto_servicios.destino:
                    raise ValueError("El destino del servicio no puede estar vacío.")

                objeto_servicios.precio_venta = input("Ingrese el precio de venta del servicio: ")
                if not objeto_servicios.precio_venta.replace('.', '', 1).isdigit() or float(
                        objeto_servicios.precio_venta) <= 0:
                    raise ValueError("El precio de venta debe ser un número positivo.")
                objeto_servicios.precio_venta = float(objeto_servicios.precio_venta)

                fecha_str = input("Ingrese la fecha y hora de salida (AAAA:MM:DD:HH:MM:SS): ")
                try:
                    objeto_servicios.hora_salida = datetime.datetime.strptime(fecha_str, "%Y:%m:%d:%H:%M:%S")
                except ValueError:
                    raise ValueError("El formato de la fecha y hora es incorrecto.")

                objeto_servicios.max_puestos = input("Ingrese la cantidad máxima de puestos: ")
                if not max_puestos.isdigit() or int(objeto_servicios.max_puestos) <= 0:
                    raise ValueError("La cantidad máxima de puestos debe ser un número entero positivo.")
                objeto_servicios.max_puestos = int(objeto_servicios.max_puestos)

                objeto_servicios.max_kilos = input("Ingrese la cantidad máxima de kilos: ")
                if not objeto_servicios.max_kilos.isdigit() or int(objeto_servicios.max_kilos) < 0:
                    raise ValueError("La cantidad máxima de kilos debe ser un número entero positivo o cero.")
                objeto_servicios.max_kilos = int(objeto_servicios.max_kilos)

                # Crear la tupla con los datos validados del servicio
                print("Los datos ingresados son válidos, creando servicio.")
                mi_servicio = (objeto_servicios.codigo_servicio,
                               objeto_servicios.nombre,
                               objeto_servicios.origen,
                               objeto_servicios.destino,
                               objeto_servicios.precio_venta,
                               objeto_servicios.hora_salida,
                               objeto_servicios.max_puestos,
                               objeto_servicios.max_kilos)

                # Llamada al método para crear un nuevo servicio
                crear = objeto_servicios.crear_nuevo_servicio(objeto_conexion, mi_servicio)

                if crear:
                    print("Servicio creado exitosamente.")
                else:
                    pritn("Creación del servicio fallida")
                salir_servicios = True
            except ValueError as e:
                # Manejo de errores de validación
                print(f"Error: {e}")

        # Opción 2: Actualizar el nombre de un servicio
        elif opcion_servicios == "2":
            try:
                # Validación y asignación del código del servicio
                codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                codigo_servicio = int(codigo_servicio)

                # Validación del nuevo nombre del servicio
                nuevo_nombre = input("Ingrese el nuevo nombre del servicio: ").strip()
                if not nuevo_nombre:
                    raise ValueError("El nuevo nombre del servicio no puede estar vacío.")

                # Llamada al método para actualizar el nombre
                actualizacion = objeto_servicios.actualizar_nombre(objeto_conexion, codigo_servicio, nuevo_nombre)

                # Verificación de la actualización
                if actualizacion == True:
                    print("Nombre del servicio actualizado correctamente.")
                else:
                    print("Error al actualizar el servicio, por favor, intente nuevamente.")
                salir_servicios = True
            except ValueError as e:
                # Manejo de errores de validación
                print(f"Error: {e}")

        # Opción 3: Consultar la información de un servicio
        elif opcion_servicios == "3":
            try:
                # Validación y asignación del código del servicio
                codigo_servicio = input("Ingrese el código del servicio (número entero): ")
                if not codigo_servicio.isdigit():
                    raise ValueError("El código del servicio debe ser un número entero.")
                codigo_servicio = int(codigo_servicio)

                # Llamada al método para consultar la información del servicio
                consulta = objeto_servicios.consultar_informacion(objeto_conexion, codigo_servicio)

                # Verificación de la consulta
                if consulta:
                    print("Dato consultado:", consulta)
                else:
                    print(f"No se encontró información para el código de servicio {codigo_servicio}.")
                salir_servicios = True

            except ValueError as e:
                # Manejo de errores de validación
                print(f"Error: {e}")

        # Opción 4: Volver al menú principal
        elif opcion_servicios == "4":
            print("Se salió del módulo de Servicios.")
            salir_servicios = True


# menu de la tabla clientes
def menu_clientes(objetoConexion, objetoClientes):
    salirMenuClientes = False
    while not salirMenuClientes:
        opcionMenuClientes = input("""
                        MÓDULO CLIENTES
                1. Crear un nuevo cliente.
                2. Actualizar direcciòn del cliente.
                3. Consultar un datos de un cliente.
                4. Volver.

                Seleccione una opción:  """)

        if opcionMenuClientes == "1":
            objetoClientes.crearNuevoCliete(objetoConexion)
            salirMenuClientes = True

        elif opcionMenuClientes == "2":
            objetoClientes.actualizarTablaClientes(objetoConexion)
            salirMenuClientes = True

        elif opcionMenuClientes == "3":
            objetoClientes.consultarTablaClientes(objetoConexion)
            salirMenuClientes = True

        # salir del menu de clientes
        elif opcionMenuClientes == "4":
            salirMenuClientes = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# menu de la tabla ventas
def menu_ventas(objeto_conexion, objeto_servicios, objeto_clientes, objeto_ventas, objeto_factura):
    salir_ventas = False
    while not salir_ventas:

        opciones_ventas = input("""
                        MODULO VENTAS
                1. Vender un servicio.
                2. Quitar servicio vendido.
                3. Volver.

                Seleccione una opción:  """)

        # comprueba que los datos ingresados esten correctos antes de crear la venta en la base de datos
        if opciones_ventas == "1":
            while not salir_creacion_factura:
                try:

                    # Asignación y validación de datos

                    codigo_servicio = input("inserte el codigo del servicio a vender")
                    mi_servicio = objeto_servicios.consultar_informacion(objeto_conexion, codigo_servicio)
                    if not mi_servicio:
                        raise ValueError("El servicio que ingreso no existe.")

                    id_cliente = input("inserte la identificacion del cliente.")
                    mi_cliente = objeto_servicios.consultar_informacion(objeto_conexion, codigo_servicio)
                    if not existe_cliente:
                        raise ValueError("El cliente que ingreso no existe.")

                    cantidad_max = ""
                    # Pregunta el tipo de la venta (transporte o paquete)
                    while True:
                        tipo_venta = input("""TIPO VENTA
                                            1. Transporte
                                            2. Paquete
                                           Inserte el tipo de venta: """)
                        if tipo_venta == "1":
                            cantidad_max = mi_servicio[6]
                        elif tipo_venta == "2":
                            cantidad_max = mi_servicio[7]
                        else
                            print("Ingrese una opción valida.")

                    if cantidad_vender > cantidad_max or

                    # Se crea la venta y se consulta la información
                    mi_venta = (id_cliente, codigo_servicio, cantidad_vender, tipo_venta)
                    mi_servicio = objeto_servicios.consultar_informacion(objeto_conexion, objeto_servicios)

                    #Validación
                    if mi_servicio:
                        pass
                    else:
                        print("No existe el servicio.")

                except ValueError as e:
                    # Manejo de errores de validación
                    print(f"Error: {e}")

                print("Consultado información de Cliente: ")
                existe_cliente = objeto_servicios.consultar_informacion(objeto_conexion, objeto_servicios)
                if existe_cliente:
                    pass
                else:
                    print("No existe el servicio.")

                objeto_ventas.vender_servicio(self, objeto_conexion, mi_servicio, mi_cliente, mi_venta)

            agregar_venta = input("¿Desea agregar otra venta a la factuar? (s/n)").lower()
            if agregar_venta:
                salir_creacion_factura = true
            else:
                pass

            salir_ventas = True

        if opciones_ventas == "2":
            quiter = quitarServicioVendido(objeto_conexion, noFactura)
            if quitar:
                print("Registro borrado exitosamente.")
            else:
                print("No se pudo borrar el servicio.")
            salir_ventas = True

        # salir del menu de ventas
        elif opciones_ventas == "3":
            salir_ventas = True
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# menu de facturas
def menu_facturas(objetoConexion, objetoVentas, objetoFactura):
    salirMenuFacturas = False
    while not salirMenuFacturas:

        opcionesVentas = input("""
                        MODULO FACTURAS
                1. Imprimir factura.
                2. Enviar factura por correo.
                3. Volver.

                Seleccione una opción:  """)

        if opcionesVentas == "1":
            objetoFactura.imprimirFactura(objetoVentas)
            salirMenuFacturas = True

        if opcionesVentas == "2":
            objetoFactura.enviarCorreoFactura()
            salirMenuFacturas = True

        # salir del menu de ventas
        elif opcionesVentas == "3":
            enviarCorreo(miVenta, miCliente, miServicio)
            salirMenuFacturas = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def generar_menu(objeto_conexion, objeto_servicios, objeto_ventas, objeto_clientes, objeto_facturas):
    """Genera el menú principal de la aplicación y gestiona la navegación a los submenús correspondientes.

    Args:
        objeto_conexion (objeto): Objeto que gestiona la conexión a la base de datos.
        objeto_servicios (objeto): Objeto que contiene los métodos para interactuar con los servicios.
        objeto_ventas (objeto): Objeto que contiene los métodos para gestionar las ventas.
        objeto_clientes (objeto): Objeto que contiene los métodos para gestionar los clientes.
        objeto_facturas (objeto): Objeto que contiene los métodos para gestionar las facturas.

    Funcionalidad:
        - Presenta un menú principal al usuario.
        - Según la opción seleccionada, llama al submenú correspondiente:
            1. Menú de Servicios
            2. Menú de Clientes
            3. Menú de Ventas
            4. Menú de Facturas
            5. Cerrar el programa
        - Valida la opción seleccionada y maneja opciones inválidas.

    Returns:
        None
    """

    # Bucle infinito que mantiene el menú activo hasta que el usuario decide salir.
    while True:
        # Se llama a la función que muestra el menú principal y se obtiene la opción seleccionada.
        opcion_principal = menu_principal()

        if opcion_principal == "1":
            # Llama al submenú de servicios.
            menu_servicios(objeto_conexion, objeto_servicios)

        elif opcion_principal == "2":
            # Llama al submenú de clientes.
            menu_clientes(objeto_conexion, objeto_clientes)

        elif opcion_principal == "3":
            # Llama al submenú de ventas.
            menu_ventas(objeto_conexion, objeto_servicios, objeto_ventas, objeto_clientes)

        elif opcion_principal == "4":
            # Llama al submenú de facturas.
            menu_facturas(objeto_conexion, objeto_servicios, objeto_ventas, objeto_clientes)

        elif opcion_principal == "5":
            # Cierra el programa.
            print("Cerrando el programa.")
            time.sleep(1)  # Pausa de un segundo para que el usuario pueda leer el mensaje.
            sys.exit()  # Sale del programa.

        else:
            # Maneja el caso en que la opción ingresada no es válida.
            print("Opción no válida. Por favor, seleccione una opción válida.")
