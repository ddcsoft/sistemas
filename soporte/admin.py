from django.contrib import admin
from soporte.models import TipoRequerimiento, Requerimiento, Acciones
# Register your models here.
admin.site.register(TipoRequerimiento)
admin.site.register(Requerimiento)
admin.site.register(Acciones)

