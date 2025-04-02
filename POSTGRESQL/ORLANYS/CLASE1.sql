-- CREACIÒN DE BASES DE DATOS
create database bd_ic_orlanys;


--COMANDO psql


--CREAR TABLA VÌA CONSOLA;
create table contactos(
    cedula varchar(15),
    nombre varchar(80),
    apellido varchar(80),
    fechanac date,
    telefono varchar(20),
    correo varchar(60)
    );


--BORRAR TABLA;
drop table


--INGRESO DE REGISTROS
INSERT INTO contactos1(cedula,nombre,apellido,fechanac,telefono,correo) VALUES
('v7654321','ANA','VASQUEZ' ,'1690-08-15','+58 212 9876543','av@gmail.com'),
	('V18415213','YOLANDA','TORTOZA','1970-09-25','+58 212 25483','ABF@GMAIL.COM');


--CONSULTA DE REGISTROS
--TODOS LOS CAMPOS Y REGISTROS DE LA TABLA
SELECT *FROM contactos;
SELECT cedula, correo FROM  contactos;
SELECT cedula, correo FROM contactos WHERE nombre = 'ANA';



-ACTUALIZAICON DE REGISTROS
UPDATE contactos SET nombre = 'SUSANA';
--ACTUALIZACION DE REGISTROS CONDICIONADA
UPDATE contactos SET nomnbre = 'ANA' WHERE cedula = 'v7654321';
UPDATE contactos SET nombre = 'YOLANDA' WHERE CEDULA = 'V18415213';

