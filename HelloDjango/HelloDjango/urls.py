"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from pages import views
from orders.views import OrderListView, CreateOrderView, OrderDetailView, OrderCopyView
from products import views as prod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', prod.catalogView, name='catalogue'),
    path('products/<prodID>', prod.prodView, name='product'),
    #path('order/', views.order, name='orderform'), # Depreciated but kept for reference 10.18.21 BE
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order/create/', CreateOrderView.as_view(), name='create_order'),
    path('products/<prodID>/order/create/', CreateOrderView.as_view(), name='create_order'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<pk>/update', OrderCopyView.as_view(), name='copy_order')
]
