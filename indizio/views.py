from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Indizio 

def home (request):
	return render(request, 'indizio/start.html', {})

def indizio (request, indizio_id):
	indizio = get_object_or_404(Indizio, pk=indizio_id)
	scelte = indizio.fromz.all()
	context = {'scelte': scelte, 'indizio':indizio}
	if (int(indizio_id) == 29):
		return render(request, 'indizio/fine.html', {})
	else:
		return render(request, 'indizio/indizio.html', context)
	
