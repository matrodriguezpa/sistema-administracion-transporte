Módulo gestion de clientes
==========================

.. py:class:: Clientes
    Clase para gestionar la tabla clientes de la base de datos.

Atributos
---------
- **noIdentificacionCliente**: Número de identificación del cliente.
- **nombre**: Nombre del cliente.
- **apellido**: Apellido del cliente.
- **direccion**: Dirección del cliente.
- **telefono**: Número de teléfono del cliente.
- **correoElectronico**: Correo electrónico del cliente.

Métodos
-------

.. py:function:: Clientes.crearTablaClientes(objetoConexion)

   Crea la tabla 'Clientes' en la base de datos si no existe.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None

.. py:function:: Clientes.leerCliente()

   Solicita al usuario los datos de un cliente y los retorna como una tupla.

   :return: Datos del cliente ingresados por el usuario.
   :rtype: tuple

.. py:function:: Clientes.insertarTablaClientes(objetoConexion, miCliente)

   Inserta un nuevo cliente en la tabla 'Clientes'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param miCliente: Datos del cliente a insertar.
   :type miCliente: tuple
   :return: None

.. py:function:: Clientes.consultarTablaClientes1(objetoConexion)

   Consulta y muestra todos los registros de la tabla 'Clientes'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None

.. py:function:: Clientes.consultarTablaClientes2(objetoConexion, datoConsulta, noIdentificacionCliente)

   Consulta un dato específico de un cliente.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param datoConsulta: Nombre de la columna a consultar.
   :type datoConsulta: str
   :param noIdentificacionCliente: Número de identificación del cliente a consultar.
   :type noIdentificacionCliente: int
   :return: Valor del dato consultado.
   :rtype: str

.. py:function:: Clientes.consultarTablaSClientes3(objetoConexion)

   Consulta la cantidad total de registros en la tabla 'Clientes'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: Cantidad total de registros.
   :rtype: int

.. py:function:: Clientes.consultarTablaClientes4(objetoConexion, dato, consulta)

   Consulta registros en la tabla 'Clientes' filtrados por un dato específico.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param dato: Nombre de la columna por la cual filtrar.
   :type dato: str
   :param consulta: Valor del dato a buscar.
   :type consulta: str
   :return: Primer registro coincidente.
   :rtype: tuple

.. py:function:: Clientes.consultarTablaClientes5(objetoConexion, letraInicial)

   Consulta registros en la tabla 'Clientes' filtrados por la letra inicial del nombre.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param letraInicial: Letra inicial para filtrar los nombres.
   :type letraInicial: str
   :return: Lista de registros que cumplen con el filtro.
   :rtype: list

.. py:function:: Clientes.actualizarTablaClientes(objetoConexion, nuevoNombre, noIdentificacionCliente)

   Actualiza el nombre de un cliente en la tabla 'Clientes'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param nuevoNombre: Nuevo nombre para el cliente.
   :type nuevoNombre: str
   :param noIdentificacionCliente: Número de identificación del cliente a actualizar.
   :type noIdentificacionCliente: int
   :return: None

.. py:function:: Clientes.borrarRegistroTablaClientes(objetoConexion, noIdentificacionCliente)

   Elimina un registro de la tabla 'Clientes'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param noIdentificacionCliente: Número de identificación del cliente a eliminar.
   :type noIdentificacionCliente: int
   :return: None

.. py:function:: Clientes.borrarTablaClientes(objetoConexion)

   Elimina la tabla 'Clientes' de la base de datos.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None
