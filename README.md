# AppWeb
Aplicacion web repositorio de tesis

Estado el proyecto: En proceso - Activo.

<<Pasos Python>>

Descargar Python version 3.11 desde la pagina oficial.
Verifica que la opcion añadir Python 3.11 a Path se encuentre activa

<<Pasos Flask>>

Crear una carpeta en el escritoria llamada 'Pagina_Flask'.
mkdir Pagina_Flask

Ingresar a la carpeta.
cd Pagina_Flask

Instalar virtualenv en python.
pip install virtualenv

Bajar el entorno virtual en la carpeta del proyecto.
virtualenv -p python3 env

Acceder a scripts y activar el entorno.
.\env\Scripts\activate

En caso de error "la ejecución de scripts está deshabilitada en este sistema."
1-Ingresar al powershell como administrador.
2-Ejecutar comando 'Set-ExecutionPolicy Unrestricted'.
3-Aceptar, ingresando 'S'.

Instalar Flask.
pip install flask

Verificar que flask este instalado.
pip list

Ejecutar programa
python .\app\app.py

Como resultado nos entrega informacion y una URL, que por lo general corresponde a 'http://127.0.0.1:5000'
Imgresa a esa URL desde cualquier navegador y se podra visualizar la pagina.

Para cerrar el servidor se debe ingresar 'ctrl+c' en el terminal.
