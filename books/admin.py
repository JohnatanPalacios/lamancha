from django.contrib import admin

from books.models import Book, Language


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #exclude = ('news', 'favoriteGenres')
    list_display = ('pk', 'title', 'ISBN',)
    #list_display_links = ('pk', 'user',)
    #search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__username',)
    #list_filter = ('user__is_active', 'user__is_staff',)

    class Meta:
        verbose_name = 'Administrar libro'
        verbose_name_plural = 'Administrar libros'

admin.site.register(Language)




#### esto es para mostrar bien como el muckup



