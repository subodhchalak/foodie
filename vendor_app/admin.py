from django.contrib import admin
from vendor_app.models import (
    Vendor
)

# Register your models here.

@admin.register(Vendor)
class VendorApp(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile', 'name', 'is_approved')