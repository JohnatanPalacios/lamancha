from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

# Models
from books.forms import BookForm
from books.models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail-product.html'
    slug_field = 'title'


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for book in Book.objects.all():
                    data.append(book.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
            # data = Book.objects.get(pk=request.POST['id']).toJSON() # código sin datatable
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'no ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar un nuevo libro'
        context['list_url'] = reverse_lazy('list_books')
        context['action'] = 'add'
        return context


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('list_books')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'no ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un libro'
        context['list_url'] = reverse_lazy('list_books')
        context['action'] = 'edit'
        return context


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    success_url = reverse_lazy('list_books')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un libro'
        context['list_url'] = reverse_lazy('list_books')
        return context
