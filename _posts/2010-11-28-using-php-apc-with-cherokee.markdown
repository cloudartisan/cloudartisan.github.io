public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['cherokee', 'general', 'php-apc', 'system administration', 'ubuntu']
published: 2010-11-28
title: Using PHP APC with Cherokee
slug: using-php-apc-with-cherokee

If you're using Cherokee as your web server, you're probably already interested in squeezing every drop of performance out of your server.  If you're hosting PHP sites with Cherokee, using APC (Alternative PHP Cache) could enable you to squeeze out even more drops.

> The Alternative PHP Cache (APC) is a free and open opcode cache for PHP. Its goal is to provide a free, open, and robust framework for caching and optimizing PHP intermediate code.

Before we get started with `php-apc` let's get a simple `phpinfo() page working.  This will enable us to check the installed PHP modules and other aspects of the PHP configuration.

Create the file

    :::bash
    # cat >/var/www/phpinfo.php <<EOF
    <?php
      phpinfo();
    ?>
    EOF
    # chown www-data.www-data /var/www/phpinfo.php
    # chmod 750 /var/www/phpinfo.php

Fire up `cherokee-admin`:

    :::bash
    # cherokee-admin -b
    Cherokee Web Server 1.0.10 (Nov 25 2010): Listening on port ALL:9090, TLS disabled, IPv6 enabled, using epoll, 4096 fds system limit, max. 2041 connections, caching I/O, 20 threads, 102 connections per thread, standard scheduling policy
    Login:
      User:              admin
      One-time Password: 5r1cxh4Bb2ZDLJc2a<br>Web Interface:
      URL:               http://localhost:9090/

Visit `http://your.server.address:9090 in your browser and login using the credentials provided by `cherokee-admin`.  We need to add a `Behaviour Rule` to the `Default vServer`.  Click `Next` then `Create`, then click on the `SAVE` button followed by `Graceful restart`.

Once that's done, visit `http://your.server.address/phpinfo.php` and look through the page for `APC Support`.  If you already have it installed, you can skip the next step.  Otherwise, let's install `php-apc`.


    # apt-get install php-apc
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following NEW packages will be installed:
      php-apc
    0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
    Need to get 77.2kB of archives.
    After this operation, 217kB of additional disk space will be used.
    Get:1 http://us.archive.ubuntu.com/ubuntu/ maverick/universe php-apc i386 3.1.3p1-2 [77.2kB]
    Fetched 77.2kB in 0s (95.6kB/s)
    Selecting previously deselected package php-apc.
    (Reading database ... 42954 files and directories currently installed.)
    Unpacking php-apc (from .../php-apc_3.1.3p1-2_i386.deb) ...
    Setting up php-apc (3.1.3p1-2) ...
    
