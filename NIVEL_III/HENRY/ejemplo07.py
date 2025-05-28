# Importación de módulos
from flask import Flask, request, render_template
import math

# Instancia de la clase Flask
app = Flask(__name__)

# Se define la ruta principal para que cargue el
# formulario
@app.route('/')
def inicio():
    return render_template('ejemplo07.html')


@app.route('/',methods=['GET','POST'])
def procesar_entrada():
    if request.method == 'POST':
        a = eval(request.form['a'])
        b = eval(request.form['b'])
        c = eval(request.form['c'])
        if a == 0:
            texto_resultado = 'ERROR: Valor de a, debe ser diferente de cero'
        else:
            sub_radical = b * b - 4 * a * c
            if sub_radical < 0:
                texto_resultado = 'ERROR: Valor de expresión subradical, no debe ser negativo'
            else:
                x1 = (-b+math.sqrt(sub_radical))/(2*a)
                x2 = (-b-math.sqrt(sub_radical))/(2*a)
                texto_resultado = 'x1=' + str(x1) + ',x2=' + str(x2)
        return render_template('ejemplo07.html',resultado = texto_resultado)









# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5004)


