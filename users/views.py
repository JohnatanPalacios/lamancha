"""Users views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Customer
from books.models import Book
from django.db.models import Q

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Las contraseñas no son iguales'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Nombre de usuario en uso'})

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

        customer = Customer(user=user)
        customer.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
# @permission_required('view_book')
def profile_main(request):
    
    if request.GET.get('search'):
        buscar = request.GET.get('search')
        libros = Book.objects.filter(   Q(title = buscar) |
                                        Q(editorial = buscar) | 
                                        Q(author = buscar) |
                                        Q(ISBN = buscar)
                                    )
        print(libros)
        return render(request, 'books/listing.html', {'libros': libros})

    return render(request, 'users/profile-main.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario y contraseña incorrectos'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required()
def profile_payment_methods(request):
    return render(request, 'users/profile-paymentMethods.html')

