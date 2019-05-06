# TigerMeet

## Table of Contents

* [Details](#details)
* [Setup](#setup)
* [Try](#try)

## Details

TigerMeet is a web application that enables Princeton University students to connect with other students for recreation, transportation, and academic coordination. It is divided into sections of general interest (i.e. Sports, Transportation) each with a general chat as well as the ability to create specific events with chatrooms for users to connect.

## Setup
```
$ git clone "https://github.com/tiger-meet/TigerMeetGroupMe"
$ cd TigerMeetGroupMe
$ python -m venv venv
$ . venv/bin/activate (OR . venv/Scripts/activate on Windows)
(venv) $ python -m pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```
When you clone the repository:
1. Make sure you have your own GroupMe developer application
2. Change gmlogin.html to redirect to you own callback url (found in developer application page)
3. Host it on your own Heroku server
4. Set the GroupMe developer application callback url to "https://{{ your_heroku_site_name }}" + "/index"
5. Update that PostgreSQL database settings in settings.py to that on your Heroku site

If you change static files, make sure to run "python manage.py collectstatic."

To upload changes back to GitHub:
```
git checkout -b "your_branch_name" (your_branch_name is whatever you want to call it)
...
git push origin your_branch_name
```
Then, go to GitHub, and create a pull request and merge it.

## Try

<a href="https://tigermeet.herokuapp.com">https://tigermeet.herokuapp.com</a>