from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
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
                messages.success(request, f"{username}, вы успешно зашли в аккаунт")
                return HttpResponseRedirect(reverse('main2:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'ДомСтрой - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, вы успешно зарегестрировались и зашли в аккаунт")
            return HttpResponseRedirect(reverse('main2:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'ДомСтрой - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)
# запретить не авторизов польз доступ к профилям
@login_required
def profile(request):
    if request.method == 'POST':
        #  укажем для каого пользователя мы сохраняем изменения
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'ДомСтрой - Профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)
# запретить не авторизов польз доступ к профилям
# для выхода из пользователя i dr
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, вы успешно вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main2:index'))