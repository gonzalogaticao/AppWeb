from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flaskext.mysql import MySQL
from datetime import datetime

from werkzeug.utils import secure_filename
import os

app = Flask(__name__)  #Inicializa aplicacion.
app.secret_key="secretkey"

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

@app.route('/css/<archivocss>')
def css(archivocss):
    return send_from_directory(os.path.join('templates\site\css'),archivocss)

@app.route('/files/<pdf>')
def pdf(pdf):
    print(pdf)
    print(os.path.join('Pagina_Flask/app/templates/files/'),pdf)
    return send_from_directory(os.path.join('templates/files'),pdf)

@app.route('/tesis')
def tesis():
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `tesis`")
    tesis=cursor.fetchall()
    conexion.commit()

    return render_template('site/tesis.html', tesis=tesis)

@app.route('/search', methods=['GET', 'POST'])
def search():

  query = request.args.get('word')
  results = []
  
  conexion = mysql.connect()
  cursor = conexion.cursor()
  cursor.execute("SELECT * FROM `tesis` WHERE `TITULO_T` LIKE %s",('%' + query + '%'))
  results = cursor.fetchall()         
  
  cursor.close()
  conexion.close()
  
  return render_template('site/search.html', query=query, results=results)

@app.route('/admin/register')
def register():
    return render_template('admin/register.html')

@app.route('/admin/register/save',methods=['POST'])
def admin_register_save():

    _usuario=request.form['txtNombre']
    _password=request.form['txtPassword']
    _email=request.form['txtEmail']

    sql="INSERT INTO `moderadores` (`ID_M`, `NOMBRE_M`, `CORREO_M`, `CONTRASENA_M`) VALUES (NULL,%s,%s,%s);"
    datos=(_usuario,_email,_password)
    conexion = mysql.connect()      #Conexion.
    cursor=conexion.cursor()        #Se genera un cursor.
    cursor.execute(sql,datos)       #Cursor ejecuta el comando sql.
    conexion.commit()               #Se lleva a cabo.

    return redirect('/admin/login')

@app.route('/admin')
def admin():

    if not 'login' in session:
        return render_template('/admin/login.html')

    return render_template('admin/index.html')

@app.route('/admin/login')
def login():
    return render_template('admin/login.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        _usuario=request.form['txtUsername']
        _password=request.form['txtPassword']

        conexion = mysql.connect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM `moderadores` WHERE NOMBRE_M=%s AND CONTRASENA_M=%s",(_usuario,_password))
        admin=cursor.fetchone()

        if admin:
            print("ES ADMIN")
            session["login"]=True
            session["usuario"]=_usuario
            return redirect("/admin")

    return render_template('/admin/login.html', admin=admin, mensaje="Error: credenciales no coinciden")

@app.route('/admin/cerrar')
def cerrar_session():
    session.clear()
    return render_template('/admin/login.html')

@app.route('/admin/tesis')
def adminTesis():

    if not 'login' in session:
        return render_template('/admin/login.html')

    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `tesis`")
    tesis=cursor.fetchall()
    conexion.commit()

    return render_template('admin/tesis.html', tesis=tesis)

@app.route('/admin/tesis/save', methods=['GET','POST'])
def tesisSave():

    if not 'login' in session:
        return render_template('/admin/login.html')

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

    if not 'login' in session:
        return render_template('/admin/login.html')

    _id=request.form['txtID']

    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT archivo_t FROM `tesis` WHERE ID_T=%s", _id)
    tesis=cursor.fetchall()
    conexion.commit()

    if os.path.exists("Pagina_Flask/app/templates/files/"+str(tesis[0][0])):
        os.remove("Pagina_Flask/app/templates/files/"+str(tesis[0][0]))

    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM `tesis` WHERE ID_T=%s", _id)
    tesis=cursor.fetchall()
    conexion.commit()

    return redirect('/admin/tesis')

if __name__ == '__main__':  #Comprobar que estemos situados en el archivo principal.
    app.run(debug=True)