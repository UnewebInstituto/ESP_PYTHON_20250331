# programa: ej1_resolvente.py
# autor: Orlanys Lemus
# fecha: 30-04-2025
"""
Este programa es un ejemplo mediante la eucaciòn
resolvente a los efectos de demostrar ciclos repetitivos
y condicionales anidados
"""
# Declaraciòn de mòdulo
import math
# Declaraciòn de variables
s = 0
b = 0
c = 0
subradical = 0
x1 = 0
x2 = 0
# Definiciòn del ciclo principal del programna
while True:
    print('Soluciòn a ecuaciòn resolvente'.center(50,'-'))
    while True:
        try:
            a = float(input('¿Valor de a:?'))
            break
        except ValueError:
            print('ERROR: Debe ingresar un valor nùmerico')
            continue
    if a == 0:
        print('ERROR: El valor de \'a\' debe ser diferente de 0')
    else:
        while True:
            try:
                b = float(input('¿Valor de b:?'))
                break
            except ValueError:
                print('ERROR: Debe ingresar un valor nùmerico')
                continue

        while True:
            try:
                c = float(input('¿Valor de c:?'))
            except ValueError:
                break
                print('ERROR: Debe ingresar un valor nùmerico')
                continue
        subradical = b*b-4*a*c
        if subradical < 0:
            print('ERROR: Expresiòn subradical no puede ser negativa')
        else:
            x1 = (-b + math.sqrt(subradical))/2*a
            x2 = (-b - math.sqrt(subradical))/2*a 
            print('x1:',x1)# Forma 1 de presentar resultado
            print(f'x2:{x2}') # Forma 2 de presentar resultado                             
            
    continuar = input('¿Usted desea obtener la resolvente para otros valores(S/N):?')
    if continuar.upper() == 'S':
        continue
    else:
        print('Fin del programa')
        break
    
