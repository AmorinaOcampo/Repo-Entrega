from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Ventas, Producto

# Create your views here.
def index(request):
    ventas_registradas = Ventas.objects.all()
    contexto = {"ventas": ventas_registradas}
    return render(request, "venta/index.html", contexto)

def crear_ventas_predeterminadas(request):

    # Crear instancias de producto
    p1 = Producto.objects.create(nombre="Taza Cala")
    p2 = Producto.objects.create(nombre="Mate Jacinto")
    p3 = Producto.objects.create(nombre="Tazón Aurora")

    # Crear instancias de ventas
    Ventas.objects.create(producto=p1, cantidad=2)
    Ventas.objects.create(producto=p2, cantidad=1)
    Ventas.objects.create(producto=p3, cantidad=2)

    return redirect("venta:index")

def prueba_búsqueda(request):
    from datetime import date

    # Búsqueda por ventas de dos cantidades de productos
    venta_cantidad = Ventas.objects.filter(cantidad=2)

    contexto = {
        "venta_cantidad": venta_cantidad
    }
    return render(request, "venta/resultados_busqueda.html", contexto)


def crear_venta(request):
    from .form import VentaForm

    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("venta:index"))
    else:  # method == "GET"
        form = VentaForm()
    return render(request, "venta/crear.html", {"form": form})

