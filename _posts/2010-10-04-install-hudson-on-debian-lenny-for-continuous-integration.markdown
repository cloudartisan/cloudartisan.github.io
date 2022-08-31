public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['debian', 'general', 'hudson', 'software development', 'system administration']
published: 2010-10-04
title: Install Hudson on Debian Lenny for Continuous Integration
slug: install-hudson-on-debian-lenny-for-continuous-integration
summary: In this post I provide instructions for installing Hudson on Debian Lenny with some basic security...

I found that Hudson depends on `daemon` but it doesn't install automatically.  So, before we get started:


    :::bash
    apt-get install daemon


Now that's out of the way, we need to grab the Hudson key and install the package:


    :::bash
    wget -q -O - http://hudson-ci.org/debian/hudson-ci.org.key | apt-key add -
    cd /tmp
    wget http://hudson-ci.org/latest/debian/hudson.deb
    dpkg --install ./hudson.deb


If everything went well you'll see Hudson running:


    ps auxw | grep hudson
    hudson 9101 0.0 0.1 2108 516 ? Ss 09:59 0:00 /usr/bin/daemon --name=hudson --inherit --env=HUDSON_HOME=/var/lib/hudson --output=/var/log/hudson/hudson.log --pidfile=/var/run/hudson/hudson.pid -- /usr/bin/java -jar /usr/share/hudson/hudson.war --webroot=/var/run/hudson/war --httpPort=8080 --ajp13Port=-1
    hudson 9103 18.9 10.3 297064 52660 ? Sl 09:59 0:03 /usr/bin/java -jar /usr/share/hudson/hudson.war --webroot=/var/run/hudson/war --httpPort=8080 --ajp13Port=-1


... and listening on port 8080:


    root@hal:/tmp# netstat -lnp | grep 8080
    tcp6 0 0 :::8080 :::* LISTEN 9103/java


It's installed... but it isn't secured. By default the package has security disabled and anyone can do anything they want. Not awesome.

Using your browser, go to your installation of Hudson (`http://<your server>:8080`).

Click on Manage Hudson:

[caption id="attachment_254" align="aligncenter" width="660" caption="Hudson Main Page"][![Hudson Main Page](/media/img/2010/10/Hudson-Main-Page.png)](/media/img/2010/10/Hudson-Main-Page.png)[/caption]

Click on Configure System:

[caption id="attachment_255" align="aligncenter" width="851" caption="Manage Hudson"][![Manage Hudson](/media/img/2010/10/Manage-Hudson.png)](/media/img/2010/10/Manage-Hudson.png)[/caption]

In your Hudson configuration look for the _Enable security_ setting:

[caption id="attachment_256" align="aligncenter" width="919" caption="Hudson Settings"][![Hudson Settings](/media/img/2010/10/Hudson-Settings.png)](/media/img/2010/10/Hudson-Settings.png)[/caption]

If you trust your system users the the simplest approach is to select _Enable security_, select _Unix user/group database_, and select _Logged-in users can do anything_:

[caption id="attachment_260" align="aligncenter" width="653" caption="Hudson Enable Security"][![Hudson Enable Security](/media/img/2010/10/Hudson-Enable-Security.png)](/media/img/2010/10/Hudson-Enable-Security.png)[/caption]

Lastly, click _Save_.

There you have it, Hudson installed on Debian Lenny with some basic security.

You should [follow me on twitter](http://twitter.com/davidltaylor).
