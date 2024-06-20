
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
        if(opcPrincipal=='1'):
            salirPrincipal=False
        
        #Menú de gestión de clientes 
        elif(opcPrincipal=='2'):
            salirPrincipal=False

        #Menú de gestión de servicios
        elif(opcPrincipal=='3'):
            salirPrincipal=True

            while not salirServicios:
                opcionServicios=input('''
                    //---SERVICIOS---//

                1.Insertar un servicio leido por teclado
                2.Insertar un servicio
                3.Consultar un servicio
                3.Actualizar un servicio
                3.Borrar un servicio
                ...
                13.Volver

                Seleccione una opción: ''')
                
                if(opcionServicios=='1'):
                    servicioCreado=objServicios.leerServicio()
                    objServicios.insertarTablaServicios(miConexion,servicioCreado)
                if(opcionServicios=='2'):
                    objServicios.insertarTablaServicios2(miConexion)
                if(opcionServicios=='3'):
                    objServicios.consultarTablaServicios(miConexion)
                if(opcionServicios=='13'):
                    salirServicios=True
