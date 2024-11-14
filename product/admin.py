from django.contrib import admin


# Register your models here.

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'size')
    list_filter = ('size',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(Product)
