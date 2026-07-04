from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = ("priority", "title", "status", "created_at", "updated_at", "assigned_to", "reported_by")
    list_filter = ("status", "priority", )
    search_fields = ("title",)
