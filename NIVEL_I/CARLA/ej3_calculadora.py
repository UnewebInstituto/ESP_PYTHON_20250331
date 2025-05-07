# Declaración de librería o módulos
import sys
if sys.path.count('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA') == 0:
    sys.path.append('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA')
import modulo_calculadora
# Declaración de funciones
# No hay 
# Declaración de variables
opcion = 0
nro1 = 0
nro2 = 0
# Declaración del cuerpo principal del programa
while True:
    print("Calculadora básica".center(60,"-"))
    while True:
        try:
            opcion = int(input("Ingrese el número de la operación a efectuar \n 1: +\n 2: -\n 3: *\n 4: /\n 5: ^\n 6: Salir\n=>"))
            if (opcion < 1 or opcion > 6):
                print("Error: Opción no válida")
            elif opcion == 6:
                print("Fin del programa calculadora...")
                quit() #salir del programa, pero solo para consola interactiva
                sys.exit() # Salir del sistema a la consola dedl terminal
            else:
                break
        except ValueError:
            print("Error: Ingrese un número entero entre 1 y 6")
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
    if opcion == 1:
        print("El resultado es:", modulo_calculadora.sumar(nro1, nro2))
    elif opcion == 2:
        print("El resultado es:", modulo_calculadora.restar(nro1, nro2))
    elif opcion == 3:
        print("El resultado es:", modulo_calculadora.multiplicar(nro1, nro2))
    elif opcion == 4:
        print("El resultado es:", modulo_calculadora.dividir(nro1, nro2))
    elif opcion == 5:
        print("El resultado es:", modulo_calculadora.potencia(nro1, nro2))
        

