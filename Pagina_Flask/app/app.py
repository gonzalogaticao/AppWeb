from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)  #Inicializa aplicacion.
@app.route('/')
def index():
    return render_template('site/index.html')

@app.route('/tesis')
def tesis():
    return render_template('site/tesis.html')

@app.route('/envio')
def envio():
    return render_template('site/envio.html')

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/admin/login')
def login():
    return render_template('admin/login.html')

@app.route('/admin/tesis')
def adminTesis():
    return render_template('admin/tesis.html')

@app.route('/admin/tesis/save', methods=['POST'])
def atesisSave():
    print(request.form['txtTitulo'])
    return redirect('admin/tesis')

if __name__ == '__main__':  #Comprobar que estemos situados en el archivo principal.
    app.run(debug=True)