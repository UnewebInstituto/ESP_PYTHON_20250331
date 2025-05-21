# Definicion de modulos
import sys
if sys.path.count('C:\\ESP_PYTHON_20250331\\NIVEL_II\\CARLA') == 0:
    sys.path.append('C:\\ESP_PYTHON_20250331\\NIVEL_II\\CARLA')


# Definicion de funciones
def guardar_datos():
    import conexion # Se establece conexion a la base de datos
    cursor = conexion.mibd.cursor()
    sql = "select * from personas"
    resultado = cursor.execute(sql)
    resultado = cursor.fetchall()
    for detalle in resultado:
        print(detalle)
    cursor.close() # Cerrar cursor
    conexion.mibd.close() # Cerrar base de datos
    
def personas_ing():
    import conexion # Se establece conexion a la base de datos
    cursor = conexion.mibd.cursor()
    while True:
      print("Ingrese los siguientes datos:")
      cedula = input("Cedula:")
      nombre = input("Nombre:")
      apellido = input("Apellido:")
      direccion = input("Direccion:")
      fechanac = input("Fecha de naciomiento (aaa-mm-dd):")
      sql = "INSERT INTO personas(cedula, nombre, apellido, direccion, fechanac) VALUES(%s, %s, %s, %s, %s)"
      datos = (cedula, nombre, apellido, direccion, fechanac)
      cursor.execute(sql, datos)
      conexion.mibd.commit()
      continuar = input("¿Desea ingresar un nuevo registro (S/N)?")
      if continuar.upper() == 'S':
          continue
      else:
          break
while True:
    print("Mantenimiento de datos personales".center(60,"-"))
    print("Menu".center(60,' '))
    print("1- Ingresar")
    print("2- Consultar")
    print("3- Salir")
    opcion = int (input("Ingrese una opcion:"))
    if opcion == 1:
        personas_ing()
    elif opcion == 2:
        personas_con()
    else:
        print("Fin del programa...")
        break