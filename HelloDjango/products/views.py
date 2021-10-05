from django.shortcuts import render

# Create your views here.
def prod(*args, **kwargs):
	return HttpResponse("<h1>Products Catalogue</h1>")
