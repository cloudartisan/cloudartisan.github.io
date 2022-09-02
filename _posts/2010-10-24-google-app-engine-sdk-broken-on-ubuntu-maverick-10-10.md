public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['google app engine', 'paas', 'python']
published: 2010-10-24
title: Google App Engine SDK broken on Ubuntu Maverick 10.10
slug: google-app-engine-sdk-broken-on-ubuntu-maverick-10-10
summary: The Google App Engine SDK is broken on Ubuntu 10.10, but it's easy enough to fix...

The Google App Engine SDK is broken on Ubuntu 10.10, but it's easy enough to fix...

The Google App Engine SDK requires Python 2.5. It does not work with Python 2.6.

This problem is covered in these Google Code issues:

  * [http://code.google.com/p/googleappengine/issues/detail?id=1159](http://code.google.com/p/googleappengine/issues/detail?id=1159)
  * [http://code.google.com/p/googleappengine/issues/detail?id=757](http://code.google.com/p/googleappengine/issues/detail?id=757)
  
If you try to use Google App Engine SDK on Python 2.6 you will encounter tracebacks like the following:

    :::text
    Traceback (most recent call last):
      File "/home/david/lib/google_appengine/google/appengine/tools/dev_appserver.py", line 3211, in _HandleRequest
        self._Dispatch(dispatcher, self.rfile, outfile, env_dict)
      File "/home/david/lib/google_appengine/google/appengine/tools/dev_appserver.py", line 3154, in _Dispatch
        base_env_dict=env_dict)
      File "/home/david/lib/google_appengine/google/appengine/tools/dev_appserver.py", line 527, in Dispatch
        base_env_dict=base_env_dict)
      File "/home/david/lib/google_appengine/google/appengine/tools/dev_appserver.py", line 2452, in Dispatch
        CGIDispatcher.Dispatch(self, *args, **kwargs)
      File "/home/david/lib/google_appengine/google/appengine/tools/dev_appserver.py", line 2404, in Dispatch
        self._module_dict)
      File "/home/david/lib/google_appengine/google/appengine/tools/dev_appserver.py", line 2441, in curried_exec_cgi
        return ExecuteCGI(*args, **kwargs)
      File "/home/david/lib/google_appengine/google/appengine/tools/dev_appserver.py", line 2312, in ExecuteCGI
        logging.debug('Executing CGI with env: %s', pprint.pformat(env))
      File "/usr/lib/python2.6/pprint.py", line 60, in pformat
        return PrettyPrinter(indent=indent, width=width, depth=depth).pformat(object)
      File "/usr/lib/python2.6/pprint.py", line 119, in pformat
        self._format(object, sio, 0, 0, {}, 0)
      File "/usr/lib/python2.6/pprint.py", line 137, in _format
        rep = self._repr(object, context, level - 1)
      File "/usr/lib/python2.6/pprint.py", line 230, in _repr
        self._depth, level)
      File "/usr/lib/python2.6/pprint.py", line 242, in format
        return _safe_repr(object, context, maxlevels, level)
      File "/usr/lib/python2.6/pprint.py", line 284, in _safe_repr
        for k, v in _sorted(object.items()):
      File "/usr/lib/python2.6/pprint.py", line 75, in _sorted
        with warnings.catch_warnings():
      File "/usr/lib/python2.6/warnings.py", line 333, in __init__
        self._module = sys.modules['warnings'] if module is None else module
      KeyError: 'warnings'

... which is a pain in the proverbial to debug.

Ubuntu Maverick 10.10 (and some earlier releases of Ubuntu) uses Python 2.6 by default. In older versions of Ubuntu the fix involved installing the older Python 2.5 from the official repository. However, with Ubuntu Maverick 10.10 things are worse... Python 2.5 is no longer available from an official repository!

Thankfully, there is a repository on Launchpad that contains the necessary packages. To install, do the following:


    :::bash
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python2.5


Next, modify `dev_appserver.py` in the Google App Engine SDK. Change the first line from:


    :::bash
    #!/usr/bin/env python

  
to:


    :::bash
    #!/usr/bin/env python2.5


Simple. Done. Restart your `dev_appserver.py` and everything should work A-OK.

[Follow me on twitter](http://twitter.com/davidltaylor).
