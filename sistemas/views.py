from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse, Http404

from django.shortcuts import render

import datetime

ahora = datetime.datetime.now()
def hola(request):
	import os
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	return HttpResponse("Hola Mundo en laptop: "+BASE_DIR)

def raiz(request):
    ahora = datetime.datetime.now()
    return render(request, 'include/inicio.html',{'fecha_actual': ahora})

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=horas)
    return render(request, 'horas_adelante.html', {'hora_siguiente': dt, 'horas': horas })



def fecha_actual(request):
    #ahora = timezone.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora})

	

