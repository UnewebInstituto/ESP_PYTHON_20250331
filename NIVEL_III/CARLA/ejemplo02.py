from flask import *
from flask import Flask, request

# Definir una instancia de la clase Flask 

app = Flask(__name__) 

#Establecer un decorador de ruta 
@app.route('/echo')
def obtener():
    entrada1 = request.args.get('dato1')
    entrada2 = request.args.get('dato2')
    return ('<h1>Los datos que usted ingreso a traves del url fueron los siguientes:<br>'+entrada1+'<br>'+entrada2+'<br></h1>')

# Ejecutar la aplicacion
if __name__ == '__main__':
  """
  Dannysa , 
  Carla , port= 5003
  """
app.run(port=5003)
http://127.0.0.1:5003/echo?dato1=ESTO+ES+UNA+PRUEBA&dato2=DE+PASE+DE+PARAMETROS+EN+LA+URL    
    