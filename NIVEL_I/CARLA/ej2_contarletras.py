# programa: ej2_contarletras.py
# autor: Carla Suarez
# fecha: 02-05-2025
"""
Este programa solicita el ingreso de una palabra
y da como resultado,el numero de letras de contiene 
la palabra ingresada
"""
#Declaracion de variables
palabra=""
contar_letras ={} # Dicionario
# Cuerpo principal del programa
while True:
    palabra = ""
    contar_letras = {} # Dicionario
    palabra = input("Por favor ingresa una palabra:")
    #Se recorre el contenido de la palabra
    for letra in palabra:
        contar_letras[letra] = palabra.count(letra)
    #Mostrar el contenido, de los valores almacenados en el diccionario
    for acumulado in contar_letras:
        print(acumulado, contar_letras[acumulado])  
    continuar = input("¿Desea ingresar una nueva palabra (S/N):?")
    if continuar.upper() == "S":
        continue
    else:
        print("Fin del programa")
        break 
        