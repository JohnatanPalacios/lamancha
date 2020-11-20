from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *


class DebitCardView(CreateView):
    model = DebitCard
    form_class = DebitCardForm
    template_name = 'debit_card.html'
    success_url = reverse_lazy('payment_methods')
