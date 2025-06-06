# Importación de módulos
from flask import Flask, request, render_template
import math

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
        cursor.close()
        conexion.mibd.close()
        mensaje_tmp = 'Registro fue almacenado con exito'
      except (ValueError):
        mensaje_tmp = 'Error, registro no puede ser almacenado'
      return render_template('ejemplo09_ingresar.html', mensaje = mensaje_tmp)
       

# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5001)


