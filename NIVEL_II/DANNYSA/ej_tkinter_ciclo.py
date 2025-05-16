#importar modulos
from tkinter import*

#def de funciones
def ciclo():
  for numero in range(0,11):
    print(numero)

def imprimir():
  print('Usted oprimio el boton imprimir')

#crear instancia clase
ventana = Tk()
ventana.title('Ejemplo ciclo desde tkinter')
#crear instancia de clase label
etiqueta = Label(ventana, text='Por favor oprima el boton para generar el ciclo')
etiqueta.pack 
#craer instancia clase button 
boton = Button(ventana, text='Generar ciclo', command=ciclo)
boton.pack()

boton_salir = Button(ventana, text='Salir', command=ventana.quit)
boton_salir.pack()

boton_imprimir = Button(ventana, text='Imprimir', command=imprimir)
boton_imprimir.pack()
#ejecutando la ventana hasta que decida salir 
ventana.mainloop()