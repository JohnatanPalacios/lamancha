from django.urls import path
from .views import *


urlpatterns = [
    path(
        route='auth/signup/',
        view=UserCreateView.as_view(),
        name='signup'
    ),
    path(
        route='auth/login/',
        # view=auth_views.LoginView.as_view(template_name='users/auth/login.html'),
        view=LoginFormView.as_view(),
        name='login'),
    path(
        route='auth/logout/',
        view=LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='profile/settings/<pk>/',
        view=UserDetailView.as_view(),
        name='profile'
    ),
    path('profile/settings/orders_histoty/', orders_history_view, name='orders_history'),
    path('profile/settings/payment_methods/', payment_methods_view, name='payment_methods'),
    ]