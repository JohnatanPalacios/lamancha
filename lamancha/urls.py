# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from lamancha import views as local_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', local_views.home, name='home'),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
