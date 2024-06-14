from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories
# Create your views here.

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'ДомСтрой - Главная',
        'content': 'Интернет-магазин мебели "ДомСтрой"',
        'categories': categories
    }
    return render(request, 'main2/index.html', context)

def about(request):
    context = {
        'title': 'ДомСтрой - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о нас'
        
    }
    return render(request, 'main2/about.html', context)