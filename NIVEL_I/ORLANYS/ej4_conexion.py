# Se importa libreria que fue cargada en el entorno virtual
import psycopg2

# Establecer conexiòn a la base de datos
conexion = psycopg2.connect(
  dbname="bd_ic_orlanys",
  user="postgres",
  password="123456",
  host="localhost",
  port="5432"
)

# Se crea el cursor para ejcutar comandos para ejecutar instrucciones
instruccion = conexion.cursor()

# Ejecuciòn de instrucciòn de prueba
instruccion.execute("select version();")

# Mostar el resultado en pantalla
print(instruccion.fetchone())

# Cerrar la conexiòn a la base de datos
instruccion.close()
conexion.close()

