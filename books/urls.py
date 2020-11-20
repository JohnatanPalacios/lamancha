from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='book/details/<pk>',
        view=BookDetailView.as_view(),
        name='book_details'
    ),
    path(
        route='book/list/',
        view=BookListView.as_view(),
        name='list_books'
    ),
    path(
        route='book/add/',
        view=BookCreateView.as_view(),
        name='add_book'
    ),
    path(
        route='book/update/<int:pk>/',
        view=BookUpdateView.as_view(),
        name='update_book'
    ),
    path(
        route='book/delete/<int:pk>/',
        view=BookDeleteView.as_view(),
        name='delete_book'
    ),
]
