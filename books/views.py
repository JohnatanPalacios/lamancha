from django.shortcuts import render

def book(request):
    """Home page"""
    libro = {'nombre_libro':"Juego de Tronos",
    		 'autor':"George R.R. Martin",
    		 'editorial':"La mancha",
    		 'encuadernacion':"Dura",
    		 'numpages':"980",
    		 'estado':"Nuevo", 
    		 'precio':"68000",
    		 'portada':"images/portadas/juegodetronos.jpg",
    		 'descripcion':"‘Juego de tronos’ también es el nombre de la primera novela de la saga ‘Canción de hielo y fuego’. Un libro publicado en 1996 que, apenas un año más tarde, ganaría el Premio Locus a la mejor novela de fantasía en 1997. Es en este libro donde se nos presenta a los distintos reinos que conforman Poniente y al Trono de Hierro, el elemento sobre el que gira la serie de novelas."}
    return render(request, 'books/page-detail-product.html', libro)