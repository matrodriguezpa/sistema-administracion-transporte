Clase Clientes
==============

.. automodule:: clientes
   :members:
   :undoc-members:
   :show-inheritance:

La clase ``Clientes`` representa a un cliente en el sistema SAT.

Atributos
---------

* ``no_identificacion_cliente`` (int): Número de identificación único del cliente.
* ``nombre`` (str): Nombre del cliente.
* ``apellido`` (str): Apellido del cliente.
* ``direccion`` (str): Dirección del cliente.
* ``telefono`` (str): Número de teléfono del cliente.
* ``correo_electronico`` (str): Correo electrónico del cliente.

Métodos
-------

.. automethod:: Clientes.__init__

.. automethod:: Clientes.crear_nuevo_cliente

.. automethod:: Clientes.actualizar_direccion_cliente

.. automethod:: Clientes.consultar_informacion_cliente

Ejemplo de uso
--------------

.. code-block:: python

   # Crear una instancia de Clientes
   clientes = Clientes(conexion_db)

   # Crear un nuevo cliente
   nuevo_cliente = (1001, "Juan", "Pérez", "Calle 123 #45-67", "1234567890", "juan@example.com")
   clientes.crear_nuevo_cliente(conexion_db, nuevo_cliente)

   # Actualizar la dirección de un cliente
   clientes.actualizar_direccion_cliente(conexion_db, 1001, "Avenida 456 #78-90")

   # Consultar información de un cliente
   info_cliente = clientes.consultar_informacion_cliente(conexion_db, 1001)
   print(info_cliente)
