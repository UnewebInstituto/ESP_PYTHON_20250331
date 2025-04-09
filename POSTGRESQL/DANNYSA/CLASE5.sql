--CASO DE ENTRADA DESDE ARCHIVO PLANO
COPY alumnos FROM 'C:/ESP_PYTHON_20250331/POSTGRESQL/DANNYSA/CLASE5/alumnos.txt' DELIMITER';'CSV;

COPY asignaturas FROM 'C:/ESP_PYTHON_20250331/POSTGRESQL/DANNYSA/CLASE5/asignaturas.txt' DELIMITER';'CSV;

--CASO SALIDA DESDE TABLA A ARCHIVO PLANO 
COPY alumnos TO 'C:/ESP_PYTHON_20250331/POSTGRESQL/DANNYSA/CLASE5/alumnos_salida.txt' DELIMITER ';';

COPY asignaturas TO 'C:/ESP_PYTHON_20250331/POSTGRESQL/DANNYSA/CLASE5/asinaturas_salida.txt' DELIMITER ';';
COPY alumnos_asignaturas FROM 'C:/ESP_PYTHON_20250331/POSTGRESQL/DANNYSA/CLASE5/alumnos_asignaturas.txt' DELIMITER ';' CSV;

insert into alumnos_asignaturas(alumno_id,  asignatura_id) values (1,1);

--CONSULTA DE LAS TRES TABLAS OBTENER INFO DE LAS 3 TABLAS
select alumnos.nombre, 
alumnos.apellido, 
asignaturas.nombre
from alumnos, asignaturas, alumnos_asignaturas
where alumnos_asignaturas.alumno_id = alumnos.id and 
alumnos_asignaturas.asignatura_id = asignaturas.id; 

--VISTA
create view view_alumnos_asignaturas as 
select alumnos.nombre, 
alumnos.apellido, 
asignaturas.nombre as asignatura
from alumnos, asignaturas, alumnos_asignaturas
where alumnos_asignaturas.alumno_id = alumnos.id and 
alumnos_asignaturas.asignatura_id = asignaturas.id; 

DROP VIEW view_alumnos_asignaturas;

--inner join
CREATE TABLE PROVEEDORES2(
    id serial,
    nombre varchar(30),
    direccion text,
    telefono varchar(20),
    correo varchar(60),
    primary key(id)
);
CREATE TABLE PRODUCTOS2(
    id serial,
    proveedor_id integer,
    nombre varchar(30),
    precio numeric(13,2),
    existencia integer,
    primary key(id)
);

CREATE TABLE PRODUCTOS2(
    id serial,
    proveedor_id integer,
    nombre varchar(30),
    precio numeric(13,2),
    existencia integer,
    primary key(id)
);

INSERT INTO PROVEEDORES2(nombre, direccion, telefono, correo)
VALUES
('GE','AV. LECUNA','+58 212 9876543','info@ge.com'),
('LG','AV. ROMULO GALLEGOS','+58 212 8876543','info@lg.com'),
('WHIRPOOL','AV. FCO. DE MIRANDA','+58 212 7876543','info@whirpool.com'),
('ELECTROLUX','AV. PPAL. DE LAS MERCEDES','+58 212 6876543','info@electrolux.com');

INSERT INTO PRODUCTOS2(proveedor_id, nombre, precio, existencia)
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

SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       from proveedores2
       inner join productos2
       on proveedores2.id = productos2.proveedor_id;

-- guardar como vista 
create view view_inner_join_prov_prod as 
   SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       from proveedores2
       inner join productos2
       on proveedores2.id = productos2.proveedor_id;    

  INSERT INTO PROVEEDORES2(nombre, direccion, telefono, correo)
VALUES
('GE','AV. LECUNA','+58 212 9876543','info@ge.com'),
('LG','AV. ROMULO GALLEGOS','+58 212 8876543','info@lg.com'),
('WHIRPOOL','AV. FCO. DE MIRANDA','+58 212 7876543','info@whirpool.com'),
('ELECTROLUX','AV. PPAL. DE LAS MERCEDES','+58 212 6876543','info@electrolux.com'),
('HAIER','AV. PPAL. VALLE','+58 212 6876544','info@HAIER.com'),
('DAMASCO','AV. PPAL. CATIA','+58 212 6876544','info@DAMASCO.com')
;

INSERT INTO PRODUCTOS2(proveedor_id, nombre, precio, existencia)
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
--left join
create view view_inner_join_prov_prod as 
   SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       from proveedores2
       left join productos2
       on proveedores2.id = productos2.proveedor_id;  

 create view view_left_join_prov_prod as 
   SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       from proveedores2
       left join productos2
       on proveedores2.id = productos2.proveedor_id; 

--RIGHT JOIN 
INSERT INTO PRODUCTOS2(proveedor_id, nombre, precio, existencia)
VALUES
(7,'TOSTIAREPA',100.25,12),
(7,'AA',600.25,4),
(7,'HORNO A GAS',300.50,6),
(7,'HORNO ELECTRICO',400.25,7);   
SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       FROM proveedores2 
       RIGHT JOIN productos2 ON proveedores2.id = productos2.proveedor_id;      

       CREATE view view_right_join_prov_prod as
SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       FROM proveedores2 
       LEFT JOIN productos2 ON proveedores2.id = productos2.proveedor_id;

       select * from view_right_join_prov_prod;

SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       FROM proveedores2 
       FULL JOIN productos2 ON proveedores2.id = productos2.proveedor_id;

create view view_full_join_prov_prod as 
SELECT proveedores2.nombre as proveedor,
       proveedores2.telefono,
       proveedores2.correo,
       productos2.nombre as producto,
       productos2.precio,
       productos2.existencia 
       FROM proveedores2 
       FULL JOIN productos2 ON proveedores2.id = productos2.proveedor_id;     
       
         