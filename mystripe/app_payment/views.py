import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "item.html"

    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        return Response({"item": item, "stripe_api_key": settings.STRIPE_PUBLIC_KEY})


class BuyView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "buy_item.html"

    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        domain = "http://127.0.0.1:8000"
        session = stripe.checkout.Session.create(
            line_items=[{
              'price_data': {
                'currency': 'rub',
                'product_data': {
                  'name': item.name,
                },
                'unit_amount_decimal': item.price,
              },
              'quantity': 1,
            }],
            mode='payment',
            success_url=domain + '/success',
            cancel_url=domain + '/cancel',
        )
        return JsonResponse({'session_id': session.id})


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"