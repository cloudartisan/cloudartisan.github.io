public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['google app engine', 'paas', 'python']
published: 2010-06-02
title: Scheduled Tasks With Google App Engine & Python
slug: scheduled-tasks-with-google-app-engine-python
summary: Create a simple application that sends an e-mail every 5 minutes...

We'll create a simple Hello World application that sends an e-mail every 5 minutes to reassure you that the Internet is still out there and still cares.

First, download and install the [Google App Engine SDK](http://code.google.com/appengine/downloads.html).

For example:


    :::bash
    wget http://googleappengine.googlecode.com/files/google_appengine_1.3.4.zip
    unzip google_appengine_1.3.4.zip


Create a directory for your application:

    :::bash
    mkdir helloworld

Create an app.yaml file to describe your application:

    :::yaml
    application: helloworld
    version: 1
    runtime: python
    api_version: 1handlers:
    - url: /helloworld
      script: helloworld.py
      login: admin

Create a cron.yaml file to run your scheduled task:

    :::yaml
    cron:
    - description: hello... is it me you're looking for?
      url: /helloworld
      schedule: every 5 minutes

Create your script (changing the e-mail addresses, of course):

    :::python
    #!/usr/bin/env python
    #
    # Hello World via e-mail
    
    from google.appengine.api import mail

    mail.send_mail(
        sender="Your Email Address <you@example.com>",
        to="Your Email Address <you@example.com >",
        subject="Hello world",
        body="Hello world"
    )

Use appcfg.py inside the unzipped SDK to upload your application:

    :::bash
    google_appengine/appcfg.py update helloworld

Enter your username and password when prompted.  The output should look something like this:


    :::text
    Application: helloworld; version: 1.
    Server: appengine.google.com.
    Scanning files on local disk.
    Initiating update.
    Cloning 2 application files.
    Uploading 1 files and blobs.
    Uploaded 1 files and blobs
    Deploying new version.
    Checking if new version is ready to serve.
    Will check again in 1 seconds.
    Checking if new version is ready to serve.
    Will check again in 2 seconds.
    Checking if new version is ready to serve.
    Closing update: new version is ready to start serving.
    Uploading cron entries.


Simple as that.  Enjoy.
