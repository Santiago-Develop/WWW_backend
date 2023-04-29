from django.db import models

# Create your models here.

class Ciudad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, blank = False, null = False)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    direccion = models.CharField(max_length = 100, blank = False, null = False)
    email = models.EmailField(max_length = 100, blank = False, null = False)
    telefono = models.IntegerField(blank = False, null = False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    
class Mensajero(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    direccion = models.CharField(max_length = 100, blank = False, null = False)
    email = models.EmailField(max_length = 100, blank = False, null = False)
    telefono = models.IntegerField(blank = False, null = False)
    cliente_id = models.ManyToManyField(Cliente)
    
    class Meta:
        verbose_name = "Mensajero"
        verbose_name_plural = "Mensajeros"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
    
class Sucursal(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    direccion = models.CharField(max_length = 100, blank = False, null = False)
    telefono = models.IntegerField(blank = False, null = False)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre