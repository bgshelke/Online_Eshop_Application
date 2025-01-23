from django.db import models
from .catagory import Catagory


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default=None)
    image = models.ImageField(upload_to='products/')