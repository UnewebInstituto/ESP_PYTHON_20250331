from tkinter import *
from tkinter import messagebox
import sys
if sys.path.count('C:\\ESP_PYTHON_20250331\\NIVEL_II\\CARLA') == 0:
    sys.path.append('C:\\ESP_PYTHON_20250331\\NIVEL_II\\CARLA')

def limpiar_datos():
    cedula.set('')
    nombre.set('')
    apellido.set('')
    direccion.set('')
    fechanac.set('')
    tmp_cedula = ''
    tmp_nombre = ''
    tmp_apellido = ''
    tmp_direccion =''
    tmp_fechanac = ''
def guardar_datos():
  import conexion
  cursor = conexion.mibd.cursor() 

  tmp_cedula = cedula.get()
  tmp_nombre = nombre.get()
  tmp_apellido = apellido.get()
  tmp_direccion = direccion.get()
  tmp_fechanac = fechanac.get() 
  
  sql = "INSERT INTO personas(cedula, nombre, apellido, direccion, fechanac) VALUES(%s, %s, %s, %s, %s)"
  datos = (tmp_cedula, tmp_nombre, tmp_apellido, tmp_direccion, tmp_fechanac)
  cursor.execute(sql, datos)
  conexion.mibd.commit() 
  cursor.close() # Cerrar cursor
  conexion.mibd.close() # Cerrar base de datos 
  print ('Los datos fueron guardados') 
  messagebox.showwarning('Guardar datos','Los datos fueron guardados')
  limpiar_datos()
def imprimir_datos():
  print('Cedula:',cedula.get(),',Nombre:',nombre.get(),',Apellido:',apellido.get(),',Direccion:',direccion.get(),',Fecha Nacimiento:',fechanac.get())
    
def salir():
    resp = messagebox.askyesno('Salir','¿Esta seguro que quiere abandonar la aplicacion')
    if resp == True:
      ventana.quit() 
    else:
      messagebox.showinfo('Salir','Se mantiene en ejecucion la aplicacion de guardar datos')
  
  # Inicializacion de variables   
ventana = Tk()
cedula = StringVar()
nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
fechanac = StringVar()
ventana.title('Guardar Datos de personas')
''
ventana.geometry('400x400')
''
etiqueta_cedula = Label(ventana, text='CEDULA:').place(x=10, y=10)
entrada_cedula = Entry(ventana,textvariable=cedula).place(x=230, y=10)
etiqueta_nombre = Label(ventana, text='NOMBRE:').place(x=10, y=50)
entrada_nombre = Entry(ventana,textvariable=nombre).place(x=230, y=50)
etiqueta_apellido = Label(ventana, text='APELLIDO:').place(x=10, y=90)
entrada_apellido = Entry(ventana,textvariable=apellido).place(x=230, y=90)
etiqueta_direccion = Label(ventana, text='DIRECCION:').place(x=10, y=130)
entrada_direccion = Entry(ventana,textvariable=direccion).place(x=230, y=130)
etiqueta_fechanan = Label(ventana, text='FECHA NACIMIENTO (aaa-mm-dd):').place(x=10, y=170)
entrada_fechanac = Entry(ventana,textvariable=fechanac).place(x=230, y=170)

btn_guardar = Button(ventana, text='GUARDAR',command=guardar_datos).place(x=150, y=210)
btn_cerrar = Button(ventana, text='SALIR',command=salir).place(x=250, y=210)
ventana.mainloop()





