from django.urls import path
from .views import OrdersByClient

urlpatterns = [
    path('orders/<int:client_id>/<int:days>', OrdersByClient.as_view(), name='orders_by_client'),
]
