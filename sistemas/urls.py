from django.conf.urls import include, url
from django.contrib import admin
from sistemas.views import hola, raiz, fecha_actual, horas_adelante
from intranet.views import intranet, intranet_valida
from soporte.views import soporte
from inventario.views import inventario


urlpatterns = [
    # Examples:
    # url(r'^$', 'sistemas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/$', hola),
    url(r'^$', raiz),
    url(r'^fecha/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante),
    url(r'^intranet/$',intranet),
    url(r'^intranet/valida/$',intranet_valida),
    url(r'^intranet/soporte/$',soporte),
    url(r'^intranet/inventario/$',inventario),
]


