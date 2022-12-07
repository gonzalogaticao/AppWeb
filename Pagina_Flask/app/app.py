from flask import Flask
from flask import render_template

app = Flask(__name__)  #Inicializa aplicacion.
@app.route('/')
def hello_world():
    #bienvenida = "Hola Mundo!"
    #return bienvenida
    return render_template('index.html')

if __name__ == '__main__':  #Comprobar que estemos situados en el archivo principal.
    app.run(debug=True)