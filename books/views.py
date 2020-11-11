from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator

# Models
from django.views.generic import DetailView

from books.forms import BookForm
from books.models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail-product.html'
    slug_field = 'title'


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Book.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de libros'
        context['create_url'] = reverse_lazy('add_book')
        return context


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('list_books')

    # def post(self, request, *args, **kwargs):
    #    form = BookForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return HttpResponseRedirect(self.success_url)
    #    self.object = None
    #    context = self.get_context_data(**kwargs)
    #    context['form'] = form
    #    return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar un nuevo libro'
        return context