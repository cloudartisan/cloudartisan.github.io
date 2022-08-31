public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['gae', 'google app engine', 'google apps', 'gotcha', 'paas', 'sdc', 'urlfetch']
published: 2010-08-29
title: Google App Engine Gotcha 3
slug: google-app-engine-gotcha-3
summary: Do I really need to whitelist every Google IP address ever?!

## What's the problem?

Well, gotcha #3 is a simple but annoying one. The `urlfetch` call does not use a fixed source IP address.

It makes sense, when you think about it. Google App Engine is ([apparently](http://code.google.com/appengine/docs/whatisgoogleappengine.html)) distributed all over the place, with no guarantee of where your code will run at any given time. I presume this is so that Google are free to move applications between data centres to optimise uptime and performance.

## Why is this a problem?

Unfortunately, some APIs (eg, eNom) still require users to register their source IP so that it can be whitelisted. If you can't register an IP you can't use their API.

Google are really not making it easy to integrate Google App Engine with external (slow/legacy) APIs. Refer to [Google App Engine: Gotcha #2](http://www.cloudartisan.com/2010/08/google-app-engine-gotcha-2/) for another issue with `urlfetch` and consuming external APIs...

## How did I test this?

I created a simple handler in two different Google App Engine applications; the same handler in both.

In my `views.py`:

    
    :::python
    class UrlFetchTestHandler(webapp.RequestHandler):
        def get(self):
            from google.appengine.api import urlfetch
            url = "http://www.cloudartisan.com/?googleappengine=true"
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                self.response.out.write(result.content)

  
In my `index.py`:

    
    :::python
    from google.appengine.ext import webapp
    from google.appengine.ext.webapp.util import run_wsgi_app
    from handlers import views  
    application = webapp.WSGIApplication([
                        ('/urlfetchtest', views.UrlFetchTestHandler)],
                        debug=True)  
    
    def main():
        run_wsgi_app(application)  
    
    if __name__ == '__main__':
        main()

  
I then visited `/urlfetchtest` a few times in each of these applications. I also asked some friends to do the same.

The logs showed:

    
    :::text
    root@hal:/var/log/apache2# grep googleappengine cloudartisan.com-access.log
    74.125.154.83 - - [29/Aug/2010:13:17:23 +1000] "GET /?googleappengine=true HTTP/1.1" 200 19528 "-" "AppEngine-Google; (+http://code.google.com/appengine; appid: cloudzuum)"
    72.14.212.81 - - [29/Aug/2010:13:18:05 +1000] "GET /?googleappengine=true HTTP/1.1" 200 19522 "-" "AppEngine-Google; (+http://code.google.com/appengine; appid: cloudomate)"
    74.125.154.80 - - [29/Aug/2010:13:18:26 +1000] "GET /?googleappengine=true HTTP/1.1" 200 19522 "-" "AppEngine-Google; (+http://code.google.com/appengine; appid: cloudzuum)"
    72.14.212.87 - - [29/Aug/2010:13:18:28 +1000] "GET /?googleappengine=true HTTP/1.1" 200 19522 "-" "AppEngine-Google; (+http://code.google.com/appengine; appid: cloudomate)"
    74.125.154.83 - - [29/Aug/2010:13:59:31 +1000] "GET /?googleappengine=true HTTP/1.1" 200 19522 "-" "AppEngine-Google; (+http://code.google.com/appengine; appid: cloudzuum)"
    74.125.154.81 - - [29/Aug/2010:13:59:44 +1000] "GET /?googleappengine=true HTTP/1.1" 200 19522 "-" "AppEngine-Google; (+http://code.google.com/appengine; appid: cloudzuum)"
    72.14.212.81 - - [29/Aug/2010:13:59:47 +1000] "GET /?googleappengine=true HTTP/1.1" 200 19522 "-" "AppEngine-Google; (+http://code.google.com/appengine; appid: cloudzuum)"
    root@hal:/var/log/apache2#


Notice there are some common network addresses in the above requests (`74.125.154.X`, `72.14.212.X`). Apparently `urlfetch` calls could originate from any of the following networks:


    :::text
    david@continuity:~$ dig +short _netblocks.google.com TXT 
    "v=spf1 ip4:216.239.32.0/19 ip4:64.233.160.0/19 ip4:66.249.80.0/20 ip4:72.14.192.0/18 ip4:209.85.128.0/17 ip4:66.102.0.0/20 ip4:74.125.0.0/16 ip4:64.18.0.0/20 ip4:207.126.144.0/20 ip4:173.194.0.0/16 ?all"
    david@continuity:~$ 


_Cripes!_ They're all bigger than class C.

## What's the solution?

Well, there are a few. Let's go through them from definitely most annoying to probably least annoying...

You _might_ be able to get away with whitelisting the Google networks listed above. I doubt it, though. If your API provider requires whitelisted IP addresses, I doubt they're going to whitelist entire networks. Also, you would have to continually monitor those addresses in case they change. Really annoying. It could also fail at inopportune moments.

Directing requests via a proxy is the most obvious simple hack that comes to mind. This could be done using a cheap VPS or a server on Amazon EC2 with an Elastic IP address. Of course, doing this defeats some of the purpose behind using Google App Engine in the first place. Quite annoying.

Lastly, [this thread](http://groups.google.com/group/google-appengine/browse_thread/thread/d1e592a4a535378a/318ffadfb5d6c949?lnk=gst&q=ip+address#318ffadfb5d6c949) seems to indicate that Google Apps and the [SDC (Secure Data Connector)](http://code.google.com/securedataconnector/) could be used to get around the problem. I don't know if the SDC can be used with Google Apps Standard Edition or if it requires Google Apps Premium Edition (currently $50 per user per year). I have not tested it yet. Probably least annoying.

So, there you go...

Stay tuned...

You should [follow me on twitter](http://twitter.com/davidltaylor).
