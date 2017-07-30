from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# Construct dictionary to pass to template
	context_dict = {'boldmessage': "Crunchy................"}
	
	# Return rendered response
	# Note first parameter is the template to use
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	return HttpResponse("Rango says here is the About page. <br/> <a href='/rango/'>Index</a>")

