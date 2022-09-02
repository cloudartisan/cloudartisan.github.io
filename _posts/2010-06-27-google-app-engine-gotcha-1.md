public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['google app engine', 'paas', 'python']
published: 2010-06-27
title: Google App Engine Gotcha 1
slug: google-app-engine-gotcha-1
summary: No smtplib for you!

I like Google App Engine. However, there are a number of _gotchas_ that can creep up on you. Especially if you dive right in without doing any reading first.

Here's gotcha #1...

A number of standard Python modules are not available or only provide limited functionality. Click [here](http://code.google.com/appengine/kb/libraries.html) to see Google App Engine's list of enabled, partially-enabled and empty modules.

Sometimes developing for Google App Engine isn't straightforward and requires a little imagination. However, most of the time there's a simple alternative; it just takes a little reading. For example, if you want to send e-mail on Google App Engine you can't use Python's `smtplib` (because it relies on `socket`, which is implemented as an empty module). Instead, you would do the following:

    :::python
    from google.appengine.api import mail
    mail.send_mail(
        sender="<from address>",
        to="<to address>",
        subject="sending e-mail on Google App Engine...",
        body="... is easy once you know how"
    )

There are more gotchas, this is just the first that I've had time to write about. Stay tuned...
