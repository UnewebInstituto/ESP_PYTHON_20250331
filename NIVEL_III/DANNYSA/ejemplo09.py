# Importación de módulos
from flask import Flask, request, render_template
import math
import psycopg2

# Instancia de la clase Flask
app = Flask(__name__)

# Se define la ruta principal para que cargue el
# formulario
@app.route('/')
def inicio():
    return render_template('ejemplo09.html')

@app.route('/ingresar')
def ingresar():
    return render_template('ejemplo09_ingresar.html')

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar01():
    if request.method == 'POST':
      import conexion
      cursor = conexion.mibd.cursor()
      documento = request.form['documento']
      numero = request.form['numero']
      cedula = documento + numero 
      nombre = request.form['nombre']
      apellido = request.form['apellido']
      direccion = request.form['direccion']
      fechanac = request.form['fechanac']

      datos = (cedula, nombre, apellido, direccion, fechanac)

      sql = "INSERT INTO personas(cedula, nombre, apellido, direccion, fechanac) VALUES (%s, %s, %s, %s, %s)"

      mensaje_tmp = ''
      try:
        cursor.execute(sql, datos)
        conexion.mibd.commit()
        #cursor.close()
        #conexion.mibd.close()
        mensaje_tmp = 'Registro fue almacenado con exito'
      except psycopg2.IntegrityError:
        mensaje_tmp = 'Error, registro no puede ser almacenado'
      return render_template('ejemplo09_ingresar.html', mensaje = mensaje_tmp)

@app.route('/consultar')
def consultar():
    return render_template('ejemplo09_consultar.html')  
@app.route('/consultar', methods=['GET', 'POST'])     
def consultar_01():
    if request.method == 'POST':
      import conexion
      cursor = conexion.mibd.cursor()
      documento = request.form['documento']
      numero = request.form['numero']
      cedula = documento + numero 
     
      datos = (cedula,)

      sql = "SELECT * FROM personas WHERE cedula= %s"
      resultado = []

      mensaje_tmp = ''
      try:
        cursor.execute(sql, datos)
        resultado= cursor.fetchall()
        cantidad= len(resultado)
        if cantidad == 0:
           mensaje_tmp = "No se encontro ningun registro con la cedula suministrada"

        else:
           mensaje_tmp = "Consulta efectuada con exito"
      
        
       
      except psycopg2.IntegrityError:
        mensaje_tmp = 'Error, al acceder a la base de datos'

      #cursor.close()
      #conexion.mibd.close()

      return render_template('ejemplo09_consultar_01.html', mensaje = mensaje_tmp, detalle=resultado)

@app.route('/reporte')     
def reporte():
    import conexion 
    cursor = conexion.mibd.cursor()
    sql = "SELECT * FROM personas"
    resultado= []
    mensaje_tmp = ''
    try:
      cursor.execute(sql)
      resultado= cursor.fetchall()
      cantidad= len(resultado)
      if cantidad == 0:
          mensaje_tmp = "No se encontro ningun registro en la tabla personas"

      else:
          mensaje_tmp = "Reporte procesado con exito"
    
    except psycopg2.IntegrityError:
      mensaje_tmp = 'Error, al acceder a la base de datos'

    #cursor.close()
    #conexion.mibd.close()

    return render_template('ejemplo09_reporte.html', mensaje = mensaje_tmp, detalle=resultado)      

@app.route('/borrar')     
def borrar():
    import conexion 
    cursor = conexion.mibd.cursor()
    sql = "SELECT * FROM personas"
    resultado= []
    mensaje_tmp = ''
    try:
      cursor.execute(sql)
      resultado= cursor.fetchall()
      cantidad= len(resultado)
      if cantidad == 0:
          mensaje_tmp = "No se encontro ningun registro en la tabla personas"

      else:
          mensaje_tmp = "Reporte procesado con exito"
    
    except psycopg2.IntegrityError:
      mensaje_tmp = 'Error, al acceder a la base de datos'

    #cursor.close()
    #conexion.mibd.close()

    return render_template('ejemplo09_borrar.html', mensaje = mensaje_tmp, detalle=resultado)

@app.route('/actualizar')     
def actualizar():
    import conexion 
    cursor = conexion.mibd.cursor()
    sql = "SELECT * FROM personas"
    resultado= []
    mensaje_tmp = ''
    try:
      cursor.execute(sql)
      resultado= cursor.fetchall()
      cantidad= len(resultado)
      if cantidad == 0:
          mensaje_tmp = "No se encontro ningun registro en la tabla personas"

      else:
          mensaje_tmp = "Reporte procesado con exito"
    
    except psycopg2.IntegrityError:
      mensaje_tmp = 'Error, al acceder a la base de datos'

    #cursor.close()
    #conexion.mibd.close()

    return render_template('ejemplo09_actualizar.html', mensaje = mensaje_tmp, detalle=resultado)

@app.route('/borrar01')     
def borrar01():
# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5001)


