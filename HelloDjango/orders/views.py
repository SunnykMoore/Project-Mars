from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import UpdateView
from orders.models import Order
from products.models import Product
from django.db.models import Q

class OrderListView(ListView):
    model = Order
    def get_queryset(self):
        return Order.objects.exclude(hospital = "Enter Hospital") #Excludes the dummy order for a new Product that new product orders are based on

    def get_queryset(self): 
        return Order.objects.exclude(status = "DENIED")

class DenyReorderView(UpdateView):
    model = Order
    def get_queryset(self):
        return Order.objects.exclude(status_choice = "DENIED")

class CurrentOrders(ListView): #Current Orders
    model = Order
    def get_queryset(self): #Overrides the default queryset for listview
        return Order.objects.exclude(hospital = "Enter Hospital") #Excludes the dummy order for a new Product that new product orders are based on
        
    def get_context_data(self, **kwargs): #Overrides Listview get_context_data method
        context = super(CurrentOrders, self).get_context_data(**kwargs) #Calls original version of method
        context['current_orders'] = Order.objects.filter( #Creates a subset of the context with only current orders
                                                        Q(status="SUBMITTED") |
                                                        Q(status="APPROVED") |
                                                        Q(status="IN PROGRESS") |
                                                        Q(status="SHIPPED") ).exclude(hospital = "Enter Hospital")
        return context
    
    template_name='orders/current_order_list.html' #Selects which html template to pass the context to

class CompletedOrders(ListView): #Completed Orders
    model = Order
    def get_queryset(self): #Overrides the default queryset for listview
        return Order.objects.exclude(hospital = "Enter Hospital") #Excludes the dummy order for a new Product that new product orders are based on

    def get_context_data(self, **kwargs): #Overrides Listview get_context_data method
        context = super(CompletedOrders, self).get_context_data(**kwargs) #Calls original version of method
        context['completed_orders'] = Order.objects.filter( #Creates a subset of the context with only current orders
                                                        
                                                        Q(status="COMPLETED") ).exclude(hospital = "Enter Hospital")
        return context
    
    template_name='orders/completed_order_list.html' #Selects which html template to pass the context to

    
class DeniedOrders(ListView): #orders/denied
    model = Order
    def get_queryset(self): #Combines filtering to denied orders and excluding dummy new order into overriding the get_queryset method
        return Order.objects.exclude(hospital = "Enter Hospital", status = "DENIED").filter(status="DENIED") #Excludes the dummy order for a new Product that new product orders are based on
    template_name='orders/denied_order_list.html' #Selects which html template to pass the context to

class CreateOrderView(CreateView): #/orders/
    model = Order
    def form_valid(self, form): #override inherent form_valid method of CreateView
        prod = form.instance.product #grabs the product by calling the product attribute of the current instance, the order being created
        prod.num_orders = prod.num_orders + 1 #increments the num_orders field of the product
        prod.save() #saves to database
        return super().form_valid(form) #returns the results of the form_valid method of UpdateView and not this one
    
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle')
    
    success_url = '/orders/'

#class CurrentOrderListView(ListView):
  #  model = Order
  
class OrderFromCatalog(UpdateView): #The pre-filled order form for each catalog product
    model = Order #select model to create/update objects with
    
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle') #Select fields to show on form
    
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
    
    def form_valid(self, form): #override inherent form_valid method of UpdateView
        prod = form.instance.product #grabs the product by calling the product attribute of the current instance, the order being created
        prod.num_orders = prod.num_orders + 1 #increments the num_orders field of the product
        prod.save() #saves to database
        return super().form_valid(form) #returns the results of the form_valid method of UpdateView and not this one
    
    success_url = '/orders/'

class OrderDetailView(DetailView):
    model = Order

