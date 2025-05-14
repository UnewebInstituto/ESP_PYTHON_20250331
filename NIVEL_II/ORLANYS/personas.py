# Definición de módulos
import sys
if sys.path.count('C:\\ESP_PYTHON_20250331\\NIVEL_II\\ORLANYS') == 0:
    sys.path.append('C:\\ESP_PYTHON_20250331\\NIVEL_II\\ORLANYS')

# Definición de funciones
def personas_con():
    import conexion # Se establece conexión a la base de datos
    cursor = conexion.mibd.cursor()
    sql = "select * from personas"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for detalle in resultado:
        print(detalle)
    cursor.close() # Cerrar cursor
    conexion.mibd.close() # Cerrar base de datos

def personas_ing():
    import conexion # Se establece conexión a la base de datos
    cursor = conexion.mibd.cursor()
    while True:
        print("Ingrese los siguientes datos:")
        cedula = input("Cédula de identidad:")
        nombre = input("Nombre:")
        apellido = input("Apellido:")
        direccion = input("Dirección:")
        fechanac = input("Fecha de nacimiento (aaaa-mm-dd):")
        sql = "INSERT INTO personas(cedula, nombre, apellido, direccion, fechanac) VALUES (%s, %s, %s, %s, %s)"
        datos = (cedula, nombre, apellido, direccion, fechanac)
        cursor.execute(sql, datos)
        conexion.mibd.commit()
        continuar = input("¿Desea ingresar un nuevo registro (S/N)?")
        if continuar.upper() == 'S':
            continue
        else:
            break
    cursor.close() # Cerrar cursor
    conexion.mibd.close() # Cerrar base de datos

while True:
    print("Mantenimiento de datos personales".center(60,"-"))
    print("Menú".center(60,' '))
    print("1- Ingresar")
    print("2- Consultar")
    print("3- Salir")
    opcion = int(input("Ingrese una opción:"))
    if opcion == 1:
        personas_ing()
    elif opcion == 2:
        personas_con()
    else:
        print("Fin del programa...")
        break