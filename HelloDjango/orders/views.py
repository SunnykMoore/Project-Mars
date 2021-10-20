from django.shortcuts import render
from django.views.generic import ListView, CreateView
from orders.models import Order
from orders.forms import OrderForm
from orders.filters import ProductFilter

class OrderListView(ListView):
    model = Order

class CreateOrderView(CreateView):
    model = Order
    # form_class = OrderForm
    fields = '__all__'
    success_url = '/orders/'

def OrderInProgress(request):
    f = ProductFilter(request.GET, queryset=Order.objects.exclude(status__exact='Completed'))
    return render(request, 'HelloDjango/orders/templates/orders/completed.html', {'filter': f})