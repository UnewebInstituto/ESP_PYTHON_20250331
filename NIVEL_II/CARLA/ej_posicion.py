from tkinter import *
    
ventana = Tk()
ventana.title('Ejemplo posicionamiento')
boton = Button(ventana, text='Posicionamiento diferente').grid(row=0,column=1)
etiqueta1 = Label(ventana, text='Posicionamiento diferente 1').grid(row=0,column=0)
etiqueta2 = Label(ventana, text='Posicionamiento diferente 2').grid(row=1,column=1)
etiqueta3 = Label(ventana, text='Posicionamiento diferente 3').grid(row=2, column=1)                                                     
ventana.mainloop()