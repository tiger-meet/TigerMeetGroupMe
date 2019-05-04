from django.shortcuts import render, redirect
import requests
import json
import urllib.parse as urlparse
import urllib
from django.utils.safestring import mark_safe
from .models import GroupChats, SportsEvents, WorkingOutEvents, VideoGamesEvents, TransportationEvents, ProblemSetEvents, MiscellaneousEvents
from django.contrib import admin
import base64
from django.http import HttpResponse
import re
import copy

admin.site.register(GroupChats)
admin.site.register(SportsEvents)
admin.site.register(WorkingOutEvents)
admin.site.register(VideoGamesEvents)
admin.site.register(TransportationEvents)
admin.site.register(ProblemSetEvents)
admin.site.register(MiscellaneousEvents)

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
    temp_url = temp_url.replace('%3F', '?')
    temp_url = temp_url.replace('%3D', '=')
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
        try:
            token_list = token_dict['access_token']
        except:
            token_list = token_dict['?access_token']
        token = str(token_list[0])
        return token

def countandprune(todos):
    for todo in todos:

        groupid = getattr(todo, 'GroupId')
        makertoken = getattr(todo, 'MakerToken')
        url = 'https://api.groupme.com/v3/groups/' + groupid + '?token=' + makertoken
        r = requests.get(url)
        print(r.json()['meta']['code'])
        if r.json()['meta']['code'] == 404:
            todo.delete()
        else:
            todo.Size = len(r.json()['response']['members'])
            todo.save()

# loads the index page with authentication token
def index(request):
    # code for scrambling access tokens
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
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)

    not_host = request.META.get('RAW_URI')
    # case for a search
    if "search=" in not_host:

        # find the category for the database
        if group_name == "sports":
            event = copy.copy(SportsEvents)
        elif group_name == "workingout":
            event = copy.copy(WorkingOutEvents)
        elif group_name == "videogames":
            event = copy.copy(VideoGamesEvents)
        elif group_name == "transportation":
            event = copy.copy(TransportationEvents)
        elif group_name == "problemsetgroups":
            event = copy.copy(ProblemSetEvents)
        elif group_name == "miscellaneous":
            event = copy.copy(MiscellaneousEvents)

        if not_host.split("search=", 1)[1] != "":
            queryString = not_host.split("search=", 1)[1]
            todos = []
            for i in range(0, len(event.objects.all())):
                if queryString.lower() in event.objects.all()[i].title.lower():
                    todos.append(event.objects.all()[i])

            if "sortBy=Alphabetical" in not_host:
                todos.sort(key = lambda x: x.title)
                context = {
                    'access_token': mark_safe(json.dumps(encodedtoken)),
                    'group_name': mark_safe(json.dumps(group_name)),
                    'todos':todos
                }
                return render(request, 'chat/events.html', context)

            if "sortBy=Date" in not_host:
                todos.sort(key = lambda x: x.date)
                context = {
                    'access_token': mark_safe(json.dumps(encodedtoken)),
                    'group_name': mark_safe(json.dumps(group_name)),
                    'todos': todos
                }
                return render(request, 'chat/events.html', context)

            context = {
                'access_token': mark_safe(json.dumps(encodedtoken)),
                'group_name': mark_safe(json.dumps(group_name)),
                'todos':todos
            }
            return render(request, 'chat/events.html', context)

        elif "sortBy=Alphabetical" in not_host:
            todos = event.objects.order_by('title')
            context = {
                'access_token': mark_safe(json.dumps(encodedtoken)),
                'group_name': mark_safe(json.dumps(group_name)),
                'todos': todos
            }
            return render(request, 'chat/events.html/', context)

        elif "sortBy=Date" in not_host:
            todos = event.objects.order_by('date')
            context = {
                'access_token': mark_safe(json.dumps(encodedtoken)),
                'group_name': mark_safe(json.dumps(group_name)),
                'todos': todos
            }
            return render(request, 'chat/events.html/', context)

        else:
            todos = event.objects.all()
            context = {
                'access_token': mark_safe(json.dumps(encodedtoken)),
                'group_name': mark_safe(json.dumps(group_name)),
                'todos': todos
            }
            return render(request, 'chat/events.html', context)

    countandprune(SportsEvents.objects.all())
    countandprune(WorkingOutEvents.objects.all())
    countandprune(VideoGamesEvents.objects.all())
    countandprune(TransportationEvents.objects.all())
    countandprune(ProblemSetEvents.objects.all())
    countandprune(MiscellaneousEvents.objects.all())

    #create a count of the people in chats and check if they've been deleted
    if (group_name == 'sports'):
        otherTodos = SportsEvents.objects.exclude(MakerToken=token)
        myTodos = SportsEvents.objects.filter(MakerToken=token)
    elif (group_name == 'workingout'):
        otherTodos = WorkingOutEvents.objects.exclude(MakerToken=token)
        myTodos = WorkingOutEvents.objects.filter(MakerToken=token)
    elif (group_name == 'videogames'):
        otherTodos = VideoGamesEvents.objects.exclude(MakerToken=token)
        myTodos = VideoGamesEvents.objects.filter(MakerToken=token)
    elif (group_name == 'transportation'):
        otherTodos = TransportationEvents.objects.exclude(MakerToken=token)
        myTodos = TransportationEvents.objects.filter(MakerToken=token)
    elif (group_name == 'problemsetgroups'):
        otherTodos = ProblemSetEvents.objects.exclude(MakerToken=token)
        myTodos = ProblemSetEvents.objects.filter(MakerToken=token)
    elif (group_name == 'miscellaneous'):
        otherTodos = MiscellaneousEvents.objects.exclude(MakerToken=token)
        myTodos = MiscellaneousEvents.objects.filter(MakerToken=token)

    try:
        print(otherTodos)
        context = {
            'access_token': mark_safe(json.dumps(encodedtoken)),
            'group_name': mark_safe(json.dumps(group_name)),
            'otherTodos': otherTodos,
            'myTodos': myTodos
        }

    except:
        context = {
            'access_token': mark_safe(json.dumps(encodedtoken)),
            'group_name': mark_safe(json.dumps(group_name)),
            'otherTodos': "",
            'myTodos': myTodos
        }

    finally:
        if token == 'none':
            return render(request, 'chat/gmlogin.html', {})
        else:
            return render(request, 'chat/events.html', context)

