Menú Principal
==============

.. py:class:: Menu

   Clase que representa un sistema de administración de transportes con menús para gestionar servicios, clientes y ventas.

   **Librerías:**
   
   - **sys**: Utilizada para cerrar el programa desde la interfaz.
   - **time**: Utilizada para pausar el programa, proporcionando una breve demora.

   **Notas:**
   
   - Cada método de menú contiene un bucle para manejar las opciones seleccionadas por el usuario.
   - Las operaciones de CRUD (Crear, Leer, Actualizar, Borrar) se gestionan a través de métodos específicos para servicios, clientes y ventas.
   - Se realizan validaciones para asegurar la integridad de los datos ingresados por el usuario.

.. py:function:: Menu.menuPrincipal()

   Muestra el menú principal del sistema.

   :return: La opción seleccionada por el usuario.
   :rtype: str

.. py:function:: Menu.menuServicios(objetoConexion, objetoServicios)

   Muestra el menú para gestionar la tabla de servicios.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param objetoServicios: Objeto que maneja las operaciones en la tabla de servicios.
   :type objetoServicios: Clase que maneja la tabla de servicios
   :return: None

.. py:function:: Menu.menuClientes(objetoConexion, objetoClientes)

   Muestra el menú para gestionar la tabla de clientes.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param objetoClientes: Objeto que maneja las operaciones en la tabla de clientes.
   :type objetoClientes: Clase que maneja la tabla de clientes
   :return: None

.. py:function:: Menu.menuVentas(objetoConexion, objetoServicios, objetoVentas, objetoClientes)

   Muestra el menú para gestionar la tabla de ventas.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param objetoServicios: Objeto que maneja las operaciones en la tabla de servicios.
   :type objetoServicios: Clase que maneja la tabla de servicios
   :param objetoVentas: Objeto que maneja las operaciones en la tabla de ventas.
   :type objetoVentas: Clase que maneja la tabla de ventas
   :param objetoClientes: Objeto que maneja las operaciones en la tabla de clientes.
   :type objetoClientes: Clase que maneja la tabla de clientes
   :return: None

.. py:function:: Menu.menu(objetoConexion, objetoServicios, objetoVentas, objetoClientes, objetoMenu)

   Inicia el menú principal y gestiona la creación de tablas y la navegación del usuario.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param objetoServicios: Objeto que maneja las operaciones en la tabla de servicios.
   :type objetoServicios: Clase que maneja la tabla de servicios
   :param objetoVentas: Objeto que maneja las operaciones en la tabla de ventas.
   :type objetoVentas: Clase que maneja la tabla de ventas
   :param objetoClientes: Objeto que maneja las operaciones en la tabla de clientes.
   :type objetoClientes: Clase que maneja la tabla de clientes
   :param objetoMenu: Instancia de la clase Menu para manejar la navegación entre menús.
   :type objetoMenu: Clase Menu
   :return: None
