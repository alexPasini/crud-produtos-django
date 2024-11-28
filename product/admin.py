from django.contrib import admin
from .models import Product, ProductImage
from django.utils.html import format_html


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
        return ""
    image_preview.short_description = 'Preview'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'size')
    list_filter = ('size',)
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_thumbnail', 'uploaded_at')
    list_filter = ('product',)
    search_fields = ('product__name',)
    ordering = ('product',)

    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        if obj.image:
            print(obj.image.url)
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)

        return ""
    image_thumbnail.short_description = 'Thumbnail'
