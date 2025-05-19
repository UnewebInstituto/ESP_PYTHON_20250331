from tkinter import *

def imprime():
    print('Oprimiò el botòn imprimir')

ventana = Tk()
ventana.title('Ejemplo botones')

btn_imprimir = Button(ventana,text='Imprimir',fg='blue',command=imprime)
btn_imprimir.pack(side=LEFT)

btn_salir = Button(ventana,text= 'Salir',fg='red', command=ventana.quit)
btn_salir.pack(side=RIGHT)

ventana.mainloop()

