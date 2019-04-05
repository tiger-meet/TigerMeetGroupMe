from django.http import HttpResponse
from django.shortcuts import render
import json
import webbrowser
import urllib
import urllib.parse as urlparse

def index(request):
    path_info = request.META.get('PATH_INFO')
    url = 'https://tigermeetgroupme.herokuapp.com' + path_info
    return render(request, 'chat/index.html', {})

def about(request):
    return render(request, 'chat/about.html', {})

def sports(request):
    return render(request, 'chat/chat.html', {})

#def gmlogin(request):
    #my_dict['my url'] = 'https://oauth.groupme.com/oauth/authorize?client_id=BLmGX0dIG8rQGtSUZS4kcOVkP9RoNb65x01H8fxPSK9ANNR7'
    #return HttpResponse(json.dumps([my_dict]))
#def g(request):
    #url = "https://oauth.groupme.com/oauth/authorize?client_id=BLmGX0dIG8rQGtSUZS4kcOVkP9RoNb65x01H8fxPSK9ANNR7"
    #return response.write("<p>Here's the text of the Web page.</p>")

def redirect(request):
    return render(request, 'chat/chat.html', {})
