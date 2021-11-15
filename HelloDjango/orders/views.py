from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
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
  
class OrderFromCatalog(UpdateView): #The pre-filled order form for each catalog product
    model = Order
    
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle', 'status')
    
    def get_object(self, queryset=None):
        order, created = Order.objects.get_or_create(pk=self.kwargs.get('pk'))
        prod = Product.objects.get(product_id=self.kwargs['prodID'])
        order.size = prod.size
        order.instrument_category=prod.category
        order.description = prod.description
        order.instrument_type = prod.product_type
        order.instrument_handle = prod.handle
        return order
    
    """
    def get_context_data(self, **kwargs): #Gets the <prodID> from the url that we need
    	context = super(OrderFromCatalog, self).get_context_data(**kwargs)
    	context['prodID']= self.kwargs['prodID']
    	global prod
    	prod = Product.objects.get(product_id=context['prodID'])
    	#it actually gets the correct product based on the prodID,
    	#BUT IT WON'T FUCKING PASS IT OUTSIDE THE FUNCTION
    	#IT'S A GLOBAL VARIABLE WHAT THE FUCK
    	return context
    
    
    initial = { 'product': prod,	#Sets up initial values to fill fields
    'size': prod.size,
    'instrument_category': prod.category,
    'description': prod.description,
    'quantity': 1,
    'instrument_type': prod.product_type,
    'instrument_handle': prod.handle,
    }
    """
    
    success_url = '/orders/'

    
