-- crear otra tabla con contactos con clave unica indice unico via consola 
create table contactos1 (
    cedula varchar(15),
    nombre varchar(80),
    apellido varchar(80),
    fechanac date,
    telefono varchar(20),
    correo varchar(60),
    unique (cedula)
);

INSERT INTO contactos2 (cedula, nombre, apellido, fechanac, telefono, correo) VALUES
('V7654321', 'ANA','VASQUEZ' ,'1960-08-15' ,'+58 212 9876543' ,'av@gmail.com' ),
('V9654321', 'YOLANDA','TORTOZA' ,'1970-09-25' ,'+58 212 5876543' ,'yt@gmail.com');
create table contactos2 (
    cedula varchar(15),
    nombre varchar(80),
    apellido varchar(80),
    fechanac date,
    telefono varchar(20),
    correo varchar(60),
    unique (cedula),
    UNIQUE (correo)
);
INSERT INTO contactos2 (cedula, nombre, apellido, fechanac, telefono, correo) VALUES
('V7654321', 'ANA','VASQUEZ' ,'1960-08-15' ,'+58 212 9876543' ,'av@gmail.com' ),
('V9654321', 'YOLANDA','TORTOZA' ,'1970-09-25' ,'+58 212 5876543' ,'yt@gmail.com');
  INSERT INTO contactos2 (cedula, nombre, apellido, fechanac, telefono, correo) VALUES
('V7654331', 'ANA','BASTIDAS' ,'1960-08-13' ,'+58 212 9876533' ,'av@gmail.com' );
--contactos1
INSERT INTO public.contactos1(
	nombre, apellido, fechanac, telefono, correo, cedula)
	VALUES ('ANA','VASQUEZ' ,'1960-08-15' ,'+58 212 9876543' ,'av@gmail.com', 'V7654321'),
('YOLANDA','TORTOZA' ,'1970-09-25' ,'+58 212 5876543' ,'yt@gmail.com', 'V9654321');

--AOCIACION ENTRE TABLAS 
-- SE TIENE DOS TABLAS PROVEEDORES Y PRODUCTOS
--DEF DE PROVEEDORES
CREATE TABLE PROVEEDORES( 
  id serial,
  nombre varchar(30),
  direccion text,
  telefono varchar(30),
  correo varchar (60),
  primary key (id)
);
CREATE TABLE PRODUCTOS(
  id serial,
  proveedor_id integer,
  nombre varchar(30),
  precio numeric(13,2),
  existencia integer,
  primary key (id),
  foreign key (proveedor_id) references PROVEEDORES(id)
);
--CARGA DE DATOS
INSERT INTO PROVEEDORES (
  nombre, direccion, telefono, correo)
  VALUES
  ('GE','AV LECUNA','+582129999999','info@ge.com'),
  ('LG','AV ROMULO','+581111111','info@lg.com'),
  ('WHIRPOOL','las mercedes','+582123333333','info@whirpool.com'),
  ('ELECTROLUX','las mercedes','+582123333334','info@EL.com');

--  PRODUCTOS
INSERT INTO PRODUCTOS (proveedor_id, nombre, precio, existencia)
  VALUES
 (1, 'NEVERA',500.25,12),
 (1,'LAVADORA',300.75,6),
 (1,'SECADORA',500.50,8),
 (1,'CONGELADOR',200.25,3),
 (2,'AA',600,3),
 (2,'COCINA ELECTRICA',250,6),
 (2,'COCINA A GAS',175,9),
 (2,'NEVERA',200.25,3),
 (3, 'LAVADORA',500,2),
 (3,'HORNO ELECTRICO',350,3),
 (3,'MICRO ONDAS',150,6),
 (3,'CONGELADOR',250,3),
 (4, 'NEVERA',490,7),
 (4,'HORNO A GAS',250,6),
 (4,'SECADORA',550,5),
 (4,'LAVADORA',450,6
);

--RESTRICCIONES
-- 1) NO SE PUEDE BORRAR UN REGISTRO DE LA TABLA PROVEEDORES SI EXISTEN REGISTROS DEPENDIENTES DE LA TABLA PRODUCTOS 
--POR EJEMPLO 
DELETE FROM PROVEEDORES WHERE id = 1;
--2) NO SE PUEDE CAMBIAR EL VALOR DEL CAMPO ID EN LA TABLA PROVEEDORES DADO QUE EXISTEN VALORES DEPENDIENTES EN LA TABLA PRODUCTOS 
--EJEM
UPDATE PROVEEDORES SET id = 11 WHERE id =1;
--3) NO SE PUEDE INGRESAR UN REGISTRO EN PRODUCTOS CUYO ID NO EXISTA EN PROVEEDORES 
INSERT INTO PRODUCTOS (proveedor_id, nombre, precio, existencia)
  VALUES
 (5, 'NEVERA',500.25,12);