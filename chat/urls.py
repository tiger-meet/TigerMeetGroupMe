from django.urls import path, re_path

from .views import index, about, gmlogin, group, joinchat

urlpatterns = [
    path('', gmlogin, name='gmlogin'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    re_path(r'^join/(?P<group_name>/chat)', joinchat, name='joinchat'),
    # This is the url re for making any chat
    re_path(r'^makechat/(?P<group_name>[^/]+)', group, name='group')
]