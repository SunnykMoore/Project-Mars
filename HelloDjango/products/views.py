from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
import templates
from django.core.paginator import Paginator

# Create your views here.
	
def catalogView(request):
	catalog = Product.objects.all()
	paginator = Paginator(catalog, 4) # Show 4 products per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'catalog.html', {'page_obj': page_obj, 'catalog': catalog})
	
def prodView(request, prodID):
	product = Product.objects.get(product_id=prodID)
	prodID = product.product_id
	html = '<center><h1>'+ product.name +'</h1>'+'<img src='+ str(product.image) +'<br><h2>'+ str(product.price) +'</h2><br><p>'+ product.description +'<br><p><a href='+ str(prodID) +'/order/create/'' target="_blank"><button type="button">Place an Order</button></p></center>'
	
	return HttpResponse(html, status = 200)
