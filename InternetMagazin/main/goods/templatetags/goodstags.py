from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()

# для соединение каталога
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
# 
# все конт переменные(takes_context) будут доступны в context во goods/views
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
#urlencode для создание из словаря ключ значение , в kwargs popadayt imenovannie arg-ti