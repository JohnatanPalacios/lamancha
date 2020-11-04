from django.shortcuts import render

def book(request):
    """Home page"""

    return render(request, 'books/page-detail-product.html', {})