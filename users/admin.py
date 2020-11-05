# Django
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# Models
from users.models import Customer
from django.contrib.auth.models import User


# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)


class CustomerInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Customer
    can_delete = False
    verbose_name_plural = 'administradores'
    exclude = ['news', 'favoriteGenres']


class UserAdmin(UserAdmin):
    """Add profile admin to base user admin."""

    inlines = (CustomerInline,)
    # muestra lo que quiere ver el administrador
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