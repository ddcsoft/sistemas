from django.db import models
from django.conf import settings
# Create your models here.



# Create your models here.
class EstadoArticulo(models.Model):
	descripcion = models.CharField(max_length=50)
	class Meta:
		ordering = ["descripcion"]
	
	def __str__(self):
		return self.descripcion

class Empresa(models.Model):
	descripcion = models.CharField(max_length=100)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return self.descripcion

class Area(models.Model):
	descripcion=models.CharField(max_length=100)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return self.descripcion


class TipoArticulo(models.Model):
	descripcion=models.CharField(max_length=150)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return self.descripcion

class Marca(models.Model):
	descripcion = models.CharField(max_length=150)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return self.descripcion


class Clasificacion(models.Model):
	descripcion = models.CharField(max_length=150)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return self.descripcion


class Articulo(models.Model):
	codigo = models.CharField(max_length=10,unique=True)
	descripcion=models.CharField(max_length=150)
	modelo = models.CharField(max_length=150)
	serie = models.CharField(max_length=100,unique=True)
	comentario = models.CharField(max_length=300,null=True,blank=True)
	medida = models.CharField(max_length=50,null=True,blank=True)
	estado = models.ForeignKey(EstadoArticulo)
	empresa = models.ForeignKey(Empresa)
	tipo = models.ForeignKey(TipoArticulo)
	marca = models.ForeignKey(Marca)
	clasificacion = models.ForeignKey(Clasificacion)
	registradoPor = models.ForeignKey(settings.AUTH_USER_MODEL)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return "%s-%s-%s"%(self.descripcion,self.serie,self.codigo)

class TipoMvto(models.Model):
	descripcion =  models.CharField(max_length=100)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return self.descripcion

class Empleado(models.Model):
	nombre = models.CharField(max_length=50)
	apellidoP = models.CharField(max_length=50)
	apellidoM = models.CharField(max_length=50,null=True,blank=True)
	empresa = models.ForeignKey(Empresa)
	area = models.ForeignKey(Area)
	class Meta:
		ordering = ["nombre"]

	def __str__(self):
		return "%s %s-%s"%(self.nombre,self.apellidoP, self.empresa)

class Puesto(models.Model):
	descripcion = models.CharField(max_length=100)
	empresa = models.ForeignKey(Empresa)
	area = models.ForeignKey(Area)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return "%s-%s-%s"%(self.descripcion,self.area,self.empresa)

class Ubicacion(models.Model):
	descripcion = models.CharField(max_length=100)
	class Meta:
		ordering = ["descripcion"]

	def __str__(self):
		return self.descripcion

class Movimiento(models.Model):
	fecha_registro = models.DateField()
	fecha_Mvto = models.DateField()
	fecha_Retorno = models.DateField(null=True,blank=True)
	Comentario = models.CharField(max_length=200)
	responsable = models.ForeignKey(Empleado)
	tipomvto = models.ForeignKey(TipoMvto)
	ubicacion =  models.ForeignKey(Ubicacion)
	puesto = models.ForeignKey(Puesto,null = True, blank=True)
	registradoPor = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="Reg_Mvto",)

	def __str__(self):
		return self.Comentario


class Detalle_Movimiento(models.Model):
	movimiento = models.ForeignKey(Movimiento)
	articulo = models.ForeignKey(Articulo)
	
	

class Ubicacion_Articulo(models.Model):
	articulo = models.ForeignKey(Articulo)
	ubicacion = models.ForeignKey(Ubicacion)
	movimiento = models.ForeignKey(Movimiento)
