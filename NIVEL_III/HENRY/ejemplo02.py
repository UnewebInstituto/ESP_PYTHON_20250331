# Importar las librerías necesarias
from flask import *
from flask import Flask, request

# Definir una instancia de la clase Flask
app = Flask(__name__)

# Establecer un decorador de ruta
@app.route('/echo')
def obtener():
    entrada1 = request.args.get('dato1')
    entrada2 = request.args.get('dato2')
    return ('<h1>Los datos que usted ingresó a través de la url fueron los siguentes:<br>'+entrada1+'<br>'+entrada2+'<br></h1>')

# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    http://127.0.0.1:5004/echo?dato1=ESTO+ES+UNA+PRUEBA&dato2=DE+PASE+DE+PARAMETROS+EN+LA+URL
    """
    app.run(port=5004)