# joins chat
def joinchat(request, group_name):
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

def add(request, group_name):
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)

    category_name = group_name

    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})
    else:

        url = 'https://api.groupme.com/v3/groups?token=' + token
        url = str(url)

        if(request.method == 'POST'):
            title = request.POST['title']
            place = request.POST['place']
            date = request.POST['date']
            time = request.POST['time']
            description = request.POST['description']

            print(title)
            print(place)
            print(date)
            print(time)
            print(description)
            name = title + ' (' + time + ', ' + date + ')'

            chatname = name + ' | TigerMeet '
            data = {'name': chatname,
                    "share": True, }
            headers = {"Content-Type": "application/json"}
            r = requests.post(url, data=json.dumps(data), headers=headers)

            print(r.json()['response']['share_url'])
            shareurl = (r.json()['response']['share_url'])
            code = str(shareurl[-17:-9])
            sharetoken = str(shareurl[-8:])

            if (group_name == 'sports'):
                todo = SportsEvents(title=title, place=place, date=date, time=time, description=description, GroupId=code, ShareToken=sharetoken, MakerToken=token, CategoryName=group_name)
            if (group_name == 'workingout'):
                todo = WorkingOutEvents(title=title, place=place, date=date, time=time, description=description, GroupId=code, ShareToken=sharetoken, MakerToken=token, CategoryName=group_name)
            if (group_name == 'videogames'):
                todo = VideoGamesEvents(title=title, place=place, date=date, time=time, description=description, GroupId=code, ShareToken=sharetoken, MakerToken=token, CategoryName=group_name)
            if (group_name == 'transportation'):
                todo = TransportationEvents(title=title, place=place, date=date, time=time, description=description, GroupId=code, ShareToken=sharetoken, MakerToken=token, CategoryName=group_name)
            if (group_name == 'problemsetgroups'):
                todo = ProblemSetEvents(title=title, place=place, date=date, time=time, description=description, GroupId=code, ShareToken=sharetoken, MakerToken=token, CategoryName=group_name)
            if (group_name == 'miscellaneous'):
                todo = MiscellaneousEvents(title=title, place=place, date=date, time=time, description=description, GroupId=code, ShareToken=sharetoken, MakerToken=token, CategoryName=group_name)

            todo.save()

            group_name = name
            url = '?access_token=' + encodedtoken
            allurl = '/makechat/' + group_name + url

            #return redirect('/')
            #change this so it doesn't just call createchat
            return render(request, 'chat/chat.html', {
                'access_token': mark_safe(json.dumps(encodedtoken)),
                'group_name': mark_safe(json.dumps(group_name)),
                'category_name': mark_safe(json.dumps(category_name))
            })

        else:
            return render(request, 'chat/add.html', {'access_token': mark_safe(json.dumps(encodedtoken)),
                                                    'group_name': mark_safe(json.dumps(group_name))})

