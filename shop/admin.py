from django.contrib import admin
from .models import Product, Order
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "count", "rating")
    list_editable = ("price",)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product")