from django.urls import path

from .views import crear_venta, index, prueba_búsqueda, crear_ventas_predeterminadas

app_name = "venta"

urlpatterns = [
    path("", index, name="index"),
    path("crear-ventas-predeterminadas/", crear_ventas_predeterminadas, name="crear-ventas"),
    path("prueba-búsqueda/", prueba_búsqueda, name="prueba-búsqueda"),
    path("crear/", crear_venta, name="crear"),
]