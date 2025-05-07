#se importa libreria que fue cargada en el entorno virtual
import psycopg2

#establecer conexion a la base de datos

conexion = psycopg2.connect(
  dbname="bd_ic_dannysa",
  user="postgres",
  password="123456",
  host="localhost",
  port="5432"
)
#se crea el cursor para ejecutar instrucciones
instruccion = conexion.cursor()
#ejecutar consultas de prueba
instruccion.execute("SELECT version();")
#mostrar el resultado en pantalla
print(instruccion.fetchone())
#cerrar conexion a la base de datos
instruccion.close()
conexion.close()


