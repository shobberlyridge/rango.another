from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says Hello there Partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Rango says here is the About page. <br/> <a href='/rango/'>Index</a>")

