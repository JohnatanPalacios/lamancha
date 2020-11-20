from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *


urlpatterns = [
    path(
        route='auth/signup/',
        view=UserCreateView.as_view(),
        name='signup'
    ),
    path(
        route='auth/login/',
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
    path(
        route='profile/update/<pk>/',
        view=UserUpdateView.as_view(),
        name='update'
    ),
    path(
        route='profile/payment_methods/<pk>/',
        view=UserPaymentMethodsView.as_view(),
        name='payment_methods'
    ),
    #path('profile/settings/orders_histoty/', orders_history_view, name='orders_history'),
    path('validate_username', csrf_exempt(UsernameValidationView.as_view()), name='validate_username')
    ]