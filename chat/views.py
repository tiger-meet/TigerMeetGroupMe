from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
import urllib.parse as urlparse
from django.utils.safestring import mark_safe

def index(request):

    http_host = request.META.get('HTTP_HOST')
    not_host = request.META.get('RAW_URI')
    temp_url = 'https://' + http_host + not_host
    print(temp_url)

    # temp_url = 'https://api.groupme.com/v3/groups?token=3ad70e40394a0137a92656b15122bc3d'
    parsed = urlparse.urlparse(temp_url)
    print(parsed)
    token_list = urlparse.parse_qs(parsed.query)['access_token']
    token = str(token_list[0])

    return render(request, 'chat/index.html', {'access_token': mark_safe(json.dumps(token))})

def about(request):
    return render(request, 'chat/about.html', {})

def gmlogin(request):
    return render(request, 'chat/gmlogin.html', {})

def group(request, group_name):

    return render(request, 'chat/chat.html', {
        #'access_token': mark_safe(json.dumps(access_token)),
        'group_name': mark_safe(json.dumps(group_name))
    })

def chat(request):
    http_host = request.META.get('HTTP_HOST')
    not_host = request.META.get('RAW_URI')
    temp_url = 'https://' + http_host + not_host

    #temp_url = 'https://api.groupme.com/v3/groups?token=3ad70e40394a0137a92656b15122bc3d'
    parsed = urlparse.urlparse(temp_url)
    token_list = urlparse.parse_qs(parsed.query)['access_token']
    token = str(token_list[0])
    url = 'https://api.groupme.com/v3/groups?token=' + token
    url = str(url)

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
