from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts_app.models import (
    User,
    Profile
)

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role')
    filter_horizontal = ()
    fieldsets = ()
    ordering = ('-id', )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'state', 'pincode', 'updated_at')
    ordering = ('-id', )
