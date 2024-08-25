from django.shortcuts import render
from .models import Product, Order
# Create your views here.

def catalog(request):
    products = Product.objects.all()
    return render(request, "shop/catalog.html", {"products":products})
def orders(request):
    orders = Order.objects.all()
    return render(request, "shop/orders.html", {"orders":orders})
def order_create(request):
    return render(request, "shop/order_create.html")
