public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['general', 'google app engine', 'paas', 'python', 'software development']
published: 2010-10-18
title: Migrating from Google App Engine to Django
slug: migrating-from-google-app-engine-to-django
summary: Yup, I'm migrating from Google App Engine to Django.  In this post I go over some of the key differences and considerations...

Unfortunately, I had to migrate one of my projects from Google App Engine to Django on a self-managed server. I didn't want to do this. See [Google App Engine Gotcha #2](http://www.cloudartisan.com/2010/08/google-app-engine-gotcha-2/) and [Google App Engine Gotcha #3](http://www.cloudartisan.com/2010/08/google-app-engine-gotcha-3/) for the main reasons. Those headaches became bad enough that I had to bite the bullet and migrate out of Google App Engine.

_It's not for the faint-hearted..._

## Why Google App Engine In The First Place?
 
Google App Engine is a PaaS (Platform as a Service). PaaS products eliminate the need for lower-level server management and, if they're good, make it very easy to write and maintain code for that platform.

Migrating away from a PaaS means having to handle the server management again and having to deal with niggly code problems you'd prefer to forget.

## Is Django Hard?

No. It's just very different to using Google App Engine's `webapp` approach.

Note, it's even possible to [run Django on Google App Engine](http://code.google.com/appengine/articles/django.html). If you started out using Django on Google App Engine, this article ain't for you... you've got it easy... you already know what you're doing. This article is for those, like me, who started with `webapp` on Google App Engine.

I've tried to gather together the resources I found most useful in moving from Google App Engine to Django. I've also tried to provide some helpful advice and snippets on translating certain features between the two. Hopefully this stuff will help someone get through it a bit quicker than I did...

## A Gentle Overview of Django

IBM have an article in their DeveloperWorks library titled [Deploying Django applications to a production server](http://www.ibm.com/developerworks/opensource/library/os-django/). As an article on deploying Django projects to production... well... it sucks.  However, as a gentle overview of Django concepts, it rocks. It also provides some insight into the differences between development and production environments.

## Project/Application Layout

OK, this seems a persnickety subject in Django circles.  The best overall guide I could find is [http://blog.zacharyvoase.com/2010/02/03/django-project-conventions/](http://blog.zacharyvoase.com/2010/02/03/django-project-conventions/).

While you're at it, you'll want to think about how to deal with filesystem paths:

  * [http://morethanseven.net/2009/02/11/django-settings-tip-setting-relative-paths.html](http://morethanseven.net/2009/02/11/django-settings-tip-setting-relative-paths.html)
  * [http://gnuvince.wordpress.com/2007/12/22/django-paths-and-urls/](http://gnuvince.wordpress.com/2007/12/22/django-paths-and-urls/)

Yup, filesystems... I bet you forgot about those while you were living it up on Google App Engine!

## User Management

Depending on what you're hoping to achieve, you can take care of this with initial data, fixtures, and the administrative interface.

## Prepopulate Data

This is actually easier with Django than it is with Google App Engine. Of course, that's partly because we now have access to files. FILES!

Django takes care of prepopulating data with fixtures (which can be JSON, XML, or even Python code) or simple hooks into events. Check out [http://docs.djangoproject.com/en/dev/howto/initial-data/](http://docs.djangoproject.com/en/dev/howto/initial-data/).

The most common use for this is prepopulating users and groups.

## Administration Interface

You can add an administration interface to your application by adding something like the following to your project's `urls.py`:


    :::python
    # Enable the administration interface
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns = patterns('',
        # Using the admin/doc line below, add 'django.contrib.admindocs'
        # to INSTALLED_APPS to enable admin documentation:
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        # Enable the admin interface
        (r'^admin/', include(admin.site.urls)),
    )


This will come in handy when you need to play around with users, groups, permissions, etc.

## Performance / Scaling

Now that you're responsible for the underlying platform, you'll need to give some thought to performance and scaling. There are some helpful responses in this Stack Overflow thread: [http://stackoverflow.com/questions/886221/does-django-scale](http://stackoverflow.com/questions/886221/does-django-scale).

## The Case For Django

Django does give you something that Google App Engine doesn't: _flexibility_.

If you want to use an RDBMS, go nuts, it'll be easy. It's much harder to model relationships in Google App Engine.

Also, there's inter-application reuse. Django requires that you define URLs and import applications into your site/project. This means you can reuse applications in other sites by simply importing them. If you develop an awesome social data mining application, you can reuse it in multiple Django sites/projects by simply importing it. However, in Google App Engine you'd need to maintain multiple copies of the code in each site and upload it along with each site. Any time you add somebody else's awesome Google App Engine library to your own application you'll feel this pain.

## Summary

Django is awesome... for what it is... a framework for developing web applications when you need (or want) to be responsible for everything from the ground up. The same can be said if you've had to move from Heroku or Engine Yard to running your own Ruby on Rails or Sinatra application.

For some, Google App Engine can be considered Django without the irritating server management bits. For others, Django can feel like Google App Engine with a healthy dose of flexibility thrown in. Personally, I just want to get the code out of the way. If Google ever _fixes_ the limitations I've come across I'll jump back over to Google App Engine.

If you've got some helpful tidbits for people moving from Google App Engine to Django, let me know, I'll add them to the post.

In the meantime, [follow me on twitter...](http://twitter.com/davidltaylor)
