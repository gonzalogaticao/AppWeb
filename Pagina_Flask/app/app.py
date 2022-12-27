from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flaskext.mysql import MySQL
from datetime import datetime

from werkzeug.utils import secure_filename
import os

app = Flask(__name__)  #Inicializa aplicacion.
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "repositorio"
mysql.init_app(app)

#Rutas
@app.route('/')
def index():
    return render_template('site/index.html')

@app.route('/tesis')
def tesis():
    conexion = mysql.connect()
    print(conexion)

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

    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `tesis`")
    tesis=cursor.fetchall()
    conexion.commit()

    return render_template('admin/tesis.html', tesis=tesis)

@app.route('/admin/tesis/save', methods=['GET','POST'])
def tesisSave():

    _tesis=request.form['txtTitulo']
    _autor=request.form['txtAutor']
    _profesor=request.form['txtProfesor']
    _anio=request.form['txtAnio']
    _pdf=request.files['pdfTesis']

    tiempo = datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')

    if _pdf.filename!="":
        nuevoNombre = horaActual+"_"+_pdf.filename
        filesPath = "Pagina_Flask/app/templates/files/"
        _pdf.save(filesPath+nuevoNombre)


    sql="INSERT INTO `tesis` (`ID_T`, `ID_M`, `ID_U`, `TITULO_T`, `AUTORES_T`, `PROFESOR_T`, `ANIO_T`, `ARCHIVO_T`) VALUES (NULL, 1, 1, %s, %s, %s, %s, %s);"
    datos=(_tesis,_autor,_profesor,_anio,nuevoNombre)
    conexion = mysql.connect()      #Conexion.
    cursor=conexion.cursor()        #Se genera un cursor.
    cursor.execute(sql,datos)       #Cursor ejecuta el comando sql.
    conexion.commit()               #Se lleva a cabo.

    return redirect('/admin/tesis')

@app.route('/admin/tesis/delete', methods=['POST'])
def tesisDelete():
    _id=request.form['txtID']
    print(_id)

    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM `tesis` WHERE ID_T=%s", _id)
    tesis=cursor.fetchall()
    conexion.commit()
    print(tesis)

    return redirect('/admin/tesis')

if __name__ == '__main__':  #Comprobar que estemos situados en el archivo principal.
    app.run(debug=True)