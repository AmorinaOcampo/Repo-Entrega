from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Ventas(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.producto}'

