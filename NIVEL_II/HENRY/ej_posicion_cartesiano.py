from tkinter import *

ventana = Tk()
ventana.title('Ejemplo posicionamiento Cartesiano')

ventana.geometry("400x200")

boton = Button(ventana, text='Posicionamiento diferente').place(x=10, y=10)
etiqueta1 = Label(ventana, text='Posicionamiento diferente 1').place(x=200, y=10)
etiqueta2 = Label(ventana, text='Posicionamiento diferente 2').place(x=10, y=50)
etiqueta3 = Label(ventana, text='Posicionamiento diferente 3').place(x=200, y=50)

ventana.mainloop()
