from django.http import Http404 ,HttpResponse
import datetime

def hola(request):
	return HttpResponse("Hola Mundfffo")

def fecha_actual(request):
	ahora =  datetime.datetime.now()
	html= "<html> <body><h1>Fecha : </h1><h3>%s</h3></body></html>" % ahora
	return HttpResponse(html)

def horas_adelante(request, offset):
	try:
		offset=int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	html= "<html> <body><h1>En %s Horas seran: </h1><h3>%s</h3></body></html>" % (offset,dt)
	return HttpResponse(html)
