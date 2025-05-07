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
instruccion.execute("select *from proveedores;")

# Mostar el resultado en pantalla
for resultado in instruccion:
    print(resultado)

# Cerrar la conexiòn a la base de datos
instruccion.close()
conexion.close()

