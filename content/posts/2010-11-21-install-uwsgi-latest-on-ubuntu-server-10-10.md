---
title: Install uWSGI (latest) on Ubuntu Server 10.10
date: 2010-11-21
draft: false
slug: install-uwsgi-latest-on-ubuntu-server-10-10
tags: ["django", "general", "system administration", "uwsgi"]
description: uWSGI is a fast, self-healing, WSGI server. In this post I show how to install the latest version on Ubuntu Server 10.10...
---

uWSGI is a fast, self-healing, WSGI server. It is typically used with Python web applications. It works very well with the Cherokee Web Server and the Django web application framework.

To install the latest uWSGI use `pip` and the URL for the latest version of uWSGI:


    ```bash
    sudo apt-get install libxml2-dev build-essential python-dev python-pip
    sudo pip install http://projects.unbit.it/downloads/uwsgi-latest.tar.gz
```


Simple as that.

You should [follow me on Twitter](https://twitter.com/davidltaylor).
