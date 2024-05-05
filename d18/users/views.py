from django.urls import reverse
from .models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from product.models import Basket

from django.contrib import auth

def login(request) :
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(usernane = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    context = {
        'form' :form,
    }

    return render(request, 'users/login.html', context = context)


def register (request) :
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form,}


    return render(request, 'users/register.html', context = context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance = request.user)
        context = {'Title':'Профиль',
                   'form':form,
                   'baskets' : Basket.objects.all()}
        return render(request, 'users/profile.html', context = context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))