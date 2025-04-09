insert into alumnos_asignaturas(alumnos_id, asignatura_id)
values(1,1);

-- CONSULTA PARA OBTENER LA INFORMACIÒN QUE VINCULE LAS 3 TABLAS
SELECT alumnos.nombre, 
       alumnos.apellido,
       asignaturas.nombre
       from alumnos, asignaturas, alumnos_asignaturas
       where alumnos_asignaturas.alumno_id = alumnos.id and 
             alumnos_asignaturas.asignatura_id = asignaturas.id;



create view ciew_alumnos_asignaturas as 
             select alumnos.nombre,
       alumnos.apellido,
       asignaturas.nombre as asignaturas
       from alumnos, asignaturas, alumnos_asignaturas
       where alumnos_asignaturas.alumnos_id = alumnos.id and 
             alumnos_asignaturas.asignaturas_id = asignaturas.id;

 ---ELIMINAR UNA VISTA
 DROP view_alumnos_asignaturas;


-- CREACION DE TABLAS
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

 INSERT into PROVEEDORES2(nombre, direccion,telefono,correo)
VALUES
('GE','AV. LECUNA','+58 212 9876543','info@ge.com'),
('LE','AV. ROMULO GALLEGOS','+58 212 8876543','info@lg.com'),
('WHIRPOOL','AV. FCO. DE MIRANDA','+58 212 7876543','info@whirpool.com'),
('ELECTROLUX','AV. PPAL DE LAS MERCEDES','+58 212 687526','info@electrolux.com');

INSERT INTO PRODUCTOS2(proveedor_id, nombre,precio, existencia)
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

 --EJEMPLO DE INNER JOIN
 SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        INNER JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.proveedor_id;

--GUARDAR COMO VISTA
CREATE VIEW VIEW_INNER_JOIN_PROV_PROC AS
SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        INNER JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.
        proveedor_id;

INSERT into PROVEEDORES2(nombre, direccion,telefono,correo)
VALUES
('HAIER','AV. PPAL EL VALE','+58 212 6825147','info@haier.com'),
('DAMASCO','AV. SAN MARTIN','+58 212 6825569','info@damasco.com');

--EJEMPLO DE LEFT JOIN
SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        LEFT JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.proveedor_id;


CREATE VIEW VIEW_LEFT_JOIN_PROV_PROC AS
SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        LEFT JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.proveedor_id;


INSERT INTO PRODUCTOS2(proveedor_id, nombre,precio, existencia)
  VALUES
  (7,'tostiarepa',100.75,12),
  (7,'aire acondicionado',600.25,4),
  (7,'horno a gas',300.50,6),
  (7,'horno electrico',450.25,7);


--EJEMPLO DE RIGHY JOIN
SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        RIGHT JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.proveedor_id;


CREATE VIEW VIEW_RIGHT_JOIN_PROV_PROC AS
SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        RIGHT JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.proveedor_id;


--EJEMPLO DE FULL JOIN
SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        FULL JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.proveedor_id;


CREATE VIEW VIEW_FULL_JOIN_PROV_PROC AS
SELECT proveedores2.nombre as proveedor,
        proveedores2.telefono,
        proveedores2.correo,
        productos2.nombre as producto,
        productos2.precio,
        productos2.existencia
        FROM proveedores2
        FULL JOIN PRODUCTOS2 ON PROVEEDORES2.id = productos2.proveedor_id;


