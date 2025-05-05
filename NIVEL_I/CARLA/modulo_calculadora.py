# Definicion de funcion
# Es una identidad de programacion, que permite descomponer
#la complejidad del codigo, se declara de la siguiente manera:
def sumar(arg_n1,arg_n2):
    return (arg_n1 + arg_n2)

def restar (arg_n1,arg_n2):
    return(arg_n1 - arg_n2)

def multiplicar (arg_n1,arg_n2):
    return(arg_n1 * arg_n2)
    
def dividir (arg_n1,arg_n2):
  if arg_n2 == 0:
      return 'ERROR'
  else:
      return (arg_n1 / arg_n2)
def potencia(base, expo):
    producto = 1
    i = 0
    while i < expo:
        producto = producto * base
        i = i + 1
    return producto