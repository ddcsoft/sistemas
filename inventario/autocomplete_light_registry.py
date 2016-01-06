from autocomplete_light import shortcuts

from .models import Articulo, Empleado


shortcuts.register(Articulo, search_fields=('descripcion','codigo','serie',))
shortcuts.register(Empleado, search_fields=('nombre','apellidoP','apellidoM'))

