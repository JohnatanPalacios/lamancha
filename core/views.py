# Django

from django.shortcuts import render, redirect


# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView




def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'core/../templates/users/auth/signup.html', {'error': 'Las contraseñas no son iguales'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'core/../templates/users/auth/signup.html', {'error': 'Nombre de usuario en uso'})

        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.dni = request.POST['dni']
        user.photo = request.POST['photo']
        user.address = request.POST['address']
        user.birthday = request.POST['birthday']
        user.gender = request.POST['gender']
        user.favoriteGenres = 'por ahora en prueba'

        if request.POST['news'] == 'True':
            user.news = True
        else:
            user.news = False

        user.save()
        return redirect('login')
    return render(request, 'core/../templates/users/auth/signup.html')




