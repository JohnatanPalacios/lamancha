from django.http import JsonResponse
from django.views.generic import TemplateView
from orders.models import *


class OrderView(TemplateView):
    template_name = 'order.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            # if action == 'searchdata':
            #     data = []
            #     for dc in request.user.debitCards.all():
            #         data.append(dc.toJSON())
            # elif action == 'add':
            #     card = DebitCard()
            #     card.number = request.POST['number']
            #     card.nameInCard = request.POST['nameInCard']
            #     card.save()
            #     request.user.debitCards.add(card)
            #     request.user.save()
            # elif action == 'delete':
            #     card = DebitCard.objects.get(pk=request.POST['id'])
            #     card.delete()
            # else:
            #     data['error'] = 'Ha ocurrido un error'

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
        # context['title'] = 'Métodos de pago'
        # context['list_url'] = reverse_lazy('erp:client')
        # context['entity'] = 'User'
        # context['form'] = DebitCardForm()
        return context
