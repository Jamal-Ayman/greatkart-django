from django.contrib import admin
from .models import Category


# Register your models here.
class ListShow(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'description', 'category_image']
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category, ListShow)
