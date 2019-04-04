from django.urls import path, re_path

from .views import index, a, about, gmlogin

urlpatterns = [
    path('', index, name='index'),
    path('a/', a, name='a'),
    path('about/', about, name='about'),
    path('gmlogin/', gmlogin, name='gmlogin'),
    #re_path(r'user/(?P<user_token>[^/]+)/$', token, name='token'),
    #path('tigermeetgroupme.herokuapp.com?access_token=3ad70e40394a0137a92656b15122bc3d', redirect, name='redirect'),
]