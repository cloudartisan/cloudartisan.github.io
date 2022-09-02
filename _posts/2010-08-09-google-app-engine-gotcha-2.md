public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['google app engine', 'paas', 'python']
published: 2010-08-09
title: Google App Engine Gotcha 2
slug: google-app-engine-gotcha-2
summary: Inflexible outbound timeouts are a pain in the...

For _Google App Engine: Gotcha #2_ I choose the default 5 second timeout on `urlfetch`. This function is part of the Google App Engine's API and applies to both Python and Java.

The [Python documentation](http://code.google.com/appengine/docs/python/urlfetch/fetchfunction.html) states:

> The deadline can be up to a maximum of 10 seconds. If deadline is None, the deadline is set to 5 seconds.

  
The [Java documentation](http://code.google.com/appengine/docs/java/urlfetch/overview.html) states:

> You can set a deadline for a request, the most amount of time the service will wait for a response. By default, the deadline for a fetch is 5 seconds.  The maximum deadline is 10 seconds.


Sooner or later you'll find yourself writing code to fetch the contents of a URL or drive a RESTful API. Something like this:


    :::python
    from google.appengine.api import urlfetch
    urlfetch.fetch('http://www.cloudartisan.com')


If you're lucky enough to be talking to snappy APIs or zippy web sites, you'll be fine. If not, you'll soon stumble upon the following traceback:


    :::text
    ApplicationError: 2 timed out
    Traceback (most recent call last):
      File "/path/to/webapp/__init__.py", line 507, in __call__
        handler.get(*groups)
      File "/path/to/myapp/main.py", line 62, in get
        result = urlfetch.fetch(...)
      File "/path/to/urlfetch.py", line 241, in fetch
        return rpc.get_result()
      File "/path/to/apiproxy_stub_map.py", line 501, in get_result
        return self.__get_result_hook(self)
      File "/path/to/urlfetch.py", line 325, in _get_fetch_result
        raise DownloadError(str(err))
    DownloadError: ApplicationError: 2 timed out


Lucky you. If you're dealing with an external API, over which you have no control, and it is slow to respond... **WHAMMO!**

What can you do about this? Well, you can increase the timeout to its maximum: 10 seconds.

If you're still hit by the timeout, it's time to consider trickier options.

Perhaps you could try breaking your request into multiple requests?

Perhaps you could fire off the request, ignore the timeout, wait a short period, then query again for the results of the request?

Just remember, your handler also has a maximum of 30 seconds to handle a web request, so don't take too long...
