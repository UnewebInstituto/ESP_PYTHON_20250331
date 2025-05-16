# Importar librerias o mòdulos
from tkinter import *

# Definiciòn de funciones
def ciclo():
  # El resultado de esta funciòn se
  # muestrra en la consola del idle
  for numero in range(0,11):
    print(numero)

def imprimir():
  print('Usted oprimiò el botòn imprimir-')
  

# Crear instancia de la clse Tk()
ventana = Tk()
ventana.title('Ejemplo ciclo desde Tkinter')
# Crear instancia de la clase Label()
etiqueta = Label(ventana, text='Por favor oprima el botòn para generar el ciclo')
etiqueta.pack
# Crear instancia de la clase Button()
boton = Button(ventana, text='Generar ciclo', command=ciclo)
boton.pack()

boton_salir = Button(ventana, text='Salir', command=ventana.quit)
boton_salir.pack()

boton_imprimir = Button(ventana, text='Imprimir', command=imprimir)
boton_imprimir.pack()

# Ejecutando la ventana hasta que decida salir
ventana.mainloop()
