# Django
from django.shortcuts import render


def home(request):
    """Home page"""
    books = [{'nombreLibro':'El quijote de la mancha', 'portada':'images/portadas/elquijote.jpg'},{'nombreLibro':'Juego de tronos', 'portada':'images/portadas/juegodetronos.jpg'}]
    return render(request, 'index.html', {'home': home, 'book':books})

