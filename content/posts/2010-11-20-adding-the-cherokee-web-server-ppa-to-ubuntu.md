---
title: Adding the Cherokee Web Server PPA to Ubuntu
date: 2010-11-20
draft: false
slug: adding-the-cherokee-web-server-ppa-to-ubuntu
tags: ["general", "system administration", "ubuntu"]
description: Follow the commands in this post to add the Cherokee Web Server PPA to Ubuntu 9.10 or higher...
---

The following commands will add the Cherokee Web Server PPA to Ubuntu (version 9.10 and higher). The first command adds the extremely handy `add-apt-repository` program to your system. The second adds the Cherokee Personal Package Archive.


    ```bash
    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:cherokee-webserver/ppa
```


At the moment, Cherokee is at version 1.0.9.

If you don't already have Cherokee installed and you want to install it I find the following combination of packages most useful:


    ```bash
    sudo apt-get update
    sudo apt-get install cherokee cherokee-doc libcherokee-mod-libssl libcherokee-mod-streaming libcherokee-mod-rrd libcherokee-mod-admin spawn-fcgi
```

 
That's it. If you want more simple posts on building lean servers, cloud computing, software development and more, [subscribe to my RSS feed](http://www.cloudartisan.com/feed) and/or [follow me on Twitter](https://twitter.com/davidltaylor). Cheers!
