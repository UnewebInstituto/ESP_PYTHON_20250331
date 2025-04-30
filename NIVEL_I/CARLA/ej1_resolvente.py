# programa: ej1_resolvente.py
# autor: Carla Suarez
# fecha: 30-04-2025
"""
Este programa es un ejemplo mediante la ecuacion
resolvente a los efectos de demostrar ciclo repetitivos
y condicionales anidados
"""
# Declaracion de modulo
import math 
# Declaracion de variables
a = 0
b = 0
c = 0
subradical = 0
x1 = 0
x2 = 0
# Definicion del ciclo principal del programa
while True:
    print('Solucion a Ecuacion Resolvente'.center(50,'-'))
    while True:
        try:
            a = float(input('¿Valor de a:?'))
            break
        except ValueError:
            print('ERROR: Debe ingresar un valor numerico')
            continue
    if a == 0:
            print ('ERROR: El valor de \'a\' debe ser diferente de 0')
            break
    else:
        while True:
            try:
                b = float(input('¿Valor de b:?'))
                break
            except ValueError:
                print('ERROR: Debe ingresar un valor numerico')
                continue
        while True:
            try:
                c = float(input('¿Valor de c:?'))
                break
            except ValueError:
                print('ERROR: Debe ingresar un valor numerico')
                continue
        subradical = b*b-4*a*c
        if subradical < 0:
            print('ERROR: Expesion subradical no puede ser negativa')
        else:
            x1 = (-b + math.sqrt(subradical)) / 2*a
            x2 = (-b - math.sqrt(subradical)) / 2*a
            print('x1:',x1) #Forma de 1 de presentar resultado
            print(f'x2:{x2}') # Forma de 2 de presentar resultado     
    continuar = input ('¿Usted desea obtener la resolvente para otros valores (S/N) :?')
    if continuar.upper() == 'S':
        continue
    else:
        print ('Fin del programa')
        break

    
