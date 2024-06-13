from django.http import HttpResponse
from django.shortcuts import render

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
        'text_on_page': 'Текст о нас'
        
    }
    return render(request, 'main2/about.html', context)