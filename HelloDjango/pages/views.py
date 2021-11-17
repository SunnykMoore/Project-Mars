from django.shortcuts import render
from orders.models import Order


# This is where we keep our non-specific pages. Pages unique to a product/order are stored in the corresponding folder
def home(request, *args, **kwargs):
	latest_orders = Order.objects.order_by('-pk')[0:4]
	most_reorders = Order.objects.order_by('-num_reorders')[0:4]
	return render(request, "home.html", {'latest_orders': latest_orders, 'most_reorders': most_reorders})
	
def products(request, *args, **kwargs):
	return render(request, "catalogue.html", {})
	
def order(request, *args, **kwargs):
	return render(request, "orderform.html", {})
