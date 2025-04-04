--ASOCACION ENTRE TABLAS CON ATRIBUTOS URDATE CASCADE DELETE CASCADE
--SE TIENEN DOS TABLAS, PROVEEDORES Y PRODUCTOS, ESTA ÙLTIMO DEPENDE DE PROVEEDORES.
--DEFINICION DE PROVEEDORES:
CREATE TABLE PROVEEDORES1(
    id serial,
    nombre varchar(30),
    direccion text,
    telefono varchar(20),
    correo varchar(60),
    primary key(id)
);
CREATE TABLE PRODUCTOS1(
  id serial,
  proveedor_id integer,
  nombre varchar(30),
  precio numeric(13,2),
  existencia integer,
  primary key(id),
  foreign key (proveedor_id) references PROVEEDORES1(id) on delete cascade on update cascade
);

--CARDA DE DATOS
INSERT into PROVEEDORES1(nombre, direccion,telefono,correo)
VALUES
('GE','AV. LECUNA','+58 212 9876543','info@ge.com'),
('LE','AV. ROMULO GALLEGOS','+58 212 8876543','info@lg.com'),
('WHIRPOOL','AV. FCO. DE MIRANDA','+58 212 7876543','info@whirpool.com'),
('ELECTROLUX','AV. PPAL DE LAS MERCEDES','+58 212 687526','info@electrolux.com');

INSERT INTO PRODUCTOS1(proveedor_id, nombre,precio, existencia)
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


  --AL EXISTIR DEPENDENCIA ENTRE LAS TABLAS LAS SIGUIENTES ACCIONES SE PUEDEN EFECTUAR:
-- 1-) SE PUEDE BORRAR UN REGISTRO DE LA TABLA PROVEEDORES1 SI EXISTEN REGISTROS DEPENDIENTES DE LA TABLA PRODUCTOS1 ESTOS TAMBIÈN SERAN BORRADOS.
-- POR EJEMPLO:
DELETE FROM PROVEEDORES1 WHERE ID = 1;
-- 2-) SE PUEDE CAMBIAR EL VALOR DEL CAMPO ID EN LA TABLA PROVEEDORES1
      GENERANDO LA ACTUALIZACION DE ESTE CAMPO EN LA TABLA PRODUCTOS1.
-- POR EJEMPLO:
UPDATE PROVEEDORES1 SET ID = 22 WHERE ID =2;

--CONSULTA COMBINADA ENTRE TABLAS

EMPLEANDO SIN ALIAS
SELECT  proveedores.nombre,
        proveedores.telefono,
        proveedores.correo,
        productos.nombre,
        productos.precio,
        productos.existencia
        FROM proveedores, productos
        WHERE productos.proveedor_id = proveedores.id;



EMPLEANDO ALIAS
SELECT  A.nombre as proveedor,
        A.telefono,
        A.correo,
        B.nombre as producto,
        B.precio,
        B.existencia
        FROM proveedores AS A, productos AS B
        WHERE B.proveedor_id = A.id;


--CREACION DE VISTAS A PARTIR DE LAS CONSULTAS ANTERIORES
CREATE VIEW VISTA_PROV_PROD AS
SELECT  A.nombre as proveedor,
        A.telefono,
        A.correo,
        B.nombre as producto,
        B.precio,
        B.existencia
        FROM proveedores AS A, productos AS B
        WHERE B.proveedor_id = A.id;


--LA VISTA QUE SE PRODUCE VA A TENER LA ESTRUCTURA DE UNA TABLA
--POR ENDE PUEDE EFECTUAR COMANDOS PROPIOS DE TABLAS SOBRE ESTA.
SELECT * FROM VISTA_PROV_PROD;

--ESTRUCTURA DE LA VISTA 
\d VISTA_PROV_PROD;

--VER LAS VISTAS CREADAS
\dv


--COLUMNAS CALCULADAS
--SON FUNCIONES QUE SE REALIZAN SOBRE (CAMPOS) DE TABLAS
SELECT SUM()
SELECT MIN()
SELECT MAX()
SELECT AVG()
SELECT COUNT()
--SUMATORIA
SELECT SUM(existencia) FROM VISTA_PROV_PROD;
SELECT SUM(existencia) AS TOTAL_EXISTENCIA FROM VISTA_PROV_PROD;
SELECT SUM(existencia) AS "TOTAL_EXISTENCIA" FROM VISTA_PROV_PROD;
--PROMEDIO
SELECT AVG(precio) FROM VISTA_PROV_PROD;
SELECT AVG(precio) AS PROMEDIO FROM VISTA_PROV_PROD;
SELECT ROUND(AVG(precio),2) FROM VISTA_PROV_PROD;
--MINIMO
SELECT MIN(PRECIO) FROM VISTA_PROV_PROD;
--MAXIMO
SELECT MAX(PRECIO) FROM VISTA_PROV_PROD;
--CONTAR
SELECT COUNT(*) FROM VISTA_PROV_PROD;


--FORMAS DE CONDICIONAMIENTO

SELECT * FROM VISTA_PROV_PROD WHERE proveedor = 'GE' AND PRECIO >=500;

--LISTA DE VALORES
SELECT proveedor, producto, precio FROM VISTA_PROV_PROD WHERE proveedor = 'GE' OR proveedor = 'LG';

--EQUIVALENTE DE LISTA DE VALORES
SELECT proveedor, producto, precio FROM VISTA_PROV_PROD WHERE proveedor IN ('GE','LG');

--RANGO DE VALORES
SELECT * FROM VISTA_PROV_PROD WHERE PRECIO >= 500 AND PRECIO <=1000;


--EQUIVALENTE DE RANGO DE VALORES
SELECT * FROM VISTA_PROV_PROD WHERE PRECIO BETWEEN 500 AND 1000;


--TABLAS DE VERDAD
--CONJUNCIÒN
--P   Q   =>  P AND Q
--V   V          V
--V   F          F
--F   V          F
--F   F          F

--DISYUNCIÒN
--P   Q   =>  P OR Q
--V   V          V
--V   F          F
--F   V          F
--F   F          F

--NEGACION
--P   =>  NOT P
--V   F
--F   V

--FORMAS DE CONDICIINAMIENTO

-- LISTA DE VALORES
SELECT proveedor, producto, precio FROM VISTA_PROV_PROD WHERE NOT (proveedor = 'GE' OR proveedor = 'LG');

--EQUIVALENTE DE LISTA DE VALORES
SELECT proveedor, producto, precio FROM VISTA_PROV_PROD WHERE proveedor NOT IN ('GE','LG');

--RANGO DE VALORES
SELECT * FROM VISTA_PROV_PROD WHERE NOT (PRECIO >= 500 AND PRECIO <=1000);

SELECT * FROM VISTA_PROV_PROD WHERE PRECIO NOT BETWEEN 500 AND 1000;



-- CONSULTA PROXIMNADA DEL CONTENIDO DE UN CAMPO
SELECT * FROM VISTA_PROV_PROD WHERE PRODUCTO LIKE '%COCINA%';


--DIEFRENCIAS ENTRE ESPACIOS EN BLANCO Y NULL

INSERT INTO CONTACTOS1 (CEDULA, NOMBRE, APELLIDO)
VALUES ('V123)', '', '');

SELECT * FROM CONTACTOS1;

SELECT * FROM CONTACTOS1 WHERE nombre = '';

SELECT * FROM CONTACTOS1 WHERE correo = '';



select count (*) FROM CONTACTOS1;

select count (CEDULA) FROM CONTACTOS1;

select count (NOMBRE) FROM CONTACTOS1;

select count (CORREO) FROM CONTACTOS1;




