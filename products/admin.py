from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'description']


admin.site.register(Product, ProductAdmin)
