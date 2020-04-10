from django.contrib import admin
from .models import Product, ProductAdmin, Category, CategoryAdmin

# Register your models here.

admin.site.register(Product, ProductAdmin, )
admin.site.register(Category, CategoryAdmin)