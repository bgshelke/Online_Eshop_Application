from django.contrib import admin
from .models.product import Product
from .models.catagory import Catagory
from .models.customer import Customer
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','description','image','catagory']

admin.site.register(Product,ProductAdmin)

class CatagoryAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Catagory,CatagoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','phone','password']




admin.site.register(Customer)