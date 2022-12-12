from flask import Flask
from flask import render_template

app = Flask(__name__)  #Inicializa aplicacion.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tesis')
def tesis():
    return render_template('tesis.html')

@app.route('/envio')
def envio():
    return render_template('envio.html')

if __name__ == '__main__':  #Comprobar que estemos situados en el archivo principal.
    app.run(debug=True)