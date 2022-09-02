public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['djangy', 'general', 'paas', 'python', 'software development']
published: 2010-12-04
title: My first Djangy project (local testing)
slug: my-first-djangy-project-local-testing

In my [previous post](http://www.cloudartisan.com/2010/12/my-first-djangy-project-initial-testing/) I knocked out some simple code and pushed it straight to Djangy. I didn't even test it locally first (_gosh shock horror aghast_)! Well, that must end... now.

A Djangy project is, in it's heart of hearts, a Django project that you've shoved out your door into the big bad world. And the great thing about Django projects... you can run them locally for testing.

Simply go to your project's directory. In there you'll find `manage.py`. This handy script will do a lot of project management tasks, but the main one I'm interested in is running a local version of my project.


    :::text
    david@continuity:~/Git/djangy/rightscalefeed/rightscalefeed$ python manage.py runserver
    Validating models...
    0 errors found  
    Django version 1.2.3, using settings 'rightscalefeed.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


It's as simple as that. When I visit the address I can see my site is working.  I can also go back to my terminal and check the log:


    :::text
    [04/Dec/2010 05:19:36] "GET / HTTP/1.1" 200 1001


In this installment I've shown how easy it is to test your Djangy site locally before pushing it out the door. Stay tuned, next time I'll tackle something more meaty: user registration.

[Follow me on Twitter](http://twitter.com/davidltaylor). It's free.

Cheers!
