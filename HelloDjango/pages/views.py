from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
	return render(request, "home.html", {})
	
def products(request, *args, **kwargs):
	return render(request, "catalogue.html", {})
	
def order(request, *args, **kwargs):
	return render(request, "orderform.html", {})
