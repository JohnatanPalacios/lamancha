from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='debit_card/',
        view=DebitCardView.as_view(),
        name='debit_card'
    ),
]
