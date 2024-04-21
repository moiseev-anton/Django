from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('Hello, World!')


def orel_reshka(request):
    return HttpResponse(choice(['Орёл', 'Решка']))


def cube(request):
    return HttpResponse(randint(1, 7))


def some_number(request):
    return HttpResponse(randint(0, 100))


# домашнее задание
def main(request):
    logger.info('Посещение страницы main')
    html = """
    <html>
    <head><title>Главная</title></head>
    <body>
    <h3>Добро пожаловать!</h3>
    <p>Это мой первый Django сайт</p>
    <a href='/myapp/about/'>О себе</a>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    logger.info('Посещение страницы about')
    html = """
    <html>
    <head><title>О себе</title></head>
    <body>
    <h3>О себе</h3>
    <p>Меня зовут Антон</p>
    <p>Я начинающий разработчик на Python</p>
    <a href='/myapp/main/'>На главную</a>
    </body>
    </html>
    """
    return HttpResponse(html)
