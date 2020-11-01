# Django
from django.contrib import admin

#Models
from customers.models import Customer


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
    list_display_links = ()
    list_editable = ()
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__username')
    list_filter = ()
