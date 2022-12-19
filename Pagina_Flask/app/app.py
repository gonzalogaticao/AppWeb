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
def tesisSave():

    _tesis=request.form['txtTitulo']
    _autor1=request.form['txtAutor1']
    _autor2=request.form['txtAutor2']
    _profesor=request.form['txtProfesor']
    _anio=request.form['txtAnio']
    _pdf=request.files['pdfTesis']

    print(_tesis)
    print(_autor1)
    print(_autor2)
    print(_profesor)
    print(_anio)
    print(_pdf)

    return redirect('admin/tesis')

if __name__ == '__main__':  #Comprobar que estemos situados en el archivo principal.
    app.run(debug=True)