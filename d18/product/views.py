from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from users.models import User
from django.urls import reverse

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

def basket_add(request, product_id:id):
    product = Product.objects.get(id = product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)

    if not baskets.exists():
        Basket.objects.create(user = request.user, product = product, quantity = 1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(reverse('products:index'))
