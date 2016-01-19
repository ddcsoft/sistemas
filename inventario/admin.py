# Register your models here.
from django.contrib import admin
from inventario.models import EstadoArticulo, Area,Empleado,Empresa, Puesto, TipoArticulo,Marca,Clasificacion,TipoMvto,Movimiento,Ubicacion,Detalle_Movimiento,Ubicacion_Articulo,Proveedor
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
admin.site.register(Proveedor)

admin.site.empty_value_display = 'gg'


class PuestoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','area','empresa')

admin.site.register(Puesto,PuestoAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidoP','apellidoM','area','empresa')	
    search_fields = ('nombre','apellidoP','apellidoM')


admin.site.register(Empleado,EmpleadoAdmin)


class ArticuloAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('id','codigo','descripcion','modelo','serie','marca','medida','tipo','clasificacion','empresa',)
    search_fields = ('codigo','descripcion','serie','modelo')
    fields = (('codigo', 'descripcion'),('tipo', 'marca'),('modelo', 'serie'),('medida', 'comentario'),('empresa', 'clasificacion'),('estado', 'registradoPor'),('proveedor','costo'))
    list_filter = ('tipo','marca','empresa','clasificacion',)

    #form = shortcuts.modelform_factory(Articulo, fields='__all__')

admin.site.register(Articulo,ArticuloAdmin)


class Detalle_MovimientoInline(admin.TabularInline):
    model = Detalle_Movimiento
    form = shortcuts.modelform_factory(Detalle_Movimiento,exclude=[])


class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('id','responsable','puesto','fecha_Mvto','tipomvto','ubicacion',)
    inlines = (Detalle_MovimientoInline,)
    fields= (('fecha_registro','fecha_Mvto','fecha_Retorno'),('tipomvto','responsable'),('ubicacion','puesto'),('Comentario','registradoPor'))
    form = shortcuts.modelform_factory(Detalle_Movimiento,exclude=[])

admin.site.register(Movimiento,MovimientoAdmin)
