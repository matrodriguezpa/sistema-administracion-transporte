Modulo de gestion de clientes
=============================

Parámetros
----------


Métodos
-------
 Para crear la tabla que contiene la informacion de los clientes en caso tal de que no exista anteriormente :
 
 .. py:function:: crearTablaClientes(objetoConexion)

   :param objetoConexion: conecta con las base de datos
   
 Para recibir los datos necesarios y los almacena todos en una variable se usa :

 .. py:function:: leerCliente(objetoConexion)
    
    :param objetoConexion: conecta con la base de datos
    :return: cliente
    :rtype: Tuple

 Para insertar los datos almacenados en la tabla de servicios :

 .. py:function:: insertarTablaCliente(objetoConexion,miCliente
    
    :param objetoConexion: conecta con la base de datos
    :param miCliente: donde se almacenan los datos del cliente

 Para consultar todos los registros almacenados en la tabla de clientes se usa :

 .. py:function:: consultarTablaClientes1(objetoConexion)

    :param objetoConexion: conecta con la base de datos 
 
  La informacion de todos los campos de la tabla es devuelta al usuario mediante la funcion ``print()``

 
 Para consultar cualquier dato a eleccion del usuario de un cliente en especifico :

 .. py:function:: consultarTablaClientes2(objetoConexion,datoConsulta,noIdentificacionCliente)

    :param objetoConexion: conecta con la base de datos 
    :param datoConsulta: indica que dato se quiere consultar
    :type kind: String
    :param noIdentificacionCliente: indica el ID del cliente a consultar
    :type kind: Integer 
    :return: resultadosBusqueda
    :rtype: String
 
  El dato consultado es devuelto mediante la variable "resultadosBusqueda"

 Para consultar el numero de registros que hay en la tabla :

 .. py:function:: consultarTablaClientes3(objetoConexion)
   
    :param objetoConexion: conecta con la base de datos 
    :return: total
    :rtype: String

 Para consultar un registro usando el nombre del cliente :

 .. py:function:: consultarTablaClientes4(objetoConexion,nombreConsulta)

    :param objetoConexion: conecta con la base de datos
    :param nombreCliente: Indica el nombre de el cliente
     
  Los resultados de la busqueda son devueltos mediante la funcion "print"

 Para consultar registros segun la letra inicial del nombre :

 .. py:function:: consultarTablaCientes5(objetoConexion,letraInicial)

    :param objetoConexion: conecta con la base de datos
    :param letraInicial: Indica la letra inicial por la cual se hace la busqueda

  Los resultados de la busqueda son devueltos mediante la funcion "print"

 Para actualizar el nombre de un registro :

 .. py:function:: actualizarTablaClientes(objetoConexion,nuevoNombre,noIdentificacionCliente)

    :param objetoConexion: conecta con la base de datos
    :param nuevoNombre: Indica el nuevo nombre para usar en el registro
    :param noIdentificacionCliente: indica el numero de identificacion del cliente a modificar

 Para borrar un registro :
 
 .. py:function:: borrarRegistroTablaCliente(objetoConexion,noIdentificacionCliente)

    :param objetoConexion: conecta con la base de datos
    :param codigoServicio: Indica el noIdentificacionCliente del registro a eliminar

  El resultado de el metodo se da al usuario mendiante la funcion "print"

 Para borrar la tabla :

 .. py:function:: borrarTablaCliente(objetoConexion)

    :param objetoConexion: conecta con la base de datos
