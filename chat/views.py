from django.shortcuts import render, redirect
import requests
import json
import urllib.parse as urlparse
from django.utils.safestring import mark_safe
from .models import GroupChats, Todo
from django.contrib import admin

admin.site.register(GroupChats)

def gettoken(request):
    http_host = request.META.get('HTTP_HOST')
    not_host = request.META.get('RAW_URI')
    temp_url = 'https://' + http_host + not_host
    print(temp_url)

    #parse the url for the token, if there is one
    parsed = urlparse.urlparse(temp_url)
    token_dict = urlparse.parse_qs(parsed.query)
    print(token_dict)
    print(token_dict == {})

    #if there isn't a token, return the string 'none' to be later used by functions
    if token_dict == {}:
        return 'none'

    #if there is a token, continue onward
    else:
        token_list = token_dict['access_token']
        token = str(token_list[0])
        return token

# loads the index page with authentication token
def index(request):
    token = gettoken(request)
    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})
    else:
        return render(request, 'chat/index.html', {'access_token': mark_safe(json.dumps(token))})

# loads the about page
def about(request):
    return render(request, 'chat/about.html', {})

# loads the groupme authentication page
def gmlogin(request):
    return render(request, 'chat/gmlogin.html', {})

# loads the events page
def events(request, group_name):
    token = gettoken(request)
    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})
    else:
        return render(request, 'chat/events.html', {'access_token': mark_safe(json.dumps(token)),
                                                    'group_name': mark_safe(json.dumps(group_name))
                                                    })

# joins sports chat
def joinchat(request, group_name):
    token = gettoken(request)
    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})

    else:
        code = GroupChats.objects.filter(GroupName=group_name).values_list("GroupId", flat=True)[0]
        sharetoken = GroupChats.objects.filter(GroupName=group_name).values_list("ShareToken", flat=True)[0]

        url = "https://api.groupme.com/v3/groups/" + code + "/join/" + sharetoken + "?token=" + token
        print(url)
        r = requests.post(url)
        #print(sharetoken)
        #print(r)
        #print(r.json()['response']['group']['share_url'])

        return render(request, 'chat/joinchat.html', {
            'group_id': mark_safe(json.dumps(code)),
            'group_name': mark_safe(json.dumps(group_name))
        })

# creates a chat in your own personal groupme application based on which one you click
def createchat(request, group_name):
    token = gettoken(request)

    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})
    else:

        url = 'https://api.groupme.com/v3/groups?token=' + token
        url = str(url)

        try:
            GroupChats.objects.filter(GroupName=group_name).values_list("GroupId", flat=True)[0]
            group_name = 'didn\'t create group ' + group_name
            return render(request, 'chat/chat.html', {
                # 'access_token': mark_safe(json.dumps(access_token)),
                'group_name': mark_safe(json.dumps(group_name))
            })

        except:

            chatname = "TigerMeet " + group_name
            data = {'name': chatname,
                    "share": True,}
            headers = {"Content-Type": "application/json"}
            r = requests.post(url, data=json.dumps(data), headers=headers)

            print(r.json()['response']['share_url'])
            shareurl = (r.json()['response']['share_url'])
            code = str(shareurl[-17:-9])
            sharetoken = str(shareurl[-8:])


            #database stuff
            #don't delete this line below! It is used to delete items in database
            #GroupChats.objects.filter(GroupName=group_name).delete()

            p = GroupChats(GroupName=group_name, GroupId=code, ShareToken=sharetoken)
            p.save()

            return render(request, 'chat/chat.html', {
                #'access_token': mark_safe(json.dumps(access_token)),
                'group_name': mark_safe(json.dumps(group_name))
            })


# unused
#def redirect(request):
 #   return render(request, 'chat/chat.html', {})



def todo(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos':todos
    }
    return render(request, 'chat/todo.html', context)

def add(request, group_name):
    token = gettoken(request)
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        time = request.POST['time']

        todo = Todo(title=title, text=text, time=time)
        todo.save()

        group_name = string(title) + string(text)
        url = '?access_token=' + string(token)
        allurl = '/makechat/' + group_name + url

        return redirect(url)
    else:
        return render(request, 'chat/add.html', {'access_token': mark_safe(json.dumps(token))})

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'chat/details.html', context)
