# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from lamancha.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=IndexView.as_view(),
        name='index'
    ),
    path(
        route='search_book/',
        view=SearchView.as_view(),
        name='search_book'
    ),
    path(
        route='social/',
        view=Mensajeria,
        name='red_social'
    ),

    path('users/', include('users.urls'), name='users'),
    path('books/', include('books.urls'), name='books'),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),


    # reset password group
    path(
        route='reset_password/',
        view=auth_views.PasswordResetView.as_view(template_name='users/auth/reset_password.html',
                                                  html_email_template_name='users/auth/send_email.html'),
        name="password_reset"),
    path(
        route='reset_password_sent/',
        view=auth_views.PasswordResetDoneView.as_view(template_name='users/auth/reset_password_done.html'),
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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # linea nueva para statics
urlpatterns += staticfiles_urlpatterns()
