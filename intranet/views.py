from django.shortcuts import render

from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


import datetime

# Create your views here.
ahora = datetime.datetime.now()

@login_required
def intranet(request):
	return render(request,'intranet.html',)

