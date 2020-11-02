# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from users.models import Customer
from django.contrib.auth.models import User


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'dni', 'username')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__username')


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Customer
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)