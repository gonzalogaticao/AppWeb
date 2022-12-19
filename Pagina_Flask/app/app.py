from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flaskext.mysql import MySQL

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
    print(conexion)

    return render_template('admin/tesis.html')

@app.route('/admin/tesis/save', methods=['POST'])
def tesisSave():

    _tesis=request.form['txtTitulo']
    _autor1=request.form['txtAutor1']
    _autor2=request.form['txtAutor2']
    _profesor=request.form['txtProfesor']
    _anio=request.form['txtAnio']
    _pdf=request.files['pdfTesis']

    sql="INSERT INTO `tesis` (`ID`, `NOMBRES`, `AUTOR1`, `AUTOR2`, `PROFESOR`, `ANIO`, `PDF`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"
    datos=(_tesis,_autor1,_autor2,_profesor,_anio,_pdf.filename)
    conexion = mysql.connect()      #Conexion.
    cursor=conexion.cursor()        #Se genera un cursor.
    cursor.execute(sql,datos)       #Cursor ejecuta el comando sql.
    conexion.commit()               #Se lleva a cabo.

    #print(_tesis)
    #print(_autor1)
    #print(_autor2)
    #print(_profesor)
    #print(_anio)
    #print(_pdf)

    return redirect('/admin/tesis')

if __name__ == '__main__':  #Comprobar que estemos situados en el archivo principal.
    app.run(debug=True)