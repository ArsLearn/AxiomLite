from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ["username", "phone_number", "national_code"]
    list_display_links = ["username"]
    search_fields = ["username", "first_name", "last_name", "phone_number", "national_code"]
    ordering = ["username"]
    date_hierarchy = "date_joined"
    sortable_by = ["first_name", "last_name"]
    list_per_page = 32
