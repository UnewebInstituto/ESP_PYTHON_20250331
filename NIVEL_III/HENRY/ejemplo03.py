# Importar las librerías necesarias
from flask import *
from flask import Flask, render_template

# Definir una instancia de la clase Flask
app = Flask(__name__)

# Establecer un decorador de ruta
@app.route('/')
def inicio():
    enlaces = [['uneweb sitio oficial','https://www.uneweb.edu.ve'],['uneweb sitio de tutoriales','https://www.uneweb.edu.ve/tutoriales'],['uneweb plataforma online','https://www.uneweb.com/cursos']]
    return render_template('ejemplo03.html',lista=enlaces)

# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5004)

