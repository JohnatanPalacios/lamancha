# Django
from django.shortcuts import render
from books.models import Book
from django.db.models import Q


def home(request):
    if request.GET.get('search'):
        query = request.GET.get('search')
        results = Book.objects.filter(Q(title__icontains=query) |
                                      Q(editorial__icontains=query) |
                                      Q(author__icontains=query) |
                                      Q(ISBN__icontains=query)
                                     )
        return render(request, 'books/listing.html', {'books': results})
    results = Book.objects.all()
    return render(request, "index.html", {'books': results})
