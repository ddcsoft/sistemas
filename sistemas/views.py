from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404

from django.shortcuts import render

import datetime


def hola(request):
	import os
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	return HttpResponse("Hola Mundo: "+BASE_DIR)

def raiz(request):
	return HttpResponse("Esta es la raiz de la web")



def horas_adelante(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt =  datetime.datetime.now()+datetime.timedelta(hours=offset)
	html = "<html><body><h1>En %s hora(s), seran:</h1><h3>%s</h3></body></html>" % (offset, dt)
	return HttpResponse(html)

def fecha_actual(request):

	ahora = datetime.datetime.now()
	#ahora = timezone.now()
	return render(request, 'include/cabecera.html', {'fecha_actual': ahora})

