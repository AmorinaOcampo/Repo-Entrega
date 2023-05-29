from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Cliente, Pais, Ciudad


def index(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    return render(request, "cliente/index.html", contexto)


def crear_clientes_predeterminados(request):
    from datetime import date

    # Crear instancias de países
    p1 = Pais.objects.create(nombre="Argentina")
    p2 = Pais.objects.create(nombre="Chile")
    p3 = Pais.objects.create(nombre="Uruguay")

    # Crear instancias de ciudades
    c1 = Ciudad.objects.create(nombre="Santa Fe")
    c2 = Ciudad.objects.create(nombre="Santiago de Chile")
    c4 = Ciudad.objects.create(nombre="Montevideo")

    # Crear instancias de clientes
    Cliente.objects.create(nombre="Amorina", apellido="Ocampo", nacimiento=date(2001, 9, 24), pais_origen_id=p1, ciudad_residencia=c1)
    Cliente.objects.create(nombre="Gonzalo", apellido="Pomero", nacimiento=date(2005, 6, 9), pais_origen_id=p2, ciudad_residencia=c2)
    Cliente.objects.create(nombre="Amparo", apellido="Pizzi", nacimiento=date(2001, 9, 20), pais_origen_id=p3, ciudad_residencia=None)
    Cliente.objects.create(nombre="Santiago", apellido="Macagno", nacimiento=date(1999, 1, 7), pais_origen_id=None, ciudad_residencia=c4)

    # url = reverse("cliente:index")
    return redirect("cliente:index")


def prueba_búsqueda(request):
    from datetime import date

    # Búsqueda por país de origen vacío
    clientes_pais = Cliente.objects.filter(pais_origen_id=None)

    # Búsqueda por ciudad de residencia vacío
    clientes_ciudad = Cliente.objects.filter(ciudad_residencia=None)

    contexto = {
        "clientes_pais": clientes_pais,
        "clientes_ciudad": clientes_ciudad
    }
    return render(request, "cliente/resultados_busqueda.html", contexto)


def crear_cliente(request):
    from .form import ClienteForm

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("cliente:index"))
    else:  # method == "GET"
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})
