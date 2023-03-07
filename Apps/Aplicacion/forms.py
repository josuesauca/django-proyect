
from dataclasses import fields
from django import forms

from .models import Producto
from .models import Proveedor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class FormularioProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"

class FormularioUsuarios(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(FormularioUsuarios, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None