import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from cart.cart import Cart
from books.models import *


# class ShoppingCartView(TemplateView):
#     template_name = 'shopping-cart.html'
#
#     def post(self, request, *args, **kwargs):
#         cart = Cart(request)
#
#
#         # username = request.user.id
#         # book = Book.objects.get(id=bookId)
#         # order, created = Order.objects.get_or_create(user=id, complete=False)
#
#         data = {}
#         data['cart'] = cart
#         # try:
#         #     action = request.POST['action']
#         #     if action == 'searchdata':
#         #         data = []
#         #         for dc in request.user.debitCards.all():
#         #             data.append(dc.toJSON())
#         #     elif action == 'add':
#         #         data['ok'] = 'Libro añadido'
#         # except Exception as e:
#         #     data['error'] = str(e)
#         # return JsonResponse(data, safe=False)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['title'] = 'Métodos de pago'
#         # context['list_url'] = reverse_lazy('erp:client')
#         # context['entity'] = 'User'
#         context['cart'] = 'cart'
#         return context


@login_required(login_url='/users/auth/login/')
def add_product(request, product_id):
    cart = Cart(request)
    product = Book.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("cart:shopping-cart")


@login_required(login_url='/users/auth/login/')
def remove_product(request, product_id):
    cart = Cart(request)
    product = Book.objects.get(id=product_id)
    cart.remove(product)
    return redirect("cart:shopping-cart")


@login_required(login_url='/users/auth/login/')
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Book.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("cart:shopping-cart")


@login_required(login_url='/users/auth/login/')
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:shopping-cart")


@login_required(login_url='/users/auth/login/')
def shopping_cart(request):
    cart = Cart(request)
    products = Book.objects.all()
    return render(request, "shopping-cart.html", {
        "products": products
    })
