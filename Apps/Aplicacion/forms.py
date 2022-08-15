
from dataclasses import fields
from django import forms

from .models import Cliente
from .models import Producto
from .models import Proveedor
from django.contrib.auth.forms import UserCreationForm


class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class FormularioProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"


