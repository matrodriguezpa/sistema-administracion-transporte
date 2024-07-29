Modulo de gestion de clientes
=============================

Parámetros
----------


Métodos
-------
 Para crear la tabla que contiene la informacion de los clientes en caso tal de que no exista anteriormente :
 
 .. py:function:: crearTablaClientes(objetoConexion)

   :param objetoConexion: conecta con las base de datos
   
  "servicio = (codigoServicio, nombre, origen, destino, precioVenta, horaSalida, puestosMaximo, kilosMaximo)"

 Para recibir los datos necesarios y los almacena todos en una variable se usa :

 .. py:function:: leerServicio(objetoConexion)
    
    :param objetoConexion: conecta con la base de datos
    :return: DatoConsultado
    :rtype: String

 Para insertar los datos almacenados en la tabla de servicios :

 .. py:function:: insertarServicio(objetoConexion,miServicio)
    
    :param objetoConexion: conecta con la base de datos
    :param miServicio: donde se almacenan los datos de servicios

 Para consultar todos los registros almacenados en la tabla de servicios se usa :

 .. py:function:: consultarTablaServicios1(objetoConexion)

    :param objetoConexion: conecta con la base de datos 
 
  La informacion de todos los campos de la tabla es devuelta al usuario mediante la funcion ``print()``

 Para consultar la fecha y hora de salida de los todos los registros de la tabla de crearTablaServicios :

 .. py:function:: consultarTablaServicios2(objetoConexion)

    :param objetoConexion: conecta con la  base de datos

  La informacion de los campos correspondientes a el indice del servicio , el codigo del servicio , nombre del servicio , origen del servicio , fecha y hora del servcio mediante la funcion ``print``

 Para consultar los puestos maximos y el peso maximo de cada servicio se usa:

 .. py:function:: consultarTablaServicios3(objetoConexion)
    
    :param objetoConexion: conecta con la base de datos

  La informacion de los campos correspondientes a el indice del servicio , codigo del servicio , nombre del servicio, origen , destino , puestos y kilos mediante la funcion ``print``

 Para consultar cualquier dato a eleccion del usuario de un servicio en especifico :

 .. py:function:: consultarTablaServicios4(objetoConexion,dato,codigoServicio)

    :param objetoConexion: conecta con la base de datos 
    :param dato: indica que dato se quiere consultar
    :type kind: String
    :param codigoServicio: indica el codigo del servicio a consultar 
    :type kind: Integer 
    :return: DatoConsultado
    :rtype: String
 
  El dato consultado es devuelto mediante la variable "DatoConsultado"

 Para consultar el numero de registros que hay en la tabla :

 .. py:function:: consultarTablaServicios5(objetoConexion)
   
    :param objetoConexion: conecta con la base de datos 
    :return: totalRegistros
    :rtype: String

  El numero de registros es devuelto mediante la variable "totalRegistros"

 Para consultar la suma de los precios de la venta :

 .. py:function:: consultarTablaServicios6(objetoConexion)

    :param objetoConexion: conecta con la base de datos 
    :return: sumaPrecios
    :rtype: String

  La suma de los precios es devuelta mediente la variable "sumaPrecios"

 Para consultar un registro usando el nombre del mismo :

 .. py:function:: consultarTablaServicios7(objetoConexion,nombre)

    :param objetoConexion: conecta con la base de datos
    :param nombre: Indica el nombre de el registro 
     
  Los resultados de la busqueda son devueltos mediante la funcion "print"

 Para consultar registros segun la letra inicial del nombre :

 .. py:function:: consultarTablaServicios8(objetoConexion,letraInicial)

    :param objetoConexion: conecta con la base de datos
    :param letraInicial: Indica la letra inicial por la cual se hace la busqueda

  Los resultados de la busqueda son devueltos mediante la funcion "print"

 Para actualizar el nombre de un registro :

 .. py:function:: actualizarTablaServicios(objetoConexion,nuevoNombre,codigoServicio)

    :param objetoConexion: conecta con la base de datos
    :param nuevoNombre: Indica el nuevo nombre para usar en el registro
    :param codigoServicio: indica el codigo del servicio a modificar

 Para borrar un registro :
 
 .. py:function:: borrarRegistroTablaServicios(objetoConexion,codigoServicio)

    :param objetoConexion: conecta con la base de datos
    :param codigoServicio: Indica el codigo del servicio a eliminar

  El resultado de el metodo se da al usuario mendiante la funcion "print"

 Para borrar la tabla :

 .. py:function:: borrarTablaServicios(objetoConexion)

    :param objetoConexion: conecta con la base de datos
