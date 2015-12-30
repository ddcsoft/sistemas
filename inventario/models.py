from django.db import models
from django.conf import settings
# Create your models here.



# Create your models here.
class EstadoArticulo(models.Model):
	descripcion = models.CharField(max_length=50)
	
	def __str__(self):
		return self.descripcion

class Empresa(models.Model):
	descripcion = models.CharField(max_length=100)

	def __str__(self):
		return self.descripcion

class TipoArticulo(models.Model):
	descripcion=models.CharField(max_length=150)

	def __str__(self):
		return self.descripcion

class Marca(models.Model):
	descripcion = models.CharField(max_length=150)

	def __str__(self):
		return self.descripcion

class Clasificacion(models.Model):
	descripcion = models.CharField(max_length=150)

	def __str__(self):
		return self.descripcion


class Articulo(models.Model):
	codigo = models.CharField(max_length=10)
	descripcion=models.CharField(max_length=150)
	modelo = models.CharField(max_length=150)
	serie = models.CharField(max_length=100)
	comentario = models.CharField(max_length=300)
	medida = models.CharField(max_length=50)
	estado = models.ForeignKey(EstadoArticulo)
	empresa = models.ForeignKey(Empresa)
	tipo = models.ForeignKey(TipoArticulo)
	marca = models.ForeignKey(Marca)
	clasificacion = models.ForeignKey(Clasificacion)
	registradoPor = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __str__(self):
		return self.descripcion

class TipoMvto(models.Model):
	descripcion =  models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion

class Empleado(models.Model):
	nombre = models.CharField(max_length=50)
	apellidoP = models.CharField(max_length=50)
	apellidoM = models.CharField(max_length=50,null=True,blank=True)
	def __str__(self):
		return "%s %s %s"%(self.nombre,self.apellidoP, self.apellidoM)

class Puesto(models.Model):
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion
	
class Movimiento(models.Model):
	fecha_registro = models.DateField()
	fecha_Mvto = models.DateField()
	Comentario = models.CharField(max_length=200)
	registradoPor = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="Reg_Mvto",)
	responsable = models.ForeignKey(Empleado)
	def __str__(self):
		return self.Comentario

class Ubicacion(models.Model):
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion

class Detalle_Movimiento(models.Model):
	ubicacion_incial = models.ForeignKey(Ubicacion,related_name="Ini_Mvto",)
	ubicacion_final =  models.ForeignKey(Ubicacion,related_name="Fin_Mvto",)
	

class Ubicacion_Articulo(models.Model):
	articulo = models.ForeignKey(Articulo)
	ubicacion = models.ForeignKey(Ubicacion)
	movimiento = models.ForeignKey(Movimiento)
