---
title: Google App Engine - unknown URL handler type
date: 2010-08-15
draft: false
slug: google-app-engine-unknown-url-handler-type
tags: ["google app engine", "paas", "python"]
description: Ugh!!!
---

```text
    Fatal error when loading application configuration:
    
    Invalid object:
    Unknown url handler type.
    <URLMap 
        secure=always 
        static_files=None 
        auth_fail_action=redirect 
        require_matching_file=None 
        static_dir=None 
        script=None 
        url=/admin/.* 
        upload=None 
        expiration=None 
        login=admin 
        mime_type=None
    >
    in "/home/david/Subversion/cloudzu/software/cloudzuum/src/app.yaml", line 37, column 1

 
This happens when you have an error in your `script:` definition in `app.yaml` or `script:` is missing entirely.

In my case, it was missing entirely... woops!
