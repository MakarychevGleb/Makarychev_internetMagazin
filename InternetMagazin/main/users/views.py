from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm
# если данные валидны - верны то аутонтефицируемся перенаправляем
#  authenticate - есть ли такой пользователь
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main2:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'ДомСтрой - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):

    context = {
        'title': 'ДомСтрой - Регистрация',
    }
    return render(request, 'users/registration.html', context)

def profile(request):

    context = {
        'title': 'ДомСтрой - Профиль',
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    pass