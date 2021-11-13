from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from orders.models import Order
from orders.forms import OrderForm
from products.models import Product
from django.http import HttpResponse
import django.template

class OrderListView(ListView):
    model = Order

class CreateOrderView(CreateView):
    model = Order
    # form_class = OrderForm
    fields = '__all__'
    success_url = '/orders/'

class CurrentOrderListView(ListView):
    model = Order
  
class OrderFromCatalog(CreateView): #The pre-filled order form for each catalog product
    model = Order
    def get_context_data(self, **kwargs): #Gets the <prodID> from the url that we need
    	context = super(OrderFromCatalog, self).get_context_data(**kwargs)
    	context['prodID']= self.kwargs['prodID']
    	global prod
    	prod = Product.objects.get(product_id=context['prodID'])
    	#it actually gets the correct product based on the prodID,
    	#BUT IT WON'T FUCKING PASS IT OUTSIDE THE FUNCTION
    	#IT'S A GLOBAL VARIABLE WHAT THE FUCK
    	return context
    	
    fields = '__all__'
    
    prod = Product.objects.get(product_id=1) #placeholder since GLOBAL WON'T COOPERATE
    initial = { 'product': prod,	#Sets up initial values to fill fields
    'size': prod.size,
    'instrument_category': prod.category,
    'description': prod.description,
    'quantity': 1,
    'instrument_type': prod.product_type,
    'instrument_handle': prod.handle,
    }
    success_url = '/orders/'

    
