# Sistema de administración de transporte - Cooperativa La nacional
Este proyecto es una aplicación para gestionar los servicios ofrecidos, los clientes y la venta de estos servicios a clientes, así como la impresión de facturas. 

## Características

### Módulo de Gestión de Servicios

Este módulo permite gestionar una base de datos de servicios ofrecidos por la empresa.

- **Base de datos de servicios**:
    - Código del producto (identificador único)
    - Nombre del producto
    - Origen
    - Destino
    - Precio de venta por pasajero o kilo
    - Hora de salida (HH:MM:SS)
    - Cantidad de puestos ofrecidos
    - Cantidad de kilos que puede transportar

- **Funcionalidades**:
    - Crear un nuevo servicio
    - Actualizar el nombre de un servicio
    - Consultar la información vigente de un servicio

*Nota: Los productos pueden ser de pasajeros o de encomienda, sin mezclarse.*

### Módulo de Gestión de Clientes

Este módulo permite gestionar una base de datos de clientes.

- **Base de datos de clientes**:
    - Número de identificación (identificador único)
    - Nombre
    - Apellido
    - Dirección
    - Teléfono
    - Correo electrónico

- **Funcionalidades**:
    - Crear un nuevo cliente
    - Actualizar la dirección de un cliente
    - Consultar la información vigente de un cliente

### Módulo de Venta de Servicios

Este módulo permite vender servicios a clientes y gestionar ventas.

- **Base de datos de ventas**:
    - Número de factura
    - Identificación del cliente
    - Identificación del producto
    - Cantidad vendida

- **Funcionalidades**:
    - Vender servicios a un cliente
    - Quitar servicios si el cliente se arrepiente
    - imprimir el soporte de la venta.
    - Enviar la factura en un correo electrónico al cliente.

- **Impresión de soporte de venta**:
    - **Encabezado**:
        - Número de venta
    - **Datos de cliente**:
        - Nombre del cliente
        - Apellido del cliente
        - Dirección del cliente
        - Teléfono del cliente
    - **Datos del servicio**:
        - Nombre del servicio
        - Hora de salida (HH:MM:SS)
        - Cantidad
        - Precio unitario
        - Precio según la cantidad
    - **Pie final**:
        - Precio total

*Nota: No se puede ofrecer un servicio que combine puestos y peso.*

## Instalación y uso

1. Clona el repositorio: `git clone https://github.com/MatRodriguezPa/Sistema-Administracion-Transporte
2. Ejecuta la aplicación: `main.py`

---
*Desarrollado por Mateo Rodríguez Palacios(https://github.com/MatRodriguezPa)*
 
