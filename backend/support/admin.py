from django.contrib import admin
from . import models


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["creator", "assignee", "status"]


@admin.register(models.TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ["author", "created_at"]