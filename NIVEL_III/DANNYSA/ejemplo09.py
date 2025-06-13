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

@app.route('/borrar01/<tmp_id>')     
def borrar01(tmp_id):
    import conexion
    cursor = conexion.mibd.cursor()

    sql = "DELETE FROM personas WHERE id= %s"
    datos = (tmp_id,)

    try:
        cursor.execute(sql, datos)
        conexion.mibd.commit()
        sql = "SELECT * FROM personas"
        resultado= []
        cursor.execute(sql)
        resultado= cursor.fetchall()
        cantidad= len(resultado)
        if cantidad == 0:
          mensaje_tmp = "No se encontro ningun registro en la tabla personas"

        else:
          mensaje_tmp = "Registro borrado con exito"
        
    except psycopg2.IntegrityError:
        mensaje_tmp = 'Error, registro no puede ser borrado'
    return render_template('ejemplo09_borrar.html', mensaje = mensaje_tmp, detalle=resultado)
   
@app.route('/actualizar01/<tmp_id>')     
def actualizar01(tmp_id):
    import conexion
    cursor = conexion.mibd.cursor()

    sql = "SELECT * FROM personas WHERE id= %s"
    datos = (tmp_id,)

    try:
        cursor.execute(sql, datos)
        resultado= []
              
        resultado= cursor.fetchall()
      
        mensaje_tmp = "Registro ubicado con exito"
        
    except psycopg2.IntegrityError:
        mensaje_tmp = 'Error, registro no puede ser ubicado'
    return render_template('ejemplo09_actualizar01.html', mensaje = mensaje_tmp, detalle=resultado)

@app.route('/actualizar02', methods=['GET', 'POST'])
def actualizar02():
    if request.method == 'POST':
      import conexion
      cursor = conexion.mibd.cursor()

      tmp_id = request.form['tmp_id']
      nombre = request.form['nombre']
      apellido = request.form['apellido']
      direccion = request.form['direccion']
      fechanac = request.form['fechanac']

      datos = (nombre, apellido, direccion, fechanac, tmp_id)

      sql = "UPDATE personas SET nombre=%s, apellido=%s, direccion=%s, fechanac=%s WHERE id = %s"

      mensaje_tmp = ''
      try:
        cursor.execute(sql, datos)
        conexion.mibd.commit()

        sql = "SELECT * FROM personas"
        resultado= []
        cursor.execute(sql)

      
        resultado= cursor.fetchall()

        #cursor.close()
        #conexion.mibd.close()
        mensaje_tmp = 'Registro fue actualizado con exito'
      except psycopg2.IntegrityError:
        mensaje_tmp = 'Error, registro no puede ser actualizado'
      return render_template('ejemplo09_actualizar.html', mensaje = mensaje_tmp, detalle=resultado)


# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5001)


