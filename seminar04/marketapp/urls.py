from django.urls import path
from . import views

urlpatterns = [
    path('product_edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('upload_image/<int:pk>/', views.upload_image, name='upload_image'),
]
