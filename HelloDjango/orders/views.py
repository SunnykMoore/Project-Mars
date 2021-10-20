from django.shortcuts import render
from django.views.generic import ListView, CreateView
from orders.models import Order
from orders.forms import OrderForm

class OrderListView(ListView):
    model = Order

class CreateOrderView(CreateView):
    model = Order
    # form_class = OrderForm
    fields = '__all__'
    success_url = '/orders/'