from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from .models import Products
from .utils import q_search


def catalog(request, category_slug=None):
# фильтрация, страницы, поисковик
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
            )
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
#количество отоброжаемых товаров на странице (4)
    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))
    context = {
        'title': 'ДомСтрой - Каталог',
        'goods': current_page,
        "slug_url": category_slug
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request, 'goods/product.html', context)

# def product(request, product_slug=False, product_id=False):
# if product_id:
# product = Products.objects.get(id=product_id)
# else: