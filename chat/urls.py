from django.urls import path, re_path

from .views import index, about, sports

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('sports/', sports, name='sports'),
    #path('gmlogin/', gmlogin, name='gmlogin'),
    #re_path(r'user/(?P<user_token>[^/]+)/$', token, name='token'),
    #path('tigermeetgroupme.herokuapp.com?access_token=3ad70e40394a0137a92656b15122bc3d', redirect, name='redirect'),
]