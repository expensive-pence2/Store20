from django.shortcuts import render
from .models import Product, ProductCategory

app_name = 'product'

def index(request):
    context={"name":"Магазинус"}

    return render(request, 'index.html',context=context)

def products(request):
    context = {
        'title':'каталог',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all()
    }

    return render(request, 'products.html', context = context)


def login(request):

    return render(request, 'users/login.html')