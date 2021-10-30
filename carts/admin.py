from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.

class CartShow(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']
    # prepopulated_fields = {'slug': ('product_name',)}
    ordering = ['date_added']


class CartItemShow(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'is_active']
    # prepopulated_fields = {'slug': ('product_name',)}
    # ordering = ['date_added']


admin.site.register(Cart, CartShow)
admin.site.register(CartItem, CartItemShow)

