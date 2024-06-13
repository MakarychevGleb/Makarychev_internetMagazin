from django.shortcuts import render

import goods

# Create your views here.
def catalog(request):
    return render(request, 'goods/catalog.html')

def product(request):
    return render(request, 'goods/product.html')
