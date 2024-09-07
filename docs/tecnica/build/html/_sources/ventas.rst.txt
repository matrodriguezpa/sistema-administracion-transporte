Clase Ventas
============

.. automodule:: ventas
   :members:
   :undoc-members:
   :show-inheritance:

La clase ``Ventas`` representa una venta en el sistema SAT.

Atributos
---------

* ``no_factura`` (int): Número de factura de la venta.
* ``no_identificacion_cliente`` (int): Número de identificación del cliente.
* ``codigo_servicio`` (int): Código del servicio vendido.
* ``cantidad_vendida`` (int): Cantidad vendida del servicio.

Métodos
-------

.. automethod:: Ventas.__init__

.. automethod:: Ventas.generar_numero_factura

.. automethod:: Ventas.verificar_disponibilidad

.. automethod:: Ventas.añadir_servicio_factura

.. automethod:: Ventas.quitar_servicio_factura

Ejemplo de uso
--------------

.. code-block:: python

   # Crear una instancia de Ventas
   ventas = Ventas(conexion_db)

   # Generar un nuevo número de factura
   nuevo_no_factura = ventas.generar_numero_factura(conexion_db)

   # Verificar disponibilidad antes de la venta
   if ventas.verificar_disponibilidad(conexion_db, servicio, cantidad, carga_max):
       # Añadir un servicio a la factura
       venta = (nuevo_no_factura, id_cliente, codigo_servicio, cantidad)
       ventas.añadir_servicio_factura(conexion_db, venta)

   # Quitar un servicio de la factura
   ventas.quitar_servicio_factura(conexion_db, nuevo_no_factura)

Nota: Esta clase maneja las operaciones relacionadas con las ventas, incluyendo la generación de números de factura, verificación de disponibilidad y registro de ventas en la base de datos.
