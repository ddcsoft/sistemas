from autocomplete_light import shortcuts

from .models import Articulo

shortcuts.register(Articulo, search_fields=('descripcion',))