---
title: Install uWSGI (latest) on Debian Lenny
date: 2010-10-04
draft: false
slug: install-uwsgi-latest-on-debian-lenny
tags: ["general", "python", "software development", "system administration", "uwsgi"]
description: uWSGI is a fast, self-healing, WSGI server.  Follow these instructions to install it on Debian Lenny...
---

First, why would you want it? uWSGI is a fast, self-healing, WSGI server, originally intended for use with Python web applications. I intend to use it with Python Django, served by Cherokee.

As for installation...

Do not bother doing a hands-on install from source. It's messy. Just use `pip`:


    ```bash
    apt-get install gcc python-dev libxml2-dev
    apt-get install python-pip
    pip install http://projects.unbit.it/downloads/uwsgi-latest.tar.gz
```


Simple as that.

You should [follow me on twitter](https://twitter.com/davidltaylor).
