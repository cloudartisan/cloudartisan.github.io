---
title: "Python One-Liner: Debug Mail Server"
date: 2010-10-03
draft: false
slug: python-one-liner-debug-mail-server
tags: ["mail", "python", "software development", "system administration"]
description: I love a good Python one-liner...
---

Need a pretend mail server that you can use for debugging? Try this:


    ```bash
    python -m smtpd -n -c DebuggingServer localhost:1025
```


It listens on port 1025 for local connections.
