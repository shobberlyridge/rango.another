from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
	# Place the list in our context_dict dictionary
    # that will be passed to the template engine.
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	# Render the response and send it back!
	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'aboutmessage': "Rango says here is the About page."}
	return render(request, 'rango/about.html', context=context_dict)

