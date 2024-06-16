from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from goods.models import Products

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0).order_by("-rank")
    )
# для окраска слов из поиска
    result = result.annotate(
        headline=SearchHeadline(
            "name", query,
            start_sel='<span style="background-color: yellow">',
            stop_sel="</span>",
        )
    )
    # для окраска слов из поиска
    result = result.annotate(
        bodyline=SearchHeadline(
            "description", query,
            start_sel='<span style="background-color: yellow">',
            stop_sel="</span>",
        )
    )
    return result


# при в воде в поисковик с сортировкой по словам id и
#  при совпадении с товаром на 75% gde rank > 0,


# keywords = [word for word in query.split() if len(word) > 2]

# q_objects = Q()

# for token in keywords:
#     q_objects |= Q(description__icontains=token)
#     q_objects |= Q(name__icontains=token)

# return Products.objects.filter(q_objects)
