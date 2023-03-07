"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static


import sys

sys.path.append("..")

import Apps.Aplicacion.views as vista

urlpatterns = [
    path('admin/', admin.site.urls),

    path('vistaPrincipal/', vista.VistaPrincipal,name='vistaPrincipal'),

    path('productos/', vista.VistaProductos.listarProductos,name='productos'),
    path('carritoCompra/', vista.CarritoCompra,name='carritoCompra'),
    path('informacionProducto/<int:id>', vista.VistaProductos.informacionProducto,name='informacionProducto'),


    path('login/', vista.Login,name='login'),
    path('logout/', vista.LogOut,name='logout'),
    path('crearCuenta/', vista.CrearCuenta,name='crearCuenta'),

    path('administrador/',vista.Administrador,name='administrador'),

    #Navbar Principal

    path('ingresarCliente/', vista.RegistrarCliente ,name='ingresarCliente'),



    #Fin Navbar

    #Administrador Rutas
    path('administrarClientes/', vista.GestionarCliente.procesar_cliente ,name='administrarClientes'),
    path('editarCliente/<int:id>', vista.GestionarCliente.editar_cliente ,name='editarCliente'),
    path('actualizarCliente/<int:id>', vista.GestionarCliente.actualizar_cliente ,name='actualizarCliente'),
    path('eliminarCliente/<int:id>', vista.GestionarCliente.eliminar_cliente, name = "eliminarCliente"),


    path('administradorProductos/', vista.GestionarProducto.procesar_producto ,name='administradorProductos'),
    path('editarProducto/<int:id>', vista.GestionarProducto.editar_producto ,name='editarProducto'),
    path('actualizarProducto/<int:id>', vista.GestionarProducto.actualizar_producto ,name='actualizarProducto'),
    path('eliminarProducto/<int:id>', vista.GestionarProducto.eliminar_producto, name = "eliminarProducto"),


    path('administrarProveedores/', vista.GestionarProveedor.procesar_proveedor ,name='administrarProveedores'),
    path('editarProveedor/<int:id>', vista.GestionarProveedor.editar_proveedor ,name='editarProveedor'),
    path('actualizarProveedor/<int:id>', vista.GestionarProveedor.actualizar_proveedor ,name='actualizarProveedor'),
    path('eliminarProveedor/<int:id>', vista.GestionarProveedor.eliminar_proveedor, name = "eliminarProveedor"),


    path('productos/', vista.VistaProductos.listarProductos,name='productos'),
    path('compra/', vista.VistaProductos.cancelarProductos,name='compra'),

    ################################################################
    path('agregarProducto/',vista.AgregarProductoAjax,name='agregarProducto'),
    path('eliminarProductoAjax/',vista.EliminarProductoAjax,name='eliminarProductoAjax'),



    path('pagarCompra/',vista.PagarCompra,name='pagarCompra'),
     
    #Fin Rutas Administradors

    path('', vista.PaginaInicio, name="index"),

]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)