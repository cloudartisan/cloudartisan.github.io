public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['djangy', 'general', 'paas', 'paas', 'python', 'software development']
published: 2010-12-02
title: My first Djangy project (initial testing)
slug: my-first-djangy-project-initial-testing

My first Djangy project will be an application called `rightscalefeed`. It will pull down a user's RightScale event feed. Ideally, I'd like to transform the feed into a WebSocket, suitable for continuous updates, perhaps for display in a data centre or network operations centre.

I may have bitten off more than I can chew, as I'm not sure Django (or Djangy's environment) has WebSocket support yet, but we'll see...

First, I need Djangy:


    :::text
    # sudo easy_install djangy


I need a work environment for the project. Djangy uses git for releases, so:


    :::text
    # mkdir -p Projects/djangy/rightscalefeed
    # cd Projects/djangy/rightscalefeed
    # git init .


Next, I get started creating the Djangy application:


    :::text
    # djangy create
    Please enter your application name: rightscalefeed  
    Enter your email address: david@cloudartisan.com
    Please enter your password:  
    Using /home/david/.ssh/id_rsa.pub as your public key...  
    Application created.  Now you can run 'git push djangy master'.


That's the Djangy side of things, but before I push the project I need to take care of the Django side of things (ie, write some code).


    :::text
    # django-admin.py startproject rightscalefeed
    # cd rightscalefeed
    # django-admin.py startapp feed2ws


In `rightscalefeed/urls.py` I have:



    :::python
    from django.conf.urls.defaults import *  
    urlpatterns = patterns('',
        (r'^$', 'feed2ws.views.index')
    )



In `rightscalefeed/feed2ws/views.py` I have:



    :::python
    from django.http import HttpResponse  
    def index(request):
        return HttpResponse('testing')



I intend to use `feedparser`, so I have added it to `djangy.eggs`:


    :::text
    Django
    South
    feedparser


Now to commit everything, push it to Djangy, and test:


    :::text
    # git add .
    # git commit -a -m 'Initial release'
    [master fa7b52b] Initial release
     2 files changed, 10 insertions(+), 1 deletions(-)
    # git push djangy master
    The authenticity of host 'api.djangy.com (184.73.176.148)' can't be established.
    RSA key fingerprint is e0:03:fd:46:b2:3d:22:bc:d3:f8:96:6f:c4:62:b2:d5.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'api.djangy.com,184.73.176.148' (RSA) to the list of known hosts.
    Counting objects: 22, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (18/18), done.
    Writing objects: 100% (22/22), 3.83 KiB, done.
    Total 22 (delta 4), reused 0 (delta 0)
    remote: 
    remote: 
    remote: Welcome to Djangy!
    remote: 
    remote: Deploying project rightscalefeed.
    remote: 
    remote: Cloning git repository... Done.
    remote: 
    remote: Creating production settings.py file... Done.
    remote: 
    remote: Installing dependencies...
    remote: Installing Django... Success.
    remote: Installing South... Success.
    remote: Installing feedparser... Success.
    remote: Installing gunicorn... Success.
    remote: Done.
    remote: 
    remote: Saving bundle info... Done.
    remote: 
    remote: Deploying to worker hosts... Done.
    remote: 
    To git@api.djangy.com:rightscalefeed.git
     * [new branch]      master -> master


Now I can test the project by visiting [http://rightscalefeed.djangy.com](http://rightscalefeed.djangy.com) in my browser:

[![Testing rightscalefeed.djangy.com](/media/img/2010/11/rightscalefeed.djangy.com-testing-300x174.png)](/media/img/2010/11/rightscalefeed.djangy.com-testing.png)

Awesome! It worked.

I haven't done anything interesting with RightScale feeds yet, but I've shown how easy it can be to deploy a simple Django project to Djangy.

Stay tuned to see if I've bitten off more than I can chew. [Subscribe to my feed](http://feedburner.google.com/cloudartisan) and [follow me on Twitter](http://twitter.com/davidltaylor). It's free.

Cheers!
