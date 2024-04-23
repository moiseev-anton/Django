from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_client/', views.create_client, name='create_client'),
    path('get_client/<int:client_id>', views.get_client, name='get_client'),
    path('update_client/<int:client_id>', views.update_client, name='update_client'),
    path('delete_client/<int:client_id>', views.delete_client, name='delete_client'),
]