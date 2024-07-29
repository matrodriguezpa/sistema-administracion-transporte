Clase Ventas
=============

La clase `Ventas` gestiona las operaciones relacionadas con la tabla de ventas en una base de datos y el envío de facturas por correo electrónico.

.. py:class:: Ventas

   Maneja la creación, lectura, actualización y eliminación de registros de ventas, así como la capacidad para enviar facturas por correo electrónico.

Atributos
---------
- **noFactura**: Número único de la factura para identificar cada venta.
- **noIdentificacionCliente**: Número de identificación del cliente que realiza la compra.
- **codigoServicio**: Código único del servicio que se está vendiendo.
- **cantidadVendida**: Cantidad de unidades del servicio vendidas.

Métodos
-------

.. py:method:: crearTablaVentas(self, con)

    Crea la tabla `Ventas` en la base de datos si no existe.

    :param con: Objeto de conexión a la base de datos.
    :type con: Objeto de conexión
    :return: None

.. py:method:: leerVenta(self, objetoConexion, objetoVentas)

    Lee y genera un nuevo registro de venta solicitando al usuario los datos necesarios.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :param objetoVentas: Instancia de la clase que maneja la consulta de ventas.
    :type objetoVentas: Ventas
    :return: tuple de los datos de la venta generada

.. py:method:: añadirServicioAVender(self, objetoConexion, miVenta)

    Añade un nuevo registro de venta a la base de datos.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :param miVenta: Datos de la venta a insertar.
    :type miVenta: tuple
    :return: None

.. py:method:: consultarTablaVentas1(self, objetoConexion)

    Consulta y muestra todos los registros en la tabla `Ventas`.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :return: None

.. py:method:: consultarTablaVentas2(self, objetoConexion, dato, noFactura)

    Consulta un dato específico en la tabla `Ventas` basado en el número de factura.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :param dato: El dato a consultar.
    :type dato: str
    :param noFactura: Número de factura a buscar.
    :type noFactura: str
    :return: El valor del dato consultado o None si no se encuentra.

.. py:method:: consultarTablaVentas3(self, con)

    Consulta el número total de registros en la tabla `Ventas`.

    :param con: Objeto de conexión a la base de datos.
    :type con: Objeto de conexión
    :return: Número total de registros en la tabla.

.. py:method:: consultarTablaVentas4(self, objetoConexion, dato, datoConsulta)

    Consulta registros en la tabla `Ventas` basado en un dato específico.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :param dato: El dato a consultar.
    :type dato: str
    :param datoConsulta: Valor del dato a buscar.
    :type datoConsulta: str
    :return: Lista de registros que coinciden con la consulta o None si no se encuentran.

.. py:method:: consultarTablaVentas5(self, objetoConexion)

    Consulta la suma total de las cantidades vendidas en la tabla `Ventas`.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :return: La suma total de las cantidades vendidas o 0 si no hay ventas.

.. py:method:: borrarRegistroTablaVentas(self, objetoConexion, noFactura)

    Borra un registro específico en la tabla `Ventas` basado en el número de factura.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :param noFactura: Número de factura del registro a borrar.
    :type noFactura: str
    :return: None

.. py:method:: borrarTablaVentas(self, objetoConexion)

    Borra toda la tabla `Ventas`.

    :param objetoConexion: Objeto de conexión a la base de datos.
    :type objetoConexion: Objeto de conexión
    :return: None

.. py:method:: imprimirFactura(self, miVenta, miCliente, miServicio)

    Envía la factura de una venta por correo electrónico.

    :param miVenta: Datos de la venta.
    :type miVenta: tuple
    :param miCliente: Datos del cliente.
    :type miCliente: tuple
    :param miServicio: Datos del servicio.
    :type miServicio: tuple
    :return: None
