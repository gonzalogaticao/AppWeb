# AppWeb 

## Descripción
Aplicacion web para servir de repositorio de tesis.

## Estado el proyecto
    En proceso - Activo

## Instalación desde cero

### Python
- Descargar Python `version 3.11` desde la [pagina oficial](https://www.python.org/).
- Verifica que la opcion `añadir Python 3.11 a Path` se encuentre activa.

### Flask

- Instalar la biblioteca virtual envirtual en python:

      pip install virtualenv

- Bajar el entorno virtual dentro de la carpeta del proyecto. 
- En este caso nombramos al entorno como `env` y se creara una carpeta correspondiente.

      virtualenv -p python3 env

- Acceder a scripts y activar el entorno:

      .\env\Scripts\activate

- En caso de error "la ejecución de scripts está deshabilitada en este sistema".
1. Ingresar al powershell como administrador.
2. Ejecutar comando `Set-ExecutionPolicy Unrestricted.`
3. Aceptar ingresando `S.`

- Deberia visualizarse 'env' ante la ruta, de la siguiente manera: `(env) PS C:\Users\...`
- Instalar Flask en el proyecto:

      pip install flask

- Verificar que flask este instalado:

      pip list

- Crear primer `Hola Mundo`, con el siguiente codigo:
- 
![imagen](https://user-images.githubusercontent.com/115717996/206081733-05dd57bd-75db-47a1-b2da-b65fd440f6cf.png)

- Ejecutar programa con el comado `python .\carpeta\archivo.py`. En este caso:

      python .\app\app.py

- Como resultado nos entrega informacion y una URL, que por lo general corresponde a `http://127.0.0.1:5000`
- Ingresa al URL desde cualquier navegador y se podra visualizar la pagina:

![imagen](https://user-images.githubusercontent.com/115717996/206081829-c855a30b-9d6c-4090-8602-5a5ab50ddc62.png)

- Para cerrar el servidor se debe ingresar `ctrl+c` en el terminal.

- Licensia

        MIT License
