public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['software development', 'system administration']
published: 2011-03-07
title: Installing newrelic_api gem from GitHub
slug: installing-newrelic_api-gem-from-github

I needed to correlate some logs with New Relic monitoring data. I started doing this manually... and got bored very quickly. It was too slow and painstaking. After some poking around I came across [newrelic_api](https://github.com/newrelic/newrelic_api) (not to be confused with [rpm](https://github.com/newrelic/rpm), which is the monitoring agent).

Next thing I discovered... I had no idea how to install gems from GitHub!

No longer!

    :::text
    wintermute:~/Git $ mkdir newrelic
    wintermute:~/Git $ cd newrelic/
    wintermute:~/Git/newrelic $ git clone git://github.com/newrelic/newrelic_api.git
    Cloning into newrelic_api...
    remote: Counting objects: 132, done.
    remote: Compressing objects: 100% (116/116), done.
    remote: Total 132 (delta 59), reused 0 (delta 0) Receiving objects: 100% (132/132), 26.02 KiB, done.
    Resolving deltas: 100% (59/59), done.
    wintermute:~/Git/newrelic $ cd newrelic_api/
    wintermute:~/Git/newrelic/newrelic_api (master)$ ls
    CHANGELOG Gemfile.lock README.rdoc VERSION log test Gemfile LICENSE.txt Rakefile lib newrelic_api.gemspec
    wintermute:~/Git/newrelic/newrelic_api (master)$ gem build newrelic_api.gemspec
    Successfully built RubyGem
    Name: newrelic_api
    Version: 1.1.1
    File: newrelic_api-1.1.1.gem
    wintermute:~/Git/newrelic/newrelic_api (master)$ gem install newrelic_api-1.1.1.gem
    Successfully installed newrelic_api-1.1.1
    1 gem installed
    Installing ri documentation for newrelic_api-1.1.1...
    Installing RDoc documentation for newrelic_api-1.1.1...
    wintermute:~/Git/newrelic/newrelic_api (master)$

It's as simple as that.

Follow me on [twitter](http://twitter.com/davidltaylor).
