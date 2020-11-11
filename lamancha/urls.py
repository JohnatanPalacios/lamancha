# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include


from lamancha.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=home, # view=IndexView.as_view(), hay que hacer el cambio nuevamente
        name='index'
    ),
    path('users/', include('users.urls'), name='users'),
    path('books/', include('books.urls'), name='books'),

    # reset password group
    path(
        route='reset_password/',
        view=auth_views.PasswordResetView.as_view(template_name='users/auth/reset_password.html',
                                                  html_email_template_name='users/auth/send_email.html'),
        name="password_reset"),
    path(
        route='reset_password_sent/',
        view=auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),
    path(route='reset/<uidb64>/<token>/',
         view=auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"
    ),
    path(
        route='reset_password_complete/',
        view=auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)