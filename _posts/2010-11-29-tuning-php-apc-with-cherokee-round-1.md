public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['cherokee', 'general', 'php-apc', 'system administration', 'ubuntu']
published: 2010-11-29
title: Tuning PHP APC with Cherokee - Round 1
slug: tuning-php-apc-with-cherokee-round-1

Since writing [Using PHP APC with Cherokee](http://www.cloudartisan.com/2010/11/using-php-apc-with-cherokee/) I noticed that my cache hits were dropping and my cache misses were growing.  This is my first attempt at tweaking the configuration of `php-apc` to try to eke out more performance.

I enabled my `apc.php` page (check the previous article), checked the statistics, and saw that the `Cache full count` was growing. My cache had filled several times.

According to the [APC configuration documentation](http://www.php.net/manual/en/apc.configuration.php) there are two settings that control the expiration of cache entries. They are:

  * [`apc.ttl`](http://www.php.net/manual/en/apc.configuration.php#ini.apc.ttl)
  * [`apc.user_ttl`](http://www.php.net/manual/en/apc.configuration.php#ini.apc.user-ttl)
  
By default, they are set to `0`.

According to the documentation:

> In the event of a cache running out of available memory, the cache will be completely expunged if ttl is equal to 0. Otherwise, if the ttl is greater than 0, APC will attempt to remove expired entries.

  
Essentially, that meant my cache was completely expunged every time it filled and a new entry needed to be cached. Clearing the entire cache in order to store one more entry strikes me as less than optimal!

I'm surprised APC doesn't offer any smarts for managing a full or near-full cache (eg, using algorithms such as Least Recently Used or Second Chance Replacement to choose an entry to replace). The only option appears to be adjusting the cache expiry ([`apc.ttl`](http://www.php.net/manual/en/apc.configuration.php#ini.apc.ttl) and [`apc.user_ttl`](http://www.php.net/manual/en/apc.configuration.php#ini.apc.user-ttl)) or the size of the cache ([`apc.shm_segments`](http://www.php.net/manual/en/apc.configuration.php#ini.apc.shm-segments) and [`apc.shm_size`](http://www.php.net/manual/en/apc.configuration.php#ini.apc.shm-size)).

At this stage I didn't think it was a good idea to increase the memory used by `php-apc`. I'm on a Linode 512, a memory-constrained VPS. Also, by expiring infrequently-requested cache entries I might find that I can use _less_ memory for the cache instead of more.

So I added the following to `/etc/php5/cgi/conf.d/apc.ini`:


    :::ini
    # Does exactly what you think it does...
    apc.enabled=1
    # Number of seconds (7200 == 2h) before cache
    # entries are expired. Otherwise, the default (0)
    # means that the entire cache will be expunged
    # if/when the cache fills.
    apc.ttl = 7200
    apc.user_ttl = 7200


Of course, after making the changes there's still more to be done. I'm using Cherokee and FastCGI, so I need to restart the `php-cgi` processes for the change to take effect. I've found that `/etc/init.d/cherokee restart` doesn't take care of restarting the `php-cgi` processes. Nor does using the `Graceful restart` or `Hard restart` options in `cherokee-admin`. Instead, I _believe_ (again, please correct me if I'm wrong) that sending the `SIGTERM` to `php- cgi` means that the `php-cgi` processes will terminate when they have finished handling their current requests.


    :::bash
    killall -TERM php-cgi
    service cherokee start

  
After these changes:

  * if I find there is too much free memory in the cache and the cache misses are too high, I will increase the expiry times
  * if I find there is too much free memory but the cache hits are high (say, over 75%), I will probably decrease the size of the cache
  * if everything is just right, I'll leave things as they are
  
We'll find out in round 2...

In the meantime, [follow me on Twitter](http://twitter.com/davidltaylor). It's free. Cheers!
