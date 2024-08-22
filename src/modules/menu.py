import sys  # para cerrar el programa desde la interfáz y
import time


# menu principal
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
        4. Modulo de facturas
        5. Cerrar programa

        Seleccione una opción: """)


# menu de la tabla servicios
def menuServicios(objetoConexion, objetoServicios):
    salirMenuServicios = False
    while not salirMenuServicios:
        opcionMenuServicios = input("""
               MÓDULO SERVICIOS
        1. Crear un nuevo servicio
        2. Actualizar el nombre de un servicio.
        3. Consultar Informaciòn de un servicio
        4. Volver

        Seleccione una opción: """)

        if opcionMenuServicios == "1":
            salirMenuServicios = True

        elif opcionMenuServicios == "2":
            salirMenuServicios = True

        elif opcionMenuServicios == "3":
            salirMenuServicios = True

        elif opcionMenuServicios == "4":
            salirMenuServicios = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# menu de la tabla clientes
def menuClientes(objetoConexion, objetoClientes):
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
            salirMenuClientes = True

        elif opcionMenuClientes == "2":
            salirMenuClientes = True

        elif opcionMenuClientes == "3":
            salirMenuClientes = True
        # salir del menu de clientes

        elif opcionMenuClientes == "4":
            salirMenuClientes = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# menu de la tabla ventas
def menuVentas(objetoConexion, objetoServicios, objetoVentas, objetoClientes):
    salirMenuVentas = False
    while not salirMenuVentas:

        opcionesVentas = input("""
                        MODULO VENTAS
                1. Vender un servicio.
                2. Quitar servicio vendido.
                3. Volver.

                Seleccione una opción:  """)

        # comprueba que los datos ingresados esten correctos antes de crear la venta en la base de datos
        if opcionesVentas == "1":
            salirMenuVentas = True

        if opcionesVentas == "2":
            salirMenuVentas = True

        # salir del menu de ventas
        elif opcionesVentas == "3":
            salirMenuVentas = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# menu de facturas
def menuFacturas(objetoConexion, objetoServicios, objetoVentas, objetoClientes):
    salirMenuFacturas = False
    while not salirMenuFacturas:

        opcionesVentas = input("""
                        MODULO FACTURAS
                1. Imprimir factura.
                2. Enviar factura por correo.
                3. Volver.

                Seleccione una opción:  """)

        if opcionesVentas == "1":
            salirMenuFacturas = True

        if opcionesVentas == "2":
            salirMenuFacturas = True

        # salir del menu de ventas
        elif opcionesVentas == "3":
            salirMenuFacturas = True

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Generar menu
def generarMenu(objetoConexion, objetoServicios, objetoVentas, objetoClientes, objetoFacturas):
    # a partir del menu principal, llama a los submenus necesarios selecionados por el usuario.
    while True:
        opcionMenuPrincipal = menuPrincipal()

        if opcionMenuPrincipal == "1":
            menuServicios(objetoConexion, objetoServicios)

        elif opcionMenuPrincipal == "2":
            menuClientes(objetoConexion, objetoClientes)

        elif opcionMenuPrincipal == "3":
            menuVentas(objetoConexion, objetoServicios, objetoVentas, objetoClientes)

        elif opcionMenuPrincipal == "4":
            menuFacturas(objetoConexion, objetoServicios, objetoVentas, objetoClientes)

        elif opcionMenuPrincipal == "5":
            print("Cerrando el programa.")
            time.sleep(1)  # se pausa un segundo para que el usuario pueda leer el mensaje antes de que se cierre.
            sys.exit()

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
