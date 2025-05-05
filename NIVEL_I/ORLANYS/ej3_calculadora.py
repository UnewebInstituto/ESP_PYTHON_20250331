# Declaración de librerias o módulos
import sys
if sys.path.count('c:/ESP_PYTHON_20250331/NIVEL_I/ORLANYS') == 0:
    sys.path.append('c:/ESP_PYTHON_20250331/NIVEL_I/ORLANYS')
import modulo_calculadora
# Declaración de funciones
# No hay
# Declaración de variables
opción = 0
nro1 = 0
nro2 = 0
# Declaración de cuerpo principal del programa
while True:
  print("calculadora básica".center(60,"-"))
  while True:
    try:
      opción = int(input("Ingrese la operación a efectuar \n 1: +\n 2: -\n 3: *\n 4: /\n 5: ^\n 6: Salir\n=>"))
      if(opción < 1 or opción > 6):
        print("Error: Opción no vàlida")
      elif opción == 6:
          print("Fin del programa calculadora...")
          quit() # Salir del programa 
      else:
        break
    except ValueError:
      print("Error: Ingrese un número entre 1 y 6")
  while True:
    try:
      nro1 = int(input("Ingrese 1er. Número:"))
      break
    except ValueError:
      print("Error: Ingrese un número entero")

  while True:
    try:
      nro2 = int(input("Ingrese 2do. Número:"))
      break
    except ValueError:
      print("Error: Ingrese un número entero")

  if opción == 1:
    print("El resultado es:", modulo_calculadora.sumar(nro1,nro2))
  elif opción == 2:
    print("El resultado es:", modulo_calculadora.restar(nro1,nro2))
  elif opción == 3:
    print("El resultado es:", modulo_calculadora.multiplicar(nro1,nro2))
  elif opción == 4:
    print("El resultado es:", modulo_calculadora.dividir(nro1,nro2))
  elif opción == 5:
    print("El resultado es:", modulo_calculadora.potencia(nro1,nro2))
