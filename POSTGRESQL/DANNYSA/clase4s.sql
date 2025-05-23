ORDENAMIENTO DE DATOS
ASCENDENTE 
SELECT * FROM VISTA_PROV_PROD
ORDER BY PRODUCTO;

SELECT * FROM VISTA_PROV_PROD
ORDER BY PRODUCTO DESC;

--
COMBINACION DE ORDENAMIENTO
SELECT * FROM VISTA_PROV_PROD
ORDER BY PRODUCTO DESC, PRECIO ASC;

AGRUPAMIENTO 
SE PUEDEN EMPLEAR DOS CLAUSULAS 
--1) DISTINCT
--2) GROUP BY
--CASO 1
SELECT DISTINCT PRODUCTO FROM VISTA_PROV_PROD;
--CASO 2
SELECT PRODUCTO FROM VISTA_PROV_PROD
GROUP BY PRODUCTO;
-- EN AMBOS CASOS PERMITE EL ORDENAMIENTO 
 SELECT DISTINCT PRODUCTO FROM VISTA_PROV_PROD ORDER BY PRODUCTO;
 SELECT PRODUCTO FROM VISTA_PROV_PROD GROUP BY PRODUCTO ORDER BY PRODUCTO;
 SELECT PRODUCTO FROM VISTA_PROV_PROD GROUP BY PRODUCTO ORDER BY PRODUCTO DESC; 

 --ejemplo clase 
 SELECT MAX(PRECIO) FROM VISTA_PROV_PROD WHERE PROVEEDOR = 'LG';
 SELECT MIN(PRECIO) FROM VISTA_PROV_PROD WHERE PROVEEDOR = 'LG';
 SELECT AVG(PRECIO) FROM VISTA_PROV_PROD WHERE PROVEEDOR = 'LG';
 SELECT SUM(PRECIO) FROM VISTA_PROV_PROD WHERE PROVEEDOR = 'LG';

 --UTILIZANDO AGRUPAMIENTO 
 SELECT PROVEEDOR, MAX(PRECIO), MIN(PRECIO), AVG(PRECIO), SUM(EXISTENCIA) 
 FROM VISTA_PROV_PROD
 GROUP BY PROVEEDOR;
 -- UTILIZANDO AGRUPAMIENTO Y APLICANDO ALIAS 
 SELECT PROVEEDOR AS PROVEEDOR, MAX(PRECIO) AS "PRECIO MAXIMO", MIN(PRECIO) AS "PRECIO MINIMO", ROUND(AVG(PRECIO),2) AS "PROMEDIO", SUM(PRECIO) AS "CANTIDAD DE EXISTENCIA" FROM VISTA_PROV_PROD 
 GROUP BY PROVEEDOR, ORDER BY PROVEEDOR;
--OTRA FORMA 
SELECT PROVEEDOR AS proveedor, MAX(PRECIO) AS PRECIO_MAXIMO, MIN(PRECIO) AS PRECIO_MINIMO, ROUND(AVG(PRECIO),2) AS PROMEDIO, SUM(PRECIO) AS CANTIDAD_EXISTENCIA FROM VISTA_PROV_PROD 
 GROUP BY PROVEEDOR, ORDER BY PROVEEDOR;

 pg_dump -U nombre_usuario -W -F c -b -v -f "/ruta/del/backup/mi_backup.dump" nombre_base_datos
pg_dump -U postgres -W -F c -b -v -f "backup_20250407.dump" mi_base_datos
pg_dump -U postgres -W -F c -b -v -f "backup_20250407.dump" bd_ic_dannysa;
"C:\Program Files\PostgreSQL\16\bin\pg_dump" -U postgres -W -F c -b -v -f "backup_20250407.dump" bd_ic_dannysa
C:\Program Files\PostgreSQL\16\bin

--RESTORE COMANDO PARA LA RECUPERACION 

"C:\Program Files\PostgreSQL\16\bin\pg_restore" -U postgres -W -d bd_ic_dannysa_r -v "backup_20250407.dump"
"C:\Program Files\PostgreSQL\16\bin\pg_restore" -U postgres -W -d bd_ic_dannysa_r -v "backup_20250409.dump"
ABRIR UN TERMINAL DE SISTEMA OPERATIVO MS-DOS

--ASOCIACION DE MUCHOS A MUCHOS 
CREATE TABLE alumnos(
  id serial,
  nombre varchar(80),
  apellido varchar(80),
  primary key (id)
);
CREATE TABLE asignaturas(
  id serial,
  nombre varchar(80),
  descripcion text,
  primary key (id)
);
CREATE TABLE alumnos_asignaturas(
  alumno_id integer,
  asignatura_id integer,
  primary key (alumno_id,asignatura_id),
  foreign key (alumno_id) references alumnos(id) on delete cascade on update cascade,
  foreign key (asignatura_id) references asignaturas(id) on delete cascade on update cascade
);
"C:\Program Files\PostgreSQL\16\bin\pg_dump" -U postgres -W -F c -b -v -f "backup_20250409.dump" bd_ic_dannysa