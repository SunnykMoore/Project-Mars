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

class OrderCopyView(UpdateView): # Reorders, inherits from the generic django update view
    model = Order #Selects the model to use this view action on
    
    def get_object(self, queryset=None): #overrides inherent get_object method in UpdateView
        # if old_item.parent_reorder is None: WHEN TO SET THIS UP?
        old_item = super().get_object(queryset) #sets the old order by calling the generic get_object version of the method
        old_item.is_reordered = True  #sets the old order as a reorder
        old_item.num_reorders = (old_item.num_reorders + 1) #increases the number of times this reorder has been placed
        old_item.save() #saves to database
        new_item = super().get_object(queryset) #grabs the old order again, but sets to new order variable
        new_item.pk = None #removes primary key, which causes django to make a new object and assign a new pk
        new_item.is_reordered = False #lines 48-49 may not be needed, but wanted to make sure new order didn't initialize its reorder fields incorrectly.
        new_item.num_reorders = 0
        new_item.parent_reorder = Order.objects.get(pk=old_item.pk) #Sets new order's parent as old order
        new_item.save() #saves to DB
        return new_item # returns the grabbed object (the newly created order) to the UpdateView to act on
    
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle', 'status') #Selects fields to show in the form (not showing those that deal with reorders)
    success_url = '/orders/'