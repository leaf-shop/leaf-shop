from django.contrib import admin
from statistic import models



@admin.register(models.DailyRequestCount)
class DailyRequestCountAdmin(admin.ModelAdmin):
    pass
