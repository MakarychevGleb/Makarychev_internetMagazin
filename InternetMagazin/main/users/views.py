from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
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
            
            session_key = request.session.session_key
            
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, вы успешно зашли в аккаунт")

                if session_key:
                    # add new authorized user carts from anonimous session
                    Cart.objects.filter(session_key=session_key).update(user=user)
                
                # проверка на зарегестрированного
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
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

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
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

def users_cart(request):
    return render(request, 'users/users_cart.html')


# запретить не авторизов польз доступ к профилям
# для выхода из пользователя i dr
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, вы успешно вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main2:index'))