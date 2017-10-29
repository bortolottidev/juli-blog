from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Indizio 

def home (request):
	return render(request, 'indizio/start.html', {})

def indizio (request, indizio_id):
	indizio = get_object_or_404(Indizio, pk=indizio_id)
	for scelta in indizio.fromz.all():
		print(scelta)
	return render(request, 'indizio/indizio.html', \
		{'scelte': indizio.fromz.all(), 'indizio':indizio})
