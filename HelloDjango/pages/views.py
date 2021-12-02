from django.shortcuts import render
from orders.models import Order
from products.models import Product


# This is where we keep our non-specific pages. Pages unique to a product/order are stored in the corresponding folder
def home(request, *args, **kwargs):
	latest_orders = Order.objects.order_by('-pk').exclude(hospital = "Enter Hospital").exclude(status = "DENIED")[0:4]
	most_reorders = Order.objects.order_by('-num_reorders').exclude(hospital = "Enter Hospital")[0:4]
	featured_prods = Product.objects.order_by('-num_orders').exclude(name = "New Product")[0:4]
	return render(request, "home.html", {'latest_orders': latest_orders, 'most_reorders': most_reorders, 'featured_prods': featured_prods})
	
def products(request, *args, **kwargs):
	return render(request, "catalogue.html", {})
	
def order(request, *args, **kwargs):
	return render(request, "orderform.html", {})
