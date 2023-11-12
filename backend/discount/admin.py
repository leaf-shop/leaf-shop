from django.contrib import admin
from . import models
# Register your models here.


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['title', 'value']


admin.site.register(models.Discount, DiscountAdmin)
