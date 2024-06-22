BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Servicios" (
	"codigoServicio"	integer NOT NULL,
	"nombre"	text NOT NULL,
	"origen"	text NOT NULL,
	"destino"	text NOT NULL,
	"precioVenta"	integer NOT NULL,
	"horaSalida"	date NOT NULL,
	"cantidadMaxPuestos"	integer NOT NULL,
	"cantidadMaxKilos"	integer NOT NULL,
	PRIMARY KEY("codigoServicio")
);
CREATE TABLE IF NOT EXISTS "Clientes" (
	"noIdentificacionCliente"	integer NOT NULL,
	"nombre"	text NOT NULL,
	"apellido"	text NOT NULL,
	"direccion"	text NOT NULL,
	"telefono"	integer NOT NULL,
	"correoElectronico"	text NOT NULL,
	PRIMARY KEY("noIdentificacionCliente")
);
CREATE TABLE IF NOT EXISTS "Ventas" (
	"noFactura"	integer NOT NULL,
	"noIdentificacionCliente"	text NOT NULL,
	"codigoServicio"	integer NOT NULL,
	"cantidadVendida"	integer NOT NULL,
	PRIMARY KEY("noFactura")
);
INSERT INTO "Servicios" VALUES (1312,'REMESA','CHIA','COTA',100,'1900-01-01 12:15:20',10,200);
COMMIT;
