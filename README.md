# Repo-Entrega

## Tercer entrega curso Python

# Pasos para la creación del proyecto

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

# Funcionalidades
Creé una plantilla (templates) general y dentro de los directorios cliente y venta también creé sus respectivas plantillas.

En la aplicación cliente, creé tres clases en models (Pais, Ciudad, Cliente).
En la aplicación venta, creé dos clases en models (Producto, Venta).

Como funciones para ambas aplicaciones definí: index, crear_clientes/ventas_predeterminadas, prueba_búsquedad, crear_cliente/venta.
Además para la app venta creé la funcion cantidad_ventas_totales.

Creé un archivo form.py en ambos directorios (cliente y venta), para crear formularios que me permitan agregar datos a los modelos directamente desde la web.
