public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['mail', 'python', 'software development', 'system administration']
published: 2010-10-03
title: "Python One-Liner: Debug Mail Server"
slug: python-one-liner-debug-mail-server
summary: I love a good Python one-liner...

Need a pretend mail server that you can use for debugging? Try this:


    :::bash
    python -m smtpd -n -c DebuggingServer localhost:1025


It listens on port 1025 for local connections.
