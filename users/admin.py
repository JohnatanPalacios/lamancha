# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from .models import *


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    # muestra lo que quiere ver el administrador
    list_display = (
        'dni',
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


class MensajesAdmin(admin.ModelAdmin):
    """docstring for MensajesAdmin"""
    list_display = (
        'id_chat',
        'contenido',
        'hora_fecha',
        'id_emisor',
        'id_receptor',
        'estado'
    )
    
        

admin.site.register(User, BaseUserAdmin)
admin.site.register(LiteraryGenders)
admin.site.register(Mensaje, MensajesAdmin)