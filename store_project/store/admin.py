from django.contrib import admin
from .models import Product, Cathegory, Order 

# Register your models here.
admin.site.register(Product) 
admin.site.register(Cathegory)
admin.site.register(Order)