from django.contrib import admin
from .models import Product


# Register your models here.

class ProductShow(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'stock', 'is_available', 'created_at', 'image', 'modified_at']
    prepopulated_fields = {'slug': ('product_name',)}
    ordering = ['created_at']


admin.site.register(Product, ProductShow)
