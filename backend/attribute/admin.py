from django.contrib import admin
from . import models
# Register your models here.
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']


admin.site.register(models.Attribute, AttributeAdmin)
