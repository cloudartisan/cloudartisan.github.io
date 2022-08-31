public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['rails', 'ruby', 'rvm', 'software development', 'ubuntu']
published: 2010-12-10
title: Install Ruby 1.9.2 and Rails 3.0.3 using rvm on Ubuntu 10.10
slug: install-ruby-1-9-rails-3-using-rvm-on-ubuntu-10-10

It's terse, probably more for my benefit than yours, but let's dive in...

Install the packages required by `rvm`:

    :::text
    david@continuity:~$ sudo apt-get install curl git

Install `rvm`:

    :::text
    david@continuity:~$ bash < <( curl http://rvm.beginrescueend.com/releases/rvm-install-head )
    % Total % Received % Xferd Average Speed Time Time Time Current Dload Upload Total Spent Left Speed
    100 986 100 986 0 0 524 0 0:00:01 0:00:01 --:--:-- 4522
    Initialized empty Git repository in /home/david/.rvm/src/rvm/.git/
    remote: Counting objects: 16240, done.
    remote: Compressing objects: 100% (4166/4166), done.
    remote: Total 16240 (delta 10951), reused 15861 (delta 10649)
    Receiving objects: 100% (16240/16240), 2.91 MiB | 457 KiB/s, done.
    Resolving deltas: 100% (10951/10951), done.
    
    RVM: Shell scripts enabling management of multiple ruby environments.
    RTFM: http://rvm.beginrescueend.com/
    HELP: http://webchat.freenode.net/?channels=rvm (#rvm on irc.freenode.net)
    
    Installing RVM to /home/david/.rvm/
    Correct permissions for base binaries in /home/david/.rvm/bin...
    Copying manpages into place.

Backup and update your `.bashrc` to make sure `rvm` is ready whenever you fire up a terminal:

    :::text
    david@continuity:~$ cp -v ~/.bashrc ~/.bashrc-`date '+%s'`
    /home/david/.bashrc -> /home/david/.bashrc-1291952792
    david@continuity:~$ cat <<~/.bashrc >>EOF
    > # This loads RVM into a shell session
    > [[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
    > EOF
    david@continuity:~$

Load `rvm` into the current shell session:

    :::text
    david@continuity:~$ source ~/.rvm/scripts/rvm

Now, for installing Ruby 1.9.2, we can check the requirements using `rvm notes`:

    :::text
    david@continuity:~$ rvm notes | grep "^[ \t]*ruby:"
    ruby: aptitude install build-essential bison openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf
    david@continuity:~$ `

Install those packages:

    :::text
    david@continuity:~$ sudo apt-get install build-essential bison openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf
    [sudo] password for david: . . . `

Now install Ruby 1.9.2:

    :::text
    david@continuity:~$ rvm install 1.9.2
    /home/david/.rvm/rubies/ruby-1.9.2-p0, this may take a while depending on your cpu(s)...

Now make Ruby 1.9.2 your default:

    :::text
    david@continuity:~$ rvm use 1.9.2 --default Using
    /home/david/.rvm/gems/ruby-1.9.2-p0
    david@continuity:~$ 

Install the Rails gem:

    :::text
    david@continuity:~$ gem install rails

So that's it, we now have Ruby 1.9.2 and Rails 3.0.3. To verify this:

    :::text
    david@continuity:~$ ruby -v
    ruby 1.9.2p0 (2010-08-18 revision 29036) [x86_64-linux]
    david@continuity:~$ rails -v
    Rails 3.0.3

_Note: of course, this only applies to your user account. These changes do not apply system-wide and do not affect other users._

[Follow me on twitter](http://twitter.com/davidltaylor). It's free!

Cheers.
