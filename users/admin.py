# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from .models import *


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    # muestra lo que quiere ver el administrador
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'username'
    )
    ordering = 'first_name'


admin.site.register(User, BaseUserAdmin)
admin.site.register(LiteraryGenders)