After installing <code>php-apc</code> you'll have the following files installed:<br><blockquote># dpkg -L php-apc
/.
/usr
/usr/lib
/usr/lib/php5
/usr/lib/php5/20090626+lfs
/usr/lib/php5/20090626+lfs/apc.so
/usr/share
/usr/share/doc
/usr/share/doc/php-apc
/usr/share/doc/php-apc/TODO
/usr/share/doc/php-apc/README.Debian
/usr/share/doc/php-apc/copyright
/usr/share/doc/php-apc/changelog.gz
/usr/share/doc/php-apc/apc.php.gz
/usr/share/doc/php-apc/changelog.Debian.gz
/etc
/etc/php5
/etc/php5/conf.d
/etc/php5/conf.d/apc.ini</blockquote><br>In <code>/etc/php5/conf.d/apc.ini</code> you can see that the APC extension is enabled, but it is not yet configured:<br><blockquote># cat /etc/php5/conf.d/apc.ini
extension=apc.so</blockquote><br>The default settings might be fine for you.  This is really only something you can find out by monitoring your server, reading and understanding the various settings, and experimenting with changes.  To help with that, <code>php-apc</code> comes with <code>apc.php</code>, which provides detailed information about the APC opcode cache.<br><blockquote># zcat /usr/share/doc/php-apc/apc.php.gz > /var/www/apc.php
# chown www-data.www-data /var/www/apc.php
# chmod 750 /var/www/apc.php</blockquote><br>Next, we'll install <code>php5-gd</code> so we'll have some sexy graphics to help us understand what's happening in the cache.<br><blockquote># apt-get install php5-gd</blockquote><br>Once that's done, visit <em>http://your.server.address/apc.php</em> and you should see something like the following:<br><a href="/media/img/2010/11/APC-Opcode-Cache.png"><img src="/media/img/2010/11/APC-Opcode-Cache-300x171.png" alt="APC Opcode Cache" title="APC Opcode Cache" width="300" height="171" class="aligncenter size-medium wp-image-364" /></a><br>You'll need to run your site(s) with APC for a while before you have sufficient information to start tuning.  I suggest letting things tick along for a day or so, gathering statistics from typical usage, before you make any changes to the APC configuration.<br>In the meantime, I recommend disabling <code>phpinfo()</code> and <code>apc.php</code> until you're ready to tune your configuration.  To do this, click on the <em>Default vServer</em>, click on the <code>Behaviour</code> tab, then click on the <code>Rule Management</code> button.<br><a href="/media/img/2010/11/Default-Behaviour-Rules.png"><img src="/media/img/2010/11/Default-Behaviour-Rules-300x159.png" alt="Default Behaviour Rules" title="Default Behaviour Rules" width="300" height="159" class="aligncenter size-medium wp-image-365" /></a><br>Each of the rules has a green indicator next to them.  Click on the green indicator of the <code>Extensions php</code> rule that we added earlier.<br><a href="/media/img/2010/11/Behaviour-Rules-All-Enabled.png"><img src="/media/img/2010/11/Behaviour-Rules-All-Enabled-193x300.png" alt="Behaviour Rules All Enabled" title="Behaviour Rules All Enabled" width="193" height="300" class="aligncenter size-medium wp-image-366" /></a><br>Then click on the <code>SAVE</code> and <code>Graceful restart</code> buttons.  This will disable it.<br>When you're ready again to tune APC, click on the grey indicator of the <code>Extensions php</code> rule, then <code>SAVE</code> then <code>Graceful restart</code>.  This will enable it again.<br>If you want to force some basic load tests, make some configuration changes, rinse, repeat, you could do something like:<br><blockquote># apt-get install httperf
# httperf --hog --server=your.site.com --num-conns=1000 --rate=20 --timeout=5
httperf --hog --timeout=10 --client=0/1 --server=www.cloudartisan.com --port=80 --uri=/ --rate=20 --send-buffer=4096 --recv-buffer=16384 --num-conns=1000 --num-calls=1
Maximum connect burst length: 1<br>Total: connections 1000 requests 1000 replies 1000 test-duration 49.956 s<br>Connection rate: 20.0 conn/s (50.0 ms/conn, <=50 concurrent connections)
Connection time [ms]: min 5.1 avg 74.0 max 2624.2 median 5.5 stddev 332.8
Connection time [ms]: connect 0.0
Connection length [replies/conn]: 1.000<br>Request rate: 20.0 req/s (50.0 ms/req)
Request size [B]: 73.0<br>Reply rate [replies/s]: min 20.0 avg 20.0 max 20.0 stddev 0.0 (9 samples)
Reply time [ms]: response 73.5 transfer 0.5
Reply size [B]: header 508.0 content 42599.0 footer 2.0 (total 43109.0)
Reply status: 1xx=0 2xx=1000 3xx=0 4xx=0 5xx=0<br>CPU time [s]: user 15.17 system 34.78 (user 30.4% system 69.6% total 100.0%)
Net I/O: 844.1 KB/s (6.9*10^6 bps)<br>Errors: total 0 client-timo 0 socket-timo 0 connrefused 0 connreset 0
Errors: fd-unavail 0 addrunavail 0 ftab-full 0 other 0</blockquote><br>Make your configuration changes in <code>/etc/php5/conf.d/apc.ini</code>.  The setting you're most likely going to want to play with is <code>apc.shm_size</code>.  Be mindful of the amount of memory you have available.  Also, be sure to repeat the monitoring and tuning a few times.<br>There's more documentation on tuning <code>php-apc</code> at <a href="http://php.net/apc">http://php.net/apc</a>.
