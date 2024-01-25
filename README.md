# Django-REST-CRUD

git clone project 

go inside the folder

pip install virtualenv

python -m venv venv

.\venv\Scripts\activate

pip install django 

pip install djangorestframework

django-admin startproject simple_crud_app

in root application CRUD_Application in setting.py in installed apps add rest_framework and simple_crud_app

also update database object

add model class in models.py for me it is users

python manage.py makemigrations

python manage.py migrate



database-link
jdbc:sqlite:C:\Users\abdur\OneDrive\Documents\cruddatabase.sqlite