class OrderCopyView(UpdateView): # Reorders, inherits from the generic django update view
    model = Order #Selects the model to use this view action on
    
    def get_object(self, queryset=None): #overrides inherent get_object method in UpdateView
        # if old_item.parent_reorder is None: WHEN TO SET THIS UP?
        old_item = super().get_object(queryset) #sets the old order by calling the generic get_object version of the method
        if old_item.parent_reorder is not None: #checks if old order is a re-order
            old_item = old_item.parent_reorder #if old order is already a re-order, parent set to its parent 
        old_item.is_reordered = True  #sets the old order as a reorder
        old_item.num_reorders = (old_item.num_reorders + 1) #increases the number of times this reorder has been placed (Bugged, can't find fix, but doesn't break functionality.  Iterates 2 times for all orders)
        old_item.save() #saves to database
        new_item = super().get_object(queryset) #grabs the old order again, but sets to new order variable
        new_item.pk = None #removes primary key, which causes django to make a new object and assign a new pk
        new_item.is_reordered = False #lines 48-49 may not be needed, but wanted to make sure new order didn't initialize its reorder fields incorrectly.
        new_item.num_reorders = 0
        new_item.parent_reorder = old_item #Sets new order's parent as old order
        new_item.status = 'SUBMITTED' #so reorders aren't automatically approved/denied
        return new_item # returns the grabbed object (the newly created order) to the UpdateView to act on
    
    def form_valid(self, form): #override inherent form_valid method of UpdateView
        prod = form.instance.product #grabs the product by calling the product attribute of the current instance, the order being created
        prod.num_orders = prod.num_orders + 1 #increments the num_orders field of the product
        prod.save() #saves to database
        return super().form_valid(form) #returns the results of the form_valid method of UpdateView and not this one
    
    fields = ('product', 'SR_first_name', 'SR_last_name', 'SR_phone_number', 'SM_first_name', 'SM_last_name',
        'SR_email', 'department', 'physician', 'hospital', 'customer_type', 'clinical_need',
        'instrument_category', 'description', 'size', 'quantity', 'disclaimer', 'instrument_type',
        'instrument_handle') #Selects fields to show in the form (not showing those that deal with reorders)
    success_url = '/orders/'
    
class OrderApprove(UpdateView):
	model = Order
	
	def get_object(self, queryset=None): #overrides inherent get_object method in UpdateView
		old_item = super().get_object(queryset) #sets the old order by calling the generic get_object version of the method
		old_item.status = "APPROVED"
		
		return old_item #updates the order with our new status
	fields = ('product', 'SR_first_name', 'SR_last_name', 'status')
	success_url = '/orders/'
	
class OrderDeny(UpdateView):
	model = Order
	
	def get_object(self, queryset=None): #overrides inherent get_object method in UpdateView
		old_item = super().get_object(queryset) #sets the old order by calling the generic get_object version of the method
		old_item.status = "DENIED"
		old_item.denial_reason = ""
		
		return old_item #updates the order with our new status
	fields = ('product', 'SR_first_name', 'SR_last_name', 'status', 'denial_reason')
	success_url = '/orders/'
 
class SearchOrders(ListView): #/orders/search
    model = Order
    def get_queryset(self): #Override listview get_queryset to just get the orders that match search terms
        query = self.request.GET.get('q') #obtains 'q', the query submitted by the user
        return Order.objects.filter( #searches applicable order attributes for search terms
                                    Q(product__name__icontains=query) |
                                    Q(SR_first_name__icontains=query) |
                                    Q(SR_last_name__icontains=query) |
                                    Q(SR_phone_number__icontains=query) |
                                    Q(SM_last_name__icontains=query) |
                                    Q(SR_email__icontains=query) |
                                    Q(department__icontains=query) |
                                    Q(physician__icontains=query) |
                                    Q(hospital__icontains=query) |
                                    Q(customer_type__icontains=query) |
                                    Q(clinical_need__icontains=query) |
                                    Q(instrument_category__icontains=query) |
                                    Q(description__icontains=query) |
                                    Q(size__icontains=query) |
                                    Q(instrument_type__icontains=query) |
                                    Q(instrument_handle__icontains=query) |
                                    Q(denial_reason__icontains=query)
                                    )
