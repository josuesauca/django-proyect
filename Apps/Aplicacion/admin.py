from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(CarritoCompras)
admin.site.register(OrdenCompra)
admin.site.register(Factura)
admin.site.register(TarjetaCredito)