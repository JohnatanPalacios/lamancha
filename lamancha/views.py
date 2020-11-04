# Django
from django.shortcuts import render

def home(request):
    """Home page"""
    books = [{'nombreLibro': 'El quijote de la mancha', 'portada': 'images/portadas/elquijote.jpg'},
             {'nombreLibro': 'Juego de tronos', 'portada': 'images/portadas/juegodetronos.jpg'},
             {'nombreLibro': 'Relatos de un asesino', 'portada': 'images/portadas/relatos.jpg'},
             {'nombreLibro': 'Diccionario ingles español', 'portada': 'images/portadas/diccionario.jpg'},
             {'nombreLibro': 'Aprende a programar Python', 'portada': 'images/portadas/python.jpg'}
             ]
    return render(request, 'index.html', {'book': books})
