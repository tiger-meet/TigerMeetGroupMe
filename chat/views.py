from django.shortcuts import render, redirect
import requests
import json
import urllib.parse as urlparse
from django.utils.safestring import mark_safe
from .models import GroupChats, SportsEvents, WorkingOutEvents, VideoGamesEvents, TransportationEvents, ProblemSetEvents, MiscellaneousEvents
from django.contrib import admin
import base64

admin.site.register(GroupChats)
admin.site.register(SportsEvents)

def encodetoken(token):
    bytestoken = token.encode()
    b64bytestoken = base64.b64encode(bytestoken)
    b64stringtoken = b64bytestoken.decode()
    return b64stringtoken

def decodetoken(encodedtoken):
    b64bytestoken = encodedtoken.encode()
    bytestoken = base64.b64decode(b64bytestoken)
    token = bytestoken.decode()
    return token


def gettoken(request):
    http_host = request.META.get('HTTP_HOST')
    not_host = request.META.get('RAW_URI')
    temp_url = 'https://' + http_host + not_host

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
    #code for scrambling access tokens
    token = gettoken(request)

    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})
        #print(token)

    elif len(token) == 32 or len(token) == 40:
        print(token)
        encodedtoken = encodetoken(token)
        http_host = request.META.get('HTTP_HOST')
        url = 'https://' + http_host + '/index/' + '?access_token=' + encodedtoken
        return redirect(url)

    else:
        print(token)
        encodedtoken = token
        return render(request, 'chat/index.html', {'access_token': mark_safe(json.dumps(encodedtoken))})

# loads the about page
def about(request):
    return render(request, 'chat/about.html', {})

# loads the groupme authentication page
def gmlogin(request):
    return render(request, 'chat/gmlogin.html', {})

# loads the events page
def events(request, group_name):
    #token = gettoken(request)
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)

    if (group_name == 'sports'):
        todos = SportsEvents.objects.all()[:10]
    elif (group_name == 'workingout'):
        todos = WorkingOutEvents.objects.all()[:10]
    elif (group_name == 'videogames'):
        todos = VideoGamesEvents.objects.all()[:10]
    elif (group_name == 'transportation'):
        todos = TransportationEvents.objects.all()[:10]
    elif (group_name == 'problemsetgroups'):
        todos = ProblemSetEvents.objects.all()[:10]
    elif (group_name == 'miscellaneous'):
        todos = MiscellaneousEvents.objects.all()[:10]

    context = {
        'todos':todos
    }
    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})
    else:
        return render(request, 'chat/events.html',{'access_token': mark_safe(json.dumps(encodedtoken)),
                                                    'group_name': mark_safe(json.dumps(group_name)),
                                                    } )

# joins sports chat
def joinchat(request, group_name):
    #token = gettoken(request)
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)
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
    #token = gettoken(request)
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)

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
    todos = VideoGamesEvents.objects.all()[:10]

    context = {
        'todos':todos
    }
    return render(request, 'chat/todo.html', context)

def add(request, group_name):
    #token = gettoken(request)
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)

    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        time = request.POST['time']

        print(title)
        print(text)
        print(time)

        if (group_name == 'sports'):
            todo = SportsEvents(title=title, text=text, time=time)
        elif (group_name == 'workingout'):
            todo = WorkingOutEvents(title=title, text=text, time=time)
        elif (group_name == 'videogames'):
            todo = VideoGamesEvents(title=title, text=text, time=time)
        elif (group_name == 'transportation'):
            todo = TransportationEvents(title=title, text=text, time=time)
        elif (group_name == 'problemsetgroups'):
            todo = ProblemSetEvents(title=title, text=text, time=time)
        elif (group_name == 'miscellaneous'):
            todo = MiscellaneousEvents(title=title, text=text, time=time)

        todo.save()

        group_name = title + time
        url = '?access_token=' + encodedtoken
        allurl = '/makechat/' + group_name + url

        #return redirect('/')
        return redirect(allurl)
    else:
        return render(request, 'chat/add.html', {'access_token': mark_safe(json.dumps(encodedtoken)), 
                                                'group_name': mark_safe(json.dumps(group_name))})

def details(request, group_name, id):
    
    if (group_name == 'sports'):
        todo = SportsEvents.objects.get(id=id)
    elif (group_name == 'workingout'):
        todo = WorkingOutEvents.objects.get(id=id)
    elif (group_name == 'videogames'):
        todo = VideoGamesEvents.objects.get(id=id)
    elif (group_name == 'transportation'):
        todo = TransportationEvents.objects.get(id=id)
    elif (group_name == 'problemsetgroups'):
        todo = ProblemSetEvents.objects.get(id=id)
    elif (group_name == 'miscellaneous'):
        todo = MiscellaneousEvents.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'chat/details.html', context)
