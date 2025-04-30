# programa: ej1_resolvente.py
# autor dannysa andres
# fecha 30/04/25
"""
este programa es un ejemplo de la ecuacion resolvente para demostrar ciclos repetitivos y
condicionales anidados
"""
#declaracion de modulos
import math

# declaracion de variables
a = 0
b = 0
c = 0
subradical = 0
x1 = 0
x2 = 0
#definicion del ciclo ppal del programa

while True:
    print('solucion a ecuacion resolvente'.center(50 ,'-'))
    while True:
        try:
            a = float(input('valor de a:'))
            break
        except ValueError:
            print('error:debe ingresar un valor numerico')
            continue
    if a == 0:
        print('error: el valor de \'a\' debe ser diferente de 0')
    else:
        while True:
            try:
                b = float(input('valor de b:'))
                break
            except ValueError:
                print('error:debe ingresar un valor numerico')
                continue        
        while True:
            try:
                c = float(input('valor de c:'))
                break
            except ValueError:
                print('error:debe ingresar un valor numerico')
                continue
        subradical = b*b-4*a*c
        if subradical < 0:
            print('error: expresion subradical no puede ser negativa')
        else:
            x1 = (-b + math.sqrt(subradical))/2*a
            x2 = (-b - math.sqrt(subradical))/2*a
            print('x1:',x1)#forma1 de presentar
            print('x2:',x2)
                       
    continuar = input('usted desea obtener la resolvente para otros valores (S/N):')
    if continuar.upper() == 'S':
        continue
    else:
        print('Fin del programa')
        break
