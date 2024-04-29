from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, ImageUploadForm


# задание 6
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.date_added = form.cleaned_data['date_added']
            product.save()
            return HttpResponse('Данные товара изменены')
    else:
        form = ProductForm(instance=product)

    return render(request, 'marketapp/product_edit.html', {'form': form})


# задание 7
def upload_image(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            product.image = image
            fs = FileSystemStorage()
            fs.save(image.name, image)
            return HttpResponse('Изображение товара сохранено')
    else:
        form = ImageUploadForm()
    return render(request, 'marketapp/upload_image.html', {'form': form})
