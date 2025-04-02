-- ELIMINACIÓN DE REGISTROS
delete from contactos where cedula = 'V7654321';
delete from contactos;
truncate contactos;

-- CREAR TABLA CON ÍNDICE ÚNICO VÍA CONSOLA:
create table contactos1(
    cedula varchar(15),
    nombre varchar(80),
    apellido varchar(80),
    fechanac date,
    telefono varchar(20),
    correo varchar(60),
    unique(cedula)
);

INSERT INTO contactos1(cedula, nombre, apellido, fechanac, telefono, correo) VALUES
('V7654321', 'ANA','VASQUEZ' ,'1960-08-15' ,'+58 212 9876543' ,'av@gmail.com' ),
('V9654321', 'YOLANDA','TORTOZA' ,'1970-09-25' ,'+58 212 5876543' ,'yt@gmail.com');

create table contactos2(
    cedula varchar(15),
    nombre varchar(80),
    apellido varchar(80),
    fechanac date,
    telefono varchar(20),
    correo varchar(60),
    unique(cedula),
    unique(correo)
);


INSERT INTO contactos2(cedula, nombre, apellido, fechanac, telefono, correo) VALUES
('V7654321', 'ANA','VASQUEZ' ,'1960-08-15' ,'+58 212 9876543' ,'av@gmail.com' ),
('V9654321', 'YOLANDA','TORTOZA' ,'1970-09-25' ,'+58 212 5876543' ,'yt@gmail.com');

INSERT INTO contactos2(cedula, nombre, apellido, fechanac, telefono, correo) VALUES
('V7654322', 'ANA','BASTIDAS' ,'1969-09-25' ,'+58 212 7876543' ,'av@gmail.com' );

--pgadmin:
INSERT INTO public.contactos1(
	nombre, apellido, fechanac, telefono, correo, cedula)
	VALUES ('ANA','VASQUEZ' ,'1960-08-15' ,'+58 212 9876543' ,'av@gmail.com' , 'V7654321'),
('YOLANDA','TORTOZA' ,'1970-09-25' ,'+58 212 5876543' ,'yt@gmail.com', 'V9654321');

-- ASOCIACIÓN ENTRE TABLAS
-- SE TIENEN 2 TABLAS, PROVEEDORES Y PRODUCTOS, ESTA ÚLTIMA DEPENDE DE PROVEEDORES.
-- DEFINICIÓN DE PROVEEDORES:
CREATE TABLE PROVEEDORES(
    id serial,
    nombre varchar(30),
    direccion text,
    telefono varchar(20),
    correo varchar(60),
    primary key(id)
);
CREATE TABLE PRODUCTOS(
    id serial,
    proveedor_id integer,
    nombre varchar(30),
    precio numeric(13,2),
    existencia integer,
    primary key(id),
    foreign key(proveedor_id) references proveedores(id)
);

-- CARGA DE DATOS
INSERT INTO PROVEEDORES(nombre, direccion, telefono, correo)
VALUES
('GE','AV. LECUNA','+58 212 9876543','info@ge.com'),
('LG','AV. ROMULO GALLEGOS','+58 212 8876543','info@lg.com'),
('WHIRPOOL','AV. FCO. DE MIRANDA','+58 212 7876543','info@whirpool.com'),
('ELECTROLUX','AV. PPAL. DE LAS MERCEDES','+58 212 6876543','info@electrolux.com');

INSERT INTO PRODUCTOS(proveedor_id, nombre, precio, existencia)
VALUES
(1,'NEVERA',500.25,12),
(1,'LAVADORA',300.75,6),
(1,'SECADORA',500.50,8),
(1,'CONGELADOR',200.25,3),
(2,'AIRE ACONDICIONADO',600,3),
(2,'COCINA ELECTRICA',250,6),
(2,'COCINA A GAS',175,9),
(2,'NEVERA',480,7),
(3,'LAVADORA',500,2),
(3,'HORNO ELECTRICO',350,3),
(3,'MICRO ONDAS',150,6),
(3,'CONGELADOR',250,3),
(4,'NEVERA',490,7),
(4,'HORNO A GAS',250,6),
(4,'SECADORA',550,5),
(4,'LAVADORA',450,6);

-- RESTRICCIONES:
-- 1-) NO SE PUEDE BORRAR UN REGISTRO DE LA TABLA PROVEEDORES
--     SI, EXISTEN REGISTROS DEPENDIENTES EN LA TABLA PRODUCTOS.
--     POR EJEMPLO:
DELETE FROM PROVEEDORES WHERE ID = 1;
-- 2-) NO SE PUEDE CAMBIAR EL VALOR DEL CAMPO ID EN LA TABLA PROVEEDORES
--     DADO QUE EXISTEN VALORES DEPENDIENTES EN LA TABLA PRODUCTOS
--     POR EJEMPLO:
UPDATE PROVEEDORES SET ID = 11 WHERE ID = 1;
-- 3-) NO SE PUEDE INGREDAR UN REGISTRO EN PRODUCTOS, CUYO ID NO EXISTA EN 
--     LA TABLA PROVEEDORES
--     POR EJEMPLO:
INSERT INTO PRODUCTOS(proveedor_id, nombre, precio, existencia)
VALUES
(5,'NEVERA',500.25,12);










