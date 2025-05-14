#def de modulos 
import sys
if sys.path.count('C:\\ESP_PYTHON_20250331\\NIVEL_II\\DANNYSA') == 0:
  sys.path.append('C:\\ESP_PYTHON_20250331\\NIVEL_II\\DANNYSA')

#definicion de funciones
def personas_con():
  import conexion #se establece conexion a la base de datos 
  cursor = conexion.mybd.cursor()
  sql = "select * from personas"
  cursor.execute(sql)
  resultado = cursor.fetchall()
  for detalle in resultado:
    print(detalle)
  cursor.close()
  conexion.mybd.close()


def personas_ing():
  import conexion
  cursor = conexion.mybd.cursor()
  while True:
    print("Ingrese los siguientes datos:")
    cedula = input("Cedula:")
    nombre = input("Nombre:")
    apellido = input("Apellido:")
    direccion = input("Direccion:")
    fechanac = input("fecha nac (aaaa-mm-dd):")
    sql = "INSERT INTO personas(cedula, nombre, apellido, direccion, fechanac) VALUES(%s, %s, %s, %s, %s)"
    datos = (cedula, nombre, apellido, direccion, fechanac)
    cursor.execute(sql, datos)
    conexion.mybd.commit()
    continuar = input("¿Desea ingresar un nuevo registro (S/N)?")
    if continuar.upper() == 'S':
            continue
    else:
            break  
  cursor.close()
  conexion.mybd.close()

while True:
  print("Mantenimiento de datos personales".center(60,"-"))
  print("Menu".center(60,'-'))
  print("1- Ingresar")
  print("2- Consultar")
  print("3- Salir")
  opcion = int(input("Ingrese una opcion:"))
  if opcion == 1:
    personas_ing()
  elif opcion == 2:
    personas_con()
  else:
    print("Fin del programa...")
    break 