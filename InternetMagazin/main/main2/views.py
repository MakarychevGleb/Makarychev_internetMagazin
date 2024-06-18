from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
# Create your views here.

def index(request):

    context = {
        'title': 'ДомСтрой - Главная',
        'content': 'Интернет-магазин мебели "ДомСтрой"',
    }
    return render(request, 'main2/index.html', context)

def about(request):
    context = {
        'title': 'ДомСтрой - О нас',
        'content': 'О нас',
        'text_on_page': ' ДомСтрой - это поистине мебельный рай. В нашем интернет-магазине вы сможете подобрать себе мебель под любые вкусовые и цветовые предпочтения. Наш ассортимент наполнен различными вариантами под каждую из ценовых категорий от бюджетных  до моделей премиум класса'
        
    }
    return render(request, 'main2/about.html', context)