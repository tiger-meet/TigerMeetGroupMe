from django.urls import path, re_path

from .views import index, a, about, g, redirect

urlpatterns = [
    path('', index, name='index'),
    path('a/', a, name='a'),
    path('g/', g, name='g'),
    path('about/', about, name='about'),
    re_path(r'user/(?P<user_token>[^/]+)/$', token, name='token'),
    #path('tigermeetgroupme.herokuapp.com/user?access_token=3ad70e40394a0137a92656b15122bc3d', redirect, name='redirect'),
]