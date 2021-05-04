from django.contrib import admin

from .models import Contact, Address


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name', 'first_name']
    inlines = [AddressInline]
