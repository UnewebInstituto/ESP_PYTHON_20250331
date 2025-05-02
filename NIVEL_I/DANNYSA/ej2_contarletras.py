#programa ej2_contarletras
#autor dannysa
#fecha 2 de mayo

#este programa solicita el ingreso de una palabra y da como resultado
#el numero de letras de la palabra ingresada


#declaracion de variables
palabra = ""
contar_letras = {} #diccionario
#cuerpo principal del programa
while True:
    palabra = ""
    contar_letras = {}
    palabra = input("Por favor ingrese una palabra:")
    #se recorre el contenido de la palabra
    for letra in palabra:
      contar_letras[letra] = palabra.count(letra)
    #mostrar el contenido de los valores almacenados en diccionario
    for acumulado in contar_letras:
      print(acumulado, contar_letras[acumulado])
    continuar = input("¿Desea ingresar una nueva palabra (S/N):?")
    if continuar.upper() == "S":
        continue
    else:
        print("Fin del programa")
        break   