from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='details/',
        view=OrderView.as_view(),
        name='order_details'
    ),
]