from tkinter import *

def imprime():
    print('Oprimio el boton imprimir')
    
ventana = Tk()

btn_imprimir = Button(ventana,text='Imprime',fg='blue',
command=imprime)
btn_imprimir.pack(side=LEFT)

btn_salir = Button(ventana,text='Salir',fg='red',
command=ventana.quit)
btn_salir.pack(side=RIGHT) 
ventana.mainloop()