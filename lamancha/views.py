# Django
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from books.models import Book
from django.db.models import Q


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('search'):
            action = request.GET.get('search')
            results = Book.objects.filter(Q(title__icontains=action) |
                                          Q(editorial__icontains=action) |
                                          Q(author__icontains=action) |
                                          Q(ISBN__icontains=action)
                                          )
            if results:
                return render(request, 'books/search-results.html', {'books': results})
            else:
                results = Book.objects.all()
                return render(request, 'books/search-results.html', {'books': results})
        results = Book.objects.all()
        return render(request, self.template_name, {'books': results})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Buscar libros'
        return context


class SearchView(ListView):
    model = Book

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.GET.get('action')
            if action == 'autocomplete':
                data = []
                books = Book.objects.filter(Q(title__icontains=request.GET.get('term')) |
                                            Q(editorial__icontains=request.GET.get('term')) |
                                            Q(author__icontains=request.GET.get('term')) |
                                            Q(ISBN__icontains=request.GET.get('term'))
                                            )
                for book in books:
                    item = book.toJSON()
                    item['text'] = book.title
                    data.append(item)
            else:
                data['error'] = 'Libro no encontrado'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Buscar libros'
        return context
