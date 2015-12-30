# Register your models here.
from django.contrib import admin
from inventario.models import EstadoArticulo, Area,Empleado,Empresa, Puesto, TipoArticulo,Marca,Clasificacion,Articulo,TipoMvto,Movimiento,Ubicacion,Detalle_Movimiento,Ubicacion_Articulo


admin.site.register(EstadoArticulo)
admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Area)
admin.site.register(TipoArticulo)
admin.site.register(Marca)
admin.site.register(Clasificacion)
admin.site.register(Articulo)
admin.site.register(TipoMvto)
admin.site.register(Movimiento)
admin.site.register(Ubicacion)
admin.site.register(Puesto)
admin.site.register(Detalle_Movimiento)
admin.site.register(Ubicacion_Articulo)
