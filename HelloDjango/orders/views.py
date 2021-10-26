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
  
class CreateOrderView(CreateView, Product): #foundation technically there
    model = Order
    # form_class = OrderForm
    #fields = '__all__'
    product = Product
    size = Product.size
    instrument_handle = Product.handle
    instrument_type = Product.product_type
    instrument_category = Product.category
    #print(str(Product.product_id))
    fields = ['product', 'size']
    success_url = '/orders/'
