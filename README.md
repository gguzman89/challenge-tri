# challenge-tri
Aplicacion desarrollada en Django para asociar personas con cursos de idiomas.

## Lenguaje
* Python 3.8.1

## Dependencias del proyecto 
* virtualenv 16.7.9
* django 3.0.2
* djangorestframework 3.11.0

## Instalacion y configuracion del entorno
* clonar el proyecto
* acceder al carpeta root del proyecto y correr: venv\Scripts\activate
* instalar dependencias
* cd ~/api_persons/ y correr el comando: manage.py makemigrations
* correr el comando: manage.py migrate
* correr el comando: manage.py createsuperuser
* por ultimo levantamos el server: manage.py runserver
* a jugar!

## Si usas... PyCharm
* abrir el proyecto con PyCharm
* instalar dependencias
* ir a Terminal cd ~/api-persons y correr el comando: manage.py makemigrations
* correr el comando: manage.py migrate
* correr el comando: manage.py createsuperuser
* correr el comando: manage.py runserver
* configurar Django: runserver (opcional)

![Django Runserver](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/runserver.jpg "run server")


## API Personas
* [API-Personas](http://gguzman.challenge.trinom.io/api/documentation)

## Agregar persona

![POST Persona](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/post-before.png "post before")
![POST2 Persona](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/post-created.png "post after")

## Modificar persona | Asociar curso-persona

![PUT Persona](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/put-before.png "put before")
![PUT2 Persona](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/put-ok.png "put after")

## Eliminar persona

![DELETE Persona](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/delete-before.png "delete before")
![DELETE2 Persona](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/delete-instance.png "delete instance")
![DELETE3 Persona](https://github.com/gguzman89/challenge-tri/blob/develop/screenshot/delete-after.png "delete after")

