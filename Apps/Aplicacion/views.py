from warnings import catch_warnings
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User as usuarios

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail

import os
import copy
# Create your views here.

from .forms import FormularioCliente
from .forms import FormularioProducto
from .forms import FormularioProveedor 


from .models import Cliente
from .models import Producto
from .models import Cuenta
from .models import Proveedor


def PaginaInicio(request):
    return render(request, 'index.html', {})

def VistaPrincipal(request):
    return render(request, 'VistaPrincipal/VistaPrincipal.html', {})

def CorreoElectronico(request):
    if(request.method == 'POST'):
        pass


class VistaProductos(HttpRequest):
    def listarProductos(request):
        productos = Producto.objects.all()
        return render(request, "Producto/Productos.html",{"productos":productos})
    
    def informacionProducto(request,id):
        producto = Producto.objects.get(pk=id)
        return render(request, "Producto/InformacionProducto.html", {"producto":producto})
    
    def cancelarProductos(request):
        return render(request, "Compra/PagarCompra.html", {})

def CarritoCompra(request):
    return render(request, "Compra/CarritoCompra.html",{})

def CrearCuenta(request):
    return render(request, "Login/Signup.html",{})

def check_admin(user):
   return user.is_superuser

@user_passes_test(check_admin)
def Administrador(request):
    return render(request, "Administrador/AdministradorVentana.html",{})

def Login(request):
    if(request.method == "POST"):
        bandera = False
        User = request.POST['username']
        Pass = request.POST['password']
        cuentas = Cuenta.objects.all()
        clientes = Cliente.objects.all()
        cuentaDatos = Cuenta()
        user = authenticate(request,username = User, password = Pass)
        if user is not None:
            for cuenta in cuentas:
                if(user.username == User):
                    cuentaDatos = copy.copy(cuenta)
                    bandera = True

            clienteCuenta = Cliente()

            for cliente in clientes:
                if(cliente.nombreUsuario == cuentaDatos.usuario):
                    clienteCuenta = copy.copy(cliente)

        if bandera :
            login(request,user)
            print("Ingresaste")
            print(user)
            return render(request, "index.html",{"cuenta" : user,"cliente" : clienteCuenta})
        else : 
            messages.success(request,("Hubo un problema al ingresar"))
            return render(request, "Login/Login.html",{})
    else :
        return render(request, "Login/Login.html",{})

def RegistrarCliente(request):
    if(request.method == "POST"):
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        nombreUsuario = request.POST['nombreusuario']
        password = request.POST['password']
        email = request.POST['email']
        domicilio = request.POST['domicilio']
        telefono = request.POST['telefono']

        cliente = Cliente()
        cuenta = Cuenta()

        cliente.nombres = nombres
        cliente.apellidos = apellidos
        cliente.nombreUsuario = nombreUsuario
        cliente.password = password
        cliente.email = email
        cliente.domicilio = domicilio
        cliente.telefono = telefono

        cuenta.usuario = nombreUsuario
        cuenta.password = password

        cuenta.save()
        cliente.save()

        return render(request, "Login/Login.html",{})
    else:
        return render(request, "Login/Signup.html",{})


def LogOut(request):
    logout(request)
    print("saliste")
    return redirect("index")

class GestionarProducto(HttpRequest):
    @user_passes_test(check_admin)
    def procesar_producto(request):
        producto = FormularioProducto()
        productos = Producto.objects.all()
        if request.method == "POST":
            formulario = FormularioProducto(request.POST,request.FILES)
            if formulario.is_valid():
                formulario.save()
                print("Ingreso")
            else:
                print("Error algo paso")
        return render(request, "Administrador/AdministrarProductos.html",{"form":producto, "productos":productos})
    @user_passes_test(check_admin)
    def editar_producto(request,id):
        producto = Producto.objects.get(pk=id)
        form = FormularioProducto(instance=producto)
        return render(request, "Administrador/EditarProducto.html",{"form":form, "producto":producto})
    @user_passes_test(check_admin)
    def actualizar_producto(request,id):
        producto = Producto.objects.get(pk=id)
        formulario = FormularioProducto(request.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administradorProductos")
    @user_passes_test(check_admin)
    def eliminar_producto(request,id):
        producto = Producto.objects.get(pk=id)
        producto.delete()
        return redirect(to="administradorProductos")

@user_passes_test(check_admin)
class GestionarProveedor(HttpRequest):
    @user_passes_test(check_admin)
    def procesar_proveedor(request):
        proveedor = FormularioProveedor()
        proveedores = Proveedor.objects.all()
        #print(proveedores," asdas")
        if request.method == 'POST':
            formulario = FormularioProveedor(data=request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request,"Administrador/AdministrarProveedor.html",{"form":proveedor,"proveedores":proveedores})
    @user_passes_test(check_admin)
    def editar_proveedor(request,id):
        proveedor = Proveedor.objects.get(id=id)
        form = FormularioProveedor(instance=proveedor)
        return render(request, "Administrador/EditarProveedor.html",{"form":form, "proveedor":proveedor})
    @user_passes_test(check_admin)
    def actualizar_proveedor(request,id):
        proveedor = Proveedor.objects.get(pk=id)
        formulario = FormularioProveedor(request.POST,instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarProveedores")
    @user_passes_test(check_admin)
    def eliminar_proveedor(request,id):
        proveedor = Proveedor.objects.get(pk=id)
        proveedor.delete()
        return redirect(to="administrarProveedores")
        

@user_passes_test(check_admin)
class GestionarCliente(HttpRequest):
    @user_passes_test(check_admin)
    def procesar_cliente(request):
        cliente = FormularioCliente()
        clientes = Cliente.objects.all()
        if request.method == "POST":
            formulario = FormularioCliente(data = request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request, "Administrador/AdministrarClientes.html",{"form":cliente, "clientes":clientes})
    @user_passes_test(check_admin)
    def editar_cliente(request,id):
        cliente = Cliente.objects.get(id=id)
        form = FormularioCliente(instance=cliente)
        return render(request, "Administrador/EditarCliente.html",{"form":form, "cliente":cliente})
    @user_passes_test(check_admin)
    def actualizar_cliente(request,id):
        cliente = Cliente.objects.get(pk=id)
        formulario = FormularioCliente(request.POST,instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarClientes")
    @user_passes_test(check_admin)
    def eliminar_cliente(request,id):
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
        return redirect(to="administrarClientes")
        
