public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['general', 'spawn-fcgi', 'system administration']
published: 2010-10-04
title: Cherokee failing to exec spawn-fcgi
slug: cherokee-failin-to-exec-spawn-fcgi
summary: Ugh!!!

If you're using `spawn-fcgi` with Cherokee (probably to get a wiki or PHP application or similar working) and you see:

    503 Service Unavailable

... you might be having the same problem I had. That is, Cherokee was failing to launch `spawn-fcgi`.

To verify this is the cause of your problem, stop Cherokee, then start it manually at the command line:


    # /usr/sbin/cherokee --admin_child -C /etc/cherokee/cherokee.conf
    Cherokee Web Server 1.0.8 (Aug 18 2010): Listening on port ALL:80, TLS disabled, IPv6 enabled, using epoll, 4096 fds system limit, max. 2041 connections, caching I/O, 20 threads, 102 connections per thread, standard scheduling policy


Next, try to visit the site giving you the problem. If you see the following in your terminal then you've probably got the same problem I had:


    PID 22960: launched '/bin/sh -c exec /usr/bin/spawn-fcgi -n -a 127.0.0.1 -p 53993 -- /usr/share/moin/server/moin.fcg' with uid=33, gid=33, env=inherited
    PID 22960: exited re=1
    PID 22961: launched '/bin/sh -c exec /usr/bin/spawn-fcgi -n -a 127.0.0.1 -p 53993 -- /usr/share/moin/server/moin.fcg' with uid=33, gid=33, env=inherited
    PID 22961: exited re=1
    PID 22962: launched '/bin/sh -c exec /usr/bin/spawn-fcgi -n -a 127.0.0.1 -p 53993 -- /usr/share/moin/server/moin.fcg' with uid=33, gid=33, env=inherited
    PID 22962: exited re=1


That's Cherokee trying _and failing_ to launch `spawn-fcgi`.

In my case, I had no idea _why_ it was failing, but I found that when I enabled error logging for that vServer then `spawn-fcgi` would magically start to work. Go figure.

This should do it...

[caption id="attachment_244" align="aligncenter" width="654" caption="Cherokee Error Logging"][![Cherokee Error Logging](/media/img/2010/10/Cherokee-Error-Logging.png)](/media/img/2010/10/Cherokee-Error-Logging.png)[/caption]

You should [follow me on twitter](http://twitter.com/davidltaylor).
