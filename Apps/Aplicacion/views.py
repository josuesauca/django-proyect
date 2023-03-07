from warnings import catch_warnings
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_protect


import os
import copy
# Create your views here.

from .forms import FormularioProducto
from .forms import FormularioProveedor
from .forms import FormularioUsuarios


from .models import Producto
from .models import Proveedor
from .models import CarritoCompras


def PaginaInicio(request):
    return render(request, 'index.html', {})


def VistaPrincipal(request):
    return render(request, 'VistaPrincipal/VistaPrincipal.html', {})


class VistaProductos(HttpRequest):
    def listarProductos(request):
        productos = Producto.objects.all()
        return render(request, "Producto/Productos.html", {"productos": productos})

    def informacionProducto(request, id):
        producto = Producto.objects.get(pk=id)
        return render(request, "Producto/InformacionProducto.html", {"producto": producto})

    def cancelarProductos(request):
        return render(request, "Compra/PagarCompra.html", {})


def CarritoCompra(request):

    productos = Producto.objects.all()
    total_productos = []

    for item in productos:
        total_productos.append(item.id)

    cantidad_items = CarritoCompras.objects.filter(idUsuario=request.user).filter(productos__in=total_productos).count()
    ids_productos = CarritoCompras.objects.filter(idUsuario=request.user).filter(productos__in=total_productos).values('productos')
    lista_ids = []

    for item in ids_productos:
        lista_ids.append(item['productos'])
    
    productos_filtrados = Producto.objects.filter(id__in=lista_ids).values()
    print(type(productos_filtrados))

    return render(request, "Compra/CarritoCompra.html",{"cantidad_items":cantidad_items,"lista_imagenes":productos_filtrados})

def PagarCompra(request):
    if(request.method == "GET"):
        carritoUsuario = CarritoCompras.objects.filter(idUsuario = request.user)
        
        pass

    return render(request, "Compra/PagarCompra.html", {})

@csrf_protect
def AgregarProductoAjax(request):
    if(request.method =="POST"):
        try:
            datos = dict(request.POST)
            id = datos.get('producto')
            id = int(id[0])

            productos = Producto.objects.all()
            total_productos = []

            for item in productos:
                total_productos.append(item.id)

            usuario = CarritoCompras.objects.filter(idUsuario=request.user)

            lista_productos = []

            if usuario:
                lista_compras = list(CarritoCompras.objects.filter(idUsuario=request.user).filter(productos__in=total_productos).values('productos'))

                for item in lista_compras:
                    lista_productos.append(item['productos'])

                lista_productos.append(id)
                usuario = usuario.first()
                usuario.productos.set(lista_productos)
                usuario.save()
            else:
                nuevo_carrito = CarritoCompras.objects.create(idUsuario=request.user)
                nuevo_carrito.productos.set(id) 
                nuevo_carrito.save()

        except Exception as e:
            print("exeptcoopm ",e)

    productos = Producto.objects.all()
    return render(request, "Producto/Productos.html",{"productos":productos})


@user_passes_test
@csrf_protect
def EliminarProductoAjax(request):
    if (request.method == 'POST'):
        pass
    

def CrearCuenta(request):
    print (request.GET)
    return render(request, "Login/Signup.html",{})

def check_admin(user):
   return user.is_superuser

@user_passes_test(check_admin)
def Administrador(request):
    return render(request, "Administrador/AdministradorVentana.html",{})

def Login(request):
    if(request.method == "POST"):
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])

        if user is None:
            return redirect("login")
        else:
            login(request, user)
            return redirect("index")
    else :
        return render(request, "Login/Login.html",{})

def RegistrarCliente(request):
    if(request.method == "POST"):

        if request.POST["password1"] == request.POST["password2"]:
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            user = User.objects.create_user(
                        username=username, password=password1, email=email,first_name=first_name,last_name=last_name)

            user.save()
            login(request, user)
        return redirect("index")
    else:
        return render(request, "Login/Signup.html",{})


def LogOut(request):
    logout(request)
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
        # print(proveedores," asdas")
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

        
        clientes = User.objects.all()
        cliente = FormularioUsuarios()

        # print(request)

        if request.method == "POST":
            formulario = FormularioUsuarios(data = request.POST)
            # print(formulario)
            if formulario.is_valid():
                print("entra")
                formulario.save()
        return render(request, "Administrador/AdministrarClientes.html",{"form":cliente, "clientes":clientes})


    @user_passes_test(check_admin)
    def editar_cliente(request,id):
        # cliente = Cliente.objects.get(id=id)
        # form = FormularioCliente(instance=cliente)

        cliente = User.objects.get(id=id)
        form = FormularioUsuarios(instance=cliente)

        return render(request, "Administrador/EditarCliente.html",{"form":form, "cliente":cliente})
    
    @user_passes_test(check_admin)
    def actualizar_cliente(request,id):

        # cliente = Cliente.objects.get(pk=id)
        # formulario = FormularioCliente(request.POST,instance=cliente)

        cliente = User.objects.get(pk=id)
        formulario = FormularioUsuarios(request.POST,instance=cliente)
        print (formulario)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarClientes")
        return redirect(to="administrarClientes")
        

    @user_passes_test(check_admin)
    def eliminar_cliente(request,id):
        # cliente = Cliente.objects.get(pk=id)
        cliente = User.objects.get(pk=id)
        cliente.delete()
        return redirect(to="administrarClientes")
        
