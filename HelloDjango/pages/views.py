from django.shortcuts import render

# This is where we keep our non-specific pages. Pages unique to a product/order are stored in the corresponding folder
def home(request, *args, **kwargs):
	return render(request, "home.html", {})
	
def products(request, *args, **kwargs):
	return render(request, "catalogue.html", {})
	
def order(request, *args, **kwargs):
	return render(request, "orderform.html", {})
