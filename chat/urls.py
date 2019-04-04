from django.urls import path

from .views import index, a, about, g, redirect

urlpatterns = [
    path('', index, name='index'),
    path('a/', a, name='a'),
    path('g/', g, name='g'),
    path('about/', about, name='about'),
    path('?access_token=ACCESS_TOKEN', redirect, name='redirect'),
]
