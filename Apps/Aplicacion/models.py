from django.db import models
# Create your models here.

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=15,null=True)
    password = models.CharField(max_length=15,null=True)
    

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)

    nombres = models.CharField(max_length=25,null=True)
    apellidos = models.CharField(max_length=25,null=True) 
    nombreUsuario = models.CharField(max_length=20,null=True) 
    password = models.CharField(max_length=20,null=True) 
    email = models.EmailField(max_length=20,null=True) 
    domicilio= models.CharField(max_length=15,null=True) 
    telefono= models.DecimalField(max_digits=13,decimal_places=0,null=True) 

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    idCuenta = models.OneToOneField(Cuenta, on_delete= models.CASCADE, null=True)

    nombre = models.CharField(max_length=15,null=True)
    apellidos = models.CharField(max_length=15,null=True) 
    contacto = models.CharField(max_length=15,null=True) 
    email = models.EmailField(max_length=20,null=True) 
    
class CarritoCompras(models.Model):
    id = models.AutoField(primary_key=True)
    idCliente = models.OneToOneField(Cliente,on_delete=models.CASCADE,null=True)
    prueba = models.DecimalField(max_digits= 7,decimal_places=0,null=True) 





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

"""
class Suministrar(models.Model):    
    idProveedor = models.ForeignKey(Producto,on_delete=models.CASCADE,null=True)
    idProducto = models.ForeignKey(Proveedor,on_delete= models.CASCADE, null=True)

"""

class OrdenCompra(models.Model):
    id = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, null=True,on_delete=models.CASCADE)
    prueba = models.DecimalField(max_digits= 7,decimal_places=0,null=True) 

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    idOrdenCompra = models.OneToOneField(OrdenCompra,null=True, on_delete=models.CASCADE)

    numeroFactura = models.CharField(max_length=10,null=True)
    fechaFactura = models.DateField(null=True)
    subtotal = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 
    totalPagar = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 

class TarjetaCredito(models.Model):
    id = models.AutoField(primary_key=True)
    numeroTarjeta= models.CharField(max_length=10,null=True)
    fechaCreacion= models.DateField(null=True)
    fechaExpiracion= models.DateField(null=True)