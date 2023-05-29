from django import forms

from .models import Ventas

class VentaForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ["producto", "cantidad"]