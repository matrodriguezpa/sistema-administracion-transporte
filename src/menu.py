
def menu(miConexion,objServicios):
    salirPrincipal=False
    while not salirPrincipal:
        opcPrincipal=input('''
                           
//--------- Sistema de información Cooperativa de transportes la nacional-----------//

                    //---MENU PRINCIPAL---//

                1.Menú de Ventas
                2.Menú de gestión de Clientes
                3.Menú de gestión de Servicios

                Seleccione una opción: ''')
        
        #Menú de ventas
        if(opcPrincipal=='2'):
            salirPrincipal=True
            salirVentas=False

            while not salirVentas:
                opcionVentas=input('''
                    //---Ventas---//

                1.Insertar un servicio leido por el teclado.
                2.Salir
                                   ''')
                if(opcionVentas=='1'):
                    salirVentas=True
                if(opcionVentas=='2'):
                    salirVentas=True
        
        #Menú de gestión de clientes 
        elif(opcPrincipal=='2'):
            salirPrincipal=True
            salirClientes=False

            while not salirClientes:
                opcionClientes=input('''
                    //---CLIENTES---//

                1.Insertar un servicio leido por el teclado.
                2.Salir
                                     ''')
                if(opcionClientes=='1'):
                    salirClientes=True
                elif(opcionClientes=='2'):
                    salirClientes=True

        #Menú de gestión de servicios
        elif(opcPrincipal=='3'):
            salirPrincipal=True
            salirServicios=False

            while not salirServicios:
                opcionServicios=input('''
                    //---SERVICIOS---//

                1.Insertar un servicio leido por el teclado.
                2.Consultar todos los registros de la tabla servicios.
                3.Consultar fecha y hora de salida.
                4.Consultar puestos máximos y peso máximos.
                5.Consultar cuantos registros hay en la base de datos.
                6.Consultar suma de los precios de las ventas.
                7.Consultar registro por nombre.
                8.Consultar registros por letra.
                9.Actualizar el nombre de un registro.
                10.Actualizar el origen de un registro.
                11.Actualizar el destino de un registro.
                12.Actualizar el precio de venta de un registro.
                13.Actualizar la hora de salisade un registro.
                14.Actualizar la cantidad máxima de puestos de un registro.
                15.Actualizar la cantidad máxima de kilos de un registro.
                16.Borrar un registro.
                17.Borrar la tabla servicios.
                18.Volver.

                Seleccione una opción: ''')
                
                if(opcionServicios=='1'):
                    servicioCreado=objServicios.leerServicio()
                    objServicios.insertarTablaServicios(miConexion,servicioCreado)
                elif(opcionServicios=='2'):
                    objServicios.consultarTablaServicios0(miConexion)
                elif(opcionServicios=='13'):
                    salirServicios=True