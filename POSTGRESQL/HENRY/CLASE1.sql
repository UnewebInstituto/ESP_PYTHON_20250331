-- CREACIÓN DE BASES DE DATOS
create database bd_ic_henry;
create database bd_ic_dannysa;
create database bd_ic_orlanys;

-- COMANDO psql
\c bd_ic_henry;
\c bd_ic_dannysa;
\c bd_ic_orlanys;

-- CREAR TABLA VÍA CONSOLA:
create table contactos(
    cedula varchar(15),
    nombre varchar(80),
    apellido varchar(80),
    fechanac date,
    telefono varchar(20),
    correo varchar(60)
);

-- BORRAR TABLA
drop table prueba;

-- INGRESO DE REGISTROS
INSERT INTO contactos(cedula, nombre, apellido, fechanac, telefono, correo) VALUES
('V7654321', 'ANA','VASQUEZ' ,'1960-08-15' ,'+58 212 9876543' ,'av@gmail.com' ),
('V9654321', 'YOLANDA','TORTOZA' ,'1970-09-25' ,'+58 212 5876543' ,'yt@gmail.com');

-- CONSULTA DE REGISTROS
-- TODOS LOS CAMPOS Y REGISTROS DE LA TABLA
SELECT * FROM contactos;
SELECT cedula, correo FROM contactos;
SELECT cedula, correo FROM contactos WHERE nombre = 'ANA';

-- ACTUALIZACIÓN DE REGISTROS
UPDATE contactos SET nombre = 'SUSANA';
-- ACTUALIZACIÓN DE REGISTROS CONDICIONADA
UPDATE contactos SET nombre = 'ANA' WHERE cedula = 'V7654321';
UPDATE contactos SET nombre = 'YOLANDA' WHERE cedula = 'V9654321';

