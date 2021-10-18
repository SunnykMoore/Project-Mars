from django.shortcuts import render
from django.views.generic import ListView
from orders.models import Order

class OrderListView(ListView):
    model = Order