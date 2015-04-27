from django.shortcuts import render
from django.shortcuts import render_to_response
from soporte.models import Requerimiento
from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.

ahora = datetime.datetime.now()
@login_required
def soporte(request):

	lista = Requerimiento.objects.all()
	return render(request,'soporte.html',{'lista_requerimientos': lista})

