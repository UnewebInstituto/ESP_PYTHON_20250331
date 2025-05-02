#definición de función
#Es una entidad de programación, que permite descomponer
#la complejidad del código, se declara de la siguiente manera:
def sumar(arg_n1,arg_n2):
    return (arg_n1 + arg_n2)

def restar(arg_n1,arg_n2):
    return (arg_n1 - arg_n2)

def multiplicar(arg_n1,arg_n2):
    return (arg_n1 * arg_n2)

def dividir(arg_n1,arg_n2):
    if arg_n2 == 0:
        return 'ERROR'
    else:
        return (arg_n1 / arg_n2)