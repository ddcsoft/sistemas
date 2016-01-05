# Register your models here.
from django.contrib import admin
from inventario.models import EstadoArticulo, Area,Empleado,Empresa, Puesto, TipoArticulo,Marca,Clasificacion,TipoMvto,Movimiento,Ubicacion,Detalle_Movimiento,Ubicacion_Articulo
from autocomplete_light import shortcuts
from .models import Articulo

admin.site.register(EstadoArticulo)
admin.site.register(Empresa)
admin.site.register(Area)
admin.site.register(TipoArticulo)
admin.site.register(Marca)
admin.site.register(Clasificacion)

admin.site.register(TipoMvto)
admin.site.register(Ubicacion)

admin.site.register(Ubicacion_Articulo)

class PuestoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','area','empresa')

admin.site.register(Puesto,PuestoAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidoP','apellidoM','area','empresa')	
    search_fields = ('nombre','apellidoP','apellidoM')

admin.site.register(Empleado,EmpleadoAdmin)


class ArticuloAdmin(admin.ModelAdmin):
    #list_display = ('codigo','descripcion','modelo','serie','marca','medida','empresa')
    #search_fields = ('codigo','descripcion')
    fields = (('codigo', 'descripcion'),('modelo', 'marca'))	
    form = shortcuts.modelform_factory(Articulo, fields='__all__')

admin.site.register(Articulo,ArticuloAdmin)


class Detalle_MovimientoInline(admin.TabularInline):
    model = Detalle_Movimiento


class MovimientoAdmin(admin.ModelAdmin):
    inlines = (Detalle_MovimientoInline,)

admin.site.register(Movimiento,MovimientoAdmin)