def details(request, group_name, id):
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)

    if (group_name == 'sports'):
        todo = SportsEvents.objects.get(id=id)
    if (group_name == 'workingout'):
        todo = WorkingOutEvents.objects.get(id=id)
    if (group_name == 'videogames'):
        todo = VideoGamesEvents.objects.get(id=id)
    if (group_name == 'transportation'):
        todo = TransportationEvents.objects.get(id=id)
    if (group_name == 'problemsetgroups'):
        todo = ProblemSetEvents.objects.get(id=id)
    if (group_name == 'miscellaneous'):
        todo = MiscellaneousEvents.objects.get(id=id)

    if (todo.MakerToken == token):
        is_creator = True
    else:
        is_creator = False

    context = {
        'todo': todo,
        'access_token': mark_safe(json.dumps(encodedtoken)),
        'group_name': mark_safe(json.dumps(group_name)),
        'id': mark_safe(json.dumps(id)),
        'is_creator': is_creator
    }
    return render(request, 'chat/details.html', context)

def joinsubchat(request, id, group_name):
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)
    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})

    else:
        if (group_name == 'sports'):
            code = SportsEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
            sharetoken = SportsEvents.objects.filter(id=id).values_list("ShareToken", flat=True)[0]
            title = SportsEvents.objects.filter(id=id).values_list("title", flat=True)[0]
            time = SportsEvents.objects.filter(id=id).values_list("time", flat=True)[0]
        if (group_name == 'workingout'):
            code = WorkingOutEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
            sharetoken = WorkingOutEvents.objects.filter(id=id).values_list("ShareToken", flat=True)[0]
            title = WorkingOutEvents.objects.filter(id=id).values_list("title", flat=True)[0]
            time = WorkingOutEvents.objects.filter(id=id).values_list("time", flat=True)[0]
        if (group_name == 'videogames'):
            code = VideoGamesEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
            sharetoken = VideoGamesEvents.objects.filter(id=id).values_list("ShareToken", flat=True)[0]
            title = VideoGamesEvents.objects.filter(id=id).values_list("title", flat=True)[0]
            time = VideoGamesEvents.objects.filter(id=id).values_list("time", flat=True)[0]
        if (group_name == 'transportation'):
            code = TransportationEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
            sharetoken = TransportationEvents.objects.filter(id=id).values_list("ShareToken", flat=True)[0]
            title = TransportationEvents.objects.filter(id=id).values_list("title", flat=True)[0]
            time = TransportationEvents.objects.filter(id=id).values_list("time", flat=True)[0]
        if (group_name == 'problemsetgroups'):
            code = ProblemSetEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
            sharetoken = ProblemSetEvents.objects.filter(id=id).values_list("ShareToken", flat=True)[0]
            title = ProblemSetEvents.objects.filter(id=id).values_list("title", flat=True)[0]
            time = ProblemSetEvents.objects.filter(id=id).values_list("time", flat=True)[0]
        if (group_name == 'miscellaneous'):
            code = MiscellaneousEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
            sharetoken = MiscellaneousEvents.objects.filter(id=id).values_list("ShareToken", flat=True)[0]
            title = MiscellaneousEvents.objects.filter(id=id).values_list("title", flat=True)[0]
            time = MiscellaneousEvents.objects.filter(id=id).values_list("time", flat=True)[0]

        name = title + ' ' + time
        url = "https://api.groupme.com/v3/groups/" + code + "/join/" + sharetoken + "?token=" + token
        print(url)
        r = requests.post(url)
        #print(sharetoken)
        #print(r)
        #print(r.json()['response']['group']['share_url'])

        return render(request, 'chat/joinchat.html', {
            'group_id': mark_safe(json.dumps(code)),
            'group_name': mark_safe(json.dumps(name))
        })

def destroy(request, id, group_name):
    encodedtoken = gettoken(request)
    token = decodetoken(encodedtoken)
    if token == 'none':
        return render(request, 'chat/gmlogin.html', {})

    else:
        if (group_name == 'sports'):
            code = SportsEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
        if (group_name == 'workingout'):
            code = WorkingOutEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
        if (group_name == 'videogames'):
            code = VideoGamesEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
        if (group_name == 'transportation'):
            code = TransportationEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
        if (group_name == 'problemsetgroups'):
            code = ProblemSetEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]
        if (group_name == 'miscellaneous'):
            code = MiscellaneousEvents.objects.filter(id=id).values_list("GroupId", flat=True)[0]

        url = "https://api.groupme.com/v3/groups/" + code + "/destroy" + "?token=" + token
        print(url)
        r = requests.post(url)
        print(r)

        return render(request, 'chat/index.html', {'access_token': mark_safe(json.dumps(encodedtoken))})

def getgroupname(request):
    if request.method == 'GET':
        name = request.GET['group_name']
        token = request.GET['access_token']
    return HttpResponse(name, token)
