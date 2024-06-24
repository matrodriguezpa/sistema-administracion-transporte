# Sistema de administración de transporte - La nacional

Este proyecto es una aplicación para gestionar los servicios ofrecidos y clientes, así como para la venta de servicios a clientes y la impresión de facturas. 

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

- **Gestión de ventas**:
    - Número de factura
    - Identificación del cliente
    - Identificación del producto
    - Cantidad vendida

- **Funcionalidades**:
    - Vender servicios a un cliente
    - Quitar servicios si el cliente se arrepiente

### Módulo de Impresión de Factura

Este módulo permite imprimir el soporte de la venta.

- **Impresión de soporte de venta**:
    - **Encabezado**:
        - Número de venta
        - Nombre del cliente
        - Apellido del cliente
        - Dirección del cliente
        - Teléfono del cliente
    - **Cuerpo de la factura**:
        - Nombre del producto
        - Hora de salida (HH:MM:SS)
        - Cantidad
        - Precio unitario
        - Precio según la cantidad
    - **Pie final**:
        - Precio total

*Nota: No se puede ofrecer un servicio que combine puestos y peso.*

### Funcionalidad Adicional

- Enviar un correo electrónico al cliente (si el desarrollo lo permite).

## Instalación

1. Clona el repositorio: `git clone https://github.com/tu_usuario/gestion-servicios-clientes.git`
2. Navega al directorio del proyecto: `cd gestion-servicios-clientes`

## Uso

1. Ejecuta la aplicación: `npm start` o `python main.py`
2. Accede a la aplicación en tu navegador web en `http://localhost:3000` o el puerto configurado.

## Contribución

1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b mi-rama-de-caracteristica`
3. Realiza tus cambios y haz commits: `git commit -am 'Agrega nueva característica'`
4. Envía tus cambios a tu fork: `git push origin mi-rama-de-caracteristica`
5. Crea un Pull Request en el repositorio original.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

---

*Desarrollado por Mateo Rodríguez Palacios(https://github.com/MatRodriguezPa)*
 
