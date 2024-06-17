from django.urls import path
from main2 import views

app_name = 'main2'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
