from autocomplete_light import shortcuts

from .models import TipoRequerimiento

shortcuts.register(TipoRequerimiento, search_fields=('descripcion',))