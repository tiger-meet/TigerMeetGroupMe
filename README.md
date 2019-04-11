# TigerMeetGroupMe
When you clone the repository:
1. make sure you have your own groupme developer application
2. change gmlogin.html to redirect to you own callback url (found in developer application page)
3. host it on your own heroku server
4. set the groupme developer application callback url to "https://(your_heroku_site_name) + "/index"

If you change static files, make sure to run "heroku run python manage.py collectstatic"
