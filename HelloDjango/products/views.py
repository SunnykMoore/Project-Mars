from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.
def prod(*args, **kwargs):
	return HttpResponse("<h1>Products Catalogue</h1>")
	
def catalogView(request):
	catalog = Product.objects.all()
	
	html = '<h1></h1>'
	for product in catalog:
		prodID = product.product_id
		item = '<a href="http://127.0.0.1:8000/products/' + str(prodID) + '"><img src='+ str(product.image) +'></a><br><h2>'+ product.name +'</h2><br>'
		html += item
	return HttpResponse(html, status = 200)
	
def prodView(request, prodID):
	product = Product.objects.get(product_id=prodID)
	html = '<h1>'+ product.name +'</h1>'+'<img src='+ str(product.image) +'<h2>'+ str(product.price) +'</h2>'
	
	return HttpResponse(html, status = 200)
