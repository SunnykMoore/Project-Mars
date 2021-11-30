from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from pages.views import products
from .models import Product
from django.http import HttpResponse
import templates
from django.core.paginator import Paginator

# Create your views here.
	
def catalogView(request):
	catalog = Product.objects.exclude(name = "New Product")
	paginator = Paginator(catalog, 4) # Show 4 products per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'catalog.html', {'page_obj': page_obj, 'catalog': catalog})
	
def prodView(request, prodID):
	product = Product.objects.get(product_id=prodID)
	prodID = product.product_id
	html = '<center><h1>'+ product.name +'</h1>'+'<img src="{{ product.image.url }}"><br><h2>Price: $'+ str(product.price) +'</h2><br><p>About this product: '+ product.description +'</p><br>Total Orders: ' + str(product.num_orders) + '\tProduct ID: ' + str(product.product_id) + '<br><h3>Default Specs: </h3><br>Category: ' + str(product.category) + '<br>Size: ' + str(product.size) + '<br>Type: ' + str(product.product_type) + '<br>Handle: ' + str(product.handle) + '<br><a href='+ str(prodID) +'/order/create/ target="_blank"><button type="button">Place an Order</button></center>'
	return render(request, 'product_detail.html', {'product': product, 'prodID': prodID})

class SearchCatalog(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'page_obj'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            						  Q(name__icontains=query) |
                                      Q(description__icontains=query) |
                                      Q(price__icontains=query) |
                                      Q(category__icontains=query) |
                                      Q(size__icontains=query) |
                                      Q(handle__icontains=query) |
                                      Q(product_type__icontains=query))
