from django import forms
from .models import MetodoPago

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = [
            'colegio',
            'nombre',
            'descripcion',
        ]

        labels = {
            'colegio' : 'Colegio',
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
        }