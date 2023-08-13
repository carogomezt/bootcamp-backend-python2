# Bases de Datos en Flask

## Proceso de Instalación
1. [Instala MySQL](https://dev.mysql.com/downloads/)
2. Crea un ambiente virtual:
```
python3 -m venv env
```
3. Activa el ambiente virtual:
```
# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate
```
4. Instala los requerimientos del proyecto:
```
pip install -r requirements.txt
```
5. Copia las variables de entorno:
```commandline
cp .env.example .env
```
6. Conectate en una nueva terminal y abre la consola de MySQL:
```
mysql -u root -p
```
6. Crea una base de datos para nuestro proyecto:
```sql
CREATE DATABASE store;
```
5. Abre una nueva terminal en tu proyecto y corre tu aplicación:
```
flask run --debug
```
