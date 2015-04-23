from django.db import models

# Create your models here.
class TipoRequerimiento(models.Model):
	nombre = models.CharField(max_length=100)


class Requerimiento(models.Model):
	fecha_inicio = models.DateField()
	hora_incio = models.TimeField()
	fecha_fin = models.DateField()
	hora_fin = models.TimeField()
	tipo_requerimiento = models.ForeignKey(TipoRequerimiento)
	status = models.BooleanField()


class Acciones(models.Model):
	fecha = models.DateField()
	hora = models.TimeField()
	requerimiento = models.ForeignKey(Requerimiento)



