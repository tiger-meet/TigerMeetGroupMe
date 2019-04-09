from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
import urllib.parse as urlparse
from django.utils.safestring import mark_safe
from .models import GroupChats

def gettoken(request):
    http_host = request.META.get('HTTP_HOST')
    not_host = request.META.get('RAW_URI')
    temp_url = 'https://' + http_host + not_host

    parsed = urlparse.urlparse(temp_url)
    token_list = urlparse.parse_qs(parsed.query)['access_token']
    token = str(token_list[0])
    return token

# loads the index page with authentication token
def index(request):
    token = gettoken(request)

    return render(request, 'chat/index.html', {'access_token': mark_safe(json.dumps(token))})

# loads the about page
def about(request):
    return render(request, 'chat/about.html', {})

# loads the groupme authentication page
def gmlogin(request):
    return render(request, 'chat/gmlogin.html', {})

# joins sports chat
def joinsportschat(request):
    token = gettoken(request)
    code = GroupChats.objects.filter(GroupName="sports").values_list("GroupId", flat=True)[0]
    sharetoken = GroupChats.objects.filter(GroupName="sports").values_list("ShareToken", flat=True)[0]

    url = "https://api.groupme.com/v3/groups/" + code + "join" + sharetoken + "token=" + token
    requests.post(url)

    return render(request, 'chat/joinsportschat.html', {
        'GroupId': mark_safe(json.dumps(code))
    })

# creates a chat in your own personal groupme application based on which one you click
def group(request, group_name):
    token = gettoken(request)

    url = 'https://api.groupme.com/v3/groups?token=' + token
    url = str(url)

    chatname = "TigerMeet " + group_name
    data = {'name': chatname,
            "share": True,}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    print(r.json()['response']['share_url'])
    shareurl = (r.json()['response']['share_url'])
    code = str(shareurl[-16:-9])
    sharetoken = str(shareurl[-8:])


    #database stuff
    #Foo.objects.create
    p = GroupChats(GroupName=group_name, GroupId=code, ShareToken=sharetoken)
    p.save()

    return render(request, 'chat/chat.html', {
        #'access_token': mark_safe(json.dumps(access_token)),
        'group_name': mark_safe(json.dumps(group_name))
    })

#def gmlogin(request):
    #my_dict['my url'] = 'https://oauth.groupme.com/oauth/authorize?client_id=BLmGX0dIG8rQGtSUZS4kcOVkP9RoNb65x01H8fxPSK9ANNR7'
    #return HttpResponse(json.dumps([my_dict]))
#def g(request):
    #url = "https://oauth.groupme.com/oauth/authorize?client_id=BLmGX0dIG8rQGtSUZS4kcOVkP9RoNb65x01H8fxPSK9ANNR7"
    #return response.write("<p>Here's the text of the Web page.</p>")

# unused
def redirect(request):
    return render(request, 'chat/chat.html', {})
