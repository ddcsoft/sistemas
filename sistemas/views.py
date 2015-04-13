from django.http import HttpResponse
import datetime


def hola(request):
	return HttpResponse("Hola Mundo")

def raiz(request):
	return HttpResponse("Esta es la raiz de la web")

def fecha_actual(request):
	ahora =  datetime.datetime.now()
	html = "<html> <body><h1> Fecha: </h1><h3>%s</h3></body></html>" % ahora
	return HttpResponse(html)