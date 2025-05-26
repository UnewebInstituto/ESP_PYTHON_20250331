from flask import *
from flask import Flask 

# Definir una instancia de la clase Flask 

app = Flask(__name__) 

#Establecer un decorador de ruta 
@app.route('/')
def saludar():
  return ('<h1>Hola, bienvenidos a Flask</h1>')

# Ejecutar la aplicacion
if __name__ == '__main__':
  """
  Dannysa , 
  Carla , port= 5003
  """
app.run(port=5003)
    
    