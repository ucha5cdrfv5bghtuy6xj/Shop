from django.shortcuts import redirect, render
from .models import Product, Order
# Create your views here.

def catalog(request):
    products = Product.objects.all()

    return render(request, "shop/catalog.html", {"products":products})


def orders(request):
    orders = Order.objects.all()
    
    return render(request, "shop/orders.html", {"orders":orders})


def order_create(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        Order.objects.create(product = product, adres = request.POST.get("delivery_address"))
        return redirect("orders")
    
    return render(request, "shop/order_create.html", {"product":product})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, "shop/product_detail.html", {"product":product})


