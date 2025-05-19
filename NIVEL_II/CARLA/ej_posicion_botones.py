from tkinter import *

def saludar():
  print('Usted oprimio el boton saludar')
  
def minimizar():
      ventana.iconify()

def salir():
    ventana.quit()  


    
ventana = Tk()
ventana.title('Ejemplo posicionamiento cartesiano')
ventana.geometry("400x200")

boton1 = Button(ventana, text='Saludar',command=saludar).place(x=10,y=10)

etiqueta1 = Label(ventana, text='Posicionamiento diferente 1').place(x=200,y=10)
boton2 = Button(ventana, text='Salir',command=salir).place(x=10,y=50)

boton3 = Button(ventana, text='Minimizar',command=minimizar).place(x=200, y=50)                                                     
ventana.mainloop()