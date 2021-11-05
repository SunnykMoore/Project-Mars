from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
import templates
from django.core.paginator import Paginator

# Create your views here.
	
def catalogView(request):
	catalog = Product.objects.all()
	
	html = '<center><h1>Medtronics Supply Store</h1><h2>Products Catalogue<h2><h1></h1>'
	for product in catalog:
		prodID = product.product_id
		item = '<a href="/products/' + str(prodID) + '"><img src='+ str(product.image) +'></a><br><h2>'+ product.name +'</h2><br>'
		html += item
	html += '</center>'#so not everything is shoved to the left
	return HttpResponse(html, status = 200)
	
def prodView(request, prodID):
	product = Product.objects.get(product_id=prodID)
	prodID = product.product_id
	html = '<center><h1>'+ product.name +'</h1>'+'<img src='+ str(product.image) +'<br><h2>'+ str(product.price) +'</h2><br><p>'+ product.description +'<br><p><a href='+ str(prodID) +'/order/create/'' target="_blank"><button type="button">Place an Order</button></p></center>'
	
	return HttpResponse(html, status = 200)
