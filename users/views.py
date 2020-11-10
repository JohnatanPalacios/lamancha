# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Models
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, RedirectView, DetailView

from .forms import UserRegistrationForm
from .models import User


class LoginFormView(LoginView):
    template_name = 'users/auth/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class LogoutView(RedirectView):
    pattern_name = 'index'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


@login_required
# @permission_required('view_book')
def profile_view(request):
    return render(request, 'users/profile/profile.html')


@login_required
def payment_methods_view(request):
    return render(request, 'users/profile/paymentMethods.html')


@login_required
def orders_history_view(request):
    return render(request, 'users/profile/ordersHistory.html')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/auth/signup.html'
    success_url = reverse_lazy('login') # succes_url redirecciona al sitio indicado al terminar con el formulario
                                        # reverse_lazy me retorna la direccion absoluta del redireccionamiento
    # permission_required = 'user.add_user' #esto es cuando se está usando el mixing
    url_redirect = success_url

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
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Regístrate'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/profile/update.html'
    success_url = reverse_lazy('index') # si voy a hacer un modal, retornar a la vista setting
    permission_required = 'user.add_user'
    url_redirect = success_url

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
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar perfil'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'users/profile/profile.html'
    slug_field = 'pk'


