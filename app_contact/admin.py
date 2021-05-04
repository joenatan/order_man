from django.contrib import admin

from .models import Contact, Address


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name', 'first_name']
