# Importar las librerias necesarias
from flask import *
from flask import Flask, request

# Definir una instancia de la clase flask
app = Flask(__name__)

# Establecer un decorador de ruta
@app.route('/echo')
def obtener():
  entrada1 = request.args.get('dato1')
  entrada2 = request.args.get('dato2')
  return ('<h1>Los datos que usted ingresò a travès del url fueron los siguientes:<br>'+entrada1+'<br>'+entrada2+'<br></h1>')

# Ejecutar la aplicaciòn
if __name__ == '__main__':
  """
  Dannysa, port = 5001
  Orlanys, port = 5002
  Carla, port = 5003
  Henry, port = 5004
  """

  app.run(port=5002)