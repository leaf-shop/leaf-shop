from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['is_active']
    list_display = ['title', 'price', 'is_active', 'count']
    list_editable = ['price', 'is_active', 'count']


admin.site.register(models.Product, ProductAdmin)
