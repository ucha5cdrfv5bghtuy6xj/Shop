from django.shortcuts import render

# Create your views here.

def catalog(request):
    return render(request, "shop/catalog.html")
def orders(request):
    return render(request, "shop/orders.html")
def order_create(request):
    return render(request, "shop/order_create.html")
