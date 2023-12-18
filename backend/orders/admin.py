from django.contrib import admin
from . import models



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "user", "datetime_created",]

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity"]