from flask import *
from flask import Flask 

#Definir una instancia de la clase Flask 
app = Flask(__name__)

@app.route('/')
def saludar():
  return('<h1>Hola, bienvenidos a Flask</h1>')

if __name__=='__main__':
  app.run(port=5001)
