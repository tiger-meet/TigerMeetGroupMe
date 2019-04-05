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


@csrf_exempt
def sports(request):
    path_info = request.META.get('PATH_INFO')
    url = 'https://tigermeetgroupme.herokuapp.com' + path_info
    #parsed = urlparse.urlparse(url)
    #print(urlparse.parse_qs(parsed.query)['access_token'])
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
