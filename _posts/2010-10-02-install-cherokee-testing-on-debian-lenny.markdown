public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['debian', 'general', 'lenny', 'system administration']
published: 2010-10-02
title: Install Cherokee (testing) on Debian Lenny
slug: install-cherokee-testing-on-debian-lenny
summary: How to install Cherokee (testing) on Debian Lenny...

Add the following to `/etc/sources`:


    :::text
    deb http://ftp.us.debian.org/debian/ testing main contrib non-free


Create `/etc/apt/apt.conf` with:


    :::text
    APT::Default-Release "stable";


Create `/etc/apt/preferences` for pinning the testing packages:


    :::text
    Package: libssl-dev
    Pin: release a=testing
    Pin-Priority: 999  
    Package: libssl0.9.8
    Pin: release a=testing
    Pin-Priority: 999  
    Package: libcherokee-base0
    Pin: release a=testing
    Pin-Priority: 999  
    Package: mysql-common
    Pin: release a=testing
    Pin-Priority: 999  
    Package: libmysqlclient16
    Pin: release a=testing
    Pin-Priority: 999  
    Package: libcherokee-server0
    Pin: release a=testing
    Pin-Priority: 999  
    Package: libcherokee-config0
    Pin: release a=testing
    Pin-Priority: 999  
    Package: libcherokee-mod-admin
    Pin: release a=testing
    Pin-Priority: 999  
    Package: cherokee
    Pin: release a=testing
    Pin-Priority: 999  
    Package: *
    Pin: release a=stable
    Pin-Priority: 500


Then install the packages:


    :::bash
    apt-get install -t testing cherokee libcherokee-base0 libcherokee-server0 libcherokee-config0 libcherokee-mod-admin libssl0.9.8


That's the installation. For the configuration, check out the [Cherokee cookbooks](http://www.cherokee-project.com/doc/cookbook.html).
