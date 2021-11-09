from django.shortcuts import render
from django.views.generic import ListView, CreateView
from orders.models import Order
from orders.forms import OrderForm
from products.models import Product
from django.http import HttpResponse

class OrderListView(ListView):
    model = Order

class CreateOrderView(CreateView):
    model = Order
    # form_class = OrderForm
    fields = '__all__'
    success_url = '/orders/'

class CurrentOrderListView(ListView):
    model = Order
  
class OrderFromCatalog(CreateView, Product): #foundation technically there
    model = Order
    prodID = Product.product_id
    print(Product)
    prod = Product.objects.get(product_id=1)
    # form_class = OrderForm
    fields = '__all__'
    initial = { 'product': prod,
    'size': prod.size,
    'instrument_category': prod.category,
    'description': prod.description,
    'quantity': 1,
    'instrument_type': prod.product_type,
    'instrument_handle': prod.handle,
    }
    success_url = '/orders/'
