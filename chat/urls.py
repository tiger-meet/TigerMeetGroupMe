from django.urls import path, re_path

from .views import index, about, chat, gmlogin, group

urlpatterns = [
    path('', gmlogin, name='gmlogin'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('chat/', chat, name='chat'),
    #re_path(r'^(?P<group_name>[^/]+)?access_token=(?P<access_token>)$', group, name='group')
    #path('gmlogin/', gmlogin, name='gmlogin'),
    #re_path(r'user/(?P<user_token>[^/]+)/$', token, name='token'),
    #path('tigermeetgroupme.herokuapp.com?access_token=3ad70e40394a0137a92656b15122bc3d', redirect, name='redirect'),
]