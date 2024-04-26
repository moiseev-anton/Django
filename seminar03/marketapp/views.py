from django.shortcuts import render, get_object_or_404
from django.views import View
from datetime import date, timedelta
from . import models


class OrdersByClient(View):

    def get(self, request, client_id, days):
        client = get_object_or_404(models.Client, pk=client_id)
        start_date = date.today() - timedelta(days=days)
        orders = models.Order.objects.filter(client_id=client_id, date__gte=start_date).order_by('-date')

        context = {
            "client": client,
            "orders": orders,
            "days": days,
        }

        return render(request=request, template_name="marketapp/orders_by_client.html", context=context)
