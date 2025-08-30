from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """
    Admin panel for "Ticket"
    """
    list_display = ["title", "owner", "created", "type"]
    list_display_links = ["title"]
    list_per_page = 10
    list_filter = ["type"]
    search_fields = ["title", "text"]
    ordering = ["-created"]
    prepopulated_fields = {
        "slug": ["title"]
    }
    
