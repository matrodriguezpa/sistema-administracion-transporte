Clase Facturas
==============

.. automodule:: facturas
   :members:
   :undoc-members:
   :show-inheritance:

La clase ``Facturas`` maneja la generación e impresión de facturas en el sistema SAT.

Atributos
---------

* ``objetoConexion`` (objeto): Conexión a la base de datos.

Métodos
-------

.. automethod:: Facturas.__init__

.. automethod:: Facturas.imprimir_factura

Ejemplo de uso
--------------

.. code-block:: python

   # Crear una instancia de Facturas
   facturas = Facturas(conexion_db)

   # Imprimir una factura
   facturas.imprimir_factura(conexion_db, numero_factura)

Nota: Esta clase se encarga de generar y mostrar las facturas basándose en la información de ventas, clientes y servicios almacenada en la base de datos.
