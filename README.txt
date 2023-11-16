# Der virtueller Umbkreis wird erstellt
python -m venv venv 


# Der virtueler Umkreis wird aktiviert
venv\scripts\activate


# Der Paket-Manager wird geupgradet
python -m pip install --upgrade pip


# Framework Django wird installiert
pip install django


# Das Projekt Djungo wird erschaffen
django-admin startproject store_project


# wir gehen in die mappe projekt rüber
cd store_project


# eine App wird erschaffen
python manage.py startapp store 


# wir erschaffen die hilfs tabellen in der datenbank
python manage.py migrate 


# server wird gestartet
python manage.py runserver


#bei Veränderung des Aufbaus von Basen
python manage.py makemigrations
python manage.py migrate


#Admin wird registriert
python manage.py createsuperuser


bei arbeit mit grafiken
pip install pillow 

#acc 
Rustam
277353