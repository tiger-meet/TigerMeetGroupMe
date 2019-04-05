from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import webbrowser
import urllib
import urllib.parse as urlparse

def index(request):
    return render(request, 'chat/index.html', {})

def about(request):
    return render(request, 'chat/about.html', {})


#@csrf_exempt
def sports(request):
    http_host = request.META.get('HTTP_HOST')
    path_info = request.META.get('PATH_INFO')
    url = http_host + path_info
    #url = 'https://api.groupme.com/v3/groups?token=3ad70e40394a0137a92656b15122bc3d'
    #parsed = urlparse.urlparse(url)
    #token = urlparse.parse_qs(parsed.query)['token']
    data = {'name':'sports'}
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=json.dumps(data), headers=headers)
    #return HttpResponse(status=200)
    return render(request, 'chat/chat.html', {})

#def gmlogin(request):
    #my_dict['my url'] = 'https://oauth.groupme.com/oauth/authorize?client_id=BLmGX0dIG8rQGtSUZS4kcOVkP9RoNb65x01H8fxPSK9ANNR7'
    #return HttpResponse(json.dumps([my_dict]))
#def g(request):
    #url = "https://oauth.groupme.com/oauth/authorize?client_id=BLmGX0dIG8rQGtSUZS4kcOVkP9RoNb65x01H8fxPSK9ANNR7"
    #return response.write("<p>Here's the text of the Web page.</p>")

def redirect(request):
    return render(request, 'chat/chat.html', {})
