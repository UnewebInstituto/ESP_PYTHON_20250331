--ELINICACION DE REGISTROS





--CREAR TABLA CON ÌNDICE ÙNICO VÌA CONSOLA;
create table contactos1(
    cedula varchar(15),
    nombre varchar(80),
    apellido varchar(80),
    fechanac date,
    telefono varchar(20),
    correo varchar(60),
    unique (cedula)
    );

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


INSERT INTO contactos2(cedula,nombre,apellido,fechanac,telefono,correo) VALUES
('v7654321','ANA','VASQUEZ' ,'1690-08-15','+58 212 9876543','av@gmail.com'),
	('V18415213','YOLANDA','TORTOZA','1970-09-25','+58 212 25483','ABF@GMAIL.COM');

  INSERT INTO contactos2(cedula,nombre,apellido,fechanac,telefono,correo) VALUES
('v7654321','ANA','VASQUEZ' ,'1690-08-15','+58 212 9876543','av@gmail.com'),
	('V18415213','YOLANDA','TORTOZA','1970-09-25','+58 212 25483','ABF@GMAIL.COM');


INSERT INTO public.contactos4(
	nombre, apellido, fechanac, telefono, correo, cedula)
	VALUES ('ANA','VASQUEZ','1690-08-15','+58 212 9876543','av@gmail.com','v7654321'),
('YOLANDA','TORTOZA','1970-09-25','+58 212 25483','ABF@GMAIL.COM','V18415213');

--ASOCACION ENTRE TABLAS
--SE TIENEN DOS TABLAS, PROVEEDORES Y PRODUCTOS, ESTA ÙLTIMO DEPENDE DE PROVEEDORES.
--DEFINICION DE PROVEEDORES:
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
  foreign key (proveedor_id) references PROVEEDORES(id)
);

--CARGA DE DATOS
INSERT into PROVEEDORES(nombre, direccion,telefono,correo)
VALUES
('GE','AV. LECUNA','+58 212 9876543','info@ge.com'),
('LE','AV. ROMULO GALLEGOS','+58 212 8876543','info@lg.com'),
('WHIRPOOL','AV. FCO. DE MIRANDA','+58 212 7876543','info@whirpool.com'),
('ELECTROLUX','AV. PPAL DE LAS MERCEDES','+58 212 687526','info@electrolux.com');

INSERT INTO PRODUCTOS(proveedor_id, nombre,precio, existencia)
  VALUES
  (1,'nevera',500.25,12),
  (1,'lavadora',300.75,6),
  (1,'secadora',500.50,8),
  (1,'congelador',200.25,3),
  (2,'aire acondicionado',600,3),
  (2,'cocina',250,6),
  (2,'cocina a gas',175,9),
  (2,'nevera',480,7),
  (3, 'lavadora',500,2),
  (3,'horno electico',350,3),
  (3,'micro ondas',150,6),
  (3,'congelador',250,3),
  (4, 'nevera',490,7),
  (4,'horno a gas',250,6),
  (4,'secadora',550,5),
  (4,'lavadora',450,6);


--RESTRICCIONES:
-- 1-) NO SE PUEDE BORRAR UN REGISTRO DE LA TABLA PROVEEDORES SI EXISTEN REGISTROS DEPENDIENTES DE LA TABLA PRODUCTOS.
-- POR EJEMPLO:
DELETE FROM PROVEEDORES WHERE ID = 1;
-- 2-) NO SE PUEDE CAMBIAR EL VALOR DEL CAMPO ID EN LA TABLA PROVEEDORES
      DADO QUE EXISTEN VALORES DEPENDIENTES EN LA TABLA PRODUCTOS.
-- POR EJEMPLO:
UPDATE PROVEEDORES SET ID = 11 WHERE ID =1;
-- 3-) NO SE PUEDE INGRESAR UN REGISTRO EN PRODUCTOS CUYO ID NO EXISTA EN LA TABLA PROVEEDORES.
-- POR EJEMPLO:
INSERT INTO PRODUCTOS(proveedor_id, nombre,precio, existencia)
  VALUES
  (5,'nevera',500.25,12);


