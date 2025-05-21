# Importar librerías
from tkinter import *

# Declaración de funciones
def imprimir_datos():
    print('Cédula:',cedula.get(),',Nombre:',nombre.get(),',Apellido:',apellido.get(),',Dirección:',direccion.get(),',Fecha Nacimiento:',fechanac.get())

def salir():
    ventana.quit()

# Inicialización de variables
ventana = Tk()

cedula = StringVar()
nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
fechanac = StringVar()
ventana.title('Entrada Datos de Personas')
''
ventana.geometry('400x400')
''

# Cuerpo principal del programa
etiqueta_cedula = Label(ventana,text='CEDULA:').place(x=10, y=10)
entrada_cedula = Entry(ventana,textvariable=cedula).place(x=200, y=10)
etiqueta_nombre = Label(ventana,text='NOMBRE:').place(x=10, y=50)
entrada_nombre = Entry(ventana, textvariable=nombre).place(x=200, y=50)
etiqueta_apellido = Label(ventana, text='APELLIDO:').place(x=10, y=90)
entrada_apellido = Entry(ventana, textvariable=apellido).place(x=200, y=90)
etiqueta_direccion = Label(ventana, text='DIRECCION:').place(x=10, y=130)
entrada_direccion = Entry(ventana, textvariable=direccion).place(x=200, y=130)
etiqueta_fechanac = Label(ventana, text='FECHA NACIMIENTO:').place(x=10, y=170)
entrada_fechanac = Entry(ventana, textvariable=fechanac).place(x=200, y=170)
btn_guardar = Button(ventana,text='GUARDAR',command=imprimir_datos).place(x=150, y=210)
btn_cerrar = Button(ventana,text='SALIR',command=salir).place(x=250, y=210)

ventana.mainloop()

