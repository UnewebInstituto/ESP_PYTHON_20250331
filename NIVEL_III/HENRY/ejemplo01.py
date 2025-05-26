# Importar las librerías necesarias
from flask import *
from flask import Flask

# Definir una instancia de la clase Flask
app = Flask(__name__)

# Establecer un decorador de ruta
@app.route('/')
def saludar():
    return ('<h1>Hola, bienvenidos a Flask</h1>')

# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5004)

