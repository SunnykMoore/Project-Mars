from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
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
    fields = '__all__'
    product = Product
    size = product.size
    instrument_handle = product.handle
    instrument_type = product.product_type
    instrument_category = product.category
    success_url = '/orders/'

class OrderDetailView(DetailView):
    model = Order