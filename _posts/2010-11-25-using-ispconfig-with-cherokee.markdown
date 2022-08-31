public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['general', 'ispconfig', 'system administration']
published: 2010-11-25
title: Using ISPConfig with Cherokee
slug: using-ispconfig-with-cherokee

The [Cherokee Project](http://www.cherokee-project.com/) describes Cherokee as:

> a very fast, flexible and easy to configure Web Server. It supports the widespread technologies nowadays: FastCGI, SCGI, PHP, CGI, uWSGI, SSI, TLS and SSL encrypted connections, Virtual hosts, Authentication, on the fly encoding, Load Balancing, Apache compatible log files, Data Base Balancing, Reverse HTTP Proxy, Traffic Shaper, Video Streaming and much more.

It makes a great alternative to the swiss-army chainsaw that is [Apache](http://www.apache.org) and the documentation, wizards, and screencasts make it infinitely more friendly than [nginx](http://nginx.net).

[ISPConfig](http://www.ispconfig.org/) is an Open Source control panel for providing managed hosting. If your needs are simple enough, it makes a decent alternative to heavyweights such as [cPanel/WHM](http://www.cpanel.net/) or [Parallels Plesk](http://www.parallels.com/plesk/). In my case it makes it easier to provide virtual hosting for family members.

The thing is...

The ISPConfig installer comes with automagic support for configuring Apache and nginx, but no support for configuring Cherokee.

On top of that...

The default install of ISPConfig doesn't play well with Cherokee.

There are some very good instructions for installing ISPConfig on various distributions [here](http://www.ispconfig.org/ispconfig-3/documentation/), so I won't repeat them.

Also, I've previously written about installing Cherokee on Ubuntu and Debian Lenny (using the testing repository):

  * [Adding the Cherokee Web Server PPA to Ubuntu](http://www.cloudartisan.com/2010/11/adding-the-cherokee-web-server-ppa-to-ubuntu/)
  * [Install Cherokee (testing) on Debian Lenny](http://www.cloudartisan.com/2010/10/install-cherokee-testing-on-debian-lenny/)
  
Once you're past that, you need to get them both to work together.

First you'll need to fire up `cherokee-admin` before you can configure a _vServer_ to serve ISPConfig. The easiest way is to run the following on your server:


    :::text
    # cherokee-admin -b
    Cherokee Web Server 1.0.10 (Nov 25 2010): Listening on port ALL:9090, TLS
    disabled, IPv6 enabled, using epoll, 4096 fds system limit, max. 2041
    connections, caching I/O, 20 threads, 102 connections per thread, standard
    scheduling policy  
    Login:
      User:              admin
      One-time Password: aryusp7DBcNZESml  
    Web Interface:
      URL:               http://localhost:9090/

  
_Note: the administration interface is now available, unencrypted, to the world on port 9090. Don't leave it this way once you're done._

Point your browser at your server on port 9090 and log in.

[![Cherokee Admin Login](/media/img/2010/11/Cherokee-Admin-Login-300x160.png)](/media/img/2010/11/Cherokee-Admin-Login.png)

Next, click on the `vServers` tab up the top and then the plus sign in the top-left corner:

[![Add vServer](/media/img/2010/11/Add-vServer.png)](/media/img/2010/11/Add-vServer.png)

Select `Languages` then `PHP` and click on `Add`:

[![Select Language PHP](/media/img/2010/11/Select-Language-PHP-300x189.png)](/media/img/2010/11/Select-Language-PHP.png)

Then click `Next`:

[![Welcome to the PHP Wizard](/media/img/2010/11/Welcome-to-the-PHP-Wizard-300x129.png)](/media/img/2010/11/Welcome-to-the-PHP-Wizard.png)

Enter the document root (probably `/var/www/ispconfig` unless you strayed from the recommended default when installing ISPConfig) and click `Next`:

[![Document Root](/media/img/2010/11/Document-Root-300x140.png)](/media/img/2010/11/Document-Root.png)

Enter your hostname, choose whether you want to use the same logging configuration as an existing site, then click `Create`:

[![Create New Virtual Server](/media/img/2010/11/Create-New-Virtual-Server-300x173.png)](/media/img/2010/11/Create-New-Virtual-Server.png)

Unless you have a simple Cherokee configuration and plan to keep it that way, (which, if you need ISPConfig, is unlikely), you'll want to reconfigure the `Host Match` tab so that your new site matches on wildcards, regular expressions or server IP. For example:

[![Host Match Wildcards](/media/img/2010/11/Host-Match-Wildcards-300x141.png)](/media/img/2010/11/Host-Match-Wildcards.png)

and:

[![Add New Wildcard](/media/img/2010/11/Add-New-Wildcard-300x139.png)](/media/img/2010/11/Add-New-Wildcard.png)

Once you're done, click on `SAVE` in the top-right corner, followed by `Graceful restart`:

[![Save Configuration Graceful Restart](/media/img/2010/11/Save-Configuration-Graceful-Restart-300x97.png)](/media/img/2010/11/Save-Configuration-Graceful-Restart.png)

Ordinarily, you'd expect that you might be finished at this point... but you're not. If you try to visit the site now you will either get `404` (Page Not Found) or `504` (Gateway Timeout) errors.

What's going on...?

ISPConfig is typically installed in `/usr/local/ispconfig` and a symbolic link at `/var/www/ispconfig` points to a location beneath that. All the directories and files are owned by the `ispconfig` user and the `ispconfig` group with `0750` permissions. That seems to pose a problem. Although `cherokee-worker` and `php-cgi` run as `www-data` and `www-data` is a member of the `ispconfig` group, that does not seem to be sufficient.

Now, I admit, I got bored at this point before digging any further. Also, Cherokee is not extremely helpful when it comes to error messages and debugging. I changed the ownership of the files and directories to the `www- data` user and group and everything started to work. That was good enough for me. To do the same:


    :::text
    # chown -R www-data:www-data /usr/local/ispconfig


Try loading the site again. As long as the usual culprits are OK (eg, DNS) ISPConfig should now be working.

_Caveat: these permissions might pose a problem for future upgrades to ISPConfig. Also, it's the easy way out... I became bored and gave up before figuring out exactly what was experiencing permissions problems. If you know, let me know, I'll update the post._

You should [subscribe to my feed](http://www.cloudartisan.com/feed/) and [follow me on twitter](http://twitter.com/davidltaylor).

Cheers!
