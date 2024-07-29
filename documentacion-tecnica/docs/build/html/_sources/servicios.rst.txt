Módulo gestion de servicios
===========================

.. py:class:: Servicios

   Clase para gestionar la tabla servicios de la base de datos.

Atributos
---------
- **codigoServicio**: Código único del servicio.
- **nombre**: Nombre del servicio.
- **origen**: Ciudad de origen del servicio.
- **destino**: Ciudad de destino del servicio.
- **precioVenta**: Precio de venta del servicio.
- **horaSalida**: Fecha y hora de salida del servicio.
- **cantidadMaxPuestos**: Cantidad máxima de puestos disponibles.
- **cantidadMaxKilos**: Peso máximo permitido en kilogramos.

Métodos
-------

.. py:function:: Servicios.crearTablaServicios(objetoConexion)

   Crea la tabla 'servicios' en la base de datos si no existe.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None

.. py:function:: Servicios.leerServicio()

   Solicita al usuario los datos de un servicio y los retorna como una tupla.

   :return: Datos del servicio ingresados por el usuario.
   :rtype: tuple

.. py:function:: Servicios.insertarServicio(objetoConexion, miServicio)

   Inserta un nuevo servicio en la tabla 'servicios'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param miServicio: Datos del servicio a insertar.
   :type miServicio: tuple
   :return: None

.. py:function:: Servicios.consultarTablaServicios1(objetoConexion)

   Consulta y muestra todos los registros de la tabla 'servicios'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None

.. py:function:: Servicios.consultarTablaServicios2(objetoConexion)

   Consulta y muestra el código, nombre, origen, fecha y hora de salida de todos los registros.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None

.. py:function:: Servicios.consultarTablaServicios3(objetoConexion)

   Consulta y muestra los puestos máximos y peso máximo de todos los registros.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None

.. py:function:: Servicios.consultarTablaServicios4(objetoConexion, dato, codigoServicio)

   Consulta un dato específico de un servicio.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param dato: Nombre de la columna a consultar.
   :type dato: str
   :param codigoServicio: Código del servicio a consultar.
   :type codigoServicio: int
   :return: Valor del dato consultado.
   :rtype: str

.. py:function:: Servicios.consultarTablaServicios5(objetoConexion)

   Consulta la cantidad total de registros en la tabla 'servicios'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: Cantidad total de registros.
   :rtype: int

.. py:function:: Servicios.consultarTablaServicios6(objetoConexion)

   Consulta la suma de los precios de venta de todos los servicios.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: Suma total de los precios de venta.
   :rtype: float

.. py:function:: Servicios.consultarTablaServicios7(objetoConexion, dato, nombre)

   Consulta registros en la tabla 'servicios' filtrados por un dato específico.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param dato: Nombre de la columna por la cual filtrar.
   :type dato: str
   :param nombre: Valor del dato a buscar.
   :type nombre: str
   :return: Primer registro coincidente.
   :rtype: tuple

.. py:function:: Servicios.consultarTablaServicios8(objetoConexion, letraInicial)

   Consulta registros en la tabla 'servicios' filtrados por la letra inicial del nombre.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param letraInicial: Letra inicial para filtrar los nombres.
   :type letraInicial: str
   :return: Lista de registros que cumplen con el filtro.
   :rtype: list

.. py:function:: Servicios.actualizarTablaServicios(objetoConexion, nuevoNombre, codigoServicio)

   Actualiza el nombre de un registro en la tabla 'servicios'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param nuevoNombre: Nuevo nombre para el servicio.
   :type nuevoNombre: str
   :param codigoServicio: Código del servicio a actualizar.
   :type codigoServicio: int
   :return: None

.. py:function:: Servicios.borrarRegistroTablaServicios(objetoConexion, codigoServicio)

   Elimina un registro de la tabla 'servicios'.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :param codigoServicio: Código del servicio a eliminar.
   :type codigoServicio: int
   :return: None

.. py:function:: Servicios.borrarTablaServicios(objetoConexion)

   Elimina la tabla 'servicios' de la base de datos.

   :param objetoConexion: Objeto de conexión a la base de datos.
   :type objetoConexion: Objeto de conexión
   :return: None
