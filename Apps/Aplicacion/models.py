from django.db import models
# Create your models here.

from django.contrib.auth.models import User


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    #idAdministrador = models.ForeignKey(Administrador, null=True,on_delete=models.CASCADE)
    
    """
    idSuministrar = models.ManyToManyField(
        Producto,
        through="Suministrar"
    )
    """

    nombres = models.CharField(max_length=20,null=True)
    direccion = models.CharField(max_length=30,null=True)
    pais = models.CharField(max_length=15,null=True)
    cuidad = models.CharField(max_length=15,null=True)
    ruc = models.DecimalField(max_digits=13,decimal_places=0,null=True) 
    email = models.CharField(max_length=20,null=True) 
    telefono = models.DecimalField(max_digits=13,decimal_places=0,null=True)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    idProveedor = models.ForeignKey(Proveedor, null=True,on_delete=models.CASCADE)

    nombre = models.CharField(max_length=15,null=True)
    precio = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 
    marca = models.CharField(max_length=20,null=True) 
    cantidad = models.IntegerField(null=True) 
    imagenProducto = models.ImageField(upload_to= "imagenes/", null=True)
    informacion = models.CharField(max_length=200,null=True) 

    def __str__(self):
        return f"Producto : {self.id} , {self.nombre} , {self.precio} , {self.marca} , {self.cantidad} "


class OrdenItem(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto,null=True,on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)
class CarritoCompras(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    productos = models.ManyToManyField(Producto,null=True)
    total_pagar = models.DecimalField(max_digits=6, decimal_places=2, null=True)



class OrdenCompra(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    idCarritoCompras = models.ForeignKey(CarritoCompras,null=True,on_delete=models.CASCADE)

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    idOrdenCompra = models.OneToOneField(OrdenCompra,null=True, on_delete=models.CASCADE)

    numeroFactura = models.CharField(max_length=10,null=True)
    fechaFactura = models.DateField(null=True)
    subtotal = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 
    totalPagar = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 