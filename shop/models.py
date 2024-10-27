from django.db import models
from core.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField( max_length=100)
    img = models.ImageField(upload_to="images/Product/")
    desk = models.TextField()
    price = models.FloatField()
    sale = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    is_available = models.BooleanField(default= True)





class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    adres = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)




