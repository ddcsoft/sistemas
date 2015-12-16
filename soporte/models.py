from django.db import models

# Create your models here.
class TipoRequerimiento(models.Model):
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion

class Requerimiento(models.Model):
	fecha_inicio = models.DateField(blank=True, null=True)
	hora_incio = models.TimeField(blank=True,null=True)
	fecha_fin = models.DateField(blank=True,null=True)
	hora_fin = models.TimeField(blank=True,null=True)
	tipo_requerimiento = models.ForeignKey(TipoRequerimiento)
	status = models.BooleanField()
	descripcion = models.CharField(max_length=250)
	
	def __str__(self):
		return self.descripcion



class Acciones(models.Model):
	fecha = models.DateField(blank=True,null=True)
	hora = models.TimeField(blank=True,null=True)
	requerimiento = models.ForeignKey(Requerimiento)
	descripcion = models.CharField(max_length=250)

	class Meta:
		verbose_name_plural = "Acciones"
	def __str__(self):
		return self.descripcion



