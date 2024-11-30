from django.db import models

class Cliente(models.Model):
    
    primer_nombre = models.CharField(max_length=30, null=False)
    segundo_nombre = models.CharField(max_length=30, null=False)
    primer_apellido = models.CharField(max_length=30, null=False)
    segundo_apellido = models.CharField(max_length=30, null=False)
    numero_cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField(null=False)
    correo = models.EmailField(max_length=50, unique=True)
    numero_telefono = models.CharField(max_length=15)
    pais = models.CharField(max_length=30, null=False)
    GENERO = [
        ("Femenino", "Femenino"),
        ("Masculino", "Masculino"),
    ]
    genero = models.CharField(max_length=30, choices=GENERO, null=False)
    direccion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.primer_nombre} {self.primer_apellido}'


class Categoria(models.Model):
    CATEGORIAS_CHOICES = [
        ('Alimentos', 'Alimentos'),
        ('Vestimenta', 'Vestimenta'),
        ('Decoracion', 'Decoración'),
        ('Textiles', 'Textiles'),
        ('Bisuteria', 'Bisutería'),
    ]
    categorias = models.CharField(max_length=50, choices=CATEGORIAS_CHOICES)
   
    def __str__(self):
        return self.categorias  


class Emprendimiento(models.Model):
    nombre_emprendimiento = models.CharField(max_length=100, unique=True)
    categorias = models.ManyToManyField('Categoria') 
    numero_telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    propietaro = models.CharField(max_length=100, null=True, blank=True) 
    logo_emprendimiento = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return self.nombre_emprendimiento
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    emprendimiento = models.ForeignKey('Emprendimiento', on_delete=models.CASCADE)
    imagen_producto = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre_producto

class Tipopago(models.Model):
    
    nombre_pago = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.nombre_pago}'


class PerfilesUsuarios(models.Model):
    nombre_perfil = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.nombre_perfil}'

 



