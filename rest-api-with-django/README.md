# REST API con Django

## Proceso de Instalación
1. Crea un ambiente virtual:
```
python3 -m venv env
```
2. Activa el ambiente virtual:
```
# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate
```
3. Instala Django:
```
pip install django
```
4. Crea un nuevo proyecto en Django:
```
django-admin startproject shopping_cart
```
5. Crea una nueva aplicación en Django:
```
cd shopping_cart
python manage.py startapp api
```
6. Agrega esta aplicación en el archivo de `settings.py`:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api'
]
```
7. Genera las migraciones y ejeculatas:
```
python manage.py makemigrations
python manage.py migrate 
```
8. Crea un super usuario:
```
python manage.py createsuperuser
```
9. Corre la aplicación:
```
python manage.py runserver
```
### Probando nuestra API

Para probar nuestra REST API vamos a usar Postman para hacer peticiones a nuestra API, descargala [aquí.](https://www.postman.com/downloads/)

Abre postman e importa la colección que esta en el repositorio.
