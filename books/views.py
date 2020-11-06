from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render

# Models
from django.views.generic import DetailView

from books.models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail-product.html'
    slug_field = 'title'


def search(request):
    return render(request, 'books/listing.html')

class PostsFeedView(LoginRequiredMixin, ListView):
    """retorna todos los libros ."""

    template_name = 'books/listing.html'
    model = Book
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'books'

