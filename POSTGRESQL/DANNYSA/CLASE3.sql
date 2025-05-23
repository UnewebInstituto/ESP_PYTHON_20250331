--


CREATE TABLE PRODUCTOS1(
  id serial,
  proveedor_id integer,
  nombre varchar(30),
  precio numeric(13,2),
  existencia integer,
  primary key (id),
  foreign key (proveedor_id) references PROVEEDORES1(id) on delete cascade on update cascade
);
INSERT INTO PROVEEDORES1 (
  nombre, direccion, telefono, correo)
  VALUES
  ('GE','AV LECUNA','+582129999999','info@ge.com'),
  ('LG','AV ROMULO','+581111111','info@lg.com'),
  ('WHIRPOOL','las mercedes','+582123333333','info@whirpool.com'),
  ('ELECTROLUX','las mercedes','+582123333334','info@EL.com');

--  PRODUCTOS
INSERT INTO PRODUCTOS1 (proveedor_id, nombre, precio, existencia)
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
-- ELIMINAR EN CASCADA 
--RESTRICCIONES
-- 1) SI SE PUEDE BORRAR UN REGISTRO DE LA TABLA PROVEEDORES1 SI EXISTEN REGISTROS DEPENDIENTES DE LA TABLA PRODUCTOS 
--POR EJEMPLO 
DELETE FROM PROVEEDORES1 WHERE id = 1;
--2) SI SE PUEDE CAMBIAR EL VALOR DEL CAMPO ID EN LA TABLA PROVEEDORES1 DADO QUE EXISTEN VALORES DEPENDIENTES EN LA TABLA PRODUCTOS1 
--EJEM
UPDATE PROVEEDORES1 SET id = 22 WHERE id =2;
--3) NO SE PUEDE INGRESAR UN REGISTRO EN PRODUCTOS CUYO ID NO EXISTA EN PROVEEDORES1 
INSERT INTO PRODUCTOS1 (proveedor_id, nombre, precio, existencia)
  VALUES
 (5, 'NEVERA',500.25,12);
 -- AHORA COMO HAY DEPENDENCIA AL EXISTIR DEPENDENCIA ENTRE LAS TABLAS LAS ACCIONES ANTERIORES 1 2 SE PUEDEN EFECTUAR EL 3 NO 
 --CONSULTA COMBINADA ENTRE TABLAS
 --EMPLEANDO ALIAS A PROVEEDORES B PRODUCTOS
 SELECT A.nombre as proveedor, A.telefono, A.correo, B.nombre as producto, B.precio, B.existencia
 FROM PROVEEDORES1 as A, PRODUCTOS1 as B
 WHERE B.proveedor_id = A.id;

 --CREACION DE VISTA A PARTIR DE LAS CONSULTAS ANTERIORES 
  CREATE VIEW VISTA_PROVEEDOR_PRODUCTO as 
  SELECT A.nombre as proveedor, A.telefono, A.correo, B.nombre as producto, B.precio, B.existencia
 FROM PROVEEDORES1 as A, PRODUCTOS1 as B
 WHERE B.proveedor_id = A.id;
-- LA VISTA QUE SE PRODUCE VA A TENER LA ESTRUCTURA DE UNA TABLA POR ENDE PUEDE EFECTUAR COMANDOS PROPIOS DE TABLAS SOBRE ESTA 
SELECT * FROM VISTA_PROVEEDOR_PRODUCTO;
--ESTRUCTURA DE LA VISTA
\dv VISTA_PROVEEDOR_PRODUCTO;
--VER VISTAS CREDAS 
\dv
--COLUMNAS CALCULADAS 
SELECT SUM()
SELECT MIN()
SELECT MAX()
--PROMEDIO
SELECT AVG()
SELECT SUM(existencia) as TOTAL_EXISTENCIA FROM VISTA_PROVEEDOR_PRODUCTO;
SELECT SUM(existencia) as "TOTAL EXISTENCIA" FROM VISTA_PROVEEDOR_PRODUCTO;
SELECT AVG(precio) FROM VISTA_PROVEEDOR_PRODUCTO;
SELECT AVG(precio) as PROMEDIO FROM VISTA_PROVEEDOR_PRODUCTO;
SELECT ROUND (AVG(precio),2) as PROMEDIO FROM VISTA_PROVEEDOR_PRODUCTO; 
SELECT MAX(precio) FROM VISTA_PROVEEDOR_PRODUCTO;
SELECT COUNT(*) FROM VISTA_PROVEEDOR_PRODUCTO;

--FORMAS DE CONDICIONAMIENTO
SELECT * FROM VISTA_PROVEEDOR_PRODUCTO
WHERE proveedor= 'GE' AND precio>=500;
--LISTA DE VALORES
SELECT producto, precio, proveedor
FROM VISTA_PROVEEDOR_PRODUCTO
WHERE proveedor= 'GE' OR proveedor = 'LG';
--EL EQUIVALENTE
SELECT producto, precio, proveedor
FROM VISTA_PROVEEDOR_PRODUCTO
WHERE proveedor IN ('GE','LG');
--RANGO DE VALORES
SELECT * FROM VISTA_PROVEEDOR_PRODUCTO
WHERE precio>= 500 AND precio<=1000;
--equivalente rango valores
SELECT * FROM VISTA_PROVEEDOR_PRODUCTO
WHERE precio BETWEEN 500 AND 1000;
--NEGACION DE LO ANTERIOR (TABLAS DE VERDAD)
--CONJUNCION
V V V
V F F
F V F
F F F
--DISYUNCION
V V V
F V V 
V F V
F F F
--NEGACION
V F 
F V 

SELECT * FROM VISTA_PROVEEDOR_PRODUCTO
WHERE NOT (proveedor= 'GE' AND precio>=500);
SELECT producto, precio, proveedor
FROM VISTA_PROVEEDOR_PRODUCTO
WHERE NOT ( proveedor= 'GE' OR proveedor = 'LG');
SELECT producto, precio, proveedor
FROM VISTA_PROVEEDOR_PRODUCTO
WHERE proveedor NOT IN ('GE','LG');
SELECT * FROM VISTA_PROVEEDOR_PRODUCTO
WHERE NOT (precio>= 500 AND precio<=1000);
SELECT * FROM VISTA_PROVEEDOR_PRODUCTO
WHERE precio NOT BETWEEN 500 AND 1000;
--CONSULTA APROXIMADA DEL CONTENIDO DE UN CAMPO
SELECT * FROM VISTA_PROVEEDOR_PRODUCTO
WHERE producto LIKE '%COCINA%';
--DIFERENCIA ENTRE ESPACIO EN BLANCO Y NULO
SELECT * FROM contactos1;
insert into CONTACTOS1 (cedula, nombre, apellido)
VALUES ('V123','','');
SELECT * FROM contactos1;
SELECT * FROM contactos1;
SELECT * FROM CONTACTOS1 WHERE nombre = '':
SELECT * FROM CONTACTOS1 WHERE correo IS NULL;
SELECT COUNT (*) FROM PROVEEDORES1;
SELECT COUNT (id) FROM PROVEEDORES1;
