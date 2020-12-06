# Django
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Models
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, RedirectView, DetailView, View, TemplateView

from lamancha import settings
from .forms import UserRegistrationForm, DebitCardForm
from .models import User, DebitCard


class LoginFormView(LoginView):
    template_name = 'users/auth/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class LogoutView(LoginRequiredMixin, RedirectView):
    pattern_name = 'index'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/auth/signup.html'
    success_url = reverse_lazy('login')
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


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile/profile.html'
    slug_field = 'pk'


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Solo se aceptan valores alfanuméricos'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'El usuario ya existe'}, status=409)
        return JsonResponse({'username_valid': True})


class UserCardsView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile/paymentMethods.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for dc in request.user.debitCards.all():
                    data.append(dc.toJSON())
            elif action == 'add':
                card = DebitCard()
                card.number = request.POST['number']
                card.nameInCard = request.POST['nameInCard']
                card.save()
                request.user.debitCards.add(card)
                request.user.save()
            elif action == 'delete':
                card = DebitCard.objects.get(pk=request.POST['id'])
                card.delete()
            else:
                data['error'] = 'Ha ocurrido un error'

            # elif action == 'edit':
            #     cli = Client.objects.get(pk=request.POST['id'])
            #     cli.names = request.POST['names']
            #     cli.surnames = request.POST['surnames']
            #     cli.dni = request.POST['dni']
            #     cli.date_birthday = request.POST['date_birthday']
            #     cli.address = request.POST['address']
            #     cli.gender = request.POST['gender']
            #     cli.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Métodos de pago'
        # context['list_url'] = reverse_lazy('erp:client')
        context['entity'] = 'User'
        context['form'] = DebitCardForm()
        return context


def Mensajeria(request):
    model = User
    template_name = 'redSocial/ListaAmigos.html'

    action = request.GET.get('action')
    return render(request, template_name, {})