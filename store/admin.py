from django.contrib import admin

from .models import Product, Variation


# Register your models here.

class ProductShow(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'stock', 'is_available', 'created_at', 'image', 'modified_at']
    prepopulated_fields = {'slug': ('product_name',)}
    ordering = ['created_at']
    list_filter = ('is_available',)


class Variationadmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    ordering = ['created_at']
    list_editable = ['is_active', ]
    list_filter = ('product', 'variation_category', 'variation_value')


admin.site.register(Product, ProductShow)
admin.site.register(Variation, Variationadmin)
