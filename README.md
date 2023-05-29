# Repo-Entrega

## Tercer entrega curso Python

Pasos para la creación del proyecto

`git clone https://github.com/AmorinaOcampo/Repo-Entrega.git`
> Clona el repositorio creado en GitHub

`python -m venv entornov`
> Crea el entorno virtual
> Luego se activa el entorno virtual desde VSC

`pip install django`
> Installa Django

`pip list`
> Visualizamos los paquetes instalados en el repositorio
> Aseguramos tener Django instalado

`django-admin startproject proyectoTercerE`
> Crea un proyecto llamado proyectoTercerE en el directorio proyecto

`python manage.py runserver`
> Ejecuta el servidor

`python manage.py startapp cliente`
> Crea una aplicacion llamada cliente dentro del directorio apps

`python manage.py startapp venta`
> Crea una aplicacion llamada venta dentro del directorio apps