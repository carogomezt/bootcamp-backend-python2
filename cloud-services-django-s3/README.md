# Integración de Servicios Cloud con Django (S3)

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
pip install django boto3 django-storages python-dotenv
```
4. Crea un nuevo proyecto en Django:
```
django-admin startproject cloudbox
```
5. Crea una nueva aplicación en Django:
```
cd cloudbox
python manage.py startapp documents
```
6. Crea un archivo `.env` con el siguiente contenido en el root del proyecto:
```
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=your-region  # e.g., us-west-1
```
6. Agrega las siguientes lineas al final de INSTALLED_APPS en el archivo de `settings.py`:
```
INSTALLED_APPS = [
    ...
    'documents',
    'storages'
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

### Servicio Cloud
1. Crea una cuenta en [AWS](https://aws.amazon.com/es/).
2. Crea un bucket en [S3](https://s3.console.aws.amazon.com/s3).
    - Bucket Name: documents-django-bucket
    - Region: us-east-1
3. Crea un [IAM User](https://console.aws.amazon.com/iam/).
    - Click `Users` → `Create user`
    - User Name: `django-s3-user`
    - `Attach policies directly` → `AmazonS3FullAccess`
    - Abre el usuario y Crea llaves de acceso dando click en `Create access key`
    - Descarga el archivo con las llaves de acceso.

### Probando nuestra API

Para probar nuestra REST API vamos a usar Postman para hacer peticiones a nuestra API, descargala [aquí.](https://www.postman.com/downloads/)

Abre postman e importa la colección que esta en el repositorio.