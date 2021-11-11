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
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle', 'status')
    success_url = '/orders/'

class CurrentOrderListView(ListView):
    model = Order
  
class OrderFromCatalog(CreateView, Product): #foundation technically there
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

class OrderCopyView(UpdateView): # Reorders
    model = Order
    
    def get_object(self, queryset=None):
        old_item = super().get_object(queryset)
        old_item.is_reordered = True
        old_item.num_reorders = (old_item.num_reorders + 1)
        old_item.save()
        new_item = super().get_object(queryset)
        new_item.pk = None
        new_item.is_reordered = False
        new_item.num_reorders = 0
        new_item.save()
        return new_item
    
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle', 'status')
    success_url = '/orders/'