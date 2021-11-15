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
    model = Order #select model to create/update objects with
    
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle', 'status') #Select fields to show on form
    
    def get_object(self, queryset=None): #override inherent get_object method
        order = Order() #Instead of selecting an existing object, create brand new one
        prod = Product.objects.get(product_id=self.kwargs.get('prodID')) #get the product using the prodID section of the url
        order.product = prod #lines 33-38 set the attributes of the order based on the selected product
        order.size = prod.size
        order.instrument_category=prod.category
        order.description = prod.description
        order.instrument_type = prod.product_type
        order.instrument_handle = prod.handle
        return order
    
    success_url = '/orders/'

    
