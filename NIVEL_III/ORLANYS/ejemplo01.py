# Importar las librerias necesarias
from flask import *
from flask import Flask

# Definir una instancia de la clase flask
app = Flask(__name__)

# Establecer un decorador de ruta
@app.route('/')
def saludar():
  return ('<h1>Hola, bienvenido a Flask</h1')

# Ejecutar la aplicaciòn
if __name__ == '__main__':
  """
  Dannysa, port = 5001
  Orlanys, port = 5002
  Carla, port = 50003
  Henry, port = 50004
  """

  app.run(port=5002)