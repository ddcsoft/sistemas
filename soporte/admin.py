from django.contrib import admin
from soporte.models import TipoRequerimiento, Requerimiento, Acciones
from autocomplete_light import shortcuts

# Register your models here.
admin.site.register(TipoRequerimiento)
admin.site.register(Acciones)



class RequerimientoAdmin(admin.ModelAdmin):
    form = shortcuts.modelform_factory(Requerimiento, exclude=[])
    

admin.site.register(Requerimiento,RequerimientoAdmin)
