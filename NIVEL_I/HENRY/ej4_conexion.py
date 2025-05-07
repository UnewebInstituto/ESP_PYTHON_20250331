# Se importa libería que fue cargada en el entorno virtual
import psycopg2

# Establecer conexión a la base de datos
conexion = psycopg2.connect(
    dbname="bd_ic_henry",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)

# Se crea el cursor para ejecutar instrucciones
instruccion = conexion.cursor()

# Ejecucion de instrucción de prueba
instruccion.execute("SELECT version();")

# Mostrar el resultado en pantalla
print(instruccion.fetchone())

# Cerrar conexion a la base de datos
instruccion.close()
conexion.close()
