from _typeshed import Self
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import UpdateView
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

class OrderCopyView(UpdateView):
    model = Order
    new_item = Order.objects.get(Self)
    new_item.pk = None
    fields = '__all__'
    success_url = '/orders/'
    
def OrderCopy(request, id):
    new_item = Order.objects.get(pk=id)
    new_item.pk = None
    form =  MyForm(request.POST or None, instance = new_item)