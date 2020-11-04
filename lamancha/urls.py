# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from lamancha import views as local_views
from users import views as users_views
from books import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', local_views.home, name='home'),

    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),

    path('users/profile/main/', users_views.profile_main, name='profile_main'),
    path('users/profile/payment_methods/', users_views.profile_payment_methods, name='profile_payment_methods'),
    path('book', book_views.book, name='book'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
