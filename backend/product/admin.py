from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['is_active']
    list_display = ['title', 'price', 'is_active', 'count']
    list_editable = ['price', 'is_active', 'count']


class AttributeAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Attribute, AttributeAdmin)
admin.site.register(models.ProductGallery)