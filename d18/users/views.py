from django.urls import reverse
from d18.users.models import User
from d18.users.forms import UserLoginForm
from django.shortcuts import render, HttpResponseRedirect

from django.contrib import auth

def Login(request) :
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST["usernane"]
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
       return render(request, 'users/register.html')