from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('orel_reshka/', views.orel_reshka, name='orel_reshka'),
    path('cube/', views.cube, name='cube'),
    path('some_number/', views.some_number, name='some_number'),
    # домашнее задание 1
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
]


