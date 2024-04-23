from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from random import randint


def index(request):
    return HttpResponse('Hello, world!')


def create_client(request):
    client = Client(
        name=f'name{randint(1,99)}',
        email=f'user{randint(1,99)}@mail.com',
        phone_number=f'684-{randint(100, 999)}',
        address='some address'
    )
    client.save()
    return HttpResponse(f'Клиент {client.name} добавлен')


def get_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if not client:
        return HttpResponse('Клиент не найден')
    return HttpResponse(client)


def update_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if not client:
        return HttpResponse('Клиент не найден')
    client.name = 'new_name'
    client.email = 'new@mail.com'
    client.phone_number = '123456'
    client.save()
    return HttpResponse(f'Данные клиента {client.name} обновлены')


def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if not client:
        return HttpResponse('Клиент не найден')
    client.delete()
    return HttpResponse(f'Клиент {client.name} удален')

