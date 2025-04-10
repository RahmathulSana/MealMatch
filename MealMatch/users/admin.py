from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'phone_no', 'is_staff', 'is_active')  # Customize display
    fieldsets = UserAdmin.fieldsets + (  # Add new fields in admin panel
        ('Additional Info', {'fields': ('role', 'phone_no')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

