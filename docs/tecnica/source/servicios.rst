Clase Servicios
===============

.. automodule:: servicios
   :members:
   :undoc-members:
   :show-inheritance:

La clase ``Servicios`` representa un servicio de transporte en el sistema SAT.

Atributos
---------

* ``codigo_servicio`` (int): Código único del servicio.
* ``nombre`` (str): Nombre del servicio.
* ``origen`` (str): Lugar de origen del servicio.
* ``destino`` (str): Lugar de destino del servicio.
* ``precio_venta`` (float): Precio de venta del servicio.
* ``hora_salida`` (datetime): Hora de salida del servicio.
* ``cantidad_max_puestos`` (int): Cantidad máxima de puestos disponibles.
* ``cantidad_max_kilos`` (int): Cantidad máxima de kilos permitidos.

Métodos
-------

.. automethod:: Servicios.__init__

.. automethod:: Servicios.crear_nuevo_servicio

.. automethod:: Servicios.actualizar_nombre_servicio

.. automethod:: Servicios.consultar_informacion_servicio

Ejemplo de uso
--------------

.. code-block:: python

   # Crear una instancia de Servicios
   servicios = Servicios(conexion_db)

   # Crear un nuevo servicio
   nuevo_servicio = (1, "Ruta Express", "Ciudad A", "Ciudad B", 50.0, "2023-09-01 08:00:00", 50, 1000)
   servicios.crear_nuevo_servicio(conexion_db, nuevo_servicio)

   # Actualizar el nombre de un servicio
   servicios.actualizar_nombre_servicio(conexion_db, 1, "Ruta Rápida")

   # Consultar información de un servicio
   info_servicio = servicios.consultar_informacion_servicio(conexion_db, 1)
   print(info_servicio)
