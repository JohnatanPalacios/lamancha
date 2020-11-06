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

# RECOMIENDO HACERLO POR ESTE MÉTODO, ES MÁS FÁCIL Y SALE RÁPIDO
class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'books/listing.html'
    model = Book
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'books'

