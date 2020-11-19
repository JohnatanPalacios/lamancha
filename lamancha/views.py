# Django
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

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