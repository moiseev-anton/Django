from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
from django.views.generic import TemplateView

import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('Hello, World!')


def orel_reshka(request, n):
    coins = [choice(['Орёл', 'Решка']) for _ in range(n)]
    context = {'coins': coins}
    return render(request, 'myapp/main.html', **context)


def cube(request):
    return HttpResponse(randint(1, 7))


def some_number(request):
    return HttpResponse(randint(0, 100))


def main(request):
    return render(request, 'myapp/main.html')


class About(TemplateView):
    template_name = "myapp/about.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# домашнее задание 1
# def main(request):
#     logger.info('Посещение страницы main')
#     html = """
#     <html>
#     <head><title>Главная</title></head>
#     <body>
#     <h3>Добро пожаловать!</h3>
#     <p>Это мой первый Django сайт</p>
#     <a href='/myapp/about/'>О себе</a>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)
#
# def about(request):
#     logger.info('Посещение страницы about')
#     html = """
#     <html>
#     <head><title>О себе</title></head>
#     <body>
#     <h3>О себе</h3>
#     <p>Меня зовут Антон</p>
#     <p>Я начинающий разработчик на Python</p>
#     <a href='/myapp/main/'>На главную</a>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)
