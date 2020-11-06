# Django
from django.shortcuts import render
from books.models import Book
from django.db.models import Q
def home(request):
	if request.GET.get('search'):
		buscar = request.GET.get('search')
		libros = Book.objects.filter(	Q(title = buscar) |
										Q(editorial = buscar) | 
										Q(author = buscar) |
										Q(ISBN = buscar)
									)
		print(libros)
		return render(request, 'books/listing.html', {'libros': libros})

	books = Book.objects.all()
	return render(request, 'index.html', {'book': books})
