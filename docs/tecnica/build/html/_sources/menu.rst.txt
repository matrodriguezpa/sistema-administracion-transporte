Funciones del Menú Principal
============================

Este módulo contiene las funciones principales para la gestión del menú y la interacción con el usuario en el sistema SAT.

Funciones
---------

.. autofunction:: mostrar_menu_principal

.. autofunction:: gestionar_menu_servicios

.. autofunction:: gestionar_menu_clientes

.. autofunction:: gestionar_menu_ventas

.. autofunction:: gestionar_menu_facturas

.. autofunction:: cerrar_programa

.. autofunction:: generar_menu

Ejemplo de uso
--------------

.. code-block:: python

   # Inicializar objetos necesarios
   conexion_db = ...  # Crear conexión a la base de datos
   servicios = Servicios(conexion_db)
   clientes = Clientes(conexion_db)
   ventas = Ventas(conexion_db)
   facturas = Facturas(conexion_db)

   # Ejecutar el menú principal
   generar_menu(conexion_db, servicios, ventas, clientes, facturas)

Nota: Este módulo maneja la interacción principal con el usuario y coordina las diferentes funcionalidades del sistema SAT.
