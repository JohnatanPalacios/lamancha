# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include


from lamancha.views import *
from books import views as books_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'), name='users'),
    path(
        route='',
        view=IndexView.as_view(),
        name='index'
    ),
    # vistas de libros
    path('books/details/<pk>', books_views.BookDetailView.as_view(), name='book_details'),



    # reset password group
    path(
        route='reset_password/',
        view=auth_views.PasswordResetView.as_view(template_name='users/auth/reset_password.html',
                                                  html_email_template_name='users/auth/send_email.html'),
        name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)