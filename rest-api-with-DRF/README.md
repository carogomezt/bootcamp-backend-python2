# REST API con Django REST Framework

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
3. Instala Django y DRF:
```
pip install django
pip install djangorestframework
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
6. Agrega la aplicación de `rest_framework` y la que acabamos de crear en el archivo de `settings.py`:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
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
10. Para probar nuestra REST API vamos a usar Postman para hacer peticiones a nuestra API, descargala [aquí.](https://www.postman.com/downloads/)
11. Ejemplo de peticion para agregar productos:
```commandline
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"
```
12. URL de nuestra API: http://127.0.0.1:8000/api/cart-items/
12. Ejemplo de peticion para obtener productos:
```commandline
curl -X GET http://127.0.0.1:8000/api/cart-items/
```
13. Ejemplo de peticion para modificar productos:
```commandline
curl -X PATCH http://127.0.0.1:8000/api/cart-items/1 -H 'Content-Type: application/json' -d '{"product_quantity":6}'
```
14. Ejemplo de peticion para borrar un producto:
```commandline
curl -X "DELETE" http://127.0.0.1:8000/api/cart-items/1
```

_Ejemplo base tomado de: [Creating a REST API with Django REST Framework](https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/)_
