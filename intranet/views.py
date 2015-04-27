from django.shortcuts import render

from django.template import Context
from django.http import HttpResponse, Http404


import datetime

# Create your views here.
ahora = datetime.datetime.now()


def intranet(request):
	return render(request,'intranet.html',)